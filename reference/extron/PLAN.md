# Extron Module-Maker — Build Plan

Kanban board for adding **Extron ControlScript** support to Module-Maker. Cards
are **vertical slices**: each delivers one thin, independently reviewable
end-to-end piece. Deliverable target: a **reusable device module** (a class in
`src/modules/device/`), per the 2026-08-30 scoping decision.

## Anchor / definition of done (whole effort)

Done = a user can run an Extron skill against a device description and get a
correct, static-analysis-clean device-module `.py` that follows
`EXTRON_CONSTRAINTS.md` and `EXTRON_PATTERNS.md`, plus a matching revise skill.

## Confirmed decisions

- **Deliverable:** reusable device module (not full-project scaffold; not UI).
- **Docs:** vendored into `reference/extron/` (`extronlib/` stubs, `template/`,
  `snippets/`) — overrides the Q-SYS "index-only" copyright precedent by user
  choice; revisit before public distribution (see `README.md` Provenance).
- **This session (DONE):** reference gathering only — `OVERVIEW`, `CONSTRAINTS`,
  `PATTERNS`, vendored material, this plan. **No skills authored yet.**
- **Verification model:** ControlScript has **no CLI compiler** (unlike SIMPL+).
  A module is "verified" by **static analysis against the vendored stubs**
  (pyright/mypy with `extronlib/<version>/` on the path) + import/lint, not a build.

## Inter-phase contracts (define before implementing)

- **Skill roots:** register `./skills/extron/` in `.claude-plugin/plugin.json`
  `skills` array (currently only qsys + crestron). Discovery is non-recursive —
  each skill is its own dir with `SKILL.md`.
- **Reference API used by all slices:** skills read the three `EXTRON_*.md` docs
  and delegate deep API lookups to an **Explore subagent** over
  `reference/extron/extronlib/<version>/` (same convention as `simplplus-create`).
- **Module contract (what generated modules always expose):** a class taking
  connection args; `Connect()` called from `system.Initialize()`; commands as
  methods; feedback via `ModuleSupport.WatchVariable`/`eventEx`. This is the
  stable shape both create and revise skills assume.

---

## 📋 To Do

### Slice 2 — `extron-revise` skill (audit + fix existing module)  ·  vertical
*Standalone (no PRD): paste code/path → audited against constraints → revised
module + change summary. Mirrors `qsys-refactor` / `simplsharp-revise`.*
- [ ] `skills/extron/extron-revise/SKILL.md` — audit checklist == the 12
      constraints; output revised file + per-change summary citing constraint #.
- **Tests to drive it (write first):**
  - [ ] A seeded module with each violation (str-assumed RX, unbuffered parse,
        `time.sleep`, unchecked `Connect`, dual RX+SendAndWait) is detected and fixed.
  - [ ] Revised output passes the Slice 1 static-analysis gate.

### Slice 3 — static-analysis verify harness  ·  supporting  ·  MOSTLY DONE
*Folded into Slice 1 — the checker was the test target that made the skill
testable.* Built as an **AST-based** checker (stdlib only; pyright optional),
since pyright/mypy aren't installed on the dev host.
- [x] `scripts/extron/extron_check.py` — AST checks (`EX-SLEEP`, `EX-CONN`,
      `EX-RXBUF`, `EX-MIX`, `EX-SYNTAX`) + optional pyright pass against a
      selectable stub tree; `file:line` diagnostics; non-zero exit on error.
- [ ] *(remaining)* Add pyright to the dev host (or document install) so the
      type-check pass actually runs; today it's silently skipped when absent.
- [ ] *(remaining)* Extend AST checks as new constraints surface from real use.

---

## 🚧 In Progress

_(none)_

---

## ✅ Done

- **Reference foundation** — `reference/extron/`: `README`, `EXTRON_OVERVIEW`,
  `EXTRON_CONSTRAINTS` (12 rules), `EXTRON_PATTERNS` (5 skeletons), vendored
  `extronlib/{1.8.21xi,3.13.39}/`, `template/`, `snippets/`. (2026-08-30)
- **Slice 1 — `extron-create` skill** (2026-08-30):
  - `scripts/extron/extron_check.py` — AST-based verify harness (TDD: tests
    written first) + `scripts/extron/README.md`.
  - `scripts/extron/tests/test_extron_check.py` — 9 passing tests (good/bad
    fixtures per check; canonical Pattern §1 verified clean end-to-end).
  - `skills/extron/extron-create/SKILL.md`; registered `./skills/extron/` in
    `.claude-plugin/plugin.json`.

---

## Parking lot (out of scope this pass)

- Full-project scaffold from `template/` (main/devices/system/ui) — the other
  deliverable option; revisit if a per-module skill proves insufficient.
- Touchpanel/UI generation (`extronlib.ui`, `.gdl` GUI layouts).
- `project.json` descriptor generation from a materials list (part numbers are
  already in `snippets/device-snippets.json`).
- Index→URL + WebFetch migration of the vendored docs if the repo goes public.
