# Ralph `TODO.md` — Module-Creation Loop Contract

This is the **single source of truth** for how the create/build skills turn a
module into a resumable, loopable task board. It is platform-agnostic: Q-SYS,
SIMPL+, and SIMPL# skills all emit and drive the same format. The board engine
that performs every transition is `scripts/ralph/board.py`.

## What a Ralph loop is here

A **raw** Ralph loop: a bash `while` loop (`scripts/ralph/ralph-module-loop.sh`)
that re-runs `claude -p` with the **same prompt** every pass. Each pass is a
**fresh process with a clean context window** — that is the whole point. Because
the model remembers nothing between passes, progress must live **outside** the
model.

**We do not use git as that memory.** The memory is exactly two things:

1. **`TODO.md`** in the module directory — the board (what's done, what's next).
2. **The files already written** in the module directory.

So every card must carry enough spec to be executed cold, and every pass must
**read the existing module files before writing** to stay consistent. This is
*not* the `/ralph-loop` plugin — that one keeps a single accumulating session
via a Stop hook, which is the opposite of fresh context.

## Board layout

`TODO.md` lives in the module output directory (it is git-ignored). Exact shape:

```markdown
# TODO — <Module Name> (<platform>)

_Last updated: YYYY-MM-DD_
_Status: in-progress_        <!-- machine-readable: in-progress | done | blocked -->
_Plan: frozen_              <!-- frozen: the loop may not add cards (see below) -->
_Loop: ralph (raw bash, fresh context per pass) · Memory: this file + files on disk_

**Module dir:** ./<Module-Dir>/
**Emitting skill:** module-maker:<skill>
**Verify gate:** <exact command that must exit 0>
**Done when:** Next Up and In Progress are empty AND the verify gate passes.

## 📋 Next Up
- [ ] **<title>** — one-line summary.
  - Spec: everything needed to build this cold. No prior-context assumptions.
  - Depends: <title>, <title>          # optional; comma list of other card titles
  - Verify: how to know this card is correct.

## 🔄 In Progress
<!-- at most ONE card ever lives here -->

## ✅ Done
- [x] **<title>** — summary.

## 🚫 Blocked
<!-- card + a `- Blocked: <reason>` line; the loop halts when this is non-empty -->
```

### Rules for the board

- **`_Status:`** is the machine-readable line the bash loop greps:
  `in-progress` → keep looping; `done` → success; `blocked` → halt for a human.
- **`_Plan: frozen_`** is the runaway guard. An emit-mode board is planned
  **complete up front** and frozen, so the loop can never grow it: `board.py add`
  is **refused** on a frozen board. A cold pass that discovers genuinely new,
  necessary work `block`s the current card instead (reason `needs-new-card: …`) —
  which halts the loop so a human can amend the plan and resume. This stops an
  eager model from endlessly appending "improvements" and never finishing. (An
  `open` board — no `_Plan:` line — still accepts `add`, e.g. during interactive
  board construction; emit-mode boards must ship `frozen`.)
- **Card title** is the bold text after the checkbox — usually the target
  filename or stage (`controls.lua`, `compile`). Titles are unique per board.
- **The last card is always the verify gate** — the compile/build command that
  must exit 0 (e.g. `python "${CLAUDE_PLUGIN_ROOT}/scripts/qsys/compile.py"
  ./My-Plugin/`). The module is not done until that card passes.
- **`Depends:`** lists card titles that must be in Done before this card is
  eligible. Order Next Up by dependency; deep/foundational cards first.

## The board engine — `scripts/ralph/board.py`

Never hand-edit the section moves; call the engine so transitions are exact.

| Command | Effect |
|---|---|
| `python board.py next <dir>` | Prints the title to work (resume In Progress, else top eligible Next Up), or `NONE`. |
| `python board.py start <dir> <title>` | Move Next Up → In Progress; stamp date; `_Status: in-progress_`. |
| `python board.py done <dir> <title>` | Move In Progress → Done, mark `[x]`; recompute status (`done` iff drained). |
| `python board.py block <dir> <title> <reason>` | Move → Blocked with reason; `_Status: blocked_`. |
| `python board.py add <dir> <title> [body…]` | Append a card to Next Up. **Refused (non-zero) on a `frozen` board** — the loop never calls it; discovery `block`s instead. |
| `python board.py status <dir>` | Print `in-progress` \| `done` \| `blocked`. |
| `python board.py remaining <dir>` | Print the count of unfinished cards (Next Up + In Progress). The loop's convergence guard greps this. |

The model authors card **content** (titles, specs, follow-ups) and does the
actual file work; the engine owns the **markdown surgery** and the status line.

## The per-pass protocol

Each `claude -p` pass runs `scripts/ralph/module-loop-prompt.md`, which does:

1. `board.py next <dir>` → the card to work (`NONE` ⇒ verify + finish).
2. `board.py start <dir> <title>` (skip if already In Progress — resume it).
3. **Read the existing files in `<dir>`** — this is the memory git would give.
4. Do exactly that **one** card, then check its `Verify`. Run the verify-gate
   command only when the card *is* the gate.
5. Success → `board.py done <dir> <title>`.
6. Genuinely stuck (unmet dep, ambiguity, or verify fails twice) **or you
   discovered necessary work the frozen board is missing** →
   `board.py block <dir> <title> "<reason>"` (use `needs-new-card: …` for the
   latter). **Do not `add` cards** — the board is frozen; a human amends it.
7. Exit. The next pass starts clean.

When `board.py status` reports `done`, the loop stops and prints `RALPH-DONE`.
The loop also stops early if the board `_Status:` is `blocked`, or if the
convergence guard sees the unfinished-card count fail to drop for two passes
running (a spinning loop) — both halt for a human rather than burn the pass budget.

## How a create/build skill emits a board

Translate the skill's existing creation order into one card per file/stage,
dependency-ordered, with the compile/verify command as the final card. Write
`TODO.md` **before** writing any module files, then hand off to the loop. See
each skill's *"Emit a `TODO.md` plan"* section for the platform's card list and
verify gate.
