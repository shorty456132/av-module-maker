# Q-SYS Lua Code Patterns Reference

Reference material for writing Q-SYS plugin Lua. Read this file when generating or revising
plugin code — it is **not** loaded automatically. `QSYS_CONSTRAINTS.md` holds the hard
constraints; this file holds the patterns those constraints imply.

---

## Script Organization

Every runtime script follows this section order. Do not invent a different layout.

1. Header comment block
2. Constants
3. Global variables and component references
4. Helper functions
5. Event handlers
6. Initialization block

```lua
-- [Component Name]
-- [One sentence: what this script does]
-- Dependencies: [named components referenced, or "none"]

--*** Constants ***
POLL_INTERVAL = 5

--*** Globals ***
-- Sockets, timers, and component references are global by necessity: a local
-- one is garbage collected and silently stops working. See QSYS_CONSTRAINTS.md.
TCP = TcpSocket.New()
PollTimer = Timer.New()
Mixer = Component.New("Main Gain")

--*** Helper Functions ***

--*** Event Handlers ***

--*** Initialization ***
```

Section dividers use the `--*** Name ***` form throughout.

---

## Control Arrays — Full Property-Driven Loop Example

`QSYS_CONSTRAINTS.md` forbids `Count` > 1. This is the full four-file pattern it replaces:

```lua
-- In properties.lua: define a property for the count
table.insert(props, {
  Name = "NumIO",
  Type = "integer",
  Value = 2,
  Min = 1,
  Max = 100
})

-- In controls.lua: loop to create individual controls
local NumOfIO = props["NumIO"].Value
for i = 1, NumOfIO do
  table.insert(ctrls, {
    Name = "Input" .. i,
    ControlType = "Button",
    ButtonType = "Trigger",
    Count = 1,
    UserPin = true,
    PinStyle = "Input"
  })
end

-- In layout.lua: loop to position each control
for i = 1, NumOfIO do
  layout["Input" .. i] = {
    PrettyName = string.format("Input %i", i),
    Style = "Button",
    Position = { 25, (30 * i) + 40 },
    Size = { 50, 30 }
  }
end

-- In runtime.lua: loop to set up event handlers
local NumOfIO = Properties["NumIO"].Value
for i = 1, NumOfIO do
  Controls["Input" .. i].EventHandler = function()
    print("Input " .. i .. " triggered")
  end
end
```

This keeps control names simple (`"Input1"`, `"Input2"`) and consistent across
`controls.lua`, `layout.lua`, and `runtime.lua`.

---

## Basic Patterns

### EventHandler Setup
```lua
Controls["MyButton"].EventHandler = function(ctl)
  print("Button pressed, value:", ctl.Value)
end
```

### Control Visibility
```lua
Controls["MyControl"].IsInvisible = not shouldShow
```

### Dispatch Tables Over Metatables
Prefer dispatch table patterns for cleaner separation of concerns. Use metatables only when
inheritance is truly needed.

### Deep Modules — Simple Interface, Rich Functionality
Design modules and helper classes to be "deep": expose a simple, abstract interface
(functions and properties) and hide the implementation complexity behind it. Hiding internal
state reduces cognitive load and makes the script easier for whoever maintains it next.

### Loop Variable Capture
Always capture loop variables in local variables before using them in closures/EventHandlers:
```lua
for i = 1, count do
  local idx = i  -- capture
  Controls["Button" .. idx].EventHandler = function()
    print("Button " .. idx .. " pressed")
  end
end
```

---

## Network & Transport

### TCP Socket
```lua
TCP = TcpSocket.New()
TCP.ReadTimeout = 0   -- disabled; only set non-zero for TCP servers
TCP.WriteTimeout = 0  -- disabled; only set non-zero for TCP servers
TCP.ReconnectTimeout = 5

TCP.Connected = function()
  print("Connected")
end

TCP.Reconnect = function()
  print("Reconnecting...")
end

TCP.Data = function()
  local data = TCP:ReadLine(TcpSocket.EOL.Custom, "\r\n")
  while data do
    ParseResponse(data)
    data = TCP:ReadLine(TcpSocket.EOL.Custom, "\r\n")
  end
end

TCP.Closed = function()
  print("Socket closed")
end

TCP.Error = function(sock, err)
  print("Socket error:", err)
end

TCP.Timeout = function()
  print("Socket timeout")
end

TCP:Connect(host, port)
```

### UDP Socket
```lua
UDP = UdpSocket.New()

UDP.EventHandler = function(udpSocket, packet)
  -- packet.Address, packet.Port, packet.Data
  print("RX from " .. packet.Address .. ": " .. packet.Data)
end

UDP:Open(nil, listenPort)  -- nil IP binds to all interfaces
UDP:Send(targetIP, targetPort, "data")
```

