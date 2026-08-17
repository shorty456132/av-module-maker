# TCPSocket Debugging

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Code_Examples/TCPSocket_Debugging.htm

# TCPSocket Debugging

It is often necessary to debug communication of a TCPSocket object within a Lua script. This topic covers several steps to take to verify and troubleshoot issues.

[Common Issues](javascript:void(0))

### Connection

The most common TCP/IP errors relate to connection problems.

* Confirm the IP address and port are correct.
* Double-check login credentials.
* Verify the remote device is online and available.
* Verify that both remote device and the Q-SYS Core are running on the same network segment.
* Confirm there is a valid route from one to the other.
* Verify switches and routers are online.

### Script Errors

Errors within the script can cause it to stop operating or misbehave. Within Q-SYS Designer Software, the Inspector is at the bottom of the Design Elements pane. The Inspector lists the loads from plugins and scripts and notes any errors.

The scripting window will open a debug panel when the design is pushed to a Core or is emulated. Plugins have a âShow Debugâ property that can be set to open the debug panel. Use these error messages to trace errors that occur from within the script.

### Unexpected Data

Data that is unexpected or missing a component can often occur. Common issues are unexpected or unhandled end of line characters, tabs, carriage returns, and linefeed values.

[Add Debug Output](javascript:void(0))

The TCPSocket code below is instrumental for debugging. The DebugTx, DebugRx and DebugFunction flags are added to easily turn on and off debugging output. The debug output can be used to trace the process of the plugin, when instrumented in this manner, for debugging issues.

[TCPSocket Debugging](javascript:void(0))

```lua
--Debug flags  
DebugTx, DebugRx, DebugFunction = true, true, true  
  
-- Connection Variables  
IPAddress = "192.168.1.1"  
Port = 10001  
  
-- Sockets  
TCP = TcpSocket.New()    -- Create new TcpSocket object  
TCP.ReadTimeout = 5      -- Set the timeout to 5 seconds  
TCP.WriteTimeout = 5     -- Set the timeout to 5 seconds  
TCP.ReconnectTimeout = 5 -- Set the wait time bfore reconnecting  
  
-- Functions  
-- Helper Functions  
-- Connect the TCP socket to the address  
function Connect()  
  if DebugFunction then print("Connect() called") end  
  TCP:Connect( IPAddress, Port )  
end  
  
-- Returns true if TCP Socket is connected  
function IsConnected()  
  if DebugFunction then print("IsConnect() called") end  
  return TCP.IsConnected  
end  
  
-- When TCPSocket is successfully connected  
function Connected()  
  if DebugFunction then print("Connected() called") end  
  -- On connect functionality  
end  
  
-- When the TCPSocket loses connection  
function Disconnected()  
  if DebugFunction then print("Disconnected() called") end  
  -- On disconnect functionality  
end  
  
-- TCP socket callbacks  
-- Called when TCP socket is connected  
TCP.Connected=function(socket)  
  if DebugFunction then print("TCP Socket Connect handler called") end  
  Connected()  
end  
  
-- Called when TCP socket is reconnecting  
TCP.Reconnect=function(socket)  
  if DebugFunction then print("TCP Socket Reconnect handler called") end  
  Disconnected()  
end  
  
-- Called when TCP socket is closed  
TCP.Closed=function(socket)  
  if DebugFunction then print("TCP Socket Closed handler called") end  
  Disconnected()  
end  
  
-- Called when TCP socket has an error  
TCP.Error=function(socket, err)  
  if DebugFunction then print("TCP Socket Error handler called: " .. err) end  
  Disconnected()  
end  
  
-- Called when TCP socket times out  
TCP.Timeout=function(socket)  
  if DebugFunction then print("TCP Socket Timeout handler called") end  
  Disconnected()  
end  
  
-- Called when the TCPSocket receives data from remote device  
TCP.Data = function(socket)  
  if DebugFunction then print("TCP Socket Data handler called") end  
  ParseResponse()  -- Call ParseResponse when the TCP socket has data  
end  
  
-- Use the TCPSocket to send cmd to the remote device  
function Send(cmd)    
  if DebugFunction then print("Send() called") end  
  if TCP.IsConnected then   -- If the TCP socket is connected write the command and EOL to the socket  
    if DebugTx then print("TX: " .. cmd) end  
    TCP:Write(cmd)   
  else  
    print("Error - Disconnected; unable to send " .. cmd .. EOL)  
  end  
end  
  
--Parsers  
-- Pull the data from the TCPSocket and parse/use it  
function ParseResponse()  
  if DebugFunction then print("ParseResponse() called") end  
  local rx = TCP:Read(TCP.BufferLength)  -- Read the data in the buffer  
  if DebugRx then print("RX: " .. rx) end  
  
  -- Add data handling routines here  
  
end  
  
-- Run at start  
Connect()
```

