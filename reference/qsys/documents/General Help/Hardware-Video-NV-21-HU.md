# NV-21-HU Network Video Endpoint

> Source: https://help.qsys.com/Content/Hardware/Video/NV-21-HU.htm

# NV-21-HU Network Video Endpoint

The Q-SYS NV Series NV-21-HU is the next evolution for native video distribution on the Q-SYS Platform. The NV-21-HU is a software configurable endpoint offering a comprehensive single-cable solution for audio and video distribution, AV bridging and device charging via USB-C. The NV-21-HUâs compact size and reduced I/O make it ideal for supporting meeting rooms, learning spaces, hospitality and entertainment installations. The NV-21-HU can be used alongside other Q-SYS NV Series video endpoints, providing system design flexibility. Like all Q-SYS products, the NV-21-HU offers native integration and control, simplifying configuration and operation.

**Note:** This topic provides an overview of the NV-21-HU. For complete specifications, installation documentation, and product drawings, see the [NV-21-HU product page](https://www.qsys.com/products-solutions/q-sys/processing/nv-21-hu/) on the Q-SYS website.

[Features](javascript:void(0))

* Single cable solution for video distribution, AV bridging, and device charging.
* Native HDMI video and audio distribution for Q-SYS
* Q-SYS Shiftâ¢ adaptive video compression
* Software configurable as an encoder or decoder
* HDMI and USB-C Mode selection

**Note:**  An external power supply is required for any device charging over the USB-C connection. See the [NV-21-HU Hardware User Manual](https://www.qsys.com/resource-files/productresources/dn/nv21/q_dn_qsys_nv-21-hu_usermanual.pdf) for power requirements.

[Design Components](javascript:void(0))

Add the NV-21-HU to your design Inventory from the Video category. The following components are available for the NV-21-HU:

#### Standard Components

* [Status (NV-21-HU)](../../Schematic_Library/vstreamer_nv1smb_status.htm)
* [AV I/O (NV-21-HU)](../../Schematic_Library/av_io.htm)
* [Serial Port (NV-21-HU)](../../Schematic_Library/serial_port_nv1smb_vstreamer.htm)
* [HID Keyboard](../../Schematic_Library/usb_keyboard.htm)
* [HID Media](../../Schematic_Library/usb_ccontrols.htm)
* [HID Conferencing](../../Schematic_Library/usb_telephony.htm)
* [USB Input](../../Schematic_Library/usb_input.htm)
* [USB Output](../../Schematic_Library/usb_output.htm)

#### USB Video Bridge

* [USB Video Bridge](../../Schematic_Library/usb_uvc.htm)

#### USB Audio Bridge

* [USB Audio Bridge â Speakerphone / Sound Card In](../../Schematic_Library/usb_receiver.htm)
* [USB Audio Bridge â Speakerphone / Sound Card Out](../../Schematic_Library/usb_transmitter.htm)

#### Related Components

* [Generic AV Source](../../Schematic_Library/vst_hdmi_source.htm)
* [Generic HDMI Display](../../Schematic_Library/vst_hdmi_display.htm)

[Connections and Callouts](javascript:void(0))

### Front Panel

1. Power LED â Illuminates blue when the NV-21-HU is powered on.
2. ID Button â Locates the NV-21-HU in Q-SYS Designer Software and Q-SYS Peripheral Manager.
3. ID LED â Blinks green when placed into ID Mode via ID Button or Q-SYS Peripheral Manager.

### Rear Panel

1. External Power Input â Auxiliary power, 12VDC, 10A. Uses a 2-pin Euro connector (included with purchased power supply).
2. LAN / PoE â RJ-45 connector, 2.5GbE, 802.3bt Type 3 Class 5 (45W from PSE, 40W at NV-21-HU). For connection to Q-LAN.
3. USB-A â USB 3.0 Type-A Host Port. Supports 5VDC @ 900mA max.
4. RS232 â Serial Transmit and Receive. Uses the black 3-pin Euro connector.
5. Reset Button â Use a paper clip, or similar tool, to press and hold the reset button for 10 seconds to reset the NV-21-HU to factory values.
6. USB-C â USB 3.2 Gen 1x1 (5Gbps) Type-C Device Port, supporting DisplayPort Alt-Mode (DP 1.4 Sink) , USB Power Delivery up to 65W, support for HDCP 2.3 and HDCP 1.4.
7. HDMI In â HDMI 2.0 Input with support for HDCP 2.3 and HDCP 1.4.
8. HDMI Out â HDMI 2.0 Output with support for HDCP 2.3 and HDCP 1.4.

### Control

#### RS-232

Three Pin Euro terminal connection to control third-party devices with Q-SYS Control, user-configurable.

### USB

#### USB HID control

Control host PCs with a USB connection using USB HID components in Q-SYS Designer Software.

#### Q-SYS AV Bridging

The Q-SYS AV Bridging feature expands the functionality of the NV-21-HU, allowing users to connect their devices via USB-C directly to the network video endpoint to integrate Q-SYS audio and camera feeds for remote meetings easily. The NV-21-HU emulates a webcam (for video streams from Q-SYS network cameras), a speakerphone, and a multichannel soundcard over a single driverless USB connection.

### Audio

#### HDMI Audio Input

Receive up to 8 channels of PCM audio from your video source, which are routable within Q-SYS Designer Software.

#### USB-C Audio Input

Receive up to 8 channels of PCM Audio from your video source, which are routable within Q-SYS Designer. Additional 1x1 Speakerphone and 2x2 Soundcard options are available with the Q-SYS AV Bridging feature.

#### HDMI Audio Output

Embed up to 8 channels of PCM audio from Q-SYS to the HDMI output of the NV-21-HU to utilize the built-in speakers of a display as a Q-SYS audio destination for source audio content or any other audio, including paging, background music, etc.

[Security and Authentication](javascript:void(0))

#### AES-128

NV Series supports AES-128 encryption for audio and video signals from encoders to decoders.

#### Content Protection

HDCP 1.4 & HDCP 2.3 complaint

#### 802.1x

802.1x authentication is available and configurable through Q-SYS Peripheral Manager.

[Q-SYS Shiftâ¢ Adaptive Bitrate Codec](javascript:void(0))

The NV-21-HU uses Q-SYS Shiftâ¢ video compression to provide high-quality, low-latency video streaming supporting video formats up to 4k60 4:4:4 over a standard gigabit network. Q-SYS Shiftâ¢ leverages DCT and temporal compression technologies, much like those found in H.264 and H.265 video compression codecs. Q-SYS optimized Shiftâ¢ to provide flawless image quality from the most demanding content sources. Further, Shiftâ¢ intelligently manages and optimizes the resulting network bitrate by only refreshing changes within each frame, allowing for significantly reduced bandwidth usage as compared to other compression codecs.

**Note:** 4k60 formats require Display Stream Compression (DSC) or reduced blanking for USB-C video inputs.

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

The NV-21-HU features a robust 4K60 4:4:4 scaler that can accommodate the most challenging resolution and frame rate conversions from network streams or local HDMI and USB-C sources. The scaler is capable of operating in three modes (configurable within Q-SYS Designer Software):

* Stretch-to-fit
* Maintain aspect ratio
* 1:1 pixel mapping

[Specifications](javascript:void(0))

For complete product specs, refer to the Specifications Sheet on the [NV-21-HU product page](https://www.qsys.com/products-solutions/q-sys/processing/nv-21-hu/) at qsys.com.
