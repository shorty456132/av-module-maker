# Status (DCIO, DCIO-H)

> Source: https://help.qsys.com/Content/Schematic_Library/io_dcio_status.htm

# Status (DCIO, DCIO-H)

This topic covers both DCIO and DCIO-H Status component. Where differences exist, they are noted in the text.

The **DCIO and DCIO-H**, in the Q-SYS Designer **Inventory** list, represent physical pieces of equipment. the Status component provides an overall status of the hardware and software associated with the DCIO.

The physical DCIO is an Input / Output device. Audio inputs include AES3 Digital, HDMI, and analog. The output is analog audio. Automation outputs include a GPI, Relay outputs, and a RS-232 Serial interface.

For installation and operation of the DCIO hardware refer to the [User Manual](https://www.qsys.com/resource-files/productresources/dn/io_peripherals/dcio/q_dn_dcio_dcioh_usermanual.pdf).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

### DCIO Status

#### ID

When the ID / Identify button is pressed in one of the following:

* Q-SYS Designer Status component
* Configurator's Network Configuration for the hardware
* The physical hardware

The **ID** buttons in the Configurator and Status component flash, and the LCD screen on the hardware displays "ID *<name>*" to indicate the association between the three.

The indicators will flash for 5 minutes unless you stop them by pressing any one of the ID buttons.

#### Status LED

This LED changes color to indicate the current status of the DCIO. See Status for the meanings of the various colors.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### Details

You must select Verbose Yes in the Properties for this field to display.

Text indicating the Details of any errors occurring with the DCIO. The information in this field is updated regularly and is cumulative. None of the items listed below display unless there is a value associated with it. If there are values associated with these, call [Support](../Support.htm).

|  |  |
| --- | --- |
| fpga\_fifo\_error | sequence\_error |
| recv\_fifo\_error | xmit\_task\_early |
| xmit\_fifo\_error | xmit\_task\_late |
| recv\_dma\_error | xmit\_task\_error |
| xmit\_dma\_error | xmit\_overrun |
| sync\_error | clock\_sync\_loss |

#### Reset Details

You must select Verbose Yes in the Properties for this field to display.

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

To see both input and output Audio Streams information, you must have cards installed in the slots giving both inputs and outputs. For example, a Line Input card gives you Input Audio Streams, a Line Out card gives you Output Audio Streams.

#### Input OK

LED indicating the status of the Input Audio Stream for LAN A or LAN B.

#### Suppress button

If the "Is Network Redundant" property is set to 'Yes', but the redundant network is not connected, an error is displayed. This button suppresses the error caused by LAN B not being connected.

#### Input Details1

Text indicating the details of the status of the DCIO Input Audio Stream. The information in this field is updated regularly and is displayed as running totals. An item is displayed only when the value is not zero.

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

#### Output Details1

Text indicating the details of the status of the DCIO Output Audio Stream. The information in this field is updated regularly and is displayed as running totals. An item is displayed only when the value is not zero.

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

#### Reset Details

You must select Verbose Yes in the Properties for this field to display.

Click this button to reset the information in the Details field to zero.

#### 1Notes:

###### In Input and Output Audio Streams, accept\_count should be equivalent to the on\_time packets. This value is expected to be non-zero.

###### The units are 16 samples, so accept\_count should go up by 3000 per second.

###### too\_late indicates clock sync problems. If Clock Offset is larger than a single digit, check the QoS configuration on the switches for the clock traffic (the highest priority DSCP). If too\_late is not zero but the Clock Offset is zero or very small, check the QoS configuration on the switches for audio traffic (the second highest priority DSCP).

###### missing\_count could mean network problems such as bad cables, check the CRC error counters for the switches.

[Control Pins](javascript:void(0))

The **DCIO** in the **Inventory** list has no **Control Pins**. The available **Control Pins** for the **DCIO Status Component** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Clock Grandmaster Name | text field | | | Output |
| Clock Offset From Master | â | 0 ms to *n* ms | â | Output |
| Clock Parent Port Name | text field | | | Output |
| DCIO Status | text field | | | Output |
| Details | text field | | | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| LAN A Input Stream Details | text field | | | Output |
| LAN A Input Stream OK | 0  1 | false  true | 0  1 | Output |
| LAN A Output Stream Details | text field | | | Output |
| LAN A Output Stream OK | 0  1 | false  true | 0  1 | Output |
| LAN B Input Stream Details | text field | | | Output |
| LAN B Input Stream OK | 0  1 | false  true | 0  1 | Output |
| LAN B Output Stream Details | text field | | | Output |
| LAN B Output Stream OK | 0  1 | false  true | 0  1 | Output |
| LAN B Suppress | 0  1 | false  true | 0  1 | Input / Output |
| Reset Details | trigger | | | Input / Output |
| Temperature | *nn.n* | *nn.n*Â°C | 0 to 1.00 | Output |
