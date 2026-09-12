#!/usr/bin/env python3
"""Ralph TODO board engine — the deterministic core of the module-creation loop.

A no-git Ralph loop keeps *all* of its memory in the module's TODO.md plus the
files on disk. This module owns every mechanical edit to that TODO.md so the
transitions are exact and testable, instead of leaving markdown surgery to the
model each pass. The model still decides *what* to build and authors each card's
spec; it calls this module to record the moves.

Board layout (see reference/RALPH_TODO.md for the authored contract):

    _Status: in-progress_            # machine-readable: in-progress | done | blocked
    _Last updated: YYYY-MM-DD_

    ## 📋 Next Up
    - [ ] **<title>** — summary.
      - Spec: ...
      - Depends: a, b                # comma list of other card titles
      - Verify: ...
    ## 🔄 In Progress
    ## ✅ Done
    ## 🚫 Blocked

CLI (used by the loop prompt):
    python board.py next   <dir>                  -> prints title to work, or NONE
    python board.py show   <dir> <title>          -> prints only that card's raw block
    python board.py deps   <dir> <title>          -> prints its Depends: filenames, one per line
    python board.py start  <dir> <title>
    python board.py done   <dir> <title>
    python board.py block  <dir> <title> <reason>
    python board.py add    <dir> <title> [body...]  (refused on a frozen board)
    python board.py status <dir>                  -> prints in-progress|done|blocked
    python board.py remaining <dir>               -> prints count of Next Up + In Progress
    python board.py summary <dir> [--shell]       -> run summary as JSON (or B_* shell vars)
"""

from __future__ import annotations

import datetime
import json
import os
import re
import shlex
import sys
from dataclasses import dataclass, field
from typing import List, Optional

# Section display names, in board order. The emoji live in the markdown headers
# but we key everything off the trailing plain-text name so parsing is robust.
SECTIONS = ["Next Up", "In Progress", "Done", "Blocked"]

_CARD_RE = re.compile(r"^- \[(?P<mark>[ xX])\] \*\*(?P<title>.+?)\*\*")
_HEADER_RE = re.compile(r"^##\s+.*?(" + "|".join(re.escape(s) for s in SECTIONS) + r")\s*$")
# Trailing match is horizontal whitespace only ([^\S\n]) so .sub() never eats the
# line's newline (which would collapse the blank line that follows the front matter).
_STATUS_RE = re.compile(r"^_Status:[^\S\n]*(?P<val>[a-z-]+)_[^\S\n]*$", re.MULTILINE)
_PLAN_RE = re.compile(r"^_Plan:[^\S\n]*(?P<val>[a-z]+)_[^\S\n]*$", re.MULTILINE)
_STAMP_RE = re.compile(r"^_Last updated:[^\S\n]*.*_[^\S\n]*$", re.MULTILINE)
_DEPENDS_RE = re.compile(r"^\s*-\s*Depends:\s*(?P<val>.+?)\s*$", re.MULTILINE)
_BLOCKED_RE = re.compile(r"^\s*-\s*Blocked:\s*(?P<val>.+?)\s*$", re.MULTILINE)


@dataclass
class Card:
    title: str
    done: bool
    raw: str  # the full card block, including its indented body lines

    @property
    def depends(self) -> List[str]:
        m = _DEPENDS_RE.search(self.raw)
        if not m:
            return []
        return [d.strip() for d in m.group("val").split(",") if d.strip()]

    @property
    def blocked_reason(self) -> Optional[str]:
        """The `- Blocked: <reason>` line block() appended, or None. Mirrors
        `depends` so observers read the reason through the same parser the
        engine writes it with."""
        m = _BLOCKED_RE.search(self.raw)
        return m.group("val").strip() if m else None


@dataclass
class Board:
    status: str
    # plan is the runaway guard: `frozen` boards are emitted complete up front
    # and reject `add()` (discovery must `block`, not grow the board). `open`
    # (the default when no `_Plan:` line is present) preserves the old behavior.
    plan: str = "open"
    sections: dict = field(default_factory=dict)

    def section(self, name: str) -> List[Card]:
        return self.sections.get(name, [])


# --- parsing --------------------------------------------------------------

