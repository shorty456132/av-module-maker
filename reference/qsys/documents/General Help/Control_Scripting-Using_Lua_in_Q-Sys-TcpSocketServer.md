# TcpSocketServer

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/TcpSocketServer.htm

# TcpSocketServer

The TcpServer object allows Q-SYS Core processors to accept client TCP/IP connections from devices on the network.

[Overview](javascript:void(0))

TcpSocketServer is different from the [TcpSocket](TcpSocket.htm) library because of the inbound/waiting nature of a TCP server. TcpSocket generally allows Q-SYS to establish outgoing TCP client sessions to remote TCP servers. The TcpSocketServer library enables a script to create a TCP "listener" on a specific TCP port. This listener isn't the individual TCP socket itself â it "emits" a unique TcpSocket instance whenever a remote TCP client connects to the listen port. Thus, the TcpSocketServer instance's EventHandler is where the specific incoming TCP socket connection is granted a unique socket instance (the argument of the TcpSocketServer's EventHandler function). The EventHandler target function for this new socket instance will be defined as an anonymous function or (more likely) as a reference to a separate socket event handling function.

**Note:** If multiple incoming socket connections are made, a separate socket instance (and EventHandler) are created by the Lua runtime engine for each connection and all socket transactions are handled by each socket connection's separate EventHandler instances (which are assigned only as necessary). The IP address of the connecting device will be available in each sock instance, see [.PeerAddress](TcpSocket.htm#PeerAddress) for more information.

[Methods](javascript:void(0))

[:New](javascript:void(0))

Static class method. Creates a new instance of the TcpServer class.

### Syntax

`New()`

### Arguments

None.

### Response

The newly created TcpServer.

[:Listen](javascript:void(0))

Opens the TcpServer on the specified TCP port on all network interfaces.

### Syntax

`Listen (port)`

### Arguments

*port* : Integer. The port to use for listening for connections.

### Response

The port will open and start listening for incoming connections.

[:Close](javascript:void(0))

Closes the TcpServer / disconnects the socket.

### Syntax

`Close()`

### Arguments

None.

### Response

N/A

[Properties](javascript:void(0))

| Name | Arguments | Description |
| --- | --- | --- |
| .EventHandler | Signature of function is 'function(socket, event)' | Function called on any incoming socket event. See definition of 'event' in the table below.  The arguments for this EventHandler are documented in the EventHandler definition of [TcpSocket Properties](TcpSocket.htm#Properties). |

[Example](javascript:void(0))

**Note:** The EventHandler arguments and function names in this example were chosen to assist in understanding what is happening when a TCP socket connection occurs. These names are not special and can be changed in your own scripts.

```lua
server = TcpSocketServer.New()  
  
-- table to store connected client sockets  
-- this is required so the sockets don't  
-- get garbage collected since there aren't  
-- any other references to them in the script  
sockets = {}  
  
function RemoveSocketFromTable(sock)  
  for k,v in pairs(sockets) do  
    if v == sock then   
      table.remove(sockets, k)   
      return  
    end  
  end  
end  
   
  
function SocketHandler(sock, event) -- the arguments for this EventHandler are documented in the EventHandler definition of TcpSocket Properties  
  print( "TCP Socket Event: "..event )  
  if event == TcpSocket.Events.Data then  
    print( sock, sock:Read(sock.BufferLength) )  
  elseif event == TcpSocket.Events.Closed or  
         event == TcpSocket.Events.Error or  
         event == TcpSocket.Events.Timeout then  
    -- remove reference of socket from table so  
    -- it's available for garbage collection  
    RemoveSocketFromTable(sock)  
  end  
end  
   
server.EventHandler = function(SocketInstance) -- the properties of this socket instance are those of the TcpSocket library  
  SocketInstance.ReadTimeout = 10  
  print( "Got connect", SocketInstance )  
  table.insert(sockets, SocketInstance)  
  SocketInstance.EventHandler = SocketHandler  
end  
  
server:Listen(1720) -- This listen port is opened on all network interfaces
```
