# Core 8 Flex

> Source: https://help.qsys.com/Content/Hardware/Processing/Core_8_Flex.htm

# Core 8 Flex

The Core 8 Flex audio, video and control (AV&C) processor extends the applications of the Q-SYS Ecosystem into a wider range of smaller-scale installations across corporate, higher education, healthcare and beyond. Built on the same foundational technology as the rest of the Q-SYS processor portfolio, including the best-in-class Q-SYS Core 110f, Core 8 Flex is designed for applications with lower network or analog channel capacity and/or targeted processing requirements.

**Note:** For installation and connection instructions, drawings, and other documentation, refer to the Resources section on the [Core 8 Flex product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/q-sys-cores/core-8-flex/) on the QSC website.

[Features](javascript:void(0))

**Note:** Q-SYS Scaling Licenses expand the capabilities of the Core 8 Flex. Refer to the [Licensing](../../Core_Manager/Core_Management/Licensing.htm) topic for more information.

| Feature | Core 8 Flex |
| --- | --- |
| Total Network I/O | 64 x 64 |
| Onboard I/O | 8 flex |
| Software-based Dante Capacity | 8 x 8 included (up to 32 x 32) |
| USB Audio Channel Count | 8 x 8 |
| AEC Processors | 8 |
| VoIP Instances | 2 |
| Onboard AV Bridging (USB) | Yes |
| Onboard GPIO | 8 x 8 |
| Onboard RS232 Control Ports | 2 |
| Q-SYS Peripheral Limit[1](#Includes) | 32 |
| Size | 1/2 rack, 1RU |

###### 1. Includes native Q-SYS cameras, I/O (including NL), NV, TSCs, paging stations, Extensions and plugins with their âIs Managedâ property set to âYesâ. It does not include Streaming I/O, Loudspeakers, Scripts or plugins with their âIs Managedâ property set to âNoâ.

[Switching Modes](javascript:void(0))

The Core 8 Flex is configurable in Core Mode or Peripheral Mode. By default, the Core 8 Flex ships from the factory in Core Mode. It's easy to switch modes.

[Core Mode to Peripheral Mode](javascript:void(0))

1. Open [Core Manager](../../Core_Manager/CoreManager_Overview.htm) for the Core 8 Flex.
2. From the Utilities menu, change the Mode property to 'Peripheral'.
3. Click Switch.

Once the device reboots, you can then configure it using [Configurator](../0017_Configurator.htm) > Peripheral Manager. In your design, add the I/O-Core 8 Flex to your design from the Inventory > Audio - Q-LAN menu. Once you save and run your design to the Core, the I/O-Core 8 Flex will then be functional as a peripheral after its firmware updates.

[Peripheral Mode to Core Mode](javascript:void(0))

1. From [Configurator](../0017_Configurator.htm) (Tools > Show Configurator), locate the I/O-Core 8 Flex from the I/O Devices category.
2. Click the device to open Peripheral Manager.
3. From the Utilities tab, change the Mode property to 'Core'.
4. Click Switch.

Once the device reboots, you can then configure it using [Core Manager](../../Core_Manager/CoreManager_Overview.htm). In your design, be sure to change Core Properties > Model to 'Core 8 Flex'. Once you save and run your design to the Core, the Core 8 Flex will then be functional as a Q-SYS Core processor after its firmware updates.

[Design Components](javascript:void(0))

Available Inventory components depend on whether the Core 8 Flex is configured for Core Mode or Peripheral Mode.

[Core Mode](javascript:void(0))

**Core Mode** allows the Q-SYS Core processor to operate as a standalone audio and control processing unit. In Core Mode, this Q-SYS Core functions independently without relying on an external Q-SYS system or design file.

#### Standard Components

* [Status (Core)](../../Schematic_Library/core_status.htm)
* [Flex In (I/O-Core 8 Flex)](../../Schematic_Library/io_card_flex_in_io_core_8_flex.htm)
* [Flex Out (Core 8 Flex)](../../Schematic_Library/io_card_flex_out_core_8flex.htm)
* [GPIO In (Core 8 Flex , Core 24f, and I/O-Core 24f)](../../Schematic_Library/io8flex_gpio_input.htm)
* [GPIO Out (Core 8 Flex , Core 24f, and I/O-Core 24f)](../../Schematic_Library/io8flex_gpio_output.htm)
* [Serial Port (Core and I/O Devices)](../../Schematic_Library/serial_port.htm)
* [Loudspeaker Monitor](../../Schematic_Library/loudspeaker_monitor.htm)
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

[Peripheral Mode (I/O-Core 8 Flex)](javascript:void(0))

**Peripheral Mode** allows the Q-SYS Core processor to operate as a peripheral device in an AV network rather than the central processing unit. In this mode, this Core can serve as an input/output expander, handling audio and control signals, while the core processing tasks are offloaded to a separate Q-SYS Core processor.

#### Standard Components

* [Status (I/O-Core 8 Flex)](../../Schematic_Library/io_core_8_flex_status.htm)
* [GPIO In (Core 8 Flex , Core 24f, and I/O-Core 24f)](../../Schematic_Library/io8flex_gpio_input.htm)
* [GPIO Out (Core 8 Flex , Core 24f, and I/O-Core 24f)](../../Schematic_Library/io8flex_gpio_output.htm)
* [Serial Port (Core and I/O Devices)](../../Schematic_Library/serial_port.htm)
* [HID Keyboard](../../Schematic_Library/usb_keyboard.htm)
* [HID Media](../../Schematic_Library/usb_ccontrols.htm)
* [HID Conferencing](../../Schematic_Library/usb_telephony.htm)

**Note:** USB Input and USB Output components are not supported in Peripheral Mode.

#### External USB Audio

* [External USB Audio Device In](../../Schematic_Library/alsa_receiver_sound_card.htm)
* [External USB Audio Device Out](../../Schematic_Library/alsa_transmitter_sound_card.htm)

#### USB Video Bridge

* [USB Video Bridge](../../Schematic_Library/usb_uvc.htm)

#### USB Audio Bridge

* [USB Audio Bridge â Speakerphone / Sound Card In](../../Schematic_Library/usb_receiver.htm)
* [USB Audio Bridge â Speakerphone / Sound Card Out](../../Schematic_Library/usb_transmitter.htm)

[Connections and Callouts](javascript:void(0))

### Front Panel

1. Power LED â Illuminates blue when the Q-SYS Core 8 Flex is powered on.
2. ID LED â Blinks when placed into ID Mode via ID Button or Q-SYS Configurator.
3. ID Button â Locates the Q-SYS Core 8 Flex in Q-SYS Designer and Configurator. Pressing the button for 10 seconds resets the Core to its default network settings and host name and also clears the currently running design.

### Rear Panel

1. FLEX Channels â Eight user-configurable analog audio input/output channels, with phantom power on inputs
2. +12VDC â up to 0.1A source. Connector pins â+â
3. GPIO Outputs â 8 outputs, open collector (24V, 0.2A max.) with p/u to +3.3V (lower pins 1 â 8)
4. GND â Earth ground. Connector pins with ground symbol.
5. GPIO Inputs â 8 inputs, 0-24V analog input or contact closure (upper pins 1 â 8)
6. RS232 â COM x2. 3-position, 3.5mm connector
7. USB Type C â USB 3.1, Host port, DisplayPort, Device port (when USB Type B not in use)
8. USB Type B â USB 3.0, dedicated Device port
9. LAN A â RJ45, 1000 Mbps, primary, Q-LAN, AES67, Dante, VoIP, WAN streaming, control
10. USB Type A â USB 3.0 x2, Host ports
11. LAN B â RJ45, 1000 Mbps, backup, Q-LAN, AES67, Dante, VoIP, WAN streaming, control
12. USB Type A â USB 3.0 x2, Host ports
13. AC mains â IEC 60320, C14 receptacle, universal power in (100V â 240V, 50/60 Hz)

[Specifications](javascript:void(0))

Refer to the Specifications Sheet on the [Core 8 Flex product page](https://www.qsys.com/products-solutions/q-sys/processing/core-8-flex/) at qsys.com.
