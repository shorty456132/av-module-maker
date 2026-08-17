# Telnet

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Code_Examples/Telnet_Example.htm

# Telnet

This is a code example for connecting to a device via the Telnet protocol.

## Text Controller Setup

Drag in a Text Controller and name it Telnet. Add three **Text Boxes** named **IPAddress**, **UserName**, and **Password** (see screenshot).

Next, copy the Example Code to the Text Controller.

[Telnet Example Code](javascript:void(0))

```lua
-- Aliases  
IPAddress = Controls.IPAddress  
UserName = Controls.UserName  
Password = Controls.Password  
  
  
-- Variables  
TelnetActive = false  -- flag for the state of the telnet session  
TelnetIsSetup = false  -- flag for the state of the telnet negotiation    
AttemptedLogin = false  -- flag for attempting to login but failed  
  
  
-- Constants  
Telnet = TcpSocket.New()  -- create new TCP object  
Port = 23  -- port of the telnet server  
EOL = "\r"  -- End Of Line character  
IAC = 0xFF  -- telnet Interpret As Command character  
TelSetResp = {  -- table of telnet setup options, these are examples of WONT options.    
  {cmd=0xFC,opt=0x18},  
  {cmd=0xFC,opt=0x20},  
  {cmd=0xFC,opt=0x23},  
  {cmd=0xFC,opt=0x27},  
  {cmd=0xFC,opt=0x03},  
  {cmd=0xFC,opt=0x01},  
  {cmd=0xFC,opt=0x1F},  
  {cmd=0xFC,opt=0x05},  
  {cmd=0xFC,opt=0x21}  
}  
UserPrompt = "login"  -- telnet user name prompt to look for during telnet login  
PassPrompt = "Password"  -- telnet password prompt to look for during telnet login  
LoggedInPrompt = "Login successful"  -- telnet logged in prompt to look for during telnet login  
LoginFailPrompt = "Login incorrect"  -- telnet login fail prompt to look for during telnet login  
  
  
-- Functions  
function CredentialsEntered()  -- returns true if ip, user name and password have been entered  
  return IPAddress.String~="" and UserName.String~="" and Password.String~=""  
end  
  
function TelnetSetup()  -- function to pack and send the do/dont/will/wont bits  
  print("Setting up telnet session")  
  local data={}  
  for _,resp in ipairs(TelSetResp) do  
    table.insert(data,string.pack("BBB",IAC,resp.cmd,resp.opt))  
  end  
  Telnet:Write(table.concat(data))  
end  
  
function TelnetAuth(rx)  -- function to look for user name and password prompts and send proper credentials  
  if rx:match(UserPrompt) then print("Found UserPrompt") Telnet:Write(UserName.String..EOL) print("Sending: "..UserName.String)  
  elseif rx:match(PassPrompt) then print("Found PassPrompt") Telnet:Write(Password.String..EOL) print("Sending: "..Password.String)  
  end  
end  
  
function Disconnected()  -- function called when disconnected from the   
  TelnetActive = false  
  TelnetIsSetup = false  
  AttemptedLogin = false  
end  
  
function Connected()  -- function called when the telnet session is first active  
  print("Telnet session active")  
end  
  
function TelnetIsConnected()  -- returns true when the telnet session flag is high  
  return TelnetActive  
end  
  
function Connect()  -- function to connect the TCP socket  
  if Telnet.IsConnected then Telnet:Disconnect() Disconnected() end  
  if CredentialsEntered() then Telnet:Connect(IPAddress.String,Port) end  
end  
  
function Initialization()  -- function called at start of runtime  
  print("Initializing plugin")  
  Connect()  
end  
  
--Parsers  
function ParseResponse()  -- function that reads and parses the TCP socket  
  local rx=Telnet:Read(Telnet.BufferLength)  -- assign the contents of the buffer to a variable  
  --print("RX: "..rx)  
  if AttemptedLogin==false then  
    if string.find(rx,LoggedInPrompt) then  
      TelnetActive=true  
      Connected()  
    elseif string.find(rx,UserPrompt) or string.find(rx,PassPrompt) then  
      print("Telnet session initiated")  
      TelnetIsSetup=true  
      TelnetAuth(rx)  
    elseif string.find(rx,LoginFailPrompt) then   
      print("Telnet credentials incorrect")  
      AttemptedLogin=true  
    end  
  end  
  if TelnetIsSetup==false then TelnetSetup() end  
end  
  
  
  
-- TCP socket callbacks  
Telnet.Connected=function()  -- function called when the TCP socket is connected  
  print("Socket connected")  
end  
  
Telnet.Reconnect=function()  -- function called when the TCP socket is reconnected  
  print("Socket reconnecting...")  
end  
  
Telnet.Closed=function() -- function called when the TCP socket is closed  
  print("Socket closed")  
  Disconnected()  
end  
  
Telnet.Error=function()  -- function called when the TCP socket has an error  
  print("Socket error")  
  Disconnected()  
end  
  
Telnet.Timeout=function()  -- function called when the TCP socket times out  
  print("Socket timeout")  
  Disconnected()  
end  
  
Telnet.Data=ParseResponse  -- ParseResponse is called when Telnet has data  
  
  
-- EventHandlers  
IPAddress.EventHandler = Connect  
UserName.EventHandler = Connect  
Password.EventHandler = Connect  
  
  
-- Start at runtime  
Initialization()  -- calls the Initialization function at the start of runtime
```

## Using the Example

This code is a generic example of connecting to a Telnet device, sending example Telnet setup bits (varies depending on the device, if needed at all) and passing a username and password to start the session. **UserPrompt**, **PassPrompt**, **LoggedInPrompt**, and **LoginFailPrompt** are device-dependent and will vary depending on the device. How they are defined in this script is just an example.
