# CobraNet In

> Source: https://help.qsys.com/Content/Schematic_Library/io_cobranet_input_card.htm

# CobraNet In

The [CobraNet card](../Hardware/IO_Expanders/CCN32.htm) gives you a total of sixteen inputs and sixteen outputs of CobraNet digital audio when used in an I/O Frame. When used in a Q-SYS Core, you can have 32 inputs, and 32 outputs. You can also use the CobraNet inputs to sync Q-SYS to an external clock source. Refer to the [Core Status](core_status.htm) topic for details. In Q-SYS Designer, the CobraNet card has two components associated with it that you can add to your design; an Input Component, and an Output Component. This topic is for the CobraNet Output component.

## Type 2 Hardware

The CobraNet card is available only in Type 2 hardware.

Type 2 hardware provides new cables and connectors between the I/O cards and main boards in Cores and I/O Frames. Due to this change, the Type 2 hardware is not physically compatible with the older hardware. You can still integrate the new I/O Frames and Cores in the same system with older hardware, but the I/O cards are not interchangeable. Type 2 hardware can be identified by a yellow label on the back of the Core and I/O Frame, and the bottom of the I/O cards.

[Properties](javascript:void(0))

When the CobraNet In component is selected in the Schematic, you will see all of the Properties of the Core or I/O Frame in which it is installed. Under the I/O Frame slot in which the card is installed, or under the Core I/O Slot, you can set the Input and Output Counts for the CobraNet card.

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Input Count

The number of input or output pins available on the CobraNet input or output component.

An I/O Frame can have a maximum of 16 input channels, and 16 output channels regardless of the I/O card types. A Core can have up to 32 input channels, and 32 output channels with a CobraNet card.

The CobraNet card has four modes: 4 x 4, 8 x 8, 16 x 16, and 32 x 32 (32x32 Core only). On an I/O Frame you can mix the I/O cards, as long as the total channel count does not exceed 16 inputs and 16 outputs, regardless if the channels are wired in the design or not.

[Controls](javascript:void(0))

### CobraNet

#### Peak Input Level (dBFS)

Graphic display of the peak input level to the CobraNet Input, measured in dBFS.

### Digital

#### Invert

Inverts the input signal.

#### Mute

Mutes the input signal.

#### Gain (dB)

Sets the gain of the input signal.

### Status

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Level (Peak Input Level (dBFS)) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Status | Text | | | Output |
