---
name: create-plugin
description: Scaffold a complete Q-SYS plugin from scratch, creating all required Lua files with correct structure and cross-references
argument-hint: plugin description
---

# Create Q-SYS Plugin

Create a complete Q-SYS plugin based on the following description:

**$ARGUMENTS**

## Output Directory

Before creating any files, ask the user where they want the plugin files placed. Suggest a default directory name based on the plugin name (e.g., `./My-Plugin/`). Create the directory if it doesn't exist, then write all `.lua` files into it.

## Q-SYS Reference Documentation

When the plugin interacts with Q-SYS components or features, confirm behaviors, parameter names, and value ranges against the help docs before designing controls, properties, and runtime logic. This prevents creating controls that don't match how Q-SYS actually works.

**Do not Grep or Read `${CLAUDE_PLUGIN_ROOT}/reference/qsys/documents/` in this thread** — the corpus is ~800 files, many 25–65 KB, and reading them inline exhausts the context window. Delegate every Q-SYS API or component question to a read-only subagent instead:

Call the **Agent tool with `subagent_type: "Explore"`** and give it:

1. **The search root** — `${CLAUDE_PLUGIN_ROOT}/reference/qsys/documents/`
2. **The question**, in this shape:

   ```
   Query:         [natural-language question]
   API hint:      [e.g. Component.New, GetControlLayout, TcpSocket, rapidjson]
   Doc area hint: [e.g. Control Scripting, Schematic Library, SDK / Plugin, Code Examples]
   What's needed: [syntax | example | property/method list | gotchas | all]
   ```
3. **The output contract** — return only the relevant excerpts plus the file paths they came from. No file dumps.

Useful doc-area hints: `Schematic_Library-*` (Q-SYS components), `Control_Scripting-*` (Lua API), `External_Control_APIs-*`, `Hardware-*`, `Networking-*`, `Application_Integration-*`, and in `SDK Help/`: `Getting_Started-*`, `Standards_Definitions-*`, `Code_Examples-*`, `Recommended_Practices-*`, `Development_Tools-*`.

If the agent reports **Not found**, fall back to a pattern in `QSYS_PATTERNS.md` or ask the user — never invent Q-SYS API behavior from memory.

Also read `${CLAUDE_PLUGIN_ROOT}/reference/qsys/QSYS_PATTERNS.md` before writing Lua — most common needs (sockets, timers, JSON, control types, reserved names) are already answered there, no subagent required. And read `${CLAUDE_PLUGIN_ROOT}/reference/qsys/QSYS_CONSTRAINTS.md` before writing or revising any Lua — it covers design-time vs runtime rules, control-array conventions, naming/scoping rules, and the platform's most common pitfalls.

## Connection Settings as Runtime Controls (IMPORTANT)

Device connection details like **IP addresses, port numbers, display IDs, device keys, usernames, and passwords** must be **runtime-settable controls**, NOT properties. Properties are baked in at design-time and cannot be changed without editing the design.


**Rules:**
- Create these as **Text controls** in `controls.lua` (e.g., `IPAddress`, `Port`, `DeviceID`)
- Place them on a **"Setup"** or **"Settings" page** in `layout.lua` — separate from the main control page
- In `runtime.lua`, read connection values from `Controls["IPAddress"].String`, `Controls["Port"].String`, etc.
- Use the Q-SYS reserved control names where applicable: `IPAddress`, `Username`, `Password` — these enable built-in Q-SYS features
- The plugin should have at least 2 pages: **"Control"** (main controls) and **"Setup"** (connection settings)
- Only put things in **properties** that truly need to be design-time only (e.g., number of channels, model selection, protocol type)

**Example controls.lua pattern for connection settings:**
```lua
table.insert(ctrls, {
  Name = "IPAddress",
  ControlType = "Text",
  Count = 1,
  UserPin = true,
  PinStyle = "Both"
})
table.insert(ctrls, {
  Name = "Port",
  ControlType = "Text",
  Count = 1,
  UserPin = true,
  PinStyle = "Both"
})
table.insert(ctrls, {
  Name = "Connect",
  ControlType = "Button",
  ButtonType = "Toggle",
  Count = 1,
  UserPin = true,
  PinStyle = "Both"
})
table.insert(ctrls, {
  Name = "Status",
  ControlType = "Indicator",
  IndicatorType = "Status",
  Count = 1,
  UserPin = true,
  PinStyle = "Output"
})
```

