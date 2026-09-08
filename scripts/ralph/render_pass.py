#!/usr/bin/env python3
"""Live renderer for one Ralph pass's `claude -p` stream.

`claude -p` with no `--output-format` prints nothing until the pass ends, which
is what made the loop opaque: several minutes of silence, then a wall of text.
Run it with `--output-format stream-json --verbose` and pipe it through here
instead, and the pass narrates itself — one short line per tool call, per error,
and a final line carrying the API's own token and cost accounting.

    { claude -p ... & echo $! > child.pid; wait $!; } \
        | tee .ralph/logs/pass-07.jsonl \
        | python render_pass.py --dir ./My-Plugin --pass 7 --pid-file child.pid

Two rules, because this sits in the middle of a pipe carrying model output:

- **Never raise.** A malformed line, a truncated event, or an event type from a
  newer CLI renders nothing and the stream continues. A traceback here would
  break the pipe mid-pass and lose the run.
- **Usage comes from the `result` event** — the API's accounting, not ours.

It also stamps `last_event_at` into `.ralph/status.json` (the idle detector's
heartbeat) and checks for `.ralph/STOP` between events, so `touch STOP` halts a
run mid-pass without anyone hunting for a PID.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import shutil
import signal
import subprocess
import sys
import threading
import time
from typing import Iterable, List, Optional

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import status as st  # noqa: E402

EXIT_STOPPED = 5          # matches the loop's exit-code contract (status.EXIT_MEANING)

TEXT_MAX = 200            # assistant prose is context, not the deliverable
ERR_MAX = 240

# Per tool, the input key worth showing. The point is *what* it touched, never
# the payload — a dumped `old_string` would bury the line it belongs to.
_TOOL_TARGET_KEYS = ("file_path", "command", "path", "pattern", "notebook_path",
                     "url", "prompt", "description")


def parse_line(line: str) -> Optional[dict]:
    """One NDJSON line -> dict, or None if it is blank/garbage/not an object."""
    line = (line or "").strip()
    if not line:
        return None
    try:
        obj = json.loads(line)
    except (ValueError, TypeError):
        return None
    return obj if isinstance(obj, dict) else None


def _content_blocks(event: dict) -> List[dict]:
    message = event.get("message")
    if not isinstance(message, dict):
        return []
    content = message.get("content")
    if not isinstance(content, list):
        return []
    return [c for c in content if isinstance(c, dict)]


def _one_line(text: str, limit: int) -> str:
    flat = " ".join(str(text).split())
    return flat if len(flat) <= limit else flat[: limit - 1] + "…"


def _tool_target(block: dict) -> str:
    args = block.get("input")
    if not isinstance(args, dict):
        return ""
    for key in _TOOL_TARGET_KEYS:
        value = args.get(key)
        if isinstance(value, str) and value.strip():
            if key in ("file_path", "path", "notebook_path"):
                # Long absolute paths are noise; the basename identifies the file.
                return os.path.basename(value.rstrip("/\\")) or value
            return _one_line(value, 90)
    return ""


def _render_usage(event: dict) -> str:
    usage = event.get("usage")
    usage = usage if isinstance(usage, dict) else {}
    return "in {i:,} · out {o:,} · cache-read {cr:,}".format(
        i=int(usage.get("input_tokens") or 0),
        o=int(usage.get("output_tokens") or 0),
        cr=int(usage.get("cache_read_input_tokens") or 0))


def render_event(event) -> List[str]:
    """Zero or more display lines for one stream event. Never raises."""
    if not isinstance(event, dict):
        return []
    try:
        kind = event.get("type")

        if kind == "system" and event.get("subtype") == "init":
            session = str(event.get("session_id") or "")[:8] or "?"
            return ["⏵ session {s} · model {m}".format(
                s=session, m=event.get("model") or "?")]

        if kind == "assistant":
            lines = []
            for block in _content_blocks(event):
                if block.get("type") == "tool_use":
                    target = _tool_target(block)
                    lines.append("🔧 {n}{t}".format(
                        n=block.get("name") or "?",
                        t=" " + target if target else ""))
                elif block.get("type") == "text":
                    text = _one_line(block.get("text") or "", TEXT_MAX)
                    if text:
                        lines.append("💬 " + text)
            return lines

        if kind == "user":
            lines = []
            for block in _content_blocks(event):
                if block.get("type") == "tool_result" and block.get("is_error"):
                    content = block.get("content")
                    if isinstance(content, list):
                        content = " ".join(
                            c.get("text", "") for c in content if isinstance(c, dict))
                    lines.append("❌ " + _one_line(content or "tool error", ERR_MAX))
            return lines

        if kind == "result":
            mark = "✗" if event.get("is_error") else "✔"
            duration = event.get("duration_ms")
            secs = "{d:.0f}s".format(d=duration / 1000.0) if isinstance(
                duration, (int, float)) else "?"
            return ["{mark} pass complete · {t} turns · {s} · ${c:.4f} · {u}".format(
                mark=mark, t=event.get("num_turns", "?"), s=secs,
                c=float(event.get("total_cost_usd") or 0.0),
                u=_render_usage(event))]
    except Exception:  # noqa: BLE001 — a render bug must never break the pipe
        return []
    return []


def usage_from_result(event) -> Optional[dict]:
    """The `result` event's accounting, keyed for `status.write()`'s `+` merge
    so a pass's numbers accumulate into the run total. None for other events."""
    if not isinstance(event, dict) or event.get("type") != "result":
        return None
    usage = event.get("usage")
    usage = usage if isinstance(usage, dict) else {}

    def num(key):
        try:
            return int(usage.get(key) or 0)
        except (TypeError, ValueError):
            return 0

    try:
        cost = float(event.get("total_cost_usd") or 0.0)
    except (TypeError, ValueError):
        cost = 0.0
    return {
        "+cost_usd": cost,
        "+input_tokens": num("input_tokens"),
        "+output_tokens": num("output_tokens"),
        "+cache_read_tokens": num("cache_read_input_tokens"),
        "+cache_creation_tokens": num("cache_creation_input_tokens"),
    }


