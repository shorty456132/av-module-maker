# SSH Object

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Code_Examples/SSH_Example.htm

# SSH Object

This is a code example for using the SSH object. Refer to the [Ssh](https://q-syshelp.qsc.com/#Control_Scripting/Using_Lua_in_Q-Sys/Ssh.htm) topic in Q-SYS Help for more information.

## Text Controller Setup

Drag in a Text Controller and name it SSH. Add three Text Boxes named **IPAddress**, **Username**, and **Password** (see picture below).

Next, copy the code below to the Text Controller.

[SSH Example Code](javascript:void(0))

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

## Using the Example

This code is a generic example of using the SSH object. Simply enter the **Username**, **Password**, and **IPAddress** to start an ssh session.
