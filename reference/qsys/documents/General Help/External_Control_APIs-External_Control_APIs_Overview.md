# External Control APIs

> Source: https://help.qsys.com/Content/External_Control_APIs/External_Control_APIs_Overview.htm

# External Control APIs

Q-SYS is designed to allow third-party systems to control and monitor various aspects of the system â including controls from Inventory and Schematic Library components in your design â via custom code.

There are multiple External Control APIs available. Click a link to learn more.

#### [Q-SYS Remote Control Protocol (QRC)](QRC/QRC_Overview.htm)

QRC is a Unicode-based TCP/IP control protocol and is the newest and most advanced API for external control of the Q-SYS system. The client connects to the Q-SYS Core processor on port 1710 and sends JSON RPC 2.0 null-terminated commands. QRC includes a separate set of API commands for PA Router control.

#### [External Control Protocol (ECP)](ECP/ECP_Overview.htm)

ECP is a legacy external control API that is still supported in all versions of Q-SYS. The client connects to the Q-SYS Core processor using a TCP/IP connection on port 1702.

#### [Q-SYS Remote WebSocket Control (QRWC)](QRWC/qrwc_overview.htm)

The QRWC External API is a tool designed to facilitate communication between third-party software and Q-SYS design controls.

#### [NPM Library](QRWC/qrwc_npm_library.htm)

Q-SYS Remote WebSocket Control (QRWC) is an NPM library designed to facilitate the interaction between third-party software and Q-SYS design controls.

#### [Q-SYS Communications Library](Communications_Library.htm)

The Q-SYS Communications Library is an alternative to connecting and controlling a Q-SYS Core processor directly via a TCP/IP connection. It presents connection, status, control, and monitoring of a Core at a higher level than direct TCP/IP socket communications, and thus is easier to use.

#### [Change Groups for ECP and QRC](external_controls_change_groups.htm)

A Change Group is a grouping of controls, created by your code, that is polled at a schedule interval. When the Change Group is polled, it returns the state of any controls that have changed since the last polling.
