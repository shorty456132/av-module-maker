"""Unit tests for the Ralph run-state writer (scripts/ralph/status.py).

`status.json` is the loop's only machine-readable heartbeat: it is what a
second terminal, the Claude session that launched a background run, and P6's
token measurement all read. Three properties are load-bearing here:

1. It embeds `board.summarize()` verbatim — one board parser, not two, so the
   watcher can never name a different card than the engine.
2. Writes MERGE. The loop writes it many times per run (pass start, pass end,
   terminal path); a later write must never clobber `started_at`/`pid`.
3. It never raises. A crashed pass that leaves a half-written file must degrade
   to a message — a traceback here would take the loop down with it.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import status as st  # noqa: E402


BOARD = """\
# TODO — Sample Plugin (qsys)

_Last updated: 2026-09-01_
_Status: in-progress_
_Plan: frozen_

## 📋 Next Up
- [ ] **controls.lua** — Define all controls.
  - Depends: info.lua

## 🔄 In Progress
- [ ] **info.lua** — PluginInfo table.

## ✅ Done

## 🚫 Blocked
"""


def module(tmp_path, text=BOARD):
    (tmp_path / "TODO.md").write_text(text, encoding="utf-8")
    return str(tmp_path)


# --- write ----------------------------------------------------------------

def test_write_creates_schema_v1_with_embedded_board_summary(tmp_path):
    d = module(tmp_path)
    st.write(d, {"pass": 1, "max_passes": 40, "state": "running", "pid": 4242})
    data = json.loads((tmp_path / ".ralph" / "status.json").read_text(encoding="utf-8"))
    assert data["schema"] == 1
    assert data["pass"] == 1 and data["max_passes"] == 40
    assert data["state"] == "running"
    # The board block is summarize()'s dict, not a re-derived copy.
    assert data["board"]["current"] == "info.lua"
    assert data["board"]["remaining"] == 2
    assert data["started_at"] and data["updated_at"]


def test_second_write_merges_and_keeps_started_at_and_pid(tmp_path):
    d = module(tmp_path)
    st.write(d, {"pass": 1, "pid": 4242})
    first = st.read(d)
    st.write(d, {"pass": 2})
    second = st.read(d)
    assert second["started_at"] == first["started_at"]
    assert second["pid"] == 4242          # not clobbered by a write that omits it
    assert second["pass"] == 2            # but the supplied key did move


def test_write_refreshes_the_board_block_from_disk(tmp_path):
    d = module(tmp_path)
    st.write(d, {"pass": 1})
    (tmp_path / "TODO.md").write_text(
        BOARD.replace("_Status: in-progress_", "_Status: done_"), encoding="utf-8")
    st.write(d, {"pass": 2})
    assert st.read(d)["board"]["status"] == "done"


def test_plus_prefixed_keys_accumulate_for_cumulative_spend(tmp_path):
    # The per-pass renderer reports one pass's usage; the run total is the sum.
    d = module(tmp_path)
    st.write(d, {"+cost_usd": 0.10, "+input_tokens": 1200})
    st.write(d, {"+cost_usd": 0.05, "+input_tokens": 800})
    data = st.read(d)
    assert round(data["cost_usd"], 4) == 0.15
    assert data["input_tokens"] == 2000


def test_write_survives_a_corrupt_status_file(tmp_path):
    d = module(tmp_path)
    ralph = tmp_path / ".ralph"
    ralph.mkdir()
    (ralph / "status.json").write_text("{ this is not json", encoding="utf-8")
    st.write(d, {"pass": 7})              # must not raise
    assert st.read(d)["pass"] == 7


def test_write_works_without_a_todo_file(tmp_path):
    # The loop writes status before it has validated the board; no TODO.md must
    # not be fatal.
    st.write(str(tmp_path), {"state": "starting"})
    assert st.read(str(tmp_path))["board"] is None


# --- show / report --------------------------------------------------------

def test_show_renders_pass_card_and_progress(tmp_path, capsys):
    d = module(tmp_path)
    st.write(d, {"pass": 3, "max_passes": 40, "state": "running", "cost_usd": 0.42})
    assert st.main(["show", d]) == 0
    out = capsys.readouterr().out
    assert "pass 3/40" in out
    assert "info.lua" in out          # the current card, by name
    assert "0.42" in out              # spend so far
    assert "running" in out


def test_show_on_a_corrupt_file_prints_a_message_not_a_traceback(tmp_path, capsys):
    d = module(tmp_path)
    ralph = tmp_path / ".ralph"
    ralph.mkdir()
    (ralph / "status.json").write_text("{ nope", encoding="utf-8")
    rc = st.main(["show", d])
    out = capsys.readouterr().out + capsys.readouterr().err
    assert rc != 0
    assert "unreadable" in out.lower() or "could not" in out.lower()


def test_show_with_no_run_says_so(tmp_path, capsys):
    rc = st.main(["show", module(tmp_path)])
    assert rc != 0
    assert "no run" in capsys.readouterr().out.lower()


def test_report_writes_markdown_and_prints_its_path(tmp_path, capsys):
    d = module(tmp_path)
    st.write(d, {"pass": 5, "max_passes": 40, "state": "finished", "exit_code": 0,
                 "cost_usd": 1.25})
    assert st.main(["report", d]) == 0
    printed = capsys.readouterr().out.strip().splitlines()[-1]
    report = tmp_path / ".ralph" / "REPORT.md"
    assert report.exists()
    assert os.path.basename(printed) == "REPORT.md"
    body = report.read_text(encoding="utf-8")
    assert "exit 0" in body and "done" in body.lower()
    assert "1.25" in body


def test_report_explains_a_nonzero_exit_in_words(tmp_path):
    # Exit codes are the loop's contract (0 done · 1 max · 2 no TODO · 3 blocked
    # · 4 not converging · 5 stopped · 6 timeout); the report must name them so a
    # human reading it the next morning does not have to look them up.
    d = module(tmp_path)
    st.write(d, {"state": "finished", "exit_code": 4})
    st.main(["report", d])
    body = (tmp_path / ".ralph" / "REPORT.md").read_text(encoding="utf-8")
    assert "not converging" in body.lower()


def test_write_cli_accepts_key_value_pairs(tmp_path):
    # This is the shape ralph-module-loop.sh calls: bare key=value words.
    d = module(tmp_path)
    assert st.main(["write", d, "pass=2", "state=running", "+cost_usd=0.25"]) == 0
    data = st.read(d)
    assert data["pass"] == 2 and data["state"] == "running"
    assert data["cost_usd"] == 0.25
