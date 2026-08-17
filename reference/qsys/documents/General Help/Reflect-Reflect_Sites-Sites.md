# Domains

> Source: https://help.qsys.com/Content/Reflect/Reflect_Sites/Sites.htm

# Domains

In the Q-SYS Reflect hierarchy, a Domain typically represents a physical location within an Organization. For example, hotel chains and restaurant chains have multiple locations, and each one of these could be a Domain within Q-SYS Reflect. Domains contain one or more [Systems](Systems.htm).

The Domains page provides a list of all Domains to which you have access, including Domains across multiple Organizations. Click a Domain name to see the Systems within it.

**Note:** Refer to the [Overview](Overview.htm) topic to understand the relationship between Organizations, Domains, Systems, and Peripherals.

## Creating a Domain

Domains are created from the Organizations page. To learn how to create a new Domain, see [Organizations](../Organizations.htm).

## Domain Views

You can view domains using Cards View (the default view) or Table View:

* Click  to enable Cards View. This view provides a more visual way of seeing the Systems status for each Domain.
* Click  to enable Table View.

## Domain Information

For each Domain, the following data is provided. If any Domains are reporting Systems in a Fault, Warning, or Offline status, select the Domain to investigate the list of Systems and their statuses.

* Your Role: Your current Domain membership role, Manager or Member. For more information, see [Reflect Users and Roles](Users_Roles.htm).
* Systems: The total number of Systems associated with the Domain, as well as the number within each status category:

  |  |  |
  | --- | --- |
  | OK | The number of Systems within the Domain that are currently reporting an OK, or normal, status. |
  | Faults | The number of Systems within the Domain that are currently reporting a Fault status â for example, a missing inventory component. Note that if a Domain is reporting a System in Fault status, it is also possible for that System to be reporting Warnings as well. (Faults have a higher priority for reporting purposes.) Select the Domain to investigate the list of Systems and their statuses. |
  | Warnings | The number of Systems within the Domain that are currently reporting a Warning status â for example, an inventory component configured for network redundancy with no LAN B connection. |
  | Offline | The number of Systems within the Domain that are currently not communicating with Q-SYS Reflect. |
  | Paused | The number of Systems within the Domain whose reporting to the Alerts table has been paused. For more information, see [Systems](Systems.htm). |

## Quick Status View

This option enables you to easily access comprehensive information about various statuses. You can access it through both the card and table views.

**Domain View - Cards View**: This is the default view in Q-SYS Reflect.

**Domain View - Table View**: You can choose this view in Q-SYS Reflect by selecting the Table View icon .

## Quick Status Drop-down Lists

Depending on the status, the drop-down can be displayed in one of two ways: a flat list or an expandable list.

* The flat list belongs to the next statuses: â**OK**â, â**Offline**â, and â**Paused**â.
* The expandable list belongs to the â**Faults**â and â**Warnings**â statuses.

### Flat Lists

A flat drop-down list contains item elements that display both the system name and system status.

### Expandable Lists

An expandable drop-down list contains item elements that display both the system name and system status. In addition, each item can be expanded to reveal more information about 'Devices' and 'Messages.'

#### Device Information

In the 'Devices' tab, you can find the first 5 devices from the Inventory that have fault or warning statuses. Each devie will be listed along with its current status and name for easy identfication.

#### Messages Information

In the 'Messages' tab, you can view the last 5 fault or warning messages related to devices experiencing issues.

### Live Updates

Live updates are unavailable in the current quick status view. To see updated content, the drop-down must be closed and reopened.

Similarly, to update data within an expanded item, you will need to collapse and expand it again.
