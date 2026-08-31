# Extron ControlScript Reference

Reference material for building **Extron ControlScript** device modules — the
Python programming model for Extron Pro / Pro xi control processors.

## What's here

| Path | What it is |
|---|---|
| `EXTRON_OVERVIEW.md` | Platform model, hardware generations, project structure, the `extronlib` package map, and what a "device module" is on this platform. Read first. |
| `EXTRON_CONSTRAINTS.md` | Hard rules and gotchas a module author must know **before** writing code (event model, bytes vs str, blocking calls, buffer chunking). |
| `EXTRON_PATTERNS.md` | Ready-to-adapt device-module skeletons (Ethernet + Serial), buffer parsing, connection/keepalive management, and how to expose device state to the rest of a project. |
| `extronlib/<version>/` | **Vendored** ControlScript API type stubs, one tree per hardware generation (`1.8.21xi` = Pro xi, `3.13.39` = Pro / classic). Authoritative signatures + docstrings. |
| `template/` | **Vendored** ControlScript default project template — the canonical `src/` layout (`main.py`, `devices.py`, `system.py`, `control/`, `ui/`, `modules/`) plus `modules/helper/ModuleSupport.py`. |
| `snippets/` | **Vendored** VS Code snippets (`python.json`, `device-snippets.json`) — Extron's own object-instantiation and event patterns, and JSON project-descriptor device entries by part number. |

## Provenance

The vendored `extronlib/`, `template/`, and `snippets/` material is extracted from
the **Extron ControlScript Extension for VS Code** (`extron.controlscript-1.9.0-16`,
publisher `Extron`). The stubs carry Extron's own docstrings; `ModuleSupport.py`
is `Copyright 2020-2023, Extron Electronics`. This is third-party material included
for reference only — see the repo `LICENSE` scope. If this repo is distributed
publicly, confirm redistribution is acceptable or swap these for a topic→URL index
per the Q-SYS docs strategy.

## How the skills use this

The Extron scaffolding skills (planned — see `PLAN.md`) read `EXTRON_OVERVIEW.md`,
`EXTRON_CONSTRAINTS.md`, and `EXTRON_PATTERNS.md` before generating a module, and
delegate deeper API lookups to an Explore subagent over `extronlib/<version>/`.
