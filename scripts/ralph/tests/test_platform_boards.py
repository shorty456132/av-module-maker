"""Contract-conformance tests for platform-emitted Ralph boards.

P1 proved the board engine on a Q-SYS board (see test_board.py). These tests
prove the *same* engine drives boards emitted by the other platform skills,
with **no engine changes** — that is the whole point of P2/P3: the P1 contract
(reference/RALPH_TODO.md) is genuinely platform-agnostic.

No skill and no LLM are exercised here. Each fixture is a hand-written board of
the exact shape a create skill emits, and the assertions check that the engine
(parse / pick / start / done / derive_status) can drive it start-to-finish in
dependency order to a drained `done` board whose final card is the compile gate.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import board as b  # noqa: E402


# --- helpers --------------------------------------------------------------

def drive(text):
    """Simulate the raw loop deterministically: pick -> start -> done until the
    board drains. Returns (order_of_titles, final_board_text). File work is a
    no-op here; we only exercise the engine's card selection and transitions."""
    order = []
    # Hard cap guards against a bug that would otherwise loop forever.
    for _ in range(1000):
        title = b.pick(b.parse(text))
        if title is None:
            break
        text = b.start(text, title)
        text = b.done(text, title)
        order.append(title)
    return order, text


def deps_of(text):
    """Map card title -> its Depends list, across every section."""
    board = b.parse(text)
    out = {}
    for name in b.SECTIONS:
        for card in board.section(name):
            out[card.title] = card.depends
    return out


# --- SIMPL+ representative board ------------------------------------------
#
# Mirrors the card list the simplplus-create skill emits (SKILL.md "Emit a
# TODO.md plan"): I/O structure -> event handlers -> parameters -> module body
# -> final compile gate. Dependencies encode the SIMPL+ constraints (all I/O in
# strict type order first; _SKIP_ pad count = number of parameters).

SIMPLPLUS_BOARD = """\
# TODO — Sony Projector (simplplus)

_Last updated: 2026-09-01_
_Status: in-progress_
_Plan: frozen_
_Loop: ralph (raw bash, fresh context per pass) · Memory: this file + files on disk_

**Module dir:** ./Sony-Projector/
**Emitting skill:** module-maker:simplplus-create
**Verify gate:** python "${CLAUDE_PLUGIN_ROOT}/scripts/crestron/simplplus_build.py" ./Sony-Projector/Sony-Projector.usp
**Done when:** Next Up and In Progress are empty AND the verify gate passes.

## 📋 Next Up
- [ ] **io-structure** — Top directives + all I/O in strict type order.
  - Spec: Required top-of-module directives, then INPUT then OUTPUT then
    PARAMETER declarations. Order strictly digital -> analog -> serial within
    inputs, then within outputs. This module has 2 parameters (IP_Address,
    Port), so prepend 2 `_SKIP_` entries to the first input and first output
    declaration (gotcha #6) so parameter labels don't cover signal names.
  - Verify: signals declared inputs-before-outputs-before-parameters.
- [ ] **event-handlers** — CHANGE / PUSH / RELEASE / EVENT handlers.
  - Spec: One handler per interactive input; scalars declared before arrays.
  - Depends: io-structure
  - Verify: every declared digital input drives a handler.
- [ ] **parameters** — *_PARAMETER declarations with bounds/defaults.
  - Spec: propBounds BEFORE propDefaultValue for each parameter.
  - Depends: io-structure
  - Verify: IP_Address/Port carry bounds then defaults.
- [ ] **module-body** — Function Main() + SOCKET connect/parse logic.
  - Spec: Open the TCP socket from IP_Address/Port params; parse the RX buffer.
  - Depends: event-handlers, parameters
  - Verify: Main() references the socket handle and buffer.
- [ ] **compile** — Run the verify gate.
  - Spec: Compile the .usp; fix any diagnostics and recompile until clean.
  - Depends: module-body
  - Verify: python "${CLAUDE_PLUGIN_ROOT}/scripts/crestron/simplplus_build.py" ./Sony-Projector/Sony-Projector.usp  -> exit 0

## 🔄 In Progress

## ✅ Done

## 🚫 Blocked
"""


