# AV I/O (NV-1-H-WE)

> Source: https://help.qsys.com/Content/Schematic_Library/vstreamer_nv1wp_av_io.htm

# AV I/O (NV-1-H-WE)

Use the AV I/O Encoder component to configure AV video and audio routing in Q-SYS.

[Supported Q-SYS Hardware](javascript:void(0))

### NV-1-H-WE as an Encoder

For NV-1-H-WE Network Video Endpoints, the AV I/O component represents a single NV-1-H-WE device configured as an Encoder for sending or receiving AV signals over the network.

#### Q-SYS Shift Networked AV Streaming

An Encoder takes source AV signals and places them on the network in streams. Encoders can process a single stream up to 4K60.

[AV Connection Requirements](javascript:void(0))

#### HDMI

* QSC supports the direct connection between NV Series Video Endpoints and HDMI sources and displays.
* The use of signal extension solutions (for example: HDBaseT extenders, HDMI distribution amps, and active/optical HDMI cables and keystones) and docking stations in-line with NV Series HDMI ports may introduce handshake issues or signal attenuation-related issues. QSC does not test any configurations with these products.
* To maximize HDMI signal reliability, use Premium or Ultra High Speed certified cables.

[Inputs and Outputs](javascript:void(0))

### Input Pins

#### HDMI AV Input

There is one HDMI input on the NV-1-H-W. Connect this pin to a [Generic AV Source](vst_hdmi_source.htm) component HDMI AV Output pin.

### Output Pins

#### AV Output

The AV Output pins send combined video and audio signals over the Q-LAN network. The output correspond to a respective AV Input pin.

[Schematic Examples](javascript:void(0))

In this example, a single display is being used in a small conference room.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### HDMI / Shift AV

#### AV IP Streaming

This property determines the network streaming method for Q-LAN AV streams:

* Compiler Choice: (Default) Select this option to allow Q-SYS Designer Software to determine whether unicast (one-to-one) or multicast (one-to-many) is best for your configuration. This is the recommended option.
* Unicast: Select this option when your design contains one-to-one AV routing, meaning that each AV output pin in your design is connected to a single AV input pin.
* Multicast: Select this option when your design contains one-to-many AV routing, meaning that an AV output pin is connected to multiple AV input pins.

[Controls](javascript:void(0))

### Encoder Network Settings

#### Source

Displays the AV Stream in which it is wired.

#### IP Streaming

LED indicates whether the Encoder is actively transmitting AV audio and video data to a Decoder via SRTP on the Q-LAN network. This applies to both unicast or multicast streams.

#### SRTP Address

Displays the IP address that the Encoder is using to send AV network audio and video streams directly to Decoders:

* For unicast streams, this is the Encoder's IP address.
* For multicast streams, this is the multicast address assigned in [Core Manager](../Core_Manager/CoreManager_Overview.htm).

#### Bitrate (Mbps)

Specify the maximum average network video bitrate the Encoder can use to send AV streams to Decoders, from 50 to 800. The default is 750.

Lower bitrates consume less network bandwidth, but at the expense of compromised video quality during fast motion and transitions. For acceptable video quality:

* 4K60 stream â set the bitrate to at least 650 Mbps.
* 1080p streams â set to the bitrate so that each stream can use at least 250 Mbps.

**Note:** The Bitrate value is shared across all AV streams. For example, if you set the Bitrate to 600, the first AV stream can use a maximum of 600 Mbps. If a second stream becomes active, both streams can use 300 Mbps. If a third stream becomes active, each stream can use 200 Mbps.

#### Ref Frame Interval

This value determines how often video artifacts introduced by network errors are eliminated in the video stream. The value, between 90 and 255, is the number of video frames before a complete refresh occurs. The default is 90. A longer interval results in a lower video bitrate (thus consuming less network bandwidth), but at the expense of video artifacts persisting during the interval.

#### Encoder Mode

This property determines the maximum allowed AV stream resolution and what happens when the Encoder video streaming capabilities are exceeded.

* 4K60 max - One Hot Plug Event: (Default) This option allows a maximum stream resolution of 4K60. However, because an Encoder is limited to processing a single stream at resolutions above 1080p60, a request from a Decoder to process an additional AV stream on another input triggers a "hot plug event": Any Encoder input EDID with a resolution greater than 1080p60 is automatically re-negotiated down to 1080p60 maximum, thus allowing the Encoder to provide up to three streams. When this occurs, there is a momentary disruption of video processing across all AV streams. (This negotiation and disruption mimics what occurs when unplugging and plugging back in an HDMI cable, hence the term.) When all AV inputs become idle, the source EDIDs then reset to allow resolutions greater than 1080p60 again.
* 1080p60 max - No Hot Plug Events: This option limits all streams to 1080p60 maximum. Because an Encoder can process three simultaneous streams up to 1080p60, there is no EDID re-negotiation when a Decoder requests subsequent streams.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Network | | | | |
| Input 1 | | | | |
| Source | 0  n | 0  n | 0.000 to 1.00 | Output |
| SRTP Address | (text) | | | Output |
| Streaming | 0  1 | false  true | 0  1 | Output |
| Encoder Mode | - | 4K60 max - One Hot Plug Event  1080p60 max - No Hot Plug Events | - | Input / Output |
| Ref Frame Interval | 5 to 255 | - | 0.000 to 1.00 | Input / Output |
| Video Bitrate | 50 to 800 | - | 0.000 to 1.00 | Input / Output |
