# TcpSocket

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/TcpSocket.htm

# TcpSocket

The TcpSocket object allows Q-SYS cores to make client TCP/IP connections to devices on the network.

The functions in the v2 TcpSocket communication library allow an Event-Based scheme to simplify scripting. Also, the v2 TCP Socket functionality allows for connection monitoring and automatic reconnect, buffer searches and custom EOL sequences. Asynchronous callbacks are no longer necessary as the Event Handler functionality now takes care of that behind the scenes.

For an example of the how the Event-Handled TcpSocket functions, see "[Button to Send Text String to Simple TCP/IP Socket (v2)](#Button_)".

[Methods](javascript:void(0))

[:New()](javascript:void(0))  
Creates a new TcpSocket instance.  

**Note:** Do not scope your TcpSocket locally. This causes the object to be managed by Lua's garbage collector, which may lead to its removal even if it is still in use.

### Syntax

`:New()`

[:NewTls](javascript:void(0))  
Creates a new TCP socket instance that uses TLS.

**Note:** Do not scope your TcpSocket locally. This causes the object to be managed by Lua's garbage collector, which may lead to its removal even if it is still in use.

### Syntax

`:NewTls()`

[:Connect()](javascript:void(0))  
Attempts to connect to the specified ip/host name and port. The Connect() function should be considered as a means to start the process to open a socket.

### Syntax

`:Connect( ipAddress/hostname, port )`

### Arguments

*ipAddress/hostname*: The IP Address or FQDN (fully qualified domain name) which represents the remote host.

*port* : Integer, 0 - 65535. The connection port number on the remote host.

[:Disconnect()](javascript:void(0))  
Disconnects the socket.

### Syntax

`:Disconnect()`

[:Write()](javascript:void(0))  
Writes specified data to the socket. Calling Write() should be avoided until the socket triggers its "Connected" event. Raises error if socket is not connected.

### Syntax

`:Write( data )`

### Arguments

*data* : String. The data to write to the socket.

[:Read()](javascript:void(0))  
Attempts to read up to 'length' bytes from socket. These bytes are removed from the buffer, leaving any remaining bytes beyond the 'length' specified.

### Syntax

`:Read( length )`

### Arguments

*length* : Positive integer. The number of bytes of data to read from the socket buffer.

### Return Value

String containing the number of bytes requested or the number of bytes available, whichever comes first.

[:ReadLine()](javascript:void(0))  
Attempts to read a 'line' from the socket buffer. 'EOL' is defined in the table. 'custom' is an optional string only used by 'EOL.Custom'.

### Syntax

`:ReadLine( EOL, <custom> )`

### Arguments

*EOL*: The EOL name can be any of the types shown in the EOL table below.

*custom* : Used only if the EOL keyword is Custom. A string literal containing the custom end of line character combination to search for.

| TcpSocket.EOL Table | |
| --- | --- |
| Name | Description |
| Any | The end of line is any sequence of any number of carriage return and/or linefeed characters. This is the appropriate choice if the protocol uses simply a carriage return as the end of message. |
| CrLf | The end of the line is an optional carriage return, followed by a linefeed. (In other words, it is either a "\r\n" or a "\n".) This format is useful in parsing text-based Internet protocols, since the standards generally prescribe a "\r\n" line-terminator, but nonconformant clients sometimes use just "\n". |
| CrLfStrict | The end of a line is a single carriage return, followed by a single linefeed. (This is also known as "\r\n". The ASCII values are 0x0D 0x0A). |
| Lf | The end of a line is a single linefeed character. (This is also known as "\n". It is ASCII value is 0x0A.) |
| Null | The end of line is a single byte with the value 0âââan ASCII NUL. |
| Custom | The end of line is defined by the string passed into the ReadLine() method. |

### Return Value

Nil if the EOL was not found, otherwise returns the string up to the EOL sequence.

[:Search()](javascript:void(0))  
Searches the socket buffer for string 'str' (starting at integer 'start\_pos') and returns the index of where 'str' is found. 'start\_pos' defaults to 1.

### Syntax

