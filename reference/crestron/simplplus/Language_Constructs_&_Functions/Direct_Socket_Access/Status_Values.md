# Status Values

The returned Status values of TCP_CLIENT, TCP_SERVER, and UDP_SOCKET connections can be found in the following table.

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

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Direct_Socket_Access/Status_Values.htm*
