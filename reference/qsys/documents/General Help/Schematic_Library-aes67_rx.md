# AES67 Receiver

> Source: https://help.qsys.com/Content/Schematic_Library/aes67_rx.htm

# AES67 Receiver

The AES67 Receiver component provides the means for receiving valid AES67 audio streams.

AES67 allows high performance audio streaming between Q-SYS and third-party products supporting different native networked audio technology without requiring any additional hardware or license costs.

Q-SYS implements the AES67 mandated "Compatibility Mode" which is:

* 1ms packet time
* offering 10 channels per stream
* at L24 or L16, 48kHz

[Connection Modes](javascript:void(0))

In the component Properties, you can set the Connection Mode to configure how devices are discovered and managed:

* **Auto** mode â This mode ensures that the AES67 receiver/transmitter is configured to use SAP (Session Announcement Protocol) for Discovery and Connection Management. This enables automatic discovery and connection to any SAP enabled AES67 stream, including those transmitted by a Dante based device.
* **Manual** mode â Allows manual configuration of stream TX/RX parameters for integration with devices not using SAP.
* **RTSP** mode â In this mode, you specify the AES67 transmitter **URI** in the receiver component control panel connection parameters.

[Configure the AES67 Receiver](javascript:void(0))

Refer to the information in the Controls, and Properties tables for information about items used in this procedure. This procedure is focused on the AES67 Receiver, so it is assumed that you have the appropriate elements in your design to use the receiver.

1. From the Inventory add list, select Streaming I/O > AES67 Receiver. The receiver is added to your Inventory.
2. Drag and drop the AES67 RX Status/Control component into the schematic.
3. Double click the component to display the components control panel.
4. In the Properties, Give the transmitter a new **Name** if desired. The default is AES67-RX-*n*.
5. Select or create a new **Location** for the receiver if desired.
6. Set the **Connection Mode** to **Auto**.   
   Auto mode configures this AES67 Receiver to use the SAP protocol for Discovery and Connection Management. This enables automatic discovery and connection to any SAP enabled AES67 stream, including those transmitted by a Dante based device.
7. Set the **Channel Count** to the number of streams (1 to 10) you will be receiving.
8. Run the design on the Core.
9. Status shows "Not Present â Waiting for SAP"
10. When the first SAP announcement is received, the status changes to "Not Present â No Stream Specified"
11. Click in the **Stream Name** field to select the stream you want from the "discovered" list.

**Note:** that it may take up to 30 seconds for all connected devices to broadcast their SAP announcements on to the network. As such it may be necessary to wait up to 30 seconds for the Stream Name field to populate with the stream to which you wish to connect.

1. If the transmitter is transmitting, you can see the levels in the receiver's control panel as Peak Input Level (dBFS). Make adjustments as needed.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Channel Count**Property.

### Input Pins

This component does not have any input pins.

### Output Pins

#### Output 1 - n

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the AES67 Receiver component is set to 8 outputs. You can choose between 1 and 10.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### AES67 Receiver Properties

#### Connection Mode

