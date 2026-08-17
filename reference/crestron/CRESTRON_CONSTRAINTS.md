# Crestron Constraints (WIP)

> Status: **stub** — to be populated as Crestron skills are built.
> Mirrors the role of `reference/qsys/QSYS_CONSTRAINTS.md`: the hard rules and
> common pitfalls an author must know *before* writing code for each target.

Crestron module development spans three distinct targets. They are **not**
interchangeable — different languages, toolchains, and output artifacts.

| Target        | Language            | Output  | Compiled in                                  | Runs on |
|---------------|---------------------|---------|----------------------------------------------|---------|
| SIMPL+        | SIMPL+ (C-like)     | `.usp` → `.ush` | SIMPL Windows / SIMPL+ Cross Compiler | 3-Series & 4-Series (as part of a SIMPL program) |
| SIMPL#        | C# (.NET, S#)       | `.clz`  | Visual Studio + Crestron SIMPL# template     | Loaded by SIMPL Windows as a custom module |
| SIMPL# Pro    | C# (.NET, S# Pro)   | `.cpz`  | Visual Studio + Crestron SDK / MSBuild        | 4-Series appliances, VC-4 |

## To document per target
- Toolchain / SDK versions and how compilation is invoked (much of it is
  proprietary IDE tooling, unlike the open Q-SYS `compile.py`).
- Threading and event model constraints (esp. SIMPL# `ProgramStatusEventHandler`,
  no blocking on the main thread).
- Reserved names, join/parameter conventions, INPUT/OUTPUT signal rules (SIMPL+).
- Memory/lifetime rules, `Dispose`, and program-stop handling.
- What must be a runtime parameter vs. compile-time constant.

_Add rules here as they are confirmed against Crestron help docs._
