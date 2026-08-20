---
name: simplplus-revise
description: Review and revise an existing Crestron SIMPL+ module (.usp) — fix bugs, improve logic, and verify against SIMPL+ constraints
argument-hint: module file or directory path
---

# Revise Crestron SIMPL+ Module

## Before revising
- Read `${CLAUDE_PLUGIN_ROOT}/reference/crestron/CRESTRON_CONSTRAINTS.md` and
  `${CLAUDE_PLUGIN_ROOT}/reference/crestron/CRESTRON_PATTERNS.md`. The
  **SIMPL+ Gotchas** section lists hard compile-error rules (scalars before
  arrays, required top-of-module directives, I/O declared in strict type order
  **digital → analog → serial** — all inputs, then all outputs, then parameters,
  `propBounds` before `propDefaultValue`) plus the `_SKIP_` padding rule that
  keeps parameters from covering signal names on the symbol — verify the module
  against every one of them.
- For API/behavior questions, search `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplplus/documents/`.
- Establish a baseline: compile the module **before** changing it (see below) so
  you know whether it started clean and don't blame a pre-existing error on your edit.

## Revision checklist
- [ ] Audit against SIMPL+ signal/handler conventions and reserved names
- [ ] Verify I/O declaration order: all inputs (digital → analog → serial), then
      all outputs (same type order), then parameters — reorder if violated
- [ ] Verify symbol alignment: if the module has N parameters, the first input
      and first output declarations should each lead with N `_SKIP_` entries so
      parameter labels don't cover signal names — add/adjust if missing (gotcha #6)
- [ ] Fix bugs; preserve the module's INPUT/OUTPUT contract unless asked otherwise
- [ ] Re-compile clean (0 errors) via **Compile & verify** before finishing
- [ ] Summarize every change made

## Compile & verify
Compile the revised `.usp` to confirm it still builds — a revision isn't done
until it compiles with 0 errors:

```
python "${CLAUDE_PLUGIN_ROOT}/scripts/crestron/compile.py" <path/to/module.usp>
```

- With no `--target`, the module builds for **both current generations**
  (`series3,series4`) — the default. Match `--target` to a specific processor
  (`series2`, `series3`, `series4`) only when the project requires it.
- **On `[FAILED]`:** read each `file: ERROR <code> (Line <n>) - <message>`, fix,
  and recompile until clean. Compare against the pre-edit baseline so you know
  which errors your change introduced versus which were already present.
- **If the script prints `SIMPL+ compiler not found`:** the Crestron toolchain
  isn't installed here — tell the user to install it (Crestron Master Installer)
  or point `--compiler=<path>` / the `SPLUSCC` env var at `SPlusCC.exe`, and give
  them the compile command to run themselves. Don't report the module as broken.
