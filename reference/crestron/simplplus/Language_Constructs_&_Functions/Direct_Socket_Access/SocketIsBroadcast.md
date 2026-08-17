# SocketIsBroadcast

Name:

SocketIsBroadcast

Syntax:

SIGNED_INTEGER SocketIsBroadcast (UDP_SOCKET UDP_Variable);

Description:

This function indicates whether the socket was configured with a broadcast address. It is only valid for enabled UDP sockets. This can be used to determine whether a new socket should be created if a unicast response is desired.

Parameters:

UDP_Variable: the socket variable declared in the input/output section

Return Value:

0: The UDP variable is not in a broadcast configuration.

1: The UDP variable is in a broadcast configuration

<0: Error

-1:UDP_Variable is not a UDP socket variable.

-5: No connection has been established

NOTE: Return values that are negative numbers are errors. More information on error codes for Direct Socket functions can be found [here](<Direct_Socket_Error_Codes.htm>).

Example:

In the case of Direct Socket Access Functions and events, the example code is best when viewed in the context in which it applies. For that reason, the example code for this event can be viewed by clicking [here](<Direct_Socket_Access_Example_Code.htm>). A scrolling pop up will open for your convenience.

Version:

SIMPL Version 2.10.00 or later

SIMPL+ Version 3.03.00 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Direct_Socket_Access/SocketIsBroadcast.htm*
