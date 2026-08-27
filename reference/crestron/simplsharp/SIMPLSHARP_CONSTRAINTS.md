# SIMPL# Constraints

> Scope: **SIMPL# only** (C# / .NET class library compiled to `.clz` and loaded
> by SIMPL Windows as a custom module, reached through a SIMPL+ `.usp` wrapper).
> Mirrors the role of `reference/qsys/QSYS_CONSTRAINTS.md`: the hard rules and
> common pitfalls an author must know *before* writing code.
>
> Sibling targets have their own files: SIMPL+ → `../simplplus/SIMPLPLUS_CONSTRAINTS.md`,
> SIMPL# Pro → `../simplsharp-pro/SIMPLSHARP_PRO_CONSTRAINTS.md`. They are **not**
> interchangeable — different languages, toolchains, and output artifacts. Which
> target a job is: [`../SIMPLSHARP_OVERVIEW.md`](../SIMPLSHARP_OVERVIEW.md).
>
> **Sourcing note.** A rule tagged `> Source:` is verified against the API corpus
> ([`../SIMPLSHARP_API_CORPUS.md`](../SIMPLSHARP_API_CORPUS.md), searched via
> `crestron-lookup`) or the in-repo SIMPL+ corpus. Rules tagged **[convention]**
> are the established SIMPL#↔SIMPL+ boundary contract: the core boundary types
> (`SimplSharpString`, `CTimer`/`CrestronThread`, `DelegateProperty`) live in the
> base `Crestron.SimplSharp` assembly and are **not present in this Pro-skewed
> corpus** (grep-confirmed absent) — as Slice 1 already noted for `SimplSharpString`.
> They are documented here as convention, never fabricated as a corpus citation.

## Toolchain
- Language: C# (the Crestron SIMPL# subset of .NET).
- **.NET target: .NET Framework 4.7 (`net47`), 4-Series only** — **never** CF 3.5 /
  VS 2008. Full build/version rules: [`../SIMPLSHARP_COMPILATION.md`](../SIMPLSHARP_COMPILATION.md).
- Output: **`.clz`** (Crestron library archive, *not* a plain `.dll`), loaded by SIMPL
  Windows as a custom module — built with the Crestron **SIMPL# 4-Series library** template.
- Referenced from SIMPL+ by bare name (no extension, no path) — see Gotcha #6.

## Gotchas (must-know before writing a `.clz`)

These mirror the SIMPL+ "Gotchas" list in depth. Most SIMPL# failures are not
compile errors in the C# sense — they are runtime/boundary mistakes that make the
module *look* built while doing nothing, or that hang the SIMPL Windows program.
Check these first.

### 1. Target .NET Framework 4.7 (4-Series) — constrained runtime, no CF 3.5

This repo builds SIMPL# libraries against **.NET Framework 4.7 (`net47`) for
4-Series only**. Do **not** target .NET Compact Framework 3.5 or use Visual Studio
2008 (the legacy 3-Series stack), and **never install CF 3.5** — 3-Series is out of
scope. See [`../SIMPLSHARP_COMPILATION.md`](../SIMPLSHARP_COMPILATION.md) for the full
build rules.

Even on `net47` this is still a **constrained runtime** — a SIMPL# library does not
get the full desktop BCL; it runs on the control processor. Desktop-only APIs (much
of `System.Threading`, `System.Net` sockets, reflection emit, `System.Drawing`,
etc.) either aren't present or aren't supported — use the Crestron-provided
equivalents (`Crestron.SimplSharp.*`) instead of `System.*` where one exists.
Referencing an unsupported API compiles on your desktop and fails on the processor.

