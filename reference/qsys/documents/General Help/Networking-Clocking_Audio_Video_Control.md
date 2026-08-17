# Clocking, Audio, Video, & Control

> Source: https://help.qsys.com/Content/Networking/Clocking_Audio_Video_Control.htm

# Clocking, Audio, Video, & Control

Q-LAN is a collection of open, IT-standard protocols and solutions designed to allow Q-SYS to integrate easily with modern IT networks. Q-SYS leverages the Q-LAN protocol suite for audio and video distribution as well as device discovery, synchronization, control, and management. All Q-LAN protocols are Internet Protocol (IP) based and can easily reside on either Layer-2 (single VLAN) or Layer-3 (multi-VLAN and Routed) networks.

[Sampling Clock](javascript:void(0))

Q-SYS uses IEEE 1588-2008 Precision Time Protocol (PTPv2) for synchronization. By default, the Q-SYS Core is the PTP grandmaster for all Q-SYS peripheral devices.

### Protocols

Uses UDP ports 319 and 320 and destination IP 224.0.1.129 (multicast - registered to NIST/IEEE).

### QoS

The Q-LAN sampling clock requires real-time performance (QoS Strict Priority Queuing) with packets marked DSCP 46 (Highest priority) for QoS prioritization. See the [Quality of Service (QoS)](QoS.htm) topic.

### Network Usage

The Q-LAN sampling clock transmits â¤100 packets per second, with â¤100 bytes per packet.

[Audio Streams](javascript:void(0))

Q-LAN audio is transmitted in streams (ongoing series of packets), which are unicast from source to destination (Q-SYS Core to peripheral or vice-versa). Each packet contains 16 audio samples for each of up to 16 audio channels. Samples are in 32-bit floating-point format (RTP).

**Tip:** To learn about network audio channels, network audio streams, and creating efficient designs when wiring components, see [Networked Audio Design](../Q-Sys_Designer/Networked_Audio_Design.htm).

### Protocols

* Source port UDP range 6518-7030 (one port per stream) is assigned to each stream.
* Destination port UDP range 6518-7030 is used for RTCP control of each audio stream.

**Note:** Although not real-time critical, RTCP packets are also marked as DSCP 34 (AF41) to prevent these packets from being dropped.

### QoS

Q-LAN audio streams require real-time performance (QoS Strict Priority Queuing) with packets marked DSCP 34 (Second Highest priority) for QoS prioritization. See the [Quality of Service (QoS)](QoS.htm) topic.

### Network Usage

* Per-channel bandwidth: 1.65 Mbps (with 16 channels of audio) to 3.31 Mbps (with 1 channel of audio) bandwidth per channel.
* Per-stream bandwidth: 3.31 Mbps (with 1 channel of audio) to 26.41 Mbps (with 16 channels of audio) per stream .
* 100 to 1100 bytes per packet with 3000 UDP packets per second, per stream. Packet size depends on channel count per stream. Audio packets contain Ethernet, IP, and UDP headers, the audio data itself, stream identifier, and time-stamp fields.
* 100 acknowledgments are sent every second and contain receiver-side stats.
* Duplicate, identical, simultaneous streams are generated on secondary Q-LAN network interface ports (e.g., LAN B) if Network Redundancy is enabled.
* The formula for determining total bandwidth per port is: Mb = ( 1.77 \* total stream count ) + ( 1.54 \* total channel count )

**Tip:** You can check your Core's bandwidth calculations using the Check Design dialog in Q-SYS Designer. Go to File > Check Design.

### Q-SYS Core Processor Capacities

**Note:** Q-SYS Scaling Licenses expand the capabilities of some Q-SYS Core processor models. Refer to the [Licensing](../Core_Manager/Core_Management/Licensing.htm) topic for more information.

Network Audio Streams vs. Channels

Each Q SYS Core has separate limits for Network Audio Channels and Network Audio Streams. A single stream may carry one or more audio channels. In many cases, you will reach the stream limit before you hit the channel limit.

For most Core models, the maximum number of Network Audio Streams (Tx and Rx) is half of the maximum Network Audio Channels. Notable exceptions:

