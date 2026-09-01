---
name: simplsharp-create
description: Scaffold a Crestron SIMPL# library (.clz) in C# that exposes signals to SIMPL Windows as a custom module, with its SIMPL+ .usp wrapper
argument-hint: module description
---

# Create Crestron SIMPL# Library

A SIMPL# deliverable is **two halves**: a C# class compiled to a `.clz`, and a
SIMPL+ `.usp` wrapper that is the actual SIMPL Windows symbol. **This skill owns
the C# half** (the `.clz` and the marshaling seam) and, once the `.clz` exists,
**calls `simplplus-create`** to generate the wrapper from the built class. Build
the halves in strict order — **wrapper last** — so the wrapper provably matches
the class instead of being re-designed from prose.

## Target
- **Language:** C# (the Crestron SIMPL# subset of .NET Framework 4.7, 4-Series only).
- **Artifact:** `.clz` (a Crestron library archive, *not* a plain `.dll`), loaded by
  SIMPL Windows through its `.usp` wrapper.
- **Toolchain:** `dotnet build` / MSBuild driving the **`Crestron.SimplSharp.SDK.Library`**
  NuGet package — Visual Studio is optional, not required. Compilation **is**
  automatable: `scripts/crestron/simplsharp_build.py` chains `dotnet build` → stage
  `.clz` → compile the wrapper. See `${CLAUDE_PLUGIN_ROOT}/reference/crestron/SIMPLSHARP_COMPILATION.md`.

## Before writing code
- Confirm this is a **SIMPL#** job (`.clz` + `.usp` wrapper), not SIMPL# Pro (`.cpz`):
  `${CLAUDE_PLUGIN_ROOT}/reference/crestron/SIMPLSHARP_OVERVIEW.md`.
- Read `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplsharp/SIMPLSHARP_CONSTRAINTS.md` —
  the **Gotchas #1–8** are the hard boundary rules (`net47`/4-Series only;
  `SimplSharpString` for serial and `ushort` for digital/analog at the boundary;
  never block the SIMPL+ thread; feedback only through delegate properties;
  `IDisposable` on program stop). Apply every one.
