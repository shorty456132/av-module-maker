# Q-SYS Plugin Constraints & Conventions

Read this before writing or revising any plugin Lua. It covers the platform rules that,
if violated, produce plugins that fail to compile, misbehave at runtime, or break in
Q-SYS Designer in ways that aren't obvious from the error messages.

## Design-Time vs Runtime

- `GetControls()`, `GetProperties()`, `GetControlLayout()`, and all other lifecycle
  functions execute at **design-time** in Q-SYS Designer, not at runtime.
- You **cannot** dynamically create controls at runtime. All controls must be pre-defined
  in `controls.lua`.
- Use `IsInvisible` on pre-generated controls to simulate dynamic UI behavior.
- Design-time functions run in strict order and are **case-sensitive**.
- The `Controls` object only exists at runtime — never reference it in design-time functions.
- Runtime code lives inside `if Controls then ... end`.

## Control Arrays — Never Use `Count` > 1

`Count` > 1 creates controls with space-separated auto-numbered names (`"Button 1"`,
`"Button 2"`), which causes indexing confusion and bugs. **Instead, drive a loop from an
integer property** to create individually named controls (`"Input1"`, `"Input2"`), looping
consistently in `controls.lua`, `layout.lua`, and `runtime.lua`. Full example:
`QSYS_PATTERNS.md`.

## Controls

- Control values are **floats** — convert for string concatenation: `tostring(value)`
- Access control properties: `.Value` (float), `.String` (text), `.Boolean` (bool)

## Properties

- Properties are **read-only at runtime**: `Properties["My Prop"].Value`
- **Do NOT put connection details in properties** — IP addresses, port numbers, device IDs,
  usernames, and passwords must be runtime-settable Text controls on a Setup page.
  Properties cannot be changed without editing the design.

## Naming Conventions

- **Globals, functions, objects**: PascalCase — `MySocket`, `ParseResponse`
- **Local variables**: camelCase — `myLocalVar`, `bufferData`
- **Control names**: PascalCase with spaces — `"Send Button"`, `"Status Indicator"`
- **Lua is case-sensitive** — `"string"` and `"String"` are different

## Scoping Rules

- **Never declare sockets, timers, or serial ports as `local`** — they will be garbage
  collected
- Top-level plugin variables should be global (no `local` keyword)
- Use `local` only for temporary variables inside functions and loop iterators
- Socket parameters from `TcpSocketServer.EventHandler()` must be stored globally

## Debug Logging

Every plugin that communicates with a device must include debug prints:
- **TX**: `print("TX: " .. cmd)` — **RX**: `print("RX: " .. data)`
- **Errors**: socket errors, timeouts, parse failures, pcall errors
- **State changes**: connect, disconnect, reconnect events

Keep logging concise — trace command flow and diagnose issues, not verbose variable dumps.

## Versioning

- `Version` uses 3-part format: `"1.0.0"` (Major.Minor.Fix)
- `BuildVersion` uses 4-part format: `"1.0.0.0"` (Major.Minor.Fix.Development)
- The compiler updates both fields when bumping versions

## Common Pitfalls

1. **Don't create controls at runtime** — pre-generate them in `controls.lua`
2. **Capture loop variables in closures** — use local captures for EventHandlers
3. **Check protocol variations** — TCP vs UDP, manufacturer-specific differences
4. **Validate control references** — ensure controls exist before accessing
5. **Don't use reserved names** — see reserved control names and functions in
   `QSYS_PATTERNS.md`
6. **Never declare sockets/timers as `local`** — they get garbage collected and stop working
7. **UDP has no buffer** — implement manual buffering for incomplete messages
8. **Delay serial port open** — use `Timer.CallAfter(fn, 1)` to ensure connection is ready
9. **Always check `.IsConnected` / `.IsOpen`** before writing to sockets/ports
10. **Wrap risky operations in `pcall`** — socket opens, server listen, port opens
11. **Properties are read-only at runtime** — use `RectifyProperties` for design-time
    changes only
12. **Dynamic pages require calling the helper in both `GetPages` and `GetControlLayout`**
