# Compiler Error 1611

construct error: Invalid Structure type. Expected Structure(s): '<identifier>'

An invalid structure type was encountered within a construct.

The following are examples of this error:

ANALOG_INPUT AnlgIn;

TCP_CLIENT tcpClient[1024];

TCP_SERVER tcpServer[1024];

UDP_SOCKET udpSocket[1024];

CONNECT tcpClient // ok

{

}

DISCONNECT tcpServer // ok

{

}

RECEIVE udpSocket // ok

{

}

CONNECT AnlgIn // error – AnlgIn is not a socket type

{

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1611.htm*
