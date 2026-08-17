# AES67 Transmitter

> Source: https://help.qsys.com/Content/Schematic_Library/aes67_tx.htm

# AES67 Transmitter

The AES67 Transmitter component provides the means for sending valid AES67 audio streams.

Q-SYS implements the AES67 mandated "Compatibility Mode" which is:

* 1ms packet time
* offering 10 channels per stream
* at L24 or L16, 48kHz

[Connection Modes](javascript:void(0))

In the component Properties, you can set the Connection Mode to configure how devices are discovered and managed:

* **Auto** mode â This mode ensures that the AES67 receiver/transmitter is configured to use SAP (Session Announcement Protocol) for Discovery and Connection Management. This enables automatic discovery and connection to any SAP enabled AES67 stream, including those transmitted by a Dante based device.
* **Manual** mode â Allows manual configuration of stream TX/RX parameters for integration with devices not using SAP.
* **RTSP** mode â In this mode, you copy the stream **URI** from the connection parameters in the component control panel and use this URI in your AES67 receiver settings.

[Configure the AES67 Transmitter](javascript:void(0))

Refer to the Controls, and Properties tables for information about items used in this procedure. This procedure is focused on the AES67 Transmitter, so it is assumed that you have the appropriate elements in your design to use the transmitter.

1. From the Inventory add list, select Streaming I/O > AES67 Transmitter. The transmitter is added to your Inventory.
2. Drag and drop the AES67 TX Status/Control component into the schematic.
3. Double click the component to display the components control panel.
4. In the Properties, Give the transmitter a new **Name** if desired. The default is AES67-TX-*n*.
5. Select or create a new **Location** for the transmitter.
6. Set the **Connection Mode** to **Auto**.   
   Auto mode configures this AES67 Transmitter to use the SAP protocol for Discovery and Connection Management. This enables automatic discovery and connection by any SAP enabled AES67 receiver, including Dante based devices.
7. Set the Channel Count to the number of streams (1 to 10) you will be transmitting.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Channel Count**Property.

### Input Pins

#### Input 1 - n

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the AES67 Transmitter component is set to 8 inputs. You can choose between 1 and 10.

### Output Pins

This component does not have any output pins.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### AES67 Transmitter Properties

#### Connection Mode

