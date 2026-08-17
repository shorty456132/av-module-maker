# TCP Recommended Practices

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Recommended_Practices/TCP.htm

# TCP Recommended Practices

## TcpSocket

[Property Usage and Considerations](javascript:void(0))

#### .ReadTimeout

If the socket does not receive any data within the time, assigned in seconds, the socket will disconnect and call its `Timeout` EventHandler. Assigning a value of 0 will disable this behavior, which is the default value. After this occurs, the socket will attempt to reconnect if `.ReconnectTimeout` is greater than 0.

This property is useful for ensuring you are receiving a steady stream of data from the connected device.

This value should be greater than your poll rate to prevent unwanted timeouts.

#### .WriteTimeout

If the socket does not send any data within the time, assigned in seconds, the socket will disconnect and call its `Timeout` EventHandler. Assigning a value of 0 will disable this behavior, which is the default value. After this occurs, the socket will attempt to reconnect if `.ReconnectTimeout` is greater than 0.

This property is useful for ensuring you are sending a steady stream of data to the connected device.

This value should be greater than your poll rate to prevent unwanted timeouts.

#### .ReconnectTimeout

This property defines the time between reconnect attempts made by the socket, measured in seconds. Assigning a value of 0 will disable reconnect. The default value is 5 seconds.

A socket with `.ReconnectTimeout` greater than 0 will continually try to maintain its connection until `:Disconnect()` is called.

#### .IsConnected

This property is read-only and will return true if the socket is connected.

This property is useful to prevent calling `:Write()` when the socket is not connected.

```lua
function SendData(toSend)  
  if socket.IsConnected then   
    socket:Write(toSend)  
  else   
    print("Unable to send data, socket disconnected")  
  end   
end 
```

#### .BufferLength

This property is read-only and will return the length of the buffer, in bytes, as an integer.

This property is useful to determine if there is data to parse and how much.

[Events](javascript:void(0))

#### Connected

This event is called when the TcpSocket successfully connects to a server.

After this function is called, you may start logic for authentication or polling.

```lua
socket.Connected = function(sock)  
  print("Socket Connected")  
  SendData("Poll") -- send inital poll  
  -- optionally start a poll timer or other logic here  
end 
```

#### Reconnect

This event is called at each `.ReconnectTimeout` interval when the socket tries to reconnect to the server.

Typically, the only action to take when this event is triggered is a debug statement.

#### Closed

This event is called when a socket that was connected is closed.

This is the best place to reset variables, queues, and any other actions to prepare for a new connection.

#### Error

This event is called when there is an error relating to the socket connection.

Here are some error strings returned by this event:

* Empty String: Failed to connect
* *nodename nor servname provided, or not known*: Could not resolve hostname
* *non-recoverable failure in name resolution*: invalid hostname provided

#### Timeout

This event is called when a read or write timeout is triggered and the socket was closed.

`.Closed` will not be called in the event of a timeout.

Reset variables, queues, and any other actions to prepare for reconnection.

#### Data

This event is called when there is new data available in the socket buffer.

This is where you would read data from the buffer and parse appropriately.

The buffer is retained so not all data needs to be pulled from the buffer if a complete message was not received.

[Reading from the buffer](javascript:void(0))

[Whole buffer](javascript:void(0))

Read entire buffer

```lua
socket.Data = function(sock)  
  print("Socket received " .. sock.BufferLength .. " bytes")  
  local data = sock:Read(sock.BufferLength) -- read the entire buffer  
  if #data > 0 then -- ignore empty payloads  
    ParseData(data) -- parse the data in a seperate function  
  end   
end 
```

[Read until specific character](javascript:void(0))

Read until EOL char

```lua
socket.Data = function(sock)  
  print("Socket buffer has " .. sock.BufferLength .. " bytes")  
  local data = sock:ReadLine(TcpSocket.EOL.Custom,'\r') -- read until a carrige return \x0D  
  while data do -- if valid data was read loop until there is no more valid data  
    ParseData(data) -- parse the data in a seperate function  
    data = sock:ReadLine(TcpSocket.EOL.Custom,'\r') -- check for more data  
  end    
end 
```

[Local buffer](javascript:void(0))

Use local buffer

```lua
MyBuffer = ""  
  
socket.Data = function(sock)  
  print("Socket received " .. sock.BufferLength .. " bytes")  
  local data = sock:Read(sock.BufferLength) -- read the entire buffer  
  if #data > 0 then -- ignore empty payloads  
    MyBuffer = MyBuffer..data -- append data to local buffer  
    ProcessBuffer() -- process the buffer in a seperate function  
  end   
end 
```

## TcpSocketServer

[Setup and Helper Functions](javascript:void(0))

#### Define server and sockets table

Define a TcpServerSocket instance.

