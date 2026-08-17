# SocketServerStartListen

Name:

SocketServerStartListen

Syntax:

SIGNED_INTEGER SocketServerStartListen(TCP_SERVER ServerVariable, STRING Address, INTEGER port);

Description:

This function initiates listening on a TCP_SERVER socket.

Parameters:

ServerVariable: the socket variable declared in the input/output section.

Address: string variable containing the remote address; either as an IP address or as a name to be resolved into an address. If non-zero, connections are only allowed from the address matching the string.

Port: number for the TCP server connection.

Return Value:

0: Success

<0: Error

-1: ServerVariable is not a TCP/IP server variable.

-4: Port not in range of 0-65535

NOTE: Return values that are negative numbers are errors. More information on error codes for Direct Socket functions can be found [here](<Direct_Socket_Error_Codes.htm>).

Example:

In the case of Direct Socket Access Functions and events, the example code is best when viewed in the context in which it applies. For that reason, the example code for this event can be viewed by clicking [here](<Direct_Socket_Access_Example_Code.htm>). A scrolling pop up will open for your convenience.

Version:

SIMPL Version 2.10.00 or later

SIMPL+ Version 3.03.00 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Direct_Socket_Access/SocketServerStartListen.htm*
