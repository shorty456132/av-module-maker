# Media Stream Transmitter

> Source: https://help.qsys.com/Content/Schematic_Library/media_stream_transmitter.htm

# Media Stream Transmitter

The Media Stream Transmitter compresses and streams audio over the network. Source material (audio and/or video, live or recorded) is transmitted over the network to a receiver where an end user can listen to, watch, and/or record the media. To send the media over a network, the transmitter must use a set of rules (the protocol), and the receiver must be able to interpret the media by using the same protocol.

Q‑SYS has two protocols from which you can select to stream media:

* Real-time Transport Protocol (RTP)
* Southern Vision Systems Inc. (SVSi)

[Core Maximums](javascript:void(0))

**Note:** Q-SYS Scaling Licenses expand the capabilities of some Q-SYS Core processor models. Refer to the [Licensing](../Core_Manager/Core_Management/Licensing.htm) topic for more information.

| Core Model | Max Media Stream Transmitter Channels per Design | Max Media Stream Transmitter Components/Streams per Design | Max Sum of Media Stream and WAN Channels per Design | Max Sum of Media Stream and WAN Transmitter Components/Streams per Design |
| --- | --- | --- | --- | --- |
| NV-32-H (Core Capable) | 12 | 6 | 12 | 6 |
| Core Nano | 12 | 6 | 12 | 6 |
| Core 8 Flex | 12 | 6 | 12 | 6 |
| Core Nano / Core 8 Flex (Commercial AV Bundle) | 24 | 12 | 24 | 12 |
| Core 110f | 24 | 12 | 24 | 12 |
| Core 24f | 36 | 36 | 36 | 36 |
| Server Core X10 | 64 | 64 | 64 | 64 |
| Core 510i | 64 | 32 | 64 | 32 |
| Core 610 | 64 | 32 | 64 | 32 |
| Server Core X20r | 96 | 96 | 96 | 96 |
| Core 610 (Scaling License) | 96 | 48 | 96 | 48 |
| Core 5200 | 256 | 128 | 256 | 128 |

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Mode**Property.

### Input Pins

#### Channel 1, 2

Media Stream Transmitter supports stereo input only. Connect these pins to a source audio component.

### Output Pins

This component does not have any output pins.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

### Input / Channel

#### Peak Level (dBFS)

Measures the Digital Signal level prior to the D/A converter.

#### Invert

Inverts the audio signal.

#### Mute

Mutes the audio signal.

#### Gain

Controls the gain of the digital audio signal prior to the D/A converter.

### Status

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

### Stream

#### Enable

Starts and stops the streaming.

#### Protocol

The protocol used for the streaming. Based on the protocol you select, the following fields will be active or grayed out and not accessible.

#### Host (RTP)

The host name must be a valid IP address, or must follow standard naming conventions, restricted to the following:

* ASCII characters a - z, A-Z (case insensitive)
* Digits 0 - 9
* Hyphen (cannot be at the beginning or end of the name)
* Underscore (acceptable with a Q-SYS implementation)
* No other characters, symbols, punctuation, or blank spaces.

When you have entered the Host Name, it displays next to the Media Stream Transmitter icon in the left-side pane.

#### Port (RTP)

For RTP, the port number on the equipment to which the stream is sent.

#### Format (RTP)

For RTP, select the audio file format to be transmitted. Based on the format you select, the Data Rate displays different choices.

#### Data Rate (RTP - MP3)

The data rate for streaming the RTP MP3 audio.

Select from : 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320 kbits/sec

#### Data Rate (RTP - PCM)

The data rate for streaming the RTP PCM audio is fixed at:

16 bit stereo, 44.1kHz (1411.2kbit/s)

#### SVSi Stream

The stream number to be transmitted. The equipment you transmit to will have an assigned stream number.

#### SVSi Address

The address of the SVSi device to which you want to transmit. This number is based on the SVSi Stream number and SVSi rules.

#### Interface

Auto, LAN A, LAN B, AUX A, Aux B

#### Multicast TTL

