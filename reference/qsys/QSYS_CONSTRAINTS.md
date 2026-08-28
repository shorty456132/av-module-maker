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

## Script Organization

Runtime scripts follow a fixed section order, with a header comment block and section
dividers. The full skeleton is in `QSYS_PATTERNS.md` — do not invent a different layout.

## Controls

- Control values are **floats** — convert for string concatenation: `tostring(value)`
- Access control properties: `.Value` (float), `.String` (text), `.Boolean` (bool)

## Properties

- Properties are **read-only at runtime**: `Properties["My Prop"].Value`
- **Do NOT put connection details in properties** — see Connection Parameters below.
  Properties are baked in at design-time and cannot be changed without editing the design.

## Connection Parameters

IP addresses, ports, usernames, and passwords must **never** be hardcoded as string or
number literals, and must never live in properties.

- Read them from runtime Text controls on a **Setup** page: `Controls["IPAddress"]`,
  `Controls["Port"]`, `Controls["Username"]`, `Controls["Password"]`.
- `IPAddress`, `Username`, and `Password` are Q-SYS **reserved** control names and enable
  built-in features. `Port` is the conventional companion name, not a reserved one.
- An `EventHandler` on `IPAddress` (and `Port`, where applicable) must **tear down and
  re-establish** the connection when the value changes.
- A hardcoded connection value is a **blocking issue** — flag it rather than silently
  substituting one. The correct value is unknown and must come from the user.

## Component References

- `Component.New("Name")` results must be stored in **global** variables at the top of the
  script — never created inline inside an event handler or function.
- **Nil-check every `Component.New()` result** before use. A renamed or missing component
  returns nil, and the failure otherwise surfaces far from its cause.
- Preserve exact named-component strings — never rename them.

## Event Handlers

- Inline anonymous functions are fine for single-trigger handlers.
- Extract a named helper when the same logic fires from multiple controls, or is also
  needed at initialization.
- **Handlers must be safe to fire on script load** — Q-SYS fires all handlers at startup,
  so a handler that assumes a live connection or populated state will run before either
  exists.

## Naming Conventions

- **Globals, functions, objects**: PascalCase — `MySocket`, `ParseResponse`
- **Local variables**: camelCase — `myLocalVar`, `bufferData`
- **Control names**: PascalCase; spaces are allowed *between words* — `"Send Button"`,
  `"Status Indicator"`
- **Loop indices attach with no space** — `"Mute" .. i` produces `"Mute1"`, never
  `"Mute 1"`. Space-separated numbering is exactly what `Count` > 1 generates and what this
  convention exists to avoid, so a name may contain spaces but never one before its index.
- **Preserve exact control pin names** — `Controls["PinName"]` strings are the plugin's
  external contract; never rename a pin to suit the code.
- **Lua is case-sensitive** — `"string"` and `"String"` are different

## Scoping Rules

- Top-level variables (outside any function) may be `local` or global — ordinary state,
  intermediate values, and constants are fine as `local` at the top level.
- `local` **inside a function body** is for temporary values only; they go out of scope
  when the function returns.
- **Timers, sockets, websockets, and serial ports must be declared without `local`** — as
  true globals at script level. Never create one inside a function body: the garbage
  collector destroys it when the function returns and it silently stops working.
- A function-scoped timer, socket, websocket, or serial port is a **blocking issue**.
- Socket parameters from `TcpSocketServer.EventHandler()` must be stored globally.

## Comments & Documentation

- General comments go on the line **above** the code they describe, not inline. Inline
  comments only for granular single-expression clarification.
- Add a doc block above **any function whose behavior isn't immediately obvious from its
  name**:

```lua
--[[ Summary:
    Parses a device status response and updates
    the matching indicator controls.
    Params:  data (string) - a single delimited
             response line from the device
    Returns: nil
]]
function ParseResponse(data)
  -- ...
end
```

This is not "comment every function" — a well-named `Send` or `Connect` needs no doc block.
Document the ones whose purpose, parameters, or side effects aren't self-evident.

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
10. **Wrap risky operations in `pcall`** — socket opens, server listen, port opens, UDP
    sends. Print failures to the debug window (`print("Error:", err)`). `pcall` is **not**
    a substitute for input validation.
11. **Properties are read-only at runtime** — use `RectifyProperties` for design-time
    changes only
12. **Dynamic pages require calling the helper in both `GetPages` and `GetControlLayout`**
