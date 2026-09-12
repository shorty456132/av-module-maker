"""Unit tests for the Ralph TODO board engine (scripts/ralph/board.py).

These test the pure board logic only — parsing a module's TODO.md, choosing
the next card, moving cards between sections, and deriving the machine-readable
_Status: line the bash loop greps. No LLM and no subprocess are involved, so
they run anywhere.

The board is the *entire* memory of a no-git Ralph loop, so these invariants
are load-bearing: exactly one card advances per pass, and _Status: only reaches
`done` when Next Up and In Progress are both empty.
"""

import json
import os
import shlex
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import board as b  # noqa: E402


# --- Fixtures -------------------------------------------------------------

FRESH = """\
# TODO — Sample Plugin (qsys)

_Last updated: 2026-09-01_
_Status: in-progress_

**Module dir:** ./Sample-Plugin/
**Verify gate:** python compile.py ./Sample-Plugin/  -> exit 0
**Done when:** Next Up and In Progress are empty AND the verify gate passes.

## 📋 Next Up
- [ ] **info.lua** — PluginInfo table with unique random GUID.
  - Spec: Name/Version/Id/Author/Description.
  - Verify: Id is a fresh random UUID.
- [ ] **controls.lua** — Define all controls.
  - Spec: Setup-page IP/Port/Connect/Status.
  - Depends: info.lua
  - Verify: names match layout.lua & runtime.lua.

## 🔄 In Progress

## ✅ Done

## 🚫 Blocked
"""

RESUMABLE = """\
# TODO — Sample Plugin (qsys)

_Last updated: 2026-09-01_
_Status: in-progress_

## 📋 Next Up
- [ ] **controls.lua** — Define all controls.
  - Depends: info.lua

## 🔄 In Progress
- [ ] **info.lua** — PluginInfo table.

## ✅ Done

## 🚫 Blocked
"""

DRAINED = """\
# TODO — Sample Plugin (qsys)

_Last updated: 2026-09-01_
_Status: in-progress_

## 📋 Next Up

## 🔄 In Progress

## ✅ Done
- [x] **info.lua** — PluginInfo table.
- [x] **compile** — Run the verify gate.

## 🚫 Blocked
"""


# --- parse ----------------------------------------------------------------

def test_parse_reads_status():
    assert b.parse(FRESH).status == "in-progress"


def test_parse_splits_sections_and_cards():
    board = b.parse(FRESH)
    assert [c.title for c in board.section("Next Up")] == ["info.lua", "controls.lua"]
    assert board.section("In Progress") == []
    assert board.section("Done") == []


def test_parse_captures_card_body():
    card = b.parse(FRESH).section("Next Up")[0]
    assert "unique random GUID" in card.raw
    assert card.done is False


def test_parse_reads_depends():
    controls = b.parse(FRESH).section("Next Up")[1]
    assert controls.depends == ["info.lua"]


# --- pick (resume In Progress, else top eligible Next Up) ------------------

def test_pick_resumes_in_progress_card():
    assert b.pick(b.parse(RESUMABLE)) == "info.lua"


def test_pick_takes_top_next_up_when_none_in_progress():
    assert b.pick(b.parse(FRESH)) == "info.lua"


def test_pick_skips_card_with_unmet_dependency():
    # info.lua not yet done, so controls.lua (depends: info.lua) is ineligible;
    # info.lua itself has no deps and is first anyway.
    text = FRESH.replace(
        "- [ ] **info.lua** — PluginInfo table with unique random GUID.\n"
        "  - Spec: Name/Version/Id/Author/Description.\n"
        "  - Verify: Id is a fresh random UUID.\n",
        "",
    )
    # Now Next Up holds only controls.lua, whose dep info.lua is not in Done.
    assert b.pick(b.parse(text)) is None


def test_pick_returns_none_when_drained():
    assert b.pick(b.parse(DRAINED)) is None


# --- move + one-card-per-pass invariant -----------------------------------

def test_start_moves_card_next_up_to_in_progress():
    board = b.parse(b.start(FRESH, "info.lua"))
    assert [c.title for c in board.section("In Progress")] == ["info.lua"]
    assert [c.title for c in board.section("Next Up")] == ["controls.lua"]


def test_done_moves_card_in_progress_to_done_marked_x():
    board = b.parse(b.done(RESUMABLE, "info.lua"))
    done = board.section("Done")
    assert [c.title for c in done] == ["info.lua"]
    assert done[0].done is True
    assert board.section("In Progress") == []


def test_one_card_advances_per_start_done_cycle():
    after = b.done(b.start(FRESH, "info.lua"), "info.lua")
    board = b.parse(after)
    assert [c.title for c in board.section("Done")] == ["info.lua"]
    assert [c.title for c in board.section("Next Up")] == ["controls.lua"]
    assert board.section("In Progress") == []


def test_block_moves_card_and_records_reason():
    board_text = b.block(RESUMABLE, "info.lua", "missing protocol doc")
    board = b.parse(board_text)
    blocked = board.section("Blocked")
    assert [c.title for c in blocked] == ["info.lua"]
    assert "missing protocol doc" in blocked[0].raw