**Example runtime.lua pattern using connection controls:**
```lua
function Initialize()
  local ip = Controls["IPAddress"].String
  local port = tonumber(Controls["Port"].String) or 23
  if ip ~= "" and Controls["Connect"].Boolean then
    TCP:Connect(ip, port)
  end
end

Controls["Connect"].EventHandler = function(ctl)
  if ctl.Boolean then
    Initialize()
  else
    TCP:Disconnect()
  end
end
```

## Protocol & Command Discovery

If the plugin description involves communicating with a device (mentions TCP, UDP, Serial, HTTP, SSH, or a specific device brand/model), you **must** gather the device's control protocol details **before generating any files**. This ensures the correct commands, responses, and parsing logic are built into the plugin from the start.

### Step 1: Ask for Protocol Source

Use `AskUserQuestion` to ask how the user wants to provide protocol information:

- **"I have a protocol doc"** — Ask the user for the file path, URL, or to paste the protocol details. Read the document using `Read` (for local files/PDFs) or `WebFetch` (for URLs) and extract the relevant command set.
- **"Search the web"** — Use `WebSearch` to find the manufacturer's control protocol documentation (e.g., search for `"<brand> <model> RS-232 control protocol"` or `"<brand> <model> API commands"`). Use `WebFetch` to read the most relevant results. If no reliable protocol docs are found, inform the user and fall back to manual entry.
- **"I'll provide commands manually"** — Ask the user to describe or list the commands the plugin needs to send and the expected responses.

### Step 2: Extract & Organize Commands

From the gathered protocol information, identify and organize:

1. **Connection details** — protocol type (TCP/UDP/Serial/HTTP), default port, baud rate, delimiter/EOL characters
2. **Command format** — structure of commands (e.g., fixed strings, hex bytes, headers/footers, checksums)
3. **Command list** — specific commands for each function the plugin needs (power on/off, input select, volume, mute, etc.)
4. **Response format** — how the device responds (acknowledgment strings, status responses, error codes)
5. **Polling** — whether the device supports status polling and what commands to use

### Step 3: Confirm with the User

Present a summary of the discovered commands and protocol details to the user. Ask them to confirm the command set is correct or provide corrections before proceeding to file generation.

**Example summary format:**
```
Protocol: TCP, Port 23, Delimiter: \r
Commands found:
  - Power On:  "POWR 1\r"  → Response: "POWR=1\r"
  - Power Off: "POWR 0\r"  → Response: "POWR=0\r"
  - Input HDMI1: "INPT 1\r" → Response: "INPT=1\r"
  - Volume Set: "VOLM <value>\r" → Response: "VOLM=<value>\r"
  - Mute On: "AMUT 1\r" → Response: "AMUT=1\r"
  - Status Poll: "POWR?\r" → Response: "POWR=<0|1>\r"
```

If the plugin does **not** communicate with a device (e.g., a utility or logic-only plugin), skip this section entirely.

## You Must Create ALL Files

You are responsible for creating and populating **every** `.lua` file listed below. None are pre-filled or auto-generated. You must author each one with the correct content for this specific plugin.

### Required Files

| File | Purpose |
|------|---------|
| `plugin.lua` | Main entry point that defines all Q-SYS lifecycle functions and includes all other Lua files via `#include` directives. |
| `info.lua` | Declares the `PluginInfo` table with plugin metadata: Name, Version, BuildVersion, GUID, Author, and Description. |
| `properties.lua` | Defines user-configurable properties by inserting entries into the `props` table (inserted into `GetProperties`). |
| `controls.lua` | Defines all plugin controls by inserting entries into the `ctrls` table (inserted into `GetControls`). |
| `layout.lua` | Defines visual positioning and styling of controls in Q-SYS Designer UI (inserted into `GetControlLayout`). Uses `PageNames` and `props["page_index"]` for multi-page layouts. |
| `runtime.lua` | Contains all runtime logic: component references, variables, functions, event handlers, and initialization code. Executes on the Q-SYS Core when the design is running. |
| `pages.lua` | Iterates `PageNames` to build the pages table for multi-page plugin layouts (inserted into `GetPages`). |
| `model.lua` | Defines model variants for the plugin based on `props.Model` property (inserted into `GetModel`). |
| `components.lua` | Declares embedded Q-SYS components used within the plugin (inserted into `GetComponents`). Leave empty if not needed. |
| `pins.lua` | Declares external pins on the plugin block not tied to a control (inserted into `GetPins`). Leave empty if not needed. |
| `wiring.lua` | Defines wiring connections between embedded components (inserted into `GetWiring`). Leave empty if not needed. |
| `rectify_properties.lua` | Adjusts property visibility/availability based on current property values (inserted into `RectifyProperties`). Leave empty if not needed. |
| `README.md` | Documents the plugin: what it does, how to configure it, properties, controls, and any protocol/setup notes. |

