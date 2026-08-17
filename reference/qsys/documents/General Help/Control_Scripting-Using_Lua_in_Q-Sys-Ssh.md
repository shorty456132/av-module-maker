# Ssh

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/Ssh.htm

# Ssh

The Ssh object allows Q-SYS cores to make secure client connections to devices on the network. It is very similar to [TcpSocket](TcpSocket.htm), but requires additional connection arguments (host, port, user, password). Unlike TcpSocket, a standard, unified event handler function is not supported. Additionally, compared to TcpSocket, there is a LoginFailed event handler that is called if login credentials are incorrect.

**Note:** Our implementation supports the following public key algorithms: ssh-ed25519, ecdsa-sha2-nistp256, ecdsa-sha2-nistp384, ecdsa-sha2-nistp521, ssh-rsa, rsa-sha2-512, rsa-sha2-256,ssh-dss.

[Methods](javascript:void(0))

[Ssh.New](javascript:void(0))

Creates a new SSH instance.

**Note:** Do not scope your Ssh locally. This causes the object to be managed by Lua's garbage collector, which may lead to its removal even if it is still in use.

### Syntax

Ssh.New()

[:Connect](javascript:void(0))

Attempts to connect using the specified host address, port, and credentials.

### Syntax

:Connect("*host*", *port*, "*user*", "*password*")

### Arguments

*host* : String. The IP Address or FQDN (fully qualified domain name) which represents the remote host.

*port* : Integer, 0 - 65535. The connection port number on the remote host.

*user* : String. The connection user name, in quotes.

*password* : String. The connection password, in quotes.