Define a table to store all active connections. This is not only to keep them from being disposed by the garbage collector, but also to iterate through for accessing active connections for broadcasts and closing connections when closing the server.

**Note:**  To avoid any possible issues with garbage collection, do not scope the server as a local.

Global definitions

```lua
server = TcpSocketServer.New()  
sockets = {}
```

#### function RemoveSocketFromTable(sock)

This is a helper function for finding and removing a socket from the sockets table mentioned above.

function RemoveSocketFromTable(sock)

```lua
function RemoveSocketFromTable(sock)  
  for k,v in pairs(sockets) do  
    if v == sock then   
      v:Disconnect() -- disconnect in case socket is still connected.  
      table.remove(sockets, k)   
      return  
    end  
  end  
end
```

#### function CloseServer()

This is a helper function to cleanly close the server and all active connections. It will iterate through the sockets table, mentioned above, close the socket, and dispose of it before closing the server itself.

function CloseServer()

```lua
function CloseServer()  
  for k,socket in pairs(sockets) do -- iterate through all active connections  
    socket:Disconnect() -- disconnect active connections, as they are not automatically closed when the server is closed  
    table.remove(sockets,k) -- dispose of the socket  
  end   
  server:Close() -- close the server to stop new incoming connections  
end 
```

[EventHandler for connected sockets](javascript:void(0))

One nuance of the TcpSocketServer is that sockets are already connected when the server's EventHandler is called. Also, sockets won't generate a 'Reconnect' event.

There are only two things to do within the EventHandler: parse the buffer and clean up the socket after it closes.

socket EventHandler

```lua
function SocketHandler(sock, event) -- EventHandler for active connections  
  if event == TcpSocket.Events.Data then  
    -- handle incoming data here  
    data = sock:Read(sock.BufferLength) -- socket buffer works the same as a standard TcpSocket  
    print("RX", #data, data)   
    if data:find("^Poll") then -- as an example if you receive a string starting with 'Poll'  
      SendAll(sock) -- Call a function to send data to only the socket that requested it  
    end   
  elseif event == TcpSocket.Events.Closed or   
         event == TcpSocket.Events.Error or  
         event == TcpSocket.Events.Timeout then  
    print("removing connection from "..sock.PeerAddress)  
    RemoveSocketFromTable(sock)-- remove reference of socket from table so it's available for garbage collection  
  end  
end
```

[EventHandler for Incoming Connections](javascript:void(0))

The server's EventHandler will be called when there is a new connection to handle.

This is where you add new connections to the sockets table, assign an EventHandler to them, and optionally send an initial response to the connecting socket.

Like standard TcpSockets, you can also define a ReadTimeout and/or a WriteTimeout. A ReadTimeout here would be useful for severing connections that become idle for too long.

Server EventHandler

```lua
server.EventHandler = function(SocketInstance) -- the properties of this socket instance are those of the TcpSocket library  
  -- SocketInstance.ReadTimeout = 10 -- Optional ReadTimeout  
  print( "Got connection from ", SocketInstance.PeerAddress ) -- you can access the address of incomming connections using .PeerAddress  
  table.insert(sockets, SocketInstance) -- add the socket to the sockets table  
  SocketInstance.EventHandler = SocketHandler -- assign an EventHandler  
  SendAll(SocketInstance) -- Optionally send an initial response to the socket  
end
```

[Start Listening](javascript:void(0))

When you call `:Listen(port)`, it will listen on the specified port, if available, on all interfaces. There is no current way to limit a TcpSocketServer from listening only on a single specific interface.

Only one TcpSocketServer per port may be active within a design at a time. If you try to listen on an unavailable port, you will get a Lua error, `Could not bind to port`. It is recommended to wrap the `:Listen(port)` call in a pcall statement.

Note that a single TcpSocketServer can listen to multiple ports at the same time; therefore, if you are changing the port your server is listening to, then you will need to cleanly close the server and any active connections first before listening to the new port.

```lua
function Listen()  
  CloseServer() -- cleanly close the server and active connections  
  if Controls.Enable.Boolean then -- Optionally Open/Close the server with a Toggle Button  
    local success, err = pcall(function() -- wrap the listen in a pcall in case port is already in use  
      server:Listen(Controls.Port.Value)  
    end)  
    if success then -- server is listening  
      print("Listening on port ".. tostring(math.floor(Controls.Port.Value)))  
    else -- server couldn't listen, print the error  
      print("Failure to listen to port "..tostring(math.floor(Controls.Port.Value))..":",err)  
    end   
  end   
end   
Controls.Enable.EventHandler = Listen  
Controls.Port.EventHandler = Listen  
Listen()
```

## Considerations for Core redundancy

With redundant Cores, the address will change depending on the active Core. This is particularly important for a TCP Server.
