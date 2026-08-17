# Compiler Error 1317

construct error: Declaration cannot be declared as Nonvolatile: '<identifier>'

A variable was found trying to be declared with the NONVOLATILE keyword.

The following are examples of this error:

NONVOLATILE DIGITAL_INPUT di; // error

NONVOLATILE TCP_CLIENT tcpClient[1024]; // error

NONVOLATILE TCP_SERVER tcpServer[1024]; // error

NONVOLATILE INTEGER i; // ok

NONVOLATILE INTEGER str[10]; // ok

VOLATILE UDP_SOCKET udpSocket[1024]; // ok – VOLATILE is the

// default type

VOLATILE DIGITAL_INPUT di; // ok

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1317.htm*
