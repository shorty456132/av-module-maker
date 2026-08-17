# SocketGetAddressAsRequested

Name:

SocketGetAddressAsRequested

NOTE: This topic covers the SocketGetAddressAsRequested function for TCP_CLIENT ClientVariable and TCP_SERVER Server Variable.

Syntax:

SIGNED_INTEGER SocketGetAddressAsRequested (TCP_CLIENT ClientVariable, STRING Address);

SIGNED_INTEGER SocketGetAddressAsRequested (TCP_SERVER ServerVariable, STRING Address);

Description:

This function will return the address parameter used for the SocketConnectClient() call or the SocketServerStartListenCall(). It is only valid for connected sockets.

Parameters:

For TCP_CLIENT ClientVariable:

ClientVariable: the socket variable declared in the input/output section.

Address: String variable into which the address is placed.

For TCP_SERVER ServerVariable:

ServerVariable: the socket variable declared in the input/output section.

Address: String variable into which the address is placed.

Return Value:

0: Success

<0: Error

-1: ClientVariable is not a TCP client variable (TCP_CLIENT ClientVariable).

-1: ServerVariable is not a TCP server variable. (TCP_SERVER ServerVariable).

-5: No connection has been established

NOTE: Return values that are negative numbers are errors. More information on error codes for Direct Socket functions can be found [here](<Direct_Socket_Error_Codes.htm>).

Example:

In the case of Direct Socket Access Functions and events, the example code is best when viewed in the context in which it applies. For that reason, the example code for this event can be viewed by clicking [here](<Direct_Socket_Access_Example_Code.htm>). A scrolling pop up will open for your convenience.

Version:

SIMPL Version 2.10.00 or later

SIMPL+ Version 3.03.00 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Direct_Socket_Access/SocketGetAddressAsRequested.htm*