### Serial Port
```lua
MySerialPort = SerialPorts[1]

MySerialPort.Connected = function(port)
  print("Connected")
end

MySerialPort.Data = function(port)
  local data = port:ReadLine(SerialPorts.EOL.Custom, "\r")
  while data do
    ParseResponse(data)
    data = port:ReadLine(SerialPorts.EOL.Custom, "\r")
  end
end

MySerialPort.Error = function(port, err)
  print("Error:", err)
end

-- Delay open to ensure connection is ready
Timer.CallAfter(function()
  local ok, err = pcall(function()
    MySerialPort:Open(115200, 8, "N")
  end)
  if not ok then print("Error opening port:", err) end
end, 1)
```

### HTTP Client
```lua
function GetRequest(url)
  HttpClient.Download({
    Url = url,
    Method = "GET",
    Headers = { ["Content-Type"] = "application/json" },
    Timeout = 10,
    EventHandler = function(tbl, code, data, err, headers)
      if code == 200 then
        print("OK:", data)
      else
        print("Error:", code, err)
      end
    end
  })
end

-- Build URLs with HttpClient.CreateUrl
local url = HttpClient.CreateUrl({
  Host = "https://example.com",
  Port = 443,
  Path = "api/endpoint",
  Query = { key = "value" }
})
```

### SSH
```lua
SSH = Ssh.New()
SSH.ReadTimeout = 5
SSH.WriteTimeout = 5
SSH.ReconnectTimeout = 5

SSH.Connected = function() print("SSH connected") end
SSH.LoginFailed = function() print("SSH login failed") end
SSH.Data = function()
  local rx = SSH:Read(SSH.BufferLength)
  print("RX:", rx)
end

SSH:Connect(ip, 22, username, password)
```

---

## Timers

Use the Q-SYS `Timer` object for all delays and periodic work — never busy loops,
`while true do`, or Lua's native delay/time functions.

