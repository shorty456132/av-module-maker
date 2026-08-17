# Status

> Source: https://help.qsys.com/Content/RoomSuite/Status.htm

# Status

The Status page in the RoomSuite Modular System provides a centralized view of your room systemâs operational health and configuration. From this view, you can quickly verify whether the system is functioning normally, confirm processor identity and firmware details, and review the state of all connected devices. High level indicators summarize system health at-a-glance, such as processor status, system faults, and registration with Q-SYS Reflect, while detailed sections allow you to drill down into processor properties, inventory lists, and device level conditions. Use Status as your primary dashboard for monitoring, troubleshooting, and preparing for maintenance, ensuring that every room remains ready for use and aligned with organizational standards.

## Application Header

The Application Header is the top banner of the RoomSuite Modular System interface. It remains visible at all times, providing high-level context and quick access to essential system indicators.

#### Menu (Hamburger) Icon

Opens the main application menu. Use this to navigate to other areas of RoomSuite Modular System, such as Network, Access Management, or Utilities.

#### Processor Name

Shows the configured name of the processor, RMP-100, for this room system. Use this to confirm you are viewing the correct room, especially helpful when matching to asset labels or inventory records.

#### System Status

Indicates whether the room system is functioning normally.

* Green (Running, no faults) â System is operating normally.

* Red (Running with faults) â System is running but has one or more issues that need attention.

#### Reflect

Shows whether the system is registered with Reflect Enterprise Manager, if deployed.

* Registered â Remote monitoring and management are enabled.

* Not Registered â Reflect features are unavailable for this room.

#### Room System Optimization (RSO) Status

Summarizes the status of RSO.

* OK - No detected issues.
* Fault - One or more checks failed; drill into diagnostics or the Inventory section for details.
* Not Present - Not Optimized.

#### Help Icon

Provides contextual help or links to documentation.

#### Access Control Status

Indicates whether user access control is active. If disabled, anyone on the management network may access this interface.

#### Go to Users

A quick link to the Access Management page, where you can enable access control, configure user accounts, and adjust permissions.

## System Identity Panel

This panel serves as a visual summary of the room system you are currently managing. It provides clear identification of the system type, processor model, and options for customizing the system name. This section helps you confirm that you are working on the correct room and gives you a starting point for any configuration or troubleshooting tasks. Any changes you make within this context apply only to this room system, not to other rooms or global settings.

#### System Display Name

Displays the system type, Modular System, and confirms that the interface is showing a modular room system rather than another application context.

#### Processor

Shows the processor model type, RMP-100. Use this to verify the hardware model installed in the room.

#### Rename System Button

Allows you to change the systemâs display name. Use this feature to assign meaningful labels such as âHQFloor1\_Conf-Room Aâ, so administrators and support staff can easily identify the room in dashboards, reports, or support tickets.

**Tip:** If you manage multiple rooms, meaningful names and confirmed processor models help prevent configuration errors and streamline troubleshooting.

#### Reflect Presets

This section is dedicated to Reflect integration for preset management. If your organization uses Reflect, this section confirms that preset functionality is available for this room.

When you see No Linked Presets, it means that:

* No presets have been associated with this room system yet, or

* Reflect integration is not actively used in your environment.

* If Reflect is enabled and configured, this panel will list preset names and their statusâactive, pending, or unavailable.

If presets are missing, you may need to:

* Confirm whether Reflect is deployed for your organization.

* Check if presets have been created and linked to this room.

* For environments using Reflect, this panel is your quick reference to ensure the correct presets are applied to each room for consistent configuration and performance.

**Tip:** If you rely on remote monitoring and preset management, make sure this panel shows the expected presets. Missing presets could indicate incomplete setup or a registration issue with Reflect.

## Processor Details

The Processor Details section shows key information about the RMP-100 in the room. Use this section to check the processorâs name, model, and firmware version, and to make sure the firmware is trusted and up to date.

#### Processor is running QSC-Signed Firmware

Confirms that the firmware on this processor is signed and trusted by QSC. If this message changes, for example, to âNon-QSC firmwareâ or displays a warning, you should investigate or update the firmware to maintain compliance and stability.

#### Name

Represents the logical or host name for the processor and often corresponds to how the processor is referenced in the network or management systems. Use this to match against asset records or inventory systems.

#### Model

Indicates the specific hardware model installed in the room.

#### Firmware Version

Displays the exact firmware build currently installed. Support teams often request this value when diagnosing issues or advising on updates.

#### Serial Number

This is the unique identifier for the physical processor device. Use this for asset tracking, inventory management, or when submitting support tickets. Matching the serial number ensures youâre working with the correct hardware in multi-room or large deployments.

## Inventory

The Inventory section includes lists all devices the system expects in the room, such as displays, cameras, microphones, and loudspeakers, as well as tools to narrow down and manage the device list. This is your main view for checking device-level health and confirming that everything is present and functioning.

#### Status Filter

Filter devices by health status, such as OK, Not Present, or Fault. Use this to quickly focus on devices that need attention.

#### Type Filter

Filter by device type: Camera, Control Interface, Display, Network Loudspeaker, Network Microphone, Peripheral, Processor, Streaming I/O, Video I/O, or Video Source.

#### Model Filter

Narrows the list to a specific device model. Device types include: Generic AV Source, Generic HDMI Display, NC-12x80, NC-20x60, NC-90-G2, NL-C4, NL-P4, NL-SB42, NM-T1, QIO-VEN4, RMP-100, TSC-101-G3, and TSC-70-G3.

#### Manufacturer Filter

Filter by manufacturer, for example, QSC vs third-party devices.

#### Location Filter

Filters devices based on their configured physical location in the room, for example Front Wall, Ceiling North. Helps support staff quickly identify where a faulty device is installed.

#### Search Bar

Free-text search across device names or other visible fields. Use this to quickly find a specific device by name, such as HDMI-Display-2.

#### Export as CSV

Export as CSV allows you to download the current inventory view for offline analysis, reporting, or sharing with other teams.

#### Columns Drop-down

Show or hide table columns to simplify the view or expose additional fields.

### Inventory Table

#### Status

* Green dot, OK â device is present and functioning.
* Grey dot, Not Present â device is missing, not detected, device powered off, device disconnected, device removed or replaced without updating configuration, cabling issues.
* Information icon â hover or click for more details about the issue.

#### Name

Example: HDMI-Display-1. A readable identifier for the device.

#### Type

Examples: Display, Camera, Network Loudspeaker, Network Microphone. Confirms the functional role of the device.

#### Model

Examples: Generic HDMI Display, NC-90-G2, NL-P4, NM-T1. Useful for troubleshooting and verifying compatibility.

#### Manufacturer

Example: QSC. Helps distinguish QSC devices from third-party equipment.

#### Location

Example: Default Location Logical or physical location in the room.

### Status Management in Everyday Workflows

#### Quick Room Health Check

* Look at System Status, RSO Status, and check for any Not Present devices in the Inventory Panel.
* If all indicators are green or show OK, the room should be ready for use without issues.

#### Troubleshooting

* If someone reports a problem such as âThe display is not working,â open the Inventory Panel.
* Apply the Type filter to Display and review the status of each display device.
* Use the Location and Name columns to guide on-site checks and confirm which device needs attention.

#### Preparing for Maintenance Windows

* Go to the Processor Details Panel and check the Firmware Version before scheduling upgrades.
* Export the Inventory as a CSV file for documentation or sharing with other teams.

#### Ensuring Remote Monitoring is Enabled

* Check the Reflect status and the Reflect Presets Panel.
* If Reflect is not registered and your organization relies on remote monitoring, go to Reflect Registration to complete setup.