**Note:** When using PKI authentication, the password field is ignored but currently required. See [PKI Authentication Methods](#PKI).

[:Disconnect](javascript:void(0))

Disconnects the socket.

### Syntax

:Disconnect()

[:Write](javascript:void(0))

Writes specified data to the socket. Raises error if socket is not connected.

### Syntax

:Write(*data*)

### Arguments

*data* : String. The data to write to the socket.

[:Read](javascript:void(0))

Attempts to read up to 'length' bytes from socket. These bytes are removed from the buffer, leaving any remaining bytes beyond the 'length' specified.

### Syntax

:Read(*length*)

### Arguments

*length* : Positive integer. The number of bytes of data to read from the socket buffer.

### Return Value

Returns a string containing the number of bytes requested or the number of bytes available, whichever comes first. Returns Nil if the buffer is empty.

[:ReadLine](javascript:void(0))

Attempts to read a 'line' from the socket buffer.

### Syntax

:ReadLine(TcpSocket.EOL.*keyword*, <*custom*>)

### Arguments

TcpSocket.EOL.*keyword* : The EOL keyword can be any of the types shown in the EOL table below.

*custom* : Used only if the EOL keyword is **Custom**. A string literal containing the custom end of line character combination to search for.

| TcpSocket.EOL Keywords | Description |
| --- | --- |
| Any | The end of line is any sequence of any number of carriage return and/or linefeed characters. This is the appropriate choice if the protocol uses simply a carriage return as the end of message. |
| CrLf | The end of the line is an optional carriage return, followed by a linefeed. (In other words, it is either a "\r\n" or a "\n".) This format is useful in parsing text-based Internet protocols, since the standards generally prescribe a "\r\n" line-terminator, but nonconformant clients sometimes use just "\n". |
| CrLfStrict | The end of a line is a single carriage return, followed by a single linefeed. (This is also known as "\r\n". The ASCII values are 0x0D 0x0A). |
| Lf | The end of a line is a single linefeed character. (This is also known as "\n". It is ASCII value is 0x0A.) |
| Null | The end of line is a single byte with the value 0âââan ASCII NUL. |
| Custom | The end of line is defined by the string passed into the ReadLine() method. |

### Return Value

Nil if the EOL was not found, otherwise returns the string up to the EOL sequence.

[:Search](javascript:void(0))

Searches the socket buffer for string 'str' (starting at integer 'start\_pos') and returns the index of where 'str' is found. 'start\_pos' defaults to 1.

### Syntax

:Search(*str*, [*start\_pos*])

### Arguments

*str* : The string to search for.

*start\_pos* : Integer. Optional. The index of where to start in the socket buffer. Default is index 1.

### Return Value

Nil if the search string was not found, otherwise returns the integer index of where the search string was found.

[PKI Authentication Methods](javascript:void(0))

Use these methods when communicating with a client that requires PKI-based authentication.

[ssh.PublicKey](javascript:void(0))

The public key must be in SSH-format.

### Syntax

ssh.PublicKey = "<algorithm> <key> <comment>"

### Example

```lua
ssh.PublicKey = "ssh-ed12345-cert-v01@openssh.com AAAAIHNza1234....
```

[ssh.PrivateKey](javascript:void(0))

The private key must be in OpenSSL PEM format.

### Syntax

ssh.PrivateKey = [[-----BEGIN OPENSSH PRIVATE KEY----- <key> -----END OPENSSH PRIVATE KEY-----]]

### Example

```lua
ssh.PrivateKey = [[-----BEGIN OPENSSH PRIVATE KEY-----  
b3BlbnNza12341234EAAAAACmFlczI1Ni1jYmMAAAAGYmNyeXB0AAAAGAAAABA+0VY3ZM  
...  
..  
..  
-----END OPENSSH PRIVATE KEY-----]]
```

[ssh.PrivateKeyPassword](javascript:void(0))

The password used in conjunction with a private key (if the private key is password-protected).

### Syntax

ssh.PrivateKeyPassword = "<password>"

### Example

```lua
ssh.PrivateKeyPassword = "SecretDontTellAnyone"
```

[ssh.Certificate](javascript:void(0))

Use for certificate-based access.

### Syntax

ssh.Certificate = "<certificate>"

### Example

```lua
ssh.Certificate = "ssh-ed12345-cert-v01@openssh.com AAAAIHNzaC1l12345TE..."
```

[Event Handlers](javascript:void(0))

| Name | Function Signature | Description |
| --- | --- | --- |
| .LoginFailed | function( *tcpTable* ) | Assign a function which is called upon a failed login. |
| .Connected | function( *tcpTable* ) | Assign a function which is called upon connection to remote host |
| .Reconnect | function( *tcpTable* ) | Assign a function which is called when socket is attempting to reconnect to the remote host |
| .Data | function( *tcpTable*) | Assign a function which is called when there is new data available in the socket buffer |
| .Closed | function( *tcpTable* ) | Assign a function which is called when the socket is closed by the remote host |
| .Error | function( *tcpTable, err* ) | Assign a function which is called when the socket is closed due to error. The error argument in the function will contain more information, which can be displayed if a variable was created to catch the error message. |
| .Timeout | function( *tcpTable*, err) | Assign a function which is called when a read or write timeout is triggered and the socket was closed. |

[Events](javascript:void(0))

| Name | Description |
| --- | --- |
| Connected | The socket has connected to the remote host. |
| Reconnect | The socket is attempting to reconnect to the remote host |
| Data | There is new data available in the socket buffer |
| Closed | The socket was closed by the remote host |
| Error | The socket was closed due to error. The error argument to the EventHandler will have more information, which can be displayed if a variable was created to catch the error message. |
| Timeout | A read or write timeout was triggered and the socket was closed. |

[Properties](javascript:void(0))

| Name | Notes | Description |
| --- | --- | --- |
| .ReadTimeout | Optional; Default is 0 ( disabled ) | Time, in seconds, to wait for data to be available on socket before raising an error. |
| .WriteTimeout | Optional; Default is 0 ( disabled ) | Time, in seconds, to wait for data write to complete before raising an error. |
| .ReconnectTimeout | Optional; Default is 5 seconds | Time in seconds to wait before attempting to reconnect. 0 disables automatic reconnect. |
| .IsConnected | Read-Only | Returns true if socket is connected. |
| .IsInteractive | Optional; can be true or false. Default is false. | Some devices require "interactive mode" for SSH connections, which opens a PTY (Pseudoterminal). Set this property to 'true' if your device requires this. See the example [SSH with 'interactive mode' enabled](#SSH). |
| .BufferLength | Read-Only | Amount of data in buffer, in bytes. |

[Examples](javascript:void(0))

[SSH without PKI authentication](javascript:void(0))

```lua
-- Aliases  
IPAddress = Controls.IPAddress  
UserName = Controls.UserName  
Password = Controls.Password  
  
  
-- Constants  
SSH = Ssh.New()  -- create new SSH object  
SSH.ReadTimeout = 5  -- set read timeout to 5 seconds  
SSH.WriteTimeout = 5  -- set write timeout to 5 seconds  
SSH.ReconnectTimeout = 5  -- set reconnect timeout to 5 seconds  
Port = 22  -- port of the SSH server  
  
  
-- Functions  
function CredentialsEntered()  -- returns true if ip, user name and password have been entered  
  return IPAddress.String~="" and UserName.String~="" and Password.String~=""  
end  
  
function Connect()  -- function to start the SSH session  
  if SSH.IsConnected then SSH:Disconnect() end  -- if SSH is connected disconnect  
  if CredentialsEntered() then SSH:Connect(IPAddress.String,Port,UserName.String,Password.String) end  -- if all credentials are entered attempt to connect  
end  
  
function Initialization()  -- function called at start of runtime  
  print("Initializing plugin")  
  Connect()  
end  
  
--Parsers  
function ParseResponse()  -- function that reads the SSH TCP socket  
  local rx=SSH:Read(SSH.BufferLength)  -- assign the contents of the buffer to a variable  
  print("RX: "..rx)  
end  
  
  
-- SSH socket callbacks  
SSH.Connected=function()  -- function called when the TCP socket is connected  
  print("Socket connected")  
end  
  
SSH.Reconnect=function()  -- function called when the TCP socket is reconnected  
  print("Socket reconnecting...")  
end  
  
SSH.Closed=function() -- function called when the TCP socket is closed  
  print("Socket closed")  
end  
  
SSH.Error=function()  -- function called when the TCP socket has an error  
  print("Socket error")  
end  
  
SSH.Timeout=function()  -- function called when the TCP socket times out  
  print("Socket timeout")  
end  
  
SSH.LoginFailed=function()  -- function called when SSH login fails  
  print("SSH login failed")  
end  
  
SSH.Data=ParseResponse  -- ParseResponse is called when the SSH object has data  
  
  
-- EventHandlers  
IPAddress.EventHandler = Connect  
UserName.EventHandler = Connect  
Password.EventHandler = Connect  
  
  
-- Start at runtime  
Initialization()  -- calls the Initialization function at the start of runtime
```

[SSH with PKI authentication](javascript:void(0))

```lua
ssh = Ssh.New()  
address = "192.0.2.1"  
port = 22  
user = "root"  
  
-- public key   
ssh.PublicKey = [[-----BEGIN OPENSSH PUBLIC KEY-----  
b3BlbnNzaC1rZXktdjEAAAAACmFlczI...oHGKwgQgWhXiCRTkcURNyAbm  
JCLc/fsC6QbYNxfGRIMrz123456manPJcf/4fdlG123456789ygXGYSLAY8dEmod2E  
vCcO0lShYHwr4ROA==  
-----END OPENSSH PUBLIC KEY-----]]  
  
-- private key in OpenSSL PEM format  
ssh.PrivateKey = [[-----BEGIN OPENSSH PRIVATE KEY-----  
b3BlbnNzaC1rZXktdjEAAAAACmFlczI...oHGKwgQgWhXiCRTkcURNyAbm  
JCLc/fsC6QbYNxfGRIMrz123456manPJcf/4fdlG123456789ygXGYSLAY8dEmod2E  
vCcO0lShYHwr4ROA==  
-----END OPENSSH PRIVATE KEY-----]]  
ssh.PrivateKeyPassword = "test@123"  
  
timer = Timer.New()  
timer.EventHandler = function()  
    ssh:Write("date && hostname\n")  
end  
  
ssh.Connected = function()  
    print("ssh connected")  
    timer:Start(10)  
end  
  
ssh.Reconnect = function()  
    print("ssh reconnect")  
end  
  
ssh.Data = function()  
    print("ssh data")  
    line = ssh:ReadLine(TcpSocket.EOL.Any)  
    while line do  
        print(line)  
        line = ssh:ReadLine(TcpSocket.EOL.Any)  
    end  
end  
  
ssh.Closed = function()  
    print("ssh closed")  
    timer:Stop()  
end  
  
ssh.Error = function(s, err)  
    print("ssh error", err)  
end  
  
ssh.Timeout = function()  
    print("ssh timeout")  
end  
  
ssh.LoginFailed = function()  
    print("ssh LoginFailed")  
end  
  
ssh:Connect(address, port, user, "")
```

[SSH with 'interactive mode' enabled](javascript:void(0))

Set the `.IsInteractive` property to 'true' if your client device requires it.

```lua
ssh = Ssh.New()  
ssh.IsInteractive = true  
ssh:Connect(....
```
