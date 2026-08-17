# Status/Control (UCI Viewer)

> Source: https://help.qsys.com/Content/Schematic_Library/uci_viewer.htm

# Status/Control (UCI Viewer)

The UCI Viewer component allows you to control various aspects and see the status of a UCI when a UCI Viewer client is associated with the UCI.

To use the UCI Viewer Status/Control component:

1. Create a UCI by [Adding a UCI to the Design](uci_customization.htm#Adding_a_UCI)
2. From the Inventory Peripherals, place a UCI Viewer Status/Control component into your Inventory.
3. Drag the UCI Viewer Status/Control component into the Schematic.
4. Set the Properties as required. See the Properties table below.
5. Open a [UCI Viewer](uci_viewer_app.htm) client.
6. Select **UCI Viewers** (top left over the list of UCIs) Note: you can still run the UCI from the list of UCIs, but the UCI Viewer Status/Control component will be inactive.
7. Select the UCI Viewer (Status/Control component) you wish to use.
8. The Status field of the selected UCI Viewer turns to OK (Green).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### UCI Assignment

The choices are Static, only the specified UCI is used, and Dynamic you can select the UCI when the UCI is running.

#### UCI

This field displays only when the UCI Assignment is set to Static. Use the pull-down list to select the UCI assigned to this UCI Viewer component.

[Controls](javascript:void(0))

#### Status LED

This LED changes color to indicate the current status of the Core. See Status for the meanings of the various colors.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### Log Off

If a user is required to log on to the UCI, this button can log them off.

#### UCI

Displays the name of the UCI currently running on the UCI Viewer. You can change the currently running UCI if the **UCI Assignment** is set to Dynamic.

#### Page

Displays the name of the currently selected page in the UCI. You can click this field and change the viewed page.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Current Page | Text Field | | | Input/Output |
| Current UCI | Text Field | | | Output |
| Log Off | Trigger | | | Input/Output |
| Status | N / A | Status information | 0.00 = Good  1.00 = Error | Output |