def parse(text: str) -> Board:
    """Parse TODO.md markdown into a Board of sections -> [Card]."""
    status_m = _STATUS_RE.search(text)
    status = status_m.group("val") if status_m else "in-progress"
    plan_m = _PLAN_RE.search(text)
    plan = plan_m.group("val") if plan_m else "open"

    sections: dict = {name: [] for name in SECTIONS}
    current: Optional[str] = None
    card_lines: List[str] = []
    card_title: Optional[str] = None
    card_done = False

    def flush():
        nonlocal card_lines, card_title, card_done
        if card_title is not None and current is not None:
            sections[current].append(
                Card(title=card_title, done=card_done, raw="\n".join(card_lines))
            )
        card_lines, card_title, card_done = [], None, False

    for line in text.splitlines():
        header = _HEADER_RE.match(line)
        if header:
            flush()
            current = header.group(1)
            continue
        card = _CARD_RE.match(line)
        if card:
            flush()
            card_title = card.group("title").strip()
            card_done = card.group("mark").lower() == "x"
            card_lines = [line]
            continue
        if card_title is not None:
            # Continuation of the current card: indented body or blank line
            # inside the block. Stop the block at a non-indented, non-blank line.
            if line.strip() == "" or line.startswith(" ") or line.startswith("\t"):
                card_lines.append(line)
            else:
                flush()
    flush()

    # Trim trailing blank lines captured into card bodies.
    for cards in sections.values():
        for c in cards:
            c.raw = c.raw.rstrip()
    return Board(status=status, plan=plan, sections=sections)


# --- selection ------------------------------------------------------------

def pick(board: Board) -> Optional[str]:
    """Title of the next card to work: resume In Progress, else the top Next Up
    card whose Depends are all satisfied (present in Done). None if nothing is
    eligible."""
    in_prog = board.section("In Progress")
    if in_prog:
        return in_prog[0].title
    done_titles = {c.title for c in board.section("Done")}
    for card in board.section("Next Up"):
        if all(dep in done_titles for dep in card.depends):
            return card.title
    return None


def find_card(board: Board, title: str) -> Optional[Card]:
    """The card with this exact title in any section, or None. Lets a cold pass
    fetch just its card (via `show`/`deps`) without re-parsing the board itself."""
    for name in SECTIONS:
        for card in board.section(name):
            if card.title == title:
                return card
    return None


def derive_status(board: Board) -> str:
    """`done` iff Next Up and In Progress are both empty; else `in-progress`.
    (A blocked board is set explicitly by block(), not derived here.)"""
    if not board.section("Next Up") and not board.section("In Progress"):
        return "done"
    return "in-progress"


def remaining(board: Board) -> int:
    """Count of cards still to finish (Next Up + In Progress). The loop's
    convergence guard greps this each pass: it only drops when a card reaches
    Done — i.e. real forward progress — so a run of non-decreasing values means
    the loop is spinning without completing anything."""
    return len(board.section("Next Up")) + len(board.section("In Progress"))


def summarize(board: Board) -> dict:
    """One dict describing the whole run, for anything watching the loop.

    Deliberately built out of `pick()` / `remaining()` / the parsed sections —
    the *same* calls the loop makes — so a watcher can never disagree with the
    engine about which card is current or whether the board is drained. This is
    the schema `status.py` embeds and P6's measurement reads.
    """
    counts = {name: len(board.section(name)) for name in SECTIONS}
    return {
        "status": board.status,
        "plan": board.plan,
        "remaining": remaining(board),
        "done": counts["Done"],
        "total": sum(counts.values()),
        "current": pick(board),
        "blocked": [
            {"title": c.title, "reason": c.blocked_reason or ""}
            for c in board.section("Blocked")
        ],
    }


# --- rendering ------------------------------------------------------------

def render(board: Board) -> dict:
    """Render each section's cards back to a markdown block keyed by name."""
    out = {}
    for name in SECTIONS:
        out[name] = "\n".join(c.raw for c in board.section(name))
    return out


def _today(today: Optional[str]) -> str:
    return today or datetime.date.today().isoformat()


def _set_status(text: str, status: str) -> str:
    if _STATUS_RE.search(text):
        return _STATUS_RE.sub(f"_Status: {status}_", text, count=1)
    return text


def _set_stamp(text: str, today: str) -> str:
    if _STAMP_RE.search(text):
        return _STAMP_RE.sub(f"_Last updated: {today}_", text, count=1)
    return text


def _replace_section_body(text: str, name: str, body: str) -> str:
    """Replace the card lines under section `name`, preserving the header and
    the blank line that follows it."""
    lines = text.splitlines()
    out: List[str] = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        header = _HEADER_RE.match(line)
        if header and header.group(1) == name:
            out.append(line)
            i += 1
            # Skip the existing body up to the next section header / EOF.
            while i < n and not _HEADER_RE.match(lines[i]):
                i += 1
            out.append("")  # blank line under the header
            if body:
                out.extend(body.splitlines())
                out.append("")
        else:
            out.append(line)
            i += 1
    return "\n".join(out).rstrip() + "\n"


