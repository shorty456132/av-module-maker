# SIMPL# Pro Patterns

> Scope: **SIMPL# Pro only** (`.cpz`, standalone on 4-Series / VC-4). Mirrors the
> role of `reference/qsys/QSYS_PATTERNS.md`: ready-to-adapt skeletons so most work
> needs no doc search. Read alongside [`SIMPLSHARP_PRO_CONSTRAINTS.md`](SIMPLSHARP_PRO_CONSTRAINTS.md) —
> every pattern here obeys those rules (constrained BCL, non-blocking
> `InitializeSystem`, register-and-check-the-return, graceful program stop,
> `IDisposable`, I/O off the lifecycle thread).
>
> Sibling targets: SIMPL+ → `../simplplus/SIMPLPLUS_PATTERNS.md`,
> SIMPL# → `../simplsharp/SIMPLSHARP_PATTERNS.md`.
>
> **Sourcing note.** These are *skeletons*, not verbatim corpus excerpts. The Pro
> lifecycle surface (`CrestronControlSystem`, `InitializeSystem`,
> `GenericDevice.Register` → `eDeviceRegistrationUnRegistrationResponse`) is
> corpus-verified and carries `> Source:` lines. The base-runtime pieces (the
> program-status handler / `CrestronEnvironment`, `CrestronThread`, the Crestron
> socket classes) live in `Crestron.SimplSharp`, which is **not** in this Pro-skewed
> corpus (see `SIMPLSHARP_PRO_CONSTRAINTS.md` sourcing note) and is tagged
> **[convention]**. Nothing is invented.

## The shape of a SIMPL# Pro program

| Piece | Role |
|---|---|
| `CrestronControlSystem` subclass | The program entry class — one per program |
| Constructor | Cheap wiring only: set thread limits, subscribe to the program-status event. **No device I/O.** |
| `InitializeSystem()` override | Construct devices, `Register()` them, check the return, hook events — fast, non-blocking |
| Program-status handler | On *Stopping*: unregister/close/dispose everything |

There is **no** SIMPL Windows symbol and **no** `.usp` wrapper — contrast the SIMPL#
two-part deliverable (`../simplsharp/SIMPLSHARP_PATTERNS.md`).

---

## Pattern 1 — The control-system entry class

Constructor does only cheap wiring and subscribes to the program-status event;
`InitializeSystem` constructs and registers a device and **checks the registration
return** before using it; the stop handler releases everything. Real device work is
kept off the lifecycle thread (Pattern 2).

```csharp
using System;
using Crestron.SimplSharp;                 // CrestronEnvironment, ErrorLog, CrestronThread
using Crestron.SimplSharpPro;              // CrestronControlSystem, eDeviceRegistrationUnRegistrationResponse

namespace MyCompany.MyProgram
{
    public class ControlSystem : CrestronControlSystem
    {
        private MyDeviceDriver _device;    // your own driver (Pattern 2)

        public ControlSystem() : base()
        {
            try
            {
                // Cheap wiring ONLY — no device I/O in the ctor (Constraint #3).
                Thread.MaxNumberOfUserThreads = 20;

                // Graceful-stop hook (Constraint #6). [convention]
                CrestronEnvironment.ProgramStatusEventHandler += OnProgramStatus;
            }
            catch (Exception e)
            {
                ErrorLog.Error("Error in constructor: {0}", e.Message);
            }
        }

        // Runs at program start. Must return promptly (Constraint #3).
        public override void InitializeSystem()
        {
            try
            {
                _device = new MyDeviceDriver(0x03, this);   // IPID + parent (Constraint #5)

                // Register and CHECK THE RETURN — it does not throw (Constraint #4).
                var result = _device.Register();
                if (result != eDeviceRegistrationUnRegistrationResponse.Success)
                {
                    ErrorLog.Error("MyDevice registration failed: {0}", result);
                    return;
                }

                // Slow work (connect, poll) goes on a worker thread — NOT here.
                _device.StartAsync();
            }
            catch (Exception e)
            {
                ErrorLog.Error("Error in InitializeSystem: {0}", e.Message);
            }
        }

        // Program-status callback (Constraint #6). [convention]
        private void OnProgramStatus(eProgramStatusEventType status)
        {
            if (status == eProgramStatusEventType.Stopping)
            {
                // Release everything before the program unloads (Constraint #7).
                _device?.Dispose();          // stops threads/sockets, then UnRegister()
            }
        }
    }
}
```

