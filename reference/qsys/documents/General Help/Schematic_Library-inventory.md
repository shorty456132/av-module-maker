# Inventory

> Source: https://help.qsys.com/Content/Schematic_Library/inventory.htm

# Inventory

The Inventory section, in the left-side pane, displays a list of hardware items to use in your system. In a new design, the Inventory list is populated with only a Q-SYS Core processor. You must add the other items that match your physical inventory. Each inventory item contains at least one component that can be placed into the schematic, configured, and connected to other components as needed.

[Add Single Item to the Inventory](javascript:void(0))

1. Click the plus ( + ) icon in the Inventory accordion bar.
2. Select the tab for the equipment type you want to add.
3. Click the item to add to the Inventory.

For configuration details, refer to the item's individual help topic (select item and press F1).

[Batch-Add Items to the Inventory](javascript:void(0))

1. Click the plus ( + ) icon in the Inventory accordion bar.
2. Select the tab for the equipment type you want to add.
3. Hold Ctrl while selecting the item to add to your Inventory.
4. From the Quantity field, enter the number of items to add.
5. Click Add.

**Note:** When naming your item, use only letters (a-z), numbers (0-9) or hyphens (-).

### Handling Auto-Increment and Base Name Suffixes

#### Generating Sequential Names with a Suffix

Scenario: You want to create multiple QIO-L4o devices with sequentially numbered names, such as QIO-L4o-1, QIO-L4o-2, QIO-L4o-3, QIO-L4o-4.

Configuration Steps

* In the Base Name field, enter:

`QIO-L4o-${padding=1;start=1;increment=1}`

* In the Quantity field, set the number of devices you want (e.g., 4).

Result

This will generate :

* QIO-L4o-1
* QIO-L4o-2
* QIO-L4o-3
* QIO-L4o-4

#### Generating Names without a Suffix

Scenario: You want to generate a base name without any suffix (just QIO-L4o). All generated names will automatically include a numeric suffix (e.g., -1). To remove the suffix, you will need to edit the names manually after creation.

Configuration Steps

* In the Base Name field, enter:

`QIO-L4o-1-${padding=1;start=1;increment=1}`

* Generates QIO-L4o-1.

* Manually delete the â-1â.

#### Generating Names without the Suffix

Scenario: You want to create multiple QIO-L4o devices and start numbering from a specific value.

Configuration Steps

* In the Base Name field, enter:

`QIO-L4o-1-${padding=1;start=1;increment=1}, which yields QIO-L4o-1.`

* In the Quantity field, set the number of devices you want (e.g., 3).

Result

This will generate :

* QIO-L4o-5
* QIO-L4o-6
* QIO-L4o-7

#### Duplicate Handling

If some names already exist (e.g., QIO-L4o-1, QIO-L4o-2, QIO-L4o-5), the system will:

* Skip existing names.
* Fill in the next available numbers (e.g., QIO-L4o-3, QIO-L4o-4, QIO-L4o-6, etc.).

Example

Existing names:

* QIO-L4o-1
* QIO-L4o-2
* QIO-L4o-5

Adding three more devices will result in:

* QIO-L4o-3 (fills the gap)
* QIO-L4o-4 (fills the next gap)
* QIO-L4o-6 (next available after 5)

[Create New Locations for Inventory Items](javascript:void(0))

You can create virtual Locations based on physical location, or what ever you want.

For example, a Location could be an equipment room, or a specific rack in the equipment room. Another example would be one Location for all the equipment used for a specific purpose. Items are in the "Default Location" when you add them to the Inventory list.

* Select an item (in the Inventory list, or the Schematic) and type a new Location name in the Properties of that item.
* This new Location is now available to select for other Inventory items.

[Filter the Inventory List](javascript:void(0))

1. From the Inventory accordion bar, click the filter icon.
2. Select a Type from the drop-down list. Only the selected type of Inventory items display.
3. Click the **filter** icon again to close the filtering fields.

[Group the Inventory List](javascript:void(0))

Click the double braces { } to cycle through the groupings, or use the drop-down list and choose a grouping option:

* Group by Type: The Types available to group by are Amplifiers, DAB-801, Core, Line Arrays, Speakers, Subwoofers, and I/O Frames. This also works with the Filter feature.
* Group by Location: Each item in the Inventory list can be given a Location. When you Group by Location, all the items in the Inventory list are listed under their separate Locations. This grouping works in conjunction with the Filter feature. Once the list is Filtered, the Group by Location only lists those items available in the Filtered list.
* Group by Q-SYS Reflect: Sorts inventory items based on Q-SYS Reflect licensing requirements.
* Group by Status: Only works in Run mode. Groupings can be OK, Updating, Unknown, and so on.
