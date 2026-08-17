# NV-32-H (Core Capable) Network Video Endpoint

> Source: https://help.qsys.com/Content/Hardware/Video/NV-32-H_Core_Capable.htm

# NV-32-H (Core Capable) Network Video Endpoint

The NV-32-H (Core Capable) is a multipurpose, software-configurable video endpoint native to the Q-SYS Ecosystem, offering two distinct operating modes: Core Mode transforms the device into a fully integrated Q-SYS processor with local HDMI switching capabilities. Peripheral Mode allows multi-stream video encoding or decoding for network-based HDMI video distribution. Like all Q-SYS devices, the NV-32-H (Core Capable) offers native integration and control, simplifying setup, configuration and firmware management while eliminating the need for advanced programming knowledge.

**Note:** For installation and connection instructions, drawings, and other documentation, refer to the Resources section on the [NV-32-H (Core Capable) product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/q-sys-cores/nv-32-h-core-capable/) on the Q-SYS website. To learn about native HDMI distribution within the Q-SYS Ecosystem, see the [Q-SYS Video 101 Training](https://training.qsc.com/course/view.php?id=73) on the Q-SYS website.

[Features](javascript:void(0))

| Feature | NV-32-H (Core Capable) |
| --- | --- |
| Total Network I/O | 64 x 32 |
| Onboard I/O | HDMI (8-ch per port)  Stereo 3.5 mm (1 x 1) |
| Software-based Dante Capacity | None included (up to 32 x 32) |
| USB Audio Channel Count | 2 x 2 |
| AEC Processors | 8 |
| Universal Web Conferencing Compatibility | Yes |
| VoIP Instances | 1 |
| Onboard AV Bridging (USB) | Yes |
| Full-featured Control Engine | Yes |
| Onboard GPIO | 2 x 3 |
| Onboard RS232 Control Ports | 1 |
| Q-SYS Peripheral Limit[1](#Includes) | 32 |
| Size | 1/2 rack, 1RU |

###### 1. Includes native Q-SYS cameras, I/O (including NL), NV, TSCs, paging stations, Extensions and plugins with their âIs Managedâ property set to âYesâ. It does not include Streaming I/O, Loudspeakers, Scripts or plugins with their âIs Managedâ property set to âNoâ.

### Core Mode Features

* Fully integrated Q-SYS Core processor
* Onboard 3 x 2 HDMI video switcher
* 64 x 32 network audio channels
* 8x AEC channels
* 1 x VoIP softphone instance
* Audio I/O via HDMI, USB and 3.5 mm

### Peripheral Mode Features

* Native HDMI video and audio distribution for the Q-SYS Ecosystem
* Q-SYS Shiftâ¢ adaptive video compression codec
* Software-configurable as an encoder or decoder
* Simultaneous streaming capabilities

[Switching Modes](javascript:void(0))

The NV-32-H (Core Capable) is configurable in Core Mode or Peripheral Mode. By default, the NV-32-H (Core Capable) ships from the factory in Peripheral Mode. It's easy to switch modes.

[Peripheral Mode to Core Mode](javascript:void(0))

1. From [Configurator](../0017_Configurator.htm) (Tools > Show Configurator), locate and select the NV-32-H from the I/O Devices category.
2. Click the link to open Peripheral Manager.
3. From the Utilities tab, change the Mode property to 'Core'.
4. Click Switch.

Once the device reboots, you can then configure it using [Core Manager](../../Core_Manager/CoreManager_Overview.htm). In your design, be sure to change Core Properties > Model to 'NV-32-H (Core Mode)'. Once you save and run your design to the Core, the NV-32-H (Core Capable) will then be functional as a Q-SYS Core processor after its firmware updates.

[Core Mode to Peripheral Mode](javascript:void(0))

1. Open [Core Manager](../../Core_Manager/CoreManager_Overview.htm) for the NV-32-H (Core Capable).
2. From the Utilities menu, change the Mode property to 'Peripheral'.
3. Click Switch.

Once the device reboots, you can then configure it using [Configurator](../0017_Configurator.htm) > Peripheral Manager. In your design, add the NV-32-H to your design from the Inventory menu > Video section. Once you save and run your design to the Core, the NV-32-H will then be functional as a peripheral after its firmware updates.

[Design Components](javascript:void(0))

Available Q-SYS Designer inventory components depend on whether the NV-32-H (Core Capable) is configured for Core Mode or Peripheral Mode.

[Core Mode](javascript:void(0))

#### Standard Components

* [Status (Core)](../../Schematic_Library/core_status.htm)
* [HDMI I/O (NV-32-H)](../../Schematic_Library/streamer_hdmi_switcher.htm)
* [GPIO In (NV-32-H)](../../Schematic_Library/vstreamer_gpio_input.htm)
* [GPIO Out (NV-32-H)](../../Schematic_Library/vstreamer_gpio_output.htm)
* [Mic/Line In (NV-32-H)](../../Schematic_Library/io_card_mic_line_in_vstreamer.htm)
* [Line Out (NV-32-H)](../../Schematic_Library/io_card_line_out_vstreamer.htm)
* [Serial Port (Core and I/O Devices)](../../Schematic_Library/serial_port.htm)
* [HID Keyboard](../../Schematic_Library/usb_keyboard.htm)
* [HID Media](../../Schematic_Library/usb_ccontrols.htm)
* [HID Conferencing](../../Schematic_Library/usb_telephony.htm)
* [USB Input](../../Schematic_Library/usb_input.htm)
* [USB Output](../../Schematic_Library/usb_output.htm)

#### External USB Audio

* [External USB Audio Device In](../../Schematic_Library/alsa_receiver_sound_card.htm)
* [External USB Audio Device Out](../../Schematic_Library/alsa_transmitter_sound_card.htm)

#### USB Video Bridge

* [USB Video Bridge](../../Schematic_Library/usb_uvc.htm)

#### USB Audio Bridge

* [USB Audio Bridge â Speakerphone / Sound Card In](../../Schematic_Library/usb_receiver.htm)
* [USB Audio Bridge â Speakerphone / Sound Card Out](../../Schematic_Library/usb_transmitter.htm)

#### Related Components

* [Generic AV Source](../../Schematic_Library/vst_hdmi_source.htm)
* [Generic HDMI Display](../../Schematic_Library/vst_hdmi_display.htm)

[Peripheral Mode](javascript:void(0))

#### Standard Components

* [Status (NV-32-H)](../../Schematic_Library/vstreamer_status.htm)
* [HDMI I/O (NV-32-H)](../../Schematic_Library/streamer_hdmi_switcher.htm)
* [GPIO In (NV-32-H)](../../Schematic_Library/vstreamer_gpio_input.htm)
* [GPIO Out (NV-32-H)](../../Schematic_Library/vstreamer_gpio_output.htm)
* [Serial Port (NV-32-H)](../../Schematic_Library/serial_port_vstreamer.htm)
* [Mic/Line In (NV-32-H)](../../Schematic_Library/io_card_mic_line_in_vstreamer.htm)
* [Line Out (NV-32-H)](../../Schematic_Library/io_card_line_out_vstreamer.htm)
* [HID Keyboard](../../Schematic_Library/usb_keyboard.htm)
* [HID Media](../../Schematic_Library/usb_ccontrols.htm)
* [HID Conferencing](../../Schematic_Library/usb_telephony.htm)
* [USB Input](../../Schematic_Library/usb_input.htm)
* [USB Output](../../Schematic_Library/usb_output.htm)

#### External USB Audio

* [External USB Audio Device In](../../Schematic_Library/alsa_receiver_sound_card.htm)
* [External USB Audio Device Out](../../Schematic_Library/alsa_transmitter_sound_card.htm)

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

1. Power LED â illuminates blue when the Q-SYS NV-32-H is powered on
2. ID LED â LED blinks when placed into ID Mode via ID Button or Q-SYS Configurator Software
3. ID Button â Locates the Q-SYS NV-32-H in Q-SYS Designer GUI and Configurator

### Rear Panel

1. External Power Input 48 VDC 1.5 A â Auxiliary power, 48 VDC, 1.5A, 2-pin Euro connector
2. LAN A/ PoE ++ â connection for Q-LAN network, 802.3bt Type 4 power, RJ-45 connector
3. LAN B â connection for redundant Q-LAN network (Core Mode only), RJ-45 connector
4. USB Type A â USB type A host connectors (blue connector is for USB 3.0 connection).
5. GPIO Out
   * 12 VDC Output â 12 V, 0.2 A output used for GPIO signals.
   * GPIO Outputs â 3 outputs, open collector (24 V, 0.2 A maximum) with pull up to +3.3 V, (pins 1-3 equal pins 1-3 in the Q-SYS Designer GPIO Output component.
   * Ground â Use this ground reference for 12 VDC and GPIO outputs.
6. GPIO Inputs / RS-232
   * GPIO Inputs â 2 inputs, 0-24 V analog input, or contact closure, pins 1-2 equal pins 1-2 in the Q-SYS Designer GPIO Input component).
   * RS-232 â Transmit and Receive
   * Ground â Use this ground reference for GPIO inputs and RS-232.
7. Analog Audio Output â 3.5 mm connector unbalanced stereo line output
8. Analog Audio Input â 3.5 mm connector unbalanced stereo mic/line input
9. USB B â USB Type B Device connector for web conference integration
10. HDMI Inputs â H1DMI 2.0 Input with support for HDCP 2.2 and HDCP 1.4
11. HDMI Output â HDMI 2.0 Output with support for HDCP 2.2 and HDCP 1.4
12. Factory Reset Button â Use a paperclip to press and hold for 10 seconds to factory reset the NV-32-H.

### Control

#### RS-232

Three-pin Euro terminal connection to control third-party devices with Q-SYS Control, user configurable.

#### GPIO

Three inputs and two outputs for control of third-party devices via Q-SYS Control, user configurable.

### USB

#### USB HID Routing over IP

Support for USB HID sources, including keyboard, mouse, and touchscreen.

#### Bridging

The NV-32-H can act as an endpoint for the Q-SYS Web Conferencing solution, similar to the Q-SYS Core 110f processor and Q-SYS I/O-USB Bridge. This mode is available in both Core and Peripheral Mode. The NV-32-H emulates a webcam video driver (for video streams from the Q-SYS PTZ-IP conference cameras), AEC speakerphone audio driver and multi-channel soundcard driver over a single, driverless USB connection.

### Audio

#### Network Audio

Use a total network channel count of 64 x 32, including Q-SYS native audio channels or Dante channels (licensable up to 32x32).

#### HDMI Audio Input

Each HDMI input is able to receive up to eight channels of PCM audio, which are routable within Q-SYS Designer Software.

#### HDMI Audio Output

Each HDMI output has the ability to output up to eight channels of PCM audio, making each HDMI output a full-featured Q-SYS audio destination for source audio content, or any other Q-SYS audio feature such as paging, audio playback etc.

#### Analog Audio Input

Mic/line input on a 3.5 mm TRS connector, routable within Q-SYS Designer Software, for direct connection of microphones or audio players.

#### Analog Audio Output

Line output on a 3.5 mm TRS connector, routable within Q-SYS Designer Software, for direct connection of QSC non-networked amplifiers, external speakers or audio recorders.

[Q-SYS Shiftâ¢ Adaptive Video Compression Codec](javascript:void(0))

#### Modes

Multicast and unicast

#### Bitrates

10 Mbps â 800 Mbps

#### Streaming Protocol

RTP

### Supported Video Formats1

| Resolution | Frame Rate (Hz) | Chroma Sampling Level |
| --- | --- | --- |
| 3840 x 2160 (4K UHD) | 60, 59.94, 50, 30, 29.97, 25, 24 | 4:4:4 |
| 3440 x 1440 | 60 | 4:4:4 |
| 2560 x 1600 | 60 | 4:4:4 |
| 2560 x 1440 | 60 | 4:4:4 |
| 2560 x 1080 | 60, 59.94, 50, 30, 29.97, 25, 24 | 4:4:4 |
| 1920 x 1200 | 60 | 4:4:4 |
| 1920 x 1080 (1080p) | 60, 59.94, 50, 30, 29.97, 25, 24 | 4:4:4 |

\* All video formats are progressive.

1 This table is a small subset of the most common formats. Many other formats and timings are also supported.

### Scaler

Each HDMI output features a robust, polymorphic 4K60 4:4:4 scaler that can accommodate the most challenging resolution and frame rate conversions. The scaler on each HDMI output is capable of operating in three modes (configurable within Q-SYS Designer Software):

* Stretch-to-Fit
* Maintain Aspect Ratio
* 1:1 Pixel Mapping

[Security](javascript:void(0))

Supports AES-128 encryption for audio and video signals from encoders to decoders as well as 802.1x authentication (available in Q-SYS Designer Software v8.4 or higher).

Content Protection: HDCP 2.2 compliant

[I/O Configurations](javascript:void(0))

In Peripheral Mode only, the NV-32-H is software-configurable in Q-SYS Designer as either an Encoder or Decoder.

### Encoder

* Encode one 4K60 HDMI video stream or up to three 1080p HDMI videos streams for distribution across a standard gigabit network.
* Courtesy monitor: Use HDMI Out 1 as a âcourtesy monitorâ, displaying any of the three locally connected HDMI sources at resolutions up to 4K60.

### Decoder

* Decode one 4K60 network stream or up to two simultaneous 1080p60 streams (for dual display rooms) for displaying at formats up to 4K60 on a connected display.
* Local source switching: Toggle between network streams or locally connected HDMI sources (single 4K60 or dual 1080p60 sources).

[Specifications](javascript:void(0))

Refer to the Specifications Sheet on the [NV-32-H (Core Capable) product page](https://www.qsys.com/products-solutions/q-sys/processing/nv-32-h-core-capable/) at qsys.com.
