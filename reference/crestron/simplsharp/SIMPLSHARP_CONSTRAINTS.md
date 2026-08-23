# SIMPL# Constraints (WIP)

> Status: **stub** — to be populated as the SIMPL# skills are built.
> Scope: **SIMPL# only** (C# / .NET class libraries compiled to `.clz` and loaded
> by SIMPL Windows as a custom module). Mirrors the role of
> `reference/qsys/QSYS_CONSTRAINTS.md`: the hard rules and common pitfalls an
> author must know *before* writing code.
>
> Sibling targets have their own files: SIMPL+ → `../simplplus/SIMPLPLUS_CONSTRAINTS.md`,
> SIMPL# Pro → `../simplsharp-pro/SIMPLSHARP_PRO_CONSTRAINTS.md`. They are **not**
> interchangeable — different languages, toolchains, and output artifacts.

## Toolchain
- Language: C# (Crestron SIMPL# subset of .NET).
- Output: `.clz`, loaded by SIMPL Windows as a custom module.
- Built in: Visual Studio + the Crestron SIMPL# project template.

## Still to document
- Which .NET APIs are available vs. unsupported in the SIMPL# subset.
- Exposing `InputSig` / `OutputSig` to SIMPL Windows and join/parameter conventions.
- Threading and event model (no blocking on the signal-change thread).
- Memory/lifetime rules, `IDisposable`, and program-stop handling.
- What must be a runtime parameter vs. a compile-time constant.

_Add rules here as they are confirmed against SIMPL# help docs._
