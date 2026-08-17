# IR Driver

> Source: https://help.qsys.com/Content/Schematic_Library/ir_driver.htm

# IR Driver

Use the IR Driver component to send commands to the [IR Output (QIO-IR1x4)](lcqln_ir_output.htm) component (to transmit those commands to an IR receiving device, such as a television, media manager, DVD player, etc.) or an [IR Receiver](ir_receiver.htm) component in your design (to save and label commands). You can select IR commands from an extensive database of IR device brands, types, and models.

[Configuration Overview](javascript:void(0))

1. From the Schematic Elements > Components > Control Components category, drag an IR Driver component into your design.
2. From the Properties pane, select how many commands to send. See [Properties](#Properti).
3. Wire the IR Driver Out pin to one or more IR Source pins.
4. Run (F5) or emulate (F6) the design.
5. Double-click the IR Driver component to open the control panel.
6. From the combo boxes, select a Brand, Type, and Model to load a command set.
7. For each Command, select a command from the list.
8. Click Send to send the command.

[Inputs and Outputs](javascript:void(0))

### Input Pins

This component has no input pins.

### Output Pins

#### IR Driver Out

Connect this pin to the IR Source pin of the [IR Output (QIO-IR1x4)](lcqln_ir_output.htm) component or the [IR Receiver](ir_receiver.htm) component. You can connect this pin to multiple IR components (fan-out).

[IR Schematic Examples](javascript:void(0))

These examples demonstrate some use cases for all four IR-related components in Q-SYS Designer Software:

* IR Driver and IR Receiver, which are located within the Schematic Elements > Components > Control Components category
* IR Input and IR Output, which are located within the QIO-IR1x4's Inventory tree.

### Sending IR Commands

[Example 1: Single IR Driver to a single IR Output](javascript:void(0))

In this example, an IR Driver sends commands for a TV device to a single TV (or perhaps multiple TVs of the same model) in the same room.

[Example 2: Single IR Driver to multiple IR Outputs](javascript:void(0))

In this example, an IR Driver sends commands for a TV device to each of the four IR Outputs of the IR1x4. An emitter is placed in each room, and each room has the same model TV. This example shows a hypothetical setup for a restaurant that contains four spaces with entertainment.

[Example 3: Multiple IR Drivers to multiple IR Outputs](javascript:void(0))

This example is similar to Example 2, except that two rooms have TVs of one model and the other two rooms use a different model. Therefore, two IR Drivers are required.

[Example 4: Multiple IR drivers to multiple IR Source inputs](javascript:void(0))

This example demonstrates how multiple IR Drivers - each for a different IR device - can be sent to multiple IR Outputs, with some IR Outputs sending IR commands from multiple sources. Each room has an IR emitter connected to an IR Output of the QIO-IR1x4.

* The Lounge and Entry only contain a TV.
* The Bar contains both a TV and a Media Player. Its IR Source Count property is set to '2'.
* The Patio has a TV, DVD player, and Media Player. Its IR Source Count property is set to '3'.

**Note:** For those IR Outputs sending commands from multiple sources (Bar and Patio), only a single IR command can be sent at a time.

### Receiving IR Commands

[Example 5: IR Input to IR Receiver](javascript:void(0))

In this example, the QIO-IR1x4's IR Input receives IR commands from an IR device â for example, a remote control for a TV that is not in the IR Driver's database. Each command can then be saved and labeled in the IR Receiver component.

**Tip:** Commands are saved locally within the IR Receiver component within the design.

[Example 6: Multiple IR Inputs to IR Receiver](javascript:void(0))

In this example, an IR Receiver can learn commands from two QIO-IR1x4 devices. The IR Receiver's IR Source Count property is set to '2'.

[Example 7: IR Receiver configured to send](javascript:void(0))

Similar to Example 5, an IR Receiver learns commands from a QIO-IR1x4's IR Input. However, those learned commands can then be sent to one or more IR Outputs. In this example, the IR Receiver's Enable Transmit property is set to 'Yes'.

[Example 8: Receiving and relabeling commands from an IR Driver](javascript:void(0))

In this example, an IR Receiver receives commands from an IR Driver. This is useful for relabeling commands from the IR Driver's database when a different description is desired.

### Relaying IR Commands

[Example 9: IR Input direct to IR Outputs](javascript:void(0))

In this example, a QIO-IR1x4's IR Input is wired directly to its IR Outputs. This would be useful if you have an IR receiving device in one area but you want to control IR devices in other areas that are out of view of the receiver. The QIO-IR1x4 will simply relay the received commands to its outputs.

[Example 10: Multiple IR Inputs direct to IR Outputs](javascript:void(0))

This example is the same as Example 9, except that the Conference Room devices can be controlled from two locations. "Front Desk" represents the IR Input on one QIO-IR1x4 device, while "Conf Rm Hall" is the IR Input on another QIO-IR1x4.

[Properties](javascript:void(0))

### IR Driver Properties

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Number of Commands

Specify how many Command controls are available within the component, from 1 to 256 (default is 8).

#### Commands per Page

Specify how many Command controls appear on each page/tab: 8, 16, 24, 32 (default), 64, 128, or 256. This property has no effect if the Number of Commands property is less than Commands per Page.

[Controls](javascript:void(0))

#### Brand, Type, Model

Starting with Brand, select the IR device for which you want to display selectable commands to send. All three combo boxes must have selections for a Command list to appear. The combo boxes turn red if a re-selection is required based on changing the Brand or Type.

#### Command *n*

Once you have selected a Brand, Type, and Model for your IR device, you can then select an individual command for each Command combo box.

#### Send

Once you have individual commands for each Command combo box, you can hit Send to deploy the command.

**Tip:** IR codes have a one-time burst and a repeat burst. Pressing Send will emit the one-time burst while pressing and holding will continue emitting the repeat burst until the send button is released.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Command *n* | | | | |
| Button | 0  1 | false  true | 0  1 | Input / Output |
| Command | (text) | | | Input / Output |
| Brand | (text) | | | Input / Output |
| Model | (text) | | | Input / Output |
| Type | (text) | | | Input / Output |