For more information, see [Connection Modes](#Connecti).

* **Auto** mode uses SAP to ease integration with any other AES67 device using SAP.
* **Manual** allows you to manually configure additional receiver connection settings.
* **RTSP** mode allows you to specify the stream URI of the AES67 transmitter.

#### Channel Count

Number of channels for the Receiver. This count must match that of the Transmitter.

[Controls](javascript:void(0))

### Stream Tab

#### Peak Input Level (dBFS)

Meters for each channel indicating the peak input level, from -120 to 20.

#### Invert

Toggle button to invert the digital output of the AES67 Receiver.

#### Mute

Mutes the output signal.

#### Gain (dB)

Controls the Gain of the digital output signal, from -100 to 20 (default = 0).

#### OK LED

LED indicating the status of the Receiver network link.

#### AES67 Receiver Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### Connection Modes

[Auto Connection Mode](javascript:void(0))

#### Enable

Enable / Disable the Receiver.

#### Stream Name

User-defined name for the received stream.

#### Network Rx Buffer

Adds extra buffer time to the default maximum of 1 ms.

Additional Network Receive Buffer time is useful in (rare) cases where the network latency through the network exceeds the default maximum. Additional network latency my be introduced by sub-optimal QoS functionality, some layer-3 routing implementations, long distances or large networks. You can select from:

* Default
* Extra 1 ms
* Extra 2 ms
* Extra 5 ms

#### Interface

Sets the LAN on which the receiver is to communicate with the transmitter. The Auto selection will choose for you, but you can also choose LAN A or LAN B.

[Manual Connection Mode](javascript:void(0))

**Note:** Manual Connection Mode is for advanced use only. Do not use unless required by the design architecture.

#### Enable

Enable / Disable the Receiver.

#### Multicast Address

The AES67 Rx component must have the same Multicast Address assigned as the transmit device you wish to receive from.

#### Remote RTP Port

The Remote Real-Time Transport Protocol is used to send audio to an AES67 receiver. The receiver must have the same RTP Port as the transmitter. Must be different than the RTCP port number. The range is 1 to 65535 (default is 5004).

#### Remote RTCP Port

The Real-time Transport Control Protocol is used to send control information to an AES67 receiver. The receiver must have the same RTCP Port as the transmitter. Must be different than the RTP port number. The range is 1 to 65535 (default is 5005).

#### Packet Time

This sets the AES67 compatibility. 48 is the base level compatibility (conformance level A) for AES67 devices. This translates to 48kHz streams, 1-8 channels per stream at 1 mS latency.

You can select 16 or 48 (default is 48).

**Note:** 16 setting is equivalent of .33 mS with up to 30 channels per stream. This should only be used if the receive equipment specifies this setting as needed.

#### Encoding

Specifies the expected bit depth of the incoming AES67 stream (L16 for 16-bit or L24 for 24-bit audio).

#### Stream Channels

The number of channels being used as set in this field, from 1 to 10 (default is 8). This is initially set in the Properties but can be changed here. This number cannot exceed the number of channels set in the component's Properties. This number must match the number of channels in the AES67 transmitting device.

#### Payload Type

This range of Payload Types (96 to 127, default is 96) is for video and combined encodings. Must be the same as the device the stream will interface with. 96 is the setting most commonly used across devices.

#### Media Clock Offset

This sets the RTP clock offset from the synchronized local clock which is in turn precisely synchronized to a common wall clock via PTP. While some devices may call for a different setting (default is 0), this is typically 0 for ST2110 and AES67 devices.

#### Network Rx Buffer

Adds extra buffer time to the default maximum of 1 ms.

Additional Network Receive Buffer time is useful in (rare) cases where the network latency through the network exceeds the default maximum. Additional network latency my be introduced by sub-optimal QoS functionality, some layer-3 routing implementations, long distances or large networks. You can select from:

* Default
* Extra 1 ms
* Extra 2 ms
* Extra 5 ms

#### Interface

Sets the LAN on which the receiver is to communicate with the transmitter. The Auto selection will choose for you, but you can also select LAN A or LAN B.

[RTSP Connection Mode](javascript:void(0))

#### URI

Specify the URI address of the transmitting AES67 stream to be received.

#### Enable

Enable / Disable the Receiver.

#### Network Rx Buffer

Adds extra buffer time to the default maximum of 1 ms.

Additional Network Receive Buffer time is useful in (rare) cases where the network latency through the network exceeds the default maximum. Additional network latency my be introduced by sub-optimal QoS functionality, some layer-3 routing implementations, long distances or large networks. You can choose from:

* Default
* Extra 1 ms
* Extra 2 ms
* Extra 5 ms

#### Interface

Sets the LAN on which the receiver is to communicate with the transmitter. The Auto selection will choose for you, but you can also select LAN A or LAN B.

### Details Tab

#### Details

Text indicating the Details of the receiver stream. The information in this field is updated regularly and is cumulative. The following "Count" information is displayed as running totals:

* Connected: The receiver has identified the transmitter and is listening for packets from it
* DSCP: The DSCP value in the IP header of received packets
* Count: The number of packets received
* Accept: The number of packets received and successfully processed
* Drop: The number of packets received but discarded for any reason
* Duplicate: The number of packets received whose timestamp is the duplicate of a previous packet
* On Time: The number of packets that have arrived in time for processing by the receiver
* Too Late: The number of packets that were dropped because they arrived too late
* PT Mismatch: The number of packets dropped due to the RTP payload not being the expected type
* Size Mismatch: The number of packets dropped because the size of the packet did not match what was expected

[Example](javascript:void(0))

* Enabled: 1
* Connected: 1
* DSCP: 34
* Count: 2548805
* Accept Count: 2548805
* Drop Count: 0
* Duplicate Count: 0
* On Time: 2548804
* Too Late: 0
* PT Mismatch: 0
* Size Mismatch: 0

#### Reset Details

This button resets the networking details to zero, at which point the details start accumulating information again.

#### Session Name

Contains the Transmitter Name and Session Identifier. Click to select.

#### Raw SDP

The Session Description Protocol (SDP) is a format for describing streaming media initialization parameters. Contains the following information:

* v=0
  + *(protocol version number, currently only 0)*
* o=- 3616011820 3616011822 IN IP4 10.10.200.75
  + *(originator and session identifier : username, id, version number, network address)*
* s=AES67-TX-1
  + *(session name : mandatory with at least one UTF-8-encoded character)*
* c=IN IP4 239.69.125.125/32
  + *(connection informationânot required if included in all media)*
* t=0 0
  + *(time the session is active)*
* m=audio 65535 RTP/AVP 120
  + *(media name and transport address)*
* i=Channels 1-2
  + *(media title or information field)*
* For the following: *a= (zero or more media attribute lines â overriding the Session attribute lines)*

+ a=recvonly
+ a=rtpmap:120 L24/48000/2
+ a=ptime:0.333
+ a=ts-refclk:IEEE1588-2008:00-15-17-FF-FF-82-DE-98:0
+ a=mediaclk:direct=0

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Channel 1 â *n* | | | | |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Level (Peak Input) | -120 to 20 | -120 dB to 20 dB | 0.000 to 1.00 | Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Details | | | | |
| Connect SDP | Trigger | | | Input / Output |
| Raw SDP | Text | | | Output |
| Reset Stream Details | Trigger | | | Input / Output |
| Session Name | Text | | | Input / Output |
| Stream Details | Text | | | Output |
| Connection | | | | |
| Enable | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Encoding | Text  L16  L24 | | | Input / Output |
| Interface | Text  Auto  LAN A  LAN B  LAN nnn | | | Input / Output |
| Network RX Buffer | Text  Default  Extra 1 ms  Extra 2 ms  Extra 5 ms | | | Input / Output |
| Stream Name | Text | | |  |
| Media Clock Offset | 0 to *nnn* | 0 *nnn* | 0 1.00 | Input / Output |
| Multicast Address | Text *nnn.nnn.nnn.nnn* | | | Input / Output |
| Packet Time | 16 48 | 16 48 | N / A | Input / Output |
| Payload Type | 96 to 127 | 96 to 127 | 0.00 to 1.00 | Input / Output |
| Remote RTCP Port | 1 to 65535 | 1 to 65535 | 0.00 to 1.00 | Input / Output |
| Remote RTP Port | 1 to 65535 | 1 to 65535 | 0.00 to 1.00 | Input / Output |
| Stream Channels | 1 to 10 | 1 to 10 | 1 = 0  2 = 0.111  3 = 0.222  4 = 0.333  5 = 0.444  6 = 0.556  7 = 0.667  8 = 0.778  9 = 0.889  10 = 1.00 | Input / Output |
| Status | | | | |
| Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
