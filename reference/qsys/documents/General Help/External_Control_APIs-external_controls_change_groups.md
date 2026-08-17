# Change Groups for ECP and QRC

> Source: https://help.qsys.com/Content/External_Control_APIs/external_controls_change_groups.htm

# Change Groups for ECP and QRC

Q-SYS provides monitoring capability through the use of Change Groups. A Change Group is a grouping of controls, created by your code, that is polled at a schedule interval. When the Change Group is polled, it returns the state of any controls that have changed since the last polling.

When an external control system is interested in the state of a large number of controls, it is very inefficient to ask for the state of each control individually. Q-SYS provides Change Groups to reduce network bandwidth use and improve efficiency.

All Change Groups are automatically deleted from the Core when the TCP/IP connection goes down, there is a CommunicationError, or when the Core goes down. In either case, the Change Group(s) need to be re-initialized. This allows each external control connection to have its own set of Change Groups, but makes sure that a memory leak is not caused if the external control system repeatedly connects and disconnects.

### Change Group Requirements

Q-SYS operates on a client-server basis for communication with external control systems. The Q-SYS Core is the server, the external control system is the client. A Core must have a design loaded and in Run mode for an external system to connect to it.

When a control is added to an existing Change Group, it is considered changed so the Core responds with the new control's state even if it has not changed.

* Q-SYS Designer running on a PC, External Control Systems, and UCIs are all considered clients to the Core. The maximum number of simultaneous Change Groups is 512.
  + Each Q-SYS Designer instance requires 1 Change Group
  + Each active iOS UCI requires one Change Group
  + Each active UCI instance (TSC, UCI Viewer), requires one Change Group each
  + Cores 1100 and 3100 require two Change Groups each
  + Redundant Cores require two Change Groups for control synchronization when redundant networking is used, or one change group if the network is not redundant.
  + External control systems can have zero to four Change Groups.

* If your system has redundant Cores, each Core must be accessed by its own host name or IP Address.
* If you access a backup Core in the standby mode, and try to change a control, you will receive an error.
* All Change Groups are automatically deleted from the Core when the TCP/IP connection goes down, there is a CommunicationError, or when the Core goes down. In either case, the Change Group(s) need to be re-initialized. This allows each external control connection to have its own set of Change Groups, but makes sure that a memory leak is not caused if the external control system repeatedly connects and disconnects.
