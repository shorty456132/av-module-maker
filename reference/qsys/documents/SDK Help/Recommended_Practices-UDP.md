# UDP Recommended Practices

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Recommended_Practices/UDP.htm

# UDP Recommended Practices

## Use Cases

[One way communication](javascript:void(0))

In this use case, the Core will send UDP payloads to a fixed destination without expecting any responses.

#### Declare the socket

Globally declare a UdpSocket instance.

**Note:** The socket should be declared globally to prevent it from being cleaned up by the garbage collector and using a large amount of memory compared to declaring, opening, sending, then closing all within another function.

#### Open the socket

Open the socket with no arguments before sending any data. Because we did not declare a sending port, the Core will assign a random available port and will send the packet based on the current state of its network interfaces.

#### Send data

Send data by calling `:Send()` and provide the destination address as a string, port as an integer, and your data as a string.

One Way UDP

```lua
udp = UdpSocket.New() -- instantiate the socket  
  
udp:Open() -- Open the socket  
  
Controls.Send.EventHandler = function() -- When Trigger Button is pressed  
  udp:Send("192.168.0.53",57727,"Hello") -- Send a string to a destination  
end 
```

[Two way communication](javascript:void(0))

In this case, you are sending UDP data to a destination and expecting data to be returned via the sending port.

#### Declare the socket

Globally declare a UdpSocket instance.

**Note:** To avoid any possible issues with garbage collection, do not scope the UdpSocket as a local.

#### Setup event handler for responses

Set the event handler for the socket with some considerations. This function will be called whenever the socket receives data from any source. In this use case, we want to filter by address to ensure we are parsing and reacting to only data coming from the device with which we are communicating.

#### Open the socket

Open the socket with no arguments before sending any data. Because we did not declare a sending port, the Core will assign a random available port and will send the packet based on the current state of its network interfaces.

#### Send Data

Send data by calling `:Send()` and provide the destination address as a string, port as an integer, and your data as a string.

Two Way UDP

```lua
udp = UdpSocket.New() -- instantiate the socket  
IP = "192.168.0.6" -- destination address  
port = 50000 -- destination port  
  
udp.EventHandler = function(udpSocket,packet) -- Called whenever data is received  
  if packet.Address == IP then -- check that this is the device we want to listen to  
    print("RX:"..packet.Data)  
    -- parse your data here  
  end   
end   
  
udp:Open() -- Open the socket  
  
Controls.Send.EventHandler = function() -- When Trigger Button is pressed  
  udp:Send(IP,port,"Hello") -- Send a string to a destination  
end 
```

[UDP Server](javascript:void(0))

In this use case you are listening for UDP packets from other devices or services.

#### Declare the socket

Globally declare a UdpSocket instance.

**Note:** To avoid any possible issues with garbage collection, do not scope the UdpSocket as a local.

#### Setup event handler for responses

Set up the event handler to print the sending address, sending port , and payload of incoming packets. We can use that information to echo the data back to the same address and port for this example.

#### Open the socket

When opening the socket, you can set the first argument to nil so as to not specify a single specific address. This will bind the socket to the specified port on all available network interfaces not already listening on that port explicitly from another script or service.

Basic UDP Server

```lua
udp = UdpSocket.New() -- instantiate the socket  
port = 51001 -- port to listen to  
  
udp.EventHandler = function(socket, packet)  
  print(string.format("%s:%d %s",packet.Address,packet.Port,packet.Data)) -- print address, port and data  
  udp:Send(packet.Address,packet.Port,("Message recieved: "..packet.Data)) -- echo string back  
end   
  
udp:Open(nil ,port) -- listen on all available nics
```

Alternatively, you can set a specific address to bind the socket to. In the following example, the script is actively staying bound to the address of a specific interface - in this case, LAN B. If the interface active state or address changes, the script will automatically open, close, or rebind the socket appropriately.

#### Declare Global Variables to Track Socket State

