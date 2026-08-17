# Status (I/O-Core 110f)

> Source: https://help.qsys.com/Content/Schematic_Library/io_core_110f_status.htm

# Status (I/O-Core 110f)

A Q-SYS Core 110f is capable of operating simply as a peripheral I/O device. In this mode, you add the I/O-Core 110f from the Inventory, and then configure a separate Q-SYS Core processor to run your design. In Peripheral Mode, you can configure the same Mic/Line, Flex, POTS, GPIO, Serial Port, Loudspeaker Monitor, and HID components as Core Mode.

**Note:** USB routing via the USB Input and USB Output components is not supported in Peripheral Mode for the Core 110f. HID Keyboard, HID Media, and HID Conferencing are supported.

[Switching Modes](javascript:void(0))

Use Q-SYS Core Manager to switch a Q-SYS Core 110f to I/O-Core 110f mode. For more information, see [Utilities](../Core_Manager/Core_Management/Utilities.htm) in the Core Manager Help.

**Note:** After switching to I/O-Core 110f mode, use Q-SYS Configurator (within Q-SYS Designer Software) to discover and configure the device within the I/O Devices category. Selecting the I/O-Core 110f opens [Peripheral Manager](../Peripheral_Manager/PeripheralManager_Overview.htm), which you can also use to change the mode back to Core 110f mode.

[Properties](javascript:void(0))

### I/O Core 110f Properties

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

#### ID

Click to display the ID indicator on the I/O-Core 110f front panel, as well as flash an indicator in Q-SYS Configurator next to the associated I/O-Core 110f . The front panel shows the ID indicator for 5 minutes unless you press the ID button again.

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

The current temperature, in Celsius, of the I/O-Core 110f processor.

#### Chassis Temp.

The current temperature, in Celsius, of the I/O-Core 110f chassis.

#### Chassis Fan

Indicates the current RPMs of the I/O-Core 110f chassis fan.

#### Details

This section only appears when the Verbose property is set to 'Yes', and displays any error conditions. Contact [Support](../Support.htm) if you see any errors reported here. Click Reset Details to clear the information.

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

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Chassis Fan RPM | *n* | *n* | - | Output |
| Chassis Temperature | *n*.*n* | *n*.*n*Â°C | - | Output |
| Clock Grandmaster Name | (text) | | | Output |
| Clock Offset From Master | - | *n*us | - | Output |
| Clock Parent Port Name | (text) | | | Output |
| Details | (text) | | | Output |
| I/O-Core 110f Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Processor Temperature | *n*.*n* | *n*.*n*Â°C | - | Output |
| Reset Details | 0  1 | false  true | 0  1 | Input / Output |