For more information, see [Connection Modes](#Connecti).

* **Auto** mode uses SAP to ease integration with any other AES67 device using SAP.
* **Manual** allows you to manually configure additional Transmitter connection settings.
* **RTSP** mode allows you to obtain the stream URI for use in your AES67 Transmitter settings.

#### Channel Count

Number of channels for the Transmitter. This count must match that of the Receiver.

[Controls](javascript:void(0))

### Stream

#### Peak Output Level (dBFS)

Meters for each channel indicating the peak output level, from -120 to 20.

#### Clip LED

Indicates the associated channel output is clipping.

#### Clip Hold

When engaged, the Clip LED remains on until reset by disengaging this button.

#### Invert

Toggle button to invert the digital output of the AES67 Transmitter.

#### Mute

Mutes the output signal.

#### Gain (dB)

Controls the Gain of the digital output signal, from -100 to 20 (default = 0).

#### Status

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

Enable / Disable the Transmitter.

#### Stream Name

User-defined name for the transmitted stream.

#### Multicast Address

The AES67 Transmitter and Receiver must have the same Multicast Address. By default, the address is automatically assigned from the range configured on the Q-SYS Core Manager > [Network > Multicast](../Core_Manager/Core_Management/Multicast.htm) page. Once an address is auto-assigned, that address is retained unless manually changed. If you clear the Multicast Address field, the system auto-assigns a new address.

**Note:** If you specify your own address, it must be a valid Class D Multicast address between 224.0.0.0 and 239.255.255.255 and not conflict with those registered with the IANA, any Q-SYS [Network > Services](../Core_Manager/Core_Management/Network_Services.htm), or multicast address ranges for [Video > Cameras](../Core_Manager/System_Management/Cameras.htm) and [Video > Video Endpoints](../Core_Manager/System_Management/Video_Endpoints.htm).

**Note:** Transmitting AES67 audio to any Dante-based device requires address assignment within the 239.69.xxx.xxx range.

To learn more about multicast addressing in Q-SYS, see [Multicast Traffic](../Networking/Multicast_Traffic.htm).

#### Encoding

Determines the bit depth of the transmitted AES67 stream (choose L16 for 16-bit or L24 for 24-bit audio).

#### Network Tx Buffer

Adds extra buffer time to the default maximum of 1 ms.

Additional Network Receive Buffer time is useful in (rare) cases where the network latency through the network exceeds the default maximum. Additional network latency my be introduced by sub-optimal QoS functionality, some layer-3 routing implementations, long distances or large networks. You can select from:

* Default
* Extra 1 ms
* Extra 2 ms
* Extra 5 ms

#### Interface

Sets the LAN on which the transmitter is to communicate with the receiver. The Auto selection will choose for you, but you can also select LAN A or LAN B.

[Manual Connection Mode](javascript:void(0))

**Note:** Manual Connection Mode is for advanced use only. Do not use unless required by the design architecture.

#### Enable

Enable / Disable the Transmitter stream.

#### Stream Name

User-defined name for the transmitted stream.

#### Multicast Address

The AES67 Tx component must have the same Multicast Address assigned as the receive device you wish to send to.

#### Remote RTP Port

The Remote Real-Time Transport Protocol is used to send audio to an AES67 receiver. The transmitter must have the same RTP Port as the receiver. Must be different than the RTCP port number. The range is 1 to 65535 (default is 5004).

#### Remote RTCP Port

The Real-time Transport Control Protocol is used to send control information to an AES67 receiver. The transmitter must have the same RTCP Port as the receiver. Must be different than the RTP port number. The range is 1 to 65535 (default is 5005).

#### Packet Time

This sets the AES67 compatibility. 48 is the base level compatibility (conformance level A) for AES67 devices. This translates to 48kHz streams, 1-8 channels per stream at 1 mS latency.

You can select 16 or 48 (default is 48).

**Note:** 16 setting is equivalent of .33 mS with up to 30 channels per stream. This should only be used if the receive equipment specifies this setting as needed.

#### Encoding

Determines the bit depth of the transmitted AES67 stream (choose L16 for 16-bit or L24 for 24-bit audio).

#### Stream Channels

The number of channels being used as set in this field. This is initially set in the Properties but can be changed here. This number cannot exceed the number of channels set in the component's Properties.

#### Payload Type

This range of Payload Types (96 to 127, default is 96) is for video and combined encodings. Must be the same as the device the stream will interface with. 96 is the setting most commonly used across devices.

#### Media Clock Offset

This sets the RTP clock offset from the synchronized local clock which is in turn precisely synchronized to a common wall clock via PTP. While some devices may call for a different setting (default is 0), this is typically 0 for ST2110 and AES67 devices.

#### Network Tx Buffer

Adds extra buffer time to the default maximum of 1 ms.

Additional Network Transmit Buffer time is useful in (rare) cases where the network latency through the network exceeds the default maximum. Additional network latency my be introduced by sub-optimal QoS functionality, some layer-3 routing implementations, long distances or large networks. You can choose from:

* Default
* Extra 1 ms
* Extra 2 ms
* Extra 5 ms

#### Interface

Sets the LAN on which the transmitter is to communicate with the receiver. The Auto selection will choose for you, but you can also select LAN A or LAN B.

[RTSP Connection Mode](javascript:void(0))

#### Stream Path

Defines the RTSP URL suffix that receiving devices use to subscribe to the AES67 stream.

#### RTCP Port

The Real-time Transport Control Protocol is used to send control information to an AES67 receiver. The transmitter must have the same RTCP Port as the receiver. Must be different than the RTP port number. The range is 1 to 65535 (default is 5005).

#### URI

Specify the URI address of the transmitting AES67 stream to be received

#### Enable

Enable / Disable the Transmitter.

#### Encoding

Determines the bit depth of the transmitted AES67 stream (choose L16 for 16-bit or L24 for 24-bit audio).

#### Network Tx Buffer

Adds extra buffer time to the default maximum of 1 ms.

Additional Network Transmit Buffer time is useful in (rare) cases where the network latency through the network exceeds the default maximum. Additional network latency my be introduced by sub-optimal QoS functionality, some layer-3 routing implementations, long distances or large networks. You can choose from:

* Default
* Extra 1 ms
* Extra 2 ms
* Extra 5 ms

#### Interface

Sets the LAN on which the transmitter is to communicate with the receiver. The Auto selection will choose for you, but you can also select LAN A or LAN B.

### Details

#### Details

Text indicating the Details of the Transmitter stream. The information in this field is updated regularly and is cumulative. The following "Count" information is displayed as running totals:

* Enabled: 1
* Connected: 1
* Packet Count: 1875
* Timestamp: 418637872

#### Reset Details

This button resets the networking details to zero, at which point the details start accumulating information again.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Channel 1 â *n* | | | | |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | off  on | 0  1 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Level (Peak Input) | -120 to 20 | -120 dB to 20 dB | 0.000 to 1.00 | Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Details | | | | |
| Reset Stream Details | Trigger | | | Input / Output |
| Stream Details | Text Display | | | Output |
| Connection | | | | |
| Enable | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Encoding | Text Display  L16  L24 | | | Input / Output |
| Interface | Text Display  Auto  LAN A  LAN B  LAN nnn | | | Input / Output |
| Media Clock Offset | 0 to *nnn* | 0 *nnn* | 0 1.00 | Input / Output |
| Multicast Address | Text *nnn.nnn.nnn.nnn* | Input / Output | Multicast Address | Text *nnn.nnn.nnn.nnn* |
| Network RX Buffer | Text Display:  Default  Extra 1 ms  Extra 2 ms  Extra 5 ms | | | Input / Output |
| Stream Name | Text Edit | | | Input / Output |
| Packet Time | 16 48 | 16 48 | N / A | Input / Output |
| Payload Type | 96 to 127 | 96 to 127 | 0.00 to 1.00 | Input / Output |
| Remote RTCP Port | 1 to 65535 | 1 to 65535 | 0.00 to 1.00 | Input / Output |
| Remote RTP Port | 1 to 65535 | 1 to 65535 | 0.00 to 1.00 | Input / Output |
| Stream Channels | 1 to 10 | 1 to 10 | 1 = 0  2 = 0.111  3 = 0.222  4 = 0.333  5 = 0.444  6 = 0.556  7 = 0.667  8 = 0.778  9 = 0.889  10 = 1.00 | Input / Output |
| Status | | | | |
| Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
