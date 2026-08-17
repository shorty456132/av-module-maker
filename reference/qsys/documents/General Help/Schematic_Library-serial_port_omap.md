# Serial Port (DCIO/DCIO-H)

> Source: https://help.qsys.com/Content/Schematic_Library/serial_port_omap.htm

# Serial Port (DCIO/DCIO-H)

The RS-232 Serial Port component allows you to make a connection to the RS-232 connector for Lua Scripting. When a connection is made, and an appropriate [Lua script](../Control_Scripting/Scripting_Solutions.htm#Serial_Port) written, you can control and read from devices such as DVD players, recording hardware, video, lighting, and so on. Connections are made through a three-position Euro-style connector.

[RS-232 Connection](javascript:void(0))

|  |  |
| --- | --- |
|  | Pinout  * TX (Transmit) * RX (Receive) * GND (Signal Ground)   You must check the pinout of any equipment, including the cable, to be connected to a Q-SYS serial port for input or output. Many times in serial troubleshooting, problems may be solved by inserting a "null-modem" adapter or cable to swap the TX and RX pin positions. The TX pin on one end MUST be connected to an RX pin on the other and vise-verse for data to flow properly. |

[Inputs and Outputs](javascript:void(0))

#### Inputs

There are no input pins available for the Serial Port component.

#### Outputs

**Serial Port**
- Connects to the [Control Script](control_script_2.htm), [Command Buttons](command_buttons.htm), and [Text Controller](device_controller_script.htm) components. These components must be configured for Serial Port input. Serial ports are represented by the following symbol , and wiring is represented by a thin black line.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

The Serial Port has no unique Properties.

[Controls](javascript:void(0))

#### TX Bytes

Displays a running total of the number of bytes sent.

#### RX Bytes

Displays a running total of the number of bytes received.

#### Reset

Resets both TX Bytes and RX Bytes to zero.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Receive Bytes | Text Box | | | Output |
| Reset | Trigger | | | Input / Output |
| Transmit Bytes | Text Box | | | Output |
