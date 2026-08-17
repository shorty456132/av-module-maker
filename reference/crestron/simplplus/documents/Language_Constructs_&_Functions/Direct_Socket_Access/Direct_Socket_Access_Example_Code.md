# Direct Socket Access Example Code  
  
#DEFINE_CONSTANT FALSE 0

#DEFINE_CONSTANT TRUE 1

//#DEFINE_CONSTANT INCLUDE_NEW_CODE 1

DIGITAL_INPUT diStartClient;

DIGITAL_INPUT diClientReconnectEnable;

DIGITAL_INPUT diEnableServer;

DIGITAL_INPUT diEnableUDP;

ANALOG_INPUT aiClientPortNumber;

ANALOG_INPUT aiServerPortNumber;

ANALOG_INPUT aiUDP_PortNumber;

STRING_INPUT siClientIPAddress[256];

STRING_INPUT siServerIPAddress[256];

STRING_INPUT siUDP_IPAddress[256];

STRING_INPUT siClientTx[256];

STRING_INPUT siServerTx[256];

STRING_INPUT siUDP_Tx[256];

DIGITAL_OUTPUT doClientConnected;

DIGITAL_OUTPUT doServerConnected;

ANALOG_OUTPUT aoClientStatus;

ANALOG_OUTPUT aoServerStatus;

STRING_OUTPUT soClientRx;

STRING_OUTPUT soServerRx;

STRING_OUTPUT soUDP_Rx;

TCP_CLIENT MyClient[1024];

TCP_SERVER MyServer[1024];

UDP_SOCKET MyUDP[1024];

// Client Example Code

PUSH diStartClient

{

SIGNED_INTEGER status;

status = SocketConnectClient (MyClient, siClientIPAddress, aiClientPortNumber, diClientReconnectEnable);

if (status < 0)

Print("Error connecting socket to address %s on port %d",

SiClientIPAddress, aiClientPortNumber);

}

RELEASE diStartClient

{

SIGNED_INTEGER status;

status = SocketDisconnectClient (MyClient);

if (status < 0)

Print("Error disconnecting socket to address %s on port %d",

SiClientIPAddress, aiClientPortNumber);

}

SOCKETCONNECT MyClient

{

SIGNED_LONG_INTEGER PortNumber;

SIGNED_INTEGER LocalStatus;

STRING RemoteIPAddress[20];

STRING RequestedAddress[256];

doClientConnected = 1;

LocalStatus = SocketGetAddressAsRequested(MyClient, RequestedAddress);

if (LocalStatus < 0)

Print("Error getting remote ip address. %d\n", LocalStatus);

Print("OnConnect: Connect call to %s successful\n", RequestedAddress);

PortNumber = SocketGetPortNumber(MyClient);

if (PortNumber < 0)

Print("Error getting client port number. %ld\n", PortNumber);

LocalStatus = SocketGetRemoteIPAddress(MyClient, RemoteIPAddress);

if (LocalStatus < 0)

Print("Error getting remote ip address. %d\n", LocalStatus);

Print("OnConnect: Connected to port %ld on address %s\n",

PortNumber, RemoteIPAddress);

SocketSend(MyClient, "This is sent when the socket starts.");

}

SOCKETDISCONNECT MyClient

{

doClientConnected = 0;

if (diStartClient)

Print("Socket disconnected remotely");

Else

Print("Local disconnect complete.");

}

SOCKETSTATUS MyClient

{

SIGNED_INTEGER Status;

Status = SocketGetStatus();

aoClientStatus = Status;

Print("The SocketGetStatus returns: %d\n", Status);

Print("The MyClient.SocketStatus returns: %d\n", MyClient.SocketStatus);

}

SOCKETRECEIVE MyClient

{

if (Len(MyClient.SocketRxBuf) < 256)

Print("Rx: %s", MyClient.SocketRxBuf);

// for now, send to serial output and clear buffer

soClientRx = MyClient.SocketRxBuf;

ClearBuffer(MyClient.SocketRxBuf);

}

CHANGE siClientTx

