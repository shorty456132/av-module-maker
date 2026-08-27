# SIMPL# / SIMPL# Pro Compilation & .NET Target — Build Rules

> Scope: the **single source of truth** for how the two C# Crestron targets are
> **built**, what **.NET version** they compile against, and what **artifact** each
> produces. Both `simplsharp/SIMPLSHARP_CONSTRAINTS.md` and
> `simplsharp-pro/SIMPLSHARP_PRO_CONSTRAINTS.md` point here for the build/version
> rules instead of restating them.
>
> Sibling references: [`SIMPLSHARP_OVERVIEW.md`](SIMPLSHARP_OVERVIEW.md) decides
> *which target* a job is; [`SIMPLSHARP_API_CORPUS.md`](SIMPLSHARP_API_CORPUS.md) is
> *where the API docs are*. This file is *how the thing is compiled*.

## The hard build rules (this repo)

**These are project requirements, not corpus facts.** Our operative rules:

| Rule | Value |
|---|---|
| **.NET target** | **`net47` (default)** for both SIMPL# and SIMPL# Pro. The current SDK **also** ships **`net6.0`** for 4-Series/VC (see below) — supported, but not this repo's default. |
| **Processor target** | **4-Series only** (appliances / VC-4) |
| **3-Series** | **Out of scope.** Do not target it. |
| **.NET Compact Framework 3.5** | **Never.** Do not target it, and **never try to install CF 3.5.** |
| **Visual Studio 2008** | **Never.** It is the legacy 3-Series/CF-3.5 toolchain — obsolete here. |
| **Build tool** | **`dotnet build` / MSBuild** driving the Crestron **`Crestron.SimplSharp.SDK.*`** NuGet packages (below). **Visual Studio is optional, not required** — it only wraps the same MSBuild + SDK targets. No VS 2008, no CF-3.5 extension. |

> **[project requirement]** `net47` + 4-Series-only + no-CF-3.5 is this repo's
> **default** build environment (see the `simplsharp-net-target` memory). Never
> present it as a corpus-cited fact.
>
> **[SDK fact, confirmed 2026-08]** The current official SDK (`Crestron.SimplSharp.SDK.*`
> v2.21.274, updated 2026-07) targets **both `net6.0` and `net47`** for 4-Series/VC —
> `net6.0` is a *real, current, supported* target, **not** the old vendor-matrix
> "6.0 / CF 3.5" line the corpus records (that older matrix, with its CF-3.5 half, is
> still correctly ignored). We stay on `net47` by choice; `net6.0` is available if the
> default is ever revisited.

## The SDK — Crestron.SimplSharp.SDK.* NuGet packages

The 4-Series C# toolchain is delivered as **NuGet packages** (this is the modern
replacement for the old VS extension / SIMPL# 4-Series project templates). Three
packages, each producing a different artifact:

| NuGet package | Verbatim purpose (package README) | Artifact | Our target |
|---|---|---|---|
| **`Crestron.SimplSharp.SDK.Library`** | "create a C# Library you can include and **link in SIMPL+**" → "creates a larger **CLZ**" | **`.clz`** | **SIMPL#** |
| **`Crestron.SimplSharp.SDK.Program`** (→ ProgramLibrary → Library) | the C# **Program** that runs on 4-Series / Virtual Control (from a `CrestronControlSystem` entry class) | **`.cpz`** | **SIMPL# Pro** |
| **`Crestron.SimplSharp.SDK.ProgramLibrary`** (→ Library) | a C# **Library for use inside a Crestron C# Program** (referenced by a Pro program, **not** SIMPL+) | class library (`.dll`) linked into a `.cpz` | — (Pro helper lib; no dedicated skill) |

- All three list TFMs **`net6.0`** and **`net47`**; no external NuGet dependencies
  beyond the package chain shown above.
- The `.SDK.Program` and `.SDK.Library` package names are the confirmed answer to the
  old "which SDK/template" open question — reference the correct package by target.

## `.csproj` / build behavior (SDK-managed)

- **The SDK edits your `.csproj` on first build** to add the 4-Series processor
  plumbing — you do not hand-author that plumbing.
- Set the project's **Debug Type = `Portable`** (the `pdb2mdb` post-build step is no
  longer used).
- A build warning **`The target 'ResolveSDKReferences' does not exist in the project`**
  is benign — it clears on rebuild.

### Building from the command line (no Visual Studio) — **confirmed 2026-08**

`dotnet build` (or `dotnet restore` + `dotnet build`) on the SDK-style `.csproj`
produces the `.clz`. Reproduced against `Crestron.SimplSharp.SDK.Library` v2.21.x
targeting `net47` — restore and build both exit 0 and emit a valid, loadable `.clz`.

```sh
dotnet build src/PresetStore/PresetStore.csproj -c Debug
ls  bin/Debug/net47/PresetStore.clz     # the artifact (dir on PowerShell)
```

