# Status (AVB)

> Source: https://help.qsys.com/Content/Schematic_Library/io_avb_card_status_core.htm

# Status (AVB)

The AVB Card Status component provides information about the condition of both the [AVB In component](io_avb_input_card.htm), and the [AVB Output component](io_avb_output_card.htm).

For hardware information, see [CAN32 â AVB Audio Video Bridge Card](../Hardware/IO_Expanders/CAN32.htm).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

There are no properties associated with the AVB Status component.

[Controls](javascript:void(0))

### Status

#### Status LED

This LED changes color to indicate the current status of the I/O-22 Output. See Status for the meanings of the various colors.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

### AVB Interface

#### Link LED

Indicates if there is a working connection to an AVB unit.

#### Full Duplex LED

Indicates if the link is communicating in both directions.

#### Speed

Up to 100Mbps maximum.

#### MAC Address

MAC address of the AVB card. Automatically populated.

#### Clock Source

Read / Write. The source of the clock signal.

Internal: The clock comes from the AVB card. This is not the Q-SYS clock.

AVB Input Stream *<n>*: The clock is derived from the Input Stream.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| AVB Clock Source | N / A | Text | N / A | Input / Output |
| Current MAC Address | N / A | Text | N / A | Output |
| Primary Full Duplex LED | 1  2 | Present  Not Present | 0  1 | Output |
| Primary Link LED | 1  2 | Present  Not Present | 0  1 | Output |
| Primary Speed | 0 - 100 | <n> Mbps | 0 - 1 | Output |
| Status | N / A | Text | N / A | Output |
