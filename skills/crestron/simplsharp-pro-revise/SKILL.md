---
name: simplsharp-pro-revise
description: (WIP) Review and revise an existing Crestron SIMPL# Pro program (.cpz) C# project — fix bugs, improve logic, verify against SIMPL# Pro constraints
argument-hint: project file or directory path
---

# Revise Crestron SIMPL# Pro Program (WIP)

> **Status: stub.** Structure and contract only — implementation to follow.

## Before revising
- **Do not touch authorship.** Leave any existing `<Authors>`/`<Company>`/namespace value
  exactly as written, and never add one — no name inferred from `git config` or session
  identity. See `${CLAUDE_PLUGIN_ROOT}/reference/AUTHOR_POLICY.md`.
- Confirm this is a SIMPL# Pro job (standalone `.cpz`, 4-Series/VC-4), not SIMPL#:
  `${CLAUDE_PLUGIN_ROOT}/reference/crestron/SIMPLSHARP_OVERVIEW.md`.
- Read `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplsharp-pro/SIMPLSHARP_PRO_CONSTRAINTS.md` and
  `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplsharp-pro/SIMPLSHARP_PRO_PATTERNS.md`.
- For `Crestron.SimplSharp*` SDK/API questions, use the corpus per
  `${CLAUDE_PLUGIN_ROOT}/reference/crestron/SIMPLSHARP_API_CORPUS.md` — search via
  the `crestron-lookup` sub-agent; never bulk-load or invent a signature.

## To implement
- [ ] Audit control-system lifecycle, threading, and program-stop handling
- [ ] Fix bugs; preserve device/join contracts unless asked otherwise
- [ ] Summarize every change made
