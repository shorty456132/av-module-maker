# WebSocket

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/lua_web_socket.htm

# WebSocket

WebSocket enables two-way communication between a client running code in a controlled environment to a remote host that has opted-in to communications from that code. The security model used for this is the origin based security model commonly used by web browsers. WebSocket consists of an opening handshake followed by basic message framing, layered over TCP. The goal of this technology is to provide a mechanism for browser-based applications that need two-way communication with servers that does not rely on opening multiple HTTP connections.

[Usage](javascript:void(0))

To use WebSocket, add the following line to your script:

**Note:** Do not scope your WebSocket locally. This causes the object to be managed by Lua's garbage collector, which may lead to its removal even if it is still in use.

`ws = WebSocket.New`

### Example

```lua
ws = WebSocket.New()  
print(ws)
```

### Debug Output

```lua
2023-03-28T14:37:45.288	Starting Script
2023-03-28T14:37:45.288 websocket
```

[function ws:Connect()](javascript:void(0))

Connect to host with given protocol (`ws` or `wss`) to URL and port with optional sub-protocol.

### Syntax

`ws:Connect(protocol, host, url, port, <sub-protocol>,``<headers>``)`

### Arguments

*protocol*: Connects to client with given protocol.

* `ws:Connect` - insecure, equivalent to `http`

* `wss:Connect` - secure, equivalent to `https`

*host*: Connects to client using client host.

*url*: Connects to client using client URL.

*port*: Connects to client with given port.

*sub-protocol*: (Optional) Connects to client with given sub-protocol.

*<headers>*: Connects to client using HTTP headers for client authentication.

* The `<headers>` parameter in the `ws:Connect()` function allows you to include custom HTTP headers for client authentication. These headers can be used for various purposes, such as passing authentication tokens or other relevant information.
* When connecting to a WebSocket server, you can include additional headers in the connection request. These headers are typically used for authentication, authorization, or other custom requirements.

### Example

Letâs say you want to connect to a WebSocket server with the following details:

* Protocol: Secure (wss)
* Host: `example.com`
* URL: `/my-websocket-endpoint`
* Port: `443`
* Sub-protocol: None (optional)
* Custom headers: Include an authentication token in the headers

**Note:** Remember to replace "`my-auth-token`" and "`SomeValue`" with actual values relevant to your use case. The `headers` table allows you to customize the connection by adding any necessary HTTP headers.

```lua
ws = WebSocket.New()   
protocol = "wss"  
host = "example.com"  
url = "/my-websocket-endpoint"  
port = 443  
sub_protocol = nil  -- No specific sub-protocol  
headers = {  
    ["Authorization"] = "Bearer my-auth-token",  
    ["Custom-Header"] = "SomeValue"  
}  
  
ws:Connect(protocol, host, url, port, sub_protocol, headers)
```

[Included Headers](javascript:void(0))

|  |  |
| --- | --- |
| `pragma` | `no-cache` |
| `cache-control` | `no-cache` |
| `host` | `<host>` |
| `upgrade` | `websocket` |
| `Upgrade` | `Upgrade` |
| `sec-websocket-key` | `<key>` |
| `sec-websocket-version` | `13` |

[function ws:Write()](javascript:void(0))

Sends message to server.

### Syntax

ws:Write(*message*, <isBinary>)

### Arguments

*message*: Write the message you wish to send to the server.

*<isBinary>*: If `true` is used as argument, write will be *binary*. If `false` is used write will be *ascii*.

[function ws:Close()](javascript:void(0))

Closes the connection to the server.

### Syntax

ws:Close()

[ws.Connected()](javascript:void(0))

Callback called when WebSocket is connected.

### Syntax

ws:Connected = function(*ws*)

### Arguments

*ws*: Connected WebSocket.

### Examples

```lua
ws.Connected = function()  
  print("Connected")  
  ws:Write("Hey!")  
end
```

[ws.Data()](javascript:void(0))

Callback called when a new message is received by the WebSocket.

### Syntax

ws:Data = function(*ws*, `data`)

### Arguments

*ws*: Connected WebSocket.

*data*: Data received in the WebSocket message.

### Examples

```lua
ws.Data = function( ws, data)  
  print("Data", data)  
end
```

[ws.Error()](javascript:void(0))

Callback called when an error occurs on the WebSocket.

### Syntax

ws:Error = function(*ws*, `err`)

### Arguments

*ws*: Connected WebSocket.

*err*: Callback error received.

### Examples

```lua
ws.Error = function( ws, err)  
  print("Error", err)  
end 
```

[ws.Closed()](javascript:void(0))

Callback called when the WebSocket is closed.

### Syntax

ws:Closed = function(*ws*)

### Arguments

*ws*: Connected WebSocket.

### Examples

```lua
ws.Closed = function()  
  print("closed")  
end 
```

[ws:Ping()](javascript:void(0))

Ping is used to keep a WebSocket connection alive.

### Syntax

ws:Ping = function(*ws*)

### Arguments

*ws*: Connected WebSocket.

### Events

ws.Pong = function(*ws*)

### Examples

```lua
ws = WebSocket.New()  
pingTimer = Timer.New()  
  
pingTimer.EventHandler = function()  
  ws:Ping()  
end  
  
ws.Connected = function(ws)  
  print("Connected")  
    
  -- send ping every 10 seconds  
  pingTimer:Start(10)  
    
  ws:Write("Hey!")  
end  
  
ws.Error = function( ws, err)  
  pingTimer:Stop()  
  print("Error", err)  
end   
  
ws.Closed = function(ws)  
  pingTimer:Stop()  
  print("closed")  
end   
  
ws.Data = function( ws, data)  
  print("Data", data)  
end  
  
ws:Connect("wss", "192.168.0.201", "/qrc", 443)
```
