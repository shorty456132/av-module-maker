# Attero Tech unA6IO

> Source: https://help.qsys.com/Content/Schematic_Library/Attero_Tech_extension_unA6IO.htm

# Attero Tech unA6IO

Use this extension to connect to and control the unA6IO AES67 in-wall I/O interface (Attero Tech by QSC).

**Note:** See the [Attero Tech Discontinued Products page](https://www.qsys.com/systems/support/discontinued-products/attero-tech/) on the QSC website for product information and documentation.

[Compatibility](javascript:void(0))

The extension is compatible with Q-SYS Designer version 8.4 and above and Attero Tech firmware 1.1.1.2 and above. For best results, use the latest Attero Tech device firmware.

[Connection Setup](javascript:void(0))

1. In the NIC field, select the interface through which the extension will communicate to control the device.
2. In the IP field, specify the IP address of the device and press Enter.

The extension will automatically attempt a connection. The "Connected" LED glows green once a connection is established. If the extension loses its connection to the device, it will attempt to re-establish the connection every 5 seconds.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### QoS Mode

Sets the DSCP values the device uses when transmitting audio streams - AES67 (default) or Dante.

#### Show Debug

Select 'Yes' to show the Debug Output window. For details, see [Debug Output](debug_output.htm).

[Controls](javascript:void(0))

#### Force Config

If the extension detects that the configuration of the device does not match those set in the extension, click the button to update the device settings to match.

#### Refresh

Although the extension monitors the device settings for changes automatically, this button manually triggers the extension to retrieve the current settings and update the extension values to match.

#### Meters

Enables metering within the extension. The extension polls for metering information once a second and updates signal presence indicators and Dante Rx status for each channel accordingly. The metering function remains active until manually turned off. Click the button to toggle between states.

#### Identify

Causes the power LED on the front of the device to start blinking so it can easily be identified. The identify function remains active until manually turned off. Click the button to toggle between states.

#### Status

Normally, this shows "Initializing" for a few moments after starting your design, followed by "OK". If you see a "Fault" status, check your connection parameters. If you see "Missing", ensure that the device is powered on and connected to the network.

#### Details

Provides information on the connected device such as MAC address, IP address, firmware version, power type, and the data model version.

#### Save as Default

Forces the device to save its current settings as the new power-on defaults.

### Input Settings

#### Signal Indicator

LED for each channel. Only active when metering is enabled.

* Green = signal
* Grey = no signal (<60dB)
* Red = clipping

#### Input Gain

For channels 1 and 2 only, select the gain level for the input:

* Line (-15dB pad)
* Line (no Pad)
* Low Mic (+25dB)
* High Mic (+40dB)

#### Phantom Power

For channels 1 and 2 only, select the state of phantom power for the input. If the button is gray, the phantom power is inactive. If itâs orange, the phantom power is active. Click the button to toggle between states.

#### Input Select

For channels 3 and 4 only, select what unbalanced audio input is made available to the Dante network. Either the RCA, 3.5mm jack, or a mix of both can be selected for the left and right audio:

* A [RCA]
* B [3.5mm]
* A+B [Both]

### Output Settings

#### Signal Indicator

LED for each channel. Only active when metering is enabled.

* Green = signal
* Grey = no signal (<60dB)
* Red = clipping

#### Volume

Sets the volume on each output, from -60 to 0dB.

#### Mute

Toggles muting of an output. If the button is gray, the mute is inactive. If itâs orange, the mute is active.

### Network Settings

**Note:**  Except for the TX Stream and Pilot Tone controls, these are for indication only. To make changes to the other settings, use the Attero Tech unIFY application.

#### PTP Clock Sync

Indicates if the device is synchronized to a clock master.

#### PTP Clock Role

Indicates if this device is acting as a clock master or a clock slave.

#### Qos Mode

Indicates the QoS mode set in the extension properties, either Audinate or AES67.

#### Device Name

Shows the name the unit uses to advertise itself on the network. The name is also what the unIFY application indicates within its AES67 device list.

#### IP Address Mode

Indicates the devices IP address mode â Static or Dynamic.

#### Rx Stream State

There is one indicator for each device analog output that shows the state of the output stream:

* If the indicator is off, no audio is allocated.
* Green indicates that the assigned stream is connected and ok.
* Red indicates that audio is allocated but the device is not receiving it.

#### Rx Stream Name

The name of the allocated stream, which can be different for each output.

#### Rx Stream CH

The specific channel from the allocated stream thatâs being sent to the device's analog output.

#### Tx Stream Name

The name of the stream that is used when the stream is advertised to other devices.

#### Tx Stream IP

The multicast IP address used to transmit this stream's audio, typically in the range 239.69.xxx.xxx.

**Note:** This address cannot be the same as other AES67 streams on the system.

#### Tx Stream Enable

Toggles if a stream is transmitted from the unit with the device's audio or not.

#### Pilot Tone Enable

Sets whether the pilot tone generator is active or not.

#### Pilot Tone Frequency

Sets the frequency of the generated pilot tone, from 20 to 20000 Hz.

#### Pilot Tone Volume

Sets the level of the generated pilot tone, from -100 to 0 dB.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Device | | | | |
| Connected | 0  1 | false  true | 0  1 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Metering | 0  1 | false  true | 0  1 | Input / Output |
| Pilot Tone Enable | 0  1 | false  true | 0  1 | Input / Output |
| Pilot Tone Freqency | 20 to 20000 | 20 to 20000Hz | 0.00 to 1.00 | Input / Output |
| Pilot Tone Volume | -100 to 0 | -100 to 0dB | 0.00 to 1.00 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Input Gain | | | | |
| 1, 2 | - | Line (-15dB pad)  Line (no pad)  Low Mic (+25dB)  High Mic (+40dB) | - | Input / Output |
| Input Select | | | | |
| 1, 2 | - | A [RCA]  B [3.5mm]  A+B [Both] | - | Input / Output |
| Input Signal Presence | | | | |
| 1, 2, 3, 4 | 0  1 | false  true | 0  1 | Output |
| Network | | | | |
| RX State | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Output |
| PTP Clock Role | (text) | | | Output |
| PTP Clock Sync | 0  1 | false  true | 0  1 | Output |
| Tx Stream Name | (text) | | | Output |
| Tx Stream State | 0  1 | false  true | 0  1 | Output |
| Output Mute | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Output Signal Presence | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Output |
| Output Volume | | | | |
| 1, 2 | -60 to 0 | -60dB to 0dB | 0.00 to 1.00 | Input / Output |
| Phantom Power | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Disable[1](#Use) | 0  1 | disabled  enabled | 0  1 | Input / Output |

###### 1. Use this control pin to enable or disable the extension in your design. When Disabled is set to enabled (value of 1), the Connection Status changes to "Not Present - Disabled".
