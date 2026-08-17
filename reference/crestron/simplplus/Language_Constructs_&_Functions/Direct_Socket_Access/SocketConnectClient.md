# SocketConnectClient

Name:

SocketConnectClient

Syntax:

SIGNED_INTEGER SocketConnectClient(TCP_CLIENT ClientVariable,STRING Address, INTEGER Port, INTEGER Reconnect);

Description:

This function initiates a connection on a TCP_CLIENT socket.

Parameters:

ClientVariable: the socket variable declared in the input/output section.

Address: string variable containing the destination address; either as an IP address or as a name to be resolved into an address.

Port: number for the TCP client connection.

Reconnect: indicates whether the socket should reconnect automatically when disconnected from the remote end.

Return Value:

0: Success

<0: Error

-1: ClientVariable is not a TCP/IP client variable.

-2: Could not create the connection task

-3: Port not in range of 0-65535.

NOTE: Return values that are negative numbers are errors. More information on error codes for Direct Socket functions can be found [here](<Direct_Socket_Error_Codes.htm>).

Example:

In the case of Direct Socket Access Functions and events, the example code is best when viewed in the context in which it applies. For that reason, the example code for this event can be viewed by clicking [here](<Direct_Socket_Access_Example_Code.htm>). A scrolling pop up will open for your convenience.

Version:

SIMPL Version 2.10.00 or later

SIMPL+ Version 3.03.00 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Direct_Socket_Access/SocketConnectClient.htm*
