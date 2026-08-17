# Serial Recommended Practices

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Recommended_Practices/Serial.htm

# Serial Recommended Practices

## Serial Port

**Note:** For base information, see the [SerialPorts](https://help.qsys.com/#Control_Scripting/Using_Lua_in_Q-Sys/SerialPorts.htm) topic in Q-SYS Help.

[Property Usage and Considerations](javascript:void(0))

#### .IsOpen

This property is read-only and will return true if the serial port is open.

This property is useful to prevent calling `:Write()` when the serial port is not opened.

```lua
function Send(text)  
  if MySerialPort.IsOpen then    
    print("TX: "..text)  
    MySerialPort:Write(text)  
  else   
    print("Unable to Write: Port Closed")  
  end  
end
```

#### .BufferLength

This property is read-only and will return the length of the buffer, in bytes, as an integer.

This property is useful to determine if there is data to parse and how much.

[Events](javascript:void(0))

#### Connected

This event is called when the serial port successfully opens.

After this function is called, you may start logic for sending data to check that the expected device is wired up and responding.

**Note:** This function is called regardless of the physical wiring and status of the device connected to the serial port. Status should not be set to 'OK' in this callback.

```lua
socket.Connected = function(sock)  
  print("Socket Connected")  
  SendData("Poll") -- send inital poll  
  -- optionally start a poll timer or other logic here  
end 
```

#### Reconnect

This event is called at each `.ReconnectTimeout` interval when the serial port tries to reconnect to the server port.

Typically, the only action to take when this event is triggered is a debug statement.

#### Closed

This event is called when a the serial port is closed.

This is the best place to reset variables, queues, and any other actions to prepare for a new connection.

#### Error

This event is called when there is an error relating to the socket connection.

Here are some error strings returned by this event:

* Empty String: Failed to connect

#### Data

This event is called when there is new data available in the buffer.

This is where you would read data from the buffer and parse appropriately.

The buffer is retained; therefore, not all data needs to be pulled from the buffer if a complete message was not received, as RS-232 does not guarantee you will receive a full command every time this event is called.

[Defining the Pin](javascript:void(0))

#### Text Controller

In design time (not emulating or connected to a Core), below your list of controls, increment 'Serial Port Inputs' to the number of ports needed.

#### Plugin

In `GetPins()`, return a table item with `Domain` set to `"serial"` and `Direction` set to `"input"`.

Define Serial Pin in a Plugin

```lua
function GetPins(props)  
  local pins = {}  
  table.insert(  
    Name = "SerialPin",  
    Direction = "input",  
    Domain = "serial  
  )  
  return pins  
end
```

[Setup](javascript:void(0))

#### Map variable to the port

Start by mapping the port to a variable for easy use and readable code. The serial input ports will be in the `SerialPorts` table and will be numerically indexed. For plugins, they will be indexed in the order they are in when the table is returned by `GetPins()`.

**Note:**  To avoid possible issues with garbage collection, do not scope the variable as a local.

Map Serial ports to variables

```lua
MySerialPort = SerialPorts[1]
```

#### Define EventHandlers

Before opening the port, you should define event handlers for the port's various events.

```lua
MySerialPort.Connected = function(port)  
  print("Connected")  
  -- start communication  
  
end  
  
MySerialPort.Reconnect = function(port)  
  print("Reconnect")  
end  
  
MySerialPort.Closed = function(port)  
  print("Closed")  
  -- stop communication  
end  
  
MySerialPort.Error = function(port, err)  
  print("Error:", err)  
end  
  
MySerialPort.Data = function(port) -- Called when data is received  
  print("Socket buffer has " .. port.BufferLength .. " bytes")  
  local data = port:ReadLine(SerialPorts.EOL.Custom,'\r') -- read until a carrige return \x0D  
  while data do -- if valid data was read, loop until there is no more valid data  
    ParseData(data) -- parse the data in a seperate function  
    data = port:ReadLine(SerialPorts.EOL.Custom,'\r') -- check for more data  
  end    
end 
```

#### Open the port

It is recommended to wrap the :Open() call in a pcall statement.

The :Open() call will generate a Lua error if the pin is not wired to a valid Serial Server Port or if it is wired to some Serial Server Ports in Emulation.

**Note:**  To ensure a reliable connection to virtual serial server ports on other Text Controllers, Block Controllers, or Plugins, it is recommenced to not open the port for the first second of the script running. See [Complete Example Serial Client](#Complete) below.

```lua
function OpenPort()  
  local success, err = pcall(function()  
    MySerialPort:Open(115200, 8, "N")  
  end)  
  if not success then  
    print("Error Opening Port:", err)  
  else   
    print("Serial Port opened")  
  end  
end
```

[Sending Data](javascript:void(0))

As outlined in [.IsOpen](#.IsOpen), to avoid Lua errors, it is recommenced that you check that the port is open before calling `:Write()`.

```lua
function Send(text)  
  if MySerialPort.IsOpen then    
    print("TX: "..text)  
    MySerialPort:Write(text)  
  else   
    print("Unable to Write: Port Closed")  
  end  
end
```

[Reading from the buffer](javascript:void(0))

Unlike Ethernet communications, data is not guaranteed to be received in complete packets or strings. It is recommenced to use `:ReadLine()` and `:Search()` to check for and parse complete sets of information. This process is the same as TcpSockets.

[Whole buffer](javascript:void(0))

**CAUTION:** This method is not recommended.

Read entire buffer

```lua
MySerialPort.Data = function(sp) -- Event returns the SerialPort that called it.  
  print("MySerialPort received " .. sp.BufferLength .. " bytes")  
  local data = sp:Read(sp.BufferLength) -- read the entire buffer  
  if #data > 0 then -- ignore empty payloads  
    ParseData(data) -- parse the data in a seperate function  
  end   
end 
```

[Read until specific character](javascript:void(0))

Read until EOL char

```lua
MySerialPort.Data = function(sp) -- Event returns the SerialPort that called it.  
  print("Socket buffer has " .. sp.BufferLength .. " bytes")  
  local data = sp:ReadLine(SerialPorts.EOL.Custom,'\r') -- read until a carrige return \x0D  
  while data do -- if valid data was read, loop until there is no more valid data  
    ParseData(data) -- parse the data in a seperate function  
    data = sp:ReadLine(SerialPorts.EOL.Custom,'\r') -- check for more data  
  end    
end 
```

[Local buffer](javascript:void(0))

Use local buffer

```lua
MyBuffer = ""  
  
socket.Data = function(sp) -- Event returns the SerialPort that called it.  
  print("Socket received " .. sp.BufferLength .. " bytes")  
  local data = sp:Read(sp.BufferLength) -- read the entire buffer  
  if #data > 0 then -- ignore empty payloads  
    MyBuffer = MyBuffer..data -- append data to local buffer  
    ProcessBuffer() -- process the buffer in a seperate function  
  end   
end 
```

[Heartbeat](javascript:void(0))

It is highly recommended to implement heartbeat logic to ensure the device is connected and communicating to your script or plugin. This can be achieved with some simple timeout code.

The idea is to track if the port stops receiving valid data indicating a problem with the wiring or device. It relies on a timer being stopped and restarted with a time greater than the poll rate of your code.

Whenever you receive valid data, you would restart the timer so that if the timer's event handler gets called, it will be from a lack of communication with the end device.

```lua
HeartbeatTimer = Timer.New()  
HeartbeatTimeout = 5 -- must be longer than your poll rate  
HeartbeatTimer.EventHandler = function()  
  print("Lost communication with device!")  
  -- restart communication and reinitialize values here  
  Initialize()  
end  
  
function beat() -- helper function to call whenever valid data is received   
  HeartbeatTimer:Stop()  
  HeartbeatTimer:Start(HeartbeatTimeout)  
end   
  
MySerialPort.Data = function(port) -- Called when data is received  
  local data = port:ReadLine(SerialPorts.EOL.Custom,'\r')  
  while data do   
    beat()   
    print("RX: "..data)  
  
    data = port:ReadLine(SerialPorts.EOL.Custom,'\r')  
  end  
end
```

[Complete Example Serial Client](javascript:void(0))

```lua
MySerialPort = SerialPorts[1]  
  
function Send(text)  
  if MySerialPort.IsOpen then    
    print("TX: "..text)  
    MySerialPort:Write(text..'\r')  
  else   
    print("Unable to Write: Port Closed")  
  end  
end  
  
function ping()  
  Send("ping")  
end  
  
PingTime = 3 -- poll rate  
PingTimer = Timer.New()  
PingTimer.EventHandler = ping  
  
HeartbeatTimer = Timer.New()  
HeartbeatTimeout = 5 -- must be longer than your poll rate  
HeartbeatTimer.EventHandler = function()  
  print("Lost communication with device!")  
  -- restart communication and reinitialize values here  
  Initialize()  
end  
  
function beat()  
  HeartbeatTimer:Stop()  
  HeartbeatTimer:Start(HeartbeatTimeout)  
end   
  
MySerialPort.Connected = function(port)  
  print("Connected")  
  HeartbeatTimer:Start(HeartbeatTimeout)  
  PingTimer:Start(PingTime)  
  ping()  
end  
  
MySerialPort.Reconnect = function(port)  
  print("Reconnect")  
end  
  
MySerialPort.Closed = function(port)  
  print("Closed")  
  HeartbeatTimer:Stop()  
  PingTimer:Stop()  
end  
  
MySerialPort.Error = function(port, err)  
  print("Error:", err)  
end  
  
MySerialPort.Data = function(port) -- Called when data is received  
  local data = port:ReadLine(SerialPorts.EOL.Custom,'\r')  
  while data do   
    beat()   
    print("RX: "..data)  
  
    data = port:ReadLine(SerialPorts.EOL.Custom,'\r')  
  end  
end   
  
function Initialize()  
  local success, err = pcall(function()  
    if MySerialPort.IsOpen then   
      MySerialPort:Close()  
    end   
    MySerialPort:Open(115200, 8, "N")  
  end)  
  if not success then  
    print("Error Opening Port:", err)  
  else   
    print("Serial Port opened")  
  end  
end    
  
Timer.CallAfter(function() Initialize() end,1) -- It is recommended to delay this to ensure proper connection to virtual serial server ports
```
