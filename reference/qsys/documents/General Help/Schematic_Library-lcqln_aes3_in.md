# AES3 In (QIO Series)

> Source: https://help.qsys.com/Content/Schematic_Library/lcqln_aes3_in.htm

# AES3 In (QIO Series)

The AES3 Input / Output in Q-SYS Designer has two associated components that you can add to your design; an Input Component, and an Output Component. The [QIO-AES8x8](../Hardware/IO_Expanders/QIO-AES8x8.htm) gives you a total of eight inputs and eight outputs (four input ports and four output ports) of AES3 digital audio.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### QIO-AES8x8 Properties

#### Channel 1/2 3/4 5/6 7/8 SRC Disabled

Determines if the Sample Rate Conversion is done by the AES3 In or not.

[Controls](javascript:void(0))

### AES3

#### Lock

LED indicates that the device is receiving a valid AES input signal.

#### Peak Input Level (dBFS)

Graphic display of the peak input level to the AES3 Input, measured in dBFS.

### Digital

#### Invert

Inverts the input signal.

#### Mute

Mutes the input signal.

#### Gain

Controls the Gain of the digital input signal, from -100 to 20 dB (default is 0).

### Status

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
| Channel 1-*n* | | | | |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Level (Peak Input Level (dBFS)) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Lock | 0  1 | false  true | 0  1 | Output |
| Mute | 0  1 | false  true | 0  1 | Input / Output |
| Status | N / A | Text | N / A | Output |
