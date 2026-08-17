---
name: simplsharp-create
description: (WIP) Scaffold a Crestron SIMPL# library (.clz) in C# that exposes signals to SIMPL Windows as a custom module
argument-hint: module description
---

# Create Crestron SIMPL# Library (WIP)

> **Status: stub.** Structure and contract only — implementation to follow.

## Target
- **Language:** C# (.NET, SIMPL#)
- **Artifact:** `.clz`, loaded by SIMPL Windows as a custom module
- **Toolchain:** Visual Studio + Crestron SIMPL# project template (proprietary;
  compilation is not fully automatable here — document the manual step)

## Before writing code
- Read `${CLAUDE_PLUGIN_ROOT}/reference/crestron/CRESTRON_CONSTRAINTS.md`.
- Reuse patterns from `${CLAUDE_PLUGIN_ROOT}/reference/crestron/CRESTRON_PATTERNS.md`.
- For API questions, search `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplsharp/`.

## To implement
- [ ] SIMPL# class exposing `InputSig`/`OutputSig` to SIMPL Windows
- [ ] Event-driven property glue; `ushort`/`string` join mapping
- [ ] Threading-safe comms; no blocking on the main thread
- [ ] Proper `Dispose` / program-stop handling
