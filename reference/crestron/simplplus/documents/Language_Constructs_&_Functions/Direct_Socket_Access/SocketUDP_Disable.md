# SocketUDP_Disable

Name:

SocketUDP_Disable

Syntax:

SIGNED_INTEGER SocketUDP_Disable(UDP_SOCKET UDP_Variable);

Description:

This function disables the operation of an UDP_SOCKET.

Parameters:

UDP_Variable: the socket variable declared in the input/output section.

Return Value:

0: Success

<0: Error

-1: UDP_Variable is not a UDP variable.

NOTE: Return values that are negative numbers are errors. More information on error codes for Direct Socket functions can be found [here](<Direct_Socket_Error_Codes.htm>).

Example:

In the case of Direct Socket Access Functions and events, the example code is best when viewed in the context in which it applies. For that reason, the example code for this event can be viewed by clicking [here](<Direct_Socket_Access_Example_Code.htm>). A scrolling pop up will open for your convenience.

Version:

SIMPL Version 2.10.00 or later

SIMPL+ Version 3.03.00 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Direct_Socket_Access/SocketUDP_Disable.htm*
