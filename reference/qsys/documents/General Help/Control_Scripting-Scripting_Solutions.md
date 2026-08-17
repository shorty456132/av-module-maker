# Scripting Solutions

> Source: https://help.qsys.com/Content/Control_Scripting/Scripting_Solutions.htm

# Scripting Solutions

This topic contains a number of actual solutions using Lua Scripting in Q-SYS Designer.

[Radio Buttons](javascript:void(0))

In Q-SYS Designer there are a number of places that have a group of toggle type buttons that operate independently. For example, the Mixer Solo buttons. At times you may find a reason to have these buttons act like radio buttons. With the following script, you can make a group of toggle type buttons into radio buttons, allowing only one button active at a time. The Control Pin outputs of the buttons in the group connect to the Script inputs. In this example the Solo buttons normally act independently, with the script, they now function like radio buttons.

### Lua Script

```lua
-- Radio Buttons, turn off all but the control that changed  
function exclude( ctl )  
  if ctl.Value == 1 then  
    for i, c in ipairs( Controls.Inputs ) do  
      if c ~= ctl then  
        c.Value = 0  
      end  
    end  
  end  
end  
-- assign function to control change  
   
for ix, ctl in ipairs( Controls.Inputs ) do  
  ctl.EventHandler = exclude  
end
```

[Select Loudest of Two Signals](javascript:void(0))

This script is designed to switch a router to the loudest of two microphone inputs. If a person had two microphones and was moving between the two, this the microphone used is closest to the person speaking. The script can be modified to accept more inputs, and the inputs do not have to be microphones.

### Lua Script

```lua
-- Switch router to signal with greatest level --  
cin_meter1 = Controls.Inputs[1]  
cin_meter2 = Controls.Inputs[2]  
cout_select = Controls.Outputs[1]  
   
-- Compare two values and switch a router to the greater  
   
CompTimer.EventHandler = function()  
  if cin_meter1.Value &gt; cin_meter2.Value then  
    cout_select.Value = 1  
  else  
    cout_select.Value = 2  
  end  
end  
   
-- Every .5 seconds, run comparison  
   
CompTimer = Timer.New()  
Timer:Start( .5 )
```

[Buttons to Select and Play Audio File](javascript:void(0))

The default method of selecting an audio file to play is to use the drop-down list in the Audio Player. This script allows you to select and play a file by pushing a button.

### Lua Script

```lua
-- Play specified files  
-- NOTE: The number of trigger inputs to this script can be  
-- changed without changing the script  
   
files = {  
"A.wav",  
"B.wav",  
"C.wav"  
  
}  
   
cout_file = Controls.Outputs[1]  
cout_play = Controls.Outputs[2]  
   
function play( ctl )  
  print( "play: "..files[ctl.Index] )  
  cout_file.String = files[ctl.Index]  
  cout_play:Trigger()  
end  
   
for i,c in ipairs( Controls.Inputs ) do  
  c.EventHandler = play  
end
```

[Button to Send Text String to Simple TCP/IP Socket](javascript:void(0))

This script connects to the localhost IP address 127.0.0.1 on port 8080 and sends the message "This is a message" using TCP/IP. The example demonstrates the Event/EventHandler model:

* `:Connect` initiates the connection.
* The connection event callback `.Connected` transmits the message using the `:Write` method.
* An Error in the initial connection attempt is handled by the `.Error` callback function.

### Lua Script

```lua
socket = TcpSocket.New()  
  
socket.Connected = function(sock)  
  socket:Write( Controls.Message.String )  
  print(string.format('Sent "%s" and closing socket.', Controls.Message.String ) )  
  socket:Disconnect()  
end  
  
socket.Error = function(sock, err)  
  print("TCP socket had an error and will now close",err)  
  socket:Disconnect() -- prevent further attempts to connect  
end  
  
Controls.Send.EventHandler = function()  
  socket:Connect(Controls["IP Address"].String, Controls.Port.Value)  
end
```

[Serial Port (RS-232) Control Script](javascript:void(0)) 

This sample code activates the Play or Stop function on a TASCAMÂ® DVD player. Details of the commands and checksum are taken from the TASCAMÂ® DVD Player user manual. This is used in conjunction with the [RS-232 Serial Port](../Schematic_Library/serial_port.htm) and [Custom Controls](../Schematic_Library/custom_controls.htm) components.

### Lua Script

```lua
ser = SerialPorts[1]  
   
playMessage = string.char(0x02).."&gt;PLYcFWD 17"..string.char(0x03) --Command to press 'play'  
stopMessage = string.char(0x02).."&gt;STPc 98"..string.char(0x03) --Command to press 'stop'  
   
function play()  
  ser:Write(playMessage)  
  print("Sent Play: "..playMessage)  
end  
   
function stop()  
  ser:Write(stopMessage)  
  print("Sent Stop: "..stopMessage)  
end  
   
ser.EventHandler = function( port, msg )  
  if msg == SerialPorts.Events.Connected then  
    print("Serial port connected")  
  elseif msg == SerialPorts.Events.Data then  
    print( "Response: "..port:ReadLine(SerialPorts.EOL.Custom, string.char(0x03) ))  
  end  
end  
   
ser:Open(9600)  
Controls.Inputs[1].EventHandler = play  
Controls.Inputs[2].EventHandler = stop
```
