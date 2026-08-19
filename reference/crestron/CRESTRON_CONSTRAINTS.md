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

## SIMPL+ Gotchas (must-fix compile errors)

These are confirmed against the SIMPL+ Cross Compiler. Violating any of them
produces a compile error that is not always obvious from the message — check
these first when a `.usp` won't build.

### 1. Declare scalar variables before array declarations

Within a declaration scope, **all non-array variable declarations must come
before any array declarations.** The compiler rejects a scalar declared after
an array in the same block.

```simplplus
// WRONG — scalar after an array
INTEGER myArray[10];
INTEGER myCount;        // compile error

// RIGHT — scalars first, then arrays
INTEGER myCount;
INTEGER myArray[10];
```

### 2. Add the required directives at the top of every module

At minimum, put these three directives at the very top of the `.usp`, before any
declarations or user-defined functions (`#ENABLE_STACK_CHECKING` in particular
**must** precede all function declarations):

```simplplus
#DEFAULT_VOLATILE
#ENABLE_STACK_CHECKING
#ENABLE_TRACE
```

- `#DEFAULT_VOLATILE` — variables don't survive a program restart unless flagged
  `NONVOLATILE` (make the volatility explicit rather than relying on the default).
- `#ENABLE_STACK_CHECKING` — catches stack overflow from recursion or inputs
  arriving faster than PUSH/CHANGE/EVENT can return.
- `#ENABLE_TRACE` — enables `Trace()` output for debugging.

### 3. `propBounds` must precede `propDefaultValue`

Inside a `#BEGIN_PARAMETER_PROPERTIES … #END_PARAMETER_PROPERTIES` block, declare
`propBounds` **before** `propDefaultValue`. (Likewise, `propDefaultUnits` must
come **after** `propValidUnits`.) Out-of-order property lines are a compile error.

```simplplus
#BEGIN_PARAMETER_PROPERTIES DelayTime
propValidUnits  = unitTime | unitTicks;
propBounds      = 25s, 36s;    // bounds first
propDefaultValue = 26s;        // then default
#END_PARAMETER_PROPERTIES
```

## Still to document per target
- Toolchain / SDK versions and how compilation is invoked (much of it is
  proprietary IDE tooling, unlike the open Q-SYS `compile.py`).
- Threading and event model constraints (esp. SIMPL# `ProgramStatusEventHandler`,
  no blocking on the main thread).
- Reserved names, join/parameter conventions, INPUT/OUTPUT signal rules (SIMPL+).
- Memory/lifetime rules, `Dispose`, and program-stop handling.
- What must be a runtime parameter vs. compile-time constant.

_Add rules here as they are confirmed against Crestron help docs._
