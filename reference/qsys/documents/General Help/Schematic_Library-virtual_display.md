# Q-SYS Connect: Virtual UC Controller

> Source: https://help.qsys.com/Content/Schematic_Library/virtual_display.htm

# Q-SYS Connect: Virtual UC Controller

The Virtual UC Controller is a Q-SYS Designer component that works in conjunction with Q-SYS Connect to integrate Windows-based room compute devices such as, Zoom Rooms into the Q-SYS ecosystem. It creates a virtual display on the compute, streams that display as a Mediacast video feed, and enables touch feedback from Q-SYS TSC-Gen 3 touchscreens. This allows Q-SYS touch controllers to function as native UC interfaces without additional hardware.

Q-SYS Connect is included in the Inventory, in version 10.2 to help you plan your system design today. Full download availability and support will roll out in an upcoming 10.2 hotfix, unlocking the complete Q-SYS Connect experience.

[Properties](javascript:void(0))

**Q-SYS Connect Properties**

#### Name

The Name may contain ASCII letters 'a' through 'z' (case-insensitive), the digits '0' through '9', and the hyphen. Names cannot begin or end with a hyphen. No other symbols, punctuation characters, or blank spaces are permitted.

#### Location

User-defined name that groups the component with other components in the same physical location, or in the same organizational scheme.

#### Is Network Redundant

Select whether the device is connected to redundant networks.

#### Is Required

When enabled, and the device is not found on the network, the device is reported as 'Missing', which is an error condition. This is the default behavior. When disabled, and the device is not found on the network, the device is reported as 'Not Present', which is not an error condition.

#### Display On Demand

Controls when the Virtual UC Controller creates a virtual display on the Zoom Rooms compute device and starts streaming it to Q‑SYS.

#### IP Streaming

Defines how the Q‑SYS Connect component handles its network transport and streaming behavior.

#### Maintain Primary Display

Determines whether the virtual display created by the Virtual UC Controller attempts to become the primary display on the Zoom Rooms compute device.

#### Room Type

Specifies the type of room system that Q‑SYS Connect will integrate with.

Zoom Room â Configures Q‑SYS Connect to work with Zoom Rooms. This enables the Virtual UC Controller sub‑component in the Inventory and allows a Q‑SYS TSC‑Gen 3 controller to act as a native Zoom Rooms controller via the virtual display and touchback.

**Graphic Properties**

#### Label

User-defined text that appears next to the component on the Schematic. Changing the label does not affect the component name or system behavior.

#### Position

Specifies the X and Y coordinates of the component on the Schematic. The values update automatically when you move the component, and can be edited to place the component at an exact location.

#### Fill

Sets the background color of the component block on the Schematic. This is for visual organization only and does not affect system operation.

[Controls](javascript:void(0))

### Virtual UC Controller Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

### Mediacast Stream

#### Identify

When pressed, shows an ID image with the discovery name on the virtual display.

#### Enable

When pressed, turns the virtual display, on / off.

#### Display Format

Sets the virtual display resolution and framerate.

#### Preview

A preview of the virtual display. Updates 1x / second.

[Control Pins](javascript:void(0))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Pin Name | Value | String | Position | Pins Available |
| Display Enabled | 0  1 | false  true | 0  1 | Input / Output |
| Display Format | Integer / index |  | 0 | Input / Output |
| Display Hotplug Request | 0  1 | false  true | 0  1 | Input / Output |
| Display Identity | 0  1 | false  true | 0  1 | Input / Output |
| Display Status | 0  1 |  | 0  1 | Output |
| Display Type | Numeric type | type string | 0 | Input / Output |
| Mediacast Bitrate (Mbps) | Numeric bit rate value | bit rate as text | 0 | Input / Output |
| Mediacast Format | Numeric / codec | numeric / codec |  | Input / Output |
| Mediacast I-Frame Request | 0  1 | false  true | 0  1 | Input / Output |
| Mediacast RTSP URL | N/A | full RTSP URL | 0 | Output |
