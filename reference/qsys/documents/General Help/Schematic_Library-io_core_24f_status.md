# Status (I/O-Core 24f)

> Source: https://help.qsys.com/Content/Schematic_Library/io_core_24f_status.htm

# Status (I/O-Core 24f)

A Q-SYS I/O-Core 24f is capable of operating simply as a peripheral I/O device. In this mode, you add the I/O-Core 24f from the Inventory, and then configure a separate Q-SYS Core processor to run your design. In Peripheral Mode, you can configure the same Mic/Line, Flex, GPIO, Serial Port, Loudspeaker Monitor, and HID components as Core Mode.

[Properties](javascript:void(0))

### I/O Core 24f Properties

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

### I/O-Core 24f Status

#### ID

Click to display the ID indicator on the I/O-Core 24f front panel, as well as flash an indicator in Q-SYS Configurator next to the associated I/O-Core 24f . The front panel shows the ID indicator for 5 minutes unless you press the ID button again.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### Processor Temp.

The current temperature, in Celsius, of the I/O-Core 24f processor.

#### Chassis Temp.

The current temperature, in Celsius, of the I/O-Core 24f chassis.

#### Chassis Fan

Indicates the current RPMs of the I/O-Core 24f chassis fan.

#### Details

This section only appears when the Verbose property is set to 'Yes', and displays any error conditions. Contact [Support](../Support.htm) if you see any errors reported here. Click Reset Details to clear the information.

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

### LAN A and/or B

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

### Audio Streams

#### Suppress button

If the "Is Network Redundant" property is set to 'Yes', but the redundant network is not connected, an error is displayed. This button suppresses the error caused by LAN B not being connected.

#### Input / Output OK LED (LAN A / LAN B)

You must have "Is Network Redundant" set to Yes in the Properties to see LAN B.

This LED changes color to indicate the current status of the I/O USB Bridge. See Status for the meanings of the various colors.

#### Input Details

Text indicating the details of the status of the I/O Frame Input Audio Stream. The information in this field is updated regularly and is displayed as running totals. An item is displayed only when the value is not zero.

|  |
| --- |
| id |
| connected |
| dscp |
| accept\_count |
| drop\_count |
| missing\_count |
| duplicate\_count |
| on\_time |
| too\_late |
| pt\_mismatch |
| size\_mismatch |

#### Output OK

LED indicating the status of the Output Audio Stream for LAN A or LAN B.

#### Output Details

Text indicating the details of the status of the I/O Frame Input Audio Stream. The information in this field is updated regularly and is displayed as running totals. An item is displayed only when the value is not zero.

|  |
| --- |
| id |
| connected |
| dscp |
| accept\_count |
| drop\_count |
| missing\_count |
| duplicate\_count |
| on\_time |
| too\_late |
| pt\_mismatch |
| size\_mismatch |

1 Notes:

###### In Input and Output Audio Streams, accept\_count should be equivalent to the on\_time packets. This value is expected to be non-zero.

###### The units are 16 samples, so accept\_count should go up by 3000 per second.

###### too\_late indicates clock sync problems. If Clock Offset is larger than a single digit, check the QoS configuration on the switches for the clock traffic (the highest priority DSCP). If too\_late is not zero but the Clock Offset is zero or very small, check the QoS configuration on the switches for audio traffic (the second highest priority DSCP).

###### missing\_count could mean network problems such as bad cables, check the CRC error counters for the switches.

#### Reset Details

The following details are available:

connected=1 (=1 connected / =0 not connected)

dscp=34 (Differentiated services code point) You can change this number in the Design Properties dialog (Menu > File > [Design Properties](design_properties.htm)).

accept\_count= (number of packets accepted)

### Video

These controls are only shown when the USB Video Bridge component of the I/O-Core 24f is dragged into the schematic.

### Input

#### Input LED

Indicates whether or not there is active input to the Q-SYS video input device.

#### Input Connection

The network name of the Q-SYS video input device.

#### Bitrate (Kb/s)

The current input video bitrate, in kilobits per second.

#### Frames per Sec

Number of frames per second being sent by the video device.

#### Frame Count

Total number of frames sent.

#### Packet Count

Total number of packets since the last reset.

#### Packets Lost

Number of packets lost since the last reset.

#### Packet Loss%

The percentage of packets lost based on Packets Lost and Packet Count.

#### Test Button

Test the network setup for the Q-SYS video streaming implementation without having a PC or any USB connection. This tests QoS and IGMP on multicast.

### USB

#### USB Active LED

Video Bridge USB Active: Indicates if the USB is active or not.

#### USB Bridge Name

The network name of the Q-SYS video bridging device.

#### Video Format

Displays the format of the video present on the USB â for example, "1920x1080p30".

#### Encoding

Displays the type of encoding used for the USB video stream - for example, "MJPEG".

#### USB Speed

Displays the detected USB speed capability of the connection â for example, "High Speed (2.0)".

#### Bitrate (Mb/s)

USB bitrate, in megabits per second.

#### Frames per Sec

USB frames per second

#### SRC-

The number of samples removed in order to match the USB clock with the Q-SYS PTP clock

#### SRC+

The number of samples added in order to match the USB clock with the Q-SYS PTP clock

### Reset

#### Reset Button

Clears the readings, and restarts monitoring.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Network | | | | |
| Clocking | | | | |
| Grandmaster Name | (text) | | | Output |
| Offset From Master | - | *n*us | - | Output |
| Parent Port Name | (text) | | | Output |
| LAN A / B |  |  |  |  |
| Active | 0  1 | false  true | 0  1 | Output |
| IP Address | (text) | | | Output |
| Mode | (text) | | | Output |
| PTP State | (text) | | | Output |
| Speed | (text) | | | Output |
| Video Bridge | | | | |
| IP Stream 1 | | | | |
| Bitrate | n.n | n.n | - | Output |
| FPS | n | n | - | Output |
| Frame Count | n | n | - | Output |
| Packet Count | n | n | - | Output |
| Packet Loss Percentage | n.n | n.n | - | Output |
| Packet Lost | n | n | - | Output |
| Test Stream 1 | 0  1 | false  true | 0  1 | Input / Output |
| USB | | | | |
| Input Active | 0  1 | false  true | 0  1 | Output |
| Input Connection | (text) | | | Output |
| Reset | (trigger) | | | Input / Output |
| Chassis Fan RPM | *n* | *n* | - | Output |
| Chassis Temperature | *n*.*n* | *n*.*n*Â°C | - | Output |
| Details | (text) | | | Output |
| I/O-Core 24f Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| LAN A Input Stream Details | (text) | | | Output |
| LAN A Input Stream OK | 0  1 | false  true | 0  1 | Output |
| LAN A Output Stream Details | (text) | | | Output |
| LAN A Output Stream OK | 0  1 | false  true | 0  1 | Output |
| LAN B Input Stream Details | (text) | | | Output |
| LAN B Input Stream OK | 0  1 | false  true | 0  1 | Output |
| LAN B Output Stream Details | (text) | | | Output |
| LAN B Output Stream OK | 0  1 | false  true | 0  1 | Output |
| LAN B Suppress | 0  1 | false  true | 0  1 | Input / Output |
| Processor Temperature | *n*.*n* | *n*.*n*Â°C | - | Output |
| Reset Details | 0  1 | false  true | 0  1 | Input / Output |
