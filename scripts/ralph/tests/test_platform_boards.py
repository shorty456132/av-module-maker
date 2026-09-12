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


# --- Q-SYS representative board (self-contained specs) --------------------
#
# Mirrors the board qsys create-plugin emits in Ralph Loop Mode after S3: each
# card's Spec folds the house-rule nuggets, the canonical Name/author, and the
# exact control-name list it needs, so a cold pass never opens the big Q-SYS
# reference docs (QSYS_PATTERNS.md / QSYS_CONSTRAINTS.md / QSYS_DOC_INDEX.md) or
# WebFetches. Cross-file cards carry a complete Depends so scoped reads (S2)
# still see every file they build on. This is a TCP device plugin (the common
# case that pulls in the most reference material).

QSYS_BOARD = """\
# TODO — Epson Projector (qsys)

_Last updated: 2026-09-01_
_Status: in-progress_
_Plan: frozen_
_Loop: ralph (raw bash, fresh context per pass) · Memory: this file + files on disk_

**Module dir:** ./Epson-Projector/
**Emitting skill:** module-maker:create-plugin
**Verify gate:** python "${CLAUDE_PLUGIN_ROOT}/scripts/qsys/compile.py" ./Epson-Projector/
**Done when:** Next Up and In Progress are empty AND the verify gate passes.

## 📋 Next Up
- [ ] **info.lua** — PluginInfo metadata table.
  - Spec: PluginInfo = { Name = "Epson Projector", Version = "1.0.0",
    BuildVersion = "1.0.0.0", Id = <a freshly generated random UUID
    xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx, every digit random, never reused>,
    Author = "Unspecified", Description = "TCP control of an Epson projector" }.
  - Verify: Id is a fresh random UUID; Name/Version/BuildVersion/Author present.
- [ ] **properties.lua** — Design-time properties only.
  - Spec: Insert into props only genuinely design-time values. Here: an integer
    "Poll Interval" (Value 5) and a boolean "Debug Print" (Value false). Do NOT
    put IP/port here — connection details are Setup-page Text controls, not
    properties.
  - Verify: only design-time values; no IP/port/credentials in props.
- [ ] **controls.lua** — All controls (Setup + Control pages).
  - Spec: Insert into ctrls. Connection details are runtime Text controls on a
    Setup page, never properties. Define exactly these names (character-identical
    across controls.lua / layout.lua / runtime.lua): "IPAddress" (Text),
    "Port" (Text), "Connect" (Button, ButtonType Toggle), "Status" (Indicator,
    IndicatorType Status), "Power" (Button, ButtonType Toggle), "Mute" (Button,
    ButtonType Toggle), "InputHDMI1" (Button, ButtonType Trigger). All UserPin =
    true. Never use Count > 1 (single controls here — no arrays).
  - Depends: properties.lua
  - Verify: names match layout.lua & runtime.lua exactly; no Count > 1.
- [ ] **pages.lua** — Build the pages table.
  - Spec: for ix,name in ipairs(PageNames) do table.insert(pages, {name =
    PageNames[ix]}) end. PageNames is { "Control", "Setup" }.
  - Verify: one page entry per PageNames item.
- [ ] **layout.lua** — Visual layout for both pages.
  - Spec: key `layout` by control name; switch on
    PageNames[props["page_index"].Value]. Hold the house visual rules: show the
    build version somewhere; a dark GroupBox background Fill { 35, 35, 35 } behind
    each page; one Label per control; readable text contrast; meaningful button
    colors (Connect green-on { 0, 180, 80 } / dark-off { 80, 80, 80 }); set
    UnlinkOffColor = true on every toggle and the Status LED. Lay out IPAddress,
    Port, Connect, Status on the Setup page; Power, Mute, InputHDMI1 on the
    Control page. Every control from controls.lua gets exactly one layout entry.
  - Depends: controls.lua
  - Verify: each controls.lua name has one layout entry; visual rules satisfied.
- [ ] **runtime.lua** — Runtime logic and device I/O.
  - Spec: Set TCP.ReadTimeout = 0 and TCP.WriteTimeout = 0 (disabled — non-zero
    only for a TCP server). Read the target from Controls["IPAddress"].String and
    tonumber(Controls["Port"].String) or 23 — never from a property. Funnel every
    command through one Send(cmd) that print("TX: "..cmd) then TCP:Write, and one
    ParseResponse(data) that print("RX: "..data); log socket Error/Connected/
    Reconnect state changes. Confirmed protocol (TCP, port 23, delimiter \\r):
    Power On "PWR ON", Power Off "PWR OFF", Mute toggle "MUTE ON"/"MUTE OFF",
    HDMI1 "SOURCE 30", status poll "PWR?". Wire Connect to connect/disconnect;
    Power/Mute/InputHDMI1 handlers send the commands above; poll "PWR?" every
    Properties["Poll Interval"].Value seconds via a Timer. Control names must
    match controls.lua exactly.
  - Depends: controls.lua, properties.lua
  - Verify: every Controls["..."] used exists in controls.lua; both timeouts 0.
- [ ] **model.lua** — Model variants.
  - Spec: if props.Model ~= nil and props.Model.Value ~= "" then insert
    { props.Model.Value } else insert { "Base Model" } end.
  - Verify: always yields at least one model row.
- [ ] **plugin.lua** — Orchestrator entry point.
  - Spec: Header lines "-- Epson Projector", "-- by Unspecified", "-- <date>".
    PageNames = { "Control", "Setup" }. Define GetColor/GetPrettyName/GetPages/
    GetModel/GetProperties/GetPins/RectifyProperties/GetComponents/GetWiring/
    GetControls/GetControlLayout, each delegating via --[[ #include "<file>.lua"
    ]]; the trailing `if Controls then --[[ #include "runtime.lua" ]] end` block
    loads runtime on the Core. GetPrettyName shows PluginInfo.Version.
  - Depends: info.lua, properties.lua, controls.lua, pages.lua, layout.lua, runtime.lua, model.lua
  - Verify: includes every emitted file; PageNames matches layout's pages.
- [ ] **README.md** — Plugin documentation.
  - Spec: Document name/description, the two properties, every control, Setup-page
    configuration (IP/port), protocol notes (TCP port 23, \\r-delimited), and the
    Control/Setup pages.
  - Depends: controls.lua, properties.lua
  - Verify: lists every property and control; Setup + protocol notes present.
- [ ] **compile** — Run the verify gate.
  - Spec: Compile the plugin; fix any diagnostics and recompile until clean.
  - Depends: plugin.lua
  - Verify: python "${CLAUDE_PLUGIN_ROOT}/scripts/qsys/compile.py" ./Epson-Projector/  -> exit 0

## 🔄 In Progress

## ✅ Done

## 🚫 Blocked
"""