We will declare a couple variables to track the state of the socket and the last address of when it bound to the port. In this case, it is only looking at LAN B on a Core but you can look at the other examples below, too.

#### Declare a Timer to check the state of the network interface

We will set up a timer to continually check the state of the network interface and react accordingly. We want to open and close the socket when the network interface changes its state. Also, if the network interface changes its address, we want to rebind the socket.

#### Open the socket

When opening the socket, you can set the first argument to the current address of the desired network interface. This will bind the socket to the specified port on only that network interface.

UDP server on specific network interface

```lua
udp = UdpSocket.New() -- instantiate the socket  
port = 51001 -- port to listen to  
  
udp.EventHandler = function(socket, packet)  
  print(string.format("%s:%d %s",packet.Address,packet.Port,packet.Data)) -- print address, port and data  
  udp:Send(packet.Address,packet.Port,("Message recieved: "..packet.Data)) -- echo string back  
end   
  
SocketOpen = false -- track status of the socket  
nicAddress = "" -- track the last address the socket was bound to  
NicTimer = Timer.New() -- declare a timer to check the NICs status  
  
NicTimer.EventHandler = function()  
  nic = Network.Interfaces()[2] -- checking for lan B  
  if (nic and not SocketOpen) or (nic and nicAddress ~= nic.Address) then -- if nic becomes active or the address changes  
    BindToNic(nic)  
  elseif not nic and SocketOpen then -- if nic becomes inactive while the socket is open  
    print("Closing UDP Socket")  
    udp:Close()  
    SocketOpen = false   
    nicAddress = ""  
  end   
end   
  
function BindToNic(nic)  
  if nic and nic.Address then -- check if nic is active and address is defined  
    if SocketOpen then -- if it was previously open, close first  
      udp:Close()  
    end   
    print("Opening UDP on "..nic.Address.." with port "..port)  
    udp:Open(nic.Address,port) -- bind to nic  
    SocketOpen = true -- set our flag high  
    nicAddress = nic.Address -- keep track of the address the socket is bound to  
  end   
end   
  
if not System.IsEmulating then -- Check if not running in emulation  
  NicTimer:Start(1) -- check every second  
end
```

[Receive Broadcasts](javascript:void(0))

In this use case, you need to receive broadcasts on a specific network interface.

#### Declare the socket

Globally declare a UdpSocket instance.

**Note:** To avoid any possible issues with garbage collection, do not scope the UdpSocket as a local.

#### Set up event handler for responses

Set up the event handler to print the sending address, sending port , and payload of incoming packets. You can use that information to echo the data back to the sender directly.

#### Declare Global Variables to Track Socket State

Declare a couple variables to track the state of the socket, the last address of when it bound to the port, and the index of the network interface to which it is bound.

#### Declare a Timer to check the state of the network interface

Set up a timer to continually check the state of the network interface and react accordingly. We want to open and close the socket when the network interface changes its state. Also, if the network interface changes its address, we want to rebind the socket.

#### Open the socket

When opening the socket, you can set the first argument to the current broadcast address of the desired network interface. This will bind the socket to the specified port on only that network interface.

Receive UDP Broadcasts on specified Network Interface