# --- derive_status --------------------------------------------------------

def test_status_in_progress_while_work_remains():
    assert b.derive_status(b.parse(FRESH)) == "in-progress"


def test_status_done_only_when_next_up_and_in_progress_empty():
    assert b.derive_status(b.parse(DRAINED)) == "done"


def test_done_command_flips_status_line_when_board_drained():
    # Finish the only outstanding card; board becomes drained -> status done.
    one_left = RESUMABLE.replace("- [ ] **controls.lua** — Define all controls.\n  - Depends: info.lua\n", "")
    out = b.done(one_left, "info.lua")
    assert b.parse(out).status == "done"


def test_block_sets_status_blocked():
    out = b.block(RESUMABLE, "info.lua", "ambiguous spec")
    assert b.parse(out).status == "blocked"


# --- formatting -----------------------------------------------------------

def test_status_change_preserves_following_blank_line():
    # The blank line after the _Status: front-matter line must survive a status
    # rewrite (regex must not swallow the trailing newline).
    out = b.block(RESUMABLE, "info.lua", "missing doc")
    assert "_Status: blocked_\n\n" in out


def test_transitions_keep_blank_line_before_each_header():
    out = b.done(b.start(FRESH, "info.lua"), "info.lua")
    for header in ["## 📋 Next Up", "## 🔄 In Progress", "## ✅ Done", "## 🚫 Blocked"]:
        idx = out.index(header)
        preceding = out[:idx].rstrip("\n")
        # There must be a blank line (two newlines) between prior content and header.
        assert out[len(preceding):idx] == "\n\n", f"missing blank line before {header!r}"


# --- stamp ----------------------------------------------------------------

def test_transitions_update_last_updated_stamp():
    out = b.start(FRESH, "info.lua", today="2026-09-02")
    assert "_Last updated: 2026-09-02_" in out
    assert "_Last updated: 2026-09-01_" not in out


# --- plan freeze (runaway guard) ------------------------------------------
#
# A frozen board is emitted complete up front and MUST NOT grow during the loop:
# discovery becomes a `block` (halts for a human), never a silent `add`. This is
# the engine half of the runaway-loop guard — enforced here, not just in prose.

FROZEN = FRESH.replace("_Status: in-progress_", "_Status: in-progress_\n_Plan: frozen_")


def test_parse_plan_defaults_open():
    # A board with no _Plan: line is `open` (backward-compatible default).
    assert b.parse(FRESH).plan == "open"


def test_parse_reads_plan_frozen():
    assert b.parse(FROZEN).plan == "frozen"


def test_add_allowed_when_plan_open():
    out = b.add(FRESH, "extra.lua", ["  - Spec: something new."])
    assert "extra.lua" in [c.title for c in b.parse(out).section("Next Up")]


def test_add_refused_when_plan_frozen():
    with pytest.raises(ValueError):
        b.add(FROZEN, "extra.lua", ["  - Spec: sneaking a card in."])
    # And nothing about the board was mutated on the refused call.
    assert "extra.lua" not in FROZEN


# --- remaining (convergence-guard signal) ---------------------------------

def test_remaining_counts_next_up_and_in_progress():
    assert b.remaining(b.parse(FRESH)) == 2         # 2 Next Up, 0 In Progress
    assert b.remaining(b.parse(RESUMABLE)) == 2     # 1 Next Up, 1 In Progress
    assert b.remaining(b.parse(DRAINED)) == 0       # drained


# --- summarize (P5 observability contract) --------------------------------
#
# `summarize()` is the single dict every observer reads: the loop's status
# writer, `status.py show`, and P6's acceptance measurement. It must reuse the
# same parser/pick/remaining the loop itself uses — one board parser, not two —
# so a watcher can never disagree with the engine about what card is current.

BLOCKED = """\
# TODO — Sample Plugin (qsys)

_Last updated: 2026-09-01_
_Status: blocked_

## 📋 Next Up
- [ ] **compile** — Run the verify gate.
  - Depends: controls.lua

## 🔄 In Progress

## ✅ Done
- [x] **info.lua** — PluginInfo table.

## 🚫 Blocked
- [ ] **controls.lua** — Define all controls.
  - Blocked: needs-new-card: no channel map in the spec
"""


def test_summarize_fresh_board_reports_first_card_current():
    s = b.summarize(b.parse(FRESH))
    assert s["status"] == "in-progress"
    assert s["plan"] == "open"
    assert s["current"] == "info.lua"
    assert (s["done"], s["remaining"], s["total"]) == (0, 2, 2)
    assert s["blocked"] == []


def test_summarize_in_progress_board_reports_the_resumed_card():
    s = b.summarize(b.parse(RESUMABLE))
    # `current` is whatever the *engine* would pick, so a watcher and the loop
    # can never name different cards.
    assert s["current"] == "info.lua" == b.pick(b.parse(RESUMABLE))
    assert (s["done"], s["remaining"], s["total"]) == (0, 2, 2)


