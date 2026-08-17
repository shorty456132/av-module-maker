# Space Manager

> Source: https://help.qsys.com/Content/Reflect/Space_Manager.htm

# Space Manager

Space Manager is a feature within the Q-SYS Reflect platform that helps you organize and monitor AV systems by their physical locationsâfrom entire organizations down to individual rooms. It provides a flexible hierarchy and intuitive views so you can quickly visualize deployments and assess system health.

## Interface Overview

The Space Manager interface is divided into three main panels for easy navigation and management:

1. Spaces Panel (Left Pane) â Displays the hierarchical structure of spaces (organization, sites, buildings, levels, rooms).
2. Main Content Panel (Center) â Shows detailed listings of child spaces for the selected node, with options to create or delete spaces.
3. Visual Summary Panel (Right Pane) â Provides quick insights into the selected space, including system health, hierarchy, and location details.

You can switch between two views using the Hierarchy/Map toggle:

* Hierarchy View â A nested tree of all spaces, ideal for structured navigation.
* Map View â A geographical visualization of configured spaces, showing building locations and their system statuses.

### Hierarchy View

[Spaces Panel (Left Pane)](javascript:void(0))

#### Organization

A read-only field showing the organization you are currently viewing (toggle between organizations if you have access to more than one).

#### Spaces Tree

Lists all regions, sites, buildings, labs, and rooms in a hierarchical format. Users can grab any space in the left hierarchy and drag it to a new valid parent.

**Note:** Only Admins and Managers may move spaces.

* Expand/collapse nodes to view child spaces.
* Each space is marked with an icon indicating its type (e.g., building icon for physical structures).

Space ontology is enforced to preserve structural integrity. Us the following chart for allow movement of spaces:

| Space Type | Allowed New Parent |
| --- | --- |
| Region | X - Cannot be moved |
| Site | Region |
| Building | Region, Site |
| Outdoor Space | Region, Site |
| Level | Building |
| Room | Building, Level |
| Zone | Building, Outdoor Space, Level, Room, Zone |

**Note:** Attempts to move a space to an invalid parent are rejected.

#### Space Collections

Create custom groups of spaces to monitor system health, simplify navigation, and organize environments based on your operational needs.

##### + Create Collection

Click to add a custom group. Enter the desired name when prompted.

##### + Add

Click to add to a collection based on Building, Outdoor Space, Level, Room, or Zone.

##### Organization

A read-only field showing the organization you are currently viewing (toggle between organizations if you have access to more than one).

##### CollectionsTree

Lists all regions, sites, buildings, labs, and rooms in a hierarchical format.

* Expand/collapse nodes to view child spaces.
* Each space is marked with an icon indicating its type (e.g., building icon for physical structures).

#### Status Indicators

A space inherits the overall status of its child spaces. For example, if one room within a building is in fault, the entire building is shown as in fault.

[Main Content (Middle Pane)](javascript:void(0))

#### Create Space

Add a new space (e.g., a building or level) under the currently selected parent.

#### Delete Space

Remove a space (enabled only when a space is selected).

#### Columns

* Name â The name of the space.
* Type â The type of space (e.g., building, level, room).

#### Permissions

Only organization admins or managers can create and delete spaces.

#### Hierarchy Flexibility

Recommended hierarchy is Organization â Region â Site â Building/Outdoor Space â Levels â Rooms/Zones. However, hierarchy is not strictly enforced (e.g., you can create a site directly under an organization without defining a region).

[Visual Summary Panel (Right Pane)](javascript:void(0))

The right panel provides context and insights about the selected space through multiple sections:

#### General

* View or update the space name.
* Link systems to the space (a system can be linked to multiple spaces).

#### Systems

A color-coded pie chart displays the total systems in the space by status:

* **Red** â Fault (critical issues)
* **Yellow** â Warning (minor issues)
* **Green** â OK (normal)
* **Blue** â Paused (temporarily halted)
* **Black** â Offline (not connected or powered on)

#### Space Hierarchy

* Displays the nested hierarchy of the selected space.
* Use **Show Only Faults** to filter and highlight problem spaces quickly.

#### Location (only for buildings)

* Enter building address details.
* Postal Code automatically populates coordinates.
* Once coordinates are available, **View on Map** becomes active, redirecting you to Map View for a geographical preview.

### Map View

Map View offers a geographical overview of all configured buildings:

* Buildings are clustered by coordinates in the initial view.
* Hovering over a cluster shows the number of systems and their statuses.
* Clicking a cluster zooms in, displaying individual building pins.
* Hovering over a building pin shows system health details for that building.