```lua
udp = UdpSocket.New() -- instantiate the socket  
port = 51002  
  
udp.EventHandler = function(udpSocket,packet)  
  print("Received packet from "..packet.Address..":"..packet.Port)  
  print("RX:"..packet.Data)  
  -- parse your data here  
end   
  
selectedNicIndex = nil -- track the currently selected nic index  
SocketOpen = false -- track status of the socket  
nicAddress = "" -- track the last address the socket was bound to  
NicTimer = Timer.New() -- declare a timer to check the NICs status  
  
NicTimer.EventHandler = function()  
  nics = Network.Interfaces() -- get all active networkj interfaces  
  local NicChoices = {} -- instantiate an empty table to add choices to  
  for i,nic in ipairs(nics) do -- add interface names to the choices table  
    table.insert(NicChoices, nic.Interface)  
  end   
  Controls.NicSelection.Choices = NicChoices -- assign the choices to the combobox text control  
  if selectedNicIndex ~= nil then   
    nic = nics[selectedNicIndex] -- checking selected NIC  
    if (nic and not SocketOpen) or (nic and nicAddress ~= nic.BroadcastAddress) then -- if nic becomes active or the address changes  
      BindToNic(nic)  
    elseif not nic and SocketOpen then -- if nic becomes inactive while the socket is open  
      print("Closing UDP Socket")  
      udp:Close()  
      SocketOpen = false   
      nicAddress = ""  
    end  
  elseif Controls.NicSelection.String ~= "" then -- check for nic if there is a selection string but the nic was not found yet  
    GetNicSelection()  
  end   
end   
  
function BindToNic(nic)  
  if nic and nic.BroadcastAddress then -- check if nic is active and address is defined  
    if SocketOpen then -- if it was previously open, close first  
      udp:Close()  
    end   
    print("Opening UDP on "..nic.BroadcastAddress.." with port "..port)  
    udp:Open(nic.BroadcastAddress,port) -- bind to nic  
    SocketOpen = true -- set our flag high  
    nicAddress = nic.BroadcastAddress -- keep track of the address the socket is bound to  
  end   
end   
  
function GetNicSelection()  
  if SocketOpen then -- close socket if previously opened  
    print("Closing UDP Socket")  
    udp:Close()  
    SocketOpen = false   
    nicAddress = ""  
  end  
  local currentSelection = Controls.NicSelection.String -- get current nic selection string  
  if currentSelection ~= "" then    
    for i,nic in ipairs(Network.Interfaces()) do -- iterate through all active network interfaces  
      if currentSelection == nic.Interface then -- if the interface name matches the current selection  
        selectedNicIndex = i -- save the index of the currently selected nic  
        BindToNic(nic) -- bind to that nic  
        return -- return to exit function  
      end   
    end  
  end   
  selectedNicIndex = nil -- if the currently selected nic is not found set the index to nil  
  return   
end   
Controls.NicSelection.EventHandler = GetNicSelection -- update network interface selection on change  
  
GetNicSelection()  
NicTimer:Start(1) -- check every second
```

[Multicast](javascript:void(0))

#### Declare the socket

Globally declare a UdpSocket instance.

**Note:** To avoid any possible issues with garbage collection, do not scope the UdpSocket as a local.

#### Set up event handler for responses

Set up the event handler to print the sending address, sending port , and payload of incoming packets.

#### Declare Global Variables to Track Socket State

Declare a couple variables to track the state of the socket, the last address of when it bound to the port, and the index of the network interface to which it is bound.

#### Declare a Timer to check the state of the network interface

Set up a timer to continually check the state of the network interface and react accordingly. We want to open and close the socket when the network interface changes it state. Also, if the network interface changes its address, we want to rebind the socket.

#### Open the socket

Open the socket with no address specified and a port to match the traffic you expect from the Multicast address. In the example below, it is going to use port 8427 for Shure SLP.

Discover Devices on network via Multicast