def test_summarize_blocked_board_parses_the_reason():
    s = b.summarize(b.parse(BLOCKED))
    assert s["status"] == "blocked"
    assert s["blocked"] == [
        {"title": "controls.lua", "reason": "needs-new-card: no channel map in the spec"}
    ]
    # The dependent card is unreachable, so nothing is current.
    assert s["current"] is None
    assert (s["done"], s["total"]) == (1, 3)


def test_summarize_drained_board_reports_done_and_no_current():
    text = b.done(b.start(RESUMABLE, "info.lua"), "info.lua")
    text = b.done(b.start(text, "controls.lua"), "controls.lua")
    s = b.summarize(b.parse(text))
    assert s["status"] == "done"
    assert s["current"] is None
    assert (s["done"], s["remaining"], s["total"]) == (2, 0, 2)


def test_card_blocked_reason_is_none_when_absent():
    assert b.parse(FRESH).section("Next Up")[0].blocked_reason is None


def test_summary_cli_prints_parseable_json(tmp_path, capsys):
    (tmp_path / "TODO.md").write_text(BLOCKED, encoding="utf-8")
    assert b.main(["summary", str(tmp_path)]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["status"] == "blocked"
    assert payload["current"] is None
    assert payload["blocked"][0]["title"] == "controls.lua"


def test_summary_shell_emits_eval_safe_assignments(tmp_path, capsys):
    # The loop `eval`s this to get every board fact in one engine call per pass.
    # Titles are author-written text, so values must survive quoting intact.
    text = FRESH.replace("**info.lua**", "**info.lua (it's odd)**")
    (tmp_path / "TODO.md").write_text(text, encoding="utf-8")
    assert b.main(["summary", str(tmp_path), "--shell"]) == 0
    lines = capsys.readouterr().out.strip().splitlines()
    env = dict(ln.split("=", 1) for ln in lines)
    assert env["B_DONE"] == "0" and env["B_TOTAL"] == "2"
    assert env["B_STATUS"] == "in-progress"
    assert env["B_BLOCKED"] == "0"
    # Round-trips through shell quoting intact — that is what makes `eval` safe.
    assert shlex.split(env["B_CURRENT"]) == ["info.lua (it's odd)"]


def test_summary_shell_leaves_current_empty_when_nothing_is_eligible(tmp_path, capsys):
    (tmp_path / "TODO.md").write_text(BLOCKED, encoding="utf-8")
    b.main(["summary", str(tmp_path), "--shell"])
    env = dict(ln.split("=", 1) for ln in capsys.readouterr().out.strip().splitlines())
    assert env["B_CURRENT"] in ("''", '""', "")
    assert env["B_BLOCKED"] == "1"


# --- show / deps (S1: per-card reads for a cold pass) ---------------------
#
# A cold Ralph pass must be able to fetch *just its card* and *just its
# dependency filenames*, instead of reading the whole TODO.md + directory.
# These two commands are the S2 contract: `show` -> one card's raw block,
# `deps` -> the comma-split Depends: filenames one per line.

TWO_DEPS = """\
# TODO — Sample Plugin (qsys)

_Last updated: 2026-09-01_
_Status: in-progress_

## 📋 Next Up
- [ ] **info.lua** — PluginInfo table with unique random GUID.
  - Spec: Name/Version/Id/Author/Description.
  - Verify: Id is a fresh random UUID.
- [ ] **runtime.lua** — Wire runtime behavior.
  - Spec: Connect on Setup-page controls; poll status.
  - Depends: info.lua, controls.lua
  - Verify: names match controls.lua.

## 🔄 In Progress

## ✅ Done

## 🚫 Blocked
"""


def test_deps_prints_dependency_filenames(tmp_path, capsys):
    # A card with `Depends: info.lua, controls.lua` prints each filename on its
    # own line; a card with no Depends: prints nothing.
    (tmp_path / "TODO.md").write_text(TWO_DEPS, encoding="utf-8")

    assert b.main(["deps", str(tmp_path), "runtime.lua"]) == 0
    assert capsys.readouterr().out.splitlines() == ["info.lua", "controls.lua"]

    assert b.main(["deps", str(tmp_path), "info.lua"]) == 0
    assert capsys.readouterr().out.strip() == ""


def test_show_prints_only_that_card(tmp_path, capsys):
    (tmp_path / "TODO.md").write_text(FRESH, encoding="utf-8")

    assert b.main(["show", str(tmp_path), "controls.lua"]) == 0
    out = capsys.readouterr().out
    # The requested card's block is present in full...
    assert "**controls.lua**" in out
    assert "Setup-page IP/Port/Connect/Status" in out
    # ...and no *other* card's title/spec leaks in. (info.lua's unique spec text
    # never appears; its bare name may occur only inside controls.lua's Depends.)
    assert "PluginInfo table with unique random GUID" not in out
    assert "fresh random UUID" not in out


def test_show_unknown_title_errors(tmp_path, capsys):
    (tmp_path / "TODO.md").write_text(FRESH, encoding="utf-8")
    rc = b.main(["show", str(tmp_path), "nope.lua"])
    assert rc != 0
    err = capsys.readouterr().err
    assert "not found" in err
    assert "nope.lua" in err
