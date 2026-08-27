# SIMPL+ Constraints

> Scope: **SIMPL+ only** (`.usp` → `.ush`, C-like language, INPUT/OUTPUT signal
> model, compiled by the SIMPL+ Cross Compiler inside SIMPL Windows for 3-Series
> & 4-Series). Mirrors the role of `reference/qsys/QSYS_CONSTRAINTS.md`: the hard
> rules and common pitfalls an author must know *before* writing a `.usp`.
>
> Sibling targets have their own files: SIMPL# → `../simplsharp/SIMPLSHARP_CONSTRAINTS.md`,
> SIMPL# Pro → `../simplsharp-pro/SIMPLSHARP_PRO_CONSTRAINTS.md`. They are **not**
> interchangeable — different languages, toolchains, and output artifacts.

## Gotchas (must-fix compile errors)

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

### 6. Pad I/O with `_SKIP_` so parameters don't cover signal names

On the SIMPL Windows symbol, parameters render across the **top** of the block —
directly over the first input rows (left) and first output rows (right). When a
module has both parameters and I/O, the parameter labels visually cover the
names of the topmost signals.

Fix it with the `_SKIP_` keyword, which inserts a blank gap row. `_SKIP_` is a
**graphic-only** consideration — it has no effect on the input/output
relationships of the symbol, so it never changes behavior or breaks the strict
type order in gotcha #4.

Rule: if the module has **N** parameters, prepend **N** `_SKIP_` entries to the
**first input declaration** and the **first output declaration** (i.e. the
topmost signal in each column). This drops every real signal below the parameter
block so nothing is covered. Apply it only at the top of each column — not once
per type, and not on the parameter declarations themselves.

```simplplus
// 3 parameters → 3 leading _SKIP_ on the first input and first output decl.

// INPUTS — the first (topmost) input declaration gets the padding
DIGITAL_INPUT   _SKIP_, _SKIP_, _SKIP_, Enable, Reset;
ANALOG_INPUT    Level;            // later types: no extra padding
STRING_INPUT    Command[255];

// OUTPUTS — the first (topmost) output declaration gets the padding
DIGITAL_OUTPUT  _SKIP_, _SKIP_, _SKIP_, Is_Online, Error_Fb;
ANALOG_OUTPUT   Level_Fb;
STRING_OUTPUT   Response;

// PARAMETERS — last, as always (unchanged)
INTEGER_PARAMETER   RetryCount;
STRING_PARAMETER    DeviceName[64];
STRING_PARAMETER    DeviceIp[64];
```

Notes:
- The padding goes on whichever type is **first present** in each column. If a
  module has no digital inputs, the `_SKIP_` entries lead the first analog (or
  serial) input declaration instead.
- If the module has only inputs or only outputs, pad whichever column exists.
- No parameters → no `_SKIP_` padding.

### 7. Save `.usp` with CRLF (`\r\n`) line endings, never LF-only

`SPlusCC.exe` requires DOS/Windows line endings. Given an **LF-only** `.usp`, the
compiler does **not** error — it reports `Total Error(s): 0`, writes a `.ush`, and
looks like it succeeded. But that `.ush` is a degenerate stub: it silently drops
**every** `*_INPUT` / `*_OUTPUT` / `*_PARAMETER` declaration
(`MinVariableInputs=0`, no `InputCue`/`OutputCue`/`ParamCue`, `SysRev5` pinned to
an older value). Dropped into SIMPL Windows the module shows **no I/O and no
parameters** — the classic symptom of this bug.

This bites because agent file-writers (and many editors on non-Windows hosts)
emit LF-only files. `scripts/crestron/simplplus_build.py` guards against it by normalizing
every `.usp` to CRLF (`ensure_crlf`) before invoking the compiler, so compiling
through that script is always safe. If you write or hand-edit a `.usp` any other
way, ensure it is saved CRLF before compiling.

## Still to document
- Reserved names and identifier rules beyond the ordering constraints above.
- `WAIT` / `PROCESSLOGIC` / event-reentrancy behavior and when `#ENABLE_STACK_CHECKING`
  actually trips.
- `NONVOLATILE` vs. `VOLATILE` lifetime rules across program restart.
- String/buffer sizing limits and `STRING_INPUT`/`BUFFER_INPUT` gotchas.
- What must be a `*_PARAMETER` (compile-time / symbol-time constant) vs. a signal.

_Add rules here as they are confirmed against SIMPL+ help docs
(`documents/`). Keep this file SIMPL+-only — SIMPL# and SIMPL# Pro rules belong in
their own sibling files._
