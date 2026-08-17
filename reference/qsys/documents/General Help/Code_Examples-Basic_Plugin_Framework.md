# Basic Plugin Framework

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Code_Examples/Basic_Plugin_Framework.htm

# Basic Plugin Framework

Q-SYS plugins are small programs for integrating additional functionality in Q-SYS designs. These pieces, written in Lua, are saved in a file with the extension â.qplugâ. Plugins can be manually added by double clicking the qplug file, or by placing it within the correct directory. See [Q-SYS Core OS Environment Overview](../Getting_Started/Q-SYS_Core_OS_Environment_Overview.htm) for more on Lua usage with Q-SYS Designer software.

All Q-SYS plugins start with these top-level functional blocks. Each has a specific purpose for making a plugin within Q-SYS.

[Example](javascript:void(0))

```lua
-- A Basic Plugin  
-- Information block for the plugin  
PluginInfo = {  
  Name = "Base Plugin",  
  Version = "0.0",  
  BuildVersion = "0.0.0.0",  
  Id = "The_Base_Plugin",  
  Author = "QSC",  
  Description = "A very basic plugin"  
}  
  
-- Define the color of the plugin object in the design  
function GetColor(props)  
  return { 102, 102, 102 }  
end  
  
-- The name that will initially display when dragged into a design  
function GetPrettyName(props)  
  return "Base Plugin " .. PluginInfo.Version  
end  
  
-- optional function used if plugin has multiple pages  
function GetPages(props)  
  local pages = {} -- List the pages within the plugin  
  return pages  
end  
  
-- Define User configurable Properties of the plugin  
function GetProperties()  
  local props = {}  
  return props  
end  
  
-- Optional function to define pins on the plugin that are not connected to a control  
function GetPins(props)  
  local pins = {}  
  return pins  
end  
  
-- Optional function to update available properties when properties are altered by the user  
function RectifyProperties(props)  
  return props  
end  
  
-- Optional function to define components used within the plugin  
function GetComponents(props)  
  local components = {}  
  return components  
end  
  
-- Optional function to define wiring of components used within the plugin  
function GetWiring(props)  
  local wiring = {}  
  return wiring  
end  
  
-- Defines the Controls used within the plugin  
function GetControls(props)  
  local ctrls = {}  
  return ctrls  
end  
  
-- Layout of controls and graphics for the plugin UI to display  
function GetControlLayout(props)  
  local layout = {}  
  local graphics = {}  
  return layout, graphics  
end  
  
--Start event based logic  
if Controls then  
  --Script to be executed when the plugin is active (loaded into a core or emulated)  
end
```

## PluginInfo

The PluginInfo object is required. It defines the plugin information.

[PluginInfo Properties](javascript:void(0))

| Name | Type | Required? | Description |
| --- | --- | --- | --- |
| Name | String | Yes | Name of the plugin |
| Version | String | Yes | Current plugin version |
| Id | String | Yes | Unique identifier for the plugin. Must not conflict with other installed plugins |
| Description | String | No | A brief description of the plugin |
| BuildVersion | String | No | Current code iteration tracking |
| Author | String | No | Name or Contact Info of the author |
| Manufacturer | String | No | Name of manufacturer the product the plugin integrates |
| Model | String | No | Model name of the product the plugin integrates |
| IsManaged | Boolean | No | Add the plugin to the managed inventory of the design |
| Type | Reflect Type | No | Reflect reporting type |

## Functions

[GetColor()](javascript:void(0))

Returns a color for the plugin to display. A color is defined by a 4 value table of integers ranging 0-255. The format is { Red, Green, Blue, Alpha }. Alpha is optional.

```lua
-- Define the color of the plugin object in the design  
function GetColor(props)  
  return { 102, 102, 102 }  
end
```

[GetPrettyName(props)](javascript:void(0))

Returns a name for the plugin to initially display when pulled into a design.

```lua
function GetPrettyName(props)  
  return "My First Plugin, version " .. PluginInfo.Version  
end
```

[GetProperties()](javascript:void(0))

Add properties to the plugin object. These are user configurable fields defined before the plugin script code is used. To add a debug property to the plugin:

```lua
function GetProperties()  
  local props = {}  
  table.insert(props, {  
  Name = "Debug Print",  
  Type = "enum",  
  Choices = {"None", "Tx/Rx", "Tx", "Rx", "Function Calls", "All"},  
  Value = "None"  
  })  
  return props  
end
```

[GetPages(props)](javascript:void(0))