Key points, each traceable to a constraint:
- **Subclass `CrestronControlSystem`; override `InitializeSystem`** — the program entry
  surface (Constraint #1/#2). The class *is* the program; there is no SIMPL Windows.
- **Constructor stays cheap** — thread limits + program-status subscription; no device
  I/O (Constraint #3).
- **`Register()` return is checked** against `.Success` before the device is used
  (Constraint #4) — the single most common Pro bug when skipped.
- **IPID + `this`** passed to the device constructor addresses it (Constraint #5).
- **Program-status *Stopping*** disposes/unregisters (Constraints #6, #7).

> Source: `CrestronControlSystem` (base entry class; namespace `Crestron.SimplSharpPro`) —
> <https://help.crestron.com/SimplSharp/html/46269246-04c5-bc22-78ed-d86613dd8bbc.htm>
> · `InitializeSystem` method —
> <https://help.crestron.com/SimplSharp/html/ac434802-044e-8e4a-6c8a-3e03bee48d94.htm>
> · `GenericDevice.Register` →
> <https://help.crestron.com/SimplSharp/html/9553c37a-7ef0-26eb-9d71-4831524255b2.htm>
> · `eDeviceRegistrationUnRegistrationResponse` (`.Success`) →
> <https://help.crestron.com/SimplSharp/html/0fe46277-4e09-1529-dabb-f5756075703b.htm>
> **[convention]** `CrestronEnvironment.ProgramStatusEventHandler` /
> `eProgramStatusEventType`, `Thread.MaxNumberOfUserThreads`, and `ErrorLog` are base
> `Crestron.SimplSharp` runtime members, not in this Pro-skewed corpus.

---

## Pattern 2 — A device driver with threaded TCP receive

The driver keeps its network I/O **off** the lifecycle thread (Constraint #8): connect
and read on a worker thread, hand parsed responses back to the program, and dispose
cleanly. `Register()`/`UnRegister()` here delegate to whatever Crestron device or
transport the driver wraps.

```csharp
using System;
using Crestron.SimplSharp;                     // CrestronThread, ErrorLog
using Crestron.SimplSharp.CrestronSockets;     // TCPClient, SocketStatus, SocketErrorCodes

namespace MyCompany.MyProgram
{
    public class MyDeviceDriver : IDisposable
    {
        private readonly uint _ipid;
        private readonly CrestronControlSystem _cs;
        private TCPClient _client;
        private bool _running;

        public MyDeviceDriver(uint ipid, CrestronControlSystem cs)
        {
            _ipid = ipid;
            _cs   = cs;
        }

        // Fast: construct/register the underlying device. Return checked by caller.
        public eDeviceRegistrationUnRegistrationResponse Register()
        {
            // ... construct the concrete Crestron device with _ipid + _cs, then: ...
            return eDeviceRegistrationUnRegistrationResponse.Success;   // placeholder
        }

        // Called from InitializeSystem — starts the SLOW work off-thread (Constraint #8).
        public void StartAsync()
        {
            _running = true;
            _client = new TCPClient("192.168.1.50", 23, 4096);
            _client.SocketStatusChange += OnSocketStatus;
            _client.ConnectToServerAsync(OnConnected);   // async — does not block
        }

        private void OnConnected(TCPClient c)
        {
            if (c.ClientStatus == SocketStatus.SOCKET_STATUS_CONNECTED)
                c.ReceiveDataAsync(OnDataReceived);      // arm async receive
            else
                ErrorLog.Notice("Connect failed; will retry");
        }

        // Receive callback runs off the lifecycle thread. Re-arm after each read.
        private void OnDataReceived(TCPClient c, int bytes)
        {
            if (bytes <= 0) return;                      // 0/neg = disconnect
            string rx = System.Text.Encoding.ASCII.GetString(c.IncomingDataBuffer, 0, bytes);
            // ... parse rx, raise feedback into the program ...
            if (_running) c.ReceiveDataAsync(OnDataReceived);
        }

        private void OnSocketStatus(TCPClient c, SocketStatus status) { /* track online */ }

        public eDeviceRegistrationUnRegistrationResponse UnRegister()
        {
            return eDeviceRegistrationUnRegistrationResponse.Success;  // placeholder
        }

        // Constraint #7: release sockets/threads on program stop.
        public void Dispose()
        {
            _running = false;
            _client?.DisconnectFromServer();
            _client?.Dispose();
            UnRegister();
        }
    }
}
```

Key points:
- **Slow I/O is async / off-thread** — `ConnectToServerAsync` + `ReceiveDataAsync`
  never block `InitializeSystem` (Constraints #3, #8).
- **Re-arm the receive** after each callback — Crestron async receive is one-shot.
- **`IDisposable`** stops the loop, closes the socket, and unregisters (Constraint #7),
  so the Pattern 1 stop handler can release it in one call.

> Source: `GenericDevice.UnRegister` (device unregister on stop) —
> <https://help.crestron.com/SimplSharp/html/050aa801-8fb3-a76b-0f62-91bf5cfd61c4.htm>
> · registration return type `eDeviceRegistrationUnRegistrationResponse` —
> <https://help.crestron.com/SimplSharp/html/0fe46277-4e09-1529-dabb-f5756075703b.htm>
> **[convention]** `TCPClient`, `SocketStatus`, `ConnectToServerAsync`/`ReceiveDataAsync`,
> and `CrestronThread` are base `Crestron.SimplSharp[.CrestronSockets]` types, **not**
> in this Pro-skewed corpus (grep-confirmed absent). Confirm each socket signature
> against the base assembly before shipping; the threaded-receive *shape* is the
> established Pro convention.

## Still to document
- Concrete device-class examples (e.g. a specific display/DSP) with their real
  IPID/Cresnet constructors, verified per device via `crestron-lookup`.
- SmartObject / touchpanel join feedback from a standalone program.
- Retry/backoff on `ConnectToServerAsync` failure and online/offline debouncing.

_Add confirmed patterns here, each with a `> Source:` link (corpus via
`crestron-lookup`) or a clear **[convention]** tag. Keep this file SIMPL# Pro-only._