Use these outputs to confirm the function path is behaving as expected. Output the Tx and Rx and compare the data to the results to find errors in script processing.

In a plugin, the debug flags may be bound to a property to allow the debug output to be turned on or off from within the Q-SYS Design.

[Debug Print Property for Plugins](javascript:void(0))

```lua
function GetProperties()  
  props = {}  
  table.insert(props, {  
    Name = "Debug Print",  
    Type = "enum",  
    Choices = {"None", "Tx/Rx", "Tx", "Rx", "Function Calls", "All"},  
    Value = "None"  
  })  
  return props  
end  
  
--Within the runtime add:  
-- Debugging level  
DebugTx,DebugRx,DebugFunction = false, false, false  
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
```

[TCP Test Script](javascript:void(0))

This Lua script is a simple TCP intended to be built into a Text Controller. Build a Text Controller with two Text inputs named âIP Addressâ and âPortâ, and two buttons named âConnectâ and âTest Commandâ. Remember to disable any other script or plugin that is attempting to connect to the remote device. Only one scripted component can open a TCP port to a specific remote location at a time. This will allow a simple command to be sent with feedback to check that a connection is possible.

[TCP Test Lua Script](javascript:void(0))

```lua
--Initializing  
--Aliases  
button_connect = Controls.Connect  
address = Controls["IP Address"]  
port = Controls.Port  
  
--Variables  
TestCommand = "Hello, World!\n"  
  
--Objects  
sock = TcpSocket.New()  
sock.ReadTimeout = 0  
sock.WriteTimeout = 0  
sock.ReconnectTimeout = 5  
  
--Control Functions  
  
sock.Connected = function(sock)  
  print("TCP socket is connected")  
  button_connect.Color = "green"  
end  
  
sock.Reconnect = function(sock)  
  print("TCP socket is reconnecting")  
end  
  
sock.Data = function(sock)  
  print("TCP socket has data:", sock:Read(sock.BufferLength) )  
end  
  
sock.Closed = function(sock)  
  print("TCP socket was closed by the remote end")  
  button_connect.Color = "red"  
end  
  
sock.Error = function(sock, err)  
  print("TCP socket had an error:", err)  
end  
  
sock.Timeout = function(sock, err)  
  print("TCP socket timed out", err)  
end  
  
function send(cmd)  
  print("Sending: ", cmd)  
  sock:Write(cmd)  
end  
  
Controls["Connect"].EventHandler = function()  
  print(address.String, port.String)  
  sock:Connect(address.String, tonumber(port.String) )  
  button_connect.Color = "yellow"  
end  
  
Controls['Test Command'].EventHandler = function()  
  send(TestCommand)  
end  
  
button_connect.Color = "red"
```

[PuTTy](javascript:void(0))

If communication is not operating as expected within a running or emulated design, using a third-party tool to verify the connection can help with diagnosis. There are many terminal and communication programs â for example, [PuTTy](https://www.putty.org/). PuTTy allows for manually creating TCP/IP connections, with defaults for running raw packet transmission, telnet, and SSH type interfaces. Running PuTTy and manually executing the connection can prove that communication with the remote device is possible and if various commands work.

Note that running PuTTy uses your computerâs network connection. If the configuration of your computerâs network adapter differs from the Coreâs network configuration, the results may differ.

[Wireshark](javascript:void(0))

Another freely available tool is Wireshark. This program captures the data seen on the network to allow debugging of TCP packets. Note that data captured are raw TCP packets with headers and transmission information. Debugging from these packets requires knowledge of the TCP/IP specification.

1. Install Wireshark and bind the necessary communication drivers on your computer, and then open Wireshark.
2. Connect to the network interface that has access to the Q-LAN network with the Core and remote device connection being debugged.
3. Press the Start Capture button.
4. Return to the Q-SYS design and run the process that should cause communication between the Core and the remote device.
5. Return to Wireshark and search for the communication packets. A common filter that will make it easier to see specific communication of the device is:

   ip.dst==192.168.1.1 or ip.src==192.168.1.1

   \*where 192.168.1.1 is the address of the remote device.

This should show just TCP/IP packets going to or being sent by the device. After completing this, you can stop the capture and save the captured data. The captured data can help when getting assistance diagnosing these issues.
