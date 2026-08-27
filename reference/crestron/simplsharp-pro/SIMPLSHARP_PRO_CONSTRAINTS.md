# SIMPL# Pro Constraints

> Scope: **SIMPL# Pro only** (full C# / .NET programs compiled to `.cpz` and run
> standalone on 4-Series appliances and VC-4 — a `CrestronControlSystem` entry
> class, **no SIMPL Windows and no `.usp` wrapper**). Mirrors the role of
> `reference/qsys/QSYS_CONSTRAINTS.md`: the hard rules and common pitfalls an
> author must know *before* writing code.
>
> Sibling targets have their own files: SIMPL+ → `../simplplus/SIMPLPLUS_CONSTRAINTS.md`,
> SIMPL# → `../simplsharp/SIMPLSHARP_CONSTRAINTS.md`. They are **not**
> interchangeable — different languages, toolchains, and output artifacts. Which
> target a job is: [`../SIMPLSHARP_OVERVIEW.md`](../SIMPLSHARP_OVERVIEW.md).
>
> **Sourcing note.** A rule tagged `> Source:` is verified against the API corpus
> ([`../SIMPLSHARP_API_CORPUS.md`](../SIMPLSHARP_API_CORPUS.md), searched via
> `crestron-lookup`). This corpus is **skewed toward `Crestron.SimplSharpPro`**
> (the control-system and device classes), so the core Pro lifecycle types —
> `CrestronControlSystem`, `InitializeSystem`, `GenericDevice.Register`, the
> registration-response enum — **are** present and cited here. Rules tagged
> **[convention]** cover behaviour whose types live in the base
> `Crestron.SimplSharp` assembly (the program-status handler / `CrestronEnvironment`,
> `CrestronThread`, sockets, `eControlMethod`) which is **not** in this corpus
> (grep-confirmed absent) — documented as the established SIMPL# Pro contract,
> never fabricated as a corpus citation (the Slice 1 / Slice 3 precedent).

## Toolchain
- Language: C# (Crestron SIMPL# Pro / .NET).
- **.NET target: .NET Framework 4.7 (`net47`), 4-Series only** — **never** CF 3.5 /
  VS 2008. Full build/version rules: [`../SIMPLSHARP_COMPILATION.md`](../SIMPLSHARP_COMPILATION.md).