def test_emit_mode_boards_ship_frozen():
    # Every board a create/revise skill emits must be frozen: planned complete
    # up front, so the loop can never grow it (runaway guard). Discovery -> block.
    for text in (SIMPLPLUS_BOARD, SIMPLSHARP_BOARD, SIMPLSHARP_REVISE_BOARD):
        assert b.parse(text).plan == "frozen"


def test_simplplus_board_parses_into_cards():
    board = b.parse(SIMPLPLUS_BOARD)
    assert [c.title for c in board.section("Next Up")] == [
        "io-structure",
        "event-handlers",
        "parameters",
        "module-body",
        "compile",
    ]


def test_simplplus_board_picks_in_dependency_order():
    order, _ = drive(SIMPLPLUS_BOARD)
    deps = deps_of(SIMPLPLUS_BOARD)
    seen = set()
    for title in order:
        for dep in deps[title]:
            assert dep in seen, f"{title!r} worked before its dep {dep!r}"
        seen.add(title)


def test_simplplus_board_drains_to_done():
    order, final = drive(SIMPLPLUS_BOARD)
    # Every card is worked exactly once and the board reaches machine `done`.
    assert order == [
        "io-structure",
        "event-handlers",
        "parameters",
        "module-body",
        "compile",
    ]
    assert b.parse(final).status == "done"
    assert b.derive_status(b.parse(final)) == "done"


def test_simplplus_final_card_is_the_compile_gate():
    board = b.parse(SIMPLPLUS_BOARD)
    last = board.section("Next Up")[-1]
    assert last.title == "compile"
    # The verify gate must invoke the SIMPL+ build script.
    assert "simplplus_build.py" in last.raw
    # And it must be the *last* card — nothing depends-after the gate.
    all_titles = [c.title for c in board.section("Next Up")]
    assert all_titles[-1] == "compile"


# --- SIMPL# representative board ------------------------------------------
#
# Mirrors the card list the simplsharp-create skill emits: the two-half SIMPL#
# deliverable (C# .clz + SIMPL+ .usp wrapper) built in strict order — **wrapper
# last** — so the wrapper provably mirrors the built class instead of being
# re-designed from prose (Decision 5). Dependencies encode that order:
#   controller-class -> csproj -> clz-build -> wrapper -> build (orchestrator gate)
# The wrapper card Depends: clz-build (the built C# class), so pick() can never
# surface the wrapper before the .clz exists. The final `build` card runs the
# orchestrator (simplsharp_build.py) that stages the .clz beside the .usp and
# compiles the wrapper — the module is not done until it exits 0.

SIMPLSHARP_BOARD = """\
# TODO — Acme Controller (simplsharp)

_Last updated: 2026-09-01_
_Status: in-progress_
_Plan: frozen_
_Loop: ralph (raw bash, fresh context per pass) · Memory: this file + files on disk_

**Module dir:** ./Acme/
**Emitting skill:** module-maker:simplsharp-create
**Verify gate:** python "${CLAUDE_PLUGIN_ROOT}/scripts/crestron/simplsharp_build.py" ./Acme/Acme/Acme.csproj ./Acme/AcmeWrapper/AcmeWrapper.usp
**Done when:** Next Up and In Progress are empty AND the verify gate passes.

## 📋 Next Up
- [ ] **controller-class** — AcmeController.cs (the .clz call-in surface).
  - Spec: Author AcmeController from Pattern 1. Public methods = inputs
    (ushort for digital/analog, SimplSharpString for serial); delegate-typed
    properties = outputs. Parameterless ctor; IDisposable stops timers and nulls
    callbacks (Gotchas #2,#3,#4,#7). Never block the SIMPL+ thread.
  - Verify: class compiles under Pattern 1; public surface is the wrapper contract.
- [ ] **csproj** — Acme.csproj (SDK-style, net47 + SDK.Library).
  - Spec: Minimal Microsoft.NET.Sdk project; TargetFramework net47; DebugType
    portable; PackageReference Crestron.SimplSharp.SDK.Library 2.21.* — this is
    what makes the build emit a .clz, not a plain .dll.
  - Depends: controller-class
  - Verify: csproj declares net47 and the SDK.Library package.
- [ ] **clz-build** — Standalone dotnet build; .clz on disk.
  - Spec: `dotnet build Acme/Acme.csproj -c Debug`, then confirm
    Acme/bin/Debug/net47/Acme.clz exists (the .clz never appears in the
    `-> .dll` MSBuild line; list for it). This proves the class compiles.
  - Depends: csproj
  - Verify: Acme.clz (a ~MB archive) sits beside the .dll.
- [ ] **wrapper** — AcmeWrapper.usp derived from the built class.
  - Spec: Derive the signal spec mechanically from the built class surface
    (methods -> inputs, delegate properties -> outputs; ushort/SimplSharpString
    marshal types) and invoke simplplus-create to emit the wrapper with the
    SIMPL# glue (#USER_SIMPLSHARP_LIBRARY "Acme", instance decl, one CHANGE per
    input, CALLBACK FUNCTION + RegisterDelegate per output). Do NOT compile the
    wrapper standalone — the .clz isn't staged beside it yet (that's `build`).
  - Depends: clz-build
  - Verify: every public method has a CHANGE handler; every delegate property is
    RegisterDelegate'd to a CALLBACK FUNCTION; names/marshal types match the class.
- [ ] **build** — Run the orchestrator verify gate.
  - Spec: Chain both halves into one placeable symbol: rebuild the .clz, stage it
    beside the .usp, compile the wrapper. Fix any diagnostics and re-run until clean.
  - Depends: wrapper
  - Verify: python "${CLAUDE_PLUGIN_ROOT}/scripts/crestron/simplsharp_build.py" ./Acme/Acme/Acme.csproj ./Acme/AcmeWrapper/AcmeWrapper.usp  -> exit 0

## 🔄 In Progress

## ✅ Done

## 🚫 Blocked
"""