> **[project requirement]** `net47` + 4-Series-only + no-CF-3.5 is this repo's
> confirmed build target (see the `simplsharp-net-target` memory) — **not** a corpus
> fact. The API corpus version blocks state the *vendor* matrix (".NET Supported in
> 6.0 / .NET Compact Framework 3.5", present on ~1,395 of 1,499 files, e.g.
> `SimplSharpDeviceHelper` —
> <https://help.crestron.com/SimplSharp/html/758c5ad5-dc50-5c34-01d6-b98c90367d00.htm>);
> that matrix is Crestron's, and the CF 3.5 column is ignored here.

### 2. Cross the SIMPL+ boundary with `SimplSharpString`, not `System.String`

Serial/string values that move between the `.usp` wrapper and the C# class must
use **`SimplSharpString`**, the Crestron string type designed to marshal across
the SIMPL+ boundary — **not** `System.String`. A method meant to receive a serial
signal from SIMPL+, or a callback that feeds a serial signal back, takes/returns
`SimplSharpString`. Digital and analog signals cross as **`ushort`** (there is no
`bool`/`int` on the wire — a digital is a `ushort` that is 0 or 1).

Getting this wrong is the classic "the method never fires from SIMPL+" symptom:
the SIMPL+ compiler can't bind a public method whose signature uses types it can't
marshal, so the wrapper silently has nothing to call.

> **[convention]** `SimplSharpString` is a core `Crestron.SimplSharp` type; it is
> **not** in this Pro-skewed corpus (grep-confirmed). Marshaling-type mapping
> (digital/analog → `ushort`, serial → `SimplSharpString`) is the documented
> boundary contract carried forward from `../SIMPLSHARP_OVERVIEW.md`.

### 3. Never block the thread SIMPL+ calls in on

When SIMPL+ invokes one of the class's public methods, that call runs **on the
SIMPL+ program thread**. If the method blocks — a synchronous socket read, a
`Thread.Sleep`, a long loop, waiting on a device response — it stalls the entire
SIMPL Windows program, not just your module. Signal processing across the whole
program freezes until you return.

Rule: **return from the SIMPL+-invoked method almost immediately.** Offload any
real work — timers, retries, socket I/O, device polling — onto a Crestron timer
(`CTimer`) or worker thread (`CrestronThread`), and report results back later
through the callback properties (Gotcha #4). This is the C# analogue of the
SIMPL+ rule against blocking a `CHANGE`/`EVENT` handler.

> **[convention]** `CTimer` / `CrestronThread` are core `Crestron.SimplSharp`
> types, **not** in this Pro-skewed corpus (grep-confirmed). Use the Crestron
> primitives, not `System.Threading.Timer`/`Thread`, per Gotcha #1.

### 4. Feedback goes out **only** through delegate / callback properties

A `.clz` has no signals of its own — it cannot "set an output." The only way C#
drives a SIMPL Windows output is to invoke a **delegate-typed property** that the
`.usp` wrapper assigned at startup. The wrapper points each delegate property at
one of its own callback functions; that function is what actually writes the
output signal.

So the feedback path is always: *C# raises `MyFeedback(value)` → wrapper's
registered callback runs → wrapper sets its `DIGITAL_OUTPUT`/`ANALOG_OUTPUT`/
`STRING_OUTPUT`.* If a delegate property is null (wrapper never registered it),
invoking it does nothing — guard every callback invocation against null.

> **[convention]** SIMPL#'s `DelegateProperty`/callback mechanism is a core
> `Crestron.SimplSharp` boundary feature, **not** in this Pro-skewed corpus.
> Skeleton in [`SIMPLSHARP_PATTERNS.md`](SIMPLSHARP_PATTERNS.md).

### 5. The `.clz` has no symbol — the `.usp` wrapper is the SIMPL Windows symbol

A SIMPL# module is a **two-part deliverable**: the `.clz` **plus** a SIMPL+ `.usp`
wrapper. The `.clz` alone has no presence in SIMPL Windows — no block, no signals,
nothing to route. The `.usp` wrapper is what appears on the page; it declares the
I/O, instantiates the C# class, and marshals signals to/from it. Shipping the
`.clz` without its wrapper ships something SIMPL Windows cannot place.

The wrapper is an ordinary SIMPL+ `.usp` and is bound by **every** rule in
`../simplplus/SIMPLPLUS_CONSTRAINTS.md` — signal declaration order
(digital → analog → serial, inputs then outputs then parameters), `_SKIP_`
padding, required directives, and **CRLF line endings** (an LF-only `.usp`
silently produces a symbol with no I/O). See that file; do not restate its rules
in the `.clz`.

### 6. Reference the library by bare name — no path, no extension

In the `.usp` wrapper, pull the `.clz` in with `#USER_SIMPLSHARP_LIBRARY` (for a
library you wrote) or `#CRESTRON_SIMPLSHARP_LIBRARY` (for a Crestron-supplied one).
The argument is the **filename without the `.clz` extension**, and **relative or
absolute paths are not allowed** in the directive — the compiler searches the
project folder, the global SIMPL+ folder, then any `#INCLUDEPATH` paths.

```simplplus
#USER_SIMPLSHARP_LIBRARY "MyLibrary"   // pulls in MyLibrary.clz
```

Requires SIMPL v4.02.00+ (3-Series) / v4.14.06+ (4-Series).

> Source: `#USER_SIMPLSHARP_LIBRARY` —
> <https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Directives/_USER_SIMPLSHARP_LIBRARY.htm>
> · `#CRESTRON_SIMPLSHARP_LIBRARY` —
> <https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Directives/_CRESTRON_SIMPLSHARP_LIBRARY.htm>
> (both in-repo under `../simplplus/documents/Language_Constructs_&_Functions/Compiler_Directives/`).

### 7. Release resources on program stop — implement `IDisposable`

A SIMPL# class can outlive a single logic pass and holds real handles: sockets,
timers, worker threads, device subscriptions. Nothing reclaims them for you when
the program stops or restarts. Implement **`IDisposable`** and, in `Dispose()`,
stop timers/threads, close sockets, and unhook events — otherwise a program
restart leaks handles or leaves a socket bound and the module won't re-init
cleanly. (Crestron's own device classes follow the same contract — e.g.
`GenericBase.Dispose`.)

> Source: `GenericBaseDispose-Method` in the corpus confirms the Crestron
> `Dispose()` lifetime convention for long-lived objects (searchable via
> `crestron-lookup`). The **[convention]** part — that a SIMPL# module class
> should implement it for its own sockets/timers — is the boundary lifetime rule,
> not a corpus-specified requirement.

### 8. Analog is `ushort` (0–65535) — convert to/from engineering units

SIMPL Windows analog signals are unsigned 16-bit: **0–65535**. A percentage,
volume level, or 0–100 value must be scaled to that range before it goes back out,
and scaled from it on the way in. Crestron ships static helpers for the common
percent conversion so you don't hand-roll (and mis-round) it:

```csharp
ushort raw = SimplSharpDeviceHelper.PercentToUshort(75.0f);   // 75% -> ~49151
float pct  = SimplSharpDeviceHelper.UshortToPercent(raw);      // -> ~75.0
```

`PercentToUshort` clips to 65535 on overflow; `UshortToPercent` is the inverse.

> Source: `SimplSharpDeviceHelper.PercentToUshort` —
> <https://help.crestron.com/SimplSharp/html/a3d1f8c0-3803-8296-a560-735b8089dd27.htm>
> · `SimplSharpDeviceHelper.UshortToPercent` —
> <https://help.crestron.com/SimplSharp/html/d3fde26a-53d5-d885-395e-9e9217be6b16.htm>

## Still to document
- The full list of supported vs. unsupported `System.*` APIs on the `net47`
  4-Series runtime (the corpus records support per-member; there is no single manifest).
- `SimplSharpString` sizing/allocation limits across the boundary.
- Structured feedback (multiple related values) vs. one delegate property per signal.

_Add rules here as they are confirmed against the corpus (via `crestron-lookup`)
or the in-repo SIMPL+ corpus. Keep this file SIMPL#-only — SIMPL+ and SIMPL# Pro
rules belong in their own sibling files._
