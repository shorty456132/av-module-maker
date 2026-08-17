# Compiler Error 1613

construct error: SocketGetSenderIPAddress can only be used with a SOCKETRECEIVE event.

SocketGetSenderIPAddress can only be used within the SOCKETRECEIVE event. It cannot be used inside any other declared function or event type.

The following are examples of this error:

SOCKETRECEIVE MyUDP

{

SIGNED_INTEGER Status;

STRING IPAddress[32];

Status = SocketGetSenderIPAddress(MyUDP, IPAddress ); // ok

}

SOCKETDISCONNECT MyUDP

{

SIGNED_INTEGER Status;

STRING IPAddress[32];

Status = SocketGetSenderIPAddress(MyUDP, IPAddress ); // error

}

Function MyFunc()

{

SIGNED_INTEGER Status;

STRING IPAddress[32];

Status = SocketGetSenderIPAddress(MyUDP, IPAddress ); // error

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1613.htm*
