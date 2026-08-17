# SocketStatus

Name:

SocketStatus

Syntax:

SOCKETSTATUS ClientVariable

{

SIGNED_INTEGER Status;

// user code for routine

Status = SocketGetStatus();

}

NOTE: ClientVariable used as an example. ServerVariable also applies.

Description:

The STATUS event is called when the status of a TCP_CLIENT or TCP_SERVER socket changes. Use the SocketGetStatus() routine to retrieve the current status (see [SocketGetStatus](<SocketGetStatus.htm>)). The Status field of the [SOCKET_STRUCT](<Direct_Socket_Access_Functions_Overview.htm>) holds the [returned values](<Status_Values.htm>) indicating the current status.

NOTE: The STATUS event is comparable to a CHANGE event on the Status field of the socket structure.

(See also [THREADSAFE](<../Events/THREADSAFE.htm>))

Parameters:

ClientVariable: the socket variable declared in the input/output section.

ServerVariable: the socket variable declared in the input/output section.

Example:

In the case of Direct Socket Access Functions and events, the example code is best when viewed in the context in which it applies. For that reason, the example code for this event can be viewed by clicking [here](<Direct_Socket_Access_Example_Code.htm>). A scrolling pop up will open for your convenience.

Version:

SIMPL Version 2.10.00 or later

SIMPL+ Version 3.03.00 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Direct_Socket_Access/SocketStatus.htm*
