# Core 24f

> Source: https://help.qsys.com/Content/Hardware/Processing/Core_24f.htm

# Core 24f

The Q-SYS Core 24f processor provides a fully integrated audio, video, and control solution for installations with a mixture of analog and network channels, supporting meeting room environments or conferencing systems. Core 24f provides system audio, control, and VoIP telephony services, as well as Core services for other audio, video, and control peripherals.

[Features](javascript:void(0))

* 160 x 160 Network I/O
* 8 mic/line inputs, 8 line outputs, and 8 FLEX I/O
* 64 x 64 Software-based Dante capacity
* 16 x 16 USB audio channel count
* 24 AEC processors
* 8 VoIP instances
* Onboard AV bridging (USB)
* 8 x 8 Onboard GPIO
* 2 Onboard RS232 control ports
* 96 Q-SYS peripheral limit
* 1RU Size

[Switching Modes](javascript:void(0))

The Core 24f is configurable in Core Mode or Peripheral Mode. By default, the Core 24f ships from the factory in Core Mode. It's easy to switch modes.

[Core Mode to Peripheral Mode](javascript:void(0))

1. Open [Core Manager](../../Core_Manager/CoreManager_Overview.htm) for the Core 24f.
2. From the Utilities menu, change the Mode property to 'Peripheral'.
3. Click Switch.

Once the device reboots, you can then configure it using [Configurator](../0017_Configurator.htm) > Peripheral Manager. In your design, add the I/O-Core 24f to your design from the Inventory > Audio - Q-LAN menu. Once you save and run your design to the Core, the I/O-Core 24f will then be functional as a peripheral after its firmware updates.

[Peripheral Mode to Core Mode](javascript:void(0))

1. From [Configurator](../0017_Configurator.htm) (Tools > Show Configurator), locate the I/O-Core 24f from the I/O Devices category.
2. Click the device to open Peripheral Manager.
3. From the Utilities tab, change the Mode property to 'Core'.
4. Click Switch.

Once the device reboots, you can then configure it using [Core Manager](../../Core_Manager/CoreManager_Overview.htm). In your design, be sure to change Core Properties > Model to 'Core 24f'. Once you save and run your design to the Core, the Core 24f will then be functional as a Q-SYS Core processor after its firmware updates.

[Design Components](javascript:void(0))

Available Inventory components depend on whether the Core 24f is configured for Core Mode or Peripheral Mode.

[Core Mode](javascript:void(0))

**Core Mode** allows the Q-SYS Core processor to operate as a standalone audio and control processing unit. In Core Mode, this Q-SYS Core functions independently without relying on an external Q-SYS system or design file.

#### Standard Components

* [Status (Core)](../../Schematic_Library/core_status.htm)
* [Mic/Line In (Core 24f)](../../Schematic_Library/io_card_mic_line_in_core_24f.htm)
* [Line Out (Core 24f)](../../Schematic_Library/io_card_line_out_core_24f.htm)
* [Flex In (Core 24f)](../../Schematic_Library/io_card_flex_in_core_24f.htm)
* [Flex Out (Core 24f)](../../Schematic_Library/io_card_flex_out_core_24f.htm)
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

#### USB Video Bridge

* [USB Video Bridge](../../Schematic_Library/usb_uvc.htm)

#### USB Audio Bridge

* [USB Audio Bridge â Speakerphone / Sound Card In](../../Schematic_Library/usb_receiver.htm)
* [USB Audio Bridge â Speakerphone / Sound Card Out](../../Schematic_Library/usb_transmitter.htm)

[Peripheral Mode (I/O-Core 24f)](javascript:void(0))

**Peripheral Mode** allows the Q-SYS Core processor to operate as a peripheral device in an AV network rather than the central processing unit. In this mode, this Core can serve as an input/output expander, handling audio and control signals, while the core processing tasks are offloaded to a separate Q-SYS Core processor.

#### Standard Components

* [Status (I/O-Core 24f)](../../Schematic_Library/io_core_24f_status.htm)
* [Mic/Line In (I/O-Core 24f)](../../Schematic_Library/io_card_mic_line_in_io_core_24f.htm)
* [Line Out (I/O-Core 24f)](../../Schematic_Library/io_card_line_out_io_core_24f.htm)
* [Flex In (I/O-Core 24f)](../../Schematic_Library/io_card_flex_in_io_core_24f.htm)
* [Flex Out (I/O-Core 24f)](../../Schematic_Library/io_card_flex_out_io_core_24f.htm)
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

#### USB Video Bridge

* [USB Video Bridge](../../Schematic_Library/usb_uvc.htm)

#### USB Audio Bridge

* [USB Audio Bridge â Speakerphone / Sound Card In](../../Schematic_Library/usb_receiver.htm)
* [USB Audio Bridge â Speakerphone / Sound Card Out](../../Schematic_Library/usb_transmitter.htm)

[Connections and Callouts](javascript:void(0))

### Front Panel

1. **Air intake vents**
2. **2x20 character OLED display**
3. **PAGE button** â for screen navigation
4. **ID button** â invokes ID feature
5. **ID LED** â illuminates when ID feature is invoked
6. **POWER on** â LED

### Rear Panel

#### Left Side

1. **Mic/Line Inputs** â (8 channels - orange) Balanced or Unbalanced plus +48V (P48) phantom power compliant with IEC 61938
2. **Flex Channels** â (8 channels - blue) Configurable as Mic/Line Input or Line Output per channel
3. **Line Outputs** â (8 channels - green) Balanced or Unbalanced
4. **General Purpose Outputs** â (8 pins, 2-9) Open collector (24V, 0.2A max), with pullups to 3.3V or TTL output
5. **Ground Reference** â (Pin 10 on each connector)
6. **12VDC Source** â (Pin 1 on each connector). Provides up to 0.2A per pin
7. **General Purpose Inputs** â (8 pins, 2-9) 0-24VDC analog, potentiometer, TTL digital or contact closure input. GPI 1 may be configured as a word clock input

#### Right Side

1. **COM ports** â (dual) RS232, 3-terminal
2. **USB C Host** â Device or DisplayPort Alt Mode USB 3.1, source up to 2.0A to a Device
3. **USB A ports** â (dual) USB 3.1, source up to 900mA per port
4. **LAN ports** â (quad) Up to 2.5 Gbps per port
   * Two (2) 2.5 Gbps Ethernet ports for redundant networked audio (QLAN, AES67, VoIP, WAN, Media Streaming, etc.)
   * Two (2) 2.5 Gbps independent, auxiliary Ethernet ports
5. **Exhaust vents** â (do not block)
6. **AC mains inlet connector** â Supports universal (international) mains

[Specifications](javascript:void(0))

For complete product specs, refer to the Specifications Sheet on the Core 24f [product page](https://www.qsys.com/products/q-sys/processing/core-24f/) at qsys.com.
