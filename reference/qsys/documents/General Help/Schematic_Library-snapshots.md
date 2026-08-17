# Snapshots

> Source: https://help.qsys.com/Content/Schematic_Library/snapshots.htm

# Snapshots

Q-SYS Designer uses Snapshots to save a specific set of control settings that can be recalled and used for the same or similar events. There are two types of Snapshots: Global and Snapshot Banks.

The Snapshot list is located in the left-side pane, and accessed by clicking the Snapshot accordion bar. By default the Snapshot list contains a Global snapshot bank that cannot be deleted. You can add and delete user-defined Snapshots. The Snapshot banks, both Global and user-defined can be expanded to reveal their components. To configure a Snapshot component, drag it into the Schematic where you can set the Properties and add Control Pins.

For detailed information, refer see the [Snapshot Bank](snapshot_bank.htm) and [Snapshot Controller](snapshot_controller.htm) topics.

**Tip:** You can also control Snapshots via External Control. See [ECP Commands](../External_Control_APIs/ECP/ECP_Commands.htm).

[Global](javascript:void(0))

The purpose of the Global snapshot bank is to save a snapshot of all the control settings in a design. The Global Snapshot has up to 24 different snapshots available. The Global Snapshot bank is in the Snapshot list by default and cannot be deleted. For more information, see [Snapshot Bank](snapshot_bank.htm).

[User-defined Snapshot Banks](javascript:void(0))

Snapshot Banks are added to the Snapshot list as needed, and can be customized by adding all the controls or individual controls of components. You cannot add informational "controls" such as LEDs and meters, or momentary controls such as a Reset button. A user-defined Snapshot Bank has the following features:

* User-defined Name
* Up to 24 different snapshots
* Three different modes: Normal, Write Protect, and Scene

For more information, see [Snapshot Bank](snapshot_bank.htm).
