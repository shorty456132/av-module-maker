# Extron ControlScript — Overview

> Scope: the **ControlScript** Python programming model for Extron control
> processors. Mirrors the role of `reference/qsys/` and
> `reference/crestron/*/` overview docs: the mental model an author needs
> before writing a module. Our deliverable target is a **reusable device
> module** (see below), not a full turnkey project.

## Platform model

ControlScript runs a **CPython 3** interpreter on an Extron control processor
(IPCP Pro / IPCP Pro xi series and related). A project is an ordinary Python
package — **not** a compiled binary and **not** a signal-flow graph. There is no
".module" artifact like Q-SYS `.qplug` or Crestron `.clz`; code is deployed as
source (packaged and uploaded via Extron's GUI Configurator / deployment tools).

The entire program is driven by the `extronlib` package, which exposes the
processor's hardware and services as Python objects, and an **event model**: you
attach handler functions to object events with the `@event` decorator.

### Two hardware generations

`extronlib.Platform()` returns one of two values; each has its own ControlScript
version line, and this repo vendors the latest stub tree for each:

| `Platform()` | Generation | Vendored stubs | Notes |
|---|---|---|---|
| `'Pro xi'` | **Pro xi** (current) | `extronlib/1.8.21xi/` | Adds `AdapterDevice`, `DanteInterface`, `RoomSchedulingInterface`; `EthernetServerInterfaceEx`. |
| `'Pro'` | **Pro** (classic) | `extronlib/3.13.39/` | Has plain `EthernetServerInterface` too; no Adapter/Dante/RoomScheduling; ships an `extronlib.standard.exml` XML lib. |

For a **comms-based device module** the relevant classes
(`EthernetClientInterface`, `SerialInterface`, the `@event` decorator,
`system.Wait`/`Timer`) are effectively identical across both generations, so one
module usually runs on either. Confirm signatures against the matching stub tree
when a project pins a generation.

## Canonical project structure

From the vendored `template/` (Extron's default project template). A device
module slots into this structure but the module itself is just the file(s) under
`src/modules/device/`:

```
project.json              # system + device descriptor (name, part numbers, aliases, network)
src/
  main.py                 # entry: prints Platform()/Version(), imports components, calls system.Initialize()
  variables.py            # shared state used across the project
  devices.py              # DEFINE devices/interfaces here (extronlib.device + extronlib.interface objects). Definition only.
  system.py               # Initialize(): CONNECT devices, set up clocks/services. Called last by main.
  control/
    av.py                 # system control logic (separation of concerns: AV, lighting, HVAC, cloud)
  ui/                     # touchpanel (UIDevice) page/button/label logic
  modules/
    device/               # <-- reusable DEVICE MODULES live here (our deliverable target)
    helper/
      ModuleSupport.py    # Extron-provided helpers: eventEx, WatchVariable, GenericEvent, loggers
    project/              # project-specific glue
```

**Lifecycle:** `main.py` imports `variables`, `devices`, `ui.*`, `control.*`,
`system` (in that order), then calls `system.Initialize()`. Devices are
*defined* in `devices.py`, *connected* in `system.Initialize()`.

## The `extronlib` package map

(See `extronlib/<version>/` for full signatures + docstrings.)

- **`extronlib`** — `event` decorator, `Platform()`, `Version()`.
- **`extronlib.device`** — `ProcessorDevice`, `UIDevice`, `eBUSDevice`,
  `SPDevice`, `AdapterDevice` (xi). The physical control endpoints.
- **`extronlib.interface`** — the comms & I/O ports a module drives:
  `EthernetClientInterface`, `SerialInterface`, `EthernetServerInterfaceEx`,
  `RelayInterface`, `IRInterface`, `SPInterface`, `DigitalIOInterface`,
  `ContactInterface`, `FlexIOInterface`, `VolumeInterface`, `TallyInterface`,
  `PoEInterface`, `CircuitBreakerInterface`, `TemperatureInterface`,
  `SWACReceptacleInterface`, `SWPowerInterface`, `DanteInterface` (xi),
  `RoomSchedulingInterface` (xi).
- **`extronlib.system`** — `Wait`, `Timer`, `Clock`, `File`, `MESet`,
  `NetServices`, and `ProgramLog`. Non-blocking scheduling and system services.
- **`extronlib.ui`** — `Button`, `Label`, `Level`, `Slider`, `Knob` (touchpanel).
- **`extronlib.software`** — `SummitConnect`, `DanteDomainManager`.
- **`extronlib.standard`** — misc (Pro generation ships `exml`).

## What "a device module" means here

A **reusable device module** is a Python class (in `src/modules/device/`) that:

1. Owns a comms interface — an `EthernetClientInterface` (TCP/UDP/SSH) or a
   `SerialInterface` (RS-232/422/485 on a processor port).
2. Manages the connection lifecycle (connect, reconnect, keepalive).
3. Parses the device's protocol from the async `ReceiveData` byte stream
   (buffer + delimiter parsing) and/or issues synchronous `SendAndWait` queries.
4. Exposes **commands** (methods like `SetPower`, `SetInput`, `SetVolume`) and
   **feedback/state** (via `ModuleSupport.WatchVariable` / `eventEx`, or plain
   callbacks) so `control/av.py` and `ui/` can drive it without knowing the wire
   protocol.

This is the same role as an Extron **GlobalScripter/ControlScript device module
package**, authored by hand against `extronlib`. See `EXTRON_PATTERNS.md` for the
skeleton and `EXTRON_CONSTRAINTS.md` for the rules that keep it correct.
