# Code Examples

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/Lua_Code_Examples.htm

# Code Examples

This document offers a range of Lua code examples tailored for the Q-SYS platform. These examples are designed to help you automate tasks and create control mechanisms within your Q-SYS designs using Lua scripting.

[Passing an Input to the Output](javascript:void(0))

The following is a simple script in which the input of the control that changed (changedControl) is passed to the output (Controls.Outputs[1]).

```lua
function UpdateControl ()  
  Controls.OutputKnob.Value = Controls.InputKnob.Value  
end   
  
Controls.InputKnob.EventHandler = UpdateControl
```

[Define a Function During Assignment](javascript:void(0))

Lua supports anonymous functions so you can define the function during assignment as follows:

```lua
Controls.InputKnob.EventHandler = function(ctl)  
  --Note: The EventHandler function passes the control in as a argument automatically.  
  --In this example we named it ctl, but this variable can be any name.   
  Controls.OutputKnob.Value = ctl.Value  
end
```

[Address an Input Directly](javascript:void(0))

The signature of the Control value EventHandler takes the control that changed as an argument. Due to Lua's 'loose' typing, it is possible to remove that argument and just address the input directly.

```lua
Controls.InputKnob.EventHandler = function()  
  Controls.OutputKnob.Value = Controls.InputKnob.Value  
end
```

[Determine System Mode - Emulate or Not](javascript:void(0))

```lua
if System.IsEmulating then  
Controls.Outputs[1].Color = "Green"  
else  
Controls.Outputs[1].Color = "Red"  
end
```

[Performing Math](javascript:void(0))

```lua
Controls.InputKnob.EventHandler = function()  
  Controls.OutputKnob.Value = Controls.InputKnob.Value / 2  
end
```

[Vector Value Controls](javascript:void(0))

**Note:** This operation is only possible in a Control Script.

```lua
--To access the vector output of a meter.   
   
t = Controls.Inputs[1].Values  
print( t[1]..","..t[2]..","..t[3]..","..t[4] )
```

[Multiple Inputs](javascript:void(0))

If you have multiple inputs and want to run the same script if any of the inputs change, the easiest way to accomplish this would be to iterate all the inputs.

```lua
function ButtonPressed ()  
  print("One of the Buttons Was Pressed")  
end   
  
for idx,ctl in ipairs(Controls.MultipleButtons) do  
  ctl.EventHandler = ButtonPressed  
end
```

[Ramp or Position Controls](javascript:void(0))

You can also ramp control values or positions via script. RampTime is specified in seconds.

**Note:** Once a RampTime has been assigned to a Control, it will keep this RampTime until it is changed or the script is restarted.

```lua
Controls.InputKnob.EventHandler = function()  
  Controls.OutputKnob.RampTime = 3  
  Controls.OutputKnob.Value = Controls.InputKnob.Value  
end
```

[Metadata](javascript:void(0)) 

When controls have metadata attached to them, you can do the following:

* set a control to visible or invisible,
* set a control to enabled or disabled,
* specify its choices, and
* set its color.

Metadata is used on some built-in controls - for example, the [High-Pass Filter](../../Schematic_Library/filter_highpass.htm "Click to view the High-Pass Filter topic.") uses metadata to disable the Q control when the filter type is not set to Variable Q. The controls in the Custom Controls component have metadata turned on by default. Attempting to access metadata on a control which does not have metadata will result in an error.

Color metadata is in the form of a string. Q-SYS uses the built in .NET string->color converter which allows for strings in the form "#RGB", "#RRGGBB", [CSS Color Names](http://www.w3schools.com/colors/colors_names.asp "Click to visit the w3schools.com CSS Color Names reference."), and HSV values using the format "!HHSSVV".

[NamedControl](javascript:void(0))

**Note:** See the [NamedControl](NamedControl.htm) section for syntax.

```lua
NamedControl.SetValue("CustomControlsInteger1", 7, 15)  -- Set value of a named integer control to 7, ramp 15 seconds  
NamedControl.GetString("CustomControlsTextdisplay1")  --Get string value of a control  
NamedControl.Trigger("CustomControlsTrigger1")  --Triggers a controlled trigger button
```

[Timer](javascript:void(0)) 

Each Control Script has a timer available. It has a Tick event that a TickHandler can be attached to. You can start or stop the timer. The Timer TickHandler signature looks like:

**Note:** See the [Timer](Timer.htm) section for syntax

```lua
--Simple Timer  
Controls.InputKnob.EventHandler = function()  
  Timer.CallAfter(  
    function()  
      Controls.OutputKnob.Value = Controls.InputKnob.Value  
      end, 3 --Time in Seconds to Wait  
  )  
end  
  
--Named Timer  
myTimer = Timer.New()   --Define timer  
  
myTimer.EventHandler = function()   --Event to run when timer expires  
  Controls.OutputKnob.Value = Controls.OutputKnob.Value + 1  
end  
  
Controls.UpButton.EventHandler = function(ctl)  
  if ctl.Boolean then  --if button is on / pressed  
    myTimer:Start(.5) --Argument is number of seconds to run the timer  
  else -- if button is off / released  
    myTimer:Stop()  --Note: Timer will keep repeating until stopped  
  end  
end
```

[Encode Icons to Buttons](javascript:void(0))

The following is a sample script to encode icons to a button. The codes for each icon can be found in C:\Program Files\QSC\Q-SYS Designer\lua\icons.lua.

**Note:** Although this example shows a supported method to encode icons to buttons, the better approach is to use CSS. See [Referencing Images and Fonts](../../Schematic_Library/uci_styles.htm#Referenc4) for information and examples.

```lua
json = require("rapidjson")  
btn.EventHandler = function()  
  if btn.Boolean then  
    btn.Legend = json.encode{IconString = string.char(0xef,0x88,0x90)}  
  else  
    btn.Legend = json.encode{IconString = string.char(0xef,0x88,0x91)}  
  end  
end
```