## How It Works

`plugin.lua` is the **entry point and orchestrator**. It defines every Q-SYS plugin lifecycle function and delegates each one to a separate `.lua` file using `--[[ #include "filename.lua" ]]`. At compile time, the `compile` skill (`${CLAUDE_PLUGIN_ROOT}/scripts/compile.py`) resolves these include directives and produces a monolithic `.qplug` file that Q-SYS Designer can load.

### Two Execution Phases

See the design-time vs runtime constraints in `${CLAUDE_PLUGIN_ROOT}/reference/qsys/QSYS_CONSTRAINTS.md`. The structural consequence for scaffolding: design-time lifecycle functions occupy the body of `plugin.lua`, and the `if Controls then` block at its bottom is what includes `runtime.lua` on the Core.

## plugin.lua Template

Use this exact structure for `plugin.lua`:

```lua
-- Plugin Name
-- by Author Name
-- Date

-- Information block for the plugin
--[[ #include "info.lua" ]]

-- Define the color of the plugin object in the design
function GetColor(props)
  return { 102, 102, 102 }
end

-- The name that will initially display when dragged into a design
function GetPrettyName(props)
  return "Plugin Display Name, version " .. PluginInfo.Version
end

-- Optional function used if plugin has multiple pages
PageNames = { "Control" }  --List the pages within the plugin
function GetPages(props)
  local pages = {}
  --[[ #include "pages.lua" ]]
  return pages
end

-- Optional function to define model if plugin supports more than one model
function GetModel(props)
  local model = {}
  --[[ #include "model.lua" ]]
 return model
end

-- Define User configurable Properties of the plugin
function GetProperties()
  local props = {}
  --[[ #include "properties.lua" ]]
  return props
end

-- Optional function to define pins on the plugin that are not connected to a Control
function GetPins(props)
  local pins = {}
  --[[ #include "pins.lua" ]]
  return pins
end

-- Optional function to update available properties when properties are altered by the user
function RectifyProperties(props)
  --[[ #include "rectify_properties.lua" ]]
  return props
end

-- Optional function to define components used within the plugin
function GetComponents(props)
  local components = {}
  --[[ #include "components.lua" ]]
  return components
end

-- Optional function to define wiring of components used within the plugin
function GetWiring(props)
  local wiring = {}
  --[[ #include "wiring.lua" ]]
  return wiring
end

-- Defines the Controls used within the plugin
function GetControls(props)
  local ctrls = {}
  --[[ #include "controls.lua" ]]
  return ctrls
end

--Layout of controls and graphics for the plugin UI to display
function GetControlLayout(props)
  local layout = {}
  local graphics = {}
  --[[ #include "layout.lua" ]]
  return layout, graphics
end

--Start event based logic
if Controls then
  --[[ #include "runtime.lua" ]]
end
```

## File Content Details

### info.lua

**IMPORTANT:** Every plugin must have a unique `Id` in UUID/GUID format. When creating `info.lua`, you MUST generate a random unique ID in the format `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` where each `x` is a random hexadecimal character (0-9, a-f). Make every digit truly random — do not reuse patterns or use obvious sequences. Each plugin must get a different ID.

```lua
PluginInfo = {
  Name = "Plugin Name",
  Version = "1.0.0",
  BuildVersion = "1.0.0.0",
  Id = "a1b2c3d4-e5f6-7890-abcd-ef1234567890",  -- unique random GUID per plugin
  Author = "Author Name",
  Description = "Description of what the plugin does"
}
```

### properties.lua
Insert property definitions into the `props` table. Available property types: `string`, `integer`, `double`, `boolean`, `enum`.
```lua
table.insert(props, {
  Name = "Property Name",
  Type = "enum",
  Choices = {"Option1", "Option2", "Option3"},
  Value = "Option1"  -- default value
})
```

### controls.lua
Insert control definitions into the `ctrls` table. ControlType options: `Button`, `Knob`, `Indicator`, `Text`, `Meter`, `Header`.

**Single controls:**
```lua
table.insert(ctrls, {
  Name = "My Control",
  ControlType = "Button",
  ButtonType = "Toggle",    -- Toggle, Trigger, On, Off, Custom
  Count = 1,
  UserPin = true,           -- expose as a pin
  PinStyle = "Both",        -- Input, Output, Both, None
})
```

