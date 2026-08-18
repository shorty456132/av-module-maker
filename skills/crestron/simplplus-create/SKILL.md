---
name: simplplus-create
description: (WIP) Scaffold a Crestron SIMPL+ module (.usp) from a device description, with correct INPUT/OUTPUT signal structure and event handlers
argument-hint: module description
---

# Create Crestron SIMPL+ Module (WIP)

> **Status: WIP.** Compilation is wired (see **Compile & verify**); the scaffold
> logic is still being built out.

## Target
- **Language:** SIMPL+ (C-like)
- **Artifact:** `.usp` source → `.ush` compiled, used inside a SIMPL Windows program
- **Toolchain:** SIMPL+ Cross Compiler (`SPlusCC.exe`), driven by
  `scripts/crestron/compile.py`. Compilation **is** automatable on a Windows host
  with the Crestron SIMPL+ toolchain installed — see **Compile & verify** below.

## Before writing code
- Read `${CLAUDE_PLUGIN_ROOT}/reference/crestron/CRESTRON_CONSTRAINTS.md`.
- Reuse patterns from `${CLAUDE_PLUGIN_ROOT}/reference/crestron/CRESTRON_PATTERNS.md`.
- For API/behavior questions, search `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplplus/documents/`
  (delegate to an Explore subagent, per the Q-SYS `create-plugin` convention).

## To implement
- [ ] Module skeleton: `DIGITAL_INPUT`/`ANALOG_INPUT`/`STRING_INPUT` + matching outputs
- [ ] Event handlers: `CHANGE`, `PUSH`, `RELEASE`, `EVENT`
- [ ] Comms (serial/TCP) via `SOCKET` + buffer parsing where applicable
- [ ] Connection details (IP/port/credentials) as parameters, not hard-coded
- [ ] Compiles clean (0 errors) via **Compile & verify**

## Compile & verify
After writing the `.usp`, compile it to confirm it builds — do not consider the
module done until it compiles with 0 errors:

```
python "${CLAUDE_PLUGIN_ROOT}/scripts/crestron/compile.py" <path/to/module.usp> --target=series3
```

- Pick `--target` for the project's processor(s): `series2`, `series3`, `series4`
  (comma-separated for multiple, e.g. `--target=series3,series4`). Default `series4`.
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
