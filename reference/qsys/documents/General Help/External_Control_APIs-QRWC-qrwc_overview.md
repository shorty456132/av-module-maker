# Q-SYS Remote WebSocket Control (QRWC)

> Source: https://help.qsys.com/Content/External_Control_APIs/QRWC/qrwc_overview.htm

# Q-SYS Remote WebSocket Control (QRWC)

Q-SYS Remote WebSocket Control (QRWC) is a tool designed to facilitate communication between third-party software and Q-SYS design controls. It is implemented as an [NPM library](https://www.npmjs.com/package/@q-sys/qrwc), which allows developers to control and interact with Q-SYS [Code Name and Script Access](../../Control_Scripting/Code_Name_Script_Access.htm) components via WebSocket connections.

**Note:** This is a BETA feature. Though it is functional, it is not feature complete and is subject to change. QSC assumes no responsibility for any issues that may arise from using this feature.

[Requirements](javascript:void(0))

**CAUTION:** If you are writing your own control software to work with Q-SYS, you must have a solid understanding of JavaScript Web Apps, and using WebSockets . Forming connections across a network and handling potential error cases correctly and robustly is not a trivial task. Ignorance in this area will lead to failures and unreliable software.

1. You must have access to the [NPM Library.](https://www.npmjs.com/package/@q-sys/qrwc)
2. In Core Manager, enable the Websocket capability under the [Network > Services](../../Core_Manager/Core_Management/Network_Services.htm) page.
3. Code Access must be set to 'External' or 'All' in Q-SYS Designer. See [Code Name and Script Access](../../Control_Scripting/Code_Name_Script_Access.htm#Viewing) for more information.

[Connections](javascript:void(0))

When using QRWC, the connection is made using a WebSocket connection on port 443.

**Note:** A Remote Control client must communicate with the Q-SYS Core at least once every 60 seconds, or the socket connection will be closed by the Core. This is a form of "keep-alive" to make sure that abandoned connections get reclaimed by the Core.

### Connecting to a Core

Q-SYS operates on a client-server basis for communication with external control systems. The Q-SYS Core is the server, the remote control system is the client. A Core must have a design loaded and in Run mode for an external system to connect to it.

**Note:** Connecting to a design using QRWC is not supported in Emulation Mode.

[Controlling Redundant Cores](javascript:void(0))

Controlling a system that has redundant Cores is relatively straightforward:

* A WebSocket connection should be maintained with both Cores.
* `State` will be sent by both Cores automatically upon connection, or when the status changes. See [EngineStatus](../QRC/QRC_Commands.htm#EngineStatus) for an example.
* All commands should be directed to the currently "active" Core, as determined by the results of `State` parameter.
* In addition, the `IsRedundant`and `DesignCode` values should be verified to ensure the two Cores are indeed a primary / backup pair running the same design.
* Commands issued to the inactive Core are ignored, and commands issued while one Core fails and the other takes over can be missed, so if it is important that all commands issued take affect, the external control system should verify the state of the controls through polling.

[Network Services and Protocols](javascript:void(0))

For more information, visit [Q-SYS Remote WebSocket Control (BETA)](../../Networking/Interfaces_Services.htm#QRWC_Network).