def test_qsys_board_drains_in_dependency_order():
    """The emitted Q-SYS board drives start-to-finish, one card per pass in
    dependency order, to a drained `done` board ending on the compile gate."""
    order, final = drive(QSYS_BOARD)
    assert order[0] == "info.lua"
    assert order[-1] == "compile"
    deps = deps_of(QSYS_BOARD)
    seen = set()
    for title in order:
        for dep in deps[title]:
            assert dep in seen, f"{title!r} worked before its dep {dep!r}"
        seen.add(title)
    assert b.parse(final).status == "done"
    last = b.parse(QSYS_BOARD).section("Next Up")[-1]
    assert last.title == "compile"
    assert "compile.py" in last.raw


def test_qsys_cards_are_self_contained():
    """S3: no card's Spec defers to a big Q-SYS reference doc or a live fetch for
    a value it must write — a cold pass builds from the Spec alone — and every
    cross-file card carries a complete Depends so scoped reads still see every
    file it builds on."""
    board = b.parse(QSYS_BOARD)
    specs = {c.title: c.raw for name in b.SECTIONS for c in board.section(name)}

    # No spec may send a pass into the big reference set or the live docs.
    banned = [
        "qsys_patterns.md", "qsys_constraints.md", "qsys_doc_index.md",
        "webfetch", "help.qsys.com",
    ]
    for title, raw in specs.items():
        low = raw.lower()
        for needle in banned:
            assert needle not in low, (
                f"{title!r} spec defers to {needle!r}; S3 specs must be "
                f"self-contained so a pass never opens the big refs"
            )

    # Every cross-file card names a complete Depends set (the files it reads).
    deps = deps_of(QSYS_BOARD)
    assert "controls.lua" in deps["layout.lua"]
    assert {"controls.lua", "properties.lua"} <= set(deps["runtime.lua"])
    assert {
        "info.lua", "properties.lua", "controls.lua", "pages.lua",
        "layout.lua", "runtime.lua", "model.lua",
    } <= set(deps["plugin.lua"]), "plugin.lua must depend on every include"
    assert "plugin.lua" in deps["compile"]


# --- scoped-read safety (S2) ----------------------------------------------
#
# S2 stops each cold pass from reading the whole directory: it reads only the
# files named by the current card's `Depends:` (via `board.py deps`). That is
# only safe if every `Depends:` entry names a card that actually exists on the
# board — a dangling dependency would silently drop a file the card needs and
# the pass would never know to read it. This guards the invariant across every
# emit-mode fixture, so a future skill edit that mistypes a dep is caught here.

ALL_EMIT_BOARDS = (QSYS_BOARD, SIMPLPLUS_BOARD, SIMPLSHARP_BOARD, SIMPLSHARP_REVISE_BOARD)


def test_every_depends_names_a_real_card():
    for text in ALL_EMIT_BOARDS:
        deps = deps_of(text)
        titles = set(deps)
        for title, dep_list in deps.items():
            for dep in dep_list:
                assert dep in titles, (
                    f"{title!r} Depends on {dep!r}, which is not a card title on "
                    f"the board — a scoped pass would never read that file"
                )
