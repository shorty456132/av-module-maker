# Module-Maker — Tasks

Kanban board for the SIMPL# / SIMPL# Pro **documentation** effort. Cards are
**vertical slices**: each delivers one thin, independently reviewable end-to-end
piece — not a horizontal layer. Slices 3 & 4 are sliced *per target* (a target's
constraints **and** patterns land together), so each leaves the docs coherent.

## Context

Goal: begin creating Crestron SIMPL# modules; first step is **gathering/organizing
documentation**. Two distinct targets, neither yet documented in this repo:

| Target | Artifact | Reaches the program via | Toolchain |
|---|---|---|---|
| **SIMPL#** | `.clz` | A **SIMPL+ wrapper** (`.usp`) exposes the C# class's methods/callbacks as signals; that wrapper is the **SIMPL Windows** symbol | VS + Crestron SIMPL# library template |
| **SIMPL# Pro** | `.cpz` | Standalone program, `CrestronControlSystem` entry class, runs on **4-Series / VC-4** — no SIMPL Windows | VS + Crestron SDK / MSBuild |

Key nuance: a **SIMPL# module is a two-part deliverable** — `.clz` + a SIMPL+ `.usp`
wrapper (the wrapper half = existing `simplplus-create` skill).

Confirmed decisions: **docs only** (skills stay stubs, no code/scaffold generation) ·
**corpus by external path** (no copy/submodule) · **both targets** this pass.

Raw material (reference-only, external): the 1,499-file flat markdown corpus
`SimplSharp-helpDocs` (namespaces `Crestron.SimplSharp*`, shared by both targets) at
`C:\Users\alaia\Documents\AI\claude\claude-skills\Implement Projects\Crestron\SimplSharp-helpDocs`,
searched via the installed `crestron-lookup` sub-agent.

---

## 📋 To Do

### Slice 1 — Distinction doc  ·  `SIMPLSHARP_OVERVIEW.md`
*Thin end-to-end: a reader can tell the two targets apart and know when to use which.*
- [ ] New `reference/crestron/SIMPLSHARP_OVERVIEW.md`: the two-target table + **when to
      use which**.
- [ ] Document **SIMPL# = `.clz` + `.usp` wrapper**: wrapper marshals signals to the C#
      class (public methods from SIMPL+, delegate/callback props for feedback, `ushort`
      for digital/analog, `SimplSharpString` for serial); wrapper half = `simplplus-create`.
- [ ] Document **SIMPL# Pro = standalone**: `CrestronControlSystem` lifecycle, no SIMPL
      Windows, runs on 4-Series/VC-4.
- [ ] Note shared `Crestron.SimplSharp*` foundation; cross-link CONSTRAINTS, PATTERNS, corpus pointer.
- **Done when:** doc reads correctly on review; no code, no invented API.

### Slice 2 — Corpus wiring (external path)  ·  skills can *find* the API docs
*Thin end-to-end: a SIMPL#/Pro skill now routes to the corpus without loading 1,499 files.*
- [ ] New `reference/crestron/SIMPLSHARP_API_CORPUS.md`: single source of truth for the
      absolute corpus path, its shape (`*-Class/-Property/-Method/…md`), and "search via
      `crestron-lookup`, don't bulk-load."
- [ ] Replace empty placeholder READMEs `reference/crestron/simplsharp/README.md` and
      `.../simplsharp-pro/README.md` with pointers to `SIMPLSHARP_API_CORPUS.md` (shared corpus).
- [ ] **Pointer-line-only** edits to the four SKILL.md stubs
      (`simplsharp-{create,revise}`, `simplsharp-pro-{create,revise}`): fix the
      "For API questions, search …" line to route through the corpus pointer /
      `crestron-lookup`; add a link to `SIMPLSHARP_OVERVIEW.md`. **Leave "To implement"
      checklists untouched.**
- **Done when:** corpus path resolves on disk; every README/SKILL pointer targets a real
      in-repo file; no "To implement" list changed.

### Slice 3 — SIMPL# target fully documented  ·  CONSTRAINTS + PATTERNS (SIMPL#)
*Vertical: one target's hard rules **and** ready-to-adapt code land together.*
- [ ] `CRESTRON_CONSTRAINTS.md` — replace the SIMPL# stub with a real gotcha section
      (mirror the SIMPL+ "Gotchas" depth): constrained BCL / SIMPL# library project;
      `SimplSharpString` across the boundary (not `System.String`); never block the
      SIMPL+ callback thread (`CrestronThread`/`CTimer`); feedback via delegate/callback
      props; `Dispose`/program-stop; `.clz` shows no symbol — the `.usp` wrapper does.
- [ ] `CRESTRON_PATTERNS.md` — replace the SIMPL# stub with real skeletons: C# class
      exposing methods + callback props to SIMPL+, **and** the matching `.usp` wrapper.
- [ ] Every corpus-derived rule/pattern carries a `> Source:` link; signatures verified
      via `crestron-lookup`, never invented.
- **Done when:** SIMPL# constraints+patterns are complete and source-traced.

### Slice 4 — SIMPL# Pro target fully documented  ·  CONSTRAINTS + PATTERNS (Pro)
*Vertical: the other target's hard rules **and** ready-to-adapt code land together.*
- [ ] `CRESTRON_CONSTRAINTS.md` — replace the SIMPL# Pro stub: `InitializeSystem()` must
      not block (offload to a thread); register devices + check success before use;
      `ProgramStatusEventHandler` graceful stop; IPID/eControlMethod registration rules.
- [ ] `CRESTRON_PATTERNS.md` — replace the SIMPL# Pro stub with real skeletons:
      `CrestronControlSystem` subclass + `InitializeSystem`; device registration;
      `ProgramStatusEventHandler` stop; threaded TCP receive.
- [ ] `> Source:` links; signatures verified via `crestron-lookup`, never invented.
- **Done when:** SIMPL# Pro constraints+patterns are complete and source-traced.

## 🔧 In Progress
*(empty)*

## ✅ Done
*(empty)*

---

## Inter-slice contracts
- Slices are independently reviewable and can be handed to separate agents. **Slice 1**
  (overview) and **Slice 2** (corpus pointer) are the shared references Slices 3 & 4 link
  to — do them first; Slices 3 and 4 are then independent of each other.
- Shared doc conventions (contract for every slice): `> Source:` link on corpus-derived
  content; mirror the existing SIMPL+ "Gotchas" section and `reference/qsys/QSYS_PATTERNS.md`
  in tone/structure; never invent API — verify against the corpus via `crestron-lookup`.

## Out of scope (parking lot)
- Implementing the four SIMPL#/Pro create/revise skills (leave "To implement" lists).
- `.clz` / `.cpz` / `.cs` scaffold templates or example modules.
- A SIMPL# compile driver (proprietary VS/MSBuild — not automatable here).
- Copying / submoduling the corpus.

## Verification (whole board)
1. **Source-traced:** every class/method/property named in CONSTRAINTS/PATTERNS resolves
   to a real corpus file (spot-check via `crestron-lookup` or grep); no invented API.
2. **Pointers resolve:** path in `SIMPLSHARP_API_CORPUS.md` exists; README + SKILL pointer
   lines target real in-repo files.
3. **No scope leakage:** the four "To implement" checklists unchanged; no `.clz`/`.cpz`/`.cs` created.
4. **User read-through:** confirm the SIMPL# vs SIMPL# Pro distinction (esp. `.clz` + `.usp`
   wrapper) reads correctly before Done.
