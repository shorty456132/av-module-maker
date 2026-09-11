"""Unit tests for the per-pass stream renderer (scripts/ralph/render_pass.py).

Without this, a pass is a multi-minute silence followed by a wall of text: with
no `--output-format`, `claude -p` buffers everything to the end. The renderer
consumes `--output-format stream-json` line by line and prints one short line
per event, so a watching human sees tool calls *as they happen* and the loop can
bank the pass's real token/cost numbers.

Two properties are load-bearing:

1. **It never raises.** It sits in the middle of a pipe carrying model output —
   a malformed line, a truncated event, or an event type that did not exist when
   this was written must render nothing and keep going. A traceback here would
   break a pipe mid-pass and lose the run.
2. **Usage comes from the `result` event**, not from guesswork, so the run total
   in status.json is the API's own accounting.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import render_pass as rp  # noqa: E402


# --- fixtures: the event shapes `claude -p --output-format stream-json` emits --

INIT = {"type": "system", "subtype": "init",
        "session_id": "3f2ab8c1-dead-4beef-9999-000000000001",
        "model": "claude-opus-5", "tools": ["Read", "Edit", "Bash"]}

ASSISTANT_TEXT = {"type": "assistant", "message": {"content": [
    {"type": "text", "text": "Writing controls.lua for the Setup page."}]}}

TOOL_USE = {"type": "assistant", "message": {"content": [
    {"type": "tool_use", "name": "Edit",
     "input": {"file_path": "/tmp/My-Plugin/controls.lua", "old_string": "a"}}]}}

TOOL_USE_BASH = {"type": "assistant", "message": {"content": [
    {"type": "tool_use", "name": "Bash",
     "input": {"command": "python compile.py ./My-Plugin/"}}]}}

TOOL_RESULT_ERROR = {"type": "user", "message": {"content": [
    {"type": "tool_result", "is_error": True,
     "content": "compile.py: layout.lua: undefined control 'Connect'"}]}}

TOOL_RESULT_OK = {"type": "user", "message": {"content": [
    {"type": "tool_result", "is_error": False, "content": "ok"}]}}

RESULT = {"type": "result", "subtype": "success", "is_error": False,
          "duration_ms": 42000, "num_turns": 7, "total_cost_usd": 0.1234,
          "usage": {"input_tokens": 1203, "output_tokens": 8109,
                    "cache_read_input_tokens": 41000,
                    "cache_creation_input_tokens": 2500}}


# --- render_event ---------------------------------------------------------

def test_init_event_names_the_session_and_model():
    lines = rp.render_event(INIT)
    joined = " ".join(lines)
    assert "claude-opus-5" in joined
    assert "3f2ab8c1" in joined          # short session id, enough to correlate


def test_tool_use_renders_name_and_target():
    line = " ".join(rp.render_event(TOOL_USE))
    assert "Edit" in line
    assert "controls.lua" in line        # the target, not the whole input blob
    assert "old_string" not in line      # never dump the payload


def test_bash_tool_use_shows_the_command():
    line = " ".join(rp.render_event(TOOL_USE_BASH))
    assert "Bash" in line and "compile.py" in line


def test_assistant_text_renders_as_one_short_line():
    lines = rp.render_event(ASSISTANT_TEXT)
    assert len(lines) == 1
    assert "controls.lua" in lines[0]
    assert "\n" not in lines[0]


def test_long_assistant_text_is_truncated():
    long = {"type": "assistant", "message": {"content": [
        {"type": "text", "text": "x" * 5000}]}}
    line = rp.render_event(long)[0]
    assert len(line) < 300


def test_tool_result_error_is_surfaced():
    line = " ".join(rp.render_event(TOOL_RESULT_ERROR))
    assert "undefined control" in line


def test_successful_tool_result_is_quiet():
    # Only failures are worth a line; echoing every success buries the signal.
    assert rp.render_event(TOOL_RESULT_OK) == []


def test_result_event_renders_turns_duration_and_cost():
    line = " ".join(rp.render_event(RESULT))
    assert "0.12" in line                # cost
    assert "7" in line                   # turns
    assert "1,203" in line or "1203" in line


# --- resilience -----------------------------------------------------------

def test_unknown_event_type_renders_nothing():
    assert rp.render_event({"type": "something_new_in_a_later_cli"}) == []


def test_malformed_events_never_raise():
    for junk in ({}, {"type": "assistant"}, {"type": "assistant", "message": None},
                 {"type": "assistant", "message": {"content": "not-a-list"}},
                 {"type": "result", "usage": "nope"}, [], None, "string"):
        assert rp.render_event(junk) == [] or isinstance(rp.render_event(junk), list)


def test_parse_line_returns_none_on_malformed_json():
    assert rp.parse_line("{ not json") is None
    assert rp.parse_line("") is None
    assert rp.parse_line('{"type":"result"}') == {"type": "result"}


# --- usage extraction -----------------------------------------------------

def test_usage_from_result_maps_to_the_status_schema():
    u = rp.usage_from_result(RESULT)
    # `+`-keys accumulate into the run total; `last_context_tokens` is set (no
    # `+`) because it is the *current* window size, not a sum — it drives session
    # rotation, so it must reflect this pass alone.
    assert u == {"+cost_usd": 0.1234, "+input_tokens": 1203, "+output_tokens": 8109,
                 "+cache_read_tokens": 41000, "+cache_creation_tokens": 2500,
                 "last_context_tokens": 1203 + 41000 + 2500}


def test_last_context_tokens_is_the_window_size_and_set_not_accumulated():
    # The rotation signal: input + cache-read + cache-creation ≈ how full the
    # context window is on this pass. It is written without a `+` so a later pass
    # overwrites it rather than summing — a running total would never match the
    # window and would trip rotation far too early.
    u = rp.usage_from_result(RESULT)
    assert u["last_context_tokens"] == 44703
    assert "+last_context_tokens" not in u


def test_usage_from_non_result_event_is_none():
    assert rp.usage_from_result(TOOL_USE) is None


def test_usage_from_result_missing_usage_block_still_reports_cost():
    u = rp.usage_from_result({"type": "result", "total_cost_usd": 0.5})
    assert u["+cost_usd"] == 0.5
    assert u["+input_tokens"] == 0
    assert u["last_context_tokens"] == 0


# --- the stream driver ----------------------------------------------------

def stream(*events):
    return [json.dumps(e) for e in events]


def test_run_renders_each_event_and_banks_usage(tmp_path, capsys):
    (tmp_path / "TODO.md").write_text(
        "_Status: in-progress_\n\n## 📋 Next Up\n\n## 🔄 In Progress\n\n"
        "## ✅ Done\n\n## 🚫 Blocked\n", encoding="utf-8")
    rc = rp.run(stream(INIT, TOOL_USE, RESULT), module_dir=str(tmp_path), pass_no=1)
    out = capsys.readouterr().out
    assert "controls.lua" in out
    assert rc == 0
    data = json.loads((tmp_path / ".ralph" / "status.json").read_text(encoding="utf-8"))
    assert data["cost_usd"] == 0.1234
    assert data["input_tokens"] == 1203
    assert data["last_event_at"]         # the idle-detector's heartbeat


def test_run_survives_a_garbage_line(tmp_path, capsys):
    rc = rp.run(["{ half a line", "", "not json at all", json.dumps(RESULT)],
                module_dir=str(tmp_path), pass_no=1)
    assert rc == 0
    assert "0.12" in capsys.readouterr().out


def test_run_stops_and_kills_the_child_when_STOP_appears(tmp_path, capsys):
    # `touch <dir>/.ralph/STOP` must halt a run mid-pass without hunting a PID.
    ralph = tmp_path / ".ralph"
    ralph.mkdir()
    (ralph / "STOP").write_text("", encoding="utf-8")
    killed = []
    rc = rp.run(stream(INIT, TOOL_USE, RESULT), module_dir=str(tmp_path), pass_no=1,
                kill=lambda: killed.append(True))
    assert rc == rp.EXIT_STOPPED
    assert killed == [True]
    assert "STOP" in capsys.readouterr().out


def test_run_without_a_stop_file_never_kills(tmp_path):
    killed = []
    rp.run(stream(RESULT), module_dir=str(tmp_path), pass_no=1,
           kill=lambda: killed.append(True))
    assert killed == []


# --- the idle heartbeat ---------------------------------------------------
#
# A pass can go quiet for minutes (a long compile, a rate-limit backoff, a wedge)
# and they look identical from outside. The heartbeat lives here rather than in
# the shell for a mechanical reason: a backgrounded shell watcher leaves an
# orphaned `sleep` holding the pipe open after the pass ends, while a daemon
# thread dies with its process.

def test_idle_warning_fires_while_the_stream_is_silent(tmp_path, capsys):
    import time

    def slow():
        yield json.dumps(INIT)
        time.sleep(0.35)
        yield json.dumps(RESULT)

    rp.run(slow(), module_dir=str(tmp_path), pass_no=4, card="controls.lua",
           idle_warn=0.1, idle_poll=0.05)
    out = capsys.readouterr().out
    assert "⏳" in out
    assert "controls.lua" in out and "pass 4" in out


def test_no_idle_warning_on_a_brisk_stream(tmp_path, capsys):
    rp.run(stream(INIT, TOOL_USE, RESULT), module_dir=str(tmp_path), pass_no=1,
           idle_warn=30, idle_poll=0.05)
    assert "⏳" not in capsys.readouterr().out


def test_idle_warning_is_off_by_default(tmp_path, capsys):
    import time

    def slow():
        yield json.dumps(INIT)
        time.sleep(0.2)
        yield json.dumps(RESULT)

    rp.run(slow(), module_dir=str(tmp_path), pass_no=1)
    assert "⏳" not in capsys.readouterr().out


def test_stop_during_a_silent_stream_kills_without_waiting_for_an_event(tmp_path):
    # The case that matters: a wedged pass emits nothing, so a STOP check that
    # only runs between events would never fire — the exact situation someone
    # plants a STOP file for.
    import time

    ralph = tmp_path / ".ralph"
    ralph.mkdir()
    events = []

    def slow():
        yield json.dumps(INIT)
        (ralph / "STOP").write_text("", encoding="utf-8")
        time.sleep(0.4)
        events.append("next-event")
        yield json.dumps(RESULT)

    rc = rp.run(slow(), module_dir=str(tmp_path), pass_no=1,
                kill=lambda: events.append("kill"), idle_poll=0.05)
    assert rc == rp.EXIT_STOPPED
    assert events[0] == "kill"       # fired during the silence, not after it


# --- terminating the child safely ----------------------------------------
#
# The PID the loop parks in `.ralph/child.pid` comes from bash's `$!`. Under Git
# Bash on Windows that is an *MSYS* pid, which shares no numbering with Windows
# pids — and `os.kill` on Windows is `TerminateProcess`. Handing it an MSYS pid
# would at best fail and at worst hard-kill an unrelated process that happens to
# have that number. So: use the `kill` binary that understands the pid, and
# refuse to guess when it is absent.

def test_terminate_prefers_the_kill_binary():
    calls = []
    how = rp._terminate("1234", which=lambda n: "/usr/bin/kill",
                        run=lambda *a, **k: calls.append(a[0]))
    assert how == "kill"
    assert calls == [["/usr/bin/kill", "-TERM", "1234"]]


def test_terminate_falls_back_to_os_kill_on_posix():
    sent = []
    how = rp._terminate("1234", which=lambda n: None, os_name="posix",
                        os_kill=lambda pid, sig: sent.append((pid, sig)))
    assert how == "os.kill"
    assert sent == [(1234, rp.signal.SIGTERM)]


def test_terminate_refuses_to_guess_on_windows_without_a_kill_binary():
    sent = []
    how = rp._terminate("1234", which=lambda n: None, os_name="nt",
                        os_kill=lambda pid, sig: sent.append((pid, sig)))
    assert how is None
    assert sent == []          # never TerminateProcess an MSYS pid


def test_terminate_survives_a_missing_process():
    def boom(*a, **k):
        raise OSError("no such process")
    assert rp._terminate("1234", which=lambda n: None, os_name="posix",
                         os_kill=boom) is None


def test_kill_from_pid_file_reads_the_pid_and_terminates(tmp_path):
    pid_file = tmp_path / "child.pid"
    pid_file.write_text("4242\n", encoding="utf-8")
    seen = []
    rp._kill_from_pid_file(str(pid_file),
                           terminate=lambda p, **kw: seen.append(p))()
    assert seen == ["4242"]


def test_kill_from_pid_file_is_a_noop_without_a_file(tmp_path):
    seen = []
    rp._kill_from_pid_file(str(tmp_path / "missing.pid"),
                           terminate=lambda p, **kw: seen.append(p))()
    rp._kill_from_pid_file(None, terminate=lambda p, **kw: seen.append(p))()
    assert seen == []


def test_explicit_kill_bin_wins_over_a_path_lookup():
    # The loop resolves `kill` in its *own* shell (`type -P kill`) and passes it
    # down, because a Python child launched with a bare Windows PATH cannot see
    # Git Bash's /usr/bin — and without it the safety check above would (rightly)
    # refuse to kill anything at all.
    calls = []
    how = rp._terminate("77", kill_bin="/git/usr/bin/kill.exe",
                        which=lambda n: None, os_name="nt",
                        run=lambda *a, **k: calls.append(a[0]))
    assert how == "kill"
    assert calls == [["/git/usr/bin/kill.exe", "-TERM", "77"]]
