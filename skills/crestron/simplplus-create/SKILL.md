---
name: simplplus-create
description: Scaffold a Crestron SIMPL+ module (.usp) from a device description, with correct INPUT/OUTPUT signal structure and event handlers
argument-hint: module description
---

# Create Crestron SIMPL+ Module

## Target
- **Language:** SIMPL+ (C-like)
- **Artifact:** `.usp` source → `.ush` compiled, used inside a SIMPL Windows program
- **Toolchain:** SIMPL+ Cross Compiler (`SPlusCC.exe`), driven by
  `scripts/crestron/simplplus_build.py`. Compilation **is** automatable on a Windows host
  with the Crestron SIMPL+ toolchain installed — see **Compile & verify** below.

## Before writing code
- Read `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplplus/SIMPLPLUS_CONSTRAINTS.md` — the
  **SIMPL+ Gotchas** section lists hard compile-error rules (scalars before
  arrays, required top-of-module directives, I/O declared in strict type order
  **digital → analog → serial** — all inputs, then all outputs, then parameters,
  `propBounds` before `propDefaultValue`) plus the `_SKIP_` padding rule that
  keeps parameters from covering signal names on the symbol. Apply every one of
  them.
- Reuse patterns from `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplplus/SIMPLPLUS_PATTERNS.md`.
- For API/behavior questions, search `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplplus/documents/`
  (delegate to an Explore subagent, per the Q-SYS `create-plugin` convention).

## Each module must include
- [ ] Module skeleton: I/O in strict type order — all inputs
      (`DIGITAL_INPUT` → `ANALOG_INPUT` → `STRING_INPUT`), then all outputs
      (`DIGITAL_OUTPUT` → `ANALOG_OUTPUT` → `STRING_OUTPUT`), then `*_PARAMETER`s
- [ ] Symbol alignment: if the module has N parameters, prepend N `_SKIP_`
      entries to the first input declaration and the first output declaration so
      the parameter labels don't cover the topmost signal names (see gotcha #6)
- [ ] Event handlers: `CHANGE`, `PUSH`, `RELEASE`, `EVENT`
- [ ] Comms (serial/TCP) via `SOCKET` + buffer parsing where applicable
- [ ] Connection details (IP/port/credentials) as parameters, not hard-coded
- [ ] Compiles clean (0 errors) via **Compile & verify**

## Compile & verify
After writing the `.usp`, compile it to confirm it builds — do not consider the
module done until it compiles with 0 errors:

```
python "${CLAUDE_PLUGIN_ROOT}/scripts/crestron/simplplus_build.py" <path/to/module.usp>
```

- With no `--target`, the module builds for **both current generations**
  (`series3,series4`) — this is the default. Narrow it with `--target` only when
  the project targets a specific processor: `series2`, `series3`, `series4`
  (comma-separated for multiple, e.g. `--target=series4`).
- **On `[OK]` (exit 0):** report the generated `.ush` header and `SPlsWork/`
  artifacts (listed by the script) to the user.
- **On `[FAILED]` (non-zero exit):** read each diagnostic line
  (`file: ERROR <code> (Line <n>) - <message>`), fix the `.usp` accordingly, and
  recompile. Repeat until the compile is clean.
- **If the script prints `SIMPL+ compiler not found`:** the Crestron SIMPL+
  toolchain isn't installed on this host. Do **not** report the module as broken —
  tell the user to install it via the Crestron Master Installer (or point
  `--compiler=<path>` / the `SPLUSCC` env var at `SPlusCC.exe`), and hand them the
  compile command above to run themselves.
