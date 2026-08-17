# Status/Control (DAB-801)

> Source: https://help.qsys.com/Content/Schematic_Library/amplifier_redundancy_panel.htm

# Status/Control (DAB-801)

The DAB-801 DataPort Amplifier Backup extends Q-SYS redundancy capability to include designated QSC power **amplifiers** and **I/O Frames** populated with Q-SYS **DataPort cards**.

The DAB-801 provides N+1 amplifier redundancy for QSC 2 and 4-channel DataPort amplifiers, and supports I/O Frame redundancy. Two DAB-801s can be stacked to provide double the primary amplifier redundancy.

* A single DAB-801 supports four 2-channel primary amplifiers with one 2-channel backup amplifier, or two 4-channel primary amplifiers with one 4-channel backup amplifier.
* A pair of DAB-801s support eight 2-channel primary amplifiers with one 2-channel backup amplifier, or four 4-channel primary amplifiers with one 4-channel backup amplifier.

**Note:** The DAB-801 does not support 8-channel amplifiers.

The DAB-801 is a physical piece of hardware represented by a virtual Component in the Inventory list of Q-SYS Designer. This topic covers the virtual Component.

**Note:** Read the [DataPort Amplifier Backup Panel](../Hardware/Accessories/017_DataPort_Amplifier_Backup_Panel.htm) topic and the [DAB-801 User Manual](../Hardware/Hardware_Overview.htm) for information about the capabilities and functionality of the hardware.

[Inputs and Outputs](javascript:void(0)) 

### Input Pins

Amplifier signal pins are represented by a left-pointing () triangle, and the wiring is represented by a thin orange line. There are four DataPort connectors on a single DAB-801. Each DataPort connector carries two amplifier channels. You can have four 2-channel amplifiers, or two 4-channel amplifiers connected to a single DAB-801. With an extension DAB-801, you can have eight 2-channel amplifiers or four 4-channel amplifiers. The backup amplifier must be the same channel count (2- or 4-channel) as all the primary amplifiers.

### Output Pins

Amplifier signal pins are represented by a left-pointing () triangle, and the wiring is represented by a thin orange line. There are four DataPort connectors on a single DAB-801. Each DataPort connector carries two amplifier channels. You can have four 2-channel amplifiers, or two 4-channel amplifiers connected to a single DAB-801. With an extension DAB-801, you can have eight 2-channel amplifiers or four 4-channel amplifiers. The backup amplifier must be the same channel count (2- or 4-channel) as all the primary amplifiers.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### DAB-801 Properties

#### Amplifier Channel Count

You can have either 2- or 4-channel amplifiers connected to the DAB-801. You cannot have both connected to the same DAB-801.
This property selects the channel count of the amplifiers.

#### Dual

Specifies if you have a single DAB-801, or two connected together.

#### Mute on Alarm

Specifies if you want the **I/O Frame** to mute its output to the DAB-801 when a signal is detected from either the **Alarm** or **Page** analog inputs to the DAB-801. This applies to all channels. The DAB-801 hardware disconnects the channels designated by the **Alarm/Page** switch from the main inputs, and connects them to the **Alarm** or **Page** inputs, so regardless of this setting, the **Alarm/Page** overrides the selected channels.

[Controls](javascript:void(0))

#### Status LED

This LED changes color to indicate the current status. See Status for the meanings of the various colors.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### Panel Power Good

LED indicating the status of the **DAB-801 Panel power**.

#### Backup Amp Power Good

LED indicating the status of the **Backup Amplifier** connected to the DAB-801.

#### Backup Amp Engaged

LED indicating that the **Backup Amplifier** is in use, or engaged - one of the primary amplifiers has failed.

#### Alarm / Page Active

LED indicating that the **Alarm** or **Page** mode is active. When the **Alarm** or **Page** mode is active, regular input to the amplifiers (per hardware settings) is suspended, and there is direct input to the amplifiers from either the alarm system or page system. **Alarm** takes precedence over **Page**.

#### Automatic Mode

When this button is engaged, you are not able to manually engage the Backup Amplifier. This should be on for normal operation. When an amplifier fails, the Backup is automatically switched in.

#### Reset

Pressing this button resets the DAB-801 back to the Primary Amplifiers.

#### DataPort

Label indicating the DataPort connector, on the DAB-801, associated with the information directly below. There are four DataPort connectors (A - D) on a single DAB-801, and four more (A - D) on the Extension Panel.

#### Channel

Label indicating the channels associated with the DataPort connector on the DAB-801, as labeled directly above.

#### Amplifier Status

LED indicating the status of the associated amplifier.

#### Backup Engaged

LED indicating if the Backup Amplifier is Engaged for a specific DataPort (2-channel amp) or DataPorts (4-channel amplifier).

#### Manual Backup Engaged

Toggle button allowing you to manually switch a single DataPort for 2-channel, or two DataPorts for a 4-channel to the Backup Amplifier. When this button is pressed, the Backup Engaged LED (for the associated DataPort(s)) and the Backup Amp Engaged LED (for the Backup Amplifier) are On/Red.

This is a radio-style button allowing only one button on at a time.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Amplifier Status  DataPort A Channel 1,2 | 0 1 2 | bad (red) good (green) wait (yellow) | 0 0.5 1 | Output |
| Amplifier Status  DataPort B Channel 3,4 | 0 1 2 | bad (red) good (green) wait (yellow) | 0 0.5 1 | Output |
| Amplifier Status  DataPort C Channel 5,6 | 0 1 2 | bad (red) good (green) wait (yellow) | 0 0.5 1 | Output |
| Amplifier Status  DataPort D Channel 7,8 | 0 1 2 | bad (red) good (green) wait (yellow) | 0 0.5 1 | Output |
| Backup Engaged  DataPort A Channel 1,2 | 0  1 | false  true | 0  1 | Output |
| Backup Engaged  DataPort B Channel 3,4 | 0  1 | false  true | 0  1 | Output |
| Backup Engaged  DataPort C Channel 5,6 | 0  1 | false  true | 0  1 | Output |
| Backup Engaged  DataPort D Channel 7,8 | 0  1 | false  true | 0  1 | Output |
| Manual Backup Engage  DataPort A Channel 1,2 | 0  1 | false  true | 0  1 | Output |
| Manual Backup Engage  DataPort B Channel 3,4 | 0  1 | false  true | 0  1 | Output |
| Manual Backup EngageDataPort C Channel 5,6 | 0  1 | false  true | 0  1 | Output |
| Manual Backup Engage  DataPort D Channel 7,8 | 0  1 | false  true | 0  1 | Output |
| Alarm/Page Active | 0  1 | false  true | 0  1 | Output |
| Automatic Mode | 0  1 | false  true | 0  1 | Input / Output |
| Backup Amplifier Engaged | 0  1 | false  true | 0  1 | Output |
| Backup Amplifier Power Good | 0  1 | false  true | 0  1 | Output |
| Panel Power Good | 0  1 | false  true | 0  1 | Output |
| Reset | trigger | | | Input / Output |
| Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1 When the Property "Dual" is set to Yes, each of these has another set of Control Pins labeled with "Extension Panel" followed by the DataPort and channel information. | | | | |
