# Assets

> Source: https://help.qsys.com/Content/Reflect/Assets.htm

# Assets

The Assets page provides a consolidated list of all devices (assets) within a selected Organization. You can easily view at-a-glance status, names, and categories of devices, as well as their associated Domains, Systems, locations, and, optionally, the details for each device.

**Tip:** The Assets table does not automatically update when a device status changes. Click Refresh to update the table.

## Viewing Assets

From the Assets drop-down menu at the top-left corner of the window, select an Organization. The table lists each device within the Organization, including its Status, Name, Type, associated Domain, System, and Location. (To see a list of possible statuses and types, refer to the [Status](Status.htm) page.)

[Show and Adjust Columns](javascript:void(0))

* Click the Columns menu to select more parameters, including model, manufacturer, serial number (if available), firmware, associated Q-SYS design name, whether the asset requires a Reflect license, date & time configuration (if applicable), and network information.

  **Note:** The Serial Number field is supported by Q-SYS Core processors and Q-SYS peripherals. Early production Cores and all third-party devices will indicate "Unavailable".
* Click the Show menu to select how many assets to show per page â 100, 200, 400 (default), or 800.

**Tip:** To change the order in which columns appear, click and drag a column name within the Columns menu.

[View Asset Details in JSON Format](javascript:void(0))

Click the + button to view all the details for a device in JSON format.

* Click Copy to copy the JSON information to the clipboard.
* Click Export JSON to save the JSON details in a .json file. The file is saved to the Downloads folder on your computer with a filename format of asset-*assetname*.json.

## Filtering Assets

By default, you can filter assets by Status, Type, and Name. For simplicity, only the statuses and types as applicable to assets in the table are available for filter selection. Click + Add Filter to create additional filtering parameters by Name, Model, Manufacturer, Firmware, Domain, System, Location, and Design.

## Exporting the Assets List

You can easily export the entire table of assets to a CSV file. Click Export as CSV to save an assets.csv file to your computer's Downloads folder. The file will contain data for each column you have selected from the Columns menu.
