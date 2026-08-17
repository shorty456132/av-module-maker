# PIN Pad

> Source: https://help.qsys.com/Content/Schematic_Library/pinpad_2.htm

# PIN Pad

The PIN Pad component can be used to create a PIN to access certain pages of a User Control Interface (UCI). Though this can be useful if your UCI contains pages in which only technicians need access, it is not the only purpose. Think of the PIN Pad component as a trigger. Once the PIN is entered correctly, it will trigger another action. Someone who does not know the PIN Pad code will not be able to get past the welcome screen.

[Requirements](javascript:void(0))

You must be in the Run Mode or Emulate Mode to use PIN Pad features.

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Schematic Example](javascript:void(0))

In this example, we have three layers programed on our UCI. Each correct PIN passcode entry will show a different layer of the UCI. If guessed incorrectly, that portion of the UCI remains unseen.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### PIN Pad Properties

#### PIN Count

User-defined number of PINs. You can choose between 0 and 16.

[Controls](javascript:void(0))

#### PIN Pad Entry Box

This box displays the asterisk (\*) symbol as you type the PIN.

#### PIN 1-16

You can set up to 16 different PINs. Each PIN will be displayed on the right side.

#### LED Indicator

When the correct PIN is entered, the LED will illuminate.

#### Set Admin PIN

Type in the passcode you want to use for each PIN available.

#### PIN Pad 1 - 0

Use the numbers on the number pad to type in the correct PIN to unlock the UCI page.

#### â (Backspace)

In the event something was typed incorrectly, the Backspace button will delete the most recent number that was typed. You can press this button as many times as needed to clear the erroneous entry.

#### X (Clear)

The Clear button will wipe out the entire entry.

#### Log Out

This logs out the user and clears the trigger.

[UCI Controller Script Example](javascript:void(0))

```lua
pp = Component.New("PP")  
  
pp.pin_match_0.EventHandler = function(ctl)  
  Uci.SetLayerVisibility("Page 1", "USER1", ctl.Boolean, "fade")  
end  
  
pp.pin_match_1.EventHandler = function(ctl)  
  Uci.SetLayerVisibility("Page 1", "USER2", ctl.Boolean, "fade")  
end  
  
pp.pin_match_2.EventHandler = function(ctl)  
  Uci.SetLayerVisibility("Page 1", "USER3", ctl.Boolean, "fade")  
end  
  
timeout = 1  
count = 1  
  
function set_enabled(en)  
  for k,v in pairs(pp) do  
    v.IsDisabled = not en  
  end  
  if en then   
    Controls.Control_1.IsInvisible = true  
  else   
    Controls.Control_1.IsInvisible = false  
  end  
end  
  
  
pp.pin_mismatched.EventHandler = function()   
  set_enabled(false)  
  Timer.CallAfter( function() set_enabled(true) end, timeout )  
  Controls.Control_1.String = string.format("BAD CHOICE #%i", count)  
  count = count + 1  
  timeout = timeout * 2  
end   
  
pp.pin_matched.EventHandler = function()   
  timeout = 1   
  count = 1  
end   
  
Uci.SetLayerVisibility("Page 1", "USER1", false)   
Uci.SetLayerVisibility("Page 1", "USER2", false)   
Uci.SetLayerVisibility("Page 1", "USER3", false)   
Controls.Control_1.IsInvisible = true
```

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| PIN | | | | |
| 1-n | (text) | | | Input / Output |
| PIN Match | | | | |
| 1-n | 0  1 | false  true | 0  1 | Output |
| PIN Pad | | | | |
| 0 | trigger | | | Input / Output |
| 1 | trigger | | | Input / Output |
| 2 | trigger | | | Input / Output |
| 3 | trigger | | | Input / Output |
| 4 | trigger | | | Input / Output |
| 5 | trigger | | | Input / Output |
| 6 | trigger | | | Input / Output |
| 7 | trigger | | | Input / Output |
| 8 | trigger | | | Input / Output |
| 9 | trigger | | | Input / Output |
| Backspace | trigger | | | Input / Output |
| Clear | trigger | | | Input / Output |
| Enter | trigger | | | Input / Output |
| Logout | trigger | | | Input / Output |
| PIN | N / A | Text field | N / A | Output |
| PIN Matched | trigger | | | Input / Output |
| PIN Mismatched | trigger | | | Input / Output |