- **Create with `Timer.New()`** and store the handle in a **global** at script level, never
  inside a function body. A locally-scoped timer is garbage collected and silently stops
  (QSC's own example shows a `local` timer dying after ~22 iterations).
- **Assign the callback via `.EventHandler`.** The handler receives the timer object as its
  argument, so one handler can serve several timers by comparing identity
  (`if t == PollTimer then ... end`).
- **`Timer:Start(periodSeconds)` repeats every `periodSeconds` until `Timer:Stop()` is
  called.** It does **not** fire once — this is the most commonly misread part of the API.
- **`Timer:Stop()`** ends repetition; **`Timer:IsRunning()`** returns a boolean.
- For a one-shot delay prefer **`Timer.CallAfter(fn, delay)`** — calls `fn` once after
  `delay` seconds, no `:Stop()` needed.
- **`Timer.Now()`** returns seconds since epoch — the value **differs between Emulation mode
  and Run mode**, so never persist or compare it across modes.

```lua
-- Global handle — required so the GC does not destroy it
PollTimer = Timer.New()

PollTimer.EventHandler = function()
  -- runs every POLL_INTERVAL seconds until PollTimer:Stop()
  Poll()
end

-- repeats until stopped
PollTimer:Start(POLL_INTERVAL)
```

The Heartbeat and Polling Timer patterns below apply these rules.

---

## Connection Health

### Heartbeat
Recommended for TCP and Serial to detect dropped connections:
```lua
HeartbeatTimer = Timer.New()
HeartbeatTimeout = 5  -- Must be > poll interval

HeartbeatTimer.EventHandler = function()
  print("Lost communication!")
  Initialize()
end

function ResetHeartbeat()
  HeartbeatTimer:Stop()
  HeartbeatTimer:Start(HeartbeatTimeout)
end

-- Call ResetHeartbeat() on every valid received message
```

### Polling Timer
```lua
PollTimer = Timer.New()
PollTimer.EventHandler = function()
  if TCP.IsConnected then
    TCP:Write("STATUS\r")
  end
end
PollTimer:Start(3)  -- Every 3 seconds
```

### Error Handling (pcall)
Use `pcall` for operations that may fail (socket/port opens, server listen):
```lua
local ok, err = pcall(function()
  server:Listen(Controls.Port.Value)
end)
if ok then
  print("Listening on port " .. tostring(math.floor(Controls.Port.Value)))
else
  print("Listen failed:", err)
end
```

---

## Data Handling

### JSON
```lua
rapidjson = require("rapidjson")
local data = rapidjson.decode(jsonString)
local json = rapidjson.encode(luaTable)
```

### Hex / Binary Data
```lua
-- Byte string to hex display
function BytesToHex(str)
  return str:gsub(".", function(byte)
    return string.format("%02X ", string.byte(byte))
  end)
end

-- Hex string to byte string
function HexToBytes(str)
  return str:gsub("..", function(byte)
    return string.char(tonumber(byte, 16))
  end)
end
```

### Crypto
```lua
Crypto.Base64Encode(data, withPadding)
Crypto.Base64Decode(data)
Crypto.Sha256(data)
Crypto.Hmac("SHA256", data, key)
```

---

## Design Integration

### Named Components
Access existing design components by name. Store the result in a **global** at the top of the
script and **nil-check** it — a renamed or missing component returns nil, and the failure
otherwise surfaces far from its cause:
```lua
-- Global, declared at the top of the script
Mixer = Component.New("Main Gain")

if Mixer then
  Mixer["input.1.gain"].Value = -6
  Mixer["input.1.mute"].Boolean = true
else
  print("Error: component 'Main Gain' not found")
end
```
Never call `Component.New()` inline inside an event handler or function.

### Notifications (Script-to-Script)
```lua
-- Publisher
Notifications.Publish("my-channel", dataString)

-- Subscriber
local noteId = Notifications.Subscribe("my-channel", function(id, data)
  print("Received:", data)
end)

-- Unsubscribe
Notifications.Unsubscribe(noteId)
```

Q-SYS blocks recursive Notification calls — defer re-entrant publishes with
`Timer.CallAfter(fn, 0)`.

### Multi-Page Plugins
```lua
PageNames = { "Control", "Setup" }

function GetPages(props)
  local pages = {}
  for _, name in ipairs(PageNames) do
    table.insert(pages, { name = name })
  end
  return pages
end

function GetControlLayout(props)
  local layout, graphics = {}, {}
  local CurrentPage = PageNames[props["page_index"].Value]

  if CurrentPage == "Control" then
    -- page 1 layout
  elseif CurrentPage == "Setup" then
    -- page 2 layout
  end
  return layout, graphics
end
```

Dynamic pages require calling the page-name helper in **both** `GetPages` and
`GetControlLayout`.

### PrettyName Hierarchy
Use `~` to create nested groups in UCI/pin views:
```lua
layout["Volume 1"] = {
  PrettyName = "Audio~Inputs~Volume 1",
  -- ...
}
```

---

## Control Types Reference

| Type | Required Field | Values |
|------|---------------|--------|
| Button | `ButtonType` | `"Toggle"`, `"Momentary"`, `"Trigger"` |
| Knob | `ControlUnit` | `"dB"`, `"Hz"`, `"Float"`, `"Integer"`, `"Pan"`, `"Percent"`, `"Position"`, `"Seconds"` |
| Indicator | `IndicatorType` | `"Led"`, `"Meter"`, `"Text"`, `"Status"` |
| Text | — | Style set in layout: `"Text"`, `"ComboBox"`, `"ListBox"` |

---

## Reserved Control Names

These names have special meaning in Q-SYS and enable built-in features when used:
- `Status` — connection status indicator
- `IPAddress` — IP address input
- `Username` / `Password` — credential inputs
- `MACAddress`, `DeviceName`, `SerialNumber`, `DeviceFirmware` — device info displays

`Port` is **not** reserved — it is the conventional companion name for a connection port
control, but Q-SYS does not special-case it. Use it for consistency, not for built-in
behavior.

---

## Reserved Design-Time Functions

All receive `props` parameter (except `GetProperties`):
- `GetColor(props)` — returns `{ R, G, B }` (0–255)
- `GetPrettyName(props)` — display name string
- `GetProperties()` — property definitions table
- `RectifyProperties(props)` — adapt properties dynamically
- `GetPages(props)` — page name table
- `GetControls(props)` — control definitions table
- `GetControlLayout(props)` — returns `layout, graphics` tables
- `GetPins(props)` — audio/serial pin definitions
- `GetComponents(props)` — embedded component definitions
- `GetWiring(props)` — component wiring table

---

## Properties Detail

- Properties are **read-only at runtime**: `Properties["My Prop"].Value`
- Types: `string`, `integer`, `double`, `boolean`, `enum`
- `enum` requires a `Choices` array
- Use `RectifyProperties(props)` to show/hide properties dynamically via `IsHidden`
- `Header` and `Comment` fields supported (QDS 9.10+)

---

## Runtime Environment Detail

- Lua 5.3 runtime with most standard libraries
- Control engine processes at 30 FPS (every 33ms)
- Audio engine processes at 3000 FPS
- Network operations use Q-SYS `TcpSocket` / `UdpSocket` / `HttpClient` / `Ssh` APIs
- Targets Q-SYS Designer 10.1.1+
- `System.IsEmulating` — boolean to detect emulation mode
