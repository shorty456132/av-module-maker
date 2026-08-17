# Crestron Patterns (WIP)

> Status: **stub** — to be populated as Crestron skills are built.
> Mirrors the role of `reference/qsys/QSYS_PATTERNS.md`: ready-to-adapt
> code patterns for the most common needs, so most work needs no doc search.

## Planned pattern coverage

### SIMPL+ (`.usp`)
- Module skeleton: `DIGITAL_INPUT` / `ANALOG_INPUT` / `STRING_INPUT` and matching outputs.
- `CHANGE`, `PUSH`, `RELEASE`, `EVENT` handlers.
- Serial/TCP comms via `SOCKET` and buffer parsing.

### SIMPL# (`.clz`)
- SIMPL# class exposing InputSig/OutputSig to SIMPL Windows.
- Event-driven property glue and `ushort`/`string` join mapping.

### SIMPL# Pro (`.cpz`)
- `CrestronControlSystem` entry class + `InitializeSystem`.
- Device registration, `ProgramStatusEventHandler`, graceful stop.
- TCP/UDP client & server, threaded receive, JSON handling.

_Add confirmed patterns here, each with a `> Source:` link to the Crestron help doc it derives from._
