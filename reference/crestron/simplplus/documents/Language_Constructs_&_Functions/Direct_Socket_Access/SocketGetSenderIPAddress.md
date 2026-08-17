# SocketGetSenderIPAddress

Name:

SocketGetSenderIPAddress

Syntax:

SIGNED_INTEGER SocketGetSenderIPAddress (UDP_SOCKET UDP_Variable, STRING Address);

Description:

This function returns the IP address of the sender of a UDP. It is only valid for enabled UDP sockets. It can only be used in the SOCKETRECEIVE event for a UDP_SOCKET. 

Parameters:

UDP_Variable: the socket variable declared in the input/output section

Address: String variable into which the address is placed.

Return Value:

0: Success.

<0: Error

-1: UDP_Variable is not a UDP socket variable.

-5: No connection has been established

NOTE: Return values that are negative numbers are errors. More information on error codes for Direct Socket functions can be found [here](<Direct_Socket_Error_Codes.htm>).

Example:

In the case of Direct Socket Access Functions and events, the example code is best when viewed in the context in which it applies. For that reason, the example code for this event can be viewed by clicking [here](<Direct_Socket_Access_Example_Code.htm>). A scrolling pop up will open for your convenience.

Version:

SIMPL Version 2.10.00 or later

SIMPL+ Version 3.03.00 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Direct_Socket_Access/SocketGetSenderIPAddress.htm*
