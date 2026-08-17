# SocketGetStatus

Name:

SocketGetStatus

Syntax:

SIGNED_INTEGER SocketGetStatus();

Description:

This function is only valid within the SocketStatus event. The reason this call is needed is to retrieve the exact status that triggered the SocketStatus event. The status of a socket can change very quickly and if the field in the socket structure is used, interim values could be missed because the code in the SocketStatus routine does not get a chance to run before the structure’s status field changes. An example of this is when a server socket gets disconnected remotely. The status will change from connected to disconnected remotely to waiting. The SocketStatus event will be triggered each time but the status field of the structure may only read waiting even in the broken remotely event.

Parameters:

None

Return Value:

The status of the socket when the event was generated.

Example:

In the case of Direct Socket Access Functions and events, the example code is best when viewed in the context in which it applies. For that reason, the example code for this event can be viewed by clicking [here](<Direct_Socket_Access_Example_Code.htm>). A scrolling pop up will open for your convenience.

Version:

SIMPL Version 2.10.00 or later

SIMPL+ Version 3.03.00 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Direct_Socket_Access/SocketGetStatus.htm*
