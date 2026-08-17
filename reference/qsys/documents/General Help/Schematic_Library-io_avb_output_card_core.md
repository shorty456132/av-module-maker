# AVB Out

> Source: https://help.qsys.com/Content/Schematic_Library/io_avb_output_card_core.htm

# AVB Out

The AVB Input and Output are on the same physical card but are represented in the Q-SYS design by an AVB Input Component and an AVB Output Component.

The AVB Output component provides an output up to 32 channels in 4 streams for devices supporting the AVB protocol. Other combinations of input/output are described in the Properties section below. Connection is made with CAT-5 / RJ-45 connector.

For hardware information, see [CAN32 â AVB Audio Video Bridge Card](../Hardware/IO_Expanders/CAN32.htm).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Input / Output Count

You can choose from any of the following:

* 2x2 - 2 channels in, 2 channels out
* 4x4 - 4 channels in, 4 channels out
* 8x8 - 8 channels in, 8 channels out
* 16x16 - 16 channels in, 16 channels out
* 32x0 - 32 channels in, 0 channels out (no Output Component)
* 0x32 - 0 channels in, 32 channels out (no Input Component)

#### Talker Channels / Stream

You can have from 2 to 32 channels per stream.

If you select 32 (in or out) channels, and 2 channels per stream, the maximum number of channels is 24.

If you select 16 x 16 channels and 1 listener channel per stream, the inputs are limited to 14.

#### Listener Channels / Stream

You can have from 2 to 32 channels per stream.

If you select 32 (in or out) channels, and 2 channels per stream, the maximum number of channels is 24.

If you select 16 x 16 channels and 1 talker channel per stream, the outputs are limited to 14.

[Controls](javascript:void(0))

Each control listed in the Analog and Digital sections, are one per channel.

### Stream

#### Channels

The Channel tabs switch between channel ranges. The available ranges depend on the Input / Output count in the Properties. The controls are the same for each stream.

### AVB

#### Peak Output Level (dBFS)

Measures Peak Output level to the output device for each channel.

### Digital

#### Clip

Red LED indicating if the signal is being clipped.

#### Clip Hold

Holds the clip indication until manually cleared.

#### Invert

Inverts the audio signal.

#### Mute

Mutes the digital audio signal.

#### Gain

Controls the gain of the digital audio signal prior to the D/A converter.

### Status

#### Status LED

This LED changes color to indicate the current status of the I/O-22 Output. See Status for the meanings of the various colors.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

### Talker Streams

#### Stream Prefix

Allows you to enter a 12-byte hex number of your choice. Typically the FSID is derived from the MAC address of the AVB card.

#### Stream Prefix Set Button

After entering the 12-byte hex number in the Stream Prefix file, press this button to "set" that number is the ID

#### Stream *<n>* Full ID (FSID)

Read only. The FSID of each Talker Stream is shown here.

This is the stream Prefix with a 4-byte stream index appended.

You can copy this value and paste it into an AVB Input component's Full Stream ID field.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Level | 27.0 to -55 | 27.0 to -55 | 0 to .988 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
