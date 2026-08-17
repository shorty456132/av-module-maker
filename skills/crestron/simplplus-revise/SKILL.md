---
name: simplplus-revise
description: (WIP) Review and revise an existing Crestron SIMPL+ module (.usp) — fix bugs, improve logic, and verify against SIMPL+ constraints
argument-hint: module file or directory path
---

# Revise Crestron SIMPL+ Module (WIP)

> **Status: stub.** Structure and contract only — implementation to follow.

## Before revising
- Read `${CLAUDE_PLUGIN_ROOT}/reference/crestron/CRESTRON_CONSTRAINTS.md` and
  `${CLAUDE_PLUGIN_ROOT}/reference/crestron/CRESTRON_PATTERNS.md`.
- For API/behavior questions, search `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplplus/`.

## To implement
- [ ] Audit against SIMPL+ signal/handler conventions and reserved names
- [ ] Fix bugs; preserve the module's INPUT/OUTPUT contract unless asked otherwise
- [ ] Summarize every change made
