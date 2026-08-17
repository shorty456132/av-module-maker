# AVB In

> Source: https://help.qsys.com/Content/Schematic_Library/io_avb_input_card.htm

# AVB In

The AVB Input and Output are on the same physical card but are represented in the Q-SYS design by an AVB Input Component and an AVB Output Component.

The AVB Intput component provides connections for inputs up to 32 channels in 4 streams for devices supporting the AVB protocol. Other combinations of input/output are described in the Properties section below. Connection is made with CAT-5 / RJ-45 connector.

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

### AVB

#### Peak Input Level (dBFS)

Meters for each channel indicating the peak AVB input level. The measurement is taken before the Digital Gain.

### Digital

#### Invert

Toggle button to invert the digital output of the AVB input card.

#### Mute

Mutes the output signal.

#### Gain (dB)

Controls the Gain of the digital input signal.

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

### Listener Stream Connections

There are two ways you can connect an AVB Listener to an AVB Talker:

1. AVDECC (1722.1) (see <https://avb.statusbar.com/article/1722.1-features/>): This is the typical method and it involves a 3rd-party AVB management software for example: Riedel AVB Manager or Pivitec's AVDECC Controller. There are others available.
2. Directly via "Full Stream ID": Each stream on the network has a unique 64-bit stream ID (Full Stream ID). If you know the Full Stream ID you can just tell your Listener to listen to that stream and bypass AVDECC and any related third-party software.

#### Clear (Momentary button)

Removes all Listener / Talker mapping (AVDECC or Full Stream ID), disconnects the Listener from the Talker and audio stops.

#### AVDECC Entity and Unique ID

Read Only. IEEE-defined 64-bit Extended Unique Identifier of an AVDECC Entity. These codes are automatically derived from the Talker Stream connected to the Listener.

#### Full Stream ID

Read / Write. Enter the Unique 64-bit stream ID of the Talker Stream. When this information is entered, it removes the AVDECC information for that stream.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

### Per Channel Controls

Each channel on the AVB Input card has the following Control Pins.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Peak Input Level  (dBFS) | -120 to | -120 to | 0.00 to 1.00 | Output |

### Common Control Pins

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Clear Stream 1 and 2 | 0  1 | false  true | 0  1 | Input / Output |
| Input Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
