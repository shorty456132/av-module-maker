# Dante In

> Source: https://help.qsys.com/Content/Schematic_Library/io_dante_input_card.htm

# Dante In

The Q-SYS Dante input / output card provides a means of receiving and transmitting to and from other Dante enabled devices on a Dante network.

[Channel and Flow Usage](javascript:void(0))

As a general rule, the Q-SYS Dante Card channel and flow allocation is as follows:

* Each unicast flow can have a maximum of 4 channels.
* Each multicast flow automatically uses 8 channels.

However, the actual number of consumed channels and flows is based on the individual site circumstances â i.e., how many devices are subscribed to each flow.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Input/Output Count

Determines the number of input and output channels: 2x2, 4x4, 8x8, 16x16, 32x32, 64x64

#### Dante Sample Rate

Sets the Sample rate, in kHz. Available choices are dependent on the selected Input/Output Count: 44.1, 48, 88.2, 96

#### Dante Receive Latency

This setting defines the latency, in milliseconds, between the timestamps on the incoming audio samples and when those samples are played out: 0.15, 0.25, 0.5, 1, 5

#### External Configuration

Determines whether Dante card configuration is allowed by an external program, such as Dante Controller:

* When set to Yes, you configure the Dante card with an external program. In this mode, some controls within the Dante component in Q-SYS Designer become read-only.
* When set to No, you configure the Dante card with the Dante component in Q-SYS Designer. In this mode, any changes you make in an external program are ignored.

[Controls](javascript:void(0))

### Dante

#### Peak Input Level

Meters for each channel indicating the peak Dante input level, in dBFS. The measurement is taken directly from the Dante input signal before the Digital Controls (Invert/Gain/Mute). Range is from -100 to 20.

### Digital

#### Invert

Toggle button to invert the digital output of the signal.

#### Mute

Mutes the output signal.

#### Gain

Controls the Gain, in dB, of the digital output signal. Range is -100 to 20 (default is 0).

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

### Subscriptions

A Q-SYS input channel can subscribe to a specific channel on a specific device. The transmitting device is given a name and each channel on that device is also given a name.

Each channel has the following controls.

#### Device

The Device is selected for a Q-SYS input channel from a list of Dante output devices advertising on the network. The Device name is a unique name on the Dante network.

The Device drop-down menu can display:

* Device Name only â The Channel control then displays all the channels available on the device. For Q-SYS Core processor devices, this includes channels from all Software Dante components.
* Device Name : Channel Group â The Channel control then displays only the channels from the selected Channel Group. For Q-SYS Core processor devices, this would be the channels only from the selected Software Dante component name.

#### Channel

The Channel is selected from a list of channel names on the selected Device. Each channel has a unique name on the device.

Each Dante Channel has a name that is set by the transmitting device that cannot be changed by the Receiver. The Q-SYS CDN64 Dante card, for example, uses channel names "01", "02", etc. Each Dante Channel also uses an optional Name, which can be set by the end user with the Name control in the [Dante Out](io_dante_output_card.htm) component in Q-SYS (when the External Configuration property is set to 'No') or with Audinate's Dante Controller software (when External Configuration is 'Yes').

#### Subscription Status

The LED and status bar indicate the current status of the channel subscription. Normally, this should indicate 'OK'. A 'Fault' status indicates a problem with the channel subscription. If the message following the 'Fault' status is in all caps, it is a message returned directly from the Dante code.

These are some common Dante subscription status messages:

* Initializing - UNRESOLVED: Dante is looking for the device to whose channel it is subscribed.
* Compromised - Unresolved: Timed out looking for the device.
* Fault - NO\_TX: The Dante transmitting device to which Q-SYS is trying to subscribe has run out of Transmit Flows.
* Fault - NO\_RX: This Dante receiver has run out of available Receive Flows.

#### Subscriptions > Clear All

Click to clear all Devices and Channels for all output channels.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**. Each channel on the Dante Input card has the following Control Pins with the exception of Status.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Level | 27.0 to -55 | 27.0 to -55 | 0 to .988 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Output |
| Subscription Channel | (text) | | | Input / Output |
| Subscription Device | (text) | | | Input / Output |
| Subscription Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
| Input Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