def test_simplsharp_board_orders_wrapper_last():
    """The wrapper card Depends: the built C# class card (clz-build), so pick()
    never surfaces the wrapper before the class is Done — the wrapper is derived
    from the built .clz, never re-designed from prose (Decision 5)."""
    board = b.parse(SIMPLSHARP_BOARD)
    deps = deps_of(SIMPLSHARP_BOARD)
    assert "clz-build" in deps["wrapper"], "wrapper must depend on the built class"

    # Drive the loop and prove the class is Done before the wrapper is ever picked.
    order, _ = drive(SIMPLSHARP_BOARD)
    assert order.index("clz-build") < order.index("wrapper")
    # And the wrapper precedes the final orchestrator gate.
    assert order.index("wrapper") < order.index("build")


def test_simplsharp_board_drains():
    """Full board drains to machine `done`, one card per pass in dependency
    order, with simplsharp_build.py as the final verify gate."""
    order, final = drive(SIMPLSHARP_BOARD)
    assert order == [
        "controller-class",
        "csproj",
        "clz-build",
        "wrapper",
        "build",
    ]
    # No card is ever surfaced before all of its Depends are Done.
    deps = deps_of(SIMPLSHARP_BOARD)
    seen = set()
    for title in order:
        for dep in deps[title]:
            assert dep in seen, f"{title!r} worked before its dep {dep!r}"
        seen.add(title)

    assert b.parse(final).status == "done"
    assert b.derive_status(b.parse(final)) == "done"

    # The final card is the orchestrator gate.
    last = b.parse(SIMPLSHARP_BOARD).section("Next Up")[-1]
    assert last.title == "build"
    assert "simplsharp_build.py" in last.raw


# --- SIMPL# revise (bug-checklist) board ----------------------------------
#
# Mirrors the board simplsharp-revise emits: a baseline build first, one
# audit-and-fix card per gotcha class (fan-out from baseline), a wrapper-sync
# card that fans IN on every audit card (so it sees the final public surface),
# and the orchestrator re-verify as the final gate. The fan-in is the load-
# bearing bit — wrapper-sync must never be surfaced until all five audits Done.

