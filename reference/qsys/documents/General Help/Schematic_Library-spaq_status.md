# Status (SPA-Qf Series)

> Source: https://help.qsys.com/Content/Schematic_Library/spaq_status.htm

# Status (SPA-Qf Series)

This topic covers the Status component for SPA-Qf Series network amplifiers.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### SPA-Qf Amplifier Properties

#### Verbose

Available only when the Status component is selected in the Schematic.

Displays the Networking and Audio Stream details for LAN A.

#### Model

Select the SPA-Qf Series hardware model from the drop-down list.

#### Channel Configuration

Select the configuration needed for your venue. Available selections depend on the SPA-Qf Series model.

**Note:** The selected configuration is made available to the amplifier when you run the design. Follow the instructions on the amplifier display.

| Configuration[1](#A) | No. of Channels | Bridging |
| --- | --- | --- |
| A B | 2 Channel |  |
| A+B | 1 Channel | A B Bridged |
| A B C D | 4 Channel |  |
| A+B C D | 3 Channel | A B Bridged |
| A+B C+D | 2 Channel | A B Bridged, C D Bridged |

###### 1. A space between letters = single channels. A "+" between letters = bridged channels. Channels C and D only available on the SPA-Qf 60x4.

#### Standalone Mode

**Off** â Turns Standalone Mode off.

**One-to-all** â Input Channel 1 is routed to all outputs.

**Note:** See the [Standalone Mode](#Standalone_SPAQ) below for details.

[Controls](javascript:void(0))

### Amplifier Status

#### ID

Press the ID button to flash the SPA-Qf device's front panel LEDs for 5 minutes or until you press the button again.

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

You must set Verbose to "Yes" in the unit's Properties to see this field.

Text indicates the details of any errors occurring with the amplifier. The information in this field is updated regularly and is cumulative. An item is displayed only when the value is not zero. If there are values associated with these, call [Support](../Support.htm).

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

LED indicating the status of the Input Audio Stream for LAN A.

#### Input Details

You must set Verbose to "Yes" in the unit's Properties to see this field.

Text indicates the details of the status of the amplifier Input Audio Stream for LAN A. The information in this field is updated regularly and is displayed as running totals. An item is displayed only when the value is not zero.[1](#Notes)

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

LED indicating the status of the Output Audio Stream for LAN A.

#### Output Details

You must set Verbose to "Yes" in the unit's Properties to see this field.

Text indicates the details of the status of the amplifier Output Audio Stream for LAN A. The information in this field is updated regularly and is displayed as running totals. An item is displayed only when the value is not zero.[1](#Notes)

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

### CPU Status

This section is only available when the Verbose property is set to "Yes".

#### CPU System Status

Normally, this should be OK. If you see Compromised, it means that the % usage for CPU, RAM, or Disk has been high for a long period of time. Note that the Compromised state for CPU System Status will not affect the audio path.

#### CPU %

Indicates the percentage of consumed CPU resources.

#### RAM %

Indicates the percentage of consumed RAM resources.

#### Disk %

Indicates the percentage of consumed storage space â for log files, license files, etc.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Amplifier Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | â | Output |
| Clock Grandmaster Name | (text) | | | Output |
| Clock Offset From Master | â | 0 ms to *n* ms | â | Output |
| Clock Parent Port Name | (text) | | | Output |
| CPU System Status | â | OK  Compromised | â | Output |
| CPU Usage (%) | 0-100 | 0 to 100% | 0.0 to 1.00 | Output |
| Details | (text) | | | Output |
| Disk Usage (%) | 0-100 | 0 to 100% | 0.0 to 1.00 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| LAN A Input Stream Details | (text) | | | Output |
| LAN A Input Stream OK | 0  1 | false  true | 0  1 | Output |
| LAN A Output Stream Details | (text) | | | Output |
| LAN A Output Stream OK | 0  1 | false  true | 0  1 | Output |
| RAM Usage (%) | 0-100 | 0 to 100% | 0.0 to 1.00 | Output |
| Reset Details | (trigger) | | | Input / Output |
| Temperature | *n*.*n* | *n*.*n*Â°C | - | Output |

[Standalone Mode](javascript:void(0))

Standalone Mode provides the capability to connect the inputs of an amplifier to the outputs when connection to the Core is lost. In addition you can boot the amplifier without a connection to the Core.

Two ways to engage the Standalone Mode. For either way you must enable the **Standalone Mode** in the Q-SYS Designer Properties for the amplifier.

1. Amplifier Loses Network Connection to the Core:
   1. When connection to the Core is lost, audio is interrupted, and the amplifier counts down the number of seconds (15-60) specified in the amplifier's Properties in the Q-SYS design.
   2. After the timeout period, the inputs of the amplifier are sent directly to the outputs.
   3. When the connection to the Core is restored, the original audio streams are restored. There will be a short drop in audio while the amplifier is re-initialized.
2. Boot the Amplifier Without a Connection to the Core
   1. The amplifier waits 10 seconds to determine if the connection to the Core can be made.
   2. The amplifier then launches the last design run if it had the Standalone Mode enabled.
   3. When the amplifier re-connects to the Core, the Core pushes the design to the amplifier and the original audio is restored. There is a short loss of audio while the amplifier is initialized.
