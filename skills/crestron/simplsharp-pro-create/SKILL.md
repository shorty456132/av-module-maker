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
- **No author metadata.** Do not add `<Authors>`, `<Company>`, or `<Copyright>` to the
  project, do not put a name in a file-header comment, and keep the `MyCompany.*`
  namespace placeholder unless the user supplies a real one. Never infer any of these
  from `git config` or session identity. See
  `${CLAUDE_PLUGIN_ROOT}/reference/AUTHOR_POLICY.md`.
- Confirm this is a SIMPL# Pro job (standalone `.cpz`, 4-Series/VC-4), not SIMPL#:
  `${CLAUDE_PLUGIN_ROOT}/reference/crestron/SIMPLSHARP_OVERVIEW.md`.
- Read `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplsharp-pro/SIMPLSHARP_PRO_CONSTRAINTS.md`.
- Reuse patterns from `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplsharp-pro/SIMPLSHARP_PRO_PATTERNS.md`.
- For `Crestron.SimplSharp*` SDK/API questions, use the corpus per
  `${CLAUDE_PLUGIN_ROOT}/reference/crestron/SIMPLSHARP_API_CORPUS.md` — search via
  the `crestron-lookup` sub-agent; never bulk-load or invent a signature.

## To implement
- [ ] `CrestronControlSystem` subclass + `InitializeSystem`
- [ ] Device registration and lifecycle
- [ ] `ProgramStatusEventHandler` with graceful stop
- [ ] TCP/UDP client & server, threaded receive, JSON handling
- [ ] Connection details as runtime config, not hard-coded
