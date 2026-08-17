# SocketSend

Name:

SocketSend

NOTE: This topic covers the SocketGetPortNumber function for TCP_CLIENT ClientVariable, TCP_SERVER Server Variable and UDP_SOCKET UDP_Variable.

Syntax:

SIGNED_INTEGER SocketSend(TCP_CLIENT ClientVariable, STRING TxString);

Description:

This function transmits data on the SOCKET_STRUCT currently being used. SocketSend can be used by all three sockets; TCP_CLIENT, TCP_SERVER and UDP_SOCKET.

Parameters:

ClientVariable: the socket variable declared in the input/output section (TCP_CLIENT socket).

ServerVariable: the socket variable declared in the input/output section (TCP_SERVER socket).

UDP_Variable: the socket variable declared in the input/output section (UDP_SOCKET socket).

TxString: String variable containing the data to transmit.

Return Value:

>=0: Success with number of bytes sent (2-series processors)

=0: Success (3-series processors)

<0: Error

-1: ClientVariable is not a TCP/IP client variable (TCP_CLIENT socket).

-1: ServerVariable is not a TCP server variable (TCP_SERVER socket).

-1: UDP_Variable is not a UDP variable (UDP_SOCKET socket).

-5: No connection has been established

NOTE: Return values that are negative numbers are errors. More information on error codes for Direct Socket functions can be found [here](<Direct_Socket_Error_Codes.htm>).

Example:

In the case of Direct Socket Access Functions and events, the example code is best when viewed in the context in which it applies. For that reason, the example code for this event can be viewed by clicking [here](<Direct_Socket_Access_Example_Code.htm>). A scrolling pop up will open for your convenience.

Version:

SIMPL Version 2.10.00 or later

SIMPL+ Version 3.03.00 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Direct_Socket_Access/SocketSend.htm*