> **The `-> .dll` decoy (why a good build looks like a failure).** MSBuild's
> console prints its *primary* output — `PresetStore -> …\bin\Debug\net47\PresetStore.dll`.
> The **`.clz` never appears in that log line**; the Crestron SDK target emits it as a
> side artifact into the **same `bin\Debug\net47\` folder**. Watching the log for the
> string "clz" and seeing only ".dll" is *not* a failed build — the `.clz` is sitting
> right beside the `.dll`. Always confirm by listing the folder, not by reading the log.
>
> A real `.clz` is a ~MB **zip archive** containing the compiled assembly, the
> `SimplSharp*Interface.dll` set, **and `SimplSharpData.dat` / `.der`** (the signed
> metadata SIMPL Windows reads to discover the class's public API). A bare `.dll` with
> no `.clz` next to it is the genuine failure — it means the SDK target did not run
> (wrong package, or a plain `Microsoft.NET.Sdk` project with no SDK.Library reference).

> Sources (Crestron_Electronics, nuget.org):
> [SDK.Library](https://www.nuget.org/packages/Crestron.SimplSharp.SDK.Library/) ·
> [SDK.Program](https://www.nuget.org/packages/Crestron.SimplSharp.SDK.Program) ·
> [SDK.ProgramLibrary](https://www.nuget.org/packages/Crestron.SimplSharp.SDK.ProgramLibrary/)

## Artifacts — what each target compiles to

| Target | Project template | Output artifact | How it reaches a program |
|---|---|---|---|
| **SIMPL#** | Crestron SIMPL# **4-Series library** | **`.clz`** (Crestron library archive — *not* a plain `.dll`) | A SIMPL+ `.usp` **wrapper** references the `.clz`; that wrapper is the SIMPL Windows symbol |
| **SIMPL# Pro** | Crestron SIMPL# Pro (4-Series) | **`.cpz`** (standalone program) | It *is* the program — a `CrestronControlSystem` entry class runs on the appliance |

## The `.clz` → SIMPL Windows chain (SIMPL# only)

The point the whole SIMPL# target hinges on: **a library that will be used in SIMPL
Windows must compile to a `.clz`** so SIMPL+ can reach it. The chain is:

1. **Build** the SIMPL# library project (4-Series template, `net47`) → it packages the
   compiled assembly into a **`.clz`**. A plain `.dll` is *not* consumable by SIMPL+.
2. The **`.clz` has no SIMPL Windows symbol of its own** — it cannot be placed on a page.
3. A SIMPL+ **`.usp` wrapper** pulls the `.clz` in by **bare name**:
   `#USER_SIMPLSHARP_LIBRARY "MyLibrary"` (no path, no `.clz` extension).
4. That **`.usp` compiles into the SIMPL Windows symbol** and marshals signals ↔ the
   C# class (public methods in; delegate/callback properties out; `ushort` for
   digital/analog, `SimplSharpString` for serial).

So a SIMPL# deliverable is **always two parts**: the `.clz` **+** its `.usp` wrapper.
The deep rules for that boundary — reference directive, marshaling types, non-blocking,
`IDisposable` — live in
[`simplsharp/SIMPLSHARP_CONSTRAINTS.md`](simplsharp/SIMPLSHARP_CONSTRAINTS.md)
(Gotchas #2–#7) and the skeletons in
[`simplsharp/SIMPLSHARP_PATTERNS.md`](simplsharp/SIMPLSHARP_PATTERNS.md).

> Source: `#USER_SIMPLSHARP_LIBRARY` directive (bare-name, no path) —
> <https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Directives/_USER_SIMPLSHARP_LIBRARY.htm>
> (in-repo: `simplplus/documents/Language_Constructs_&_Functions/Compiler_Directives/_USER_SIMPLSHARP_LIBRARY.md`).

## "Compiled correctly" — how to sanity-check

- **SIMPL# library:** the build produces a **`.clz`** (not just a `.dll`), targeting
  **`net47`**. Confirm by **listing `bin\Debug\net47\` for the `.clz`** — do *not* trust
  the MSBuild `-> …\.dll` log line (see the `-> .dll` decoy above). If SIMPL+ can't
  resolve `#USER_SIMPLSHARP_LIBRARY "Name"`, the `.clz` isn't on the search path
  (project folder → global SIMPL+ folder → `#INCLUDEPATH`) — it is **not** a
  path/extension issue in the directive (bare name only).
- **SIMPL# Pro:** the build produces a **`.cpz`** for 4-Series.
- **Wrong runtime symptom:** a `net47`/4-Series mismatch, or an API that only exists
  on desktop .NET, compiles on the workstation and **fails on the processor** — keep
  to the constrained BCL and Crestron primitives (per the constraints files).

## Building the full deliverable in one command — `simplsharp_build.py`

The chain is **two toolchains**: the `.clz` is built by `dotnet build`; the `.usp`
wrapper is compiled by `SPlusCC.exe` (via `scripts/crestron/simplplus_build.py`).
**`scripts/crestron/simplsharp_build.py`** orchestrates both so you don't run — or
mis-order — them by hand:

```sh
python scripts/crestron/simplsharp_build.py <project.csproj> <wrapper.usp>
```

It runs, stopping at the first failure: **1)** `dotnet build` → **2)** locate the
`.clz` on disk (this is what catches the `-> .dll` decoy — a build that emits only a
`.dll` fails here, not silently) → **3)** copy the `.clz` beside the `.usp` so
`#USER_SIMPLSHARP_LIBRARY "Name"` resolves by bare name → **4)** `SPlusCC.exe`
compile the wrapper. Targets **`series4`** by default (SIMPL# is `net47`/4-Series
only), reuses `simplplus_build.py`'s CRLF-normalization and error parsing, and exits non-zero
if any step fails. Verified end-to-end (2026-08): a clean run produces the `.clz`,
stages it, and compiles the `.usp` to a `.ush` with full I/O.

## Still to document
- Full `net47` `.csproj` shape *after* the SDK's first-build rewrite (target framework,
  package references, output type) — capture a real post-build `.csproj` as the sample.
- Any signing / packaging / output-path conventions for shipping the `.clz`/`.cpz`.

_Confirmed build requirements land here; keep vendor-matrix (corpus) facts separate
from this repo's project requirements._
