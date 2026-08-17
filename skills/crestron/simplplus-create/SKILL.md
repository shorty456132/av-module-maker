---
name: simplplus-create
description: (WIP) Scaffold a Crestron SIMPL+ module (.usp) from a device description, with correct INPUT/OUTPUT signal structure and event handlers
argument-hint: module description
---

# Create Crestron SIMPL+ Module (WIP)

> **Status: stub.** Structure and contract only — implementation to follow.

## Target
- **Language:** SIMPL+ (C-like)
- **Artifact:** `.usp` source → `.ush` compiled, used inside a SIMPL Windows program
- **Toolchain:** SIMPL Windows / SIMPL+ Cross Compiler (proprietary; compilation
  is not fully automatable here — document the manual step, don't fake it)

## Before writing code
- Read `${CLAUDE_PLUGIN_ROOT}/reference/crestron/CRESTRON_CONSTRAINTS.md`.
- Reuse patterns from `${CLAUDE_PLUGIN_ROOT}/reference/crestron/CRESTRON_PATTERNS.md`.
- For API/behavior questions, search `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplplus/`
  (delegate to an Explore subagent, per the Q-SYS `create-plugin` convention).

## To implement
- [ ] Module skeleton: `DIGITAL_INPUT`/`ANALOG_INPUT`/`STRING_INPUT` + matching outputs
- [ ] Event handlers: `CHANGE`, `PUSH`, `RELEASE`, `EVENT`
- [ ] Comms (serial/TCP) via `SOCKET` + buffer parsing where applicable
- [ ] Connection details (IP/port/credentials) as parameters, not hard-coded