```lua
udp = UdpSocket.New() -- instantiate the socket  
udp.EventHandler = function(udpSocket,packet)  
  print("Received packet from "..packet.Address..":"..packet.Port.."\n"..packet.Data)  
  -- parse your data here  
end   
  
selectedNicIndex = nil -- track the currently selected nic index  
SocketOpen = false -- track status of the socket  
nicAddress = "" -- track the last address the socket was bound to  
NicTimer = Timer.New() -- declare a timer to check the NICs status  
  
NicTimer.EventHandler = function()  
  nics = Network.Interfaces() -- get all active networkj interfaces  
  local NicChoices = {} -- instantiate an empty table to add choices to  
  for i,nic in ipairs(nics) do -- add interface names to the choices table  
    table.insert(NicChoices, nic.Interface)  
  end   
  Controls.NicSelection.Choices = NicChoices -- assign the choices to the combobox text control  
  if selectedNicIndex ~= nil then   
    nic = nics[selectedNicIndex] -- checking selected NIC  
    if (nic and not SocketOpen) or (nic and nicAddress ~= nic.Address) then -- if nic becomes active or the address changes  
      BindToNic(nic)  
    elseif not nic and SocketOpen then -- if nic becomes inactive while the socket is open  
      print("Closing UDP Socket")  
      udp:Close()  
      SocketOpen = false   
      nicAddress = ""  
    end  
  elseif Controls.NicSelection.String ~= "" then -- check for nic if there is a selection string but the nic was not found yet  
    GetNicSelection()  
  end   
end   
  
function BindToNic(nic)  
  if nic and nic.Address then -- check if nic is active and address is defined  
    if SocketOpen then -- if it was previously open, close first  
      udp:Close()  
    end   
    print("Opening UDP")  
    udp:Open(nil ,8427) -- Shure Discovery Port  
    SocketOpen = true -- set our flag high  
    nicAddress = nic.Address -- keep track of the address the socket is bound to  
    udp:JoinMulticast("239.255.254.253",nic.Address) -- Shure Discovery Multicast  
  end   
end   
  
function GetNicSelection()  
  if SocketOpen then -- close socket if previously opened  
    print("Closing UDP Socket")  
    udp:Close()  
    SocketOpen = false   
    nicAddress = ""  
  end  
  local currentSelection = Controls.NicSelection.String -- get current nic selection string  
  if currentSelection ~= "" then    
    for i,nic in ipairs(Network.Interfaces()) do -- iterate through all active network interfaces  
      if currentSelection == nic.Interface then -- if the interface name matches the current selection  
        selectedNicIndex = i -- save the index of the currently selected nic  
        BindToNic(nic) -- bind to that nic  
        return -- return to exit function  
      end   
    end  
  end   
  selectedNicIndex = nil -- if the currently selected nic is not found set the index to nil  
  return   
end   
Controls.NicSelection.EventHandler = GetNicSelection -- update network interface selection on change  
  
GetNicSelection() -- check on script start  
NicTimer:Start(1) -- check every second
```

## Data Buffer

There is no buffer for received data like a TcpSocket, so you would need to use your own buffer logic if you don't expect to receive complete payloads each time. This can be achieved with a global variable that concatenates UDP data to then call a function that loops while it can find valid data.

UDP Buffer Example for fixed delimiter

```lua
buffer = ""  
udp.EventHandler = function(socket, packet)  
  buffer = buffer .. packet.Data -- add data to the buffer  
  ProcessBuffer() -- process the buffer  
end   
  
function ProcessBuffer()  
  while buffer:find('\r') do -- loop through valid data  
    local data = buffer:sub(0,buffer:find('\r') - 1) -- pull data from the buffer without delimiter  
    buffer = buffer:sub(buffer:find('\r') + 1) -- remove data from the buffer  
    print(data) -- do something with the data  
  end   
end 
```

## Binding to ports and network interfaces

* You will get an error if you try to bind to an invalid address such as an address outside any subnet the Core is on. You will get the following error: `bind : Cannot assign requested address (99)` or `invalid bind IP : No such file or directory (2)`
* If you open sockets without defining a specific address to listen on, then only the last socket to open will receive data. This is not an issue if you specify an address to listen to when opening the socket.

## Considerations for Core redundancy

* With redundant Cores, the address will change depending on the active Core. The code examples have been tested with redundant Cores but if sending targeted UDP data to the Core, you will need to send data to both Cores to ensure the active Core receives it.

## Differences in Emulation

* When receiving broadcast messages while bound to single address:

  + In Emulation, if a UdpSocket is bound to 192.168.0.5, it will receive data sent to 192.168.0.5 and 192.168.0.255 (subnet broadcast address).
  + On a Core, if a UdpSocket is bound to 192.168.0.5, it will receive data sent to 192.168.0.5 only.
* In Emulation, sending a UDP packet to an invalid destination or port may close the socket. This behavior is not present on a Core.
