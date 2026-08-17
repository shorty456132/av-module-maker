# Dante Out

> Source: https://help.qsys.com/Content/Schematic_Library/io_dante_output_card_core.htm

# Dante Out

The Q-SYS Dante input / output card provides a means of receiving and transmitting to and from other Dante enabled devices on a Dante network.

[Channel and Flow Usage](javascript:void(0))

As a general rule, the Q-SYS Dante Card channel and flow allocation is as follows:

* Each unicast flow can have a maximum of 4 channels.
* Each multicast flow automatically uses 8 channels.

However, the actual number of consumed channels and flows is based on the individual site circumstances â i.e., how many devices are subscribed to each flow.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Input/Output Count

Determines the number of input and output channels: 2x2, 4x4, 8x8, 16x16, 32x32, or 64x64.

#### Dante Sample Rate

Sets the Sample rate, in kHz. Available choices are dependent on the selected Input/Output Count: 44.1, 48, 88.2, 96.

#### Dante Receive Latency

This setting defines the latency, in milliseconds, between the timestamps on the incoming audio samples and when those samples are played out: 0.15, 0.25, 0.5, 1, 5.

#### External Configuration

Determines whether Dante card configuration is allowed by an external program, such as Dante Controller:

* When set to Yes, you configure the Dante card with an external program. In this mode, some controls within the Dante component in Q-SYS Designer become read-only.
* When set to No, you configure the Dante card with the Dante component in Q-SYS Designer. In this mode, any changes you make in an external program are ignored.

[Controls](javascript:void(0))

Each control listed in the Dante and Digital sections, are one per channel.

### Dante

#### Peak Output Level (dBFS)

Measures Peak Output level to the output device

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

Controls the gain of the digital audio signal prior to the D/A converter, from -10 to +21 (default is 21).

### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

**Note:** Dante card (CDN64) "Initializing" status can appear for 10-20 seconds during design startup.

### Config

#### Name

The name of the output channel on a device, also called the Active Name. The name must be less than or equal to 31 characters and cannot contain '.' , '=', or '@' characters. If you either don't provide a custom name or clear an existing Name control, the default name is used, which is the channel number â for example "04".

#### Flow

The name of the flow. Usage depends on the setting for Properties > External Configuration.

When External Configuration is set to Yes:

* Flow control is read-only, and displays the flow info for the channel as configured in Dante Controller.

When External Configuration is set to No:

* The default is "Auto". The channel will use an automatically configured unicast flow.
* If you enter a string other than "Auto", the channel is added to the multicast flow with the specified name.
* A new flow is created if one doesn't already exist with that name.
* The flow name must be less than or equal to 31 characters and cannot contain '.' , '=', or '@' characters.

#### Device Name

The name used to identify the particular device on the network.

#### Names and Flows > Reset All

Click to clear all channel Names and reset Flows back to "Auto".

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Level | 27.0 to -55 | 27.0 to -55 | 0 to .988 | Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Tx Flow | (text) | | | Input / Output |
| Tx Name | (text) | | | Input / Output |
| Device Name | (text) | | | Input / Output |
| Output Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
