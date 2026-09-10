#!/usr/bin/env python3
"""Ralph run state — the loop's machine-readable heartbeat.

A raw Ralph loop is opaque by construction: every pass is a fresh `claude -p`
process, so there is no session to inspect and nothing accumulates in memory.
This module is the fix. It keeps one JSON file per run at
`<module-dir>/.ralph/status.json` that answers, at any moment and from anywhere:
*which pass, which card, how many done, how long, how much spend, is it alive.*

Design rules:

- **One board parser.** The `board` block is `board.summarize()` verbatim, so a
  watcher can never name a different card than the engine driving the loop.
- **Writes merge.** The loop writes many times per run; a later write must not
  clobber `started_at` / `pid`. Keys prefixed `+` accumulate numerically, which
  is how per-pass token/cost numbers become a run total.
- **It never raises.** A crashed pass can leave a half-written file; degrading
  to a message keeps the loop alive instead of taking it down.

CLI:
    python status.py write  <dir> [key=value | +key=value ...]
    python status.py show   <dir>     -> human-readable one-screen render
    python status.py report <dir>     -> writes .ralph/REPORT.md, prints its path
"""

from __future__ import annotations

import datetime
import json
import os
import sys
from typing import Optional

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import board as b  # noqa: E402

SCHEMA = 1
RALPH_DIR = ".ralph"
STATUS_FILE = "status.json"
REPORT_FILE = "REPORT.md"
STOP_FILE = "STOP"

# The loop's exit-code contract, in one place so the shell, the report and the
# docs cannot drift apart.
EXIT_MEANING = {
    0: "done — the board drained and the verify gate passed",
    1: "hit max passes without draining the board",
    2: "no TODO.md — the create/build skill has not emitted a board",
    3: "blocked — a card needs a human (see the Blocked section)",
    4: "not converging — remaining cards did not drop for STALL_MAX passes",
    5: "stopped — a .ralph/STOP file was planted",
    6: "pass timeout — a pass exceeded PASS_TIMEOUT and was killed",
}

# Set once, on the first write of a run, and preserved by every later merge.
_STICKY = ("started_at",)


def _now() -> str:
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def ralph_dir(module_dir: str) -> str:
    return os.path.join(module_dir, RALPH_DIR)


def status_path(module_dir: str) -> str:
    return os.path.join(ralph_dir(module_dir), STATUS_FILE)


def stop_path(module_dir: str) -> str:
    return os.path.join(ralph_dir(module_dir), STOP_FILE)


def _board_summary(module_dir: str) -> Optional[dict]:
    """summarize() of the module's TODO.md, or None if there is no board yet.
    A malformed board must not kill the writer, so failures are None too."""
    todo = os.path.join(module_dir, "TODO.md")
    try:
        with open(todo, "r", encoding="utf-8") as f:
            return b.summarize(b.parse(f.read()))
    except (OSError, ValueError):
        return None


