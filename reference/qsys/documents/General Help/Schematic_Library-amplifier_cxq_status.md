# Status (CX-Q, CXD-Q, DPA-Q Series)

> Source: https://help.qsys.com/Content/Schematic_Library/amplifier_cxq_status.htm

# Status (CX-Q, CXD-Q, DPA-Q Series)

This topic covers the Status component for the CX-Q, CXD-Q, and DPA-Q network amplifiers.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### CX-Q, CXD-Q, and DPA-Q Amplifier Properties

#### Is Network Redundant

Selecting Yes allows a device to maintain network connectivity even if one network path fails. If a network problem occurs, the secondary network takes over automatically.

#### Channel Configuration

Select the configuration needed for your venue.

**Note:** Eight-channel models have two sets of four channels for configuration.

* 4 Channel, A B C D
* 3 Channel, A+B Bridged
* 2 Channel, A+B Bridged C+D Bridged
* 3 Channel, AB Parallel
* 2 Channel, AB Parallel C+D Bridged
* 2 Channel, A B Parallel C D Parallel
* 1 Channel, A B Parallel Bridged with CD Parallel
* 2 Channel, A B C Parallel
* 1 Channel, A B C D Parallel

Channel configurations are as follows:

* Space between letters (A B C D) = single channels,
* "+" between letters (A+B) = bridged,
* no space between letters (ABCD) = parallel.

When you make your selection, then run the design, the configuration is made available to the amplifier. Follow the instructions on the amplifier display.

#### Standalone Mode

**Off** â Turns Standalone Mode off.

**One-to-one** â Each audio input is routed to its corresponding output Ch1 â Output A, Ch2 â Output B, Ch3 â Output C, Ch4 â Output D.

**One-to-all** â Input Channel 1 is routed to all outputs.

**Note:** See the [Standalone section](#Standalone_Mode) below for details.

[Controls](javascript:void(0))

The controls for the **Amplifier Status** component, listed below, are divided into sections to match the Control Panel sections.

### Amplifier Status

#### ID

When the ID/Identify button, in Status component, the Configurator's Network Configuration,or on the physical hardware is pressed, the **ID** buttons in all three places blink to easily identify hardware with the software.

The indicators will flash for 5 minutes unless you stop them by pressing any one of the buttons.

#### Status LED

This LED changes color to indicate the current status of the amplifier. See Status for the meanings of the various colors.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### Temperature

Indicates the current power supply unit (PSU) temperature in Centigrade.

#### Details

You must set Verbose in the unit's Properties to "Yes" in order to see this field.

Text indicating the Details of any errors occurring with the amplifier. The information in this field is updated regularly and is cumulative. An item is displayed only when the value is not zero. If there are values associated with these, call [Support](../Support.htm).

|  |  |
| --- | --- |
| fpga\_fifo\_error | sequence\_error |
| recv\_fifo\_error | xmit\_task\_early |
| xmit\_fifo\_error | xmit\_task\_late |
| recv\_dma\_error | xmit\_task\_error |
| xmit\_dma\_error | xmit\_overrun |
| sync\_error | clock\_sync\_loss |

#### Reset Details

Click this button to reset the information in the Details field to zero.

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

To see both input and output Audio Streams information, you must have audio passing both directions.

#### Input OK

LED indicating the status of the Input Audio Stream for LAN A or LAN B.

#### Suppress button

If the "Is Network Redundant" property is set to 'Yes', but the redundant network is not connected, an error is displayed. This button suppresses the error caused by LAN B not being connected.

#### Input Details

Text indicating the details of the status of the amplifier Input Audio Stream for LAN A and LAN B. The information in this field is updated regularly and is displayed as running totals. An item is displayed only when the value is not zero. [1](#Notes)

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

Text indicating the details of the status of the amplifier Output Audio Stream for LAN A and LAN B. The information in this field is updated regularly and is displayed as running totals. An item is displayed only when the value is not zero. [1](#Notes)

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

###### 1. Notes:

###### In Input and Output Audio Streams, accept\_count should be equivalent to the on\_time packets. This value is expected to be non-zero.

###### The units are 16 samples, so accept\_count should go up by 3000 per second.

###### too\_late indicates clock sync problems. If Clock Offset is larger than a single digit, check the QoS configuration on the switches for the clock traffic (the highest priority DSCP). If too\_late is not zero but the Clock Offset is zero or very small, check the QoS configuration on the switches for audio traffic (the second highest priority DSCP).

###### missing\_count could mean network problems such as bad cables, check the CRC error counters for the switches.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Clock Grandmaster Name | Text field - Name of the Clock Grandmaster | | |  |
| Clock Offset From Master | â | 0 ms to *n* ms | â | Output |
| Clock Parent Port Name | Text field - Name of the Parent Port | | | Output |
| Amplifier Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
| Details | Text field - Details of the current amp status. | | | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| LAN A (or B) Input Stream Details | Text Field | | |  |
| LAN (or B) Input Stream OK | 0  1 | false  true | 0  1 | Output |
| LAN (or B) Output Stream Details | Text Field | | |  |
| LAN (or B) Output Stream OK | 0  1 | false  true | 0  1 | Output |
| Reset Details | trigger | | | Input / Output |

[Standalone Mode](javascript:void(0))

Standalone Mode provides the capability to connect the inputs of an amplifier to the outputs when connection to the Core is lost. In addition you can boot the amplifier without a connection to the Core.

Two ways to engage the Standalone Mode. For either way you must enable the Standalone Mode in the Q-SYS Designer Properties for the amplifier.

1. Amplifier Loses Network Connection to the Core:
   1. When connection to the Core is lost, audio is interrupted, and the amplifier counts down the number of seconds (15-60) specified in the amplifier's Properties in the Q-SYS design.
   2. After the timeout period, the inputs of the amplifier are sent directly to the outputs either one-to-one (each input goes to its corresponding output), or one-to-all (one input goes to all the outputs). While in Standalone mode, the front panel display of the amplifier displays OK in the Status field.
   3. When the connection to the Core is restored, the original audio streams are restored. There will be a short drop in audio while the amplifier is re-initialized.
2. Boot the Amplifier Without a Connection to the Core
   1. The amplifier waits 10 seconds to determine if the connection to the Core can be made.
   2. The amplifier then launches the last design run if it had the Standalone Mode enabled. During this time, the amplifier front-panel Status field displays OK, and the Design field displays "Stand-alone".
   3. When the amplifier re-connects to the Core, the Core pushes the design to the amplifier and the original audio is restored. There is a short loss of audio while the amplifier is initialized.

**Note:** Standalone Mode is not supported by CXD-Qn, CX-Qn, and DPA-Qn series amplifiers. Qn series amplifiers only support network connectivity and do not have line inputs.
