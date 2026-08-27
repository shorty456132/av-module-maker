# SIMPL# Patterns

> Scope: **SIMPL# only** (`.clz` + its SIMPL+ `.usp` wrapper). Mirrors the role of
> `reference/qsys/QSYS_PATTERNS.md`: ready-to-adapt skeletons so most work needs no
> doc search. Read alongside [`SIMPLSHARP_CONSTRAINTS.md`](SIMPLSHARP_CONSTRAINTS.md) —
> every pattern here obeys those rules (constrained BCL, `SimplSharpString` at the
> boundary, never block the SIMPL+ thread, feedback via delegate properties,
> `IDisposable`, `ushort` analog).
>
> Sibling targets: SIMPL+ → `../simplplus/SIMPLPLUS_PATTERNS.md`,
> SIMPL# Pro → `../simplsharp-pro/SIMPLSHARP_PRO_PATTERNS.md`.
>
> **Sourcing note.** These are *skeletons*, not verbatim corpus excerpts. The
> boundary mechanism (public methods in, delegate-property callbacks out,
> `SimplSharpString`/`ushort` marshaling) is the established SIMPL#↔SIMPL+
> **[convention]** — its core types live in `Crestron.SimplSharp`, which is **not**
> in this Pro-skewed corpus (see `SIMPLSHARP_CONSTRAINTS.md` sourcing note). Corpus-
> and SIMPL+-corpus-verified facts carry a `> Source:` line; nothing is invented.

## The two halves at a glance

| Half | File | Role |
|---|---|---|
| C# class | `.clz` | Public methods = "call in" from SIMPL+; delegate properties = "feed back" to SIMPL+ |
| SIMPL+ wrapper | `.usp` | The SIMPL Windows symbol: declares I/O, instantiates the class, wires signals ↔ methods/callbacks |

Author them together. The wrapper's inputs map to the class's public methods; the
class's delegate properties map to the wrapper's outputs.

---

## Pattern 1 — The C# class (`.clz` half)

A minimal device-control class: two inputs from SIMPL+ (a digital "connect" and a
serial "send command"), and two feedbacks (a digital "is online" and a serial
"response"). Note the marshaling types, the non-blocking offload, the null-guarded
callbacks, and `IDisposable`.

```csharp
using System;
using Crestron.SimplSharp;   // SimplSharpString, CTimer, CrestronConsole

namespace MyCompany.MyDevice
{
    // Delegate types the wrapper assigns callbacks to. Digital/analog feedback
    // is ushort (0/1 for digital); serial feedback is SimplSharpString.
    public delegate void OnlineFeedback(ushort isOnline);
    public delegate void ResponseFeedback(SimplSharpString response);

    public class DeviceController : IDisposable
    {
        // ----- Feedback OUT: delegate properties the .usp wrapper registers -----
        public OnlineFeedback   ReportOnline   { get; set; }
        public ResponseFeedback ReportResponse { get; set; }

        private CTimer _pollTimer;
        private bool   _online;

        // A parameterless ctor is required so SIMPL+ can declare the instance.
        public DeviceController() { }

        // ----- Call IN: public methods SIMPL+ invokes from CHANGE/PUSH -----
        // MUST return fast — this runs on the SIMPL+ thread (Constraint #3).
        public void Connect(ushort enable)
        {
            if (enable > 0)
                // Offload the real work; do NOT block here.
                _pollTimer = new CTimer(Poll, null, 0, 5000);
            else
            {
                _pollTimer?.Stop();
                SetOnline(false);
            }
        }

        // Serial in crosses the boundary as SimplSharpString, not System.String.
        public void SendCommand(SimplSharpString command)
        {
            string cmd = command.ToString();   // convert once inside C#
            // ... queue/send asynchronously; never block the SIMPL+ thread ...
        }

        // ----- Runs off the SIMPL+ thread (timer callback) -----
        private void Poll(object _)
        {
            // ... talk to the device ...
            SetOnline(true);
            // Guard: the wrapper may not have registered this delegate.
            ReportResponse?.Invoke(new SimplSharpString("OK"));
        }

        private void SetOnline(bool value)
        {
            _online = value;
            ReportOnline?.Invoke((ushort)(value ? 1 : 0));   // ushort on the wire
        }

        // ----- Constraint #7: release handles on program stop/restart -----
        public void Dispose()
        {
            _pollTimer?.Stop();
            _pollTimer?.Dispose();
            ReportOnline = null;
            ReportResponse = null;
        }
    }
}
```