SIMPLSHARP_REVISE_BOARD = """\
# TODO — Acme Controller (simplsharp · revise)

_Last updated: 2026-09-01_
_Status: in-progress_
_Plan: frozen_
_Loop: ralph (raw bash, fresh context per pass) · Memory: this file + files on disk_

**Module dir:** ./Acme/
**Emitting skill:** module-maker:simplsharp-revise
**Verify gate:** python "${CLAUDE_PLUGIN_ROOT}/scripts/crestron/simplsharp_build.py" ./Acme/Acme/Acme.csproj ./Acme/AcmeWrapper/AcmeWrapper.usp
**Done when:** Next Up and In Progress are empty AND the verify gate passes.

## 📋 Next Up
- [ ] **baseline-build** — Orchestrator build BEFORE any edit.
  - Spec: Run the gate to establish a baseline; record the current public surface
    (public methods + delegate properties) so later cards know it cold.
  - Verify: baseline result + public surface recorded.
- [ ] **audit-block** — Gotcha #3: never block the SIMPL+ thread.
  - Spec: No Thread.Sleep / sync socket read / long loop in a public method;
    offload to CTimer/CrestronThread. Fix inside existing members where possible.
  - Depends: baseline-build
  - Verify: no blocking call remains in any public method.
- [ ] **audit-marshal** — Gotcha #2: boundary marshal types.
  - Spec: SimplSharpString for serial, ushort for digital/analog; no System.String.
  - Depends: baseline-build
  - Verify: every public member's boundary signature is marshalable.
- [ ] **audit-feedback** — Gotcha #4: feedback only via delegate properties.
  - Spec: Outputs driven only through null-guarded delegate properties.
  - Depends: baseline-build
  - Verify: no other path drives an output.
- [ ] **audit-dispose** — Gotcha #7: IDisposable cleanup.
  - Spec: Dispose stops timers/threads, closes sockets, nulls callbacks.
  - Depends: baseline-build
  - Verify: Dispose releases every handle the class holds.
- [ ] **audit-runtime** — Gotchas #1/#8: runtime + analog scaling.
  - Spec: No unsupported desktop System.* on net47 4-Series; analog scaled 0-65535.
  - Depends: baseline-build
  - Verify: only Crestron.SimplSharp.* runtime APIs used.
- [ ] **wrapper-sync** — Re-sync the wrapper only if the public surface changed.
  - Spec: Compare post-edit surface to baseline. Unchanged -> record "surface
    unchanged, wrapper needs no edit". Changed -> re-derive spec from the new
    class surface and invoke simplplus-revise.
  - Depends: audit-block, audit-marshal, audit-feedback, audit-dispose, audit-runtime
  - Verify: wrapper mirrors the final class surface (or is confirmed unchanged).
- [ ] **re-verify** — Run the orchestrator verify gate.
  - Spec: Re-run the orchestrator; compare to the baseline; fix and re-run until clean.
  - Depends: wrapper-sync
  - Verify: python "${CLAUDE_PLUGIN_ROOT}/scripts/crestron/simplsharp_build.py" ./Acme/Acme/Acme.csproj ./Acme/AcmeWrapper/AcmeWrapper.usp  -> exit 0

## 🔄 In Progress

## ✅ Done

## 🚫 Blocked
"""


def test_simplsharp_revise_board_syncs_wrapper_after_every_audit():
    """wrapper-sync fans in on all five audit cards, so it is never surfaced
    until every audit is Done — it must see the final public surface before
    deciding whether the wrapper needs re-syncing (Decision 5/8)."""
    deps = deps_of(SIMPLSHARP_REVISE_BOARD)
    audits = {"audit-block", "audit-marshal", "audit-feedback",
              "audit-dispose", "audit-runtime"}
    assert audits <= set(deps["wrapper-sync"]), "wrapper-sync must depend on every audit"

    order, _ = drive(SIMPLSHARP_REVISE_BOARD)
    last_audit = max(order.index(a) for a in audits)
    assert last_audit < order.index("wrapper-sync")
    assert order.index("wrapper-sync") < order.index("re-verify")


def test_simplsharp_revise_board_drains():
    """Baseline first, re-verify (orchestrator gate) last, board drains to done."""
    order, final = drive(SIMPLSHARP_REVISE_BOARD)
    assert order[0] == "baseline-build"
    assert order[-1] == "re-verify"
    # No card is ever surfaced before all of its Depends are Done.
    deps = deps_of(SIMPLSHARP_REVISE_BOARD)
    seen = set()
    for title in order:
        for dep in deps[title]:
            assert dep in seen, f"{title!r} worked before its dep {dep!r}"
        seen.add(title)

    assert b.parse(final).status == "done"
    last = b.parse(SIMPLSHARP_REVISE_BOARD).section("Next Up")[-1]
    assert last.title == "re-verify"
    assert "simplsharp_build.py" in last.raw
