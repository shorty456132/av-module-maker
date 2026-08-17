# Snapshot Controller

> Source: https://help.qsys.com/Content/Schematic_Library/snapshot_controller.htm

# Snapshot Controller

The Snapshot Controller is the Component part of the Snapshot Bank. The Snapshot Controller is placed in the Schematic, and contains the Control Panel with all the Controls necessary for using and maintaining Snapshots.

This topic covers both Global and user-defined Snapshot Controllers.

[Using the Snapshot Controller](javascript:void(0))

After you have placed all the controls and/or components you want to control into the [Snapshot Bank](snapshot_bank.htm):

1. Drag the Snapshot Controller component into the schematic and open the Control Panel.
2. Set all the controls in all the components, that are in the Snapshot Bank, to the settings you want.
3. Click the Save button of the Snapshot in which you want to save the current control settings.
4. Adjust all controls to settings for another situation.
5. Click the Save button of the Snapshot in which you want to save the new control settings.
6. Continue saving control settings in Snapshots as necessary. If you need more than 24 Snapshots, you can add more Snapshot Banks to cover your needs.

After you have saved all the control settings, click the Load button of the Snapshot that meets the needs of your venue at this time.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

The properties for the Snapshot Controller can be set while the Snapshot Controller component in the Schematic is selected, or when the [Snapshot Bank](snapshot_bank.htm) in the Snapshot list is selected.

### Global Bank Properties

#### Snapshot Count

Sets the number of snapshots that can be saved and loaded in this Snapshot bank, from 1 to 24 (default is 4).

### User-defined Snapshot Bank Properties

#### Name

User-defined name for the Snapshot Bank. The default is "Snapshot Bank *n*".

#### Snapshot Count

Sets the number of snapshots that can be saved and loaded in this Snapshot bank, from 1 to 24 (default is 8).

#### Mode

* Normal: (Default) All functions are enabled.
* Scene: Saves the current snapshot before loading a new one. Used primarily during a theater type rehearsal where the controls are set for the scene, then the snapshot is saved when the next snapshot is loaded.
* WriteProtect: Enables the Write Protect button in the Snapshot Controller control panel. The Save buttons for all the Snapshots in the Snapshot Bank are disabled so that settings cannot be overwritten.

#### Is JSON

**Note:** In Q-SYS Designer version 9.10.x, there is a feature labeled Is JSON under the snapshot properties. However, it is advisable to refrain from utilizing this feature in the current version.

[Controls](javascript:void(0))

#### Load

One button for each Snapshot that loads the control settings saved in the associated Snapshot.

* When a Snapshot is not loaded, the associated button is dark green. (Control pin value = 0, position = 0)
* When a Snapshot is last-loaded but one or more controls contained in the Snapshot has been changed, the button is dimmed green. (Control pin value = 1, position = .5)
* When a Snapshot is last-loaded and all its controls match the saved Snapshot configuration, the button is bright green. (Control pin value = 2, position = 1)

#### Save

One button for each Snapshot that saves the current state of the Controls in the Snapshot Bank in the associated Snapshot.

#### Prev

Loads the Snapshot to the left of the one currently loaded. When the last Snapshot on the left is selected, the Prev button is grayed out.

#### Next

Loads the Snapshot to the right of the one currently loaded. When the last Snapshot on the right is selected, the Next button is grayed out.

#### Ramp Time

Not available in the Global Snapshot. Sets the time it takes for the controls to reach the saved position or value, from 0 to 60 seconds (default is 0). If there are binary type controls (buttons, list selections, etc.) in the Snapshot, they change state at 50% of the Ramp Time.

**Note:** Some components will not be recalled by a Snapshot if the Ramp Time is set to a non-zero number. For more information, please see [Using Components with Snapshot Controller Ramp Time](#Using).

#### Write Protect

Not available in the Global Snapshot. Available when Write Protect or Scene mode is selected in the Properties. Disables or enables the Save buttons for all Snapshots.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Last[1](#1) | | | | |
| 1-*n* | 0  1 | false  true | 0  1 | Output |
| Load[2](#2) | | | | |
| 1-*n* | 0  1  2 | 0  1  2 | 0  .5  1 | Input / Output |
| Match[3](#3) | | | | |
| 1-*n* | 0  1 | false  true | 0  1 | Output |
| Save | | | | |
| 1-*n* | trigger | | | Input / Output |
| Load Next | trigger | | | Input / Output |
| Load Previous | trigger | | | Input / Output |
| Ramp Time | 0 to 60000 | 0 ms to 60 sec | 0.000  1.000 | Input / Output |
| Write Protect (only for user-defined) | 0  1 | disable  enable | 0  1 | Input / Output |

1. "Last" pins indicate the last snapshot that was selected.

2. See the [Controls](#Controls) section for value definitions.

3. "Match" pins indicate when current values match saved snapshot values. Can match with multiple snapshots depending on the values.

[Troubleshooting](javascript:void(0))

### Using Components with Snapshot Controller Ramp Time

Components such as the [Crossover Component](crossover.htm) or other [Text Controller](device_controller_script.htm) or [Custom Controls](custom_controls.htm) like the Integer Knobs, and Hexadecimal Knobs will not be recalled by Snapshot if the Ramp Time is a non-zero number.

### Using Snapshots with Text or Block Controller

When you drag an entire block controller or text controller component into a snapshot and then save settings to that snapshot, the snapshot retains the state of all controls, including the code. If you load the snapshot later, it updates all the controls, including the "code" control. This implies that if any modifications were made to the code between saving and loading the snapshot, those code changes will not be preserved.

### Reverse Action not applied to Load buttons in Snapshot Controller

The Reverse Action for the Load buttons in the Snapshot Controller operates similarly to a trigger. This means the action is initiated when the button is pressed.
