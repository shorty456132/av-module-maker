# Compiler Error 1315

construct error: Socket receive buffer size missing: '<identifier>'

The receiving buffer size was not specified within the socket declaration. All socket declarations must contain a buffer size.

The following are examples of this error:

TCP_CLIENT tcpClient[1024]; // ok

TCP_SERVER tcpServer[1024]; // ok

UDP_SOCKET udpSocket[1024]; // ok

TCP_CLIENT tcpClient2; // error

TCP_SERVER tcpServer2; // error

UDP_SOCKET udpSocket2; // error

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1315.htm*
