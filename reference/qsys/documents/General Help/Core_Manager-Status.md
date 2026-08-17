# Status

> Source: https://help.qsys.com/Content/Core_Manager/Status.htm

# Status

The Status page provides an overview of the health of the Q-SYS system, including a list of all devices in the running design and their statuses.

## System Details

#### Redundancy

Indicates the status of the redundant Core configuration (if redundancy is enabled in the design).

#### System Name

By default, the System Name matches the Design File name. Click Rename System to assign a friendly name for the location or area being managed by this Q-SYS Core processor â for example, "Conference Room 1".

**Note:** Once you assign a new name, that name persists even if the Design File name changes. To revert to the default name, click Rename System > Reset to Design File Name.

#### Design File

The design file currently running on the Core.

#### Last Update

A date stamp corresponding to the last time the design file was changed on the Core.

## Reflect Presets

This section indicates whether a Preset is assigned to the Q-SYS Core processor (System), the status of Preset, and a timestamp of the last date and time a sync of the Preset was attempted. If a Preset is assigned, click its name to adjust its settings in Q-SYS Reflect.

To learn how to configure and link Presets, see the [Presets](../Reflect/Reflect_Sites/Presets.htm) topic in Q-SYS Reflect Help.

## Core Details

#### Name

This is the Core's hostname, as defined in the Network Settings page. See [Network > Basic](Core_Management/Network_Settings.htm).

#### Model

The Q-SYS Core processor model â for example, "Core 510i".

#### Firmware Version

The Q-SYS firmware currently running on the Core.

**Note:** If you see a Core is running QSC-Signed Firmware notification, it means that the Core is running Q-SYS firmware version 9.1.0 or later. To increase the security and integrity of the Q-SYS Ecosystem, Q-SYS v9.1.0 (and later) implements cryptographic code signing for Core firmware images to ensure their authenticity. Once a Core is updated to version 9.1.0 and later, it will inspect subsequent firmware updates for a digital signature and, by default, will only install firmware that is signed by QSC. This protects the Core against illegitimate and potentially unsafe firmware. Refer to the Utilities > [Utilities](Core_Management/Utilities.htm#Firmware) section to learn about downgrading to version 9.0.1 or lower.

#### Serial Number

This displays the Q-SYS Core's serial number.

#### Card Slots

For Q-SYS Core processor models supporting Q-SYS I/O cards, click View to see a list of installed card types.

## Inventory

The Inventory table lists all devices within the running design, and provides an at-a-glance view of their statuses, assigned names, types, Q-SYS model name, and location. Location information is determined from the Location component property in the design.

[Filtering the Inventory](javascript:void(0))

You can filter the Inventory table by Status, Type, Model, Manufacturer, and Location. You can also search for Inventory items using the Search field.

**Tip:** When selecting filter parameters, the quantity for each parameter is indicated. This can help you quickly determine, for example, the number of devices in a particular status, the number of devices of the same model, and so on.

[Hiding/Showing Columns](javascript:void(0))

Click the Columns button to select what Inventory columns to show or hide. You can toggle all columns except for Status and Name. By default, Alerts, Status, Name, Type, Model, Manufacturer, and Location are columns already shown. Additionally, you can add Serial Number, Firmware, Design, Date & Time, and Network columns.

**Tip:** To change the order in which columns appear, click and drag a column name within the Columns menu.

[Status](javascript:void(0))

|  |  |
| --- | --- |
| Unknown | This status appears during a Core reboot (for example, during a firmware update), or when a design is being pushed to the Core and before it has started running. |
| OK | The device is functioning normally. |
| Initializing | The device is in the process of a firmware or configuration update, or the design is starting. If available, click  for more information. |
| Compromised | The device is functioning, but a non-fatal problem exists. Click  for details about the problem. |
| Missing | The device cannot be discovered. Click  for details about the problem. |
| Fault | The device is malfunctioning or is mis-configured. Click  for details about the problem. |
| Not Present | This status appears when the device is not connected to the network and its Is Required component property is set to 'No'.  This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. For more information about dynamic pairing, see [Dynamic Pairing](System_Management/Dynamic_Pairing.htm). |

[Name](javascript:void(0))

The Name column indicates the Name of the device. Name information is determined from the Name property in the design.

[Type](javascript:void(0)) 

The Type column indicates the category of the device. Q-SYS peripherals and Q-SYS Reflect-enabled plugins are hard-coded with an assigned category. If your design includes third-party devices that you are monitoring using the Monitoring Proxy component, you can select from any of the following categories, or assign your own. For more information, see the Monitoring Proxy topic in the Q-SYS Designer Help.

* Amplifiers
* Audio I/O
* Cameras
* Capture Devices
* Conferencing
* Control I/O
* Control Interfaces
* Digital Signage
* Displays
* HVAC
* Lighting
* Media Players
* Media Server
* Microphones
* Network Infrastructure
* Power
* Powered Speakers
* Projectors
* Sensors
* Shades
* Video Distribution
* Video Switching
* Wireless Presentation

[Model](javascript:void(0)) 

The Model column indicates the model of the device that is in use in the Q-SYS Design.

[Manufacturer](javascript:void(0))

The Manufacturer column indicates the manufacturer of the piece of hardware being used in the Q-SYS Design.

[Location](javascript:void(0))

The Location column indicates the location of the device. Location information is determined from the Location component property in the design.

[Serial Number](javascript:void(0))

The Serial Number column indicates the Serial Number of the device. Q-SYS peripherals are hard-coded with an assigned serial number. If your design includes third-party devices, the column may show n/a as the serial number.

[Firmware](javascript:void(0))

The Firmware column indicates the specific firmware being run on the device itself. If your design includes third-party devices, the column may show n/a as the firmware.

[Design](javascript:void(0))

The Design column indicates the specific design in which the equipment is being used within Q-SYS Designer Software.

[Date & Time](javascript:void(0))

The Date & Time column includes further information for **Time Zone**, **NTP Synchronization**, and **NTP Servers**.

* **Time Zone**: If applicable, the Time Zone field will display the time zone of the equipment.
* **NTP Synchronization**: If applicable, the NTP Synchronization will show either Enabled or Disabled. It is used to synchronize with computer clock time sources in the network.
* **NTP Servers**: If applicable, the NTP Server field will show from what server the device is requesting and receiving time.

[Network](javascript:void(0))

The Network column includes further information for **LAN A**, **LAN B**, **AUX A**, **AUX B**, and **DNS**.

* **LAN A**, **LAN B**, **AUX A**, and **AUX B** offer the same information in each:
  + **Mode**: The mode determines if the device is set to a Static IP Address.
  + **IP Address**: The IP Address field reports the IP Address of the device.
  + **Netmask**: The netmask determines the network mask address the device is connected to.
  + **Gateway**: The gateway determines the gateway address the device is connected to.
  + **MAC Address**: The MAC address determines the embedded MAC Address of the device.
  + **Link Speed**: The link speed shows the maximum speed the data can move across the network.
  + **LLDP Chassis**: If applicable, the LLDP chassis field will display the identity of the chassis.
  + **LLDP Port**: If applicable, the LLDP port displays the unique number assigned to identify the endpoint connection.

* **DNS** offers additional information for **DNS Servers** and **Search Domains**.
