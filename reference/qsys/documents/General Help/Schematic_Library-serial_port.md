# Serial Port (Core and I/O Devices)

> Source: https://help.qsys.com/Content/Schematic_Library/serial_port.htm

# Serial Port (Core and I/O Devices)

Q-SYS Core processors and peripherals include an RS-232 connection for extension of Q-SYS Control to third-party devices, such as projectors, TVs, and A/V receivers. You can control and read from these devices using Lua script from a Q-SYS scripting component.

**Tip:** To learn about scripting in Q-SYS, see [Control Scripting](../Control_Scripting/Using_Lua_in_Q-Sys/01_Using_Lua_in_Q-Sys_Overview.htm).

[Supported Q-SYS Hardware](javascript:void(0))

* [NV-32-H (Core Capable) Network Video Endpoint](../Hardware/Video/NV-32-H_Core_Capable.htm)
* [Core Nano](../Hardware/Processing/Core_Nano.htm)
* [Core 8 Flex](../Hardware/Processing/Core_8_Flex.htm)
* [Core 110f](../Hardware/Processing/Core_110f.htm)
* [Core 24f](../Hardware/Processing/Core_24f.htm)
* [Core 510i](../Hardware/Processing/Core_510i.htm)
* [Server Core X10](../Hardware/Processing/Server_Core_X10.htm)
* [Core 610](../Hardware/Processing/Core_610.htm)
* [Server Core X20r](../Hardware/Processing/Server_Core_X20r.htm)
* [Core 5200](../Hardware/Processing/Core_5200.htm)
* [Core 6000 CXR](../Hardware/Processing/Core_6000_CXR.htm)
* [Core 110c](../Hardware/Processing/Core_110c.htm)
* [Core 510c](../Hardware/Processing/Core_510c.htm)

[RS-232 Connections](javascript:void(0))

The Serial Port component represents the RS-232 serial connection pins on the rear of the Q-SYS Core. The connector varies depending on the hardware.

The RS-232 Serial Port Components allow you to make a connection to the RS-232 connectors on the processor for Lua Scripting. When a connection is made, and an appropriate [Serial Port (RS-232) Control Script](../Control_Scripting/Scripting_Solutions.htm#Serial_Port)  written, you can control and read from devices such as DVD players, recording hardware, video, lighting, and so on.

To learn about scripting in Q-SYS, see [Control Scripting](../Control_Scripting/Using_Lua_in_Q-Sys/01_Using_Lua_in_Q-Sys_Overview.htm).

[3-pin Euro](javascript:void(0))

| Pin | Description |
| --- | --- |
| TX | Transmit pin. Connect this pin to the RX (receive) pin on the other device. |
| RX | Receive pin. Connect this pin to the TX (transmit) pin on the other device. |
| Ground | Earth ground reference. |

[3-pin Euro: NV-32-H (Core Capable)](javascript:void(0))

**Note:** On the NV-32-H (Core Capable), the RS-232 and GPIO IN pins share a 5-pin Euro connector. You can use both connection types simultaneously.

| Pin | Description |
| --- | --- |
| TX | Transmit pin. Connect this pin to the RX (receive) pin on the other device. |
| RX | Receive pin. Connect this pin to the TX (transmit) pin on the other device. |
| Ground | Earth ground reference for GPIO input and RS-232 connections. |

[Male DE-9](javascript:void(0))

| Pin | Description |
| --- | --- |
| 2 | RX (Receive) |
| 3 | TX (Transmit) |
| 4 | (I/O-22 only) Provides +5.5VDC @ 70mA |
| 5 | GND (Signal Ground) |

**Note:** All other pins on a Core are not supported.

This signal to DE-9 configuration is known as DTE. All 9-pin D-Shell RS-232 pinned as DTE have this configuration. All PC serial ports are DTE as is the Core. Usually peripherals are DCE, which reverses the receive and transmit pins, allowing a straight-thru cable to be used.

You must check the pinout of any equipment, including the cable, to be connected to a Q-SYS serial port for input or output. Many times in serial troubleshooting, problems may be solved by inserting a "null-modem" adapter or cable to swap the TX and RX pin positions. For custom terminated DE-9 connectors, pins 2 and 3 may need to be swapped on one end of the cable. In any case, a TX pin on one end MUST be connected to an RX pin on the other and vise-versa for data to flow properly.

[Inputs and Outputs](javascript:void(0))

### Input Pins

*This component has no output pins.*

### Output Pins

#### Serial Port

Connect this pin to the Serial Input pin of a Q-SYS scripting component, such as [Block Controller](device_controller.htm), [Text Controller](device_controller_script.htm), or [Control Script](control_script_2.htm). You must configure these components for serial communication.

[Properties](javascript:void(0))

The Serial Port component has no specific configurable properties.

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

#### TX Bytes

Displays a running total of the number of bytes sent.

#### RX Bytes

Displays a running total of the number of bytes received.

#### Reset

Resets both TX Bytes and RX Bytes to zero.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Receive Bytes | Text Box | | | Output |
| Reset | Trigger | | | Input / Output |
| Transmit Bytes | Text Box | | | Output |
