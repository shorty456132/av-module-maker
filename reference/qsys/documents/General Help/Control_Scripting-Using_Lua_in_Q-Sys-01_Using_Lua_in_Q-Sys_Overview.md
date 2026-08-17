# Control Scripting

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/01_Using_Lua_in_Q-Sys_Overview.htm

# Control Scripting

You can write a control script for the purpose of automatically accomplishing tasks or creating other control mechanisms by associating a control script with standard controls in the Schematic Elements of a Q-SYS design.

Control scripting in Q-SYS Designer uses the [Lua.org](http://www.lua.org/ "Click to visit Lua.org") programming language with extensions that allow it to control Q-SYS hardware and software.

* See [Q-SYS Extensions to Lua](Q-SYS_Extensions_to_Lua.htm) for a list of documented Q-SYS-specific extensions.
* Refer to the [Lua 5.3 Reference Manual](../Lua_5.3_Reference_Manual/1_-_Introduction.htm)for information about native Lua commands supported in Q-SYS.
* Refer to the [UCI Controller](../../Schematic_Library/device_controller_proxy.htm)  topic to learn about using the User Control Interfaces > UCI Script tab to script controls that you have added to your UCI from the Toolbox tab. These scripts are specific to each UCI in your design and do not support all Lua methods.

[Scripting Components](javascript:void(0))

Scripting Components allow you to write scripts to perform operations on values, positions, strings, colors and other metadata, and timing of controls in the Schematic Elements. Q-SYS Designer includes multiple scripting components, each with a different approach to authoring a script.

* [Control Script](../../Schematic_Library/control_script_2.htm) is used to write scripts, using the Lua language, for control and monitoring from within Q-SYS Designer. You can change or monitor the position, value, string, metadata and other attributes of controls. The script you write interacts with components through their control pins.
* [Block Controller](../../Schematic_Library/device_controller.htm) allows you to easily declare a number of controls and their connections in an elements configurator, and then build the Lua script associated with those controls using a visual block interface.
* [Text Controller](../../Schematic_Library/device_controller_script.htm) is similar to Block Controller, in that you declare controls in an elements configurator, but then write your configuration exclusively in the Lua script editor.

[UCI Scripting](javascript:void(0))

Refer to the [UCI Controller](../../Schematic_Library/device_controller_proxy.htm)  topic to learn about using the User Control Interfaces > UCI Script tab to script controls that you have added to your UCI from the Toolbox tab. These scripts are specific to each UCI in your design and do not support all Lua methods.

[Control Scripting Basics](javascript:void(0))

* Q-SYS specific functions are capitalized, while native Lua functions are lower case (e.g. Q-SYS' `Timer.Start` vs Lua's `math.abs`).
* Control scripts use an Event/EventHandler model. EventHandlers (functions) are attached to an Event. When that Event takes place, the EventHandler is invoked.
* EventHandlers can be attached to Control Input objects that are invoked when the value of the Control changes.
* For Control Script component, both the input and output objects are in arrays called `Controls.Inputs` and `Controls.Outputs`. Access to these objects is accomplished with the [] operator. For example, `Controls.Inputs[1].Value` gives you access to the value of the Control assigned to input 1.

  **Note:** Lua Arrays are 1 based.
* For the Text Controller component, Controls are in an array called `Controls`. Access to these controls is accomplished by referencing the Control name. For example, `Controls.MyButton.Value` gives you access to the value of the Control named MyButton. Controls with a Count greater than 1 are available as an array and are can be accessed as `Controls.MultipleButtons[1].Value`.
* Code changes can be made in a control script without redeploying a design.  A yellow notification bar appears at the top of the Control Panel window alerting the user that code is out of sync with the running design.  Clicking the yellow bar allows the script to be updated without having to redeploy the design or interrupting audio.
* Statements entered in the main body of a script (outside of functions) are executed when a design is deployed and when control scripts are updated in a running design.

[Lua Training, Education, and Examples](javascript:void(0))

* [Q-SYS Training - Control 101](https://training.qsc.com/course/view.php?id=58)

  Learn the basic Q-SYS third party control principles, including Lua scripting basics.
* The book "[Programming in Lua](http://www.lua.org/pil/)" is highly recommended for learning Lua.
* For examples of solutions using scripting refer to the [Scripting Solutions](../Scripting_Solutions.htm) topic.
* For Lua code examples, see [Code Examples](Lua_Code_Examples.htm).

[Troubleshooting](javascript:void(0))

### Maximum Execution Error

The Maximum Execution Error is thrown when an individual call of a Lua function exceeds the maximum allowed number of CPU cycles. Infinite loops are the most common cause of this error. "Max execution limits exceeded" is displayed in the debug log when this error occurs.
