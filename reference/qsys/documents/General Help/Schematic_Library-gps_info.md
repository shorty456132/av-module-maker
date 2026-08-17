# GPS Info

> Source: https://help.qsys.com/Content/Schematic_Library/gps_info.htm

# GPS Info

The GPS Info component displays various information received from connected GPS receiver hardware. Most often this hardware is used in conjunction with the [Loop Player](loop_player.htm) to synchronize audio playback between systems. This information is transmitted to the Core over RS-232 in NMEA 0183 format.

**Note:** All information may not be available depending on the features and configuration of the specific GPS hardware.

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### GPS Info Properties

*This component has no configurable properties*.

[Controls](javascript:void(0))

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### UTC

Displays current UTC time in HH;MM;SS format.

#### Date

Displays the current UTC date. Reads as **Day**, **Month**, **Year**.

#### Latitude

Latitude read by GPS in the form of 37Â° 41' 22.68" N.

#### Longitude

Longitude read by GPS. In the form 106Â° 55' 22.30" W.

#### Speed

Speed read by GPS.

#### Course

Course read by GPS.

#### Satellite Count

Current number of satellites GPS is locked to.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Course | **Float** (text) | | | Input / Output |
| Day | **Integer** (text) | | | Input / Output |
| Latitude | **String**: nÂ° n' n.nn" N|S | | | Output |
| Longitude | **String**: nÂ° n' n.nn" W|E | | | Output |
| Month | **Integer** (text) | | | Input / Output |
| Satellite Count | **Integer** (text) | | | Input / Output |
| Speed | **Float** (text) | | | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| UTC | **Time Control** (text) | | | Input / Output |
| Year | **Integer** (20XX - i.e. 23 for 2023) | | | Input / Output |