**Arrays of controls — IMPORTANT:** Never use `Count` > 1. Drive a loop from an integer property to create individually named controls (`"Mute1"`, `"Mute2"`) — the full four-file walkthrough (properties → controls → layout → runtime) is in `${CLAUDE_PLUGIN_ROOT}/reference/qsys/QSYS_PATTERNS.md`.

Two things the scaffold must get right: the same loop bound must be read in all three files (`props["Channel Count"].Value` at design time, `Properties["Channel Count"].Value` at runtime), and the name expression must be character-identical everywhere (`"Mute" .. i` — no space before the index).

### layout.lua
Position controls using a `layout` table keyed by control name. Uses `props["page_index"]` for multi-page support.

**Visual Design Requirements — Every plugin layout MUST follow these rules:**

1. **Include the build version in the bottom left of each plugin**
1. **Use a dark background GroupBox** as the plugin canvas (first graphic, lowest ZOrder)
2. **Group related controls** inside lighter GroupBox sections with descriptive titles
3. **Use Header graphics** to label major sections
4. **Use Label graphics** next to every control so users know what each control does
5. **Ensure text contrast** — use light text (`{255,255,255}` or `{221,221,221}`) on dark backgrounds, dark text (`{0,0,0}`) on light backgrounds
6. **Color buttons meaningfully** — e.g., green for connect/enable, red for disconnect/stop, blue for actions, gray for settings
7. **Use `UnlinkOffColor`** on toggle buttons so on/off states are visually distinct (e.g., green on, dark gray off)
8. **Set `ButtonVisualStyle = "Flat"`** for a modern, clean look
9. **Set `CornerRadius`** on buttons (4–8px) and GroupBoxes (8px) for rounded edges
10. **Use consistent spacing** — align controls on a grid, use uniform padding (10px from GroupBox edges, 5px between controls)
11. **Set `FontSize`** appropriately — 14+ for headers, 11–12 for labels, 10 for small status text
12. **Use the `Legend` property** on buttons to label them instead of relying on separate text labels
13. **Use `Icon` on buttons** when applicable — e.g., `Icon = "Power"` for power buttons in the control definition (`controls.lua`)
14. **Status indicators** should use LED style with colored on/off states
15. **Size controls appropriately** — buttons at least `{80, 24}`, text fields at least `{150, 24}`, LEDs `{16, 16}`

**Available layout Style values:** `"Fader"`, `"Knob"`, `"Button"`, `"Text"`, `"Meter"`, `"Led"`, `"ListBox"`, `"ComboBox"`, `"Media"`, `"None"`

**Available graphic Type values:** `"Label"`, `"GroupBox"`, `"Header"`, `"Image"`, `"Svg"`

**Available fonts:** `"Roboto"` (default), `"Montserrat"`, `"Open Sans"`, `"Lato"`, `"Poppins"`, `"Roboto Mono"` (monospace), `"Noto Serif"`, `"Roboto Slab"`

**Example of a well-styled layout:**
```lua
local CurrentPage = PageNames[props["page_index"].Value]

if CurrentPage == "Control" then
  -- Plugin background
  table.insert(graphics, {
    Type = "GroupBox",
    Fill = { 35, 35, 35 },
    StrokeColor = { 35, 35, 35 },
    StrokeWidth = 0,
    CornerRadius = 0,
    Position = { 0, 0 },
    Size = { 400, 300 },
    ZOrder = -10
  })

  -- Connection section group
  table.insert(graphics, {
    Type = "GroupBox",
    Text = "Connection",
    Fill = { 55, 55, 55 },
    Color = { 221, 221, 221 },
    StrokeColor = { 80, 80, 80 },
    StrokeWidth = 1,
    CornerRadius = 8,
    Font = "Roboto",
    FontSize = 11,
    Position = { 10, 10 },
    Size = { 380, 80 },
    ZOrder = -5
  })

  -- IP Address label
  table.insert(graphics, {
    Type = "Label",
    Text = "IP Address",
    Color = { 200, 200, 200 },
    FontSize = 11,
    Font = "Roboto",
    HTextAlign = "Right",
    Position = { 20, 35 },
    Size = { 80, 24 }
  })

  -- IP Address text field
  layout["IPAddress"] = {
    PrettyName = "Connection~IP Address",
    Style = "Text",
    Position = { 105, 35 },
    Size = { 150, 24 },
    FontSize = 11,
    Color = { 255, 255, 255 },
    CornerRadius = 4
  }

  -- Connect button (green on, dark off)
  layout["Connect"] = {
    PrettyName = "Connection~Connect",
    Style = "Button",
    ButtonStyle = "Toggle",
    ButtonVisualStyle = "Flat",
    Position = { 270, 35 },
    Size = { 100, 24 },
    Color = { 0, 180, 80 },
    OffColor = { 80, 80, 80 },
    UnlinkOffColor = true,
    Legend = "Connect",
    FontSize = 12,
    CornerRadius = 4
  }

  -- Status LED
  layout["Status"] = {
    PrettyName = "Connection~Status",
    Style = "Led",
    Position = { 20, 60 },
    Size = { 16, 16 },
    Color = { 0, 255, 0 },
    OffColor = { 100, 0, 0 },
    UnlinkOffColor = true
  }

  -- Section header
  table.insert(graphics, {
    Type = "Header",
    Text = "Controls",
    Color = { 221, 221, 221 },
    Font = "Roboto",
    FontSize = 14,
    FontStyle = "Bold",
    HTextAlign = "Left",
    Position = { 10, 100 },
    Size = { 380, 20 }
  })
end
```

