---
name: simplsharp-revise
description: (WIP) Review and revise an existing Crestron SIMPL# library (.clz) C# project — fix bugs, improve logic, verify against SIMPL# constraints
argument-hint: project file or directory path
---

# Revise Crestron SIMPL# Library (WIP)

> **Status: stub.** Structure and contract only — implementation to follow.

## Before revising
- Confirm this is a SIMPL# job (`.clz` + `.usp` wrapper), not SIMPL# Pro:
  `${CLAUDE_PLUGIN_ROOT}/reference/crestron/SIMPLSHARP_OVERVIEW.md`.
- Read `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplsharp/SIMPLSHARP_CONSTRAINTS.md` and
  `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplsharp/SIMPLSHARP_PATTERNS.md`.
- For `Crestron.SimplSharp*` API questions, use the corpus per
  `${CLAUDE_PLUGIN_ROOT}/reference/crestron/SIMPLSHARP_API_CORPUS.md` — search via
  the `crestron-lookup` sub-agent; never bulk-load or invent a signature.

## To implement
- [ ] Audit threading, disposal, and join-mapping correctness
- [ ] Fix bugs; preserve the exposed signal contract unless asked otherwise
- [ ] Summarize every change made
