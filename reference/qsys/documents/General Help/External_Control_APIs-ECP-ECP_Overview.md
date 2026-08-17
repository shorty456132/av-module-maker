# External Control Protocol (ECP)

> Source: https://help.qsys.com/Content/External_Control_APIs/ECP/ECP_Overview.htm

# External Control Protocol (ECP)

The Q-SYS External Control Protocol (ECP) is the original Named Control -based external control protocol that has been available since version 1.0 of Q-SYS Designer Software and firmware. Though ECP has been superseded by the newer [Q-SYS Remote Control Protocol (QRC)](../QRC/QRC_Overview.htm), it is still supported in all versions of Q-SYS. Therefore, If you have developed code on a third-party control system for using this protocol to control Q-SYS, you do not need to rewrite any code to use QRC.

**Note:** Refer to the [Named Controls](../../Schematic_Library/external_control.htm) topic for details on exposing controls and indicators to external control and monitoring using ECP. Refer to the [ECP Commands](ECP_Commands.htm) topic for a list of supported commands.

[Requirements](javascript:void(0))

If you are writing your own control software to work with Q-SYS, it is highly recommended that you have a good working knowledge of either TCP/IP socket programming or using a Microsoft .NET framework library assembly. Correctly, and robustly, forming connections across a network and handling the possible error cases is not a trivial task.

[Connections](javascript:void(0))

When using the Q-SYS External Control Protocol, the connection is made using a TCP/IP connection on port 1702. You can also connect to a Core using the Q-SYS Communications Library.

**Note:** An External Control client must communicate with the Q-SYS Core at least once every 60 seconds, or the socket connection will be closed by the Core. This is a form of "keep-alive" to make sure that abandoned connections get reclaimed by the Core. Most client programs poll a Change Group at a much higher rate which serves as a keep-alive. If not, the client program can issue a "Status Get" command periodically, or a "Control Set Value" on an unused control if no return response is desired.

### Connecting to a Core

Q-SYS operates on a client-server basis for communication with external control systems. The Q-SYS Core is the server, the external control system is the client. A Core must have a design loaded and in Run mode for an external system to connect to it.

### Connecting to Q-SYS Designer in Emulate Mode

In order to connect to a design in Emulate mode, the design must be open in Q-SYS Designer, and be in Emulate mode.

* Using a TCP/IP connection, you can connect using "localhost" (on your own PC), your computer's name, or IP Address on port 1702.
* Using the Communications Library, you can connect PC's name or IP Address.

### Redundant Cores

During a Core failover, where the active Core stops accepting control and the standby Core takes over, the controlling application needs to recognize the failover situation by polling the Cores in the background using Status Get. When a Core goes down, the controlling application naturally re-syncs it's state with that of the newly active Core when it connects to it. This happens in the following manner: the controlling application, after connecting to a Core, creates a change group of all controls of interest after which the first change group poll will return the values of all of the controls, thus syncing the controller to Q-SYS. Note that this "re-sync" will occur whether the controlling application is connecting to a backup Core that has become active or reconnecting to the same Core due to a network failure.

[Change Groups](javascript:void(0))

You can create and poll Change Groups in your code using the following procedure:

**Note:** In the following procedure, the Q-SYS External Control Protocol call is given first, followed by the Q-SYS Communications Library method.

1. Create a Change Group using the Change Group Create (cgc) call or the CreateChangeGroup method.
2. Add controls and/or indicators to the Change Group using the Change Group Add (cga) call or the AddControlToChangeGroup method.
3. Poll the Change Group using the Change Group Poll (cgp) call or the PollChangeGroup method.
4. In response to the polling, the Core responds (cv or cvv, or ControlResponse or ControlVectorResponse) with the state of every control in the Change Group that has changed since the last poll, if any, followed by the Change Group Poll Ack (cgpa or ChangeGroupAck) response. If the Change Group is being polled for the first time, the Core responds with all the controls in the Change Group and their states. If any metadata aspect attached to a control in the Change Group changes, the Core responds with (cmv or cmvv, or ControlMetaDataResponse or ControlMetaDataVectorResponse) in response to the Change Group Poll.

For additional Change Group Requirements, visit [Change Groups for ECP and QRC](../external_controls_change_groups.htm).

[Procedure](javascript:void(0))

1. In Q-SYS Designer, select and name the controls you want to make available to external control.
   1. Each control is selected individually.
   2. Each control has a unique identifying name.
2. Run the design on a Core  
    or  
   Emulate the design.
3. Test external control.
   1. Use the external control system to access the controls over a TCP/IP connection or using the Communications Library.
   2. Optionally, for TCP/IP use Telnet to test external Control. Refer to [Test External Controls](Test_External_Controls.htm) for details.
      1. If running on a Core, connect to that Core using Telnet.
      2. If emulating, connect to the design using Telnet.
      3. Enter commands at the Telnet command prompt to verify proper operation. Refer to the [ECP Commands](ECP_Commands.htm) topic for the commands.
4. The third-party system is now ready to use for controlling Q-SYS.

[Controlling Redundant Cores](javascript:void(0))

Controlling a system that has redundant Cores is relatively straightforward:

* A TCP/IP connection should be maintained with both Cores.
* The status of each Core should be periodically polled using the Status Get command.
* All other commands should be directed to the currently "active" Core, as determined by the results of status polling.
* In addition, the DESIGN\_ID values and the IS\_PRIMARY flags of the two Cores should be checked to verify that the two Cores are indeed a primary/backup pair running the same design.
* Commands issued to the inactive Core are ignored, and commands issued while one Core fails and the other takes over can be missed, so if it is important that all commands issued take effect, the external control system should verify the state of the controls through polling.
