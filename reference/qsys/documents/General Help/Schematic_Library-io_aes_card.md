# AES3 In / Out

> Source: https://help.qsys.com/Content/Schematic_Library/io_aes_card.htm

# AES3 In / Out

The AES3 Input / Output in Q-SYS Designer has two associated components that you can add to your design; an Input Component, and an Output Component. The [AES3 Card](../Hardware/IO_Expanders/CAES4.htm) gives you a total of four inputs and four outputs (two input ports and two output ports) of AES3 digital audio.

You can also use the AES3 inputs to sync Q-SYS to an external clock source. Refer to the [Core Status](core_status.htm) topic for details. The AES3-1 and AES3-2 options display in the Core's Properties when you have an AES3 In / Out card selected for the Core I/O slot. Use these options to sync to an external AES3 signal. The AES3 selections require either regular AES3 or AES3 black. The clock should be connected to the [AES3 card](../Hardware/IO_Expanders/CAES4.htm) either connector **Channel 1/2 In**, or **Channel 3/4 In**.

**Note:** Typically, Internal is used as the clock source. Only if there is a need to synchronize the Q-SYS system to an external clock would you use GPIO or AES3. You would use GPIO if the external clock signal is a word clock. You would use AES3 if the external clock signal is an AES3 signal. Often an AES3 signal without audio is used to reduce the clock jitter. This signal is called AES3 black.

## Type 2 Hardware

Type 2 hardware provides new cables and connectors between the I/O cards and main boards in Cores and I/O Frames. Due to this change, the Type 2 hardware is not physically compatible with the older hardware. You can still integrate the new I/O Frames and Cores in the same system with older hardware, but the I/O cards are not interchangeable. Type 2 hardware can be identified by a yellow label on the back of the Core and I/O Frame, and the bottom of the I/O cards.

[Properties](javascript:void(0))

When the AES In component is selected in the Schematic, you will see all of the Properties of the Core or I/O Frame in which it is installed. The only Property for the AES3 In component is Sample Rate Conversion. The AES3 Out component does not have any Properties.

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Sample Rate Conversion

Determines if the Sample Rate Conversion is done by the AES3 In card or not.

[Controls](javascript:void(0))

[AES3 In](javascript:void(0)) 

### AES3

#### Lock

LED indicating that the card is receiving a valid AES input signal.

#### Peak Input Level (dBFS)

Graphic display of the peak input level to the AES3 Input, measured in dBFS.

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

[AES3 Out](javascript:void(0))

### AES3

#### Peak Input Level (dBFS)

Graphic display of the peak output level, measured in dBFS.

### Digital

#### Clip

Indicates if the signal is in clipping or not.

#### Clip Hold

Holds the clip indication until manually cleared.

#### Invert

Inverts the output signal.

#### Mute

Mutes the output signal.

#### Gain (dB)

Sets the gain of the output signal.

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

### AES3 Input

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Channel 1-*n* | | | | |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Level (Peak Input Level (dBFS)) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Lock | 0  1 | false  true | 0  1 | Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Status | N / A | Text | N / A | Output |

### AES3 Output

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Channel 1-*n* | | | | |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Level (Peak Output Level (dBFS)) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
