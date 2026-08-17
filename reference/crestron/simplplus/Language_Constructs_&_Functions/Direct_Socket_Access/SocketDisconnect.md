# SocketDisconnect:

Name:

SocketDisconnect

Syntax:

SOCKETDISCONNECT ClientVariable

{

// user code for routine

}

NOTE: ClientVariable used as an example. ServerVariable also applies.

Description:

The SocketDisconnect event is called when a TCP_CLIENT or TCP_SERVER socket is disconnected. The Status field of the [SOCKET_STRUCT](<Direct_Socket_Access_Functions_Overview.htm>) holds the [returned values](<Status_Values.htm>) indicating the cause of the disconnection.

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
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Direct_Socket_Access/SocketDisconnect.htm*
