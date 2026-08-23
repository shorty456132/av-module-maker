---
name: simplsharp-pro-create
description: (WIP) Scaffold a Crestron SIMPL# Pro program (.cpz) in C# for 4-Series appliances and VC-4, with a CrestronControlSystem entry class
argument-hint: program description
---

# Create Crestron SIMPL# Pro Program (WIP)

> **Status: stub.** Structure and contract only — implementation to follow.

## Target
- **Language:** C# (.NET, SIMPL# Pro)
- **Artifact:** `.cpz`, runs on 4-Series appliances and VC-4
- **Toolchain:** Visual Studio + Crestron SDK / MSBuild (proprietary; compilation
  is not fully automatable here — document the manual step)

## Before writing code
- Read `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplsharp-pro/SIMPLSHARP_PRO_CONSTRAINTS.md`.
- Reuse patterns from `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplsharp-pro/SIMPLSHARP_PRO_PATTERNS.md`.
- For SDK/API questions, search `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplsharp-pro/`.

## To implement
- [ ] `CrestronControlSystem` subclass + `InitializeSystem`
- [ ] Device registration and lifecycle
- [ ] `ProgramStatusEventHandler` with graceful stop
- [ ] TCP/UDP client & server, threaded receive, JSON handling
- [ ] Connection details as runtime config, not hard-coded