def read(module_dir: str) -> Optional[dict]:
    """The run state, or None if there is no run / the file is unreadable."""
    try:
        with open(status_path(module_dir), "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError):
        return None
    return data if isinstance(data, dict) else None


def write(module_dir: str, fields: Optional[dict] = None) -> dict:
    """Merge `fields` into the run state and persist it.

    `key` sets; `+key` adds numerically to whatever is there (0 if absent),
    which is how one pass's usage rolls up into the run's cumulative spend. The
    board block and `updated_at` refresh on every write; `started_at` only on
    the first. Never raises on a corrupt existing file — it starts a fresh one.
    """
    data = read(module_dir) or {}
    for key, value in (fields or {}).items():
        if key.startswith("+"):
            name = key[1:]
            data[name] = (data.get(name) or 0) + value
        else:
            data[key] = value

    data["schema"] = SCHEMA
    data["module_dir"] = os.path.abspath(module_dir)
    for key in _STICKY:
        data.setdefault(key, _now())
    data["updated_at"] = _now()
    data["board"] = _board_summary(module_dir)

    os.makedirs(ralph_dir(module_dir), exist_ok=True)
    tmp = status_path(module_dir) + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    os.replace(tmp, status_path(module_dir))
    return data


# --- rendering ------------------------------------------------------------

def _age(iso: Optional[str]) -> Optional[int]:
    """Seconds since an ISO stamp, or None if missing/unparseable."""
    if not iso:
        return None
    try:
        then = datetime.datetime.fromisoformat(iso)
    except ValueError:
        return None
    now = datetime.datetime.now().astimezone()
    if then.tzinfo is None:
        then = then.astimezone()
    return int((now - then).total_seconds())


def _dur(seconds: Optional[int]) -> str:
    if seconds is None:
        return "?"
    if seconds < 60:
        return f"{seconds}s"
    if seconds < 3600:
        return f"{seconds // 60}m{seconds % 60:02d}s"
    return f"{seconds // 3600}h{(seconds % 3600) // 60:02d}m"


def render(data: dict) -> str:
    """One screen of human-readable run state — what `show` prints."""
    board = data.get("board") or {}
    lines = [
        "Ralph run — {d}  [{s}]".format(
            d=data.get("module_dir", "?"), s=data.get("state", "?")),
        "  pass {p}/{m} · card: {c} · {d}/{t} cards done · {r} remaining".format(
            p=data.get("pass", "?"), m=data.get("max_passes", "?"),
            c=board.get("current") or "—",
            d=board.get("done", "?"), t=board.get("total", "?"),
            r=board.get("remaining", "?")),
        "  board: {s} · plan {pl} · started {st} · idle {idle}".format(
            s=board.get("status", "?"), pl=board.get("plan", "?"),
            st=data.get("started_at", "?"),
            idle=_dur(_age(data.get("last_event_at") or data.get("updated_at")))),
        "  spend: ${c:.2f} · in {i:,} · out {o:,} · cache read {cr:,}".format(
            c=data.get("cost_usd", 0.0) or 0.0,
            i=int(data.get("input_tokens", 0) or 0),
            o=int(data.get("output_tokens", 0) or 0),
            cr=int(data.get("cache_read_tokens", 0) or 0)),
    ]
    for blocked in board.get("blocked") or []:
        lines.append("  🚫 {t}: {r}".format(t=blocked["title"], r=blocked["reason"]))
    exit_code = data.get("exit_code")
    if exit_code is not None:
        lines.append("  exit {c} — {m}".format(
            c=exit_code, m=EXIT_MEANING.get(exit_code, "unknown")))
    else:
        lines.append("  pid {p} · stop with: touch {f}".format(
            p=data.get("pid", "?"),
            f=os.path.join(data.get("module_dir", "."), RALPH_DIR, STOP_FILE)))
    return "\n".join(lines)


def render_report(data: dict) -> str:
    """The after-the-fact REPORT.md, written on every terminal path so a run
    that ended overnight explains itself without re-deriving anything."""
    board = data.get("board") or {}
    exit_code = data.get("exit_code")
    elapsed = None
    start_age, end_age = _age(data.get("started_at")), _age(data.get("updated_at"))
    if start_age is not None and end_age is not None:
        elapsed = start_age - end_age
    rows = [
        ("Outcome",
         "exit {c} — {m}".format(c=exit_code, m=EXIT_MEANING.get(exit_code, "unknown"))
         if exit_code is not None else "state: {s}".format(s=data.get("state", "?"))),
        ("Board status", board.get("status", "?")),
        ("Cards", "{d}/{t} done · {r} remaining".format(
            d=board.get("done", "?"), t=board.get("total", "?"),
            r=board.get("remaining", "?"))),
        ("Passes", "{p} of {m} max".format(
            p=data.get("pass", "?"), m=data.get("max_passes", "?"))),
        ("Elapsed", _dur(elapsed)),
        ("Started", data.get("started_at", "?")),
        ("Finished", data.get("updated_at", "?")),
        ("Cost", "${c:.2f}".format(c=data.get("cost_usd", 0.0) or 0.0)),
        ("Tokens", "in {i:,} · out {o:,} · cache read {cr:,} · cache write {cw:,}".format(
            i=int(data.get("input_tokens", 0) or 0),
            o=int(data.get("output_tokens", 0) or 0),
            cr=int(data.get("cache_read_tokens", 0) or 0),
            cw=int(data.get("cache_creation_tokens", 0) or 0))),
    ]
    out = [
        "# Ralph run report — {n}".format(
            n=os.path.basename(data.get("module_dir", "") or "?")),
        "",
        "| | |",
        "|---|---|",
    ]
    out += ["| {k} | {v} |".format(k=k, v=v) for k, v in rows]
    blocked = board.get("blocked") or []
    if blocked:
        out += ["", "## 🚫 Blocked cards", ""]
        out += ["- **{t}** — {r}".format(t=x["title"], r=x["reason"]) for x in blocked]
    out += [
        "",
        "Per-pass streams: `{d}/logs/pass-NN.jsonl` · full log: `{d}/run.log`".format(
            d=RALPH_DIR),
        "",
    ]
    return "\n".join(out)


def report(module_dir: str) -> str:
    """Write REPORT.md from the current run state and return its path."""
    data = read(module_dir) or {"module_dir": os.path.abspath(module_dir)}
    os.makedirs(ralph_dir(module_dir), exist_ok=True)
    path = os.path.join(ralph_dir(module_dir), REPORT_FILE)
    with open(path, "w", encoding="utf-8") as f:
        f.write(render_report(data))
    return path


# --- CLI ------------------------------------------------------------------

def _coerce(value: str):
    """key=value arrives from bash as text; keep numbers numeric so `+` sums
    and the JSON stays useful to jq."""
    for cast in (int, float):
        try:
            return cast(value)
        except ValueError:
            pass
    low = value.lower()
    if low in ("true", "false"):
        return low == "true"
    if low in ("null", "none", ""):
        return None
    return value


def _parse_pairs(words) -> dict:
    fields = {}
    for word in words:
        if "=" not in word:
            raise ValueError("expected key=value, got {w!r}".format(w=word))
        key, value = word.split("=", 1)
        fields[key] = _coerce(value)
    return fields


def main(argv) -> int:
    # Windows pipes default to the locale encoding, which cannot encode the
    # status glyphs; without this the first rendered line kills the process.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass
    if not argv:
        print(__doc__)
        return 2
    cmd, rest = argv[0], argv[1:]
    if not rest:
        print("{c}: missing <module-dir>".format(c=cmd), file=sys.stderr)
        return 2
    module_dir = rest[0]

    if cmd == "write":
        try:
            write(module_dir, _parse_pairs(rest[1:]))
        except ValueError as e:
            print("write: {e}".format(e=e), file=sys.stderr)
            return 2
        return 0

    if cmd == "show":
        if not os.path.exists(status_path(module_dir)):
            print("no run state in {d} — no run has started here.".format(
                d=ralph_dir(module_dir)))
            return 1
        data = read(module_dir)
        if data is None:
            print("run state at {p} is unreadable (corrupt or half-written) — the "
                  "loop may still be alive; check {l}.".format(
                      p=status_path(module_dir),
                      l=os.path.join(ralph_dir(module_dir), "run.log")))
            return 1
        print(render(data))
        return 0

    if cmd == "report":
        print(report(module_dir))
        return 0

    print("unknown command: {c}".format(c=cmd), file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
