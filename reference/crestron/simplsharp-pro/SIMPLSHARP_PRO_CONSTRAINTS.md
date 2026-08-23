# SIMPL# Pro Constraints (WIP)

> Status: **stub** — to be populated as the SIMPL# Pro skills are built.
> Scope: **SIMPL# Pro only** (full C# / .NET programs compiled to `.cpz` for
> 4-Series appliances and VC-4). Mirrors the role of
> `reference/qsys/QSYS_CONSTRAINTS.md`: the hard rules and common pitfalls an
> author must know *before* writing code.
>
> Sibling targets have their own files: SIMPL+ → `../simplplus/SIMPLPLUS_CONSTRAINTS.md`,
> SIMPL# → `../simplsharp/SIMPLSHARP_CONSTRAINTS.md`. They are **not**
> interchangeable — different languages, toolchains, and output artifacts.

## Toolchain
- Language: C# (Crestron SIMPL# Pro / .NET).
- Output: `.cpz`, runs on 4-Series appliances and VC-4.
- Built in: Visual Studio + the Crestron SDK / MSBuild.

## Still to document
- `CrestronControlSystem` entry class rules and `InitializeSystem` constraints.
- Threading and event model — `ProgramStatusEventHandler`, no blocking on the
  main thread.
- Device registration lifecycle, `Register()` return handling.
- Memory/lifetime rules, `IDisposable`, and graceful program-stop handling.
- What must be a runtime parameter vs. a compile-time constant.

_Add rules here as they are confirmed against SIMPL# Pro help docs / SDK reference._
