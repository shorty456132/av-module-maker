# I/O-USB Bridge

> Source: https://help.qsys.com/Content/Hardware/IO_Expanders/IOUSB_Bridge.htm

# I/O-USB Bridge

The I/O-USB Bridge allows you to integrate networked Q-SYS conference room camera video â alongside industry-leading audio processing â into soft-codec applications via a USB connection, without the need for special drivers. The I/O-USB Bridge can act as an in-rack or Bring Your Own Device (BYOD) endpoint for Q-SYS PTZ IP conferencing camera feeds and audio processed with Q-SYS acoustic echo cancellation (AEC).

**Note:** This topic provides an overview of the I/O-USB Bridge peripheral. For installation instructions and other details, see the [I/O-USB Bridge product page](https://www.qsys.com/products-solutions/q-sys/audio-io-peripherals/io-usb-bridge/).

[Features](javascript:void(0))

* Driverless USB 2.0 Connection
* Built for BYOD (plug and play)
* Resolutions up to 1080p
* Emulates webcam video and AEC speakerphone audio over single USB connection
* Emulates computer soundcard
* Bridges audio and video over Q-LAN to USB
* External Power Supply or PoE enabled (802.3af)

[Design Components](javascript:void(0))

Add the I/O-USB Bridge to your design inventory from the Peripherals category. The following components are available for the I/O-USB Bridge, depending on its Properties:

* [Status (I/O USB Bridge)](../../Schematic_Library/io_usb_bridge.htm)
* [USB Audio Bridge â Speakerphone / Sound Card In](../../Schematic_Library/usb_receiver.htm)
* [USB Audio Bridge â Speakerphone / Sound Card Out](../../Schematic_Library/usb_transmitter.htm)
* [USB Video Bridge](../../Schematic_Library/usb_uvc.htm)
* [HID Keyboard](../../Schematic_Library/usb_keyboard.htm)
* [HID Media](../../Schematic_Library/usb_ccontrols.htm)
* [HID Conferencing](../../Schematic_Library/usb_telephony.htm)
* [USB Input](../../Schematic_Library/usb_input.htm)
* [USB Output](../../Schematic_Library/usb_output.htm)
* [Serial Port (I/O USB Bridge)](../../Schematic_Library/serial_port_usbbr.htm)
* [External USB Audio Device In](../../Schematic_Library/alsa_receiver_sound_card.htm)
* [External USB Audio Device Out](../../Schematic_Library/alsa_transmitter_sound_card.htm)

[Connections and Callouts](javascript:void(0))

### Front Panel

1. **USB 2.0 Type A host ports**âTotal maximum current available from these ports is 500 mA with PoE or external 12 V 2A DC supply.
2. **USB 2.0 Type B device port**âConnect to a host PC to bridge Q-SYS audio and/or video (UAC / UVC).
3. **Power LED** indicator.
4. **ID button and LED indicator**âPress the button to identify this unit in Q-SYS Designer or Q-SYS Configurator. The LED blinks when this device's ID mode is enabled by pressing the ID button or through Q-SYS Designer or Q-SYS Configurator.

### Rear Panel

1. **LAN A / PoE port**âfor LAN connection. The I/O-USB Bridge is a PoE Enabled Device (802.3af). Use a suitable PoE network switch or supply through this port.
2. **LAN B port**âfor LAN connection.
3. **HDMI output port**âfor future functionality.
4. **Reset switch**. To reset the unit, insert a straightened paper clip or similar tool into this opening to press this switch for 10 seconds.
5. **RS232 port**.
6. **External 12V DC power supply connection**âfor redundancy, or in the absence of a PoE supply. The minimum power requirements are 12 V, 1 A; to provide maximum current for multiple USB connections, use a 12 V, 2 A supply.

[Specifications](javascript:void(0))

|  |  |
| --- | --- |
| Supported Resolutions | (All aspect ratios 16:9, all refresh rates 30fps)  MJPEG: 1080p, 720p, 576p YUY2: 360p, 270p, 180p |
| USB Connection | - USB 2.0 (UVC/UAC) driverless connection for Windows and OS X devices  - Emulates webcam video driver, AEC speakerphone audio driver, and multi-channel soundcard driver over single USB connection |
| Power Supply | PoE Enabled Device (802.3af - Class 3) or 12v DC (1A) |
| Dimensions | 1in x 3.35in x 7.2in (25mm x 85mm x 183mm) |
| Weight | 1.1 lbs. (500g) |

For more information, and to see a list of related documentation, visit the [I/O-USB Bridge](https://www.qsys.com/systems/products/q-sys-platform/products-peripherals-accessories/conference-room-integration/io-usb-bridge/) product page on the QSC website.
