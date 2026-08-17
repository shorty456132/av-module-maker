# SerialServerPorts

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/SerialServerPorts.htm

# SerialServerPorts

Use the SerialServerPorts library to emulate the functionality of Q-SYS hardware Serial Port components, while internally redirecting connection state and data bidirectionally to and from a remote serial server device. SerialServerPorts allows you to bridge the gap between serial wiring and Lua TcpSocket library paradigms.

If you already have a script that successfully interfaces with RS-232-controlled gear using native Q-SYS serial ports, it can now be wired to a Virtual Serial Port, which establishes a communication path to a remote networked device port. This port acts as a serial tunnel to the remote physical serial port.

**Note:** To use the SerialServerPorts library in a Lua script, you must expose Virtual Serial Ports in a supported Q-SYS scripting component: [Text Controller](../../Schematic_Library/device_controller_script.htm) or [Control Script](../../Schematic_Library/control_script_2.htm). Refer to these topics for more information.

[Properties](javascript:void(0))

`.IsOpen` : Read-only. Returns true if the port is connected.

`.BufferLength` : Read-only. Number of bytes of data in the buffer.

[Methods](javascript:void(0))

[Event()](javascript:void(0))

Trigger an EventHandler in the associated serial âclient scriptâsâ serial EventHandler logic.

### Description

Issuing this command triggers the associated EventHandler in the virtual serial client script. For the Error event, you can optionally send a string containing more information about the error condition.

### Syntax

:Event( SerialEvent [, error] )

### Arguments