def _move(text: str, title: str, to: str, *, mark_done=False, mark_open=False,
          append_lines: Optional[List[str]] = None) -> str:
    board = parse(text)
    moved: Optional[Card] = None
    for name in SECTIONS:
        remaining = []
        for c in board.section(name):
            if moved is None and c.title == title:
                moved = c
            else:
                remaining.append(c)
        board.sections[name] = remaining
    if moved is None:
        raise ValueError(f"card not found: {title!r}")

    if mark_done and not moved.done:
        moved.raw = re.sub(r"^- \[[ xX]\]", "- [x]", moved.raw, count=1)
    if mark_open and moved.done:
        moved.raw = re.sub(r"^- \[[ xX]\]", "- [ ]", moved.raw, count=1)
    if append_lines:
        moved.raw = moved.raw.rstrip() + "\n" + "\n".join(append_lines)

    board.sections[to].append(moved)

    rendered = render(board)
    for name in SECTIONS:
        text = _replace_section_body(text, name, rendered[name])
    return text


# --- public transitions ---------------------------------------------------

def start(text: str, title: str, today: Optional[str] = None) -> str:
    out = _move(text, title, "In Progress", mark_open=True)
    out = _set_status(out, "in-progress")
    return _set_stamp(out, _today(today))


def done(text: str, title: str, today: Optional[str] = None) -> str:
    out = _move(text, title, "Done", mark_done=True)
    out = _set_status(out, derive_status(parse(out)))
    return _set_stamp(out, _today(today))


def block(text: str, title: str, reason: str, today: Optional[str] = None) -> str:
    out = _move(text, title, "Blocked", append_lines=[f"  - Blocked: {reason}"])
    out = _set_status(out, "blocked")
    return _set_stamp(out, _today(today))


def add(text: str, title: str, body_lines: Optional[List[str]] = None,
        today: Optional[str] = None) -> str:
    board = parse(text)
    if board.plan == "frozen":
        raise ValueError(
            "plan is frozen — new work must be blocked, not added. Emit the full "
            "plan up front; if a cold pass finds unforeseen work, `block` the card "
            "so a human can amend the board and resume."
        )
    raw = f"- [ ] **{title}**"
    if body_lines:
        raw += "\n" + "\n".join(
            ln if ln.startswith("  ") else f"  {ln}" for ln in body_lines
        )
    board.sections["Next Up"].append(Card(title=title, done=False, raw=raw))
    rendered = render(board)
    for name in SECTIONS:
        text = _replace_section_body(text, name, rendered[name])
    return _set_stamp(text, _today(today))


# --- CLI ------------------------------------------------------------------

def _todo_path(module_dir: str) -> str:
    return os.path.join(module_dir, "TODO.md")


def _read(module_dir: str) -> str:
    with open(_todo_path(module_dir), "r", encoding="utf-8") as f:
        return f.read()


def _write(module_dir: str, text: str) -> None:
    with open(_todo_path(module_dir), "w", encoding="utf-8") as f:
        f.write(text)


def main(argv: List[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    cmd, rest = argv[0], argv[1:]
    if cmd == "next":
        print(pick(parse(_read(rest[0]))) or "NONE")
        return 0
    if cmd == "show":
        card = find_card(parse(_read(rest[0])), rest[1])
        if card is None:
            print(f"card not found: {rest[1]!r}", file=sys.stderr)
            return 3
        print(card.raw)
        return 0
    if cmd == "deps":
        card = find_card(parse(_read(rest[0])), rest[1])
        if card is None:
            print(f"card not found: {rest[1]!r}", file=sys.stderr)
            return 3
        for dep in card.depends:
            print(dep)
        return 0
    if cmd == "status":
        print(parse(_read(rest[0])).status)
        return 0
    if cmd == "remaining":
        print(remaining(parse(_read(rest[0]))))
        return 0
    if cmd == "summary":
        data = summarize(parse(_read(rest[0])))
        if "--shell" in rest[1:]:
            # One engine call per pass: the loop `eval`s these. Values are
            # shell-quoted because card titles are free text.
            for key, value in (
                ("B_STATUS", data["status"]), ("B_PLAN", data["plan"]),
                ("B_REMAINING", data["remaining"]), ("B_DONE", data["done"]),
                ("B_TOTAL", data["total"]), ("B_CURRENT", data["current"] or ""),
                ("B_BLOCKED", len(data["blocked"])),
            ):
                print(f"{key}={shlex.quote(str(value))}")
            return 0
        print(json.dumps(data, indent=2))
        return 0
    if cmd == "start":
        _write(rest[0], start(_read(rest[0]), rest[1]))
        return 0
    if cmd == "done":
        _write(rest[0], done(_read(rest[0]), rest[1]))
        return 0
    if cmd == "block":
        _write(rest[0], block(_read(rest[0]), rest[1], " ".join(rest[2:])))
        return 0
    if cmd == "add":
        try:
            _write(rest[0], add(_read(rest[0]), rest[1], list(rest[2:])))
        except ValueError as e:
            print(f"add refused: {e}", file=sys.stderr)
            return 3
        return 0
    print(f"unknown command: {cmd}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
