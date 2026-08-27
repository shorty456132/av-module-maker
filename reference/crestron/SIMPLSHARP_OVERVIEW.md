# SIMPL# vs SIMPL# Pro — Which Target?

> Scope: the distinction doc for the two C#/.NET Crestron targets in this repo.
> Read this first to decide **which target a job is** before reaching for a
> `simplsharp-*` or `simplsharp-pro-*` skill. Both compile C# against the shared
> `Crestron.SimplSharp*` foundation, but they ship different artifacts, run in
> different places, and reach the program by different means — they are **not**
> interchangeable.
>
> Sibling reference for the third Crestron target (SIMPL+, the `.usp`/`.ush`
> language) lives in `simplplus/`. A SIMPL# module's wrapper half *is* a SIMPL+
> `.usp`, so the two targets overlap there — see below.

## The two targets at a glance

| | **SIMPL#** | **SIMPL# Pro** |
|---|---|---|
| Artifact | `.clz` (C# class library) | `.cpz` (standalone program) |
| Reaches the program via | A **SIMPL+ `.usp` wrapper** exposes the C# class's methods/callbacks as signals; that wrapper is the **SIMPL Windows** symbol | Nothing — it *is* the program. A `CrestronControlSystem` entry class runs directly on the appliance |
| Runs on | **4-Series** (this repo's target), inside a SIMPL Windows program | **4-Series appliances / VC-4** |
| Needs SIMPL Windows? | **Yes** — the `.clz` has no symbol of its own; the `.usp` wrapper is what appears in SIMPL Windows | **No** — there is no SIMPL Windows program at all |
| Deliverable shape | **Two parts:** `.clz` **+** a SIMPL+ `.usp` wrapper | One part: the `.cpz` |
| .NET target | **`net47`** default, 4-Series — **never** CF 3.5 (SDK also ships `net6.0`) | **`net47`** default, 4-Series (SDK also ships `net6.0`) |
| Toolchain | Modern VS + **`Crestron.SimplSharp.SDK.Library`** NuGet → `.clz` | Modern VS + **`Crestron.SimplSharp.SDK.Program`** NuGet → `.cpz` |
| In-repo skills | `simplsharp-create`, `simplsharp-revise` | `simplsharp-pro-create`, `simplsharp-pro-revise` |

## When to use which

- **The C# logic must live inside an existing SIMPL Windows program** — alongside
  SIMPL+ modules, symbols, and signal routing an integrator wired up — → **SIMPL#**.
  You are writing a reusable component that a SIMPL Windows program consumes as a
  custom module.
- **The C# program owns the whole processor** — no SIMPL Windows in the picture,
  targeting a 4-Series appliance or a VC-4 server — → **SIMPL# Pro**. You are
  writing the application itself, from its `CrestronControlSystem` entry point out.

If a scope says "custom module for a SIMPL Windows program," it's SIMPL#. If it
says "standalone program / 4-Series / VC-4 / no SIMPL Windows," it's SIMPL# Pro.

## SIMPL# = `.clz` + a `.usp` wrapper (a two-part deliverable)

A SIMPL# module is **never** just the `.clz`. The `.clz` is a plain class library
with no SIMPL Windows presence; it is a **SIMPL+ `.usp` wrapper** that gives it a
symbol and marshals SIMPL Windows signals to and from the C# class. Shipping the
`.clz` without its wrapper ships something SIMPL Windows cannot place.

The wrapper's job, by convention:

- **Call in** — SIMPL+ invokes the C# class's **public methods** (typically from
  `CHANGE`/`PUSH`/`EVENT` handlers on the wrapper's input signals).
- **Feed back** — the C# class raises **delegate / callback properties** that the
  wrapper subscribes to and drives back out onto its output signals.
- **Signal types across the boundary** — digital and analog signals marshal as
  `ushort`; serial signals marshal as `SimplSharpString` (the Crestron string type
  used across the SIMPL+ boundary, **not** `System.String`).

The wrapper half is an ordinary SIMPL+ `.usp` — so it is authored with the
existing **`simplplus-create`** skill and is bound by every rule in
`simplplus/SIMPLPLUS_CONSTRAINTS.md` (signal declaration order, `#SKIP_` padding,
CRLF line endings, etc.). Exact wrapper/callback signatures are documented and
source-traced in Slice 3 (`simplsharp/SIMPLSHARP_PATTERNS.md`).

## SIMPL# Pro = a standalone program

A SIMPL# Pro program has no wrapper and no SIMPL Windows symbol. Its entry point
is a subclass of **`CrestronControlSystem`** — "the base class for the
CrestronControlSystem; the customer application is derived over this class." The
program's lifecycle hangs off that class: the customer overrides
**`InitializeSystem()`** to register devices and set up system parameters, and the
program runs directly on a 4-Series appliance or VC-4.

> Source: `CrestronControlSystem` class, namespace `Crestron.SimplSharpPro`
> (assembly `SimplSharpPro.dll`) —
> <https://help.crestron.com/SimplSharp/html/46269246-04c5-bc22-78ed-d86613dd8bbc.htm>

Hard rules (init must not block, device-registration success checks, graceful
program-stop, IPID/registration) are documented and source-traced in Slice 4
(`simplsharp-pro/SIMPLSHARP_PRO_CONSTRAINTS.md`).

## Shared foundation

Both targets compile C# against the same **`Crestron.SimplSharp*`** namespaces —
Crestron's help site is even titled *"Crestron Simpl# and Simpl# Pro Help,"* and
the two share one API reference. The corpus skews toward `Crestron.SimplSharpPro*`
(device support, sigs, control-system classes); core types such as
`SimplSharpString` live in the base `Crestron.SimplSharp` namespace. Search the
shared API reference with the **`crestron-lookup`** sub-agent rather than
bulk-loading it — the canonical corpus pointer is `SIMPLSHARP_API_CORPUS.md`
(added in Slice 2). Never invent a signature; verify it against the corpus.

## Cross-links

| Target | Constraints | Patterns |
|---|---|---|
| SIMPL# | [`simplsharp/SIMPLSHARP_CONSTRAINTS.md`](simplsharp/SIMPLSHARP_CONSTRAINTS.md) | [`simplsharp/SIMPLSHARP_PATTERNS.md`](simplsharp/SIMPLSHARP_PATTERNS.md) |
| SIMPL# Pro | [`simplsharp-pro/SIMPLSHARP_PRO_CONSTRAINTS.md`](simplsharp-pro/SIMPLSHARP_PRO_CONSTRAINTS.md) | [`simplsharp-pro/SIMPLSHARP_PRO_PATTERNS.md`](simplsharp-pro/SIMPLSHARP_PRO_PATTERNS.md) |
| SIMPL+ (wrapper half) | [`simplplus/SIMPLPLUS_CONSTRAINTS.md`](simplplus/SIMPLPLUS_CONSTRAINTS.md) | [`simplplus/SIMPLPLUS_PATTERNS.md`](simplplus/SIMPLPLUS_PATTERNS.md) |

- API reference: `SIMPLSHARP_API_CORPUS.md` (Slice 2) → shared corpus via the
  `crestron-lookup` sub-agent.
- Build / .NET version rules: [`SIMPLSHARP_COMPILATION.md`](SIMPLSHARP_COMPILATION.md)
  → `net47`, 4-Series only, no CF 3.5; `.clz`/`.cpz` output and the `.clz`→`.usp` chain.
