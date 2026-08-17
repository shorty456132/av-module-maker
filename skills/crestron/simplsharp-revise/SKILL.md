---
name: simplsharp-revise
description: (WIP) Review and revise an existing Crestron SIMPL# library (.clz) C# project — fix bugs, improve logic, verify against SIMPL# constraints
argument-hint: project file or directory path
---

# Revise Crestron SIMPL# Library (WIP)

> **Status: stub.** Structure and contract only — implementation to follow.

## Before revising
- Read `${CLAUDE_PLUGIN_ROOT}/reference/crestron/CRESTRON_CONSTRAINTS.md` and
  `${CLAUDE_PLUGIN_ROOT}/reference/crestron/CRESTRON_PATTERNS.md`.
- For API questions, search `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplsharp/`.

## To implement
- [ ] Audit threading, disposal, and join-mapping correctness
- [ ] Fix bugs; preserve the exposed signal contract unless asked otherwise
- [ ] Summarize every change made
