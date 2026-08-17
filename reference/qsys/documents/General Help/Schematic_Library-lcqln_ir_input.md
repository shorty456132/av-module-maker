# IR Input (QIO-IR1x4)

> Source: https://help.qsys.com/Content/Schematic_Library/lcqln_ir_input.htm

# IR Input (QIO-IR1x4)

The IR Input component represents the single IR Input connection on a [QIO-IR1x4](../Hardware/IO_Expanders/QIO-IR1x4.htm) device. Use the component to configure port communication and monitor IR activity to the port.

[Inputs and Outputs](javascript:void(0))

### Input Pins

This component has no input pins.

### Output Pins

#### IR Input Out

Connect this pin to the IR Source pin of the [IR Receiver](ir_receiver.htm) component or the [IR Output (QIO-IR1x4)](lcqln_ir_output.htm) component. You can connect this pin to multiple IR components (fan-out).

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

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Assign component to

Select whether the IR Input is assigned to the Core (default) or an I/O Frame in your design. For I/O Frame, you must also type the Name of the device in your design.

[Controls](javascript:void(0))

#### Carrier Frequency (kHz)

If you know the frequency of the IR receiving device, specify it here, from 26 to 460 (default is 30). Otherwise, use Auto Detect.

#### Auto Detect

When enabled, the QIO-IR1x4 will attempt to detect the Carrier Frequency of the IR device.

#### Port Activity

This LED turns on whenever the IR Input port is actively receiving information.

#### Last Received Code

This is the IR code that was last received by the IR Input. This field remains populated with the last received code until the next code is received.

#### Active Code

This is the IR code currently being received.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Active Code | (text) | | | Output |
| Carrier Frequency | 26 to 460 | 26 to 460 | - | Input / Output |
| Carrier Frequency Auto Detection | 0  1 | false  true | 0  1 | Input / Output |
| Last Received Code | (text) | | | Output |
| Port Activity | 0  1 | false  true | 0  1 | Output |

[IR Input and Output Troubleshooting](javascript:void(0))

### IR Emitter/Transmitter support

The QIO-IR1x4 works with a wide range of emitters/transmitters from various manufacturers. Devices from Inteset, BAFX, Herfair, and uxcell have been used successfully with QIO-IR1x4. However, these devices can vary widely with regard to pinout, operating voltage, and supported carrier frequency. Refer to the manufacturer's specification sheet to confirm compatibility.

### IR Input: "Compromised - IR Rx protocol not recognized" error

This error indicates that auto detection of the IR carrier frequency has failed. You can either try sending a code again (and attempt to detect the Carrier Frequency again) or turn off the Auto Detect control and manually specify a Carrier Frequency based on the IR device specifications.