`:Search( str, [start_pos] )`

### Arguments

*str*: The string to search for.

*start\_pos*: Integer. Optional. The index of where to start in the socket buffer. Default is index 1.

### Return Value

Nil if the search string was not found, otherwise returns the integer index of where the search string was found.

[Events](javascript:void(0))

| TcpSocket.Events Table | |
| --- | --- |
| Name | Description |
| Connected | The socket has connected to the remote host. |
| Reconnect | The socket is attempting to reconnect to the remote host |
| Data | There is new data available in the socket buffer |
| Closed | The socket was closed by the remote host |
| Error | The socket was closed due to error. The error argument to the EventHandler will have more information, which can be displayed if a variable was created to catch the error message. |
| Timeout | A read or write timeout was triggered and the socket was closed. |

[Properties](javascript:void(0))

| TcpSocket Properties | | |
| --- | --- | --- |
| Name | Notes | Description |
| .EventHandler | Signature of function is 'function(socket, event, err)' | Function called on any socket event. See definition of 'event' in the table below. |
| .ReadTimeout | Optional; Default is 0 ( disabled ) | Time, in seconds, to wait for data to be available on socket before raising an Error through the EventHandler. |
| .WriteTimeout | Optional; Default is 0 ( disabled ) | Time, in seconds, to wait for data write to complete before raising an Error through the EventHandler. |
| .ReconnectTimeout | Optional; Default is 5 seconds | Time in seconds to wait before attempting to reconnect. 0 disables automatic reconnect. |
| .IsConnected | Read-Only | Returns true if socket is connected |
| .BufferLength | Read-Only | Amount of data in buffer, in bytes |
| .PeerAddress | Read-Only | If a TcpSocket is being used as a client, then this field will be an empty string.  If a TcpSocket was created as a response to a connection request to TcpSocketServer, this field returns the connected clientâs IP.  Otherwise, a string representing a connection error. |

[Callbacks](javascript:void(0))

Optional callback functions may be defined instead of using the singular EventHandler. Depending upon the application, defining separate functions for each event may be preferable. The choice to use either a single EventHandler to capture all socket events or separate callback functions is up to the programmer. There is no need to change a functioning script because this new functionality exists and you may choose to never use it. But some programmers may feel that the callback method better matches their logical style.

| TcpSocket Callbacks | | |
| --- | --- | --- |
| Name | Function Signature | Description |
| .Connected | function( *tcpTable* )' | Assign a function which is called upon connection to remote host |
| .Reconnect | function( *tcpTable* )' | Assign a function which is called when socket is attempting to reconnect to the remote host |
| .Data | function( *tcpTable*)' | Assign a function which is called when there is new data available in the socket buffer |
| .Closed | function( *tcpTable* )' | Assign a function which is called when the socket is closed by the remote host |
| .Error | function( *tcpTable, error* )' | Assign a function which is called when the socket is closed due to error. The error argument in the function will contain more information, which can be displayed if a variable was created to catch the error message. |
| .Timeout | function( *tcpTable* )' | Assign a function which is called when a read or write timeout is triggered and the socket was closed. |

[Examples](javascript:void(0))

### Button to Send Text String to Simple TCP/IP Socket (v2)

This script automatically connects to the remote socket server. When a user presses a button, the script sends a text string. Any received text is displayed in the debug window if terminated with a <CR><LF>. The script will automatically attempt to reconnect after 5 seconds if the socket is closed,.

### Using Single EventHandler

