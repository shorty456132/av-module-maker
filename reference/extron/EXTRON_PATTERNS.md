# Extron ControlScript — Device Module Patterns

> Scope: ready-to-adapt skeletons for a **reusable device module** (a class in
> `src/modules/device/`). Mirrors `reference/crestron/*/›*_PATTERNS.md`. Every
> pattern obeys `EXTRON_CONSTRAINTS.md` (bytes not str, buffer the 1024-byte
> chunks, no blocking, check `Connect()` result, one model per interface).
> Signatures are from the vendored `extronlib/<version>/` stubs.

---

## 1. Ethernet device module (async, buffered) — the default shape

A TCP device with unsolicited feedback. Owns the interface, manages reconnect +
keepalive, parses `\r`-delimited frames, and exposes state via `WatchVariable`.

```python
# src/modules/device/SampleDisplay.py
import time

from extronlib import event
from extronlib.interface import EthernetClientInterface
from extronlib.system import Wait, Timer

from modules.helper.ModuleSupport import WatchVariable, eventEx


class SampleDisplay:
    """Async Ethernet driver for <device>. Commands are methods; feedback is
    published through WatchVariable instances the project subscribes to."""

    def __init__(self, hostname, ipport=23):
        self._link = EthernetClientInterface(hostname, ipport)   # TCP by default
        self._buffer = b''
        self._lastRx = None

        # Published state — project subscribes with @eventEx(dev.Power, 'Changed')
        self.Power = WatchVariable('Power')
        self.Input = WatchVariable('Input')
        self.Online = WatchVariable('Online')

        self._link.Connected = self._handleConnection
        self._link.Disconnected = self._handleConnection
        self._link.ReceiveData = self._handleReceiveData

    # -- lifecycle -----------------------------------------------------------
    def Connect(self):
        """Call from system.Initialize(). Retries on failure (constraint #7)."""
        if 'Connected' not in self._link.Connect(10):
            Wait(5, self.Connect)

    def _handleConnection(self, interface, state):
        self.Online.Change(state == 'Connected')
        if state == 'Connected':
            interface.StartKeepAlive(5, b'PWR?\r')   # constraint #10
        else:
            interface.StopKeepAlive()
            Wait(5, self.Connect)

    # -- receive (constraints #4, #5) ---------------------------------------
    def _handleReceiveData(self, interface, data):
        self._lastRx = time.monotonic()
        self._buffer += data                          # data is bytes
        while True:
            frame, delim, rest = self._buffer.partition(b'\r')
            if not delim:                             # no complete frame yet
                break
            self._buffer = rest
            self._parse(frame)

    def _parse(self, frame):
        text = frame.decode(errors='ignore').strip()
        if text.startswith('PWR='):
            self.Power.Change(text[4:] == 'ON')
        elif text.startswith('INP='):
            self.Input.Change(text[4:])

    # -- commands ------------------------------------------------------------
    def SetPower(self, on):
        self._link.Send(b'PWR=ON\r' if on else b'PWR=OFF\r')

    def SetInput(self, source):
        self._link.Send('INP={}\r'.format(source).encode())
```

Wiring into a project:

```python
# devices.py — DEFINITION only (constraint #11)
from modules.device.SampleDisplay import SampleDisplay
Display = SampleDisplay('192.168.1.50', 23)

# system.py
from devices import Display
def Initialize():
    Display.Connect()
    print('System Initialized')

# control/av.py — SUBSCRIBE to feedback
from devices import Display
from modules.helper.ModuleSupport import eventEx

@eventEx(Display.Power, 'Changed')
def _onPower(src, isOn):
    print('Display power ->', isOn)
```

---

## 2. Serial variant

Same shape; swap the interface. `SerialInterface` needs the host processor and a
port name (constraint #8).

```python
from extronlib.interface import SerialInterface
from devices import Processor            # an extronlib.device.ProcessorDevice

self._link = SerialInterface(Processor, 'COM1', Baud=9600, Parity='None',
                             Stop=1, Mode='RS232')
# SerialInterface has no Connect()/Connected — a serial port is always "up".
# Keep ReceiveData buffering identical; drive keepalive/poll with @Timer if needed.
```

---

## 3. Synchronous polling module (`SendAndWait`) — the alternative model

Use when the device only answers queries (no unsolicited data). **Never** combine
this with a `ReceiveData` handler on the same interface (constraint #6).

```python
import re
from extronlib.interface import EthernetClientInterface

class SamplePoller:
    def __init__(self, hostname, ipport):
        self._link = EthernetClientInterface(hostname, ipport)
        self._rex = re.compile(b'PWR=(ON|OFF)\r')

    def Connect(self):
        if 'Connected' not in self._link.Connect(10):
            Wait(5, self.Connect)

    def QueryPower(self):
        resp = self._link.SendAndWait(b'PWR?\r', 0.3, deliRex=self._rex)  # blocks
        if not resp:                       # b'' on timeout (constraint #6)
            return None
        return self._rex.match(resp).group(1) == b'ON'
```

Delimiter options (pick one): `deliLen=<int>`, `deliTag=<bytes>`, `deliRex=<regex>`.

---

## 4. Reconnect watchdog (optional hardening)

When a device can go silent without dropping TCP, watch `time.monotonic()` since
last receive and force a reconnect. Drive it with `@Timer`, never a blocking loop.

```python
@Timer(1)
def _watchdog(timer, count):
    if self._lastRx and time.monotonic() - self._lastRx > 15:
        self._lastRx = None
        self._link.Disconnect()
        self.Connect()
```

---

## 5. Exposing state — three publishing options

| Tool (`ModuleSupport`) | Use when | Fire it with |
|---|---|---|
| `WatchVariable('name')` | Module holds a state value the project reacts to | `self.Power.Change(value)` → `@eventEx(dev.Power, 'Changed')` |
| `GenericEvent('name')` | Wrapping a library callback into an `@event`-style event | `evt.Trigger(args)` → `@eventEx(evt, 'Triggered')` |
| plain callback attribute | Simplest one-consumer case | assign `dev.OnPower = fn`, call `fn(...)` |

Prefer `WatchVariable`/`eventEx` so multiple consumers (UI + control logic) can
subscribe (constraint #1).

---

## Reference snippets

Extron's own object-instantiation and event snippets are vendored in
`../snippets/python.json` (e.g. `Extron Event ReceiveData`,
`Extron Interface EthernetClientInterface`, `Extron TimerDecorator`) and JSON
project-descriptor device entries by part number in `device-snippets.json`.
