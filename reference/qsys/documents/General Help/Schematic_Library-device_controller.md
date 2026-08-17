# Block Controller

> Source: https://help.qsys.com/Content/Schematic_Library/device_controller.htm

# Block Controller

Use the Block Controller component to easily declare one or more controls and their connections, and then build the Lua script associated with those controls using a visual block interface.

After you configure your controls and connections in the elements configurator, you can then build your configuration using a visual programming tool that uses interlocking graphical blocks to represent common code programming concepts including logical expressions and loops. Rapid code creation and editing allows you to compose simple or sophisticated AV scripts while ensuring that the generated code is always syntactically correct.

The underlying script interacts with components through their control pins. You can write scripts to control elements entirely within the Q-SYS Designer file, or you can use it to interface Q-SYS with third-party hardware accessible via TCP, UDP, Serial, or SSH.

[Configuration Overview](javascript:void(0))

1. In your schematic, double-click the **Block Controller** component to open the elements editor.
2. In the **Controls** section, click  to add a new control.
3. In the **Properties** section, configure the new control, including its name, count, and type.
4. In the **Connections** section, click  to add a new connection.
5. In the **Properties** section, configure the new connection, including its name, type, and control pins.
6. Click  to edit and save the Lua script for your control configuration using a visual block interface.
7. You can add Panels to a Block Controller, by clicking on the at the top of the Controller window. After a panel is added, you can name the panels by double-clicking on Panel 1-*n*. The same capabilities exist for a panel that exist for the schematic page with the exception of wiring.

**Note:** If there are no Panels, then the "Controls" tab is shown.

**Tip:** The âEditâ and âAdd Panelâ buttons are next to the component name for easier access, even with large scripts. The âCloseâ button stays on the right, but you can double-click the header to close it quickly.

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Block Controller Properties

#### User Panel Lock

When the property is set to **no** (Default), a Panel can be deleted by clicking on the X in the Panel tab.

When the property is set to **yes**, A lock icon appears on the Panel tab preventing any changes within or the option to delete the active Panel.

#### Display User Panel

**Note:** If there are no Panels, then the "Controls" tab is shown.

The dropdown will provide Panel 1-*n*, depending on how many you have set up. Whichever Panel you choose in this dropdown will be displayed by default when opening the Block Controller.

#### Start Automatically

When the property is set to **no**, the script will not start when entering emulation or loading a design to a core.

When the property is set to **yes** (Default), the script will start when entering emulation mode or when loading a design to a core.

[Using the Elements Editor](javascript:void(0))

Double-click the Block Controller component to open the elements editor, which is where you define controls for your block configuration. After defining your controls, click  to open the Blocks editor.

[Controls and Connections](javascript:void(0))

#### Controls

