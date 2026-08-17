# TCPSocket

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Code_Examples/TCPSocket_Example.htm

# TCPSocket

The TCPSocket class is included in the Q-SYS Designer Software's implementation of Lua. It will bind a TCP/IP socket for use on the Q-SYS Core when the design is deployed, following the network configuration of the Core for network interface access. [Documentation of the TCPSocket Class is found here](https://q-syshelp.qsc.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/04_TCP_Socket.htm).

This example builds a TCPSocket and uses it to communicate with a remote device. The example device uses an ASCII string call response interface, with a login and password prompt and ping response that are built into the example.

[Usage Example](javascript:void(0))

```lua
-- Connection Variables  
IPAddress = "192.168.1.1"  
Port = 10001  
Username = "user"  
Password = "password"  
EOL = "\n"                       -- End of line character as defined in device's API  
EOLCharacter = TcpSocket.EOL.Lf  -- EOL Character lookup for TCPSocket ReadLine  
LoginPrompt = "login"            -- Match user prompt string as defined in the API  
PasswordPrompt = "Password"      -- Match password prompt as defined in the API  
LoginMatch = "Login successful"  -- Match sucessful login string as defined in the API  
ResponseData = ""                -- Hold the last message received from the remote device  
  
-- Timers  
PollTimer = Timer.New()  -- Timer for polling commands  
  
-- Sockets  
TCP = TcpSocket.New()     -- Create new TcpSocket object  
TCP.ReadTimeout = 5       -- Set the timeout to 5 seconds  
TCP.WriteTimeout = 5      -- Set the timeout to 5 seconds  
TCP.ReconnectTimeout = 5  -- Set the wait time bfore reconnecting  
    
-- Variables  
PollTime = 3      -- Time between polls in seconds   
LoggedIn = false  -- Flag for when a successful login is made  
    
-- ***   Functions   ***  
-- Returns true if TCP Socket is connected  
function IsConnected()    
  return TCP.IsConnected  
end  
  
-- Connect to device  
function Connect()  
  print("Connecting...")  
  TCP:Connect( IPAddress, Port )  
end  
  
-- Starts the polltimer  
function Connected()  
  PollTimer:Start(PollTime)  
end  
  
-- Stops PollTimer, sets LoggedIn low  
function Disconnected()  
  PollTimer:Stop()  
  LoggedIn = false  
end  
  
-- TCP socket callbacks  
-- Called when TCP socket is connected  
TCP.Connected = function()  
  print("Connected.")  
  Connected()  
end  
  
-- Called when TCP socket is reconnecting  
TCP.Reconnect = function()  
  print("Reconnecting...")  
  Disconnected()  
end  
  
-- Called when TCP socket is closed  
TCP.Closed = function()  
  print("Socket closed.")  
  Disconnected()  
end  
  
-- Called when TCP socket has an error  
TCP.Error = function()  
  print("Socket error.")  
  Disconnected()  
end  
  
-- Called when TCP socket times out  
TCP.Timeout = function()  
  print("Socket timeout.")  
  Disconnected()  
end  
  
-- Called when the TCP socket receives data  
TCP.Data = function()  
  print("Data received")  
  ParseResponse()  -- Call ParseResponse when the TCP socket has data  
end  
  
-- Sends data to the remote device over the TCP socket  
function Send(cmd)  
  if IsConnected() then   -- If the TCP socket is connected write the command and EOL to the socket  
    print("Tx: " .. cmd)  
    TCP:Write(cmd .. EOL)   
  else  
    print("Error - Disconnected; unable to send " .. cmd)  
  end  
end  
  
-- If the Username or Password prompt is matched then the Username or Password is sent   
function Authenticate(rx)  
  if rx:find(LoginMatch) then  
    print("Logged in")  
    LoggedIn = true  
    Connected()  
  elseif rx:match(LoginPrompt) then   
    print("Found \"" .. LoginPrompt .. "\" Sending Username: " .. Username)   
    Send(Username)  
  elseif rx:match(PasswordPrompt) then   
    print("Found \"" .. PasswordPrompt .. "\" Sending Password: " .. Password)  
    Send(Password)  
  end  
end  
  
-- Polling  
function PollDevice()  
  Send("PING")  -- Sends command defined by the target device for poll functionality  
end  
  
-- ***   Parsers   ***  
-- Get the Data from the TCP Socket and act on it  
function ParseResponse()  
  local rx = TCP:ReadLine(EOLCharacter)  -- Read a line of data from the socket  
  local buffer = {}  
  while rx do  
    if DebugRx then print("Rx: " .. rx) end  
    table.insert(buffer, rx)  
    rx = TCP:ReadLine(EOLCharacter)  
  end  
  -- If login has not been authenticated, try to authenticate  
  if not IsLoggedIn() then  
    for index = 1,#buffer do  
      Authenticate(buffer[index])  
    end  
  else   
    for index = 1,#buffer do  
  
      -- Handle the data from the remote device here  
      ResponseData = buffer[index]  
  
    end  
  end  
end  
  
  
-- ***   Event Handlers   ***  
PollTimer.EventHandler = PollDevice  -- Call PollDevice when the PollTimer EventHandler is called  
  
  
-- Run at start  
Connect()  
end
```

