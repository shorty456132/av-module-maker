# Test External Controls

> Source: https://help.qsys.com/Content/External_Control_APIs/ECP/Test_External_Controls.htm

# Test External Controls

When the controls within Q-sys have been selected and named (see [Named Controls](../../Schematic_Library/external_control.htm)) you can test their functionality over a Telnet connection. This topic describes how to do this.

**Note:** An External Control client must communicate with the Q-SYS Core at least once every 60 seconds, or the socket connection will be closed by the Core. This is a form of "keep-alive" to make sure that abandoned connections get reclaimed by the Core. Most client programs poll a Change Group at a much higher rate which serves as a keep-alive. If not, the client program can issue a "Status Get" command periodically, or a "Control Set Value" on an unused control if no return response is desired.

[Telnet to Local Host](javascript:void(0))

1. In Q-SYS Designer, open the design file with the controls set up for external control. (see [Named Controls](../../Schematic_Library/external_control.htm))
2. Press F6 to enter Emulate mode. If you are not in Emulate mode, you can't open the localhost port.
3. Open a Command Prompt window.
4. At the command prompt type:  
   `telnet`  
   `open localhost 1702`
5. Type the desired commands according to the [ECP Commands](ECP_Commands.htm). For example, using a Gain control named "gain1":

**Note:** Control IDs are case sensitive, and if there is a space in the name you must enclose the entire name in double quotes â "My Control".

1. Type:   
   `get gain1`  
   Returns:  
   `cv "gain1" "-20.0dB" -20 0.444444`"
2. Type:   
   `csv gain1 5`  
     
   Returns:  `cv "gain1" "5.00dB" 5 0.75`

6. If everything is working, the control addressed changes to the new value, position, etc.

[Telnet to a Live Core](javascript:void(0))

1. In Q-SYS Designer, load the design with the controls set up for external control.
2. Press F5 to enter Run mode.
3. Open a Command Prompt window.
4. At the command prompt type:  
   `telnet`  
   `open <hostname of Core>.local 1702`  
   OR  
   `open <IP address> 1702`
5. Type the desired commands according to the [ECP Commands](ECP_Commands.htm). For example, using a Gain control named "gain1":
   1. Type:   
      `get gain1`  
      Returns:  
      `cv "gain1" "-20.0dB" -20 0.444444`"
   2. Type:   
      `csv gain1 5`  
        
      Returns:  `cv "gain1" "5.00dB" 5 0.75`
6. If everything is working, the control addressed changes to the new value, position, etc.
