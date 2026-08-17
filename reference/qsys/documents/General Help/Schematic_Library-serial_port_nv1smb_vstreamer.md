# Serial Port (NV-21-HU)

> Source: https://help.qsys.com/Content/Schematic_Library/serial_port_nv1smb_vstreamer.htm

# Serial Port (NV-21-HU)

The NV-21-HU includes an RS-232 connection for extension of Q-SYS Control to third-party devices, such as projectors, TVs, and A/V receivers. You can control and read from these devices using Lua script from a Q-SYS scripting component.

**Tip:** To learn about scripting in Q-SYS, see [Control Scripting](../Control_Scripting/Using_Lua_in_Q-Sys/01_Using_Lua_in_Q-Sys_Overview.htm).

[RS-232 Connection](javascript:void(0))

The Serial Port component represents the RS-232 serial connection pins on the rear of the NV-21-HU.

**Note:** On the NV-21-HU, the RS-232 uses the black 3-pin Euro connector.

| Pin | Description |
| --- | --- |
| TX | Transmit pin. Connect this pin to the RX (receive) pin on the other device. |
| RX | Receive pin. Connect this pin to the TX (transmit) pin on the other device. |
| Ground | Earth ground reference for GPIO input and RS-232 connections. |

[Inputs and Outputs](javascript:void(0))

The Serial Port component represents the **RS 232** connector on the rear of the NV-21-HU.

### Input Pins

This component has no input pins.

### Output Pins

#### Serial Port

Connect this pin to the Serial Input pin of a Q-SYS scripting component, such as [Block Controller](device_controller.htm), [Text Controller](device_controller_script.htm), or [Control Script](control_script_2.htm). You must configure these components for serial communication.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

The Serial Port has no unique Properties. See the [AV I/O (NV-21-HU)](av_io.htm) for Network Video Endpoint Properties.

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
