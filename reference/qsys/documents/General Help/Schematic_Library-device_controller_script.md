# Text Controller

> Source: https://help.qsys.com/Content/Schematic_Library/device_controller_script.htm

# Text Controller

Use the Text Controller component to easily declare one or more custom controls and then build the Lua script associated with those controls using a Lua text editor.

[Configuration Overview](javascript:void(0))

1. In your schematic, double-click the Text Controller component to open the elements editor.
2. In the **Controls** section, click  to add a new control.
3. In the **Properties** section, configure the new control. See [Text Controller](#Properti).
4. Click to open the Lua text editor.
5. Write Lua code for your defined controls. Click **Save changes** (yellow bar) to save your script.
6. Run (F5) or emulate (F6) your design to start the script.
7. You can add Panels to a Text Controller, by clicking on the at the top of the Controller window. After a panel is added, you can name the panels by double-clicking on Panel 1-*n*. The same capabilities exist for a panel that exist for the schematic page with the exception of wiring.

**Note:** If there are no Panels configured, then the "Controls" tab is shown.

**Tip:** The âEditâ and âAdd Panelâ buttons are next to the component name for easier access, even with large scripts. The âCloseâ button stays on the right, but you can double-click the header to close it quickly.

To see an example configuration, see [Example](#Example).

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Text Controller Properties

#### User Panel Lock

When the property is set to **no** (Default), a Panel can be deleted by clicking on the X in the Panel tab.

When the property is set to **yes**, A lock icon appears on the Panel tab preventing any changes within or the option to delete the active Panel.

#### Display User Panel

**Note:** If there are no Panels, then the "Controls" tab is shown.

The dropdown will provide Panel 1-*n*, depending on how many you have set up. Whichever Panel you choose in this dropdown will be displayed by default when opening the Text Controller.

#### Start Automatically

When the property is set to **no**, the script will not start when entering emulation or loading a design to a core.

When the property is set to **yes** (Default), the script will start when entering emulation mode or when loading a design to a core.

[Using the Elements Editor](javascript:void(0))

Double-click the Text controller component to open the elements editor, which is where you define controls for your Lua script. After defining controls, click  to open the Lua text editor.

[Controls](javascript:void(0))

#### Controls

* Click  to add a new control to the list, and then configure its properties.
* Click and drag the  icon to re-order the list of controls.
* Select one or more control icons and drag or copy/paste them into your schematic or user control interface. (Use the Ctrl key to select multiple controls.)

#### Serial Port Inputs

Specify how many serial port input pins to expose, from 0 to 128. Use these pins with the [SerialPorts](../Control_Scripting/Using_Lua_in_Q-Sys/SerialPorts.htm) Lua library.

#### Virtual Serial Port Outputs

Specify how many virtual serial port output pins to expose, from 0 to 128. Use these pins with the [SerialServerPorts](../Control_Scripting/Using_Lua_in_Q-Sys/SerialServerPorts.htm) Lua library.

[Controls Properties](javascript:void(0))

#### General Properties

#### Name

Specify a name for the input.

#### Count

Specify the number of controls of the specified type to create.

#### Control Type

#### Category

[Button](javascript:void(0))

Select a **Push Action**:

* Momentary: When the button is clicked, it stays in its opposite state until released.
* Toggle: Allows you to turn the button on or off.
* Trigger: Sends a single command.
* State Trigger: Sends a command when conditions are met. See the [State Trigger](../Control_Scripting/State_Trigger.htm) topic.

[Knob](javascript:void(0))

Specify a **Max Value** and **Min Value** for the specified **Units**:

* dB: -100 to 20
* Hz: 10 to 20000
* Float: (No limit)
* Integer: -999999999 to 99999999
* Pan: -1 to 1

  **Note:** The Pan range is ignored when setting the Pan value. When setting a pan control value in the Block Controller control panel, the valid range is L100 to 0 (or C) to R100. In the Blocks Editor, the valid range is -1 to 1, where -1 is the equivalent of 'L100', 0 is the equivalent of 'C', and 1 is the equivalent of 'R100'. For example, a value of -0.5 is L50, and a value of 0.5 is R50.
* Percent: 0 to 100
* Position: 0 to 1
* Seconds: (No limit)

[Indicator](javascript:void(0))

Specify a **Type**: LED, Meter, Text, Status.

[Text](javascript:void(0))

Specify a **Type**: Text Box, Combo Box, List Box

#### Control Pin

Expose pins for these controls: None, Input (pins on the left), Output (pins on the right), or Both.

[Using the Script Editor](javascript:void(0))

**Tip:** While in the Script area, press F1 for help on the Lua scripting language.

The script editor contains these areas:

* Text editor â Write script for your configuration. You can edit the script in the Design, Emulate, or Run modes, but any errors are only detected in the Run or Emulate modes.
* Script menu â Click  to start or stop the script.
* Information bar at the top of the script â Click the yellow "Save changes" bar to reload (not run) the script. Syntax errors are indicated in a red bar at top-right, as well as in the Debug Output area.
* Search bar â Click the Search bar on the right side of the page to locate or replace text in your script. As a shortcut, press F3 to find the next item.

Platform-level horizontal scrolling is supported here to navigate layouts that extend beyond the visible workspace. You can scroll horizontally using any of the following input methods:

* Touchpad Gestures: Use side-to-side (two finger swipes on supported trackpads.
* Mouse Wheel: Hold the Shift key while scrolling vertically with a mouse wheel.
* Native HID Devices: Use devices with dedicated horizontal scroll support (e.g., horizontal scroll wheels).
* Scroll Bar: Use mouse or arrow keys to drag the bar.

### Rules for Referencing Control Names in Script

* Control names that contain no spaces can be referenced with dotted notation. Examples: 'Button' could be referenced 'Controls.Button.Boolean'; Names with spaces: 'Big Button' = 'Controls["Big Button"].Boolean'
* For a single control (Count = 1), you can directly access the control. Example: 'MyKnob' = `'Controls.MyKnob.Value'`
* If at least two controls are defined in a row (Count = 2+), you must access the controls as an array. Example: 'MyKnobs' x 3 = `'Controls.MyKnobs[1].Value', 'Controls.MyKnobs[2].Value', 'Controls.MyKnob[3].Value'`
* If at least two controls are defined in a row (Count = 2+) and spaces are used in the control name, quotes must be used around the control name. Example: 'My Knobs' x 2 = `'Controls["My Knobs"][1].Value', 'Controls["My Knobs"][2].Value'`

[Debug Output](javascript:void(0))

See [Debug Output](debug_output.htm).

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Code | (text)  Allows you to enter code. | | | Input / Output |
| Script Start | (trigger)  Starts the script running. | | | Input / Output |
| Script Status | (text)  Current status of the script. | | | Output |
| Script Stop | (trigger)  Stops the script. | | | Input / Output |

[Example](javascript:void(0))

In this simple example, Text Controller is configured with a control button that can be used to retrieve a list of control names from any named component in the design.

### Naming components

This example contains two audio components - Gain and Delay. Rename each with a custom name ("MyGain", "MyDelay"). Renaming the components with custom names allows the Named Components function to retrieve a table of control names for those components. For more information about named components in Lua, see [Component](../Control_Scripting/Using_Lua_in_Q-Sys/Component.htm).

### Defining controls

Drag Text Controller onto the canvas and double-click it to open the elements editor. Add three controls with these names and properties:

* Get Controls â A trigger button that retrieves a table of control names for the specified component custom name. (Category = Button; Push Action = Trigger)
* Component Name â A text box for entering the custom name of a component. (Category = Text; Type = Text Box)
* Output â A text box to contain the returned table of control names. (Category = Text; Type = Text Box)

### Adding Lua script

Click  to open the Lua text editor. Add the following script, and then click **Save changes**.

```lua
Controls["Component Name"].EventHandler = function(ctl)  
comp = Component.New(ctl.String)  
end  
  
-- Returns all controls of the component in "Component Name"  
  
Controls["Get Controls"].EventHandler = function()  
local str = " Get Controls for "..Controls["Component Name"].String.."\r"  
for k,v in pairs(comp) do  
str = str..k.."\r"  
end  
Controls.Output.String = str  
end  
  
comp = Component.New(Controls["Component Name"].String)
```

### Running the script

1. Emulate (F6) or run (F5) the design to start the script.
2. Click the schematic page tab ("Page 1" if you didn't rename it).
3. In the Component Name text box, type the name of one of the custom control names - MyGain - and then press Enter.
4. Click **Get Controls**.
5. The Output text box shows the list of controls for that component name. Repeat the process for MyDelay to see how the output changes.

[Reference and Training](javascript:void(0))

* Refer to [Control Scripting](../Control_Scripting/Using_Lua_in_Q-Sys/01_Using_Lua_in_Q-Sys_Overview.htm) and the [Lua 5.3 Reference Manual](../Control_Scripting/Lua_5.3_Reference_Manual/1_-_Introduction.htm) for information about writing scripts.
* [Q-SYS Training - Control 101](https://training.qsc.com/course/view.php?id=58)

  Learn the basic Q-SYS third party control principles, including Lua scripting basics.

[Troubleshooting](javascript:void(0))

### Using Components with Snapshot Controller Ramp Time

Components such as the [Crossover Component](crossover.htm) or other [Text Controller](#) or [Custom Controls](custom_controls.htm) like the Integer Knobs, and Hexadecimal Knobs will not be recalled by Snapshot if the Ramp Time is a non-zero number.

### LED State Retention

In a text controller, if you use a script to set the state of an LED, then disconnect and emulate again, the LED always starts in the âoff' status. This is normal as an LED is an indicator. Indicators such as LED, Status, Text Indicators, and Meters reset their state to the default anytime the script restarts unless they are wired to another control and can get their state from the wired logic.

### UCI Layer Name Retrieval

When using a script to obtain the names of the layers on a UCI from a UCI Layer Controller component, it is recommended to avoid using underscores (â\_â ) in the layer names. This ensures that the name returned matches the actual layer name, preventing any potential discrepancies.

### Text Controller settings not mirrored on Backup Core

Currently, scripts are only executed on the active Core, and not on the standby Core. Additionally, read-only controls are not synchronized between the Cores.
