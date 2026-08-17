# UDPSocket

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/UdpSocket.htm

# UDPSocket

Use the UdpSocket commands to send and receive data over a UdpSocket connection.

[Methods](javascript:void(0))

[.New](javascript:void(0))

Static class method. Creates a new instance of the UdpSocket class.

**Note:** Do not scope your UdpSocket locally. This causes the object to be managed by Lua's garbage collector, which may lead to its removal even if it is still in use.

### Syntax

`UdpSocket.New()`

### Arguments

None.

### Returns

UdpSocket object.

[:Open](javascript:void(0))

Opens the UdpSocket. Optionally bind to a local IP and Port (either or both).

### Syntax

`Open( <IP>, <Port> )`

### Arguments

*IP* : String. Optional. The local IP address that the connection should use. If not specified, UDP would be sent from a single IP address based on the connected LAN ports. This selection is made based on network conditions. The LAN connection outputting UDP data may change as LAN connections to the Core are changed. Makes no difference in receiving.

*Port* : Integer, 0 - 65535. Optional. The local Port that the connection should use. If not specified, the port is selected by the system.

[:Close](javascript:void(0))

Closes an open UdpSocket on a specified port.

### Syntax

`Close( )`

### Arguments

None.

[:Send](javascript:void(0))

Sends data to IP Address and port.

### Syntax

`Send( IP_Address, Port, Data )`

### Arguments

*IP\_Address* : String. IP Address to send to.

*Port* : Integer, 0 - 65535. The port to send to.

*Data* : String, up to 65535 bytes. Binary data, represented in Lua as a string.

[:JoinMulticast](javascript:void(0))

Joins the multicast address, binding to local IP.

**Note:** If there are multiple NICs present (failover systems and redundant systems), you need to specify the local IP for the `JoinMulticast()` method to ensure proper recovery on system stop/start up.

### Syntax

`JoinMulticast( Address, <Local_IP>)`

### Arguments

*Address* : String. Multicast IP Address to receive packets from.

*Local\_IP* : String. Local IP address to bind to. This is an optional argument for single NIC systems, otherwise QDS will randomly choose a NIC to receive packets from and might not be the correct one in a multi-NIC system.

[Properties](javascript:void(0))

| Name | Description |
| --- | --- |
| EventHandler | Function to call when UDP packet is received. The signature of function is 'function(socket, data)'  data is a table consisting of the following:   * Address - string * Port - integer * Data - data payload |
| .MulticastTtl | A number from 0 to 255. Default is 1.  Changes the multicast time-to-live (TTL) value in multicast UDP packets sent from Lua.  The TTL value can be set before the socket is opened and can also be changed dynamically while the socket is in use.  See [Example 4: Change the multicast TTL value](#Example2). |

[Callbacks](javascript:void(0))

Optional callback functions may be defined instead of using the singular EventHandler. Depending upon the application, defining separate functions for each event may be preferable. The choice to use either a single EventHandler to capture all socket events or separate callback functions is up to the programmer. There is no need to change a functioning script because this new functionality exists and you may choose to never use it. But some programmers may feel that the callback method better matches their logical style.

| Name | Function Signature | Description |
| --- | --- | --- |
| .Data | function( *udpTable, data* )'  data is a table consisting of the following:   * Address - string * Port - integer * Data - data payload | Assign a function which is called when data is received. See [Example 3: Using the UdpSockets Callback method](#Example). |

[Examples](javascript:void(0))

[Example 1: Open connection, printout Multicast UDP packets received.](javascript:void(0))

```lua
-- receiving multicast  
-- (Port 2468 is the port for the Q-SYS Core's IO device queries sent every two seconds)  
udp = UdpSocket.New()  --Create new UDP object  
   
udp.EventHandler = function(udp, packet)  
    print( packet.Address, packet.Port, packet.Data )  
end  
   
udp:Open( "192.168.1.100", 2468 ) -- IP address is optional  
udp:JoinMulticast("224.0.23.175") -- Sends a multicast join report for the multicast address
```

[Example 2: Send a UDP message](javascript:void(0))

```lua
local udp = UdpSocket.New()  
   
udp:Open()  
udp:Send(  
    "224.0.23.175",  
    2467,  
    "<QDP><query_ref>device.ioframe.*</query_ref></QDP>" )
```

[Example 3: Using the UdpSockets Callback method](javascript:void(0))

```lua
udp = UdpSocket.New()  --Create new UDP object  
   
udp.Data = function(udp, packet)  
    print( packet.Address, packet.Port, packet.Data )  
end  
   
udp:Open( "192.168.1.100", 2468 ) -- IP address is optional
```

[Example 4: Change the multicast TTL value](javascript:void(0))

```lua
udp = UdpSocket.New()  
udp.MulticastTtl = 10  
udp:Open()  
  
udp:Send( "224.0.23.175", 1234, "THIS IS A TEST" )
```

[Troubleshooting](javascript:void(0))

[Originating UDP Port Receives Responses from UDP-Enabled Remote Devices](javascript:void(0))

Because of the nature of UDP/IP, there may only be one script listening to a port on a given IP address. But another script may use that same port on a different IP address (NIC). The expected behavior of UDP-enabled remote devices is to send any responses back to the originating UDP port. The port you specify in the `Send()` method is not necessarily the one you assign with the `Open()` method (although they frequently match). Assuming you had many identical devices to control (via the same or separate scripts) that all used the same UDP port number for their remote interfaces, you could have many scripts, each controlling another device on the same remote UDP port. However, on the Q-SYS end, if you expect to also handle UDP responses, you need to be careful to choose unique UDP ports for the `Open()` method to ensure incoming packets go to the correct script.

Unfortunately, some remote interfaces always send UDP responses to the same UDP port, regardless of the originating port on the opposite end (Q-SYS in this case). In those rare cases, you have no alternative but to write a single script to receive all responses from all devices and then farm them out to other scripts for final processing, once a determination has been made where the packet originated. This determination is typically done by parsing some type of ID from the received packet. At this point this receiver script would have to send the data to a script associated with the specific instance of remote product.

**Note:** One exception to this is when receiving multicast UDP packets. Those are sent to the same port on every NIC on a Layer 2 network, unless using IGMP Snooping or similar multicast filtering scheme. The above Multicast Receive example allows you to see Q-SYS Discovery Protocol (QDP) packets on your network.

[Receiving UDPSocket for Multicast Traffic](javascript:void(0))

If you open a UdpSocket component and assign an IP of the host interface and then use that connection to receive multicast traffic through it, it will work in Emulate Mode, but does not work when the same code is pushed to a Core until you bind the UdpSocket to the multicast group and join the multicast group.

#### Running on a Core (Linux)

* For traffic on a specific multicast address, the receiving socket needs to bind to the multicast group and port.
* Can also bind the wildcard IP address (INADDR\_ANY - pass nil to `Open()` call) for receiving data from multiple multicast addresses.
* Must also join the multicast group `JoinMulticast()`.

#### Running Emulate mode (Windows)

* Receiving socket needs to bind to the local interface IP and port.
* Can also bind the wildcard IP address (INADDR\_ANY - pass nil to `Open()` call) for receiving data from multiple multicast addresses.
* Must also join the multicast group `JoinMulticast()`.