The TCPSocket framework above can then be integrated for further functionality. This framework binds the TCP socket responses to helper functions. Send() and ParseResponse can be extended and used to integrate the remote communication into the local script.

* Disconnect and Connect states trigger the Connected() and Disconnected() responses.
* Incoming data routes through an authentication check. A login following the known prompts is handled automatically.
* Incoming data is pulled from the socket buffer when full lines are available and parsed.
* Once a connection is made, an automatic poll timer sends the string âPINGâ to the device every 3 seconds.
* The connection is initiated automatically as the last step.

This socketâs ParseResponse() uses the ReadLine( TCP.EOL.Lf ) function call to pull a full line of data from the TCPSocketâs buffer. When a TCP packet is received, the data is buffered and ReadLine() pulls a complete line, leaving incomplete messages in the buffer. If an EOL character is not part of the remote deviceâs API, the Read( bytes ) function can be used instead. An example of using the Read() function is shown in the plugin code.

The following code can be built into a plugin, starting from the [Basic Plugin Framework](Basic_Plugin_Framework.htm). The TCP client example is built into the runtime.

**Tip:** This is a common type of interface needed. The Authentication and polling command can be updated to meet the needs of a real device.

[TCP Socket Plugin](javascript:void(0))

```lua
-- TCP Example Plugin  
-- by QSC  
-- October 2020  
  
-- Information block for the plugin  
PluginInfo = {  
  Name = "TCP Example Plugin",  
  Version = "0.0",  
  BuildVersion = "0.0.0.1",  
  Id = "d5467c28-012a-4afd-ab58-b72f73348cd5",  
  Author = "QSC",  
  Description = "An example of TCPSocket usage."  
}  
  
-- Global Variables  
EmptyIPMessage = "Enter an IP Address"  
  
-- Define the color of the plugin object in the design  
function GetColor(props)  
  return { 102, 102, 102 }  
end  
  
-- The name that will initially display when dragged into a design  
function GetPrettyName(props)  
  return "TCP Example, ver. " .. PluginInfo.Version  
end  
  
-- Define User configurable Properties of the plugin  
function GetProperties()  
  local props = {}  
  table.insert(props, {  
    Name = "Debug Print",  
    Type = "enum",  
    Choices = {"None", "Tx/Rx", "Tx", "Rx", "Function Calls", "All"},  
    Value = "None"  
  })  
  return props  
end  
  
-- Optional function to update available properties when properties are altered by the user  
function RectifyProperties(props)  
  if props.plugin_show_debug.Value == false then   
    props["Debug Print"].IsHidden = true   
  end  
  return props  
end  
  
-- Defines the Controls used within the plugin  
function GetControls(props)  
  local ctrls = {}  
  table.insert(ctrls, {  
    Name = "Status",  
    ControlType = "Indicator",  
    IndicatorType = "Status",  
    PinStyle = "Output",  
    UserPin = true,  
    Count = 1  
  })  
  table.insert(ctrls, {  
    Name = "IPAddress",  
    ControlType = "Text",  
    DefaultValue = EmptyIPMessage,  
    UserPin = true,  
    PinStyle = "Both",  
    Count = 1  
  })  
  table.insert(ctrls, {  
    Name = "Port",  
    ControlType = "Knob",  
    ControlUnit = "Integer",  
    Min = 1,  
    Max = 65535,  
    DefaultValue = 10001,  
    UserPin = true,  
    PinStyle = "Both",  
    Count = 1  
  })  
  table.insert(ctrls, {  
    Name = "Username",  
    ControlType = "Text",  
    UserPin = true,  
    PinStyle = "Both",  
    Count = 1  
  })  
  table.insert(ctrls, {  
    Name = "Password",  
    ControlType = "Text",  
    UserPin = true,  
    PinStyle = "Both",  
    Count = 1  
  })  
  table.insert(ctrls, {  
    Name = "SendButton",  
    ControlType = "Button",  
    ButtonType = "Momentary",  
    Count = 1,  
    UserPin = true,  
    PinStyle = "Input"  
  })  
  table.insert(ctrls, {  
    Name = "ResponseText",  
    ControlType = "Text",  
    Count = 1,  
    UserPin = true,  
    PinStyle = "Output"  
  })  
  return ctrls  
end  
  
--Layout of controls and graphics for the plugin UI to display  
function GetControlLayout(props)  
  local layout = {}  
  local graphics = {}  
  -- Connection Controls  
  table.insert(graphics, {  
    Type = "Text",  
    Text = "IP Address:",  
    Position = {5, 5},  
    Size = {95, 16},  
    FontSize = 14,  
    HTextAlign = "Right"  
  })  
  table.insert(graphics, {  
    Type = "Text",  
    Text = "Port:",  
    Position = {5, 25},  
    Size = {95, 16},  
    FontSize = 14,  
    HTextAlign = "Right"  
  })  
  table.insert(graphics, {  
    Type = "Text",  
    Text = "Username:",  
    Position = {205, 5},  
    Size = {95, 16},  
    FontSize = 14,  
    HTextAlign = "Right"  
  })  
  table.insert(graphics, {  
    Type = "Text",  
    Text = "Password:",  
    Position = {205, 25},  
    Size = {95, 16},  
    FontSize = 14,  
    HTextAlign = "Right"  
  })  
  layout["IPAddress"] = {  
    PrettyName = "IP Address",  
    Style = "Text",  
    Position = {100, 5},  
    Size = {100, 16}  
  }  
  layout["Port"] = {  
    PrettyName = "Port",  
    Style = "Text",  
    Position = {100, 25},  
    Size = {100, 16}  
  }  
  layout["Username"] = {  
    PrettyName = "Username",  
    Style = "Text",  
    Position = {300, 5},  
    Size = {100, 16}  
  }  
  layout["Password"] = {  
    PrettyName = "Password",  
    Style = "Text",  
    Position = {300, 25},  
    Size = {100, 16}  
  }  
    
  -- Data and Response Controls  
  layout["Status"] = {  
    PrettyName = "Connection Status",   
    Position = {115, 50},   
    Size = {180, 20}  
  }  
  layout["SendButton"] = {  
    PrettyName = "Send Request",  
    Legend = "Send",  
    FontSize = 12,  
    Style = "Button",  
    Position = {150, 100},  
    Size = {100, 24}  
  }  
  layout["ResponseText"] = {  
    PrettyName = "Data",  
    Position = {15, 125},   
    Size = {360, 20}  
  }  
  return layout, graphics  
end  
  
--Start event based logic  
if Controls then  
  -- Aliases  
  IPAddress = Controls.IPAddress  
  Port = Controls.Port  
  Username = Controls.Username  
  Password = Controls.Password  
  Status = Controls.Status  
  SendButton = Controls.SendButton  
  ResponseText = Controls.ResponseText  
    
  -- Constants  
  EOL = "\n"                       -- End of line character as defined in device's API  
  EOLCharacter = TcpSocket.EOL.Lf  -- EOL Character lookup for TCPSocket ReadLine  
  LoginPrompt = "login"            -- Match user prompt string as defined in the API  
  PasswordPrompt = "Password"      -- Match password prompt as defined in the API  
  LoginMatch = "Login successful"  -- Match sucessful login string as defined in the API  
  StatusState = {OK=0, COMPROMISED=1, FAULT=2, NOTPRESENT=3, MISSING=4, INITIALIZING=5}  -- Status states in designer  
    
  -- Timers  
  PollTimer = Timer.New()  -- Timer for polling commands  
    
  -- Sockets  
  TCP = TcpSocket.New()     -- Create new TcpSocket object  
  TCP.ReadTimeout = 5       -- Set the timeout to 5 seconds  
  TCP.WriteTimeout = 5      -- Set the timeout to 5 seconds  
  TCP.ReconnectTimeout = 5  -- Set the wait time bfore reconnecting  
  --Buffer = ""             -- If an EOL character is not used by the remote device, the plugin will need a buffer to manage incoming data  
    
  -- Variables  
  PollTime = 3      -- Time between polls in seconds   
  LoggedIn = false  -- Flag for when a successful login is made  
    
  --Debug level  
  DebugTx, DebugRx, DebugFunction = false, false, false  
  DebugPrint = Properties["Debug Print"].Value  
  if DebugPrint == "Tx/Rx" then  
    DebugTx, DebugRx = true, true  
  elseif DebugPrint == "Tx" then  
    DebugTx = true  
  elseif DebugPrint == "Rx" then  
    DebugRx = true  
  elseif DebugPrint == "Function Calls" then  
    DebugFunction = true  
  elseif DebugPrint == "All" then  
    DebugTx, DebugRx, DebugFunction = true, true, true  
  end  
    
    
  -- ***   Functions   ***  
  -- Helper Functions  
  -- Function that sets device status  
  function ReportStatus(state,msg)    
    local msg = msg or ""  
    Status.Value = StatusState[state]  -- Sets status state  
    Status.String = msg  -- Sets status message  
  end  
    
  -- Returns true if TCP Socket is connected  
  function IsConnected()    
    return TCP.IsConnected  
  end  
    
  -- Returns true if sucessful login string is matched  
  function IsLoggedIn()  
    return LoggedIn  
  end  
    
  -- Function returns true if all credentials needed for connection is entered  
  function CredentialsEntered()  
    return IPAddress.String ~= "" and IPAddress.String ~= EmptyIPMessage and Username.String ~= "" and Password.String ~= ""  
  end  
    
  -- Connect to device if credentials have been entered  
  function Connect()  
    if DebugFunction then print("Connect() called") end  
    if CredentialsEntered() then   
      TCP:Connect( IPAddress.String, Port.Value )  
    else  
      ReportStatus("MISSING","Invalid Credentials")  
    end    
  end  
    
  -- Connect to device if credentials have been entered  
  function Disonnect()  
    if DebugFunction then print("Disconnect() called") end  
    TCP:Disconnect()  
    Disconnected()  
  end  
    
  -- Starts the polltimer  
  function Connected()  
    if DebugFunction then print("Connected() called") end  
    PollTimer:Start(PollTime)  
  end  
    
  -- Stops PollTimer, sets LoggedIn low  
  function Disconnected()  
    if DebugFunction then print("Disconnected() called") end  
    PollTimer:Stop()  
    LoggedIn = false  
  end  
    
  -- TCP socket callbacks  
  -- Called when TCP socket is connected  
  TCP.Connected = function()  
    if DebugFunction then print("TCPSocket Connected Handler called") end  
    ReportStatus("OK")  
    Connected()  
  end  
    
  -- Called when TCP socket is reconnecting  
  TCP.Reconnect = function()  
    if DebugFunction then print("TCPSocket Reconnect Handler called") end  
    Disconnected()  
  end  
    
  -- Called when TCP socket is closed  
  TCP.Closed = function()  
    if DebugFunction then print("TCPSocket Closed Handler called") end  
    ReportStatus("MISSING", "Socket closed")  
    Disconnected()  
  end  
    
  -- Called when TCP socket has an error  
  TCP.Error = function()  
    if DebugFunction then print("TCPSocket Error Handler called") end  
    ReportStatus("MISSING", "Socket error")  
    Disconnected()  
  end  
    
  -- Called when TCP socket times out  
  TCP.Timeout = function()  
    if DebugFunction then print("TCPSocket Timeout Handler called") end  
    ReportStatus("MISSING", "Timeout")  
    Disconnected()  
  end  
    
  -- Called when the TCP socket receives data  
  TCP.Data = function()  
    if DebugFunction then print("TCPSocket Data Handler called") end  
    print("Data received")  
    ParseResponse()  -- Call ParseResponse when the TCP socket has data  
  end  
    
  -- Sends data to the remote device over the TCP socket  
  function Send(cmd)  
    if DebugFunction then print("Send() called") end  
    if IsConnected() then   -- If the TCP socket is connected write the command and EOL to the socket  
      if DebugTx then print("Tx: " .. cmd) end  
        
      -- Add command formatting for the API here  
      TCP:Write(cmd .. EOL)   
    
    else  
      print("Error - Disconnected; unable to send " .. cmd)  
    end  
  end  
    
  -- If the Username or Password prompt is matched then the Username or Password is sent   
  function Authenticate(rx)  
    if DebugFunction then print("Authenticate() called") end  
    if rx:find(LoginMatch) then  
      print("Logged in")  
      LoggedIn = true  
      Connected()  
    elseif rx:match(LoginPrompt) then   
      print("Found \"" .. LoginPrompt .. "\" Sending Username: " .. Username.String)   
      Send(Username.String)  
    elseif rx:match(PasswordPrompt) then   
      print("Found \"" .. PasswordPrompt .. "\" Sending Password: " .. Password.String)   
      Send(Password.String)  
    end  
  end  
    
  -- Polling  
  function PollDevice()  
    if DebugFunction then print("PollDevice() called") end  
    Send("PING")  -- Sends command defined by the target device for poll functionality  
  end  
    
  -- ***   Parsers   ***  
  -- Get the Data from the TCP Socket and act on it  
  function ParseResponse()  
    if DebugFunction then print("ParseResponse() called") end  
    
    -- If an EOL character is known, use the TCPSocket buffer to retrieve data line by line  
    local rx = TCP:ReadLine(EOLCharacter)  -- Read a line of data from the socket  
    local buffer = {}  
    while rx do  
      if DebugRx then print("Rx: " .. rx) end  
      table.insert(buffer, rx)  
      rx = TCP:ReadLine(EOLCharacter)  
    end  
    -- If login has not been authenticated, try to authenticate  
    if not IsLoggedIn() then  
      for index = 1,#buffer do  
        Authenticate(buffer[index])  
      end  
    else   
      for index = 1,#buffer do  
    
        --Handle the data from the remote device here  
        ResponseData.String = buffer[index]  
    
      end  
    end  
    
    --[[  
    -- If the remote device does not support EOL characters, read all the data from the buffer  
    -- A global Buffer within the plugin will be needed to handle messages for incomplete frames of data  
    Buffer = Buffer .. TCP:Read(TCP.BufferLength)  -- Read the data in the buffer  
    if DebugRx then print("Rx: " .. Buffer) end  
    if not IsLoggedIn() then  
      Authenticate(Buffer)  
      Buffer = ""  --Clear the buffer after checking for login.  This assumes the login request will always be in 1 frame of data  
    else  
      -- Use the API to find the messages within the received data  
      local eol = Buffer:find("End of Message")   -- Replace this with the message parsing algorythm  
      while eol do                                -- Repeat until no message is found in the Buffer  
        ResponseData.String = Buffer:sub(1, eol)  -- Handle the message that was found  
        Buffer = Buffer:sub(eol+1, -1)            -- Clear the processed data from the buffer  
        eol = Buffer:find("End of Message")       -- Find the next message, if it exists  
      end  
      -- Leave the data after the last message in Buffer to be appended onto the next received data  
    end  
    ]]  
    
  end  
    
    
  -- ***   Event Handlers   ***  
  -- Connect when the IPAddress changes, or set the empty message when no IP Address is entered  
  IPAddress.EventHandler = function()  
    if DebugFunction then print("IPAddress handler called") end  
    if IPAddress.String == "" then  -- If the user enters blank IP stop communication  
      IPAddress.String = EmptyIPMessage  
      Disconnect()  
    else  
      Connect()  -- Otherwise Call Connect when the IPAddress EventHandler is called  
    end  
  end  
    
  Port.EventHandler = Connect          -- Call Connect when the Port EventHandler is called  
  Username.EventHandler = Connect      -- Call Connect when the Username EventHandler is called  
  Password.EventHandler = Connect      -- Call Connect when the Password EventHandler is called  
  PollTimer.EventHandler = PollDevice  -- Call PollDevice when the PollTimer EventHandler is called  
    
  -- Send the Hello, World message when the user presses the button  
  SendButton.EventHandler=function(self)  
    if DebugFunction then print("SendButton Eventhandler called") end  
    if self.Value == 1 then  -- Momentary button event occurs on both press and release;  Only activate on press, not on release  
      Send("Hello, World!")  
    end  
  end  
    
    
  -- Run at start  
  Connect()  
end
```
