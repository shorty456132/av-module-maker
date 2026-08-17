# SerialPorts

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/SerialPorts.htm

# SerialPorts

Serial port communication is supported via the RS-232 ports on some Q-SYS devices. You can use a scripting component, including Control Script and Block Controller, to create a serial port connection in Q-SYS.

The following content describes creating a serial connection with the Control Script component. To see an example of creating a serial connection with the Block Controller component, see [Block Examples](../../Schematic_Library/device_controller.htm#Block).

## Creating a Serial Connection with Control Script

To access serial communications, Serial Inputs must be enabled (not 0) in the [Control Script's](../../Schematic_Library/control_script_2.htm) Properties. The Q-SYS device's Serial Port component is then dragged into the design's schematic and wired to the Control Script. In the script itself, there is no 'New' SerialPort method because SerialPort objects are automatically created for you whenever a Q-SYS device's serial port Inventory component is wired into the ControlScript block.

**Note:** Serial functionality is only available when deployed to a Q-SYS Core and is not available via emulation like many other Q-SYS Lua extensions.

## Callbacks

Optional callback functions may be defined instead of using the singular EventHandler. Depending upon the application, defining separate functions for each event may be preferable. The choice to use either a single EventHandler to capture all socket events or separate callback functions is up to the programmer. There is no need to change a functioning script because this new functionality exists and you may choose to never use it. But some programmers may feel that the callback method better matches their logical style. See the equivalent example in [TcpSocket](TcpSocket.htm). The TcpSocket callback function usage is identical to SerialPorts.

## Reference Tables

| SerialPorts Properties | | |
| --- | --- | --- |
| Name | Notes | Description |
| .EventHandler | Signature of function is 'function( port, event )' | Function called on any serial event. See definition of 'event' in the table below. |
| .IsOpen | Read-Only | Returns true if port is connected |
| .BufferLength | Read-Only | Number of bytes of data in buffer |

| SerialPorts Methods | | |
| --- | --- | --- |
| Name | Arguments | Description |
| [:Open](#Open) | ( baudRate [,dataBits] [, parity] [,stop bits] ) | Attempts to open the serial port with the specified baud rate (up to 230400 bits per second).  dataBits - optional: 7, 8. Default = 8.  parity - optional with dataBits: "N" (None, default), "E" (Even), "O" (Odd).  stop bits - optional with dataBits and parity: 1 to one stop bit, 2 for two stop bits. |
| [:Close](#Close) | N / A | Closes the serial port |
| [:Write](#Write) | ( data ) | Writes specified data to the serial port. Raises error if port is not open. |
| [:Read](#Read) | ( length ) | Attempts to read up the 'length' bytes from serial buffer. Data is removed from serial buffer. |
| [:ReadLine](#ReadLine) | ( EOL, <custom> ) | Attempts to read a 'line' from the serial buffer. 'EOL' is defined in the table below. '<custom>' is an optional string only used by EOL.Custom. |
| [:Search](#Search) | ( string, [start\_pos] ) | Searches the serial buffer for string 'str' (starting at integer 'start\_pos') and returns the index of where 'str' is found. 'start\_pos' defaults to 1. |

| SerialPorts.Events Table | |
| --- | --- |
| Name | Description |
| Connected | The port is now open |
| Reconnect | The Core is attempting to reconnect to the port |
| Data | There is new data in the serial buffer |
| Closed | The port was closed due to an error. The second argument (msg) to the EventHandler will have more information, which can be printed to catch the error message. |
| Error | The socket was closed due to error. The error argument to the EventHandler will have more information, which can be displayed if a variable was created to catch the error message. |
| Timeout | A read or write timeout was triggered and the port was closed. |

| SerialPorts Callbacks | | |
| --- | --- | --- |
| Name | Function Signature | Description |
| .Connected | function( *serialTable* )' | Assign a function which is called upon connection to the serial port |
| .Reconnect | function( *serialTable* )' | Assign a function which is called when socket is attempting to reconnect to the serial port |
| .Data | function( *serialTable*)' | Assign a function which is called when there is new data available in the serial buffer |
| .Closed | function( *serialTable* )' | Assign a function which is called when the serial port is closed |
| .Error | function( *serialTable, error* )' | Assign a function which is called when the serial port is closed due to error. The error argument in the function will contain more information, which can be displayed if a variable was created to catch the error message. |
| .Timeout | function( *serialTable*, error)' | Assign a function which is called when a read or write timeout is triggered and the serial port was closed. |

| SerialPorts.EOL Table | |
| --- | --- |
| Name | Description |
| Any | The end of line is any sequence of any number of carriage return and/or linefeed characters. This is the appropriate choice if the protocol uses simply a carriage return as the end of message. |
| CrLf | The end of the line is an optional carriage return, followed by a linefeed. (In other words, it is either a "\r\n" or a "\n".) This format is useful in parsing text-based Internet protocols, since the standards generally prescribe a "\r\n" line-terminator, but nonconformant clients sometimes use just "\n". |
| CrLfStrict | The end of a line is a single carriage return, followed by a single linefeed. (This is also known as "\r\n". The ASCII values are 0x0D 0x0A). |
| Lf | The end of a line is a single linefeed character. (This is also known as "\n". It is ASCII value is 0x0A.) |
| Null | The end of line is a single byte with the value 0âââan ASCII NUL. |
| Custom | The end of line is defined by the string passed into the ReadLine() method. |

#### Open()

#### **Purpose:**Opens the serial port for reading and writing

#### **Parameter:** baudRate

#### **Type:** integer

#### **Definition:** The baud rate to use for sending and receiving data. Maximum baud rate is 230400

#### dataBits

#### **Type:** integer

#### **Definition:** Optional - The number of data bits

#### **Definition:** 8 (default), 7

#### **Example:**

```lua
ser = SerialPorts[1]  
ser:Open(9600) -- Opens serial port at 9600 baud.
```

#### Close( )

#### **Purpose:**Closes the serial port.

#### Write( data )

#### **Purpose:**Writes data to the socket. Raises error if serial port is not open or device hosting serial port is disconnected from network.

#### **Parameter:** data

#### **Type:** string

#### **Definition:** The data to send

#### **Response:**error

#### **Type:** string

#### **Definition:** nil if open succeeded, otherwise a string representing the error

#### **Example:**

```lua
ser = SerialPorts[1]  
ser:Open(9600)  
e = ser:Write("data out to serial port")  
if e then print("error:"..e) end
```

#### Read( length )

#### **Purpose:**Attempts to read up to 'length' bytes from serial buffer. Any bytes read are removed from the buffer.

#### **Parameter:** length

#### **Type:** integer

#### **Definition:** The number of bytes to read from the serial buffer.

#### **Response:**data

#### **Type:** string

#### **Definition:** The data read from the socket. Nil if the buffer is empty

```lua
ser:Read( 10 ) --Read up to 10 bytes of data.  
ser:Read(ser.BufferLength) --Read the whole buffer
```

#### ReadLine( EOL, <custom> )

#### **Purpose:**Attempts to read a 'line' from the serial buffer. Retrieved data is removed from the buffer.

#### **Parameter:** EOL

#### **Type:** predefined constant

#### **Definition:** One of the defined EOL types. See definitions in the [SerialPorts.EOL Table](#SerialPorts.EOLTable) above.

#### <custom>

#### **Type:** string

#### **Definition:** An EOL string used only with the 'Custom' EOL type. This argument is not used for any other EOL type

#### **Response:**data

#### **Type:** string

#### **Definition:** The data read from the socket. Nil if the read failed.

```lua
ser:ReadLine( SerialPorts.EOL.CrLf ) --Read data until a <CR><LF> or <LF> is reached  
ser:ReadLine( SerialPorts.EOL.Custom, '.') --Read data until a period is reached
```

#### Search( str, [start\_pos] )

#### **Purpose:**Searches the serial buffer for string 'str' (starting at 'start\_pos') and returns the index of where str is found

#### **Parameter:** str

#### **Type:** string

#### **Definition:** The string to search for

#### **Response:**data

#### **Type:** integer

#### **Definition:** Nil if 'str' not found, otherwise the index of the first character of where the search string is found

#### **Example:**

```lua
ser = SerialPorts[1]  
-- Assuming serial buffer contains 'all your base'  
index = ser:Search('base') --Search for the sequence 'base'  
-- index at this point would equal 10, which is the first character  
-- of the found sequence
```

## Example

**Tip:** It is best practice to loop on ReadLine(), checking for nil each loop. This ensures that no data is lost.

```lua
sp = SerialPorts[1]  
  
sp.EventHandler = function( port, msg )  
  if msg == SerialPorts.Events.Data then  
    local line = port:ReadLine(SerialPorts.EOL.Null)  
    while line ~= nil do  
      print( "read line", line)  
      line = port:ReadLine(SerialPorts.EOL.Null)  
    end  
  end  
end  
  
data = "ABCDEFG\0"  
idata = 1  
   
Controls.Inputs[1].EventHandler = function()  
  if not sp.IsOpen then  
    sp:Open( 9600, 8, "N")  
  end  
  local tx = string.sub(data, idata, idata)  
  print( "send", tx)  
  sp:Write( tx)  
  idata = idata + 1  
  if idata > #data then idata = 1 end  
end
```
