# Direct Socket Access Functions Overview

Socket functions make it possible for SIMPL+ to access the Internet, or even simply use Ethernet, without the necessity of going through the SIMPL program. This is important because SIMPL imposes a returned character limit that would truncate a web page or string after about 255 characters. SIMPL+ does not have this limitation so socket functions through SIMPL+ are highly desirable.

There are three socket types implemented in SIMPL+ and they are treated as new I/O data types: TCP/IP clients (TCP_CLIENT), TCP/IP server (TCP_SERVER) and UDP socket (UDP_SOCKET). These three sockets each use a pre-defined structure called SOCKET_STRUCT to access the variables and functions in the table later in this topic.

NOTE: Declarations of direct socket types must come after all input and output declarations. The reason for this is that the implied receive buffer for each socket will be indexed starting from the last string or buffer input.

The implied structure of client, server and UDP socket SOCKET_STRUCT is shown immediately below.

STRUCTURE SOCKET_STRUCT

{

INTEGER SocketStatus;

STRING SocketRxBuf;

}TCP_CLIENT, TCP_SERVER, UDP_SOCKET

where;

Status equals the current status of the socket. The following returned values are comparable to those in the TCP/IP Client and Server symbols:

Keyword |  Value |  Connection Status  
---|---|---  
SOCKET_STATUS_NO_CONNECT |  0 |  Not Connected  
SOCKET_STATUS_WAITING |  1 |  Waiting for Connection  
SOCKET_STATUS_CONNECTED |  2 |  Connected  
SOCKET_STATUS_CONNECT_FAILED |  3 |  Connection Failed  
SOCKET_STATUS_BROKEN_REMOTELY |  4 |  Connection Broken Remotely  
SOCKET_STATUS_BROKEN_LOCALLY |  5 |  Connection Broken Locally  
SOCKET_STATUS_DNS_LOOKUP |  6 |  Performing DNS Lookup  
SOCKET_STATUS_DNS_FAILED |  7 |  DNS Lookup Failed  
SOCKET_STATUS_DNS_RESOLVED |  8 |  DNS Name Resolved  
  
String contains received serial data from the socket.

The error codes that can be returned by Direct Socket Access functions are listed in the following table.

Keyword |  Value |  Connection Status  
---|---|---  
SOCKET_INVALID_SOCKET  |  -1 |  Client, Server or UDP variable not a TCP/IP or UDP variable.  
SOCKET_NO_CONNECT_TASK  |  -2 |  Could not create the connection task  
SOCKET_NO_DNS_RESOLVE  |  -3 |  Could not resolve address  
SOCKET_INVALID_PORT_NUMBER |  -4 |  Port not in range of 0-65535.  
SOCKET_NOT_CONNECTED  |  -5 |  No connection has been established  
SOCKET_STRING_TOO_SMALL  |  -6 |  Not enough room in string parameter to hold IP address.  
  
The available Direct Socket Functions are described as follows:

FUNCTION |  DESCRIPTION  
---|---  
[SocketConnect](<SocketConnect.htm>) |  The SocketConnect event is called when a connection is completed on a TCP_CLIENT or TCP_SERVER variable.  
[SocketDisconnect](<SocketDisconnect.htm>) |  The SocketDisconnect event is called when a TCP_CLIENT or TCP_SERVER socket is disconnected.   
[SocketReceive](<SocketReceive.htm>) |  The SocketReceive event is called when a TCP_CLIENT or TCP_SERVER socket receives data.  
[SocketConnectClient](<SocketConnectClient.htm>) |  This function initiates a connection on a TCP_CLIENT socket.  
[SocketDisconnectClient](<SocketDisconnectClient.htm>) |  This function disconnects a TCP_CLIENT socket.  
[SocketServerStartListen](<SocketServerStartListen.htm>) |  This function initiates listening on a TCP_ SERVER socket.  
[SocketServerStopListen](<SocketServerStopListen.htm>) |  This function halts listening on a TCP_SERVER socket.  
[SocketUDP_Enable](<SocketUDP_Enable.htm>) |  This function enables the operation of an UDP_SOCKET.  
[SocketUDP_Disable](<SocketUDP_Disable.htm>) |  This function disables the operation of an UDP_SOCKET  
[SocketSend](<SocketSend.htm>) |  This function transmits data on the SOCKET_STRUCT currently being used. SocketSend can be used by all three sockets; TCP_CLIENT, TCP_SERVER and UDP_SOCKET .  
[SocketStatus](<SocketStatus.htm>) |  The SocketStatus event is called when the status of a TCP_CLIENT or TCP_SERVER socket changes.  
[SocketGetStatus](<SocketGetStatus.htm>) |  The SocketGetStatus event is called to retreive the exact status that triggers a SocketStatus event.  
[SocketGetPortNumber](<SocketGetPortNumber.htm>) |  This function returns the current port number for the given socket. It is only valid for connected sockets.  
[SocketGetRemoteIPAddress](<SocketGetRemoteIPAddress.htm>) |  This function will return the IP Address of the remote device for a given connection or the IP address of a remote client connected to the given server variable.  
[SocketGetAddressAsRequested](<SocketGetAddressAsRequested.htm>) |  This function will return the address parameter used for the SocketConnectClient() call or the SocketServerStartListenCall(). It is only valid for connected sockets.  
[SocketIsBroadcast](<SocketIsBroadcast.htm>) |  This function indicates whether the socket was configured with a broadcast address. It is only valid for enabled UDP sockets. This can be used to determine whether a new socket should be created if a unicast response is desired.  
[SocketIsMulticast](<SocketIsMulticast.htm>) |  This function indicates whether the socket was configured with a mulitcast address. It is only valid for enabled UDP sockets. This can be used to determine whether a new socket should be created if a unicast response is desired.  
[SocketGetSenderIPAddress](<SocketGetSenderIPAddress.htm>) |  This function returns the IP address of the sender of a UDP. It is only valid for enabled UDP sockets. It can only be used in the SOCKETRECEIVE event for a UDP_SOCKET.   
  
Version:

SIMPL Version 2.10.00 or later

SIMPL+ Version 3.03.00 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Direct_Socket_Access/Direct_Socket_Access_Functions_Overview.htm*
