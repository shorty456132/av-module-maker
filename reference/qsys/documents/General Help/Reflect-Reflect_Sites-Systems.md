# Systems

> Source: https://help.qsys.com/Content/Reflect/Reflect_Sites/Systems.htm

# Systems

In the Q-SYS Reflect hierarchy, a System is a Q-SYS design file running on a Q-SYS core processor. A System typically represents a particular space within the Domain. For example, a hotel could have a System (design file) for each public space within the building â lobby, bar, outdoor patio, individual conference rooms, and so forth. The design file defines the connections to Q-SYS peripherals, such as amplifiers, cameras, touch screens, and network video endpoints.

**Note:** Refer to the [Overview](Overview.htm) topic to understand the relationship between Organizations, Domains, Systems, and Peripherals.

## Add a Core to a Domain

It's easy to register a Q-SYS Core with Q-SYS Reflect and add it to your Domain.

1. In Q-SYS Core Manager, obtain an Authorization Code from the Reflect page.
2. On the Q-SYS Reflect > Systems page, click + Add Core.
3. Paste the Authorization Code, and then click Add.

## Viewing and Pausing System Status

The Systems table provides a list of all Q-SYS Cores registered within this Domain and their associated System names.

* The Status column indicates whether a System is initializing, running, or offline. Click a System name to open the Q-SYS Core's [Status](../Status.htm) page to investigate any indicated warnings or alerts.
* Click Pause to disallow the System from reporting its status to the Alerts table and generating Notification emails. This is useful, for example, when commissioning a System or recognizing a recurring issue that is already under investigation. For more information, see [Alerts & Notifications](../Alerts.htm).

  **Tip:** You can also pause individual Inventory components within a System. Click the System name to open the Core's Status page, and then click Pause for an Inventory item. For more information, see [Status](../Status.htm).

## Manage a System

From the Systems table, click a System name to remotely manage the Q-SYS Core from Q-SYS Reflect. The available Core Management and System Management pages depend on the purchased subscription tier.

**Note:** For more information about licenses, see [Q-SYS Reflect Subscriptions](Overview.htm#Software).

|  | Q-SYS Reflect | Q-SYS Reflect Plus |
| --- | --- | --- |
| [Status](../Status.htm) |  |  |
| [Network > Basic](../Core_Management/Network_Settings.htm) |  |  |
| [Network > Date & Time](../Core_Management/Date_Time.htm) |  |  |
| [Licensing](../Core_Management/Licensing.htm) |  |  |
| [Event Log](../Event_Log.htm) |  |  |
| [Access Management > Users](../Core_Management/Users.htm) |  |  |
| [Network > Services](../Core_Management/Network_Services.htm) |  |  |
| [Files](../Core_Management/Audio_Files.htm) |  |  |
| [Utilities](../Core_Management/Utilities.htm) |  |  |
| [User Control Interfaces](../System_Management/User_Control_Interfaces.htm) |  |  |
| [Telephony > Softphones](../System_Management/Softphones.htm) |  |  |
| [Telephony > Contacts](../System_Management/Contacts.htm) |  |  |
| [Video > Cameras](../System_Management/Cameras.htm) |  |  |
| [Video > Video Endpoints](../System_Management/Video_Endpoints.htm) |  |  |
| [Dynamic Pairing](../System_Management/Dynamic_Pairing.htm) |  |  |
| [Design Backup and Restore (Beta)](../System_Management/Design_Backup.htm)[1](#1.backup) |  |  |
| [Presets](Presets.htm) |  |  |
| Remote UCIs[2](#2.UCI) |  |  |
| Remote Q-SYS Designer[3](#3.load) |  |  |

###### 1. Any Q-SYS Core processor registered with Reflect will regularly back up its running design. A Q-SYS Reflect Plus subscription is required to export a backup or restore from a backup. To learn more, see [Design Backup and Restore (Beta)](../System_Management/Design_Backup.htm).

###### 2. Access and control a UCI remotely from Q-SYS Reflect. See [User Control Interfaces](../System_Management/User_Control_Interfaces.htm).

###### 3. From Q-SYS Designer Software, remotely load from and save to Reflect-connected Cores. See the [Loading and Saving Designs](https://q-syshelp.qsc.com/#Schematic_Library/load_from_core.htm) topic for more information. The ability to remotely update Core firmware via Q-SYS Reflect is not yet available, so the Core firmware version and Q-SYS Designer Software version must match.