{

signed_integer iStatus;

iStatus = SocketSend(MyClient, siClientTx );

if (iStatus < 0)

Print("Error Sending to MyClient: %d\n", iStatus);

}

// Server Example code

PUSH diEnableServer

{

SIGNED_INTEGER status;

status = SocketServerStartListen(MyServer, siServerIPAddress, aiServerPortNumber);

if (status < 0)

Print("Error listening to %s on port %u (status: %d)", siServerIPAddress, aiServerPortNumber, status);

}

RELEASE diEnableServer

{

SIGNED_INTEGER status;

status = SocketServerStopListen(MyServer);

if (status < 0)

Print("Error stopping server (status: %d)", status);

}

SOCKETCONNECT MyServer

{

SIGNED_INTEGER PortNumber;

doServerConnected = 1;

Print("OnConnect: input buffer size is: %d\n", Len(MyServer.SocketRxBuf));

SocketSend(MyServer, "This is sent when the socket starts.");

}

SOCKETDISCONNECT MyServer

{

doServerConnected = 0;

if (diEnableServer)

Print("Socket disconnected remotely");

Else

Print("Local disconnect complete.");

}

SOCKETSTATUS MyServer

{

SIGNED_INTEGER Status;

Status = SocketGetStatus();

aoServerStatus = Status;

Print("The SocketGetStatus returns: %d\n", Status);

Print("The MyServer.SocketStatus returns: %d\n", MyServer.SocketStatus);

}

SOCKETRECEIVE MyServer

{

if (Len(MyServer.SocketRxBuf) < 256)

Print("Rx: %s", MyServer.SocketRxBuf);

// for now, send to serial output and clear buffer

soServerRx = MyServer.SocketRxBuf;

ClearBuffer(MyServer.SocketRxBuf);

}

CHANGE siServerTx

{

signed_integer iStatus;

iStatus = SocketSend(MyServer, siServerTx );

if (iStatus < 0)

Print("Error Sending to MyServer: %d\n", iStatus);

}

// UDP Example code

PUSH diEnableUDP

{

SIGNED_INTEGER status;

status = SocketUDP_Enable(MyUDP, siUDP_IPAddress, aiUDP_PortNumber);

if (status < 0)

Print("Error listening to %s on port %d", siUDP_IPAddress, aiUDP_PortNumber);

}

RELEASE diEnableUDP

{

SIGNED_INTEGER status;

status = SocketUDP_Disable (MyUDP);

if (status < 0)

Print("Error listening on port %d", aiServerPortNumber);

}

SOCKETRECEIVE MyUDP

{

SIGNED_INTEGER IsBroadcast;

SIGNED_INTEGER IsMulticast;

SIGNED_INTEGER LocalStatus;

STRING SenderIPAddress[32];

IsBroadcast = SocketIsBroadcast(MyUDP);

if (IsBroadcast < 0)

Print("IsBroadcast returned error: %d\n", IsBroadcast);

IsMulticast = SocketIsMulticast(MyUDP);

if (IsMulticast < 0)

Print("IsMulticast returned error: %d\n", IsMulticast);

LocalStatus = SocketGetSenderIPAddress(MyUDP, SenderIPAddress);

if (LocalStatus < 0)

Print("SocketGetSenderIPAddress returned error: %d\n", LocalStatus);

if (IsBroadcast)

Print("Broadcast data received from %s\n", SenderIPAddress);

else if (IsMulticast)

Print("Multicast data received from %s\n", SenderIPAddress);

else

Print("Unicast data received from %s\n", SenderIPAddress);

if (Len(MyUDP.SocketRxBuf) < 256)

Print("Rx: %s", MyUDP.SocketRxBuf);

// for now, send to serial output and clear buffer

soUDP_Rx = MyUDP.SocketRxBuf;

ClearBuffer(MyUDP.SocketRxBuf);

}

CHANGE siUDP_Tx

{

signed_integer iStatus;

iStatus = SocketSend(MyUDP, siUDP_Tx );

if (iStatus < 0)

Print("Error Sending to MyUDP: %d\n", iStatus);

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Direct_Socket_Access/Direct_Socket_Access_Example_Code.htm*
