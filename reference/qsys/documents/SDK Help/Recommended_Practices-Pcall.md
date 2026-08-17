# Pcall

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Recommended_Practices/Pcall.htm

# Pcall

Pcall is a basic Lua function for calling another function in a protected mode. This is akin to a try-catch call in other languages. It should be used when there is a chance of a Lua error that needs to be handled.

## Basic usage

```lua
local callSuccess, result = pcall(functToCall, Arg1, ...)  
if callSuccess then -- call succeeded  
    -- result will equate the first returned value by funcToCall if it has no errors  
    if result ~= nil then  
        -- continue loginc here  
    else  
        --handle possible error if expecting a result  
    end  
else --Call failed, result will contain the error message  
    print("Failed to call functToCall:",result)  
    -- any other error handling here  
end
```

Alternatively, you can use an anonymous function:

```lua
local callSuccess, result = pcall(function()  
    --insert any logic here  
end)  
if callSuccess then -- call succeeded  
    -- continue here  
    -- if there is a return statement then result will equal the first value returned  
else --Call failed, result will contain the error message  
    print("Pcall Failed:",result)  
    -- any other error handling here  
end
```

## When to use

It is recommended to use a pcall when there is the possibility of a Lua error due to user input or an expected behavior.

Pcall should not be used in place of proper input validation and error prevention.

Also, even if a pcall succeeds, the output should still be validated to avoid subsequent Lua errors.

## Examples of recommended usage

[Opening TCP Socket Server](javascript:void(0))

```lua
function Listen()  
  local success, err = pcall(  
    function()  
      -- wrap the listen in a pcall in case port is already in use  
      server:Listen(Controls.Port.Value)  
    end  
  )  
  if success then -- server is listening  
    print("Listening on port " .. tostring(math.floor(Controls.Port.Value)))  
  else -- server couldn't listen, print the error  
    print("Failure to listen to port " .. tostring(math.floor(Controls.Port.Value)) .. ":", err)  
  end  
end
```

[UDP Sockets](javascript:void(0))

```lua
function OpenUdpSocket()  
  local success, err = pcall(  
    function()  
      -- wrap the listen in a pcall in case port is already in use  
      UDP:Open(ip, port)  
    end  
  )  
  if success then -- port is open  
    print("UDP is open at "..ip.." on port " .. tostring(math.floor(port)))  
  else -- server couldn't listen, print the error  
    print("Failure to open UDP at "..ip.." on port " .. tostring(math.floor(port)) .. ":", err)  
    -- common error is that the ip is not valid  
  end  
end  
  
function SendUdpMessage(message)  
  local success, err = pcall(  
    function()  
      UDP:Send(message)  
    end  
  )  
  if success then  
    print("UDP message sent: " .. message)  
  else  
    print("Failure to send UDP message: ", err)   
    -- common error is that the socket is not open  
  end  
end
```

[Opening Serial Ports](javascript:void(0))

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

[DAPI Browser](javascript:void(0))

```lua
function StartDanteBrowser()  
  if System.IsEmulating then  
    print("DanteBrowser is not supported in the emulator")  
    return nil -- Not supported in the emulator; return nil to indicate that the function was not executed successfully  
  else  
    local success, result = pcall(DanteBrowser.New)  
    if success then  
      return result -- result is the DanteBrowser object in this case  
    else  
      print("Error starting DanteBrowser: " .. result)  
      return nil  
      -- common error is that there are no Dante TX or RX components in the design, resulting in Dante being disabled  
    end  
  end  
end
```

[Websockets](javascript:void(0))

```lua
-- Connecting to a websocket  
local success, err =  
    pcall(  
    function()  
        ws:Connect(protocol, host, url, port, sub_protocol, headers)  
    end  
)  
if success then  
    print("Connected to WebSocket server")  
else  
    print("Failed to connect to WebSocket server: " .. err)  
end  
  
-- Writing to a websocket  
local success, err =  
    pcall(  
    function()  
        self.Client:Write(msg)  
    end  
)  
if not success then  
    print("Failed to write to WebSocket server: " .. err)  
end
```
