"""Unit tests for the Ralph TODO board engine (scripts/ralph/board.py).

These test the pure board logic only — parsing a module's TODO.md, choosing
the next card, moving cards between sections, and deriving the machine-readable
_Status: line the bash loop greps. No LLM and no subprocess are involved, so
they run anywhere.

The board is the *entire* memory of a no-git Ralph loop, so these invariants
are load-bearing: exactly one card advances per pass, and _Status: only reaches
`done` when Next Up and In Progress are both empty.
"""

import os
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
