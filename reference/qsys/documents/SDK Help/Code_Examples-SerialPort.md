# SerialPort Usage

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Code_Examples/SerialPort.htm

# SerialPort Usage

The SerialPorts extension to Lua in Q-SYS Designer Software can be used to connect a plugin or scripted control to a serial port on a piece of hardware within a design. [Documentation of the SerialPorts interface can be found here.](https://q-syshelp.qsc.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/06_Serial_Ports.htm) The serial connection is made with a serial pin. This provides bidirectional access to the serial port on that piece of hardware. A control script or plugin with a serial port pin will allow this example code to connect to that pin and handle the interface.

[SerialPorts Usage Example](javascript:void(0))

```lua
-- Variables  
Username = "user"  
Password = "password"  
EOL = "\r\n"                         -- End of line character as defined in device's API  
EOLCharacter = SerialPorts.EOL.CrLf  -- EOL Character constant from Serial Ports usage table  
LoginPrompt = "Login: "              -- Match user prompt string as defined in the API  
PasswordPrompt = "Password: "        -- Match password prompt as defined in the API  
LoginMatch = "Login successful"      -- Match sucessful login string as defined in the API  
  
-- Serial Port  
SerialPort = SerialPorts[1]  -- Array of Serial Ports connected to the plugin, bind to the first one  
baud = 9600                  -- Baud rate of the device  
databits = 8                 -- Number of data bits  
parity = "N"                 -- Type of parity used   
  
--Functions  
function OpenSerialPort()  -- Open the Serial Port connection  
  if SerialPort.IsOpen then  -- If already open, close and restart  
    SerialPort:Close()  
  end  
  SerialPort:Open(baud, databits, parity)  -- Opens the serial port  
end  
  
function Connected()  
  print("Serial port connected")  
  -- Add on connect functionality here (poll timers, data requests, etc.)  
end  
  
function Disconnected()  
  print("Serial port disconnected")  
  -- Add on disconnect functionality here (stop timers, clear data, setup reconnect, etc.)  
end  
  
function Send(cmd)  
  print("Sending " .. cmd)  -- Print the command to be sent  
  if SerialPort.IsOpen then  -- If the serial port is open write the passed through cmd with the EOL to the socket  
    SerialPort:Write(cmd .. EOL)   
  end  
end  
  
--Parsers  
--Get Data from the serial port and act on it  
function ParseResponse()  
  --If a login message is in the buffer respond appropriately  
  if SerialPort:Search(LoginPrompt) then  
    Send(Username)  
    local rx = SerialPort:Read(SerialPort.BufferLength)  -- Read the data in the buffer; Not clearing the buffer will leave data waiting  
  elseif(SerialPort:Search(PasswordPrompt)) then  
    Send(Password)  
    local rx = SerialPort:Read(SerialPort.BufferLength)  
  elseif(SerialPort:Search(LoginMatch))then  
    print("Login Successful!")  
    local rx = SerialPort:Read(SerialPort.BufferLength)  
  else  
    -- If the interface has an EOL character, read the data until EOL is found  
    local rx = SerialPort:ReadLine(EOLCharacter) or ""  
    -- If the interface does not use EOL characters, read the entire buffer  
    -- The data will need a buffer to handle partial messages.    
    -- Add Buffer to the variables defined at the start of runtime  
    --local rx = SerialPort:Read(SerialPort.BufferLength)  
    --Buffer = Buffer .. rx  
  
    print("Received Data: " .. rx)  
  
    -- Handle data from the serial port here  
  
  end  
end  
  
-- Other errors than timeout will return a message  
function ConnectionError(port, message)  
  local msg = message or "Timeout"  
  print("Serial Port error: " .. msg)  
end  
  
-- Event Handlers  
SerialPort.Data = ParseResponse       -- Calls ParseResponse() when the serial port recieves data  
SerialPort.Connected = Connected      -- Calls Connected() when the serial port connects  
SerialPort.Error = ConnectionError    -- Calls ConnectionError() when the serial port encounters an error  
SerialPort.Closed = ConnectionError   -- Calls ConnectionError() when the serial port encounters an unexpected closure  
SerialPort.Timeout = ConnectionError  -- Calls ConnectionError() when the serial port encounters an timeout  
SerialPort.Reconnect = function()     -- Handles functionality when the SerialPort reconnects  
  print("Serial Port Reconnecting...")  
end  
  
-- Run at start  
OpenSerialPort()  -- Calls OpenSerialPort on start of runtime
```

The serial port has functionality similar to the TCPSocket. This example builds a Serial control bound to the first serial pin on the object. A series of functions to handle the data and information received from the port are then created and bound to the SerialPort. The script then initiates the serial connection when the script is loaded. Any data received is checked for the known login exchange and will automatically log in.

**Note:** This example builds the interface, but no calls are made. Data calls and handling based on the device being connected to still need to be added.

The serial port example above can be built into a plugin or control script. The following example plugin binds this engine with a command button and a polling loop. The design then connects the plugin serial pin to the serial port on a Q-SYS Core processor.

[SerialPort Plugin](javascript:void(0))

```lua
-- SerialPorts Example Plugin  
-- by QSC  
-- March 2020  
  
-- Information block for the plugin  
PluginInfo = {  
  Name = "SerialPorts Example Plugin",  
  Version = "0.0",  
  BuildVersion = "0.0.0.1",  
  Id = "599fab42-7618-4c56-99a6-f2874835e90a",  
  Author = "QSC",  
  Description = "An example of SerialPorts usage."  
}  
  
-- Define the color of the plugin object in the design  
function GetColor(props)  
  return { 102, 102, 102 }  
end  
  
-- The name that will initially display when dragged into a design  
function GetPrettyName(props)  
  return "SerialPorts Example, ver. " .. PluginInfo.Version  
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
  
-- Optional function to define pins on the plugin that are not connected to a Control  
-- A Serial Pin is required to use the SerialPort  
function GetPins(props)  
  local pins = {}  
  table.insert(pins, {  
    Name = "Serial Input",  
    Direction = "input",  
    Domain = "serial"  
  })  
  return pins  
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
    Text = "User Name:",  
    Position = {5, 5},  
    Size = {95, 16},  
    FontSize = 14,  
    HTextAlign = "Right"  
  })  
  table.insert(graphics, {  
    Type = "Text",  
    Text = "Password:",  
    Position = {205, 5},  
    Size = {95, 16},  
    FontSize = 14,  
    HTextAlign = "Right"  
  })  
  layout["Username"] = {  
    PrettyName = "Username",  
    Style = "Text",  
    Position = {100, 5},  
    Size = {100, 16}  
  }  
  layout["Password"] = {  
    PrettyName = "Password",  
    Style = "Text",  
    Position = {300, 5},  
    Size = {100, 16}  
  }  
    
  -- Data and Response Controls  
  layout["Status"] = {  
    PrettyName = "Connection Status",   
    Position = {115, 30},   
    Size = {180, 20}  
  }  
  layout["SendButton"] = {  
    PrettyName = "Send Request",  
    Legend = "Send",  
    FontSize = 12,  
    Style = "Button",  
    Position = {150, 80},  
    Size = {100, 24}  
  }  
  layout["ResponseText"] = {  
    PrettyName = "Data",  
    Position = {15, 105},   
    Size = {360, 20}  
  }  
  return layout, graphics  
end  
  
--Start event based logic  
if Controls then  
  -- Aliases  
  Username = Controls.Username  
  Password = Controls.Password  
  Status = Controls.Status  
  SendButton = Controls.SendButton  
  ResponseText = Controls.ResponseText  
    
  -- Constants  
  EOL = "\r\n"                         -- End of line character as defined in device's API  
  EOLCharacter = SerialPorts.EOL.CrLf  -- EOL Character constant from Serial Ports usage table  
  LoginPrompt = "Login: "              -- Match user prompt string as defined in the API  
  PasswordPrompt = "Password: "        -- Match password prompt as defined in the API  
  LoginMatch = "Login successful"      -- Match sucessful login string as defined in the API  
  StatusState = {OK = 0, COMPROMISED = 1, FAULT = 2, NOTPRESENT = 3, MISSING = 4, INITIALIZING = 5}  -- Status states in designer  
    
  -- Timers  
  PollTimer = Timer.New()  -- Timer for polling commands  
    
  -- Serial Port  
  SerialPort = SerialPorts[1]  -- Array of Serial Ports connected to the plugin, bind to the first one  
  baud = 9600                  -- Baud rate of the device  
  databits = 8                 -- Number of data bits  
  parity = "N"                 -- Type of parity used   
  --Buffer = ""                -- If no EOL is used, the plugin will need a buffer for incoming data  
    
  -- Variables  
  PollTime = 3  -- Time between polls in seconds  
    
  --Debug level  
  DebugTx,DebugRx,DebugFunction = false, false, false  
  DebugPrint = Properties["Debug Print"].Value  
  if DebugPrint=="Tx/Rx" then  
    DebugTx,DebugRx=true,true  
  elseif DebugPrint=="Tx" then  
    DebugTx=true  
  elseif DebugPrint=="Rx" then  
    DebugRx=true  
  elseif DebugPrint=="Function Calls" then  
    DebugFunction=true  
  elseif DebugPrint=="All" then  
    DebugTx,DebugRx,DebugFunction=true,true,true  
  end  
    
    
  -- ***   Functions   ***  
    
  -- Function that sets device connection status  
  function ReportStatus(state, msg)  
    if DebugFunction then print("ReportStatus() called") end  
    local msg = msg or ""  
    Status.Value = StatusState[state]  -- Sets status state  
    Status.String = msg  -- Sets status message  
  end  
    
  -- Open the Serial Port connection  
  function OpenSerialPort()  
    if DebugFunction then print("OpenSerialPort() called") end  
    if SerialPort.IsOpen then  -- If already open, close and restart  
      Disconnect()  
    end  
    SerialPort:Open(baud, databits, parity)  -- Opens the serial port  
  end  
    
  -- Disconnect and stop communication on the serial port  
  function Disconnect()  
    if DebugFunction then print("Disconnect() called") end  
    PollTimer:Stop()  -- Stops the poll timer  
    SerialPort:Close()  
  end  
    
  -- Operations to be performed when the serial port connects  
  function Connected()  
    if DebugFunction then print("Connected() called") end  
    ReportStatus("OK")  
    PollTimer:Start(PollTime)  -- Starts the poll timer  
  end  
    
  -- Send a string to the remote device  
  function Send(cmd)  
    if DebugFunction then print("Send() called") end  
    print(cmd)  -- Print the command to be sent  
    if SerialPort.IsOpen then  -- If the serial port is open write the passed through cmd with the EOL to the socket  
      -- Add data formatting here  
      if DebugTx then print("Sending: " .. cmd) end  
      SerialPort:Write(cmd .. EOL)  
    end  
  end  
    
  -- Function sends polling command  
  function PollDevice()  
    if DebugFunction then print("PollDevice() called") end  
    Send("PING")  -- Sends command defined by the target device api for poll functionality  
  end  
    
  -- ***   Parsers   ***  
    
  -- Get Data from the serial port and act on it  
  -- Example uses a search for login exchange with remote device  
  function ParseResponse()  
    if DebugFunction then print("ParseResponse() called") end  
    -- Search the serial port buffer for a waiting username or password prompt and send the correct response  
    if SerialPort:Search(LoginPrompt) then  
      Send(Username.String)  
      local rx = SerialPort:Read(SerialPort.BufferLength)  -- Read the data in the buffer  
      if DebugRx then print("Received Data with login prompt: " .. rx) end  
    
    elseif SerialPort:Search(PasswordPrompt) then  
      Send(Password.String)  
      local rx = SerialPort:Read(SerialPort.BufferLength)  -- Read the data in the buffer  
      if DebugRx then print("Received Data with password prompt: " .. rx) end  
    
    elseif SerialPort:Search(LoginMatch) then  
      local rx = SerialPort:Read(SerialPort.BufferLength)  -- Read the data in the buffer  
      if DebugRx then print("Received Data with login success: " .. rx) end  
    
    else  
      -- If the interface has an EOL character, read the data until EOL is found  
      local rx = SerialPort:ReadLine(EOLCharacter) or ""  
      if DebugRx then print("Received Data: " .. rx) end  
        
      -- If the interface does not use EOL characters, read the entire buffer  
      -- The plugin will need a buffer for data to handle partial messages.    
      -- Add Buffer to the variables defined at the start of runtime  
      --local rx = SerialPort:Read(SerialPort.BufferLength)  
      --Buffer = Buffer .. rx  
           
      -- Add incoming data handling here  
      ResponseText.String = rx  
    end  
  end  
    
  -- Other errors than timeout will return a message  
  function ConnectionError(port, message)  
    if DebugFunction then print("ConnectionError() called") end  
    local msg = message or "Timeout"  
    ReportStatus("MISSING", "Serial Port error: " .. msg)  
    PollTimer:Stop()  -- Stops the poll timer  
  end  
    
  SerialPort.Data = ParseResponse       -- Calls ParseResponse() when the serial port recieves data  
  SerialPort.Connected = Connected      -- Calls Connected() when the serial port connects  
  SerialPort.Error = ConnectionError    -- Calls ConnectionError() when the serial port encounters an error  
  SerialPort.Closed = ConnectionError   -- Calls ConnectionError() when the serial port encounters an unexpected closure  
  SerialPort.Timeout = ConnectionError  -- Calls ConnectionError() when the serial port encounters an timeout  
  SerialPort.Reconnect = function()     -- Handles functionality when the SerialPort reconnects  
    if DebugFunction then print("SerialPort Reconnect event handler called") end  
    -- Added any needed functionality on reconnect, such as data resetting  
  end  
    
  -- ***   Event Handlers   ***  
  -- Call PollDevice when the PollTimer eventhandler  is called  
  PollTimer.EventHandler = PollDevice   
    
  -- Send an api request when the user presses the send button  
  SendButton.EventHandler = function()  
    if DebugFunction then print("SendButton event handler called") end  
    if SendButton.Value == 1 then  -- Momentary button event occurs on both press and release;  Only activate on press  
      Send("Hello, World!")  
    end  
  end  
    
  -- Run at start  
  OpenSerialPort()  -- Calls OpenSerialPort on start of runtime  
end
```
