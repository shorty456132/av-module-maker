"""Integration tests for the raw loop itself (scripts/ralph/ralph-module-loop.sh).

This is the loop's first test. Until P5 the shell was covered only by the engine
tests underneath it, so its own contract — one pass per card, the exit codes a
caller branches on, the `.ralph/` run state a watcher polls — was unverified.

No LLM is involved: a stub `claude` is placed first on `PATH`. It emits the same
`--output-format stream-json` NDJSON the real CLI does and advances the board via
`board.py`, which is exactly what a real pass does. That makes the loop's
plumbing — argument passing, the render pipe, `${PIPESTATUS[0]}`, the status
writes, the STOP check and every exit code — testable in milliseconds.

Skipped when `bash` is unavailable.
"""

import json
import os
import shutil
import subprocess
import sys

import pytest

RALPH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOOP = os.path.join(RALPH, "ralph-module-loop.sh")


def _bash():
    """Git Bash by preference: on Windows a bare `bash` can resolve to a WSL
    bash with no view of the repo (the same trap the loop's own usage note
    warns about)."""
    for candidate in (r"C:\Program Files\Git\bin\bash.exe",
                      r"C:\Program Files (x86)\Git\bin\bash.exe"):
        if os.path.exists(candidate):
            return candidate
    return shutil.which("bash")


BASH = _bash()
pytestmark = pytest.mark.skipif(BASH is None, reason="bash unavailable")


BOARD = """\
# TODO — Stub Plugin (qsys)

_Last updated: 2026-09-01_
_Status: in-progress_
_Plan: frozen_

**Module dir:** ./Stub-Plugin/
**Verify gate:** true

## 📋 Next Up
- [ ] **info.lua** — PluginInfo table.
  - Spec: stub.
  - Verify: exists.
- [ ] **compile** — Run the verify gate.
  - Spec: stub.
  - Depends: info.lua
  - Verify: exit 0.

## 🔄 In Progress

## ✅ Done

## 🚫 Blocked
"""

# A stub `claude`: emits the stream-json event shapes the renderer parses, then
# advances exactly one card — the same contract module-loop-prompt.md gives a
# real pass. `$MODULE_DIR`/`$BOARD_PY` are baked in when the stub is written.
STUB = """\
#!/usr/bin/env bash
echo '{{"type":"system","subtype":"init","session_id":"stub1234-0000","model":"stub-model"}}'
title="$(python "{board}" next "{dir}")"
if [ "$title" != "NONE" ]; then
  echo "{{\\"type\\":\\"assistant\\",\\"message\\":{{\\"content\\":[{{\\"type\\":\\"tool_use\\",\\"name\\":\\"Edit\\",\\"input\\":{{\\"file_path\\":\\"$title\\"}}}}]}}}}"
  python "{board}" start "{dir}" "$title" >/dev/null
  {work}
fi
echo '{{"type":"result","subtype":"success","is_error":false,"duration_ms":1200,"num_turns":3,"total_cost_usd":0.01,"usage":{{"input_tokens":100,"output_tokens":50,"cache_read_input_tokens":900,"cache_creation_input_tokens":10}}}}'
"""

WORK_DONE = 'python "{board}" done "{dir}" "$title" >/dev/null'
WORK_NOTHING = ':'   # starts the card but never finishes it -> convergence guard


def make_module(tmp_path, board_text=BOARD):
    d = tmp_path / "Stub-Plugin"
    d.mkdir()
    (d / "TODO.md").write_text(board_text, encoding="utf-8")
    return d


def install_stub(tmp_path, module_dir, work=WORK_DONE):
    bin_dir = tmp_path / "stubbin"
    bin_dir.mkdir()
    board_py = os.path.join(RALPH, "board.py").replace("\\", "/")
    mod = str(module_dir).replace("\\", "/")
    script = STUB.format(board=board_py, dir=mod,
                         work=work.format(board=board_py, dir=mod))
    stub = bin_dir / "claude"
    stub.write_text(script, encoding="utf-8", newline="\n")
    os.chmod(stub, 0o755)
    return bin_dir


def _shell_utils_dir():
    """Git Bash's /usr/bin, alongside the bash we run. pytest inherits a bare
    Windows PATH, but the loop is documented to run *from* Git Bash, where these
    utilities (`kill`, `timeout`, `tee`) are always present. Without them the
    loop degrades safely rather than failing loudly, which would quietly hollow
    out these tests."""
    if BASH and BASH.lower().endswith(".exe"):
        candidate = os.path.join(os.path.dirname(os.path.dirname(BASH)), "usr", "bin")
        if os.path.isdir(candidate):
            return candidate
    return None