TTL = Time to Live. Determines how many hops a packet can make before being deleted. The default TTL for multicast datagrams is 1, which will result in multicast packets going only to other hosts on the local network.

[Control Pins](javascript:void(0))

The table below shows some examples of the type of inputs the control pins accept and the type of outputs the controls produce. The Input and Output Values were obtained using a Generic Integer knob. The Text Input uses a Text Edit box, and the output a Text Display. Notice that the inputs and outputs are occasionally different. In some cases the text is not case sensitive others it is case sensitive. Some controls do not require the entire string, others require the string to be exactly what is expected. A Position knob is used for the Position In and Out. The type of control dictates when the position knob makes a difference. If the control is a toggle (Mute, Invert) the control toggles at around 0.50 on the position knob. If the control is an integer with a very large range, the first movement of the position knob is at a very small position - a good example is the Port field below.

|  | Integer | | Text | | Position | |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pin Name | Input | Output | Input | Output | Input | Output | Pins Available |
| Channel 1, 2 | | | | | | | |
| Gain [1](#Gain_Input) | -100 to  10 | -100 to  10 | -100 to  10.0 | -100dB to  10.0dB | 0.00 = ‑100dB  0.75 = 0dB  1.00 = 10dB | -100dB = 0.00  0dB = 0.75  10dB = 1.00 | Input / Output |
| Invert | 0  >0 | 0  1 | 0  1 | normal  inverted | 0 to 0.49  0.50 to 1.00 | 0 to 0.49  0.50 to 1.00 | Input / Output |
| Mute | 0  >0 | 0  1 | 0  1 | unmuted  muted | 0 to 0.49  0.50 to 1.00 | 0 to 0.49  0.50 to 1.00 | Input / Output |
| Peak Input Level | N / A | -120 to  43.0 | N / A | -120dB to  43.0dB | N / A | 0 to  1.00 | Output |
| Data Rate [2](#RTP_only) (MP3) | N / A | N / A | 8kbit/s to  320kbit/s | 8kbit/s to  320kbit/s | N / A | N / A | Input / Output |
| Data Rate 1 (PCM) | N / A | N / A | 16 bit stereo, 44.1kHz (1411.2kbit/s) | 16 bit stereo, 44.1kHz (1411.2kbit/s) | N / A | N / A | Input / Output |
| Enable | 0  >0 | 0  1 | 0  1 | disable  enable | 0 to 0.49  0.50 to 1.00 | 0 to 0.49  0.50 to 1.00 | Input / Output |
| Format 1 | N / A | N / A | MP3 or PCM | MP3 or PCM | N / A | N / A | Input / Output |
| Host 1 |  |  | user defined | user defined | N / A | N / A | Input / Output |
| Interface [4](#Interface) | N / A | N / A | Auto  LAN A ( )  LAN B ()  AUX A ()  AUX B () | Auto  LAN A ( )  LAN B ()  AUX A ()  AUX B () | N / A | N / A | Input / Output |
| Multicast TTL | 1 to 63 | 1 to 63 | 1 to 63 | 1 to 63 | 0 to 1.00 | 0 to 1.00 | Input / Output |
| Port 1 | 1 to 65535 | 1 to 65535 | 1 to 65535 | 1 to 65535 | 0.000008 to 1.00 | 0.000008 to 1.00 | Input / Output |
| Protocol [5](#Protocol) | N / A | N / A | RTP or SVSi | RTP or SVSi | N / A | N / A | Input / Output |
| Status | N / A | N / A | N / A | text | N / A | N / A | Output |
| SVSi address [3](#SVSi_only) | Text - varies as SVSi Stream changes | | | | | | Output |
| SVSi Stream 2 | 0 to 65535 | 0 to 65535 | 0 to 65535 | 0 to 65535 | 0 to 1.00 | 0 to 1.00 | Input / Output |
|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1. The text input for Gain accepts only numeric expressions. For example, 2.5.2. RTP only.3. SVSi only.4. The information Inside the parenthesis will be an ip address or "No Link". You must have at least one ip address. Text input is case sensitive and must be the entire string.5. Protocol text input is not case sensitive. | | | | | | | |
