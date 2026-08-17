# Page Station

> Source: https://help.qsys.com/Content/Schematic_Library/page_station_hardware.htm

# Page Station

The Page Station component is a proxy for the physical Page Station. You must add one Page Station component from the Inventory Peripherals list, to your Q-SYS design **Inventory** for each physical Page Station in your system. The Page Station component is comprised of five sub-components: [Status](page_station_hardware_status.htm), [Mic/Control](page_station_hardware_mic_control.htm), [Aux Mic](page_station_hardware_aux_mic.htm), [Aux Line Out](page_station_hardware_aux_out.htm), and GPIO. Once you add a Page Station to your Inventory, you can drag all the sub-components into the design by clicking directly on the title "Page Station", and dragging it into the Schematic. You can drag individual components into the design by selecting the component, and dragging it into the design.

In order to create a functioning Public Address system, you must have at least one Page Station, and a PA Router in your design.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Is Network Redundant

Selecting Yes allows a device to maintain network connectivity even if one network path fails. If a network problem occurs, the secondary network takes over automatically.

#### Verbose

Adds CPU Statistics Audio to the Status component, along with a Reset button to reset the statistics to zero. You must have the Status component in the schematic area, and selected.

#### Model

Selects the Model of the Page Station. Initially, you choose the model when you place the Page Station into the Inventory. You can change it here if needed.

#### Enable Expander

Enables the Page Station to support the use of the Page Station Expander (PS-X ). The PS-X allows you to connect a Q-SYS handheld microphone that can be mounted in the same general area as the Page Station. For example, the Page Station is mounted on the airline gate desk, whereas the PS-X is mounted at the gate itself.

When the Expander is enabled, the Aux Mic, and GPIO components are no longer available.

[Controls](javascript:void(0))

#### ID

Click to display the ID indicator on the Page Station front panel, as well as flash an indicator in Q-SYS Configurator next to the associated Page Station. The front panel shows the ID indicator for 5 minutes unless you press the ID button again.

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

The current temperature, in Celsius, of the Page Station processor.

#### Details

This section only appears when the Verbose property is set to 'Yes', and displays any error conditions. Contact [Support](../Support.htm) if you see any errors reported here. Click Reset Details to clear the information.

### Power

#### PoE A/Aux

This LED glows if the Page Station is connected to a switch port that supports Power over Ethernet.

#### PoE B

This LED glows if the Page Station is connected to a switch port that supports Power over Ethernet.

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

#### LAN A

This LED changes color to indicate the current status of the I/O USB Bridge. See Status for the meanings of the various colors.

#### Input/Ouput Details

Must have Verbose in the Page Station Property set to Yes.

Details concerning the audio input to the Page Station.

* connected
* dscp
* accept\_count
* drop\_count
* discontinuity\_count
* on\_time
* too\_late

#### Ouput OK

Must have Verbose in the Page Station Property set to Yes. This LED changes color to indicate the current status of the I/O USB Bridge. See Status for the meanings of the various colors.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Clock Grandmaster Name | (text) | | | Output |
| Clock Offset From Master | - | *n*us | - | Output |
| Clock Parent Port Name | (text) | | | Output |
| Details | (text) | | | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| LAN A Input Stream Details | (text) | | | Output |
| LAN A Input Stream OK | 0  1 | false  true | 0  1 | Input / Output |
| also available for PS-1650 | | | | |
| LAN IP Address | (text) | | | Output |
| LAN Mode |  |  |  | Output |
| LAN Port Active | 0  1 | false  true | 0  1 | Output |
| LAN PTP State | (text) | | | Output |
| LAN Speed | (text) | | | Output |
| Page Station Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| PoE A Active | 0  1 | false  true | 0  1 | Output |
| PoE B Active | 0  1 | false  true | 0  1 | Output |
| Reset Details | 0  1 | false  true | 0  1 | Input / Output |
| Temperature | *n.n* | *n.n*Â°C | - | Output |
