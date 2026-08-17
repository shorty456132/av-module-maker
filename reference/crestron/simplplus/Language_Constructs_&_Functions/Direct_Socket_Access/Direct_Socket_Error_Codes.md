# Direct Socket Error Codes

The error codes that can be returned by Direct Socket Access functions are listed in the following table.

Keyword |  Value |  Connection Status  
---|---|---  
SOCKET_INVALID_SOCKET  |  -1 |  Client, Server or UDP variable not a TCP/IP or UDP variable.  
SOCKET_NO_CONNECT_TASK  |  -2 |  Could not create the connection task  
SOCKET_NO_DNS_RESOLVE  |  -3 |  Could not resolve address  
SOCKET_INVALID_PORT_NUMBER |  -4 |  Port not in range of 0-65535.  
SOCKET_NOT_CONNECTED  |  -5 |  No connection has been established  
SOCKET_STRING_TOO_SMALL  |  -6 |  Not enough room in string parameter to hold IP address.  
SOCKET_CLIENT_CONNECTED  |  -7 |  Connecting a client that is already connected.  
SOCKET_CLIENT_CONNECT_IN_PROGRESS  |  -8 |  Trying to connect a client that is already attempting a connection.  
SOCKET_ETHERNET_NOT_INITIALIZED  |  -9 |  Trying to connect a client when Ethernet is not fully initialized.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Direct_Socket_Access/Direct_Socket_Error_Codes.htm*
