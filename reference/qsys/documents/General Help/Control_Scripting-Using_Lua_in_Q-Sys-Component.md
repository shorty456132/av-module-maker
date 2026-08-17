# Component

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/Component.htm

# Component

Component objects allow access to Named Components in the design. To create a Named Component, enable [Code Name and Script Access](../Code_Name_Script_Access.htm) for the component block.

**Note:** The [Code Name and Script Access](../Code_Name_Script_Access.htm) feature takes the place of typing a name on a Component in previous versions of Q-SYS Designer. While it is not expected to affect existing designs, it is possible that adjustments may be needed to some scripts and/or Code Names.

## Methods

[Component.New()](javascript:void(0))

Create a Named Component reference in your script.

### Syntax

Component.New("*named\_component*")

### Example

In this example, we have two Named Components in a design, "gain a" and "gain b". We are watching the gain of "gain a" and muting "gain b" if "gain a" goes above 0 dB.

```lua
gainA = Component.New("gain a")  
gainB = Component.New("gain b")  
gainA.gain.EventHandler = function( ctl )  
 if gainA.gain.Value > 0 then  
  gainB.mute.Boolean = true  
 else  
  gainB.mute.Boolean = false  
 end  
end
```

### Exception

#### Accessing Controls with Decimals

Some controls have names that are frequencies with a decimal. To access these controls in QDS v9.12.0 and later, you must escape the decimal in the script. For instance, to access the Graphic Equalizer component controls in Lua scripting, `31.5Hz.gain` becomes `31\\.5Hz.gain`.

#### Example

```lua
GEC = Component.New("Graphic_Equalizer")  
print(GEC["31\\.5Hz.gain"].Value)
```

[Component.GetComponents()](javascript:void(0))

Returns a Lua table describing all Named Components in the design and their properties.

* With no arguments, returns a table of all Named Components.
* With a `string` argument, returns a table containing only the Named Component with that Code Name, if it exists.

Each entry in the returned table is itself a table that describes one Named Component.

The table contains the following fields:

#### Name

The Code Name of the Named Component.

#### ID

This also contains the Code Name of the Named Components returned by `Component.GetComponents()`, `Name` and `ID` are in this context, identical. Both fields do not imply different behavior.

#### Type

A string that identifies the component's class / type. Instances of the same component class share the same `Type` value. The exact format of this string may vary depending on where the component comes fromâbuilt-in, plugin, extension.

#### ControlSource

This field is primarily used for internal diagnostics and not needed in scripts.

#### Controls

Not usable by Lua scripts.

#### Properties

Table of properties of the named component that are set in Designer at design time. Values can be read, but not changed by a script.

### Syntax

`Component.GetComponents()`

### Examples

[Example 1: Get all named components in the design](javascript:void(0))

In this example, we have a Gain component named MyGain in the design.

```lua
Components = {}                                  --Create a table called Components  
DebugOutput = ""                                 --Build string to be displayed in the Debug Output window  
Components = Component.GetComponents()           --Set Components table equal to the table returned by Component.GetComponents()  
  
  
--Loop through all table entries in the Components table to display their values--------------------------  
for _,v1 in ipairs(Components) do     
  DebugOutput = "\nName: "..v1.Name              --Add the component name to the DebugOutput string  
  DebugOutput = DebugOutput.."\nType: "..v1.Type --Add the component type to the DebugOutput string  
  DebugOutput = DebugOutput.."\nProperties:"     --Add Properties text to the DebugOutput string  
  for _,v2 in ipairs(v1.Properties) do           --Add the list of properties to the DebugOutput string  
    for k3,v3 in pairs(v2) do   
      DebugOutput = DebugOutput.."\n      "..k3.." = "..v3  
    end  
    DebugOutput = DebugOutput.."\n"  
  end   
  print (DebugOutput)                            --Print the DebugOutput string       
end
```

#### Debug Output

```lua
2021-01-04T16:27:53.786	
Name: MyGain
Type: gain
Properties:
      Name = max_gain
      Value = 20
      PrettyName = Max Gain (dB)

      Name = min_gain
      Value = -100
      PrettyName = Min Gain (dB)

      Name = enable_stepper
      Value = False
      PrettyName = Enable Ramp Controls

      Name = step_mode
      Value = 0
      PrettyName = Mode

      Name = num_steps
      Value = 8
      PrettyName = Number of Steps

      Name = multi_channel_type
      Value = 1
      PrettyName = Type

      Name = multi_channel_count
      Value = 8
      PrettyName = Count
```

[Example 2: Another example](javascript:void(0))

```lua
comps = Component.GetComponents()  
  -- iterate components  
 for _,comp in pairs(comps) do  
  print(string.format("Component '%s' of Type '%s'", comp.Name, comp.Type))  
  -- iterate properties  
  print("---- Properties")  
  for _,prop in pairs(comp.Properties) do  
    print(string.format("  %s ( %s ) : %s", prop.PrettyName, prop.Name, prop.Value))  
  end  
end
```