def run_loop(tmp_path, module_dir, bin_dir, max_passes=6, env_extra=None):
    env = dict(os.environ)
    path_parts = [str(bin_dir)]
    utils = _shell_utils_dir()
    if utils:
        path_parts.append(utils)
    env["PATH"] = os.pathsep.join(path_parts + [env["PATH"]])
    env.update(env_extra or {})
    return subprocess.run(
        [BASH, LOOP.replace("\\", "/"), str(module_dir), str(max_passes)],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        env=env, timeout=180)


# --- the happy path -------------------------------------------------------

def test_loop_drains_the_board_and_exits_zero(tmp_path):
    module_dir = make_module(tmp_path)
    proc = run_loop(tmp_path, module_dir, install_stub(tmp_path, module_dir))
    assert proc.returncode == 0, proc.stdout + proc.stderr
    # Two cards, one per pass — never two in a pass.
    assert "pass 2" in proc.stdout
    assert "pass 3" not in proc.stdout


def test_loop_names_the_card_before_working_it(tmp_path):
    # The old loop printed a bare pass banner: you could not tell *what* it was
    # building, or how far along it was, until it finished.
    module_dir = make_module(tmp_path)
    proc = run_loop(tmp_path, module_dir, install_stub(tmp_path, module_dir))
    assert "info.lua" in proc.stdout
    assert "compile" in proc.stdout


def test_loop_streams_tool_lines_during_a_pass(tmp_path):
    module_dir = make_module(tmp_path)
    proc = run_loop(tmp_path, module_dir, install_stub(tmp_path, module_dir))
    assert "🔧 Edit" in proc.stdout          # rendered mid-pass, not at the end
    assert "pass complete" in proc.stdout    # the per-pass cost/token line


def test_loop_writes_run_state_log_and_report(tmp_path):
    module_dir = make_module(tmp_path)
    run_loop(tmp_path, module_dir, install_stub(tmp_path, module_dir))
    ralph = module_dir / ".ralph"
    assert (ralph / "run.log").exists()
    assert (ralph / "REPORT.md").exists()
    data = json.loads((ralph / "status.json").read_text(encoding="utf-8"))
    assert data["schema"] == 1
    assert data["exit_code"] == 0
    assert data["board"]["status"] == "done"
    assert data["pass"] == 2
    # Usage accumulated across both passes, from the stream's result events.
    assert data["cost_usd"] == pytest.approx(0.02)
    assert data["input_tokens"] == 200


def test_loop_writes_a_raw_stream_log_per_pass(tmp_path):
    module_dir = make_module(tmp_path)
    run_loop(tmp_path, module_dir, install_stub(tmp_path, module_dir))
    logs = sorted((module_dir / ".ralph" / "logs").glob("pass-*.jsonl"))
    assert [p.name for p in logs] == ["pass-01.jsonl", "pass-02.jsonl"]
    first = logs[0].read_text(encoding="utf-8")
    assert json.loads(first.splitlines()[0])["type"] == "system"


