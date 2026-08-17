# Ping

> Source: https://help.qsys.com/Content/Schematic_Library/ping.htm

# Ping

Use this component to check whether a device is reachable on the network based on defined parameters.

[Getting Started](javascript:void(0))

1. Drag the Ping component into your schematic.
2. Run your design.
3. Double-click the Ping component to open the control panel.
4. Configure the Ping Settings. See [Ping](#Controls).
5. Click Start.
6. Check the Status box for the ping session results. For more information, see [Ping](#Controls).

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Schematic Example](javascript:void(0))

In this example, we are using a Ping component with its Status control pin exposed wired to a Monitoring Proxy to ping the status.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Ping Properties

This component has no configurable properties.

[Controls](javascript:void(0))

### Ping Settings

#### Host Name

Specify the IP address of the destination device on the network for which you want to check network connectivity.

#### Packet Count

Specify the number of packets to send to the destination host, from 1 to 10 (default is 5).

#### Error Tolerance

Specify the number of packets that have to successfully reach the destination host to return an "OK" status, from 1 to 10 (default is 5). Set this value to be the same or lower than the Packet Count.

#### Ping Interval

Specify the amount of time to elapse before sending the next packet, from 1.00s to 10.0s (default is 1.00s).

#### Timeout

Specify the amount of time to wait for a host to indicate a packet was successfully received, from 2.00s to 10.0s (default is 2.00s). If a host reply is not received within the specified time, the request times out, and the sending of that packet is unsuccessful.

#### Start

Click this button to start the ping session.

### Status

* While a ping session is in progress, the status shows as "Initializing".
* If the host can successfully be pinged, the status shows as "OK".
* If the host cannot be successfully pinged based on the defined Ping Settings, the status shows as "Fault - Time exceeded".

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Error Tolerance Count | 1 to 10 | 1 to 10 | 0.00 to 1.00 | Input / Output |
| Host Name | (text) | | | Input / Output |
| Packet Count | 1 to 10 | 1 to 10 | 0.00 to 1.00 | Input / Output |
| Ping Interval | 1.00 to 10 | 1.00s to 10.0s | 0.00 to 1.00 | Input / Output |
| Start | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Status | (text) | | | Output |
| Timeout | 2.00 to 10 | 2.00s to 10.0s | 0.00 to 1.00 | Input / Output |