Optional. Used when a plugin will have multiple pages of user interface. Returns the table of page name objects. Each page name object must contain a ânameâ property for each desired page. This example defines a global list of page names, and adds them to the plugin using the GetPages function:

```lua
PageNames = { "Control", "Setup" }  --List the pages within the plugin  
function GetPages(props)  
  local pages = {}  
  for ix,name in ipairs(PageNames) do  
    table.insert(pages, {name = PageNames[ix]})  
  end  
  return pages  
end
```

**Note:** PageNames is defined outside the GetPages() function to allow access elsewhere in the plugin.

[GetPins(props)](javascript:void(0))

Optional. Add Pins to the plugin object that are not connected to a control. Controls may have pins not defined here. Pins are defined by an object containing these properties:

| Name | Type | Required? | Description |
| --- | --- | --- | --- |
| Name | String | Yes | Name of the Pin. |
| Direction | âinputâ, âoutputâ or âbothâ | Yes | Defines the pin as an input or output pin |
| Domain | String | No | Defines the type of pin. Audio is defined by default. |

```lua
function GetPins(props)  
  local pins = {}  
  table.insert(pins,{  
    Name = "Audio Output",  
    Direction = "output",  
  })  
  return pins  
end
```

[RectifyProperties(props)](javascript:void(0))

Optional. This function runs after the user changes a property, as a mechanism to adapt global variables and change visibility of properties when appropriate.

```lua
function RectifyProperties(props)  
  if props.plugin_show_debug.Value == false then  
    props["Debug Print"].IsHidden = true  
  end  
  return props  
end
```

[GetComponents(props)](javascript:void(0))

Optional. Returns a table of Component objects to be used within the plugin. This allows other design elements to be wired into the plugin and connected to Lua-scripted logic.

```lua
function GetComponents(props)  
  local components = {}  
  table.insert(components,{  
    Name = "main_mixer",  
    Type = "mixer",  
    roperties =  
      {  
        ["n_inputs"] = 8,  
        ["n_outputs"] = 1,  
      }  
    })  
  return components  
end
```

[GetWiring(props)](javascript:void(0))

Optional. Returns wire objects that wire connections between components and plugin pins. Wire objects are a table of strings, defining the source (first) and the outputs to which a wire connects. Pins must be referenced by component name and pin name. This example fans 2 wires from "Audio Output" to the "main\_mixer" outputs 1 and 2:

```lua
function GetWiring(props)  
  local wiring = {}  
  table.insert( wiring, { "Audio Output", "main_mixer Output 1", "main_mixer Output 2" } )  
  return wiring  
end
```

[GetControls(props)](javascript:void(0))

Return a table containing the Control objects used within the plugin. Controls are persistent data objects stored within the design. They can be bound to user interface components and pins by the plugin.

```lua
function GetControls(props)  
  local ctrls = {}  
  table.insert(ctrls, {  
    Name = "SendButton",  
    ControlType = "Button",  
    ButtonType = "Momentary",  
    Count = 1,  
    UserPin = true,  
    PinStyle = "Input",  
    Icon = "Power"  
  })  
  return ctrls  
end
```

[GetControlLayout(props)](javascript:void(0))

Returns the layout and graphics tables that define the user interface view of the plugin. The layout table is a named set of objects, with the name of each matching the name of the Control to which it is bound. The available Controls are defined in the GetControls() function. The graphics table is the object for any graphics not bound to a Control that are used within the design. To bind the Controls above:

```lua
function GetControlLayout(props)  
  local layout   = {}  
  local graphics = {}  
  local CurrentPage = PageNames[props["page_index"].Value]  
  if CurrentPage == "Control" then  
    table.insert(graphics, {  
      Type = "GroupBox",  
      Text = "Control",  
      Fill = {200, 200, 200},  
      StrokeWidth = 1,  
      Position = {5, 5},  
      Size = {200, 100}  
    })  
    table.insert(graphics,{  
      Type = "Text",  
      Text = "Say Hello:",  
      Position = {10, 42},  
      Size = {90, 16},  
      FontSize = 14,  
      HTextAlign = "Right"  
    })  
    layout["SendButton"] = {  
      PrettyName = "Buttons~Send The Command",  
      Style = "Button",  
      Position = {105, 42},  
      Size = {50, 16},  
      Color = {0, 0, 0}  
    }  
  elseif CurrentPage == "Setup" then  
    -- TBD  
  end  
  return layout, graphics  
end
```

## Runtime Code