def _stamp() -> str:
    return datetime.datetime.now().strftime("%H:%M:%S")


def _terminate(pid_text: str, *, kill_bin: Optional[str] = None,
               which=shutil.which, run=subprocess.run,
               os_name=os.name, os_kill=os.kill) -> Optional[str]:
    """SIGTERM a pass's child by the PID bash parked for us. Returns how it was
    done, or None if it could not be done safely.

    The pid comes from bash's `$!`, which under Git Bash on Windows is an *MSYS*
    pid — a numbering unrelated to Windows pids. `os.kill` on Windows is
    `TerminateProcess`, so handing it that number would at best fail and at worst
    hard-kill an unrelated process. Hence: prefer the `kill` binary, which speaks
    the same pid namespace bash does (and forwards through `timeout` to the child
    on POSIX too), and refuse to guess when there isn't one. The loop passes
    `kill_bin` down because it resolved the binary in its own shell: a Python
    child launched with a bare Windows PATH cannot see Git Bash's /usr/bin.
    """
    kill_bin = kill_bin or which("kill")
    try:
        if kill_bin:
            run([kill_bin, "-TERM", str(pid_text)], check=False)
            return "kill"
        if os_name != "nt":
            os_kill(int(pid_text), signal.SIGTERM)
            return "os.kill"
    except (OSError, ValueError):
        pass  # already gone, or never started — nothing to stop
    return None


def _kill_from_pid_file(pid_file: Optional[str], terminate=_terminate,
                        kill_bin: Optional[str] = None):
    """A killer that SIGTERMs the `claude` child whose PID the loop parked in a
    file. The renderer is downstream in the pipe, so it cannot see the child
    directly — the file is the handoff."""
    def kill():
        if not pid_file:
            return
        try:
            with open(pid_file, "r", encoding="utf-8") as f:
                pid_text = f.read().strip()
        except OSError:
            return
        if pid_text:
            terminate(pid_text, kill_bin=kill_bin)
    return kill