[Component.GetControls()](javascript:void(0))

Returns a table of all controls in the specified Named Component.

**Note:** You can also use Tools > View Component Controls Info to see a list of all controls for a selected component, including a named component. See [Viewing Component Control Information](../../Q-SYS_Designer/Using_the_Schematic/using_controls.htm#Viewing).

### Syntax

Component.GetControls("*named\_component*")

### Examples

[Example 1: Get all controls and their properties](javascript:void(0))

In this example, we have a Blinking LED component named "led". We want to obtain a list of all its controls and their properties.

```lua
blinker = Component.New("led")  
b_ctrls = Component.GetControls(blinker)  
  
print("Component GetControls: ")  
for _,b_element in ipairs(b_ctrls) do  
  print("Name: "..tostring(b_element.Name))  
  print(".\tValue:     "..tostring(b_element.Value))  
  print(".\tString:    "..tostring(b_element.String))  
  print(".\tPosition:  "..tostring(b_element.Position))  
  print(".\tType:      "..tostring(b_element.Type))  
  print(".\tDirection: "..tostring(b_element.Direction))  
  print(".\tMinValue:  "..tostring(b_element.MinValue))  
  print(".\tMaxValue:  "..tostring(b_element.MaxValue))  
  print(".\tMinString: "..tostring(b_element.MinString))  
  print(".\tMaxString: "..tostring(b_element.MaxString))  
end
```

**Note:** `b_element.Boolean`, `RampTime`, and `Index` are omitted from the request since they do not apply in this context.

#### Debug Output

```lua
2019-10-28T18:48:10.938Starting Script
2019-10-28T18:48:10.938Component GetControls: 
2019-10-28T18:48:10.938Name: blink
2019-10-28T18:48:10.939.	Value:     true
2019-10-28T18:48:10.939.	String:    true
2019-10-28T18:48:10.939.	Position:  1.0
2019-10-28T18:48:10.939.	Type:      Boolean
2019-10-28T18:48:10.939.	Direction: Read Only
2019-10-28T18:48:10.939.	MinValue:  0.0
2019-10-28T18:48:10.939.	MaxValue:  1.0
2019-10-28T18:48:10.939.	MinString: false
2019-10-28T18:48:10.939.	MaxString: true
2019-10-28T18:48:10.939Name: duty.cycle
2019-10-28T18:48:10.939.	Value:     50.0
2019-10-28T18:48:10.939.	String:    50.0%
2019-10-28T18:48:10.939.	Position:  0.5
2019-10-28T18:48:10.939.	Type:      Float
2019-10-28T18:48:10.939.	Direction: Read/Write
2019-10-28T18:48:10.939.	MinValue:  10.0
2019-10-28T18:48:10.939.	MaxValue:  90.0
2019-10-28T18:48:10.939.	MinString: 10.0%
2019-10-28T18:48:10.939.	MaxString: 90.0%
2019-10-28T18:48:10.939Name: enable
2019-10-28T18:48:10.939.	Value:     true
2019-10-28T18:48:10.939.	String:    enabled
2019-10-28T18:48:10.939.	Position:  1.0
2019-10-28T18:48:10.939.	Type:      Boolean
2019-10-28T18:48:10.939.	Direction: Read/Write
2019-10-28T18:48:10.939.	MinValue:  0.0
2019-10-28T18:48:10.939.	MaxValue:  1.0
2019-10-28T18:48:10.939.	MinString: disabled
2019-10-28T18:48:10.939.	MaxString: enabled
2019-10-28T18:48:10.939Name: random
2019-10-28T18:48:10.939.	Value:     false
2019-10-28T18:48:10.939.	String:    disabled
2019-10-28T18:48:10.939.	Position:  0.0
2019-10-28T18:48:10.939.	Type:      Boolean
2019-10-28T18:48:10.939.	Direction: Read/Write
2019-10-28T18:48:10.939.	MinValue:  0.0
2019-10-28T18:48:10.939.	MaxValue:  1.0
2019-10-28T18:48:10.939.	MinString: disabled
2019-10-28T18:48:10.939.	MaxString: enabled
2019-10-28T18:48:10.939Name: time
2019-10-28T18:48:10.939.	Value:     10.0
2019-10-28T18:48:10.939.	String:    10.0s
2019-10-28T18:48:10.939.	Position:  1.0
2019-10-28T18:48:10.939.	Type:      Float
2019-10-28T18:48:10.939.	Direction: Read/Write
2019-10-28T18:48:10.939.	MinValue:  0.1
2019-10-28T18:48:10.939.	MaxValue:  10.0
2019-10-28T18:48:10.939.	MinString: 100ms
2019-10-28T18:48:10.939.	MaxString: 10.0s
```