To determine if the plugin is being shown to the user in Design mode, or if it has been loaded or emulated and is in Runtime mode, check for the Controls object. When the Controls object is present, the design has been loaded. Add Runtime Lua code for your plugin here.

[Example](javascript:void(0))

```lua
--Start event based logic  
if Controls then  
  Controls.SendButton.EventHandler = function()  
    print("Hello, World!")  
  end  
end
```

## Final Result

The final result is a plugin that can be pulled into Q-SYS design, providing the user with a functioning button that outputs to a Debug Output frame:

[Complete Example Code](javascript:void(0))

```lua
-- Basic Framework Plugin  
-- by QSC  
-- October 2020  
  
-- Information block for the plugin  
PluginInfo = {  
    Name = "Base Plugin",  
    Version = "0.0",  
    BuildVersion = "0.0.0.1",  
    Id = "ec6076c1-4d4e-4f40-bc5d-03e5f7126edf",  
    Author = "QSC",  
    Description = "A very basic plugin"    
  }  
    
  -- Define the color of the plugin object in the design  
  function GetColor(props)  
    return { 102, 102, 102 }  
  end  
    
  -- The name that will initially display when dragged into a design  
  function GetPrettyName(props)  
    return "My First Plugin, version " .. PluginInfo.Version  
  end  
    
  -- Optional function used if plugin has multiple pages  
  PageNames = { "Control", "Setup" }  --List the pages within the plugin  
  function GetPages(props)  
    local pages = {}  
    for ix,name in ipairs(PageNames) do  
      table.insert(pages, {name = PageNames[ix]})  
    end  
    return pages  
  end  
    
  -- Define User configurable Properties of the plugin  
  function GetProperties()  
    local props = {}  
    table.insert(props, {  
      Name = "Debug Print",  
      Type = "enum",  
      Choices = {"None", "Tx/Rx", "Tx", "Rx", "Function Calls", "All"},  
      Value = "None"  
    })  
    return props  
  end  
    
  -- Optional function to define pins on the plugin that are not connected to a Control  
  function GetPins(props)  
    local pins = {}  
    table.insert(pins,{  
      Name = "Audio Output",  
      Direction = "output",  
    })  
    return pins  
  end  
    
  -- Optional function to update available properties when properties are altered by the user  
  function RectifyProperties(props)  
    if props.plugin_show_debug.Value == false then   
      props["Debug Print"].IsHidden = true   
    end  
    return props  
  end  
    
  -- Optional function to define components used within the plugin  
  function GetComponents(props)  
    local components = {}  
    table.insert(components,{  
      Name = "main_mixer",  
      Type = "mixer",  
      Properties =     
      {  
        ["n_inputs"] = 8,  
        ["n_outputs"] = 1,  
      }  
    })  
    return components  
  end  
    
  -- Optional function to define wiring of components used within the plugin  
  function GetWiring(props)  
    local wiring = {}  
    table.insert( wiring, { "Audio Output", "main_mixer Output 1" } )  
    return wiring  
  end  
    
  -- Defines the Controls used within the plugin  
  function GetControls(props)  
    local ctrls = {}  
    table.insert(ctrls, {  
      Name = "SendButton",  
      ControlType = "Button",  
      ButtonType = "Momentary",  
      Count = 1,  
      UserPin = true,  
      PinStyle = "Input",  
      Icon = "Power"  
    })  
    return ctrls  
  end  
    
  --Layout of controls and graphics for the plugin UI to display  
  function GetControlLayout(props)  
    local layout = {}  
    local graphics = {}  
    local CurrentPage = PageNames[props["page_index"].Value]  
    if CurrentPage == "Control" then  
      table.insert(graphics,{  
        Type = "GroupBox",  
        Text = "Control",  
        Fill = {200,200,200},  
        StrokeWidth = 1,  
        Position = {5,5},  
        Size = {200,100}  
      })  
      table.insert(graphics,{  
        Type = "Text",  
        Text = "Say Hello:",  
        Position = {10,42},  
        Size = {90,16},  
        FontSize = 14,  
        HTextAlign = "Right"  
      })  
      layout["SendButton"] = {  
        PrettyName = "Buttons~Send The Command",  
        Style = "Button",  
        Position = {105,42},  
        Size = {50,16},  
        Color = {0,0,0}  
      }  
    elseif CurrentPage == "Setup" then  
      -- TBD  
    end  
    return layout, graphics  
  end  
    
  --Start event based logic  
  if Controls then  
    Controls.SendButton.EventHandler = function()  
      print("Hello, World!")  
    end  
  end  
  
```