`SerialEvent` : Integer. One of the events referenced in the [SerialPorts.Events Table](#SerialPo).

`error` : String. When using the Error event type, an optional explanation of the error condition.

### Example

```lua
ser = SerialServerPorts[1]  
sock = TcpSocket.New()  
sock.Connected = function()  
    ser:Event( SerialPorts.Events.Connected )  
end  
sock.Closed = function()  
    if ser.IsOpen then  
        ser:Event(SerialPorts.Events.Closed)  
    end  
end  
ser.OnOpen = function()  
    sock:Connect("192.168.1.254",1234)  
end
```

[Write()](javascript:void(0))

Writes data to the socket. Raises error if serial port is not open or device hosting serial port is disconnected from network.

### Description

Writes specified data to the client's serial port buffer. Raises an error if the port is not open.

### Syntax

:Write( data )

### Arguments

`data` : String. The data to send.

### Response

`error` : String. nil if open succeeded, otherwise a string representing the error.

### Example

```lua
ser = SerialServerPorts[1]  
ser:Open(9600)  
e = ser:Write("data out to serial port")if e then print("error:"..e) end
```

[Read()](javascript:void(0))

Attempts to read up to 'length' bytes from serial buffer. Any bytes read are removed from the buffer.

### Description

Attempts to read up the 'length' bytes from the serial buffer. Data is removed from the buffer. This buffer contains data bytes written by the serial client script.

### Syntax

:Read( length )

### Arguments

`length` : Integer. The number of bytes to read from the serial buffer.

### Response

`data` : String. The data read from the socket. Nil if the buffer is empty.

### Example

```lua
ser:Read( 10 ) --Receive up to 10 bytes of data.
```

[ReadLine()](javascript:void(0))

Attempts to read a 'line' from the serial buffer. Retrieved data is removed from the buffer.

### Description

Attempts to read a 'line' from the serial buffer. 'EOL' is defined in the table below. '<custom>' is an optional string used by EOL.Custom.

**Note:** This method is typically never used to get data bytes from the virtual serial buffer to be completely transparent between the serial client script and the remote serial port. Normally, every byte received from the vitual serial port is read from the buffer by the :Read method using the .BufferLength property and immediately sent to the TcpSocket connection using the :Write command. Likewise, on the TcpSocket's DATA EventHandler, the :Read method would also immediate remove all bytes from the TcpSocket buffer and :Write them, as a whole, to the virtual serial port.

### Syntax

:ReadLine( EOL [, <custom> )

### Arguments

`EOL` : Predefined constant. One of the defined EOL types. See definitions in [SerialPorts.EOL Table](#SerialPo2).

`<custom>` : String. An EOL string used only with the 'Custom' EOL type. This argument is not used for any other EOL type.

### Response

`data` : String. The data read from the socket. Nil if the read failed.

### Example

```lua
ser:ReadLine( CrLf ) --Receive data until a <CR><LF> or <LF> is reached  
ser:ReadLine( Custom, '.') --Receive data until a period is reached
```

[Search()](javascript:void(0))

Searches the serial buffer for string 'str' (starting at 'start\_pos') and returns the index of where str is found.

### Description

Searches the virtual serial port's buffer for string 'string' (starting at integer 'start\_pos') and returns the index of where 'string' is found. 'start\_pos' defaults to 1.

**Note:** This method should rarely be used for the intended purpose of the SerialServerPorts library. It is documented here for completeness.

### Syntax

:Search( string [, start\_pos] )

### Arguments

`str` : String. The string to search for.

### Response

`data` : Integer. Nil if 'str' not found, otherwise the index of the first character of where the search string is found.

### Example

```lua
ser = SerialServerPorts[1]  
-- Assuming serial buffer contains 'all your base'  
index = ser:Search('base') --Search for the sequence 'base'  
-- index at this point would equal 10, which is the first character  
-- of the found sequence
```

[SerialServerPorts Callbacks](javascript:void(0))

| Name | Function Signature | Description |
| --- | --- | --- |
| .OnOpen | function( baudRate,dataBits, parity ) | Assign a function which is called upon a serial connection Open command. Although the dataBits and parity parameters are optional for the serial port client script, they are always passed into this function, so that the default for the optional parameters may be used by the virtual serial server script. |
| .OnClose | function( ) | Assign a function which is called upon a :Close request from the attached serial client script. There are no parameters passed into the function. |
| .Data | function( ) | Assign a function which is called when there is new data in the virtual serial port buffer. |

[SerialPorts.Events Table](javascript:void(0))

| Name | Description |
| --- | --- |
| Connected | Alerts the serial client script that the connection is open. |
| Closed | Commands the serial client's serial port object that it should close the port connection, which results in triggering the Closed EventHandler. |
| Error | Alerts the serial client script that an error has occurred. There is an optional second argument to allow a string to be passed to the serial client's Error EventHandler logic. This Error event is only controlled by the logic of the serial server script. So the programmer of the server script must determine what constitutes an error condition, when to issue this command and what the error message says. |
| Timeout | Alerts the serial client script has experienced a timeout. |
| Reconnect | Alerts the serial client script that a reconnect attempt is in progress. |

[SerialPorts.EOL Table](javascript:void(0))

| Name | Description |
| --- | --- |
| Any | The end of line is any sequence of any number of carriage return and/or linefeed characters. This is the appropriate choice if the protocol uses simply a carriage return as the end of message. |
| CrLf | The end of the line is an optional carriage return, followed by a linefeed. (In other words, it is either a "\r\n" or a "\n".) This format is useful in parsing text-based Internet protocols, since the standards generally prescribe a "\r\n" line-terminator, but nonconformant clients sometimes use just "\n". |
| CrLfStrict | The end of the line is an optional carriage return, followed by a linefeed. (In other words, it is either a "\r\n" or a "\n".) This format is useful in parsing text-based Internet protocols, since the standards generally prescribe a "\r\n" line-terminator, but nonconformant clients sometimes use just "\n". |
| Lf | The end of a line is a single linefeed character. (This is also known as "\n". It is ASCII value is 0x0A.) |
| Null | The end of line is a single byte with the value 0âââan ASCII NUL. |
| Custom | The end of line is defined by the string passed into the ReadLine() method. |

[Example](javascript:void(0))

```lua
-- Constants  
IP="127.0.0.1" -- The IP address or DNS name of the destination TCP Serial Server device  
Port=1234 -- The TCP port which represents the destination serial port.  
PARITY = { N="None", E="Even", O="Odd", M="Mark", S="Space" } -- A lookup for the SerialPorts :Open() parity abbreviations  
  
-- Variables  
Reconnecting = false  
serialconnectcount = 0  
  
-- Virtual Serial Port  
ser = SerialServerPorts[1]  
  
-- TCP Socket to Serial Server --  
svr = TcpSocket.New()  
  
  -- ReadTimeout needs to be set here because there is no ReadTimeout in the SerialPorts library  
svr.ReadTimeout = 5 -- 5 Seconds, This value should be non-zero and is dependent upon the serial device API's busyness.  
  
svr.WriteTimeout = 0 -- Disabled (0 is default if not specified) - WriteTimeout can be used, but is optional  
  
-- ReconnectTimeout must be set to 0 to allow automatic reconnection from the SerialPorts client script  
svr.ReconnectTimeout = 0 -- Disabled (0 is default if not specified)  
  
-- Virtual Serial Port EventHandlers  
ser.OnOpen = function( baudrate, dataBits, reqparity )  
  print( string.format( "Virtual Serial .OnOpen: baudrate=%i, dataBits=%i, parity=%s", baudrate, dataBits, PARITY[reqparity] ) )  
  print( string.format( "Attempting to connect to TCP Server port: svr:Connect(\"%s\",%i)", IP, Port ) )  
  svr:Connect(IP,Port)  
end  
  
ser.OnClose = function()  
  print( "Serial OnClose: Now closing our end to be available for reconnection." )  
  if svr.IsConnected then  
    print( "Closing TCP Socket to Serial Server" )  
    svr:Disconnect()  
  end  
end  
  
ser.Data = function()  
  local rxdata = ser:Read( ser.BufferLength )  
  if svr.IsConnected and ser.IsOpen then  
    local prettyfied=rxdata:gsub( "%[CR%]","[CR]\r" )  
    print( "Sending Virtual Serial data to TCP:"..prettyfied )  
    svr:Write( rxdata )  
  end  
end  
  
-- TcpSocket EventHandlers  
svr.EventHandler = function( sock, evt, err )  
  if evt == TcpSocket.Events.Connected then  
    print( "TCP Socket Connected. Sending Connected to Serial")  
    ser:Event( SerialPorts.Events.Connected )  
  elseif evt == TcpSocket.Events.Reconnect then  
    print( "TCP socket reconnecting" )  
    if ser.IsOpen then ser:Event( SerialPorts.Events.Reconnect ) end  
  elseif evt == TcpSocket.Events.Data then  
    local data = sock:Read( sock.BufferLength )  
    local prettyfied=data:gsub( "%[CR%]","[CR]\r" )  
    print( "Sending TCP data to Virtual Serial Port:\r"..prettyfied )  
    ser:Write(data)  
  elseif evt == TcpSocket.Events.Closed then  
    print( "TCP socket closed by remote",ser.IsOpen )  
    if ser.IsOpen then ser:Event( SerialPorts.Events.Closed ) end  
  elseif evt == TcpSocket.Events.Error then  
    print( "TCP socket closed due to error" )  
    if ser.IsOpen then ser:Event( SerialPorts.Events.Error ) end  
  elseif evt == TcpSocket.Events.Timeout then  
    print( "TCP socket closed due to timeout" )  
    if ser.IsOpen then  
      ser:Event( SerialPorts.Events.Timeout )  
      Timer.CallAfter(function()  
        print("Closing Virtual Serial Port to allow serial client to reconnect (automatically)")  
        ser:Event( SerialPorts.Events.Closed )  
        print("Waiting for client script connection to Virtual Serial Port...")  
      end,.1)  
    end  
  end  
end  
print("Waiting for client script connection to Virtual Serial Port...")
```
