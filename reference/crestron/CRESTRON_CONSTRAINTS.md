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

### 4. Declare I/O signals in type order: digital → analog → serial

Top-level signal declarations **must** be grouped by direction and, within each
direction, follow a fixed type order: **digital, then analog, then serial.**
Declare **all inputs first** (in that type order), then **all outputs** (in that
same type order), and finally the **parameters**.

This order is strict and mechanically significant: the compiler relies on it to
actually build the I/O so the signals show up correctly on the symbol in SIMPL
Windows. Interleaving types — e.g. an analog input before a digital input —
causes the I/O to build wrong (or not appear as expected), not just a cosmetic
lint issue.

```simplplus
// INPUTS — digital, then analog, then serial
DIGITAL_INPUT   Enable, Reset;
ANALOG_INPUT    Level;
STRING_INPUT    Command[255];

// OUTPUTS — same type order: digital, then analog, then serial
DIGITAL_OUTPUT  Is_Online, Error_Fb;
ANALOG_OUTPUT   Level_Fb;
STRING_OUTPUT   Response;

// PARAMETERS — last
INTEGER_PARAMETER   RetryCount;
STRING_PARAMETER    DeviceName[64];
```

Overall order: **all inputs (digital → analog → serial) → all outputs (digital →
analog → serial) → parameters.** Serial inputs/outputs use `STRING_INPUT` /
`STRING_OUTPUT` (or `BUFFER_INPUT` for serial buffers).

### 5. Don't add `#SYMBOL_NAME`

`#SYMBOL_NAME` is **not** required and should be omitted. It doesn't affect the
compiled output and only causes confusion — leave it out entirely.

## Still to document per target
- Toolchain / SDK versions and how compilation is invoked (much of it is
  proprietary IDE tooling, unlike the open Q-SYS `compile.py`).
- Threading and event model constraints (esp. SIMPL# `ProgramStatusEventHandler`,
  no blocking on the main thread).
- Reserved names, join/parameter conventions, INPUT/OUTPUT signal rules (SIMPL+).
- Memory/lifetime rules, `Dispose`, and program-stop handling.
- What must be a runtime parameter vs. compile-time constant.

_Add rules here as they are confirmed against Crestron help docs._
