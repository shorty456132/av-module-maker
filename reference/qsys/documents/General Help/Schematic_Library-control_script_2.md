# Control Script

> Source: https://help.qsys.com/Content/Schematic_Library/control_script_2.htm

# Control Script

The Control Script component is used to write scripts, using the Lua language, for control and monitoring from within Q-SYS Designer. You can change or monitor the position, value, string, metadata and other attributes of controls. The script you write interacts with components through their control pins.

For more about scripting in Q-SYS, see [Control Scripting](../Control_Scripting/Using_Lua_in_Q-Sys/01_Using_Lua_in_Q-Sys_Overview.htm). Refer to the [Lua 5.3 Reference Manual](../Control_Scripting/Lua_5.3_Reference_Manual/1_-_Introduction.htm)for information about native Lua commands supported in Q-SYS.

[Using the Control Script](javascript:void(0))

The Control Script component is defined, in the component Properties, by the number of inputs and outputs. The body of the script is written in the Control Script Control Panel.

* Refer to the [Q-SYS Lua Environment](../Control_Scripting/Using_Lua_in_Q-Sys/01_Using_Lua_in_Q-Sys_Overview.htm) and the [Lua 5.3 Reference Manual](../Control_Scripting/Lua_5.3_Reference_Manual/1_-_Introduction.htm) topics for information about writing scripts.
* Click the Search bar on the right side of the page to locate text in your script. As a shortcut, press F3 to find the next item.

[About script compatibility](javascript:void(0))

If you open a Q-SYS 3.3 or earlier design containing a Control Script component in Q-SYS 4.0 or later, the component with become a Control Script v1 component. The existing v1 script will continue to function as before. However, if the v1 script is pasted into a newly placed Control Script component, it will most likely fail. We have made it simpler to convert a v1 script to v2 by adding a property to the Control Script v1 block by adding a property to use the New Script Engine (Yes/No). This is to avoid having to copy and paste code to a v2 Script component.

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](# "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Debug Output](javascript:void(0))

See [Debug Output](debug_output.htm).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Control Script Properties

#### Input Count

Sets the number of inputs.

#### Serial Input Count

Sets the number of serial connections. Use with the Core, I/O Frame, and Page Station Serial Port components.

#### Output Count

Sets the number of outputs.

#### Virtual Serial Output Count

Sets the number of virtual serial output pins. Use these pins with the [SerialServerPorts](../Control_Scripting/Using_Lua_in_Q-Sys/SerialServerPorts.htm) Lua library.

#### Start Automatically

When the property is set to **no**, the script will not start when entering emulation or loading a design to a core.

When the property is set to **yes** (Default), the script will start when entering emulation mode or when loading a design to a core.

[Controls](javascript:void(0))

When you double click the Control Script component, the script editing tab displays.

#### Script Area

Text-edit area to write script. You can edit the script in the Design, Emulate, or Run modes, but any errors are only detected in the Run or Emulate modes.

**Tip:** While in the Script area, press F1 for help on the Lua scripting language.

#### Top Bar

Click the yellow "Save changes" bar to reload (not run) the script. Syntax errors are indicated in a red bar at top-right, as well as in the Debug Output area.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Code | (text)  Allows you to enter code. | | | Input / Output |
| Script Start | (trigger)  Starts the script running. | | | Input / Output |
| Script Status | (text)  Current status of the script. | | | Output |
| Script Stop | (trigger)  Stops the script. | | | Input / Output |