**Looped control layout — when using control arrays:** see `${CLAUDE_PLUGIN_ROOT}/reference/qsys/QSYS_PATTERNS.md`. Stride the varying axis off the loop index (`Position = { 20 + (60 * (i - 1)), 50 }` for a row of faders) and use `string.format("Channel~Volume %i", i)` for the `PrettyName` so the pin tree groups cleanly.

### runtime.lua

#### TCP/UDP Recommended Practices

When a plugin communicates with a device via TCP, UDP, or serial, start from the transport pattern in `${CLAUDE_PLUGIN_ROOT}/reference/qsys/QSYS_PATTERNS.md` — it covers socket setup, event handlers, and buffer reading for all three.

If the plugin needs behavior beyond those patterns (TCP server management, UDP broadcast/multicast or network interface binding, non-standard serial framing), dispatch an `Explore` subagent to the matching recommended-practices doc rather than reading it here:

- **TCP Client or TCP Server**: `${CLAUDE_PLUGIN_ROOT}/reference/qsys/documents/SDK Help/Recommended_Practices-TCP.md`
- **UDP (one-way, two-way, server, broadcast, multicast)**: `${CLAUDE_PLUGIN_ROOT}/reference/qsys/documents/SDK Help/Recommended_Practices-UDP.md`
- **Serial**: `${CLAUDE_PLUGIN_ROOT}/reference/qsys/documents/SDK Help/Recommended_Practices-Serial.md`

Pass the subagent the absolute file path and ask for the specific excerpt you need.

**TCP Timeout rules**: Set `TCP.ReadTimeout = 0` and `TCP.WriteTimeout = 0` (disabled) by default for TCP client connections. Only set non-zero timeout values when the socket is used as a **TCP server** (TcpSocketServer) where idle connection cleanup is desired.

#### Using Gathered Protocol Information

If protocol discovery was performed (see "Protocol & Command Discovery" section), use the confirmed command set to generate:
- **Command functions** — dedicated `Send` functions or a command dispatch table using the exact command strings/bytes from the protocol spec
- **Response parsing** — parse handlers that match the device's actual response format (delimiters, acknowledgments, status strings)
- **Polling logic** — use the correct status query commands identified during discovery
- **Error handling** — handle device-specific error codes or NAK responses

Do **not** guess or invent commands. Use only what was confirmed by the user or found in the protocol documentation.

#### Control Array Event Handlers

Mirror the controls.lua loop in runtime.lua (base pattern and the loop-variable capture rule: `${CLAUDE_PLUGIN_ROOT}/reference/qsys/QSYS_PATTERNS.md`). The plugin-specific part is the body — emit the device command for that channel:
```lua
local numChannels = Properties["Channel Count"].Value
for i = 1, numChannels do
  local idx = i  -- capture
  Controls["Mute" .. idx].EventHandler = function(ctl)
    Send("MUTE " .. idx .. " " .. (ctl.Boolean and "1" or "0") .. "\r")
  end
  Controls["Volume" .. idx].EventHandler = function(ctl)
    Send("VOL " .. idx .. " " .. tostring(math.floor(ctl.Value)) .. "\r")
  end
end
```

Control names (`"Mute1"`, `"Volume1"`, …) must match exactly across controls.lua, layout.lua, and runtime.lua.

