# Status (Page Station)

> Source: https://help.qsys.com/Content/Schematic_Library/page_station_hardware_status.htm

# Status (Page Station)

The Page Station Status component provides status information for the physical Page Station, including clock, temperature, network communications, and other information.

[Inputs and Outputs](javascript:void(0)) 

#### Inputs

*The Page Station Status component has no inputs.*

#### Outputs

*The Page Station Status component has no outputs.*

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Page Station Properties

#### Verbose

Displays the Networking and Audio Stream details for LAN A (and LAN B, if applicable to the device). You must have Is Network Redundant set to Yes to see LAN B details.

#### Model

Selects the Model of the Page Station. Initially, you choose the model when you place the Page Station into the Inventory. You can change it here if needed.

#### Enable Expander

Enables the Page Station to support the use of the Page Station Expander (PS-X ). The PS-X allows you to connect a Q-SYS handheld microphone that can be mounted in the same general area as the Page Station. For example, the Page Station is mounted on the airline gate desk, whereas the PS-X is mounted at the gate itself.

When the Expander is enabled, the Aux Mic, and GPIO components are no longer available.

[Controls](javascript:void(0))

### Page Station Status

#### Status LED

This LED changes color to indicate the current status of the Page Station. See Page Station Status for the meanings of the various colors.

#### Page Station Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### Clock Offset

This text field displays the clock difference between the Page Station and the **Master Clock**. The unit of measure is indicated in the text readout.

#### Grandmaster

Displays either the Q-SYS Core processor name or the PTP Clock GUID. Note that:

* There can only be one Grandmaster for a Q-SYS design (for all LAN interfaces of the device). It is possible for Q-SYS to resolve to a PTP Grandmaster present on LAN B, if enabled and present.
* If available, the Core Name is displayed instead of the raw PTP clock GUID. (The Core Name is not available in some clocking topologies â for example, when a higher priority boundary clock between systems is present or with some Software Dante configurations, as when the Core syncs indirectly to another device via Software Danteâs boundary clock.)
* A PTP Clock GUID can look similar to a MAC address, but is not the same and may not be related to a deviceâs actual MAC address.
* If the PTP Clock GUID is derived from a MAC address (whether a Q-SYS Core processor or third-party device), it can be any MAC address on that device (any LAN interface, including those without a network connection).

#### Temperature

Text field indicating the current temperature inside the Page Station, measured in Celsius. Typically about 60Â° C.

#### ID

The ID button is used to identify the associated Q-SYS Designer Page Station Status component, and the Page Station's Network Configuration screen in Q-SYS Configurator.

When you click this button the ID buttons associated with this Page Station flash. The buttons will flash for five minutes unless you click one of the buttons to turn it off.

#### Parent Port

The clock Parent Port is the device and interface name to which the Core is syncing. Typically, this is the Grandmaster.

#### Details

Text indicating the Details of the status of the Page Station. The information in this field is updated regularly and is cumulative. The following information is displayed as running totals:

|  |  |
| --- | --- |
| fpga\_fifo\_error | xmit\_dma\_busy |
| recv\_fifo\_error | card\_clock\_error |
| xmit\_fifo\_error | sequence\_error |
| recv\_dma\_error | VCXO\_clock\_sync\_loss |
| xmit\_dma\_error | NIC\_clock\_sync\_loss |
| recv\_dma\_error | floating\_point\_NAN |
| recv\_dma\_busy |  |

#### Reset Details

Click this button to reset the information in the **Details** field to zero.

### Power

#### POE A/Aux

LED indicating if the PoE on LAN A is active or not, or if the auxiliary power supply is connected and active or not.

#### POE B

LED indicating if the PoE on LAN B is active or not. You must have I

### Audio Streams

To see both LAN A and LAN B information you must have Network Redundant set to Yes in the Properties.

To see the Input and Output Details for LAN A/B, you must have Verbose set to Yes in the Properties.

#### Input OK

LED indicating the status of the Input Audio Stream for LAN A or LAN B.

#### Input Details

Text indicating the details of the status of the Page Station Input Audio Stream. The information in this field is updated regularly. The following information is displayed as running totals:

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

Text indicating the details of the status of the Page Station Output Audio Stream. The information in this field is updated regularly. The following information is displayed as running totals:

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

#### Suppress

Toggle button that suppresses the input of the associated component. When the Suppress button is on, and the status of the suppressed input changes, the Suppress button automatically turns off (un-suppresses), and the status of that item can be displayed

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

### General

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Clock Offset From Master | â | 0 ms to *n* ms | â | Output |
| Details | Text Field | | |  |
| LAN A/B Input Stream Details [1](#LAN_B),[2](#Details) | Text Field | | | Output |
| LAN A/B Input Stream OK [1](#LAN_B) | 0  1 | false  true | 0  1 | Output |
| LAN A/B Output Stream Details [1](#LAN_B), [2](#Details) | Text Field | | | Output |
| LAN A/B Output Stream OK [1](#LAN_B) | 0  1 | false  true | 0  1 | Output |
| Page Station Status[2](#Details) | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
| POE A/Aux Active | 0  1 | false  true | 0  1 | Output |
| POE B Active | 0  1 | false  true | 0  1 | Output |
| Reset Details | trigger | | | Input / Output |
| Temperature | *nn.n* | *nn.n*Â°C | 0 to 1.00 | Output |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1. LAN B information available only if Is Network Redundant is set to Yes in the Properties2. LAN A/B and Page Station Status Details available only if Verbose is set to Yes in the Properties. | | | | |
