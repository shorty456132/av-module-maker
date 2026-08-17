# Status (NV-1-H-WE)

> Source: https://help.qsys.com/Content/Schematic_Library/vstreamer_nv1wp_status.htm

# Status (NV-1-H-WE)

The NV-1-H-WE Status component provides detailed information about the NV-1-H-WE, including hardware health, network AV source details and statistics, and Q-SYS Core audio streaming details (if applicable).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Network Video Endpoint Properties

#### AV IP Streaming

For Encoders only, this property determines the network streaming method for Q-LAN AV streams:

* Compiler Choice: (Default) Select this option to allow Q-SYS Designer Software to determine whether unicast (one-to-one) or multicast (one-to-many) is best for your configuration. This is the recommended option.
* Unicast: Select this option when your design contains one-to-one AV routing, meaning that each AV output pin in your design is connected to a single AV input pin.
* Multicast: Select this option when your design contains one-to-many AV routing, meaning that an AV output pin is connected to multiple AV input pins.

[Controls](javascript:void(0))

The NV-1-H-WE shows the following tabs:

* [Status](#Status)
* [Network AV Sources](#Network)
* [Core Stream Details](#Core)

## Status

### NV-1-H-WE Status

#### ID

Click to flash the green ID LED on the front of the NV-1-H-WE unit. The indicator flashes indefinitely until you press the ID button again.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### Processor Temperature

The current temperature, in Celsius, of the NV-1-H-WE central processing unit.

#### Chassis Temperature

The current temperature, in Celsius, of the NV-1-H-WE HDMI I/O hardware.

#### Fan

Indicates the current RPMs of the fan within the NV-1-H-WE.

### Power

#### PoE = 30W, Class 4

This LED glows if the NV-1-H-WE is receiving power from a switch port that supports the required PoE with a power output of 30W, classified as Class 4.

### Network

#### Grandmaster

Displays either the Q-SYS Core processor name or the PTP Clock GUID. Note that:

* There can only be one Grandmaster for a Q-SYS design (for all LAN interfaces of the device). It is possible for Q-SYS to resolve to a PTP Grandmaster present on LAN B, if enabled and present.
* If available, the Core Name is displayed instead of the raw PTP clock GUID. (The Core Name is not available in some clocking topologies â for example, when a higher priority boundary clock between systems is present or with some Software Dante configurations, as when the Core syncs indirectly to another device via Software Danteâs boundary clock.)
* A PTP Clock GUID can look similar to a MAC address, but is not the same and may not be related to a deviceâs actual MAC address.
* If the PTP Clock GUID is derived from a MAC address (whether a Q-SYS Core processor or third-party device), it can be any MAC address on that device (any LAN interface, including those without a network connection).

#### Clock Offset

Indicates how much of an offset exists, in microseconds, between the device and the network Grandmaster.

#### Parent Port

The clock Parent Port is the device and interface name to which the device is syncing. Typically, this is the Grandmaster.

### LAN A

#### Link

When the LED is lit, it means the interface is "UP," signifying that the network connection is active and functioning properly. Conversely, when the LED is not illuminated, it indicates that the interface is "DOWN," suggesting that there may be issues with the network connection.

#### IP Address

Displays the IP Address the Core is connected to.

#### Mode

Determines how device operates within the network environment.

*Auto*: The network interface automatically negotiates it settings with the network infrastructure.

*Static*: The network interface's settings are manually configured by the user, including the IP address, subnet mask, gateway, and other parameters.

*Off*: Disables the network interface, preventing it from sending or receiving network traffic.

#### Speed

Refers to the data transfer rate supported by a network interface or connection. Speed indicates the transfer rate of megabits per second (Mbps).

#### PTPv2 State

Refers to the operational state or role of a network device or interface.

*Passive*: A device in the passive state is not actively transmitting or receiving data.

*Slave*: A device in the slave state is subordinate to another device, known as the master.

*Master*: A device in the master state holds authority or control over one or more slave devices in a network.

*Uncalibrated*: The uncalibrated state indicates a transition state between modes.

### Status LED

#### LED

Sets the Status LED to Bright, Dim, or Off.

## Network AV Sources

This tab reports the audio and video details and statistics for any HDMI Input on the NV-1-H-WE connected to a [Generic AV Source](vst_hdmi_source.htm).

#### Audio

The Details section displays cumulative information for HDMI audio being received from the source. This information resets during a design restart on the Q-SYS Core or whenever you click Reset Details.

#### Video

This section displays cumulative count information for HDMI video being received from the source and transmitted to a destination display. Information refreshes every second. Click Reset Statistics to clear the information.

* Tx Count: The number of video network packets actually placed on the network. This is the Payload Count less Drop Count.
* Drop Count: The number of video network packets that could not be placed on the network.
* Payload Count: The number of video network packets intended to be placed on the network.
* Bitrate: The rolling, averaged video bitrate for the last 1 second of transmission.
* Peak Bitrate: The highest recorded video bitrate for a single frame of video, rounded to the nearest Mbps, since the statistics were reset.

  **Note:** It is possible for the Peak Bitrate value to exceed the Bitrate (Mbps) control in the [AV I/O (NV-1-H-WE)](vstreamer_nv1wp_av_io.htm) component, as the Bitrate (Mbps) setting is a maximum average network video bitrate, not an absolute maximum.
* DSCP: The current QoS DSCP value being used for video packet transmission, as configured in the [Design Properties](design_properties.htm).
* Network Test: Click this button to initiate a test of the network's ability to losslessly carry video data from an Encoder to a Decoder (or, in the case of a multicast configuration, multiple Decoders).
  + When you click the button, the Encoder generates a green, pixelated test pattern that should be visible on the display connected to the Decoder. This test pattern causes the NV-1-H-WE to create an IP video stream that reaches and sustains the Bitrate (Mbps) setting of the [AV I/O (NV-1-H-WE)](vstreamer_nv1wp_av_io.htm) component.
  + While the test runs, observe the video statistics within the Network AV Sources > Video section. Lost packets, errors, and drops should be at or near 0.
  + If you do not see a test pattern, or you see a test pattern but the Decoder's video statistics indicate lost packets, errors, or drops, the network may not be configured properly or is otherwise unable to transport the desired video bitrate. Refer to the Q-SYS Networking > [Clocking, Audio, Video, & Control](../Networking/Clocking_Audio_Video_Control.htm) topic to learn about the requirements for Q-SYS Video.
  + Click the Network Test button again to end the test, which resumes the AV signal for the HDMI Input.

  **Note:** Do not initiate a Network Test while the system is in use. Running a Network Test disrupts the AV signals being transmitted between Encoder and Decoder, as well as local HDMI output from an Encoder. Any hotplug event (such as an HDMI device waking from sleep, or connecting or disconnecting its HDMI cable) will end the test. For long term testing, you should unplug all HDMI sources.

## Core Stream Details

This tab appears only when your design requires NV-1-H-WE audio to be processed by the Q-SYS Core. This information resets during a design restart on the Q-SYS Core or whenever you click Reset Details.

#### Input Details (Audio to Core)

If audio is being passed to the Q-SYS Core from the NV-1-H-WE, details for that audio appear here, such as when any of these component output audio pins are wired in the design:

* [AV I/O (NV-21-HU)](av_io.htm) â AV Audio pins
* [Generic AV Source](vst_hdmi_source.htm) â Breakaway Channel pins

#### Output Details (Audio from Core)

If audio is being passed from the Q-SYS Core to the NV-1-H-WE, details for that audio appear here, such as when any of these component input audio pins are wired in the design:

* [Generic HDMI Display](vst_hdmi_display.htm) â Breakaway Channel pins

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Core Networked Audio | | | | |
| Input Stream Details | (text) | | | Output |
| Output Stream Details | (text) | | | Output |
| Reset Details | 0  1 | false  true | 0  1 | Input / Output |
| Network | | | | |
| Clocking | | | | |
| Grandmaster Name | (text) | | | Output |
| Offset from Master | *n*us | | | Output |
| Parent Port Name | (text) | | | Output |
| LAN A | | | | |
| Active | 0  1 | false  true | 0  1 | Output |
| IP Address | (text) | | | Output |
| Mode | (text) | | | Output |
| PTP State | (text) | | | Output |
| Speed | (text) | | | Output |
| Networked Audio | | | | |
| AV Input 1 | | | | |
| Details | (text) | | | Output |
| Reset Details | 0  1 | false  true | 0  1 | Input / Output |
| Networked Video | | | | |
| AV Input 1 | | | | |
| Bitrate | *n* | *n* | - | Output |
| Drop Count | *n* | *n* | - | Output |
| DSCP | *n* | *n* | - | Output |
| Network Test | 0  1 | false  true | 0  1 | Input / Output |
| Payload Count | *n* | *n* | - | Output |
| Peak Bitrate | *n* | *n* | - | Output |
| Tx Count | *n* | *n* | - | Output |
| Chassis Temperature | *n.n* | *n.n*Â°C | - | Output |
| Fan 1 RPM | *n* | *n* | - | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| LED | (text) | | | Input / Output |
| Networked Video Reset Statistics | 0  1 | false  true | 0  1 | Input / Output |
| NV-1-H-WE Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| PoE = 30W, Class 4 | 0  1 | false  true | 0  1 | Output |
| Processor Temperature | *n*.*n* | *n*.*n*Â°C | - | Output |
