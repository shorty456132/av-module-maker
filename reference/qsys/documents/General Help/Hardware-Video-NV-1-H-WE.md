# NV-1-H-WE Network Video Endpoint

> Source: https://help.qsys.com/Content/Hardware/Video/NV-1-H-WE.htm

# NV-1-H-WE Network Video Endpoint

The Q-SYS NV-1-H-WE wall-mount HDMI encoder enhances and extends the NV Series network video distribution into flexible and reconfigurable spaces, providing a single platform for network video distribution across every room type. The NV-1-H WE can be used alongside other Q-SYS NV Series network video endpoints, providing system design flexibility. Like all Q-SYS products, the NV-1-H-WE offers native integration into the Q-SYS platform, reducing complexity and accelerating deployment by tightly integrating device configuration, control and audio routing capabilities.

**Note:** This topic provides an overview of the NV-1-H-WE. For complete specifications, installation documentation, and product drawings, see the [NV-1-H-WE product page](https://www.qsys.com/products-solutions/q-sys/video/nv-series/nv-1-h-we) on the Q-SYS website.

[Features](javascript:void(0))

* Single cable solution for video distribution
* Native HDMI video distribution for Q-SYS
* Q-SYS Shiftâ¢ adaptive video compression

[Design Components](javascript:void(0))

Add the NV-1-H-WE to your design Inventory from the Video category. The following components are available for the NV-1-H-WE:

#### Standard Components

* [Status (NV-1-H-WE)](../../Schematic_Library/vstreamer_nv1wp_status.htm)
* [AV I/O (NV-1-H-WE)](../../Schematic_Library/vstreamer_nv1wp_av_io.htm)

#### Related Components

* [Generic AV Source](../../Schematic_Library/vst_hdmi_source.htm)

[Connections and Callouts](javascript:void(0))

### Front Panel

1. HDMI In â HDMI 2.0 input with support for HDCP 2.3 and HDCP 1.4.
2. Reset Button â (Behind perforated cover, recessed) Use a paper clip, or similar tool, to press and hold the reset button for 10 seconds to reset the NV-1-H-WE to factory values.
3. Power / ID LED â Illuminates blue when the NV-1-H-WE is powered on. Blinks green when placed into ID Mode via ID Button or Q-SYS Peripheral Manager. Solid Green indicates valid HDMI input.
4. ID Button â (Behind perforated cover) Locates the NV-1-H-WE in Q-SYS Designer Software and Q-SYS Peripheral Manager.

### Rear Panel

1. LAN / PoE â RJ-45 connector, 2.5GbE, 802.3 at Type 2 Class 4 (30W from PSE, 25.5W at NV-1-H-WE). For connection to Q-LAN.

[Q-SYS Shiftâ¢ Adaptive Bitrate Codec](javascript:void(0))

The NV-1-H-WE uses Q-SYS Shiftâ¢ video compression to provide high-quality, low-latency video streaming supporting video formats up to 4k60 4:4:4 over a standard gigabit network. Q-SYS Shiftâ¢ leverages DCT and temporal compression technologies, much like those found in H.264 and H.265 video compression codecs. Q-SYS optimized Shiftâ¢ to provide flawless image quality from the most demanding content sources. Further, Shiftâ¢ intelligently manages and optimizes the resulting network bitrate by only refreshing changes within each frame, allowing for significantly reduced bandwidth usage as compared to other compression codecs.

#### Modes

Multicast and unicast

#### Bitrates

10 Mbps â 800 Mbps

#### Streaming Protocol

RTP

### Supported Video Formats1

| Resolution | Frame Rate (Hz) | Chroma Sampling Level | Bit Depth |
| --- | --- | --- | --- |
| 3840 x 2160 (4K UHD) | 60, 59.94, 50, 30, 29.97, 25, 24 | 4:4:4 | 8 bit |
| 3440 x 1440 | 60 | 4:4:4 | 8 bit |
| 2560 x 1600 | 60 | 4:4:4 | 8 bit |
| 2560 x 1440 | 60 | 4:4:4 | 8 bit |
| 2560 x 1080 | 60, 59.94, 50, 30, 29.97, 25, 24 | 4:4:4 | 8 bit |
| 1920 x 1200 | 60 | 4:4:4 | 8 bit |
| 1920 x 1080 (1080p) | 60, 59.94, 50, 30, 29.97, 25, 24 | 4:4:4 | 8 bit |
| 1280 x 720 (720p) | 60, 59.94, 50, 30, 29.97, 25, 24 | 4:4:4 | 8 bit |
| 640 x 480 | 60 | 4:4:4 | 8 bit |

\* All video formats are progressive. 4:2:0 Chroma subsampling and HDR not supported.

1 This table is a small subset of the most common formats. Many other formats and timings are also supported.

### Scaler

The NV-1-H-WE features a robust 4K60 4:4:4 scaler that can accommodate the most challenging resolution and frame rate conversions from network streams or local HDMI sources. The scaler is capable of operating in three modes (configurable within Q-SYS Designer Software):

* Stretch-to-fit
* Maintain aspect ratio
* 1:1 pixel mapping

[Specifications](javascript:void(0))

For complete product specs, refer to the Specifications Sheet on the [NV-1-H-WE product page](https://www.qsys.com/products-solutions/q-sys/video/nv-series/nv-1-h-we) at qsys.com.
