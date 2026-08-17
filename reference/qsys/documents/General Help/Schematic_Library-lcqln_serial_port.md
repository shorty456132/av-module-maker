# Serial Port (QIO Series)

> Source: https://help.qsys.com/Content/Schematic_Library/lcqln_serial_port.htm

# Serial Port (QIO Series)

The QIO Series includes serial port(s) for extension of Q-SYS Control to third-party devices, such as projectors, TVs, and A/V receivers. You can control and read from these devices using Lua script from a Q-SYS scripting component.

**Tip:** To learn about scripting in Q-SYS, see [Control Scripting](../Control_Scripting/Using_Lua_in_Q-Sys/01_Using_Lua_in_Q-Sys_Overview.htm).

[QIO-S4 Serial Port Pinouts](javascript:void(0))

The QIO-S4 features four serial ports:

* COM 1 is configurable in the QIO-S4 Serial Port 1 inventory component Properties for RS232, RS485 Half Duplex TX, RS485 Half Duplex RX, or RS485/422 Full Duplex.
* COM 2-4 ports are dedicated to RS232 communication.

### RS232 Pinout: COM 1 (Configurable), COM 2-4 (Dedicated)

| Pin | Signal Flow | Description |
| --- | --- | --- |
|  | N/A | Signal ground |
| TX | Output | Transmit data |
| RX | Input | Receive data |
| RTS | Output | Ready to Send[1](#When) |
| CTS | Input | Clear to Send[1](#When) |

###### 1. When using hardware flow control.

### RS485 Half Duplex TX or RX Pinout: COM 1 (Configurable)

| Pin | Signal Flow | Description |
| --- | --- | --- |
|  | N/A | Signal ground |
| TX | Input/Output | Differential B- |
| RX | (Unused) | (Unused) |
| RTS | Input/Output | Differential A+ |
| CTS | (Unused) | (Unused) |

### RS485/422 Full Duplex: COM 1 (Configurable)

| Pin | Signal Flow | Description |
| --- | --- | --- |
|  | N/A | Signal ground |
| TX | Output | Differential Z- / Tx- |
| RX | Input | Differential A+ / Rx+ |
| RTS | Output | Differential Y+ / Tx+ |
| CTS | Input | Differential B- / Rx- |

[QIO-FLEX4 Serial Port Pinout](javascript:void(0))

| Pin | Signal Flow | Description |
| --- | --- | --- |
| TX | Output | Transmit data |
| RX | Input | Receive data |
| GND | N/A | Signal ground |
| WT | N/A | Witness Timer (5.5V DC 70 mA max) |

[Inputs and Outputs](javascript:void(0))

### Input Pins

This component has no input pins.

### Output Pins

#### Serial Port

Connect this pin to the Serial Input pin of a Q-SYS scripting component, such as [Block Controller](device_controller.htm), [Text Controller](device_controller_script.htm), or [Control Script](control_script_2.htm). You must configure these components for serial communication.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Amplifier Disabled

(For QIO-FLEX4 only). Enables deactivation of the amplifier functionality of the device, preventing audio amplification or output. Default is No.

#### Com Mode

(For QIO-S4 COM1 / Serial Port 1 only) Select the type of serial communication: RS232 (default), RS485 Half TX, RS485 Half RX, or RS485/422 Full. See the [QIO-S4 Serial Port Pinouts](#QIO-S4) section for more information.

#### Flow Control

(For QIO-S4 only). Select whether to enable or disable flow control on the serial port. The default is Disabled.

[Controls](javascript:void(0))

#### TX Bytes

Displays a running total of the number of transmitted bytes of data.

#### RX Bytes

Displays a running total of the number of received bytes of data.

#### Reset

Click to reset the TX Bytes and RX Bytes counters to zero.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Receive Bytes | (text) | | | Output |
| Reset | (trigger) | | | Input/Output |
| Transmit Bytes | (text) | | | Output |

[Troubleshooting](javascript:void(0))

### Checking Pinouts

Check the pinout of any equipment, including the cable, to be connected to a Q-SYS serial port for input or output. In many cases, you can solve serial communication problems by inserting a null modem adapter or cable to swap the TX and RX pin positions. The TX pin on one end must be connected to an RX pin on the other end (and vice versa) for data to flow properly.

### Proper RS-485/RS-422 Termination

To avoid communication errors with RS-485/RS-422 modes, you must match the terminating resistor's impedance to that of the cable being used. For example, if you are using a 120 Ohm cable, terminate both ends with a 120 Ohm resistor.
