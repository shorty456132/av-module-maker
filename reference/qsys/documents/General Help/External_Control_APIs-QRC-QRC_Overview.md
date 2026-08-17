# Q-SYS Remote Control Protocol (QRC)

> Source: https://help.qsys.com/Content/External_Control_APIs/QRC/QRC_Overview.htm

# Q-SYS Remote Control Protocol (QRC)

Q-SYS Remote Control (QRC) is the newer and most advanced means to allow an external control system to control various functions within Q-SYS. As opposed to the [External Control Protocol (ECP)](../ECP/ECP_Overview.htm), which requires the use of Named Controls for any control needing external control, QRC allows multiple levels of control at the component level. And, unlike ECP, you do not need to drag every control you want to control into the Named Controls pane and creatively name each control for external access.

QRC includes these features:

* [Named Controls](../../Schematic_Library/external_control.htm)
* [Control Script](../../Schematic_Library/control_script_2.htm) â Control any control within any component by customizing the name of the component to make it unique.
* Mixer Control â Specialized control of mixers using mixer concepts rather than unintelligent control of each individual control
* PA Router Control â A powerful API for integrating third-party control of the PA Router functionality. This was specifically designed to allow message assembly vendors to send audio files, control, and monitor the PA Router.

Refer to the [QRC Commands](QRC_Commands.htm) topic for details on controlling Q-SYS using this protocol. Refer to the [Q-SYS PA Remote API (PARAPI)](PARAPI.htm) topic for information on how to use QRC for interfacing third-party applications with the PA Router for paging applications.

[Requirements](javascript:void(0))

If you are writing your own control software to work with Q-SYS, it is highly recommended that you have a good working knowledge of either TCP/IP socket programming. Correctly, and robustly, forming connections across a network and handling the possible error cases is not a trivial task.

[Connections](javascript:void(0))

When using the Q-SYS Remote Control Protocol, the connection is made using a TCP/IP connection on port 1710.

**Note:** A Remote Control client must communicate with the Q-SYS Core at least once every 60 seconds, or the socket connection will be closed by the Core. This is a form of "keep-alive" to make sure that abandoned connections get reclaimed by the Core. Most client programs poll a Change Group at a much higher rate which serves as a keep-alive. If not, the client program can issue a "NoOp".

### Connecting to a Core

Q-SYS operates on a client-server basis for communication with external control systems. The Q-SYS Core is the server, the remote control system is the client. A Core must have a design loaded and in Run mode for an external system to connect to it.

### Connecting to Q-SYS Designer in Emulate Mode

In order to connect to a design in Emulate mode, the design must be open in Q-SYS Designer, and be in Emulate mode.

Using a TCP/IP connection, you can connect using "localhost" (on your own PC), your computer's name, or IP Address on port 1710.

[Change Groups](javascript:void(0))

**Note:** There is a maximum limit of four change groups, but there is no restriction on the number of controls within a change group

You can create and poll Change Groups in your code using the following procedure:

1. Add a control to a Change Group using `ChangeGroup.AddControl` or `ChangeGroup.AddComponentControl`. If the Change Group does not exist, it will be automatically added.
2. Poll the Change Group using the `ChangeGroup.Poll`.
3. In response to the polling, the Core responds with the state of every control in the Change Group that has changed since the last poll, if any. If the Change Group is being polled for the first time, the Core responds with all the controls in the Change Group and their states.

**Tip:** You can choose to have the external control system make the Change Group Poll call, or use `ChangeGroup.AutoPoll` to set up automatic polling.

For additional Change Group Requirements, visit [Change Groups for ECP and QRC](../external_controls_change_groups.htm).

[Controlling Redundant Cores](javascript:void(0))

Controlling a system that has redundant Cores is relatively straightforward:

* A TCP/IP connection should be maintained with both Cores.
* `State` will be sent by both Cores automatically upon connection, or when the status changes. See [EngineStatus](QRC_Commands.htm#EngineStatus) for an example.
* All commands should be directed to the currently "active" Core, as determined by the results of `State` parameter.
* In addition, the `IsRedundant`and `DesignCode` values should be verified to ensure the two Cores are indeed a primary / backup pair running the same design.
* Commands issued to the inactive Core are ignored, and commands issued while one Core fails and the other takes over can be missed, so if it is important that all commands issued take affect, the external control system should verify the state of the controls through polling.