- Reuse **Pattern 1** (the C# `.clz` class skeleton) from
  `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplsharp/SIMPLSHARP_PATTERNS.md`.
- For `Crestron.SimplSharp*` API questions, search the corpus per
  `${CLAUDE_PLUGIN_ROOT}/reference/crestron/SIMPLSHARP_API_CORPUS.md` via the
  `crestron-lookup` sub-agent — never bulk-load or invent a signature.

## Naming & layout
Derive `<Name>` in **PascalCase** from the module description. The deliverable is
**two sibling folders** — the C# project and (later) its wrapper — so the build
command's paths line up:

```
<Name>/
  <Name>/<Name>.csproj          + <Name>Controller.cs   ← this skill (the .clz half)
  <Name>Wrapper/<Name>Wrapper.usp                        ← later, via simplplus-create
```

- Namespace: `MyCompany.<Name>` · class: `<Name>Controller` · library/`.clz` name:
  `<Name>` · wrapper: `<Name>Wrapper.usp`.
- The `#USER_SIMPLSHARP_LIBRARY` directive resolves the `.clz` by **bare name**, so
  the library file must be named `<Name>.clz` (Constraint #6). The build script stages
  it next to the `.usp` for you.

## Step 1 — Write the C# class (`<Name>Controller.cs`)
Author the class straight from **Pattern 1** (`SIMPLSHARP_PATTERNS.md`), adapting its
method/delegate set to the device description. The class surface **is the contract**
the wrapper will mirror in Step 3, so make the boundary explicit:

- **Public methods = the call-in surface.** One per input signal. Digital/analog
  args are `ushort`; serial args are `SimplSharpString` (Gotcha #2). Each must return
  fast — offload real work to a `CTimer`/`CrestronThread`, never block (Gotcha #3).
- **Delegate-typed properties = the only feedback path.** One per output signal; the
  class invokes them (null-guarded), the wrapper drives the signals (Gotcha #4).
- **Parameterless constructor** so SIMPL+ can declare the instance.
- **`IDisposable`**: stop timers/threads and null the callbacks in `Dispose` (Gotcha #7).

For the trivial smoke-test device (1 digital-in `Power`, 1 serial-in `Command`,
1 digital-out `IsOnline`): one public `Power(ushort)`, one public
`Command(SimplSharpString)`, one `IsOnlineFeedback` delegate property — exactly the
shape of Pattern 1.

## Step 2 — Write the project file (`<Name>.csproj`)
Hand-author a **minimal SDK-style** `.csproj` — do **not** depend on a `dotnet new`
template. The Crestron SDK injects the 4-Series plumbing on the first `dotnet build`;
you only declare the target framework and the SDK package:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net47</TargetFramework>
    <DebugType>portable</DebugType>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Crestron.SimplSharp.SDK.Library" Version="2.21.*" />
  </ItemGroup>
</Project>
```

- `net47` + `Crestron.SimplSharp.SDK.Library` is what makes the build emit a `.clz`
  (not just a `.dll`); a plain `Microsoft.NET.Sdk` project with no SDK package is the
  genuine failure the build script catches. See `SIMPLSHARP_COMPILATION.md`.
- `DebugType = portable` per the SDK build rules (no `pdb2mdb` step).

At this point the C# half exists on disk in the two-sibling layout, ready to build.

## Step 3 — Build the `.clz` (standalone)
Build the project on its own **before** the wrapper exists — this proves the class
compiles and produces the `.clz` the wrapper will bind to. The orchestrator needs
the `.usp` to exist, so this first build is a plain `dotnet build` (the orchestrator
runs in Step 5, once the wrapper is generated):

```
dotnet build <Name>/<Name>.csproj -c Debug
```

- **Verify the `.clz` on disk, not the build log.** MSBuild prints its primary output
  as `<Name> -> …\bin\Debug\net47\<Name>.dll` — the **`.clz` never appears in that
  line**; the Crestron SDK target emits it as a side artifact in the *same* folder.
  Confirm the build by listing for it:

  ```
  ls <Name>/bin/Debug/net47/<Name>.clz
  ```

  A `.clz` (a ~MB Crestron archive) beside the `.dll` = success. A build that reports
  success but leaves **only a `.dll`** is the genuine failure — the SDK target didn't
  run (wrong package, or a plain `Microsoft.NET.Sdk` project). See
  `SIMPLSHARP_COMPILATION.md` (the "`-> .dll` decoy").
- **On success:** the class is proven to compile; keep the `.clz` path — Step 4 derives
  the wrapper's signal spec from this built class.
- **If `dotnet` / the SDK is missing** (`dotnet` not found, or restore of
  `Crestron.SimplSharp.SDK.Library` fails): do **not** report the module broken. The
  C# files are correct and already written — hand the user the `dotnet build` command
  above and note that the .NET SDK is required (`dotnet` on PATH; the SDK package
  restores from nuget.org). This mirrors `simplplus-create`'s graceful
  toolchain-missing fallback.

## Step 4 — Derive the signal spec from the built class, then invoke `simplplus-create`
**Hard rule (Decision 5): the wrapper is generated only now — after the `.clz` exists.**
The built class is the **source of truth**; the wrapper is derived from it, never
re-designed from the prose description. This prevents the two halves drifting apart.

**Derive the spec mechanically from the class surface** — each public member maps to
exactly one signal:

| Class member | → Signal | Direction | Marshal type |
|---|---|---|---|
| public **method**, `ushort` param | input | digital **or** analog (by Step-1 intent) | `ushort` |
| public **method**, `SimplSharpString` param | input | serial | `SimplSharpString` |
| public **delegate property**, `ushort` param | output | digital **or** analog (by intent) | `ushort` |
| public **delegate property**, `SimplSharpString` param | output | serial | `SimplSharpString` |

- **Direction is unambiguous:** methods = inputs (call-in), delegate properties =
  outputs (feedback). **Names** carry over — method name → input signal name; delegate
  property name with any `Report`/`Feedback` affix stripped → output signal name
  (e.g. `ReportIsOnline` → `IsOnline`).
- **`ushort` is digital *or* analog** — the type alone can't tell you (a digital is a
  `ushort` that is 0/1). Tag each from the Step-1 design intent (on/off/momentary =
  digital; level/value 0–65535 = analog). This is the one non-mechanical judgment.
- Order the spec the way SIMPL+ requires: inputs **digital → analog → serial**, then
  outputs in the same order, then any parameters.

For the trivial device the derived spec is:

| Signal | SIMPL+ decl | Class member |
|---|---|---|
| `Power` | `DIGITAL_INPUT` | `Power(ushort)` |
| `Command` | `STRING_INPUT` | `Command(SimplSharpString)` |
| `IsOnline` | `DIGITAL_OUTPUT` | `ReportIsOnline` delegate property |

**Invoke `simplplus-create`** with that spec to emit `<Name>Wrapper/<Name>Wrapper.usp`.
`simplplus-create` owns the SIMPL+ rules (I/O type order, required directives, `_SKIP_`
padding, CRLF); tell it this is a **SIMPL# wrapper following Pattern 2** in
`SIMPLSHARP_PATTERNS.md`, so it also emits the SIMPL#-specific glue:

- `#USER_SIMPLSHARP_LIBRARY "<Name>"` — binds `<Name>.clz` by **bare name** (Constraint #6).
- A class-instance declaration: `<Name>Controller device;`.
- One `CHANGE` handler per input signal, passing the signal straight to the matching
  public method: `CHANGE Power { device.Power(Power); }`.
- One `CALLBACK FUNCTION` per output signal that writes the output, plus a
  `RegisterDelegate(device, <DelegateProperty>, <Callback>)` for it in `Main()` — the
  only path C# feedback reaches a signal (Constraint #4).

**Verify the wrapper matches the class:** every public method has a `CHANGE` handler
that calls it; every delegate property is `RegisterDelegate`d to a `CALLBACK FUNCTION`;
signal names and marshal types line up with the spec table. If they don't, fix the
wrapper (or the derivation) — a wrapper that doesn't mirror the class silently produces
a symbol that does nothing.

> **Compile the wrapper through the orchestrator, not on its own.** `simplplus-create`'s
> own "Compile & verify" step compiles a standalone `.usp` — skip that here. This wrapper
> references `<Name>.clz`, which isn't beside it yet, so a standalone compile fails on
> library resolution. Staging the `.clz` and compiling the wrapper is Step 5's job.

## Step 5 — Build the full deliverable with the orchestrator
Now that both halves exist, chain them into one placeable SIMPL Windows symbol with the
build orchestrator — it rebuilds the `.clz`, **stages it beside the `.usp`** (so the
bare-name `#USER_SIMPLSHARP_LIBRARY` resolves), and compiles the wrapper:

```
python "${CLAUDE_PLUGIN_ROOT}/scripts/crestron/simplsharp_build.py" \
    <Name>/<Name>.csproj <Name>Wrapper/<Name>Wrapper.usp
```

The module is **not done until this exits 0.** Read the step lines it prints:

- **`[OK] SIMPL# build` (exit 0):** done — report the `.clz` path and the staged copy
  beside the wrapper. Phase complete.
- **`[FAIL] simplplus … ERROR <code> (Line <n>) …`:** a wrapper/boundary error. Common
  cause — a **method or signal name that collides with a SIMPL+ reserved word**
  (e.g. naming a method `Command` yields `ERROR 1000 'COMMAND' already defined` in the
  generated header; Pattern 1 uses `SendCommand` for exactly this reason). Rename the
  offending member in the class, rebuild, and re-run. Fix and repeat until clean.
- **`[FAIL] locate-clz … only a .dll?`:** the SDK target didn't run — check the `.csproj`
  references `Crestron.SimplSharp.SDK.Library` and targets `net47` (Step 2).
- **If the script prints `SIMPL+ compiler not found`:** the Crestron SIMPL+ toolchain
  isn't installed on this host. Do **not** report the module broken — the `.clz` built
  and the wrapper is written and staged; hand the user the `simplsharp_build.py` command
  above and tell them to install the compiler via the Crestron Master Installer (or point
  `--compiler=<path>` / the `SPLUSCC` env var at `SPlusCC.exe`). Same graceful fallback as
  `simplplus-create`.

**Deliverable:** the `.clz` (in `bin/Debug/net47/`) **and** its `<Name>Wrapper.usp`
(with the staged `.clz` beside it) — the two-part SIMPL# module, proven to build clean.

## Ralph Loop Mode (optional — for long or unattended builds)

For a large module, or when the user wants the build to run autonomously, do not
write both halves in one session. Instead **emit a `TODO.md` board** and hand off
to the raw Ralph loop, which builds one card per fresh-context pass. The full
contract is `${CLAUDE_PLUGIN_ROOT}/reference/RALPH_TODO.md`; the board engine is
`${CLAUDE_PLUGIN_ROOT}/scripts/ralph/board.py`.

Use this mode when the user asks for a Ralph loop / TODO.md / unattended build.
Otherwise build inline as usual (Steps 1–5 above).

**To emit the board**, translate Steps 1–5 into one card per stage,
dependency-ordered, and write `TODO.md` into the module directory **before**
writing any C# or wrapper files — its shape is defined in the contract doc. The
card list mirrors the two-half deliverable's strict build order (**wrapper last**,
after the `.clz` exists — Decision 5):

1. `controller-class` — `<Name>Controller.cs` from Pattern 1 (Step 1).
2. `csproj` — `<Name>.csproj` (SDK-style, `net47` + `SDK.Library`) (Step 2). Depends: `controller-class`.
3. `clz-build` — standalone `dotnet build`; confirm `<Name>.clz` on disk (Step 3). Depends: `csproj`.
4. `wrapper` — derive the signal spec from the built class, invoke `simplplus-create` to emit `<Name>Wrapper.usp` (Step 4). Depends: `clz-build`.
5. **final card `build`** — the orchestrator verify gate (Step 5). Depends: `wrapper`.

Because a loop pass has only `TODO.md` + the files on disk as memory, fold the
SIMPL# hard constraints **into the card specs** so a cold pass cannot violate
them (see `SIMPLSHARP_CONSTRAINTS.md`):

- **`controller-class` card** must state the boundary marshal types (`ushort` for
  digital/analog, `SimplSharpString` for serial — Gotcha #2), the never-block rule
  (Gotcha #3), feedback-only-through-delegate-properties (Gotcha #4), the
  parameterless constructor, and `IDisposable` cleanup (Gotcha #7). Its `Spec` must
  name the module's public methods and delegate properties, because that surface
  **is** the contract the `wrapper` card derives from — a cold pass must know it
  without reading another card.
- **`csproj` card** must state `net47` + `Crestron.SimplSharp.SDK.Library` +
  `DebugType portable` — the exact combination that makes the build emit a `.clz`
  (a plain `Microsoft.NET.Sdk` project that leaves only a `.dll` is the genuine
  failure the build catches).
- **`clz-build` card** must state that success is the **`.clz` on disk**, not the
  MSBuild `-> .dll` line (which never names the `.clz`) — the card verifies by
  listing for `<Name>/bin/Debug/net47/<Name>.clz`.
- **`wrapper` card** must state that the spec is derived **mechanically from the
  built class** (methods → inputs, delegate properties → outputs), that it invokes
  `simplplus-create` for the SIMPL+ rules + Pattern 2 glue
  (`#USER_SIMPLSHARP_LIBRARY`, instance decl, one `CHANGE` per input, `CALLBACK
  FUNCTION` + `RegisterDelegate` per output), and that it must **not** compile the
  wrapper standalone (the `.clz` isn't staged beside it yet — that's the `build`
  card's job).

The **`wrapper` card must `Depends: clz-build`** so the loop can never surface the
wrapper before the `.clz` exists — this is what keeps the wrapper derived from the
built class instead of re-guessed from prose.

The **final card is the verify gate** — its `Verify gate:` header line and the
card's command are:

```
python "${CLAUDE_PLUGIN_ROOT}/scripts/crestron/simplsharp_build.py" ./<Name>/<Name>/<Name>.csproj ./<Name>/<Name>Wrapper/<Name>Wrapper.usp
```

Do any protocol/command discovery **before** emitting the board and fold the
confirmed commands into the `controller-class` card spec, so each card is
self-contained. Then start the loop (from Git Bash on Windows):

```
scripts/ralph/ralph-module-loop.sh ./<Name>/
```
