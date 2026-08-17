# Snapshot Bank

> Source: https://help.qsys.com/Content/Schematic_Library/snapshot_bank.htm

# Snapshot Bank

Snapshots allow you to save or store settings of selected controls in your design, and to recall the settings for different events or purposes. Snapshot Banks are where you select, or specify, the controls to be able to save their settings.

**Note:** Snapshot banks do not have controls or control pins. Refer to the [Snapshot Controller](snapshot_controller.htm) topic.

[Global Snapshot Bank](javascript:void(0))

The Global snapshot bank contains all of the read/write controls in your design. It consists of the Global snapshot bank and the Snapshot Controller Global component. You cannot add individual controls or components to the Global Snapshot Bank, unlike user-defined snapshot banks.

### Properties

Select the Global snapshot bank within the Snapshots pane or the Snapshot Controller Global component within the schematic to set the properties.

#### Snapshot Count

Sets the number of snapshots that can be saved and loaded globally â for all controls within the design â from 1 to 24 (default is 4).

### Global Snapshot Auto-save

The Global snapshot bank is automatically saved 30 seconds after a change to any read/write control in the design. (Read-only controls are excluded from the Global snapshot bank and therefore do not trigger an auto-save.)

The time stamp for the most recent save, as well as the amount of time it took to complete the last save, is indicated next to the Global snapshot bank in the Snapshots pane. For example: *Autosaved at 4:17:47 PM today (0.008s)*

**Note:** The  icon appears whenever a Global snapshot bank auto-save is in progress. The auto-save process can take several seconds in very large designs.

[User-defined Snapshot Banks](javascript:void(0))

The user-defined Snapshot Bank allows you to group the controls of one or more components, the settings of which can be saved in up to 24 different sets of values for each Snapshot Bank. These sets of values, or Snapshots, can be retrieved to set all the controls in the Snapshot Bank to the values saved in a Snapshot.

A Snapshot Bank consists of a Snapshot Controller, and all the controls and components you add to it.

### Adding User-defined Snapshot Banks

To add a new Snapshot bank without any controls:

1. From the left-side pane, click the Snapshots accordion bar.
2. Click .
3. Select Create new Snapshot Bank.

To add a new Snapshot bank from selected components or controls:

1. Select one or more components or controls from components.
2. Click .
3. Select Create new Snapshot Bank from selection.

### Properties

#### Name

User-defined name for the Snapshot Bank. The default is "Snapshot Bank *n*".

#### Snapshot Count

Sets the number of snapshots that can be saved and loaded in this Snapshot bank, from 1 to 24 (default is 8).

#### Mode

* Normal: (Default) All functions are enabled.
* Scene: Saves the current snapshot before loading a new one. Used primarily during a theater type rehearsal where the controls are set for the scene, then the snapshot is saved when the next snapshot is loaded.
* WriteProtect: Enables the Write Protect button in the Snapshot Controller control panel. The Save buttons for all the Snapshots in the Snapshot Bank are disabled so that settings cannot be overwritten.

### Adding Controls to Snapshot Banks

Only adjustable controls, and controls with values can be added to a Snapshot. You cannot, for example, add a meter or trigger type control to a Snapshot.

**Note:** Components and controls within Channel Groups are not supported in Snapshots.

There are two different ways to add controls to the Snapshot Bank: Add the entire component or add controls from the Control Panel.

#### Add the entire component

1. Select the component, in the Schematic, containing the controls you want to add.
2. Drag the entire component into the Snapshot Bank. As the cursor passes over the Snapshot Bank, the Bank is highlighted, and a plus sign (+) displays beside the cursor.
3. After the component has been placed in the Snapshot Bank, an icon displays in the list under the Snapshot Bank with the name of the component (for example, Delay (All Controls)).
4. All of the adjustable controls are now in the Snapshot Bank.

#### Add controls from the Control Panel

1. Double-click the component, in the Schematic, containing the controls you want to add. The Control Panel displays.
2. Press Ctrl+A to select everything, hold the Ctrl button and click multiple controls, or select one control, in the Control Panel. Objects that you select that are not adjustable controls, are not saved in the Snapshot Bank.
3. Drag the selected controls (all together) into the Snapshot Bank. As the cursor passes over the Snapshot Bank  *name*, in the **Snapshots** pane, the Snapshot Bank is highlighted, and a plus sign (+) and the message "Add selected controls and components to bank" display beside the cursor.
4. After the controls have been placed in the Snapshot Bank, an expandable icon displays in the list under the Snapshot Bank with the name of the component (for example, **Delay**).
5. Click the "twistie" to the left of the icon to expand it or collapse it. When expanded, a list of all the controls, from that component, in the Snapshot Bank, displays.

#### Tips

* The advantage of placing an entire component in a Snapshot Bank is that when you alter the Properties of the component, the Snapshot Bank responds to the changes. For example, if you increase the Count of a control, you now have the increased Count of that control in the Snapshot Bank. If you select all of the controls (see below) from the Control Panel of a component, and drag them into the Snapshot Bank, then increase the Count of a control, the new Count does not update the Snapshot Bank.
* The advantage of placing individual controls into a Snapshot Bank is that when you Load the Snapshot, only those controls are repositioned. Any other controls that have been manually positioned, or positioned by another Snapshot do not change. If all the controls are in a Snapshot Bank, when you Load one of the Snapshots, all the controls are positioned as they were Saved in that Snapshot.
* After you have added components or controls to a Snapshot Bank, you can select either the control or the component in the Snapshots pane, or the control in its control panel, and press Ctrl+F to open Context Finder and locate its counterpart.
* Generally speaking, all controls added to a Snapshot Bank are in all the Snapshots in that Bank. If a control's value is not in a Snapshot because the Snapshot was saved before the control was added to the Snapshot Bank, the control goes to its default value when the Snapshot is loaded.

[Troubleshooting](javascript:void(0)) 

### Using Snapshots with Text or Block Controller

When you drag an entire block controller or text controller component into a snapshot and then save settings to that snapshot, the snapshot retains the state of all controls, including the code. If you load the snapshot later, it updates all the controls, including the "code" control. This implies that if any modifications were made to the code between saving and loading the snapshot, those code changes will not be preserved.