Structure your runtime logic with clear sections:
```lua
--[[ Description
    Describe the plugin's runtime behavior
]]

--------------------
-- Components ------
--------------------
-- End Components --

--------------------
-- Variables -------
--------------------
-- End Variables ---

--------------------
-- Functions -------
--------------------
-- End Functions ---

--------------------
-- EventHandlers ---
--------------------
--End Eventhandlers-

-- Initialize --
```

#### Debug Logging

Follow the debug logging rules in `${CLAUDE_PLUGIN_ROOT}/reference/qsys/QSYS_CONSTRAINTS.md` — required for every plugin that talks to a device. The socket state/error handlers that carry those prints are in the transport patterns in `${CLAUDE_PLUGIN_ROOT}/reference/qsys/QSYS_PATTERNS.md`; funnel TX/RX through a single pair of functions so every command and response is traced from one place:

```lua
function Send(cmd)
  print("TX: " .. cmd)
  TCP:Write(cmd .. "\r\n")
end

function ParseResponse(data)
  print("RX: " .. data)
  -- parsing logic...
end
```

When logging the connection target, read it from the Setup-page control (`Controls["IPAddress"].String`) — never from a property.

### pages.lua
```lua
for ix,name in ipairs(PageNames) do
  table.insert(pages, {name = PageNames[ix]})
end
```

### model.lua
```lua
if props.Model ~= nil and props.Model.Value ~= "" then
  table.insert(model, { props.Model.Value } )
else
  table.insert(model, { "Base Model" } )
end
```

### rectify_properties.lua
```lua
-- Example: hide Debug Print property when not needed
if props.plugin_show_debug.Value == false then
  props["Debug Print"].IsHidden = true
end
```

### README.md
Create a README.md in the plugin directory that documents:

1. **Plugin name and description** — what the plugin does and what device/system it controls
2. **Properties** — list each property with its type, default value, and purpose
3. **Controls** — list each control with its type and what it does
4. **Setup instructions** — how to configure the plugin in Q-SYS Designer (IP address, port, credentials, etc.)
5. **Protocol notes** — if the plugin uses a specific protocol (TCP, UDP, HTTP, Serial), briefly describe the communication details (port, command format, etc.)
6. **Pages** — if multi-page, describe what each page contains

Keep the README concise and practical — focused on what a user needs to get the plugin working.

## Creation Order

Follow this order to ensure dependencies are satisfied:

0. **Protocol discovery** — Gather device commands/responses if the plugin communicates with a device (see "Protocol & Command Discovery" section above)
1. **info.lua** — Plugin metadata (no dependencies)
2. **properties.lua** — Properties (no dependencies)
3. **controls.lua** — Controls (may reference property names for Count)
4. **pages.lua** — Page definitions (references `PageNames` from plugin.lua)
5. **layout.lua** — Layout (references control names from controls.lua, page names from plugin.lua)
6. **runtime.lua** — Runtime logic (references control names from controls.lua, property names from properties.lua)
7. **model.lua** — Model variants (usually static)
8. **plugin.lua** — Orchestrator (references `PageNames`, includes all files)
9. **components.lua**, **pins.lua**, **wiring.lua**, **rectify_properties.lua** — Supporting files as needed
10. **README.md** — Plugin documentation

## Consistency Checklist

Before finishing, verify:

- [ ] Every `Controls["..."]` reference in `runtime.lua` has a matching entry in `controls.lua`
- [ ] Every control defined in `controls.lua` has a layout entry in `layout.lua`
- [ ] Every `Properties["..."]` or `props["..."]` reference has a matching definition in `properties.lua`
- [ ] `PageNames` in `plugin.lua` matches the pages handled in `layout.lua`
- [ ] No Q-SYS reserved control names or function names are used
- [ ] All `table.insert` calls target the correct local variable (`ctrls`, `props`, `pages`, etc.)
- [ ] Control arrays use property-driven loops (not `Count` > 1) with matching names across controls.lua, layout.lua, and runtime.lua
- [ ] Looped control names are consistent (e.g., `"Mute" .. i` produces `"Mute1"`, `"Mute2"` — same pattern in all files)

## Compiling

After all files are created, compile the plugin into a single `.qplug` file:

```
python "${CLAUDE_PLUGIN_ROOT}/scripts/compile.py" <plugin-directory>
```

This resolves all `--[[ #include ]]` directives and outputs a `.qplug` file in the plugin directory. Offer to run this for the user after creating all files.
