# Extron ControlScript — Constraints

> Scope: hard rules and gotchas for **ControlScript device modules** (Python on
> Extron Pro / Pro xi). Mirrors `reference/crestron/simplplus/SIMPLPLUS_CONSTRAINTS.md`:
> the things an author must get right *before* writing a module. Every claim
> here is confirmed against the vendored `extronlib/<version>/` stubs and
> `template/src/modules/helper/ModuleSupport.py`. Cite the stub file when adding.

## Event model

### 1. One handler per event with `@event` — last assignment wins

`extronlib`'s `@event(Object, EventName)` binds **one** handler to a given
object+event. Assigning a second handler to the same event *replaces* the first.
If a module and the project both need to react to the same `ReceiveData`/
`Connected` event, use **`ModuleSupport.eventEx`** (vendored in
`template/.../helper/ModuleSupport.py`), which supports multiple handlers and can
bind to method names as well as event properties.
> Source: `extronlib/1.8.21xi/extronlib/__init__.py` (Notes: "Only one handler…
> Last handler assigned will be called"); `ModuleSupport.eventEx`.

### 2. A handler's signature must match the event exactly

The decorated function must take the exact positional args the event defines —
almost always `(interface, data)` for `ReceiveData`, `(interface, state)` for
`Connected`/`Disconnected`. Wrong arity fails at dispatch, not at definition.

### 3. Expose module state through an event object, not by reaching in

Let the project subscribe to the module rather than poll it. Use
`ModuleSupport.WatchVariable` (wrap a state var; call `.Change(newvalue)` to fire
`Changed`) or `GenericEvent` (turn a callback into an `@event`-compatible
`Triggered`). Handlers bind with `@eventEx(watcher, 'Changed')`.
> Source: `ModuleSupport.WatchVariable`, `ModuleSupport.GenericEvent`.

## Communication

### 4. `ReceiveData` delivers **bytes**, not str

The `ReceiveData` handler's second arg is a `bytes` object. Decode explicitly
(`data.decode()`) before string parsing, or parse as bytes. Don't assume `str`.
> Source: `EthernetClientInterface.ReceiveData` / `SerialInterface.ReceiveData`.

### 5. `ReceiveData` is chunked at 1024 bytes — you must buffer

Max payload per `ReceiveData` event is **1024 bytes**; larger responses arrive
across multiple events. Never parse a single event's data as a complete message.
Accumulate into a module buffer and extract complete frames by delimiter (the
canonical idiom is `buffer.partition(b'\r')` in a `while` loop — see
`EXTRON_PATTERNS.md`). For UDP, data is truncated to the buffer size (4096 default).
> Source: `EthernetClientInterface.ReceiveData` Notes.

### 6. `SendAndWait` blocks — never call it inside a `ReceiveData` handler

`SendAndWait(data, timeout, **deli)` is **synchronous/blocking**. Calling it
within a `ReceiveData` event is explicitly unsupported, and using it while
unsolicited data is arriving can lose data. Choose one model per module:
**async** (`Send` + `ReceiveData` buffer parsing) or **synchronous polling**
(`SendAndWait`) — don't mix them on the same interface.
Delimiter kwargs are mutually exclusive: `deliLen=<int>`, `deliTag=<bytes>`, or
`deliRex=<compiled regex>`. Returns `b''` on timeout/no-match.
> Source: `EthernetClientInterface.SendAndWait` / `SerialInterface.SendAndWait`.

### 7. `Connect()` returns a status string; check it, don't assume success

`EthernetClientInterface.Connect(timeout)` returns `'Connected'`,
`'ConnectedAlready'`, or a **failure reason** string. Test with
`'Connected' in result` and schedule a retry via `Wait` on failure. `Connect`/
`Disconnect` do **not** apply to UDP.
> Source: `EthernetClientInterface.Connect`.

### 8. `SerialInterface` needs a Host device and a Port name

`SerialInterface(Host, Port, …)` requires a `ProcessorDevice`/`SPDevice`/
`AdapterDevice` as `Host` and a port string (`'COM1'`, `'IRS1'`). A port already
claimed as an `IRInterface` raises if reused as `SerialInterface`. Defaults:
`Baud=9600, Data=8, Parity='None', Stop=1, FlowControl='Off', Mode='RS232'`.
> Source: `SerialInterface.__init__`.

## Scheduling & timing

### 9. Never block the interpreter — use `Wait` / `Timer`, not `time.sleep`

ControlScript is single-threaded/event-driven. Blocking (`time.sleep`, busy
loops) stalls all event processing. Use `extronlib.system.Wait(seconds, fn)` /
the `@Wait(seconds)` decorator for one-shots and `@Timer(interval)` for periodic
work (e.g. keepalive/poll). Use `time.monotonic()` only to *measure* elapsed time.
> Source: `extronlib.system.Wait`, `extronlib.system.Timer`; `EthernetClientInterface` docstring example.

### 10. Keepalive is built in — prefer it over hand-rolled polling

`StartKeepAlive(interval, data)` / `StopKeepAlive()` on the interface send a
query on a timer without you managing a `Timer`. Start it in the `Connected`
handler, stop it in `Disconnected`.
> Source: `EthernetClientInterface.StartKeepAlive`.

## Project structure

### 11. Define in `devices.py`, connect in `system.Initialize()`

Per the template: instantiate devices/interfaces in `devices.py` (definition
only), and put `Connect()` calls and service setup inside `system.Initialize()`,
which `main.py` calls **after** all components are imported. A module class may
own its interface, but its `Connect()` should be triggered from the Initialize
path, not at import time.
> Source: `template/src/{devices,system,main}.py` docstrings.

### 12. `variables.py` for cross-module shared state; mind `global`

Shared state lives in `variables.py` and is imported where needed. When a handler
reassigns a module-level variable, declare `global` (see the `WatchVariable`
example) — otherwise you shadow it locally and the update is lost.
