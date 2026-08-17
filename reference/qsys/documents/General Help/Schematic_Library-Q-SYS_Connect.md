# Q-SYS Connect

> Source: https://help.qsys.com/Content/Schematic_Library/Q-SYS_Connect.htm

# Q-SYS Connect

Q-SYS Connect is a software solution that enables seamless integration of Q-SYS TSC‑101‑G3 touch screen controllers as native Zoom Room controllers and other supported UC meeting room platforms running on Windows-based room compute devices. Q-SYS Connect runs on the room compute and exposes the UC room controller as a Mediacast video and touch stream to Q-SYS Designer.

The following properties describes the Q-SYS Connect Status component and defines how it identifies the room compute, exposes its audio I/O and processing features, and publishes status and control surfaces, including Mic In and Control components, to the rest of the Q-SYS design. Use the following tables to see which setting affect device discovery and pairing, how audio pathsânear-end, far-end, TruVoiceLift, analogâare presented and gain-structured, and which controls and control pins you can target from UIs, automation, or external systems for monitoring and logic.

Q-SYS Connect is included in the Inventory, in version 10.2 to help you plan your system design today. Full download availability and support will roll out in an upcoming 10.2 hotfix, unlocking the complete Q-SYS Connect experience.

[Properties](javascript:void(0))

#### Name

The Name may contain ASCII letters 'a' through 'z' (case-insensitive), the digits '0' through '9', and the hyphen. Names cannot begin or end with a hyphen. No other symbols, punctuation characters, or blank spaces are permitted.

#### Location

User-defined name that groups the component with other components in the same physical location, or in the same organizational scheme.

#### Is Network Redundant

Select whether the device is connected to redundant networks.

#### Is Required

When enabled, and the device is not found on the network, the device is reported as 'Missing', which is an error condition. This is the default behavior. When disabled, and the device is not found on the network, the device is reported as 'Not Present', which is not an error condition.

#### Verbose

Enables additional diagnostic information in its Status component.

#### Room Type

Identifies the unified communications platform and room profile running on the Windows compute device that hosts Q-SYS Connect.

#### Enable UCI Control

Turns on or off the âSecond Page Experienceâ / UCI integration for the selected Room Type.

#### UCI Assignment

Defines how a UCI is associated with the UC app, when Enable UCI Control is set to Yes.

#### UCI

Specifies which UCI from the design is presented on the UC platformâs controller interface when UCI integration is enabled.

[Control](javascript:void(0))

### Q-SYS Connect Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

### Room System Info

#### Discovery Name

Read-only field that displays the discovery name advertised by the Q-SYS Connect TaskBar App on the Windows compute device, for Room Manager use. This value matches the componentâs Name property in the design.

#### Room Type

Read-only field that displays the detected room system type for this device, for example, Zoom Room. Intended for Room Manager use. This value matches the Room Type property configured for the device.

#### Monitors Active (LED)

LED indicator that is lit when the Windows compute device is awake and its monitors are active. The LED is unlit when the compute is asleep or its monitors are inactive.Use this to confirm that the room system UI should be visible on the virtual display.

#### Wake-up

LED indicator that indicates the state of the wake-up input pin on the Status component. When the pin is asserted, the LED lights show that an external control signal is requesting the compute to wake up

[Control Pins](javascript:void(0))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Pin Name | Value | String | Position | Pins Available |
| Wake-up | 0  1 | false  true | 0  1 | Input |
| Current Discovery Name | N/A | Current discovery name shown by the Q-SYS Connect TaskBar app. | 0 | Input / Output |
| Current Page | 0 | Name of the currently selected page of the assigned UCI. | 0 | Output |
| Current Room Type | N/A | Current room type reported by the compute. | 0 | Output |
| Current UCI | 0 | Name of the UCI currently assigned to the room system control app. | 0 | Output |
| Display Active | 0  1 | false  true | 0  1 | Output |
| Display Off | 0  1 | false  true | 0  1 | Output |
| Display On | 0  1 | false  true | 0  1 | Output |
| Hide UCI | 0  1 | false  true | 0  1 | Input / Output |
| IP Address | Read-only | IP address or host of the Zoom Room compute discovered by Q-SYS Connect. | 0 | Output |
| Q-SYS Connect Status | 0  1 | 0  1 | 0  1 | Output |
| Remote Status | 0  1 | false  true | 0  1 | Output |
| Show UCI | 0  1 | false  true | 0  1 | Input / Output |
| UCI Visible | 0  1 | false  true | 0  1 | Output |
