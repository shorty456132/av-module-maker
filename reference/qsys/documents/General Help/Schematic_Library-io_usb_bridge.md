# Status (I/O USB  Bridge)

> Source: https://help.qsys.com/Content/Schematic_Library/io_usb_bridge.htm

# Status (I/O USB Bridge)

The I/O USB Bridge is a Q-SYS peripheral that converts Camera and Audio IP streams to USB. In the peripheral Properties, enable the [USB Video Bridge](usb_uvc.htm) and [USB Audio Bridge](USB_Audio_Bridge.htm) to expose components for this capability.

**Note:** Audio Bridges allow you to use the volume controls on a Mac that is running 10.12.6 or higher and has the IO USB Audio Bridge selected.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### I/O USB Bridge

#### External USB Audio

When enabled, you can connect an external audio device to the USB input and route audio to and from that device. See [External USB Audio Device In and Out](alsa_receiver_sound_card.htm).

#### Verbose

When set to Yes, the Control Panel displays Audio Stream Input and Output Statistics along with a Reset button to reset the statistics to zero.

**Note:** This field displays only when you have the I/O USB Status component in the design and selected.
All other Properties are the same whether you have the USB Video Bridge or the I/O USB Bridge Status component selected.

[Controls](javascript:void(0))

### I/O USB Bridge Status

#### ID

When the ID/Identify button, in the Q-SYS Designer Status component, or the Configurator's Network Configuration for the hardware, or on the physical hardware is pressed, the **ID** buttons in the Configurator and Status component flash, and the LCD on the physical Hardware flashes to indicate the association between the three.

The indicators will flash for 5 minutes unless you stop them by pressing any one of the buttons.

#### Status LED

This LED changes color to indicate the current status of the Core. See Status for the meanings of the various colors.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

### Network

#### Clock Master

LED indicating if the Core is the Master Clock for the Q-SYS system or not. The Core can be the Master Clock even if the clock is synchronized to an external clock.

#### Grandmaster

Displays either the Q-SYS Core processor name or the PTP Clock GUID. Note that:

* There can only be one Grandmaster for a Q-SYS design (for all LAN interfaces of the device). It is possible for Q-SYS to resolve to a PTP Grandmaster present on LAN B, if enabled and present.
* If available, the Core Name is displayed instead of the raw PTP clock GUID. (The Core Name is not available in some clocking topologies â for example, when a higher priority boundary clock between systems is present or with some Software Dante configurations, as when the Core syncs indirectly to another device via Software Danteâs boundary clock.)
* A PTP Clock GUID can look similar to a MAC address, but is not the same and may not be related to a deviceâs actual MAC address.
* If the PTP Clock GUID is derived from a MAC address (whether a Q-SYS Core processor or third-party device), it can be any MAC address on that device (any LAN interface, including those without a network connection).

#### PTPv1 (Dante)

Used specifically for Dante audio networking integration within the Q-SYS ecosystem

#### Clock Offset

Indicates how much of an offset exists, in microseconds, between the device and the network Grandmaster.

#### Parent Port

The clock Parent Port is the device and interface name to which the device is syncing. Typically, this is the Grandmaster.

#### LAN A and/or B

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

#### Input / Output OK LED (LAN A / LAN B)

You must have "Is Network Redundant" set to Yes in the Properties to see LAN B.

This LED changes color to indicate the current status of the I/O USB Bridge. See Status for the meanings of the various colors.

#### Suppress button

If the "Is Network Redundant" property is set to 'Yes', but the redundant network is not connected, an error is displayed. This button suppresses the error caused by LAN B not being connected.

#### Reset Details

The following details are available:

connected=1 (=1 connected / =0 not connected)

dscp=34 (Differentiated services code point) You can change this number in the Design Properties dialog (Menu > File > [Design Properties](design_properties.htm)).

accept\_count= (number of packets accepted)

### USB Reset

#### USB Reset

*(Only available on the Core 110f, Core Nano, NV-32-H Core and Peripheral Mode, NV-21-HU, Core 8 Flex, and TSC-G3 Touch Panels)* This reinitializes the USB driver without the need for a full design redeploy, restoring connections and USB functionality after a few seconds.

[Control Pins](javascript:void(0))

[I/O USB Bridge Status](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Clock Grandmaster Name | Text box indicating the network name of the Network Clock Grandmaster | | | Output |
| Clock Offset From Master | â | 0 ms to *n* ms | â | Output |
| Clock Parent Port Name | Text box indicating the network name of the Parent port, usually the same as the Clock Grandmaster with the LAN appended. | | | Output |
| I/O USB Bridge Status | Text field displaying the current status of the I/O USB Bridge | | | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |

[Audio Streams](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| LAN A (LAN B) Input Stream Details | Read-only text field listing details about the Input audio streams. | | | Output |
| LAN A (LAN B) Input Stream OK | 0  1 | false  true | 0.00  1.00 | Output |
| LAN A (LAN B) Output Stream Details | Read-only text field listing details about the Output audio streams. | | | Output |
| LAN A (LAN B) Output Stream OK | 0  1 | false  true | 0.00  1.00 | Output |
| LAN B Suppress button | 0  1 | false  true | 0.00  1.00 | Output |

[USB Audio](javascript:void(0))

The following control pins are available on the Speakerphone In and Out, Sound Card In and Out components.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Active | 0  1 | Off  On | 0  1 | Output |
| Reset Counters | Trigger button | | | Input / Output |
| SRC- | 0 and up | 0 and up | 0.00 to 1.00 | Output |
| SRC+ | 0 and up | 0 and up | 0.00 to 1.00 | Output |
| Total Samples | 0 and up | 0 and up | 0.00 to 1.00 | Output |
| USB Connected | 0  1 | Off  On | 0  1 | Output |
| USB Speed | Text Field | | | Output |

[Video Status](javascript:void(0))

The following control pins are available when the Status component or the USB Video Bridge component is selected.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| IP Streams 1 and 2 | | | | |
| Bitrate | 0.0000 and up | 0.0000 and up | 0.00 to 1.00 | Output |
| FPS | 0 to 30 | 0 to 30 | 0.00 to 1.00 | Output |
| Frame Count | 0 and up | 0 and up | 0.00 to 1.00 | Output |
| Packet Count | 0 and up | 0 and up | 0.00 to 1.00 | Output |
| Packet Loss Percentage | 0.00 to 100 | 0.00% to 100% | 0.00 to 1.00 | Output |
| Packets Lost | 0 and up | 0 and up | 0.00 to 1.00 | Output |
| Test Stream 1, 2 | 0  1 | false  true | 0  1.00 | Input / Output |
| USB | | | | |
| Active | 0  1 | false  true | 0  1.00 | Output |
| Bitrate | 0.0000 and up | 0 and up | 0.00 to 1.00 | Output |
| Bridge Name | (text) | | | Output |
| Encoding | (text) | | | Output |
| FPS | 0 to 30 | 0 to 30 | 0.00 to 1.00 | Output |
| SRC- | 0 and up | 0 and up | 0.00 to 1.00 | Output |
| SRC+ | 0 and up | 0 and up | 0.00 to 1.00 | Output |
| USB Speed | (text) | | | Output |
| Video Format | (text) | | | Output |
| Input Active | 0  1 | false  true | 0  1.00 | Output |
| Input Connection | (text) | | | Output |
| Reset | 0  1 | 0 or false  1 or true | 0.00  1.00 | Input / Output |