Key points, each traceable to a constraint:
- **Public methods = the call-in surface** — SIMPL+ invokes `Connect`/`SendCommand`.
- **Delegate properties = the only feedback path** — C# never sets a signal; it
  invokes `ReportOnline`/`ReportResponse`, which the wrapper drives out (Constraint #4).
- **`SimplSharpString` for serial, `ushort` for digital/analog** at every boundary
  crossing (Constraint #2).
- **Non-blocking**: `Connect` starts a `CTimer` and returns; polling runs off the
  SIMPL+ thread (Constraint #3).
- **`IDisposable`**: `Dispose` stops the timer and nulls the callbacks (Constraint #7).
- **Parameterless constructor** so the wrapper can declare the instance.

> **[convention]** `SimplSharpString`, `CTimer`, and the delegate-property callback
> mechanism are core `Crestron.SimplSharp` boundary features, **not** in this
> Pro-skewed corpus (grep-confirmed absent). For a corpus-verified analog helper,
> see `SimplSharpDeviceHelper.PercentToUshort`/`UshortToPercent` in
> `SIMPLSHARP_CONSTRAINTS.md` Gotcha #8.

---

## Pattern 2 — The SIMPL+ wrapper (`.usp` half)

The wrapper is an ordinary `.usp` and obeys **every** rule in
`../simplplus/SIMPLPLUS_CONSTRAINTS.md`: required directives; I/O declared
digital → analog → serial, inputs then outputs then parameters; `_SKIP_` padding
if there are parameters; CRLF line endings. It pulls in the `.clz`, declares the
class instance, calls its methods from input handlers, and registers callbacks
that write the outputs.

```simplplus
#DEFAULT_VOLATILE
#ENABLE_STACK_CHECKING
#ENABLE_TRACE

// Pull in the .clz by bare name — no path, no extension (Constraint #6).
#USER_SIMPLSHARP_LIBRARY "MyDevice"

// INPUTS — digital, then analog, then serial (SIMPL+ Gotcha #4)
DIGITAL_INPUT   Connect;
STRING_INPUT    Command[255];

// OUTPUTS — same type order
DIGITAL_OUTPUT  Is_Online;
STRING_OUTPUT   Response;

// Declare the class instance from the SIMPL# library.
DeviceController device;

// ----- Callbacks: the class invokes these; they drive the outputs -----
// This is the ONLY way C# feedback reaches a signal (Constraint #4).
CALLBACK FUNCTION OnOnline(INTEGER isOnline)
{
    Is_Online = isOnline;
}

CALLBACK FUNCTION OnResponse(STRING resp)
{
    Response = resp;
}

// ----- Input handlers: marshal signals INTO the class's public methods -----
CHANGE Connect
{
    device.Connect(Connect);        // digital crosses as ushort
}

CHANGE Command
{
    device.SendCommand(Command);    // serial crosses as SimplSharpString
}

// ----- Startup: register the callbacks so feedback has somewhere to land -----
FUNCTION Main()
{
    RegisterDelegate(device, ReportOnline,   OnOnline);
    RegisterDelegate(device, ReportResponse, OnResponse);
}
```

Key points:
- **`#USER_SIMPLSHARP_LIBRARY "MyDevice"`** binds `MyDevice.clz` — bare name only
  (Constraint #6 / SIMPL+ directive doc).
- **`RegisterDelegate`** hooks each C# delegate property to a SIMPL+ `CALLBACK
  FUNCTION`; without it, the class's `ReportOnline?.Invoke(...)` no-ops.
- **Input `CHANGE` handlers** are the call-in path; they pass the signal straight
  to the matching public method.
- The wrapper still owes the full SIMPL+ constraint set (directive order, I/O type
  order, CRLF) — this skeleton shows the SIMPL#-specific glue, not a substitute for
  `../simplplus/SIMPLPLUS_CONSTRAINTS.md`.

> Source: `#USER_SIMPLSHARP_LIBRARY` directive —
> <https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Directives/_USER_SIMPLSHARP_LIBRARY.htm>
> (in-repo: `../simplplus/documents/Language_Constructs_&_Functions/Compiler_Directives/_USER_SIMPLSHARP_LIBRARY.md`).
> **[convention]** `RegisterDelegate` + `CALLBACK FUNCTION` wiring is the core
> SIMPL#↔SIMPL+ boundary mechanism, not documented in this Pro-skewed corpus.

## Still to document
- Multiple instances of one class in a single wrapper (arrays of devices).
- Passing structured/config parameters from `STRING_PARAMETER` into the class ctor.
- Buffer/`GATHER` parsing on the SIMPL+ side vs. parsing inside the `.clz`.

_Add confirmed patterns here, each with a `> Source:` link (corpus via
`crestron-lookup`, or the in-repo SIMPL+ corpus) or a clear **[convention]** tag.
Keep this file SIMPL#-only._