```lua
address = "192.168.1.100"  
port = 1234  
sock = TcpSocket.New()  
sock.ReadTimeout = 0  
sock.WriteTimeout = 0  
sock.ReconnectTimeout = 5  
  
sendData = 'Hello\x0d\x0a'  
  
sock.EventHandler = function(sock, evt, err)  
  if evt == TcpSocket.Events.Connected then  
    print( "socket connected" )  
  elseif evt == TcpSocket.Events.Reconnect then  
    print( "socket reconnecting..." )  
  elseif evt == TcpSocket.Events.Data then  
    print( "socket has data" )  
    message = sock:ReadLine(TcpSocket.EOL.Any)  
    while (message ~= nil) do  
      print( "reading until CrLf got "..message )  
      message = sock:ReadLine(TcpSocket.EOL.Any)  
    end  
  elseif evt == TcpSocket.Events.Closed then  
    print( "socket closed by remote" )  
  elseif evt == TcpSocket.Events.Error then  
    print( "socket closed due to error", err )  
  elseif evt == TcpSocket.Events.Timeout then  
    print( "socket closed due to timeout" )  
  else  
    print( "unknown socket event", evt ) --should never happen  
  end  
end  
  
Controls.Inputs[1].EventHandler = function()  
  sock:Write(sendData)  
end  
  
sock:Connect(address, port)
```

### Using Separate Callback Functions

```lua
address = "192.168.1.100"  
port = 1234  
sock = TcpSocket.New()  
sock.ReadTimeout = 0  
sock.WriteTimeout = 0  
sock.ReconnectTimeout = 5  
  
sendData = 'Hello\x0d\x0a'  
  
sock.Connected = function(sock)  
  print("TCP socket is connected")  
end  
sock.Reconnect = function(sock)  
  print("TCP socket is reconnecting")  
end  
sock.Data = function(sock)  
  print("TCP socket has data:",sock:Read(sock.BufferLength) )  
end  
sock.Closed = function(sock)  
  print("TCP socket was closed by the remote end")  
end  
sock.Error = function(sock, err)  
  print("TCP socket had an error:",err)  
end  
sock.Timeout = function(sock, err)  
  print("TCP socket timed out",err)  
end  
  
Controls.Inputs[1].EventHandler = function()  
  sock:Write(sendData)  
end  
  
sock:Connect(address, port)
```

### Using TLS

```lua
local function readFile(path)  
  -- Open in binary to avoid newline/binary surprises for certs/keys  
  local f, err = io.open(path, "rb")  
  if not f then  
    err = ("io.open failed for %q: %s"):format(path, tostring(err))  
    error(err)  
    return nil, err  
  end  
  local content = f:read("*a")  
  f:close()  
  return content  
end   
local client_cert = readFile("media/TLS_Certificates/client.crt")  
local client_key = readFile("media/TLS_Certificates/client.key")  
local ca_cert = readFile("media/TLS_Certificates/ca.crt")  
-- local ca_cert = "fake cert bruh"  
-- local client_cert = "fake cert bruh"  
-- local client_key = "fake cert bruh"  
tlsSocket = TcpSocket:NewTls()  
-- Configure certificates  
tlsSocket.ClientCertData = client_cert  
tlsSocket.ClientKeyData = client_key  
tlsSocket.CACertData = ca_cert  
tlsSocket.ValidateCertificate = true   
address = "10.164.129.52"  
port = 5555  
tlsSocket.ReadTimeout = 0  
tlsSocket.WriteTimeout = 0  
tlsSocket.ReconnectTimeout = 5  
sendData = '~!@#$%^&*()_+{}|:"<>?`-=[];,./Â¬Î©âÃ§ââ«ËÂµâ¤â¥Ã·Â¿Â¡Ã¦ÃÃ°Ã¸ÏÅâââ'  
tlsSocket.Connected = function(tlsSocket)  
  print("TCP socket is connected")  
end  
tlsSocket.Reconnect = function(tlsSocket)  
  print("TCP socket is reconnecting")  
end  
tlsSocket.Data = function(tlsSocket)  
  print("TCP socket has data:",tlsSocket:Read(tlsSocket.BufferLength) )  
end  
tlsSocket.Closed = function(tlsSocket)  
  print("TCP socket was closed by the remote end")  
end  
tlsSocket.Error = function(tlsSocket, err)  
  print("TCP socket had an error:",err)  
end  
tlsSocket.Timeout = function(tlsSocket, err)  
  print("TCP socket timed out",err)  
end  
Controls.Control_1.EventHandler = function()  
  tlsSocket:Write(sendData)  
end  
tlsSocket:Connect(address, port)
```