* Core 510i and Core 510c: support 256 x 256 streams and 256 x 256 channesl.
* Core 610: supports 256 x 256 streams and up to 384 x 384 channels (with capacity scaling license); applying a capacity scaling license does not increase the stream limit.

The Check Design window in Q-SYS Designer always shows the authoritative maximum for both Network Audio Channels and Network Audio Streams for the selected Core model.

| Core Model | Local I/O Channels | Network Audio Channels[5](#The) | Network Audio Streams | Software Dante Audio Channels[4](#Software) | AEC Processors[5](#The) | Multitrack Audio Players | Local I/O Card Capacity | VoIP Instances |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [NV-32-H (Core Capable) Network Video Endpoint](../Hardware/Video/NV-32-H_Core_Capable.htm) | HDMI (8-ch per port) Stereo 3.5 mm (1 x 1) | 64 x 64 | 32 x 32 | Up to 32 x 32 (none included) | 8 | 16 | N/A | 1 |
| [Core Nano](../Hardware/Processing/Core_Nano.htm) | 8x8 USB audio | 64 x 64 (128 x 128 w/ [Licensing](../Core_Manager/Core_Management/Licensing.htm)) | 32 x 32 (64 x 64 w/ [Licensing](../Core_Manager/Core_Management/Licensing.htm)) | Up to 32 x 32 (8 x 8 included) | 8 | 16 (upgradable to 32) | N/A | 2 |
| [Core 8 Flex](../Hardware/Processing/Core_8_Flex.htm) | 8 flex, 8x8 USB audio | 64 x 64 (128 x 128 w/ [Licensing](../Core_Manager/Core_Management/Licensing.htm)) | 32 x 32 (64 x 64 w/ [Licensing](../Core_Manager/Core_Management/Licensing.htm)) | Up to 32 x 32 (8 x 8 included) | 8 | 16 (upgradable to 32) | N/A | 2 |
| [Core 110f](../Hardware/Processing/Core_110f.htm) | 24 (8 analog in, 8 analog out, 8 analog flex in/out), 16x16 USB audio | 128 x 128[1](#top) | 64 x 64 | Up to 32 x 32 (8 x 8 included[3](#For)) | 16 | 16 (upgradable to 32) | N/A | 4 |
| [Core 24f](../Hardware/Processing/Core_24f.htm) | 24 (8 analog in, 8 analog out, 8 analog flex in/out) | 160 x 160 | 80 x 80 | Up to 64 x 64 (8 x 8 included) | 24 | 4 | N/A | 8 |
| [Server Core X10](../Hardware/Processing/Server_Core_X10.htm) | N/A | 256 x 256 | 128 x 128 | Up to 128 x 128 (8 x 8 included) | 64 | 128 | N/A | 32 |
| [Server Core X20r](../Hardware/Processing/Server_Core_X20r.htm) | N/A | 384 x 384 | 192 x 192 | Up to 256 x 256 (8 x 8 included) | 128 | 256 | N/A | 64 |
| [Core 510i](../Hardware/Processing/Core_510i.htm) | Up to 32 analog, 128x128 (AES/CobraNet/Dante/AVB cards) | 256 x 256 | 256 x 256 | Up to 128 x 128 (8 x 8 included[2](#Starting)) | 64 | 16 (upgradable to 128) | 8 | 64 |
| [Core 610](../Hardware/Processing/Core_610.htm) | N/A | 256 x 256 (384 x 384 with Licensing) | 256 x 256 (streams stay fixed) | Up to 256 x 256 (8 x 8 included) | 64 | 16 (upgradable to 128) | N/A | 64 |
| [Core 5200](../Hardware/Processing/Core_5200.htm) | N/A | 512x512 | 256 x 256 | Up to 512 x 512 (8 x 8 included[2](#Starting)) | 160 | 16 (upgradable to 128) | N/A | 64 |
| [Core 6000 CXR](../Hardware/Processing/Core_6000_CXR.htm) | N/A | 256 x 256, upgradeable to 512 x 512 | 128 x 128 (upgradeable to 256 x 256) | Up to 512 x 512 (8 x 8 included) | 80, upgradeable to 160 | 16 (upgradable to 128) | N/A | 64 |
| Discontinued |  | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Core 110c](../Hardware/Processing/Core_110c.htm) | 24 (8 analog in, 8 analog out, 8 analog flex in/out), 16 x 16 USB audio | 128 x 128[1](#top) |  | N/A | 4 | 16 (upgradable to 32) | N/A | 1 |
| [Core 510c](../Hardware/Processing/Core_510c.htm) | Up to 32 analog, 128 x 128 (AES/CobraNet/Dante/AVB cards) | 256 x 256 |  | N/A | 64 | 16 (upgradable to 128) | 8 | 4 |
| [Core 6000 CXR](../Hardware/Processing/Core_6000_CXR.htm) | N/A | 256 x 256, upgradeable to 512 x 512 |  | Up to 512 x 512 (8 x 8 included) | 80, upgradeable to 160 | 16 (upgradable to 128) | N/A | 64 |

###### 1. When using the Core 110f on-board USB Device Port for video bridging, the Q-LAN / AES67 maximum audio channel count is 80 x 64 (Q-SYS version 9.7 and later) or 64 x 64 (Q-SYS version 9.6 and earlier).

###### 2. For units shipped after January 1, 2021. See [Licensing](../Core_Manager/Core_Management/Licensing.htm).

###### 3. For units shipped after March 31, 2020. See [Licensing](../Core_Manager/Core_Management/Licensing.htm).

###### 4. Software Dante channels count towards Network Audio Channels.

###### 5. The maximum number of third-party microphone AEC Processors and input Network Audio Channels is affected by the quantity of Q-SYS NM-T1 microphones in the design. See [NM-T1 Quantity and AEC Channel Limits](../Hardware/Audio_IO/NM-T1.htm#NM-T1).

### Q-SYS Peripheral Network Audio Channel Capacities

| Q-SYS Device | Maximum Network Audio Channels In x Out |
| --- | --- |
| I/O-510i  (Core 510i in I/O Frame mode) | 128 x 128 |
| I/O-8 Flex | 8 x 8 |
| I/O-22 | 2 x 2 |
| I/O-Frame | Depends on installed Q-SYS I/O cards |
| I/O-USB Bridge | 4 x 5 |
| Page Stations | 2 x 1 |
| NV-32-H Network Video Endpoint | When set as Encoder[1](#Does): 14 x 7  When set as Decoder[1](#Does): 22 x 7  HDMI Source: 8 x 0  HDMI Display: 0 x 8 |

###### 1. Does not include HDMI PCM audio (up to 8 channels) embedded in each AV stream. AV streams are point-to-point and not routed through nor processed by the Q-SYS Core.

### Latency

* System audio latency is configurable from 3.17 ms (default) to 5.17 ms end-to-end. To achieve 3.17 ms system audio latency, audio packets must always get across the network in 280 Î¼s or less.
* Use the Network Receive Buffer property in Q-SYS Designer to increase latency if you need to accommodate a large network with a higher forwarding delay.
* Network switches and network construction must meet Q-LAN requirements â see the [Network Switches & Infrastructure](Switches_Infrastructure.htm) topic.
* Analog latency (3.17 ms) is measured using a MIC/LINE IN card and a LINE OUT or DataPort card.
* When using an AES3 card, the measurement is taken with and without Sample Rate Conversion (SRC):
  + With SRC: Total latency is 5.69 ms
  + Without SRC: Total latency is 2.81 ms

[Video Streams](javascript:void(0))

### Protocols

#### PTZ-IP Series Cameras

* Web Services Discovery: Multicast UDP 239.255.255.250 on Port 3702.
* Video stream multicasting: User-configurable between 224.0.0.0 and 239.255.255.255. Use 'Auto' mode in Q-SYS Core Manager > Network > [Network > Multicast](../Core_Manager/Core_Management/Multicast.htm) to allow the system to supply multicast addresses.

#### NC Series Cameras

* mDNS: 239.255.255.251 (applicable to all NC Series cameras except NC-Pro15x)
* Q-SYS Discovery Protocol (QDP): Multicast UDP 224.0.23.175 on Ports 2467-2470 and Unicast on Port 6504
* Video stream multicasting: User-configurable between 224.0.0.0 and 239.255.255.255. Use 'Auto' mode in Q-SYS Core Manager > Network > [Network > Multicast](../Core_Manager/Core_Management/Multicast.htm) to allow the system to supply multicast addresses.
* RTSP/RTP packets are encoded using ports 6000 - 6006 (unicast) and 8012 (multicast) for Mediacast and preview streams, with the initial handshake on TCP/RTSP port 554. For all NC Series cameras except NC-Pro15x, unicast port numbers are incremented by the Core any time a camera stream starts â for example, when switching cameras.
* RTSP/RTP packets are decoded by USB Video Bridges on ports 7516 - 7534.

#### NV Series Encoders

* Encoders use an RTSP server to stream video packets.
* RTSP server uses TCP and listens on ports 5540-5542 â one server for each of up to three AV streams, depending on the model.
* NV-32-H: Sends RTP packets (UDP) from ports 7500, 7502, and 7504 and RTCP packets (UDP) from ports 7501, 7503, and 7505.
* NV-21-HU: Sends RTP packets (UDP) from ports 7500 and 7502 and RTCP packets (UDP) from ports 7501 and 7503.
* NV-1-H-WE: Sends RTP packets (UDP) from port 7500 and RTCP packets (UDP) from port 7501.
* Multicasting: User-configurable between 224.0.0.0 and 239.255.255.255. Use 'Auto' mode in Q-SYS Core Manager > Network > [Network > Multicast](../Core_Manager/Core_Management/Multicast.htm) to allow the system to supply multicast addresses.

#### NV Series Decoders

* NV-32-H: Receives RTP packets (UDP) on ports 7516, 7518 and RTCP packets (UDP) on ports 7517 and 7519.
* NV-21-HU: Receives RTP packets (UDP) on port 7516 and RTCP packets (UDP) on port 7517.
* NV-1-H-WE: Decoding not supported

### QoS

Q-SYS video streams for Q-SYS cameras and the NV-32-H require real-time performance (QoS Strict Priority Queuing) with packets marked DSCP 26 (Third Highest priority) for QoS prioritization. See the [Quality of Service (QoS)](QoS.htm) topic.

### Q-SYS Camera Network Usage

Network usage depends on the IP stream quality, configurable in the [Status/Control (Cameras)](../Schematic_Library/onvif_camera_operative.htm) or [USB Video Bridge](../Schematic_Library/usb_uvc.htm) component Mediacast Streams tab. Camera streams are routed between the Q-SYS camera and the USB Video Bridge.

#### Mediacast Stream (H.264)

Maximum bitrate is user-configurable between 1 to 30 Mbps.

#### Preview Stream (H.264)

Maximum bitrate is user-configurable between 0.5 and 2 Mbps.

**Note:** Instantaneous bitrates can exceed these values up to the limitations of the network.

### NV-32-H Network Usage

#### Overview

Each Q-SYS NV-32-H Network Video Endpoint is configurable in Q-SYS Designer as either an Encoder or Decoder:

* AV streams are point-to-point, meaning they are routed directly from Encoder to Decoder without Q-SYS Core processing.
* An Encoder takes source HDMI AV signals and places them on the network in streams. Encoders can process a single stream up to 4K60 or three simultaneous streams up to 1080p60 each.
* A Decoder processes incoming network HDMI signals and sends them to a display. Decoders can process a single stream up to 4K60 or two simultaneous streams up to 1080p60 each.
* Each stream can be either unicast (one Encoder to one Decoder) or multicast (one Encoder to two or more Decoders), determined by schematic wiring in Q-SYS Designer.
* Each Encoder consumes up to 800 Mbps of network bandwidth, plus overhead, depending on its bitrate setting.

#### Encoder Bitrate

Network usage is determined by the Encoder's video bitrate setting. Use the Bitrate (Mbps) control in the Encoder's HDMI I/O component control panel to set the maximum average network video bitrate for that Encoder. The value is configurable from 50 to 800 Mbps, which is shared across all Encoder AV streams (unicast or multicast) from that Encoder. You configure this value for each Encoder in your design.

Lower bitrates consume less network bandwidth, but at the expense of compromised video quality during fast motion and transitions. For acceptable video quality:

* 4K60 stream â set the bitrate to at least 650 Mbps.
* 1080p streams â set to the bitrate so that each stream can use at least 250 Mbps.

**Note:** The Bitrate value is shared across all AV streams. For example, if you set the Bitrate to 600, the first AV stream can use a maximum of 600 Mbps. If a second stream becomes active, both streams can use 300 Mbps. If a third stream becomes active, each stream can use 200 Mbps.

#### Switch Requirements for AV Streaming

For acceptable video streaming performance, observe these requirements:

* Due to the bandwidth intensity inherent to network video streaming, network switches must strictly meet Q-LAN switch requirements, including non-blocking wire-speed Gigabit Ethernet. See the [Network Switches & Infrastructure](Switches_Infrastructure.htm) topic.
* It is critical to have proper QoS and multicast configuration (IGMP snooping and/or PIM-SM). See the [Quality of Service (QoS)](QoS.htm) and [Multicast Traffic](Multicast_Traffic.htm) topics.
* Jumbo Frames: Q-SYS does not use jumbo frames (also known as jumbo packets) for any type of network transmission, and so they are not required for proper operation. The best practice is to disable jumbo frames on the Q-SYS network.

  **Note:** The use of jumbo frames on the Q-SYS network can interfere with consistent delivery of Q-LAN AV packets. In such cases, and for proper operation, it might be necessary to separate devices that require jumbo frames from the Q-SYS network.

For more switch requirements, see the [Network Switches & Infrastructure](Switches_Infrastructure.htm) topic.

#### Inter-Switch Link Requirements

As long as each switch supports Q-LAN requirements, traffic between ports on the same switch is not a concern, as each port must support non-blocking wire-speed Gigabit Ethernet. However, connections between network switches (inter-switch links) must support the aggregate consumed bandwidth of all switch ports, plus overhead. Do not exceed 80% network backbone usage without performing a proof of concept to establish if the network can deliver acceptable performance under load.

For example:

* If a 10-port 1 Gigabit switch has connections to 10 NV-32-H Encoders, each streaming 4K60 video using the maximum bitrate of 800 Mbps, then: 10 x .800 = 8 Gbps must successfully pass from this switch to other network switches with connections to NV-32-H Decoders. Assuming a 10 GbE network backbone with a maximum recommended network usage of 80%, this configuration provides adequate bandwidth.
* If a 48-port 1 Gigabit switch has connections to 48 NV-32-H Encoders, each streaming three 1080p AV streams for a combined bitrate of 750 Mbps, then: 48 x .750 = 36 Gbps must successfully pass from this switch to other network switches with connections to NV-32-H Decoders. In this case, a 40 GbE backbone may not be sufficient when allowing for 80% usage.

[Control](javascript:void(0))

Q-SYS Control traffic includes communication between the Q-SYS Core processor and Q-SYS peripherals (such as touch screens), External Control from third-party control systems (ASCII-based), Remote Control from third-party control systems (JSONRPC-based), and secure Core-to-Core communication in a Redundant Core configuration.

### Protocols

* Control communications between Q-SYS Designer and the Core are via self-signed, encrypted HTTPS (TCP port 443).
* Control communications between Q-SYS UCI Viewers, Q-SYS touch screens, and the Core are via HTTPS (TCP port 443).
* Q-SYS Discovery Protocol (QDP): Multicast UDP 224.0.23.175 on Ports 2467-2470 and Unicast on Port 6504
* Q-SYS Control Binary Secure (QCBS): TCP Port 1704
* External Control (ASCII) is on TCP port 1702
* Remote Control (JSONRPC) is on TCP port 1710

### QoS

Q-SYS Control traffic falls under the Lowest priority (DSCP 0). See the [Quality of Service (QoS)](QoS.htm) topic.

### Network Usage

Q-SYS Control traffic uses 10 Mbps or less. Non-redundant systems typically use less than 2 Mbps. Actual bandwidth depends on the number of connections to User Control Interfaces (UCIs), redundant Q-SYS Core processors, and connections to third-party control systems.

**Note:** QDP transmissions are approximately once per second per Q-SYS device.
