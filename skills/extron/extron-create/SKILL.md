---
name: extron-create
description: Scaffold an Extron ControlScript device module (.py) from a device description — a reusable class in src/modules/device/ that drives an Ethernet or serial device and exposes commands + feedback
argument-hint: device description (protocol, transport, commands/feedback)
---

# Create Extron ControlScript Device Module

## Target
- **Language:** Python 3 (CPython on an Extron Pro / Pro xi control processor).
- **Artifact:** a **reusable device module** — one class in
  `src/modules/device/<Name>.py` that owns a comms interface and exposes the
  device's commands (methods) and feedback (events). **Not** a full project,
  **not** a UI. It slots into an existing ControlScript project (see the vendored
  layout in `${CLAUDE_PLUGIN_ROOT}/reference/extron/template/`).
- **Toolchain:** ControlScript has **no CLI compiler**. The module is verified by
  **static analysis** against the vendored `extronlib` stubs — see **Verify** below.

## Before writing code
- Read `${CLAUDE_PLUGIN_ROOT}/reference/extron/EXTRON_OVERVIEW.md` — the platform
  model, the two hardware generations (`Pro xi` → stubs `extronlib/1.8.21xi/`,
  `Pro` → stubs `extronlib/3.13.39/`), the project structure, and what a device
  module is.
- Read `${CLAUDE_PLUGIN_ROOT}/reference/extron/EXTRON_CONSTRAINTS.md` — the 12
  hard rules. The checker (below) enforces the four most common ones; obey all 12.
- Reuse a skeleton from `${CLAUDE_PLUGIN_ROOT}/reference/extron/EXTRON_PATTERNS.md`:
  **§1 async buffered Ethernet** (default), **§2 Serial**, or **§3 synchronous
  `SendAndWait` poller** — pick by the device's protocol (unsolicited feedback →
  §1/§2; query/response only → §3).
- For any API/signature question, delegate to an **Explore subagent** over
  `${CLAUDE_PLUGIN_ROOT}/reference/extron/extronlib/<version>/` (per the Q-SYS
  `create-plugin` convention) — do not guess method names or event signatures.

## Decide first (ask only if the description doesn't say)
- **Transport:** Ethernet (`EthernetClientInterface`: TCP/UDP/SSH) or Serial
  (`SerialInterface`: RS-232/422/485). Serial needs a host `ProcessorDevice`/
  `SPDevice`/`AdapterDevice` and a port name.
- **Feedback model:** unsolicited (async — §1/§2) or polled (§3). One model per
  interface — never bind `ReceiveData` *and* call `SendAndWait` on the same one.
- **Generation:** `Pro xi` (default) or `Pro`, which selects the stub tree to
  verify against.

## Each module must include
- [ ] A class that owns its interface, taking connection args in `__init__`
      (hostname/port or host device/port) — no hard-coded addresses.
- [ ] Connection lifecycle: a `Connect()` method that **checks the
      `Connect(timeout)` result** and retries via `Wait` on failure; keepalive
      via `StartKeepAlive`/`StopKeepAlive` in the `Connected`/`Disconnected`
      handlers (Ethernet). `Connect()` is called from `system.Initialize()`,
      not at import.
- [ ] For async modules: a `ReceiveData` handler that **buffers** the byte
      stream (`self._buffer += data`; extract frames with `partition`/delimiter)
      — never parse a single event's `data` as a whole message, and treat it as
      **bytes** (decode explicitly).
- [ ] Commands as methods (`SetPower`, `SetInput`, …) that `Send()` the protocol.
- [ ] Feedback exposed via `ModuleSupport.WatchVariable` + `eventEx` (import from
      `modules.helper.ModuleSupport`) so multiple consumers (control + UI) can
      subscribe — not a single overwritable `@event` handler.
- [ ] No blocking: use `extronlib.system.Wait`/`Timer`, never `time.sleep`.
- [ ] Passes **Verify** with 0 errors.

## Verify
After writing the module, run the static checker — do not consider it done until
it reports `[OK]` (exit 0):

```
python "${CLAUDE_PLUGIN_ROOT}/scripts/extron/extron_check.py" <path/to/module.py>
```

- Encodes the constraint rules as AST checks (stdlib only, runs anywhere):
  `EX-SLEEP` (blocking sleep), `EX-CONN` (discarded `Connect()` result),
  `EX-RXBUF` (unbuffered `ReceiveData`), `EX-MIX` (`SendAndWait` mixed with
  `ReceiveData`), `EX-SYNTAX` (won't parse).
- Select the stub generation with `--stubs=` (default `1.8.21xi`); target a
  `Pro` module with `--stubs="${CLAUDE_PLUGIN_ROOT}/reference/extron/extronlib/3.13.39"`.
- **On a finding** (`file: ERROR <code> (Line <n>) - <message>`): read it, fix
  the module per the cited constraint, and re-run until clean.
- **`EX-MIX` is a warning** (two interfaces may be legitimately different) — the
  build still passes, but confirm it's intentional; if it's one interface, split
  the models.
- If `pyright` is installed it also type-checks against the stubs; if not, the
  AST checks still run (that pass is skipped silently).
