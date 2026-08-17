---
name: simplsharp-pro-revise
description: (WIP) Review and revise an existing Crestron SIMPL# Pro program (.cpz) C# project — fix bugs, improve logic, verify against SIMPL# Pro constraints
argument-hint: project file or directory path
---

# Revise Crestron SIMPL# Pro Program (WIP)

> **Status: stub.** Structure and contract only — implementation to follow.

## Before revising
- Read `${CLAUDE_PLUGIN_ROOT}/reference/crestron/CRESTRON_CONSTRAINTS.md` and
  `${CLAUDE_PLUGIN_ROOT}/reference/crestron/CRESTRON_PATTERNS.md`.
- For SDK/API questions, search `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplsharp-pro/`.

## To implement
- [ ] Audit control-system lifecycle, threading, and program-stop handling
- [ ] Fix bugs; preserve device/join contracts unless asked otherwise
- [ ] Summarize every change made
