# Status (NL Series, NM Series, QIO Series)

> Source: https://help.qsys.com/Content/Schematic_Library/qio_24f_status.htm

# Status (NL Series, NM Series, QIO Series)

The Status component for the NL Series network loudspeakers, NM Series beamforming microphones, and QIO Series network expanders provides health information about these devices, including overall status, network information, detected power, and audio stream health (as applicable).

**Note:** For an overview of the NL Series, NM Series, and QIO Series peripherals, see the [Q-SYS Products](../Hardware/Hardware_Overview.htm) topic.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### NL, NM, and QIO Properties

#### RJ45 LED Disable

(NM and NL Series only) Select whether the yellow (activity) and green (link speed) LAN jack status LEDs are illuminated on the underside of the NM-T1. The default is No (not disabled).

#### PoE+ Enable

(NL Series only) Determines whether the loudspeaker advertises itself on the network as a PoE+ capable device, which affects how the loudspeaker uses the PoE power budget of the connected power supply. The default is 'No' (disabled).

* If set to 'Yes' and the loudspeaker is connected to a PoE+ Type 2 Class 4 capable power supply, the output is boosted and the Power > PoE+ control turns green.
* If set to 'Yes' and the loudspeaker is not connected to a PoE+ Type 2 Class 4 capable power supply, the Power > PoE+ control is off and the Power > PoE control turns green.
* If set to 'Yes' but the connected power supply fails to allocate full PoE+ power to the loudspeaker, the Status changes to Compromised.

#### Verbose

When set to 'Yes', a Details section appears in the control panel that displays device statistics and any errors, along with a Reset button to reset the statistics to zero.

#### Amplifier Disabled

(QIO-FLEX4A only). Enables deactivation of the amplifier functionality of the device, preventing audio amplification or output. Default is No.

#### Channel Index

(NL Series, QIO-ML2x2, QIO-ML4i, and QIO-L4o only). Select how control indexes are determined for each Custom Voicing component in your design. Choices are 4 to 16,384.

* Auto: (Default) Components in existing designs upgraded to Q-SYS v9.2.0 and later will continue to use a 0-based index. New components use a 1-based index, which matches the functionality of other Q-SYS components.
* 0-Based: The component will use a 0-based index, meaning that control indexing starts at 0. This is useful for maintaining consistency with other components and for re-using control scripts.
* 1-Based: The component will use a 1-based index, meaning that control indexing starts at 1. This matches the functionality of other Q-SYS components.

#### Control ID

(NM Series, NL Series, QIO-ML2x2, QIO-ML4i, and QIO-L4o only).

You can choose between *Auto*, *Legacy*, and *Standard*.

[Controls](javascript:void(0))

### Status

#### Status ID

Click to flash the Status LED (yellow) under the NL Series loudspeaker grille, the LED Light Ring (yellow) on an NM Series microphone, or the ID LED (green) on the front of the QIO Series peripheral. The indicator flashes indefinitely until you press the ID button again.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### Processor Temp

The current temperature, in Celsius, of the peripheral's central processing unit.

#### Details

This section only appears when the Verbose property is set to 'Yes', and displays device statistics and any error conditions. Click Reset Details to clear the information.

#### Reset Details

This section only appears when the Verbose property is set to 'Yes'. Click this button to reset the information in the Details field.

#### Chassis Temp

For QIO Series Audio I/O Expanders only (with exception to AES8x8 and QIO-TEL2), this is the current temperature, in Celsius, of the device chassis.

#### Chassis Fan

For QIO Series Audio I/O Expanders only (with exception to AES8x8 and QIO-TEL2), this indicates the current RPMs of the device chassis fan.

### Audio Streams

**Note:** This section appears only for NL and NM Series peripherals.

To see both input and output Audio Stream information, you must have a device that provides both inputs and outputs. For example, a Line Input component provides Input Audio Stream(s), and a Line Out component provides Output Audio Stream(s).

#### Input OK

LED indicating the status of the Input Audio Stream for LAN [POE].

#### Input Details

Text indicating the details of the status of the Input Audio Stream. The information in this field is updated regularly and is displayed as running totals. An item is displayed only when the value is not zero.

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

LED indicating the status of the Output Audio Stream for LAN [POE].

#### Output Details

Text indicating the details of the status of the Output Audio Stream. The information in this field is updated regularly and is displayed as running totals. An item is displayed only when the value is not zero.

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

### Power

The controls shown in this section depend on the connected device. Not applicable to NM Series microphones.

[NL Series](javascript:void(0))

**Note:** See the [PoE+ Enable](#PoE+) property description for more information.

#### PoE

Glows green if the loudspeaker is not connected to a PoE+ Type 2 Class 4 capable power supply.

#### PoE+

Glows green if the loudspeaker is connected to a PoE+ Type 2 Class 4 capable power supply.

[QIO Series](javascript:void(0))

#### PoE Active

Glows green when the device is connected to a PoE power supply.

#### PoE Active+

(For QIO-FLEX4A and QIO-LVR4 only). Glows green when the device is connected to a PoE Type 2 power supply.

#### DC Power

Glows green when the device is connected to a DC power supply.

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

#### Link THRU

(Available only on QIO Control I/O devices). Indicates the status of the connection at the LAN [THRU] port.

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

[Control Pins](javascript:void(0))

**Note:** Available control pins depend on the specific peripheral model.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Chassis Fan RPM | *n* | *n* | - | Output |
| Chassis Temperature | *n*.*n* | *n*.*n*Â°C | - | Output |
| Clock Grandmaster Name | (text) | | | Output |
| Clock Offset From Master | - | *n*us | - | Output |
| Clock Parent Port Name | (text) | | | Output |
| Disable RJ45 LED | 0  1 | false  true | 0  1 | Input / Output |
| DC Power Active | 0  1 | false  true | 0  1 | Output |
| Details | (text) | | | Output |
| Disable RJ45 LED | 0  1 | false  true | 0  1 | Input / Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| NL-[model] Status  NM-[model] Status  QIO-[model] Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Output OK | 0  1 | false  true | 0  1 | Output |
| PoE+ Status | 0  1 | false  true | 0  1 | Output |
| PoE Active | 0  1 | false  true | 0  1 | Output |
| Processor Temperature | *n*.*n* | *n*.*n*Â°C | - | Output |
| Reset Details | 0  1 | false  true | 0  1 | Input / Output |