def _stamp_status(module_dir: str, fields: dict) -> None:
    """Status writes are observability: a failure here must never take the pass
    down with it."""
    fields = dict(fields)
    fields["last_event_at"] = datetime.datetime.now().astimezone().isoformat(
        timespec="seconds")
    try:
        st.write(module_dir, fields)
    except OSError:
        pass


def run(lines: Iterable[str], module_dir: str, pass_no: int, card: str = "",
        kill=None, out=None, idle_warn: Optional[float] = None,
        idle_poll: float = 5.0) -> int:
    """Render a whole pass's stream. Returns 0, or EXIT_STOPPED if `.ralph/STOP`
    appeared mid-pass (after killing the child).

    `idle_warn` seconds of silence produces a heartbeat line naming the pass and
    card. It lives here, not in the loop's shell, for a mechanical reason: a
    backgrounded shell watcher leaves an orphaned `sleep` holding the pipe open
    after the pass ends, whereas this daemon thread dies with its process.
    """
    out = out or sys.stdout
    stop_file = st.stop_path(module_dir)
    last_seen = [time.monotonic()]

    def emit(text):
        print("[{t}] {x}".format(t=_stamp(), x=text), file=out, flush=True)

    done = threading.Event()
    stopped = threading.Event()

    def watchdog():
        """Polls while the stream is silent — which is precisely when both of
        these matter. A STOP check that only ran between events would never fire
        on the wedged pass someone planted the file for."""
        while not done.wait(idle_poll):
            if os.path.exists(stop_file):
                emit("⏹ STOP file found — killing this pass.")
                if kill:
                    kill()
                stopped.set()
                _stamp_status(module_dir, {"state": "stopped"})
                return
            if idle_warn:
                idle = time.monotonic() - last_seen[0]
                if idle >= idle_warn:
                    emit("⏳ pass {p}{c} — silent for {i:.0f}s".format(
                        p=pass_no, c=" ({0})".format(card) if card else "", i=idle))
                    last_seen[0] = time.monotonic()  # once per idle_warn window

    threading.Thread(target=watchdog, daemon=True).start()

    for line in lines:
        last_seen[0] = time.monotonic()
        if os.path.exists(stop_file):
            done.set()
            emit("⏹ STOP file found — halting this pass.")
            if kill:
                kill()
            _stamp_status(module_dir, {"state": "stopped"})
            return EXIT_STOPPED

        event = parse_line(line)
        if event is None:
            continue
        for rendered in render_event(event):
            emit(rendered)

        usage = usage_from_result(event)
        fields = dict(usage) if usage else {}
        fields["pass"] = pass_no
        _stamp_status(module_dir, fields)
    done.set()
    return EXIT_STOPPED if stopped.is_set() else 0


def main(argv) -> int:
    # Windows pipes default to the locale encoding, which cannot encode the
    # status glyphs; without this the first rendered line kills the process.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass
    ap = argparse.ArgumentParser(description="Render one Ralph pass's stream-json.")
    ap.add_argument("--dir", required=True, help="module directory (holds .ralph/)")
    ap.add_argument("--pass", dest="pass_no", type=int, default=0)
    ap.add_argument("--pid-file", default=None,
                    help="file holding the `claude` child PID, killed on STOP")
    ap.add_argument("--card", default="", help="card title, for the idle warning")
    ap.add_argument("--kill-bin", default=None,
                    help="path to `kill`, resolved by the calling shell")
    ap.add_argument("--idle-warn", type=float, default=0,
                    help="seconds of silence before a heartbeat line (0 = off)")
    args = ap.parse_args(argv)
    return run(sys.stdin, module_dir=args.dir, pass_no=args.pass_no, card=args.card,
               idle_warn=args.idle_warn or None,
               kill=_kill_from_pid_file(args.pid_file, kill_bin=args.kill_bin))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