def test_status_show_reads_the_finished_run(tmp_path):
    # The point of the run state: a second terminal (or the session that
    # launched the run) can ask what happened without touching the loop.
    module_dir = make_module(tmp_path)
    run_loop(tmp_path, module_dir, install_stub(tmp_path, module_dir))
    proc = subprocess.run(
        [sys.executable, os.path.join(RALPH, "status.py"), "show", str(module_dir)],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    assert proc.returncode == 0
    assert "exit 0" in proc.stdout


# --- the exit-code contract -----------------------------------------------

def test_missing_todo_exits_2(tmp_path):
    empty = tmp_path / "Empty"
    empty.mkdir()
    proc = run_loop(tmp_path, empty, install_stub(tmp_path, empty))
    assert proc.returncode == 2


def test_planted_stop_file_halts_with_exit_5(tmp_path):
    module_dir = make_module(tmp_path)
    ralph = module_dir / ".ralph"
    ralph.mkdir()
    (ralph / "STOP").write_text("", encoding="utf-8")
    proc = run_loop(tmp_path, module_dir, install_stub(tmp_path, module_dir))
    assert proc.returncode == 5, proc.stdout + proc.stderr
    # It stopped *before* burning a pass.
    assert (module_dir / "TODO.md").read_text(encoding="utf-8").count("- [x]") == 0


def test_blocked_board_halts_with_exit_3(tmp_path):
    module_dir = make_module(tmp_path)
    board_py = os.path.join(RALPH, "board.py")
    bin_dir = install_stub(
        tmp_path, module_dir,
        work='python "{board}" block "{dir}" "$title" "needs-new-card: no spec" >/dev/null')
    proc = run_loop(tmp_path, module_dir, bin_dir)
    assert proc.returncode == 3, proc.stdout + proc.stderr
    data = json.loads((module_dir / ".ralph" / "status.json").read_text(encoding="utf-8"))
    assert data["board"]["blocked"][0]["reason"] == "needs-new-card: no spec"
    assert board_py  # (path resolved above is the one the stub was built with)


def test_non_converging_loop_halts_with_exit_4(tmp_path):
    # A pass that starts a card but never finishes it: `remaining` never drops.
    module_dir = make_module(tmp_path)
    bin_dir = install_stub(tmp_path, module_dir, work=WORK_NOTHING)
    proc = run_loop(tmp_path, module_dir, bin_dir, max_passes=10)
    assert proc.returncode == 4, proc.stdout + proc.stderr


def test_hitting_max_passes_exits_1(tmp_path):
    module_dir = make_module(tmp_path)
    bin_dir = install_stub(tmp_path, module_dir, work=WORK_NOTHING)
    # STALL_MAX high enough that MAX is the binding limit, not the stall guard.
    proc = run_loop(tmp_path, module_dir, bin_dir, max_passes=2,
                    env_extra={"STALL_MAX": "99"})
    assert proc.returncode == 1, proc.stdout + proc.stderr


def test_every_terminal_path_leaves_a_report(tmp_path):
    module_dir = make_module(tmp_path)
    bin_dir = install_stub(tmp_path, module_dir, work=WORK_NOTHING)
    proc = run_loop(tmp_path, module_dir, bin_dir, max_passes=10)
    report = module_dir / ".ralph" / "REPORT.md"
    assert report.exists()
    assert "not converging" in report.read_text(encoding="utf-8").lower()
    assert str(report).replace("\\", "/") in proc.stdout.replace("\\", "/") \
        or "REPORT.md" in proc.stdout


def test_stop_planted_mid_pass_kills_the_child(tmp_path):
    # The end-to-end STOP path: the renderer sits downstream of `claude` in the
    # pipe and cannot see it, so the loop parks the child's PID in a file and the
    # renderer SIGTERMs it. Without this the only way to stop a wedged overnight
    # run would be hunting a PID in Task Manager.
    import threading
    import time

    module_dir = make_module(tmp_path)
    # Models a real `claude`: long-running, and it terminates on SIGTERM. (A
    # naive `sleep 20` would not — bash leaves a foreground child running and
    # the orphan holds the pipe open, which would hide a kill that never landed.)
    slow = ("trap 'kill $sp 2>/dev/null; exit 143' TERM; sleep 25 & sp=$!; "
            'wait $sp; python "{board}" done "{dir}" "$title" >/dev/null')
    bin_dir = install_stub(tmp_path, module_dir, work=slow)

    stop_file = module_dir / ".ralph" / "STOP"

    def plant():
        # Wait for the pass to be underway (the loop creates .ralph/ up front).
        deadline = time.time() + 30
        while time.time() < deadline and not (module_dir / ".ralph" / "child.pid").exists():
            time.sleep(0.2)
        time.sleep(1.0)
        stop_file.write_text("", encoding="utf-8")

    planter = threading.Thread(target=plant)
    planter.start()
    started = time.time()
    proc = run_loop(tmp_path, module_dir, bin_dir)
    elapsed = time.time() - started
    planter.join()

    assert proc.returncode == 5, proc.stdout + proc.stderr
    # The load-bearing assertion: it came back well before the stub's 25s of
    # work, so the child was killed mid-pass rather than waited out.
    assert elapsed < 20, "took {0:.0f}s — STOP did not kill the pass".format(elapsed)
    assert "STOP" in proc.stdout
    assert (module_dir / ".ralph" / "REPORT.md").exists()
    # The card never completed, so the board still shows it unfinished.
    assert "- [x]" not in (module_dir / "TODO.md").read_text(encoding="utf-8")
