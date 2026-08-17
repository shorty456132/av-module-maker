# Serial Server and Serial Client

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Code_Examples/Serial_Server_Serial_Client.htm

# Serial Server and Serial Client

This example is meant to be used when wiring up the serial ports of two Text Controllers.

## Text Controller Setup

Drag in two Text Controllers and name one **Serial Server** and the other one **Serial Client**. In the **Serial Server** Text Controller, add a Virtual Serial Port Output and two knobs. Both knobs will have these control types:

* Category: Knob
* Units: Integer
* Max Value: 10
* Min Value: 1
* Control Pin: None

Name the first knob **RxData** and the second knob **TxData**. Next, in the **Serial Client** Text Controller, add a Serial Port Input, toggle button, trigger button, and a knob. Name the toggle button **AutoSend**, the trigger button **Send**, and the knob **Count**. The **Count** knob will have the same control types as the knobs in the **Serial Server** Text Controller. Next, wire up the serial pins between the two Text Controllers (see screenshot). Finally, copy the code below to its respective Text Controller.

[Serial Server Code](javascript:void(0))

```lua
-- Aliases  
TxData = Controls.TxData  -- alias for the TxData control  
RxData = Controls.RxData  -- alias for the RxData control  
  
  
-- Constants  
Serial = SerialServerPorts[1]  -- Create new Serial Server object  
Server = TcpSocket.New()  -- Create a TCP socket  
IPAddress = "127.0.0.1"  -- variable that will be used for the TCP IP address  
Port = 4888  -- variable that will be used for the TCP port  
  
  
-- Functions  
function IncData(data)  -- function that reads data passed through and increments by one or sets to one if > 9  
  print("Incomming Data: "..data)  
  RxData.Value = data  -- set the RxData control to the incoming value  
  if data > 9 then data = 1.0 else data = data + 1 end  -- evaluates data and gives it a new value  
  print("Sent Data: "..data)  
  TxData.Value = data  -- set the TxData control to the new value of data  
  return data  -- returns the new value of data  
end  
  
function ParseResponse()  -- function that reads the SerialServer port and writes it to the TCP socket  
  local data = tonumber(Serial:Read(Serial.BufferLength))  -- read the SerialServer port  
  if Server.IsConnected then Server:Write(IncData(data)) end  -- write to the TCP socket if it's connected  
end  
  
function Initialization()  -- function called at the start of runtime  
  Server:Connect(IPAddress,Port)  -- connect the TCP socket  
  print("TCP Socket Connecting to: "..IPAddress..":"..Port)  
end  
  
  
-- Serial Server Callbacks  
Serial.OnOpen = function(baud,databits,parity)  -- function called when the SerialServer is opened  
  print("Virtual Serial Port Connected | Baud: "..baud.." Data Bits: "..databits.." Parity: "..parity)  
  Serial:Event(SerialPorts.Events.Connected)  -- connected event sent to serial client  
end  
  
Serial.OnClose = function()  -- function called when the SerialServer port closes  
  print("Virtual Serial Port Closed")  
  Serial:Event(SerialPorts.Events.Closed)  -- closed event sent to serial client  
end  
  
Serial.Data = ParseResponse  -- ParseResponse is called when Serial has data  
  
  
-- TCP Socket Callbacks  
Server.Connected=function()  -- function called when the TCP socket is connected  
  print("TCP Socket Connected to: "..IPAddress..":"..Port)  
end  
  
Server.Reconnect=function()  -- function called when the TCP socket is reconnected  
  print("TCP Socket Reconnecting to: "..IPAddress..":"..Port)  
end  
  
Server.Data=function()  -- function called when the TCP socket has data  
  print("TCP Socket has data")  
end  
  
Server.Closed=function()  -- function called when the TCP socket is closed  
  print("TCP Socket Closed")  
end  
  
Server.Error=function(server,err)  -- function called when the TCP socket has an error  
  print("TCP Socket has an Error: "..err)  
end  
  
Server.Timeout=function()  -- function called when the TCP socket times out  
  print("TCP Socket has Timedout")  
end  
  
  
-- Start at runtime  
Initialization()  -- calls the Initialization function at the start of runtime
```

[Serial Client Code](javascript:void(0))

```lua
-- Aliases  
Send = Controls.Send  
Count = Controls.Count  
AutoSend = Controls.AutoSend  
  
  
-- Constants  
Poll = Timer.New()  -- create new timer object  
PollTime = 1  -- variable that will be used when starting a timer and setting the timer   
Server = TcpSocketServer.New()  -- create new TCP server object  
Port = 4888  -- variable that will be used when defining the TCP port  
Serial = SerialPorts[1]  -- create new SerialPort object  
Baud = 9600  -- variable that will be used for the baud rate  
DataBits = 8  -- variable that will be used for the data bits  
Parity = "N"  -- variable that will be used for parity  
  
  
-- Functions  
function SendData()  -- function to write to the serial port if it is open  
  print("Sending: "..Count.Value)  
  if Serial.IsOpen then Serial:Write(Count.Value) end  
end  
  
function ParseResponse(TcpSocket)  -- function to read the TCP socket  
  local data = tonumber(TcpSocket:Read(TcpSocket.BufferLength))  
  if data then print("Recieved Data: "..data) Count.Value = data end  
end  
  
function SetPollTimer()  -- function to start/stop the poll timer  
  if AutoSend.Boolean == true then SendData() Poll:Start(PollTime) else Poll:Stop() end  
end  
  
function SocketHandler(TcpSocket,event) -- function that sets the TCP socket instance data callback to the ParseResponse function   
  TcpSocket.Data = ParseResponse  
  print("Sock "..event)  
end  
  
function Initialization()  -- function that is called at the start of runtime  
  print("Initializing plugin")  
  Serial:Open(Baud,DataBits,Pairty)  -- Open the serial port  
  print("Opening Serial Port | Baud: "..Baud.." Data Bits: "..DataBits.." Parity: "..Parity)  
  Server:Listen(Port) -- This listen port is opened on all network interfaces  
  print("TCP Socket Server listening on port: "..Port)  
end  
  
  
-- Serial Port Callbacks  
Serial.Connected=function()  -- functin called when the serial port is connected  
  print("Serial Port Open")  
  SetPollTimer()  -- calls SetPollTimer when the serial port is connected  
end  
  
Serial.Reconnect=function()  
  print("Serial Port Reconnecting")  
end  
  
Serial.Data=function(serial,data)  
  print("Serial Port has data: "..data)  
end  
  
Serial.Closed=function()  
  print("Serial Port Closed")  
end  
  
Serial.Error=function(serial,err)  
  print("Serial Port Error: "..err)  
end  
  
Serial.Timeout=function(serial,err)  
  print("Serial Port Timeout: "..err)  
end  
  
  
-- EventHandlers  
Server.EventHandler = function(TcpSocket) -- the properties of this socket instance are those of the TcpSocket library  
  print("TCP Server connected on port: "..Port)  
  TcpSocket.EventHandler = SocketHandler  -- sets TCP socket instance EventHandler to call the SocketHandler function  
end  
  
AutoSend.EventHandler = SetPollTimer  
Send.EventHandler = SendData  
Poll.EventHandler = SendData  
  
  
-- Start at Runtime  
Initialization()
```

## Using the Example

The purpose of this example is to send an integer from the **Serial Client** to the Serial Server, have the **Serial Server** increment the integer, and send it back to the **Serial Client** via a TCP connection to the loopback address. The process then starts over. The integer will be incremented to 10, and then reset back to 1. Use the **Send** button to send the value or toggle the **AutoSend** button to send the values automatically on a timer.