- Output: `.cpz`, runs **standalone** on 4-Series appliances / VC-4 — there is no
  SIMPL Windows program and no SIMPL+ wrapper (contrast SIMPL# → Gotcha #1).
- Built in: a modern Visual Studio (not VS 2008) with the Crestron SIMPL# Pro
  (4-Series) project template / MSBuild.
- Entry point: a class that derives from `CrestronControlSystem` (Gotcha #2).

## Gotchas (must-know before writing a `.cpz`)

These mirror the SIMPL+ and SIMPL# "Gotchas" lists in depth. Most SIMPL# Pro
failures are not C# compile errors — they are lifecycle/registration mistakes that
make the program *look* loaded while no device responds, or that hang the processor
at startup. Check these first.

### 1. There is no SIMPL Windows and no `.usp` — the program is the whole deliverable

A SIMPL# Pro program is **standalone**. Unlike a SIMPL# `.clz` (which has no symbol
and is reached through a SIMPL+ `.usp` wrapper), a `.cpz` loads and runs on its own:
your `CrestronControlSystem` subclass **is** the program. There are no SIMPL Windows
signals, no `_SKIP_` padding, no CRLF-`.usp` rules — none of the SIMPL#/SIMPL+
boundary machinery applies. Everything (device I/O, logic, feedback, network) is C#
inside the program. If a job needs to drop into an existing SIMPL Windows page, it is
a **SIMPL#** job, not SIMPL# Pro — see [`../SIMPLSHARP_OVERVIEW.md`](../SIMPLSHARP_OVERVIEW.md).

> Source: `CrestronControlSystem` class — "Base class for the CrestronControlSystem.
> The Customer application is derived over this class." Namespace
> `Crestron.SimplSharpPro`, assembly `SimplSharpPro.dll`.
> <https://help.crestron.com/SimplSharp/html/46269246-04c5-bc22-78ed-d86613dd8bbc.htm>

### 2. Target .NET Framework 4.7 (4-Series) — constrained runtime, no CF 3.5

This repo builds SIMPL# Pro programs against **.NET Framework 4.7 (`net47`) for
4-Series only** (appliances / VC-4). Do **not** target .NET Compact Framework 3.5 or
use Visual Studio 2008, and **never install CF 3.5** — 3-Series is out of scope. See
[`../SIMPLSHARP_COMPILATION.md`](../SIMPLSHARP_COMPILATION.md) for the full build rules.

Even on `net47` this is still a **constrained runtime** — the program runs on the
appliance, not desktop .NET, so only a subset of the BCL is available. Prefer the
Crestron-provided primitives (`Crestron.SimplSharp.*` — `CrestronConsole`,
`CrestronThread`, `CTimer`, the Crestron socket classes) over their `System.*`
equivalents; a desktop-only API compiles on your workstation and fails on the appliance.

> **[project requirement]** `net47` + 4-Series-only + no-CF-3.5 is this repo's
> confirmed build target (see the `simplsharp-net-target` memory) — **not** a corpus
> fact. The API corpus version blocks state the *vendor* matrix (".NET Supported in
> 6.0 / .NET Compact Framework 3.5", e.g. the `CrestronControlSystem` page —
> <https://help.crestron.com/SimplSharp/html/46269246-04c5-bc22-78ed-d86613dd8bbc.htm>);
> that matrix is Crestron's, and the CF 3.5 column is ignored here.

### 3. `InitializeSystem()` must not block — offload real work to a thread

`InitializeSystem()` is the override where "the customer initializes their devices
and other system parameters." It runs during program start; **it is not the place for
slow work.** Blocking it — waiting on a socket connect, a device handshake, a
`Thread.Sleep`, or a long registration loop that stalls — delays or hangs program
startup. Do the fast, in-process work here (construct devices, register them, hook
events) and push anything that waits on the outside world (connecting to a device,
polling, retries) onto a worker thread (`CrestronThread`) or timer (`CTimer`), then
handle results in the callback.

> Source: `CrestronControlSystem.InitializeSystem` method — "Function for the customer
> to initialize their devices and other system parameters."
> <https://help.crestron.com/SimplSharp/html/ac434802-044e-8e4a-6c8a-3e03bee48d94.htm>
> **[convention]** The non-blocking rule and the `CrestronThread`/`CTimer` offload are
> the runtime contract (those types are base `Crestron.SimplSharp`, absent from this
> corpus) — the same "never block the lifecycle thread" rule as SIMPL# Gotcha #3.

### 4. Register every device — and check the return before you use it

Constructing a device object does **not** put it on the bus. You must call
`Register()` on it, and `Register()` returns an
**`eDeviceRegistrationUnRegistrationResponse`** — it does not throw on the common
failures. Check for `.Success` before treating the device as usable; anything else
(`Failure`, `Incompatible`, `IntegerParameterNotSet`, `NotLicensed`, …) means the
device is not live and calling it will do nothing or fault. This is the #1 SIMPL#
Pro pitfall: the program loads, but a device that never registered silently ignores
every command.

```csharp
if (myDevice.Register() != eDeviceRegistrationUnRegistrationResponse.Success)
    ErrorLog.Error("Register failed for MyDevice: {0}", myDevice.RegistrationFailureReason);
```

Registration must generally happen **inside `InitializeSystem()`** (Gotcha #3), and a
port/child device cannot register while its parent is registered — unregister the
parent first (`ParentRegistered`).

> Source: `GenericDevice.Register` — `public override
> eDeviceRegistrationUnRegistrationResponse Register()` —
> <https://help.crestron.com/SimplSharp/html/9553c37a-7ef0-26eb-9d71-4831524255b2.htm>
> · `eDeviceRegistrationUnRegistrationResponse` enum (`NoAttempt=0`, `Failure=1`,
> `Success=2`, `NonRegisterableDevice=3`, `IntegerParameterNotSet=4`,
> `StringParameterNotSet=5`, `Incompatible=6`, `ParentRegistered=7`, `NotLicensed=8`) —
> <https://help.crestron.com/SimplSharp/html/0fe46277-4e09-1529-dabb-f5756075703b.htm>
> · the `.RegistrationFailureReason` companion and the
> `eDeviceRegistrationUnRegistrationFailureReason` enum are in the corpus too
> (searchable via `crestron-lookup`).

### 5. Address devices at construction — IPID (Ethernet) or Cresnet ID

A device is bound to the control system by its address, passed to the **constructor**
before `Register()`: an **IPID** for IP/Ethernet-connected devices, or a **Cresnet ID**
for Cresnet devices (plus the `CrestronControlSystem` instance as the parent). The
address must match the hardware/program configuration; a wrong or duplicate IPID
registers to nothing or collides (`Register()` returns a failure — Gotcha #4). The
control method (Ethernet vs. Cresnet vs. internal) is fixed by which device class and
constructor you pick.

> **[convention]** `eControlMethod` and the per-device IPID/Cresnet constructor
> parameters are core `Crestron.SimplSharpPro` device wiring; `eControlMethod` is
> **not** in this corpus (grep-confirmed absent). The device constructors that take an
> IPID/Cresnet ID + control-system parent are searchable per device via
> `crestron-lookup`; the addressing rule itself is the established Pro convention.

### 6. Handle program stop gracefully — subscribe to the program-status event

A `.cpz` is long-lived and holds real handles: registered devices, sockets, threads,
timers, event subscriptions. When the program is stopped, paused, or the processor
reboots, nothing reclaims them for you. Subscribe to the **program-status event**
(`CrestronEnvironment`'s program-status handler) and, on the *Stopping* status,
unregister devices, close sockets, stop threads/timers, and dispose — otherwise a
restart leaks handles, leaves a socket bound, or fails to re-register cleanly.

> **[convention]** The program-status handler and its `eProgramStatusEventType` live
> on `CrestronEnvironment` in the base `Crestron.SimplSharp` assembly, which is **not**
> in this Pro-skewed corpus (grep-confirmed absent). It is the standard SIMPL# Pro
> lifecycle hook; skeleton in [`SIMPLSHARP_PRO_PATTERNS.md`](SIMPLSHARP_PRO_PATTERNS.md).

### 7. Release resources — dispose devices and your own handles on stop

Beyond unhooking the program-status event (Gotcha #6), release what you own. Crestron
device objects implement `Dispose()`; call it (and `UnRegister()` where appropriate) on
program stop, and implement **`IDisposable`** on your own classes that hold sockets,
threads, or timers so a restart starts clean.

> Source: `GenericDevice.Dispose` and `GenericDevice.UnRegister` are in the corpus,
> confirming the Crestron device disposal/unregister lifetime contract
> (`UnRegister` —
> <https://help.crestron.com/SimplSharp/html/050aa801-8fb3-a76b-0f62-91bf5cfd61c4.htm>;
> `Dispose` searchable via `crestron-lookup`). **[convention]** Implementing
> `IDisposable` on *your* helper classes is the boundary lifetime rule, not a
> corpus-specified requirement (same as SIMPL# Gotcha #7).

### 8. Do network / device I/O off the lifecycle thread

Socket connects, blocking reads, device polling, and retries must not run on the
`InitializeSystem`/program-status thread (Gotchas #3, #6). Use a Crestron worker
thread (`CrestronThread`) or the Crestron socket classes' asynchronous receive
callbacks, and marshal results back into your logic there. Use the Crestron threading
and socket primitives, **not** `System.Threading`/`System.Net.Sockets` (Gotcha #2).

> **[convention]** `CrestronThread` and the Crestron socket classes (e.g. the TCP
> server/client) are base `Crestron.SimplSharp` types, **not** in this corpus
> (grep-confirmed absent). Threaded-receive skeleton in
> [`SIMPLSHARP_PRO_PATTERNS.md`](SIMPLSHARP_PRO_PATTERNS.md).

## Still to document
- Which concrete device classes take IPID vs. Cresnet ID (per-device constructors —
  the corpus documents each; there is no single manifest).
- `eDeviceRegistrationUnRegistrationFailureReason` value-by-value remediation.
- Licensing (`NotLicensed`) and the object-license model for VC-4.
- SmartObject / join-based UI feedback from a standalone program (vs. the SIMPL#
  delegate-property path).

_Add rules here as they are confirmed against the corpus (via `crestron-lookup`).
Keep this file SIMPL# Pro-only — SIMPL+ and SIMPL# rules belong in their own sibling files._
