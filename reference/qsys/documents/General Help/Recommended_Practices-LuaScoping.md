# Lua Scopes

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Recommended_Practices/LuaScoping.htm

# Lua Scopes

In Lua, a variable can either be local or global. By default, all variables defined by the user are globally scoped, while function parameters and loop iterators are locally scoped.

**Note:** The following guidance applies to Lua development for Q-SYS and might not apply to other platforms where Lua is implemented.

## TLDR

Only use the local scope for temporary variables used in functions. Assign values you need later to a global variable or table. In summary, only use local when needed; otherwise, leave the variable, function, or object global.

## Simplified Description of Lua Garbage Collection

Lua has automatic memory management, meaning that you don't have to explicitly clean items out of memory when not needed anymore. These include:

* variables and objects set to nil
* function parameters
* local variables after a function executes
* for loop iterators

**Note:** Read more about Garbage Collection in Q-SYS Help, [here](https://help.qsys.com/#Control_Scripting/Lua_5.3_Reference_Manual/2_-_Basic_Concepts.htm#5).

## The Global Table

The global table, defined as `_G` in Lua, is the topmost variable in Lua where all other variables, functions, and objects live.

Any item defined without the local keyword prefixing it will be assumed to be global to that script.

Global Tables are not shared amongst separate scripts. All Lua scripts run in isolated environments.

## When to use the local scope in scripts

It is recommended to use the local scope for variables that are used solely within that function. For example, if you have an iterator or the result of a function call that is only needed in that scope, assign the local tag to it.

For Lua modules, locally scoping variables will keep them private to the module.

## When NOT to use the local scope in scripts

Anything at the top level of your script should not have the local scope assigned to it. This includes the runtime code wrapped in the `if Controls then ... end` within a plugin.

Timers should never be locally scoped and should be stopped â and their event handlers escaped â before setting to nil, if needed.

## Examples

[Scope Examples](javascript:void(0))

Scope Examples

```lua
-- global variables  
myString = "Hello, World!"  
myNumber = 42  
myBoolean = true  
myTable = {}  
myPlaceHolder = nil  
  
-- function with local variable  
function formatMessage(message)  
  -- message is locally scoped to the function as a parameter  
  local formattedMessage = Header .. tostring(message) .. "\r\n" -- local variable used only in this function  
  print("Sending: " .. formattedMessage)  
  return formattedMessage  
end  
  
-- basic loops  
for x = 1, 10 do  
  -- x is locally scoped to the loop  
  print(x)  
end
```

[Using the global table to access embedded components](javascript:void(0))

```lua
 -- Part of GetComponents(props)  
 for x = 1, (props["Output Count"].Value) do  
  table.insert(  
    components,  
    {  
      Name = "XFader" .. x,  
      Type = "crossfader",  
      Properties = {  
        ["multi_channel_type"] = multiTypeIndex,  
        ["multi_channel_count"] = props["Count"].Value  
      }  
    }  
  )  
 end  
  
  
-- Part of runtime  
local XFaders = {}  
for i = 1, Properties["Output Count"].Value do  
  table.insert(XFaders, _G["XFader" .. i])  
end
```

## Known Issues

[Known variables that need to be assigned to a global variable or table](javascript:void(0))

* socket parameters passed by TcpSocketServer.EventHandler()
* USB device parameters passed by UsbMonitor.EventHandler()
* Midi device parameters passed by MidiMonitor.EventHandler()

[Known objects that should never be locally scoped](javascript:void(0))

* Timers
* Websockets
* Serial Ports
* Serial Server ports
* Sockets

  + TCP
  + UDP
  + SSH
