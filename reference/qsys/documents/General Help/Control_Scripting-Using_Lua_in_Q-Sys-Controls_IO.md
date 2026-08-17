# Controls IO

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/Controls_IO.htm

# Controls IO

[Controls.Inputs](javascript:void(0))

Table representing a [Control Script](../../Schematic_Library/control_script_2.htm)'s input pins, used to access the properties and methods of controls wired to the control script.  .EventHandler is used to assign event handlers to inputs.

| Properties | | |
| --- | --- | --- |
| Name | Attribute | Comment |
| .Value | Read Only | Floating point value of control. If you pass in a Boolean ( like `Controls.Outputs[1].Value = true` ) it is converted to either a `0` ( false ) or `1` ( true ). |
| .Values | Read Only | Table of floating point values of controls. Only used when connected to controls that create tables of values such as the 2D panner, RTA - Band-Pass or Responsalyzer, Meters. |
| .Position | Read Only | floating point position which goes from 0.0 -> 1.0 |
| .String | Read Only | string representation of control value |
| .Boolean | Read Only | returns true if the position of the control is >0.5 |
| .Index | Read Only | index of control. |
| .EventHandler | â | called when input value changes |
| If you reference a Controls.Inputs[ *n*] in your script, and there is nothing connected to that input on the Control Script component, the following error displays in the debug log: `[string "<input name>..."]:43: attempt to index global '<index field name>' (a nil value)`. | | |

[Remarks](javascript:void(0))

Controls.Inputs is a Lua table.  Tables in Lua are not copied when they are assigned a new variable name, thus statements like:  `input1 = Controls.Inputs[1]` does not create a copy of Controls.Inputs in input1, input1 points at the original table.

While Controls.Inputs is primarily intended for reading from the inputs, it is possible to write to the inputs.

```lua
Controls.Inputs[1].Value = 5 --Writes the integer 5 to the input pin of the Control Script
```

The hash operator # can be used to determine the number of input pins (the length of the Controls.Inputs table).  This technique is useful for making Control Scripts scale to accommodate a varying number of input pins.

**Note:** This only works properly if all the input pins are connected.

```lua
numInputPins = #Controls.Inputs   --Grabs the number of input pins.
```

[Examples](javascript:void(0))

[Example 1: Defining and Assigning an EventHandler Function](javascript:void(0))

The following example defines an EventHandler function and assigns it to five Controls.Inputs, which represent the input pins of the Control Script. The code assigns the same `EventHandler` function to each of 5 inputs.  The function uses the `.Index` property to determine which input caused it to be called.

```lua
Function PrintInputString(calledControl)  
print("This event handler was called by: "..calledControl.Index)  
print("The control's string is:"..calledControl.String)  
end  
   
for i=1,5 do  
Controls.Inputs[i].EventHandler = PrintInputString  --Assign EventHandler to inputs  
end
```

OUTPUT: (if user changes value of input number 3)

```lua
This EventHandler was called by: 3  
The control's string is: 4.5 dB
```

[Example 2: List Each Input Pin and String Property](javascript:void(0))

The `ipairs` iterator is a useful Lua function for iterating through all `Controls.Inputs` or `Controls.Outputs` pins.

The following code will list each input pin and its string property:

```lua
for key,object in ipairs(Controls.Inputs) do  
    
print("Input pin:"..key.." has string:"..object.String)  
  
end
```

[Controls.Outputs](javascript:void(0))

Table representing a [Control Script](../../Schematic_Library/control_script_2.htm)'s output pins, used to write values of controls wired to the control script.  .EventHandler is used to assign event handlers to inputs.

| Properties | | |
| --- | --- | --- |
| Name | Attribute | Comment |
| .Value | Read Write | floating point value of control |
| .Position | Read Write | floating point position which goes from 0.0 -> 1.0 |
| .String | Read Write | string representation of control value |
| .RampTime | Read Write | defaults to 0 seconds |
| .Index | Read Only | index of control |
| .Legend | Read Write | string representing the Legend of a button or a fader. |
|  |  |  |
| --- | --- | --- |
| **Note:** If you reference a `Controls.Outputs [n`] in your script, and there is nothing connected to that output on the [Control Script](../../Schematic_Library/control_script_2.htm) component, the following error displays in the debug log: `[string "<input name>..."]:43: attempt to index global '<index field name>' (a nil value)`. | | |

| Methods | | |
| --- | --- | --- |
| Name | Arguments | Comment |
| :Trigger | none | Triggers the output |

[Remarks](javascript:void(0))

Controls.Outputs is primarily intended for writing values to connected controls, however it's possible to read the current value of an output pin.  For example: `Print(Controls.Outputs[1].String` will print the current value of Controls.Outputs[1], which is read from the connected control pin.

[Examples](javascript:void(0))

[Example 1: Write a value to an output pin](javascript:void(0))

```lua
theTestBox = Controls.Outputs[1]  
a = 5  
b = 6  
theTestBox.Value = a + b  --Output 1 ends up with a value of 11
```

[Example 2: Trigger an output](javascript:void(0))

```lua
Controls.Outputs[3]:Trigger() --Triggers the output of pin 3, similar to a momentary button.
```

[Example 3: Iterates though all output pins and prints the .Value property](javascript:void(0))

```lua
for key, control in ipairs(Controls.Outputs) do  
print("key is:"..key.." Value of control is:"..control.Value)  
end
```

[Control EventHandler](javascript:void(0))

The EventHandler can be assigned to be a simple function that is called each time that particular control value changes. The functions signature looks like:

```lua
void handler ( changedControl )
```

The variable changedControl contains the Control.Inputs object that called the EventHandler. This is useful in the case where multiple Controls.Inputs are assigned the same EventHandler function.

[Notes on .Values](javascript:void(0))

The property .Values is used by a few controls to receive or transmit tables of data through one control pin. `.Values` is currently supported by the 2D Panner, RTA - Band-Pass, Responsalyzer and Meters.

[Examples](javascript:void(0))

[Example 1: Set the position of an input in a matrix mixer configured as a 2D panner.](javascript:void(0))

```lua
sourcePosition = {0.5, 0.75}  --X,Y position desired in 2D panner  
Controls.Outputs[1].Values = sourcePosition --Set .Values property
```

[Example 2: Print the frequencies and RMS Levels from an RTA - Band-Pass (frequencies and RMS Level pins connected)](javascript:void(0))

```lua
freqs = Controls.Inputs[1]  -- Frequencies pin connected to input 1  
rmsLevels = Controls.Inputs[2] â RMS Levels pin connected to input 2
```