Click  to add a new control to the list, and then configure its properties. See [Controls Properties](#Controls_Properties).

#### Connections

Click  to add a new connection to the list, and then configure its properties. See [Connections Properties](#Connections_Properties).

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

[Connections Properties](javascript:void(0))

#### Name

Specify a name for the connection and its controls.

#### Type

Specify how to communicate with the external device:

[TCP](javascript:void(0))

Expose **IP Address**, **Port**, and **Status** pins for these controls: None, Input (pins on the left), Output (pins on the right), or Both.

* For an example of creating a TCP connection in the visual block interface, see [Creating a TCP Socket](#Creating2).
* The TCP connection automatically connects to a specified IP address and port and will retry if the connection is lost.

[UDP](javascript:void(0))

Expose **IP Address**, **Port**, and **Status** pins for these controls: None, Input (pins on the left), Output (pins on the right), or Both.

[Serial](javascript:void(0))

Expose **Baud Rate**, **Bits**, **Parity**, and **Status** pins for these controls: None, Input (pins on the left), Output (pins on the right), or Both. Note that this will expose a serial control pin that needs to be wired to a matching pin on the component that represents the hardware.

For an example of creating a serial connection, see [Creating a Serial Connection](#Creating3).

[SSH](javascript:void(0))

Expose **IP Address**, **Port**, **Status**, **User Name**, and **Password** pins for these controls: None, Input (pins on the left), Output (pins on the right), or Both.

* For an example of creating an SSH connection in the visual block interface, see [Creating an SSH Connection](#Creating6).
* The SSH connection automatically attempts to connect with the provided login host, port, and credentials.

[Using the Blocks Editor](javascript:void(0))

After configuring your controls and connections, click  to open the Blocks editor (**Blocks** tab). Controls and connections are presented as graphical blocks that you can drag into the script and configure with values and statements.

* In the **Controls** and **Connections** drop-downs, add and configure script components (blocks), as desired.
* If your design contains **Named Controls** or **Named Components**, use their drop-down menus to add blocks from those categories.
* Add and configure new blocks (Values, Strings, etc.) from the menu, as desired.
* Click **Save changes** to commit any changes to your script.
* Click the **Lua** tab to view your configuration in script form.

For examples of creating controls using the visual block interface, see [Block Examples](#Block). To modify your script in a traditional script editor, see [Using the Script Editor](#Using_the_Script_Editor).

Platform-level horizontal scrolling is supported here to navigate layouts that extend beyond the visible workspace. You can scroll horizontally using any of the following input methods:

* Touchpad Gestures: Use side-to-side (two finger swipes on supported trackpads.
* Mouse Wheel: Hold the Shift key while scrolling vertically with a mouse wheel.
* Native HID Devices: Use devices with dedicated horizontal scroll support (e.g., horizontal scroll wheels).
* Scroll Bar: Use mouse or arrow keys to drag the bar.

### Navigation Menu

#### Arrange

This function organizes and aligns the blocks in a neat and orderly manner, making the design more visually appealing and easier to navigate.

#### Clear All Blocks

This option removes all blocks from the design canvas, allowing you to start fresh with a clean slate.

#### Convert to Script

This feature transforms the block-based design into a script, enabling more advanced and customizable control through coding. See [Using the Script Editor](#Using_the_Script_Editor).

#### Start Script

This command initiates the execution of the script, allowing the programmed actions and controls to begin operating. This option is initially grayed out until you are in Emulation or Run Mode.

#### Stop Script

This function halts the execution of the script, stopping all programmed actions and controls. This option is initially grayed out until you are in Emulation or Run Mode.

#### Restart Script

This option stops the current script and then immediately starts it again, useful for applying changes or troubleshooting. This option is initially grayed out until you are in Emulation or Run Mode.

### Right-Click Menu

#### Undo

This function allows you to revert the last action you performed, effectively undoing any recent changes.

#### Redo

This option lets you reapply an action that was previously undone, restoring the change you had reverted.

#### Clean Up Blocks

This feature organizes and aligns the blocks on the design canvas, making the layout more orderly and visually appealing.

#### Collapse Blocks

This function minimizes the blocks, reducing their size to show only essential information and making the design more compact.

#### Expand Blocks

This option enlarges the blocks to display all their details, providing a more comprehensive view of the design.

#### Delete *n* Blocks

This command allows you to remove all blocks from the design canvas, helping you manage and streamline your layout.

[Using the Script Editor](javascript:void(0))

To edit the script using a text-based editor, click the  button and select **Convert to Script**. The Block Controller component window will update and reflect the properties as seen in Text Controller [Controls](device_controller_script.htm#Controls).

**WARNING:** When you switch to the text-based editor, the editor is initially populated with the Lua script generated from the Block editor. If you later switch back to the Block editor ( > **Revert to Blocks**), your text editor changes are lost. Any text-based script you enter is overwritten by text generated by the Block editor.

The script editor contains three areas:

* Text editor â Modify the script for your configuration. You can edit the script in the Design, Emulate, or Run modes, but any errors are only detected in the Run or Emulate modes.

**Tip:** While in the Script area, press F1 for help on the Lua scripting language.

* Information bar at the top of the script:
  + Click the yellow "Save changes" bar to reload (not run) the script.
  + Syntax errors are indicated in a red bar at top-right, as well as in the Debug Output area.

Platform-level horizontal scrolling is supported here to navigate layouts that extend beyond the visible workspace. You can scroll horizontally using any of the following input methods:

* Touchpad Gestures: Use side-to-side (two finger swipes on supported trackpads.
* Mouse Wheel: Hold the Shift key while scrolling vertically with a mouse wheel.
* Native HID Devices: Use devices with dedicated horizontal scroll support (e.g., horizontal scroll wheels).
* Scroll Bar: Use mouse or arrow keys to drag the bar.

[Notes](javascript:void(0))

* Refer to the [Q-SYS Lua Environment](../Control_Scripting/Using_Lua_in_Q-Sys/01_Using_Lua_in_Q-Sys_Overview.htm) and the [Lua 5.3 Reference Manual](../Control_Scripting/Lua_5.3_Reference_Manual/1_-_Introduction.htm) topics for information about writing scripts.
* Click the Search bar on the right side of the page to locate or replace text in your script. As a shortcut, press F3 to find the next item.

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

[Block Examples](javascript:void(0))

This section demonstrates how you can create controls using the visual block interface, which then generates the underlying Lua script. Refer to the [Control Scripting](../Control_Scripting/Using_Lua_in_Q-Sys/01_Using_Lua_in_Q-Sys_Overview.htm) topic for information on Lua scripting.

[Creating a Serial Connection](javascript:void(0))

Serial port communication is supported via the RS-232 ports on some Q-SYS devices. To create a connection:

1. In your schematic, double-click the Block Controller component to define the controls and connections using the elements editor.
2. Click  to define the controller configuration in the Blocks editor.
3. Drag the Q-SYS device's Serial Port component into your schematic and wire it to the Block Controller component.

In this example, a trigger button is used to send data (entered in a text box) through the serial port on a Core 110f. For more information on serial port connections, and to see an example of the Lua script used to create this example, see [SerialPorts](../Control_Scripting/Using_Lua_in_Q-Sys/SerialPorts.htm).

### Defining controls and connections

Double-click the Block Controller component to open the elements editor. In this example, two controls and one connection are defined.

**Tip:** You can drag individual control and connection components into your schematic or copy them to the User Control Interface editor.

#### Controls

* Trigger button (Control Type = Button; Button Type = Trigger)
* Text box for sending data (Control Type = Text; Text Type = Text Box)

#### Connections

* Serial port (Connection Type = Serial)

### Blocks and script equivalents

Click  to open the Blocks editor. Define the controller configuration using the available blocks in the left menu. The **Controls** and **Connections** categories contain the elements defined in the elements editor.

In this example, there are four groups of blocks that do the following:

* Establish the event handler for the trigger button.
* Print out baud rate, data bits, and parity once a connection has been established.
* Print disconnect messaging.
* Print any message received from the device. In the example provided, âAnyâ does not mean any character. The end of line is any sequence of any number of carriage return and/or linefeed characters. This is the appropriate choice if the protocol uses simply a carriage return as the end of message.

| Blocks | Script Equivalent |
| --- | --- |
|  | ```lua Controls['send'].EventHandler = function()   local tx = Controls['data'].String   tx = tostring(Controls['data'].String) .. tostring('\r')   sp:Write(tx)   print(tostring('sending data out to serial port ') .. tostring(Controls['data'].String)) end ``` |
|  | ```lua spStatusConnectedFunctions['W20|n-~B=8xbb@M)EUz]'] = function()   print('serial port connected')   print(tostring('baudrate ') .. tostring(Controls['sp.Baud_Rate'].String))   print(tostring('databits  ') .. tostring(Controls['sp.Data_Bits'].String))   print(tostring('parity  ') .. tostring(Controls['sp.Parity'].String)) end ``` |
|  | ```lua spStatusClosedFunctions['ik3z-W^jqC}cB9g*Vt!9'] = function(error_message)   print('serial port disconnected') end ``` |
|  | ```lua sp.Data = function()   message = sp:ReadLine(SerialPorts.EOL.Any)   while (message ~= nil) do     print(tostring('read line ') .. tostring(message))     message = sp:ReadLine(SerialPorts.EOL.Any)   end end ``` |

### Setting baud rate, data bits, and parity

The Block Controller automatically produces script for handling the setting of baud rate, data bits, and parity. When you emulate or save and run your design to the Core, open the Block Controller control panel to set baud rate, data bits, and parity using the drop-down menus.

[Creating a TCP Socket](javascript:void(0))

The TcpSocket object allows Q-SYS cores to make client TCP/IP connections to devices on the network. In this example, a trigger button is used to send data entered in a text box to a TCP device with a specified IP address and port number. For more information, and to see an example of the Lua script used to create this example, see [TcpSocket](../Control_Scripting/Using_Lua_in_Q-Sys/TcpSocket.htm).

### Defining controls and connections

Double-click the Block Controller component to open the elements editor. In this example, two controls and one connection are defined.

**Tip:** You can drag individual control and connection components into your schematic or copy them to the User Control Interface editor.

#### Controls

* Trigger button (Control Type = Button; Button Type = Trigger)
* Text box for sending data (Control Type = Text; Text Type = Text Box)

#### Connections

* TCP socket (Connection Type = TCP)

### Blocks and script equivalents

Click  to open the Blocks editor. Define the controller configuration using the available blocks in the left menu. The **Controls** and **Connections** categories contain the elements defined in the elements editor.

| Blocks | Script Equivalent |
| --- | --- |
|  | ```lua sendData = 'Hello\x0d\x0a' ``` |
|  | ```lua sockStatusConnectedFunctions['rq{I?iu_o,WJQo?H:W2X'] = function()   print('socket connected') end ``` |
|  | ```lua sockStatusClosedFunctions['jArNCFTp,o|3t(#/z?sc'] = function(error_message)   print('TCP socket was closed by the remote end') end ``` |
|  | ```lua sock.Data = function()   message = sock:ReadLine(TcpSocket.EOL.Any)   while (message ~= nil) do     print(tostring('TCP socket has data:\t') .. tostring(message))     message = sock:ReadLine(TcpSocket.EOL.Any)   end end ``` |
|  | ```lua Controls['Trigger button'].EventHandler = function()   -- A comment for this block   sock:Write(sendData)   print('sending data') end ``` |

[Creating an SSH Connection](javascript:void(0))

Use SSH to create secure client connections to devices on the network. It is very similar to creating a TCP socket, but requires additional connection arguments (host, port, user, password). For information about creating SSH connections in Lua, see [Ssh](../Control_Scripting/Using_Lua_in_Q-Sys/Ssh.htm).

In this example, an SSH connection is configured that:

1. Automatically attempts to connect with the provided login host, port, and credentials.
2. Writes the date to the connection.
3. Prints any messages received from the device.
4. Prints a login failure message if the wrong credentials are provided.

### Defining controls and connections

Double-click the Block Controller component to open the elements editor. In this example, a new SSH connection is defined. Controls are available for IP Address, Port, UserName, Password, and Status, which can be dragged into your design.

### Blocks and script equivalents

Click  to open the Blocks editor. Define the controller configuration using the available blocks in the left menu. The **Connections** category contains the elements for the SSH connection.

| Blocks | Script Equivalent |
| --- | --- |
|  | ```lua timer0 = Timer.New() ``` |
|  | ```lua SSH_Connection.Connected = function()   timer0:Start(10) end ``` |
|  | ```lua timer0.EventHandler = function()   SSH_Connection:Write('date\n') end ``` |
|  | ```lua SSH_Connection.Data = function()   message = SSH_Connection:ReadLine(TcpSocket.EOL.Any)   while (message ~= nil) do     print(message)     message = SSH_Connection:ReadLine(TcpSocket.EOL.Any)   end end ``` |
|  | ```lua SSH_Connection.LoginFailed = function()   print("Wrong password!") end ``` |

### Setting connection parameters

Run or emulate your design. In the SSH connection controls, set the host/IP address, port, username, and password. Block Controller automatically attempts to connect with the provided parameters.

[Creating a Timer](javascript:void(0))

The Timer object is used to create delays or trigger events after a defined elapsed time. It should be used instead of Lua's native delay and time functions. For more information, and to see an example of the Lua script used to create this example, see [System](../Control_Scripting/Using_Lua_in_Q-Sys/System.htm#Timer).

### Blocks and script equivalents

| Blocks | Script Equivalent |
| --- | --- |
|  | ```lua timer1 = Timer.New() timer2 = Timer.New() timer_1 = 'timer1!' timer_2 = 'timer2' timer = 'timer2' ``` |
|  | ```lua function timerFunc()   if timer == timer_1 then     print(timer_1)    elseif timer == timer_2 then     print(timer_2)   end end ``` |
|  | ```lua timer1.EventHandler = function()   timer = timer_1   timerFunc() end ``` |
|  | ```lua timer2.EventHandler = function()   timer = timer_2   timerFunc() end ``` |
|  | ```lua timer1:Start(1) timer2:Start(2) ``` |

[Creating a Timeline](javascript:void(0))

Use the **after time** block to create a single event or a series of events that execute after a specified period of seconds. Unlike a standard timer, this block only fires once.

To add more events to execute, click the gear icon and drag the **then after time** block under the **after time** block.

[Show Me](javascript:void(0))

[
Your browser does not support the video tag.
](../Resources/Videos/BlockController_Timeline.webm)

### Blocks and script equivalents

In this example, a series of debug print strings executes in three timed steps.

| Blocks | Script Equivalent |
| --- | --- |
|  | ```lua Timer.CallAfter(function()     print('This')     Timer.CallAfter(function()       print('is')       Timer.CallAfter(function()         print('Q-SYS')   print(Qlib.version().Version)       end,5)   end,3) end,2) ``` |

### Debug Output

```lua
This
is
Q-SYS
7.1.0.27
```

[Creating UCI Controls: Setting Layer Visibility](javascript:void(0))

This example shows how you can use the Block Controller component to create multiple controls (trigger buttons) and then use those controls in a user control interface with layer transitions.

### Overview

This example UCI allows the user to push one of six buttons to either show a Q-SYS product category image or remove the current image and show the Q-SYS logo:

[
Your browser does not support the video tag.
](../Resources/Videos/BlockController_UCI_Layers.webm)

There are three overall steps to creating this UCI:

1. Defining the control buttons in the Block Controller elements editor.
2. Copying those controls from the Block Controller elements editor into the UCI editor and defining layers and button images.
3. Defining the controller configuration in the Blocks editor to configure the UCI functionality, including transitions between controls.

### Defining controls

Double-click the Block Controller component to open the elements editor. In this example, six controls are defined - each for displaying a different Q-SYS product image (Control Type = Button; Button Type = Trigger).

### Configuring the UCI

**Note:** For information on creating UCIs, see [User Control Interface (UCI) Design Overview](user_control_interface.htm).

1. Create a new user control interface and name it "Q-SYS".
2. Select and copy each of the six controls (gray rectangles) from the Block Controller elements editor and paste into the UCI editor.
3. Configure the properties for each control button in the UCI:
   * Set **Graphics Properties** > **Button Style** to "Image".
   * Set **Button Images** > **On Image** to an appropriate button graphic.
4. Your UCI will now contain a single layer with six elements (buttons). Rename this layer "buttons".
5. Create six new layers â named "cores", "network", "conference", "touchscreen", "amplifiers", and "logo" â each with a large graphic that will be placed in the middle of the display above the buttons layer.

Now, you will have a UCI with one page ("Page 1") containing seven layers:

### Using the Blocks editor to define the controller configuration

Finally, use the Blocks editor to define the UCI functionality.

1. In the Block Controller elements editor, click the button to open the Blocks editor.
2. In the Blocks menu, you will see categories for various types of statements, including a Controls category that contains available blocks for each of the control buttons you defined in the elements editor.
3. Build the configuration by selecting individual blocks from the menu. This example uses blocks from the **Variables and Functions**, **System**, and **Controls** categories. See the next section for the configuration for this example.

### Blocks and script equivalents

In this example, there are three groups of blocks that do the following:

* Define the "clear" function, which clears the display of all product images with a Fade transition, revealing only the Q-SYS logo.
* Run the "clear" function when starting the UCI.
* Define what occurs when each button is pressed.

**Note:** For information about the UCI Lua functions used behind the scenes in this example, see [UCI](../Control_Scripting/Using_Lua_in_Q-Sys/Uci.htm).

| Blocks | Script Equivalent |
| --- | --- |
|  | ```lua function clear()   Uci.SetLayerVisibility('Q-SYS', 'Page 1', 'cores', false, 'fade')   Uci.SetLayerVisibility('Q-SYS', 'Page 1', 'network', false, 'fade')   Uci.SetLayerVisibility('Q-SYS', 'Page 1', 'conference', false, 'fade')   Uci.SetLayerVisibility('Q-SYS', 'Page 1', 'touchscreen', false, 'fade')   Uci.SetLayerVisibility('Q-SYS', 'Page 1', 'amplifiers', false, 'fade') end ``` |
|  | ```lua clear() ``` |
|  | ```lua Controls['cores'].EventHandler = function()   clear()   Uci.SetLayerVisibility('Q-SYS', 'Page 1', 'logo', false, 'fade')   Uci.SetLayerVisibility('Q-SYS', 'Page 1', 'cores', true, 'left') end   Controls['network'].EventHandler = function()   clear()   Uci.SetLayerVisibility('Q-SYS', 'Page 1', 'logo', false, 'fade')   Uci.SetLayerVisibility('Q-SYS', 'Page 1', 'network', true, 'right') end   Controls['conference'].EventHandler = function()   clear()   Uci.SetLayerVisibility('Q-SYS', 'Page 1', 'logo', false, 'fade')   Uci.SetLayerVisibility('Q-SYS', 'Page 1', 'conference', true, 'bottom') end   Controls['touchscreens'].EventHandler = function()   clear()   Uci.SetLayerVisibility('Q-SYS', 'Page 1', 'logo', false, 'fade')   Uci.SetLayerVisibility('Q-SYS', 'Page 1', 'touchscreen', true, 'top') end   Controls['amplifiers'].EventHandler = function()   clear()   Uci.SetLayerVisibility('Q-SYS', 'Page 1', 'logo', false, 'fade')   Uci.SetLayerVisibility('Q-SYS', 'Page 1', 'amplifiers', true, '') end   Controls['logo'].EventHandler = function()   clear()   Uci.SetLayerVisibility('Q-SYS', 'Page 1', 'logo', true, 'fade') end ``` |

[Creating UCI controls: Setting Shared Layer Visibility](javascript:void(0))

In this example, a UCI contains two pages with distinct graphics. Two shared layers â one for a Toggle Time control and another for a time display â are used on each page. When the Toggle Time button is pushed, the time display is therefore shown or hidden on both pages.

[
Your browser does not support the video tag.
](../Resources/Videos/BlockController_UCI_SharedLayers.webm)

**Note:** For information about adding a date/time text box to your UCI, see [Date/Time](date_time.htm).

### Defining controls

In this example, one control is defined (Category = Button; Push Action = Toggle). The button is configured in the visual Blocks editor to turn on/off the shared layer containing the time display.

### Configuring the UCI

This simple UCI (named "MyUCI") contains two pages, each with a different QSC graphic. Two shared layers - one for the Toggle Time control ("ToggleTime") and the other for the time display ("Time") - are also included on each page. For information about creating shared layers, see [User Control Interface (UCI) Design Overview](user_control_interface.htm#Add_Layers).

### Define the controller configuration

Use the Blocks editor (accessible via the  button) to define what happens when the Toggle Time button is pushed: Show or hide the Time shared layer across any page that includes that shared layer, and with a specified transition type. This example uses blocks from the **Flow Control**, **Operators**, **System**, and **Controls categories**.

**Note:** For information about the UCI Lua functions used behind the scenes in this example, see [UCI](../Control_Scripting/Using_Lua_in_Q-Sys/Uci.htm).

| Blocks | Script Equivalent |
| --- | --- |
|  | ```lua Controls['Toggle Time'].EventHandler = function()   if Controls['Toggle Time'].Boolean == true then     Uci.SetSharedLayerVisibility('MyUCI', 'Time', true, 'fade')    elseif Controls['Toggle Time'].Boolean == false then     Uci.SetSharedLayerVisibility('MyUCI', 'Time', false, 'fade')   end end ``` |

[Looping arguments](javascript:void(0))

In this example, whenever the Start\_Loop button is pushed, two "for loop" blocks start a countdown - one to 10, and one from 10.

| Blocks | Script Equivalent |
| --- | --- |
|  | ```lua Controls['Start_Loop'].EventHandler = function()   local output = ''   for index = 1, 10, 1 do     output = tostring(output) .. tostring((tostring('-') .. tostring(index)))   end   print('Count to 10')   print(output)   output = ''   for index = 10, 1, -1 do     output = tostring(output) .. tostring((tostring('-') .. tostring(index)))   end   print('Count from 10')   print(output) end ``` |

### Debug Output

```lua
Count to 10
-1-2-3-4-5-6-7-8-9-10
Count from 10
-10-9-8-7-6-5-4-3-2-1
```

[Triggering a Control](javascript:void(0))

In this example, a trigger button control (MyControl) changes color depending on whether a condition is met.

| Blocks | Script Equivalent |
| --- | --- |
|  | ```lua if 5 * 2 == 10 then   Controls['MyControl']:Trigger()   Controls['MyControl'].Color = '#33ff33'  else   Controls['MyControl']:Trigger()   Controls['MyControl'].Color = '#ff0000' end ``` |

[Working with Named Controls](javascript:void(0))

**Note:** Although you can name a control using an ampersand (&), it causes the block controller to stop processing named controls, resulting in the âNamed Componentâ block options not appearing.

When your design contains [Named Controls](external_control.htm), blocks for these controls become available in the block editor from a **Named Controls** drop-down menu:

[
Your browser does not support the video tag.
](../Resources/Videos/BlockController_NamedControls.webm)

In the following example, a timeline (after time) block is configured to trigger playback and set control values in a timed sequence for four named controls from an Audio Player component.

**Note:** For more information about timelines, see [Creating a Timeline](#Creating5). For information about referencing named controls in Lua script, see [NamedControl](../Control_Scripting/Using_Lua_in_Q-Sys/NamedControl.htm).

| Blocks | Script Equivalent |
| --- | --- |
|  | ```lua Timer.CallAfter(function()     NamedControl.Trigger('AudioPlayerPlay')   print('Playback started')     Timer.CallAfter(function()       NamedControl.SetPosition('AudioPlayerGain', 0.75)   print('Gain reduced')       Timer.CallAfter(function()         NamedControl.SetValue('AudioPlayerMute', 1)   print('Playback muted')         Timer.CallAfter(function()           NamedControl.SetValue('AudioPlayerMute', 0)   print('Playback unmuted')           Timer.CallAfter(function()             NamedControl.Trigger('AudioPlayerStop')   print('Playback stopped')           end,5)       end,5)     end,5)   end,15) end,5) ``` |

[Working with Named Components](javascript:void(0))

When your design contains Named Components, blocks for these components become available in the block editor from a **Named Components** drop-down menu:

**Note:** The **Named Components** section only appears if the script access of the Named Component is set to **all** or **script**.

[
Your browser does not support the video tag.
](../Resources/Videos/Block_Controller_NamedComponents2.webm)

In the following example, an Audio Player component's Code Name has been renamed "MyPlayer". In this simple script, blocks from the Named Components drop-down menu for this named component are configured to enable looped playback whenever the Play button is pressed.

**Note:** For information about renaming components to create named components, see [Labeling Schematic Elements](../Q-SYS_Designer/Using_the_Schematic/Labeling_and_Organizing_Schematic_Elements.htm#Labeling__Schematic_Elements). For information about named components in Lua script, see [Component](../Control_Scripting/Using_Lua_in_Q-Sys/Component.htm).

| Blocks | Script Equivalent |
| --- | --- |
|  | ```lua namedComponent_MyPlayer = Component.New('MyPlayer')   namedComponent_MyPlayer['play_state_trigger'].EventHandler = function(ctl)   namedComponent_MyPlayer['loop'].Boolean = true end ``` |

[Color With Block](javascript:void(0))

The Color With Block is a feature within the Q-SYS Designer software that allows for the visual management and customize of the colors of various controls and interfaces.

**Note:** All editable color values in the Block Controller are expressed in percentages only. Ensure that the values range from 0% to 100% for accurate color representation.

#### Color with Red, Green, and Blue

**Red**: This value represents the intensity of the red color in the RGB color model. It ranges from 0% (no red) to 100% (full red). For example, an RGB value of (100%, 0%, 0%) means the color is pure red.

**Green**: Similar to red, this value indicates the intensity of the green color. It also ranges from 0% to 100%. An RGB value of (0%, 100%, 0%) means the color is pure green.

**Blue**: This value shows the intensity of the blue color, ranging from 0% to 100%. An RGB value of (0%, 0%, 100%) means the color is pure blue.

#### Format as

**RGB**: This format uses three values (Red, Green, Blue) to define a color. Each value can range from 0% to 100%. For example, RGB (100%, 65%, 0%) represents the color orange.

**ARGB**: This format adds an Alpha value to the RGB values, which represents the opacity of the color. The Alpha value also ranges from 0% (completely transparent) to 100% (completely opaque). For example, ARGB (100%, 100%, 65%, 0%) represents an opaque orange color.

| Blocks | Script Equivalent |
| --- | --- |
|  | ```lua function colour_ARGB(r, g, b, a)   r = math.floor(math.min(100, math.max(0, r)) * 2.55 + .5)   g = math.floor(math.min(100, math.max(0, g)) * 2.55 + .5)   b = math.floor(math.min(100, math.max(0, b)) * 2.55 + .5)   a = math.floor(math.min(100, math.max(0, a)) * 2.55 + .5)   return string.format("#%02x%02x%02x%02x", a, r, g, b) end     foo = (colour_ARGB(20, 60, 80, 10)) ``` |

[Training Videos](javascript:void(0))

For further explanation of the Block Controller component, see the following videos:

* [Q-SYS Training - Control 101](https://training.qsc.com/course/view.php?id=58)

  Learn the basic Q-SYS third party control principles, including Lua scripting basics.
* [Q-SYS Training - Block Controller Part A](https://training.qsc.com/mod/book/view.php?id=1055)

  Learn about the Block Controller component through a navigational overview. In this lesson, you'll learn how to manipulate a simple button control using blocks.
* [Q-SYS Training - Block Controller Part B](https://training.qsc.com/mod/book/view.php?id=1056)

  Learn about sections of the Block Controller, including control change, flow control, if statements, operators, boolean values, and converting blocks to lua script.
