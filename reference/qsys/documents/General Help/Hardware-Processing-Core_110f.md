# Core 110f

> Source: https://help.qsys.com/Content/Hardware/Processing/Core_110f.htm

# Core 110f

The Q-SYSâ¢ Core 110f processor provides a fully integrated audio, video and control solution for installations with a mixture of analog and network channels, supporting medium-sized rooms through the largest Enterprise scale deployments.

**Note:** Q-SYS Core 110f units with 2 GB of RAM, manufactured before April 2017, are no longer supported in Q-SYS Designer v10.0 or later. However, some units may have had their motherboards replaced, resulting in 4 or 8 GB of RAM. Despite their earlier manufacturing dates, these upgraded units are supported in Q-SYS Designer v10.0 and later.

[Features](javascript:void(0))

| Feature | Core 110f |
| --- | --- |
| Total network I/O | 128 x 128[1](#_bm) |
| Onboard I/O | 8x in, 8x out, 8x flex |
| Software-based Dante capacity | 8 x 8 included (up to 32 x 32) |
| USB audio channel count | 16 x 16 |
| AEC processors | 16 |
| VoIP instances | 4 |
| Onboard AV bridging (USB) | Yes |
| Onboard GPIO | Core 110f: 16 x 16  Core 110f v2: N/A |
| Onboard RS232 control ports | 1 |
| Maximum NV Series Network Video Endpoints | 32 |
| Maximum NL, NM, and QIO Series Endpoints | 32 |
| Size | 1RU |

###### 1. When using the Core 110f on-board USB Device Port for video bridging, the Q-LAN / AES67 maximum audio channel count is 80 x 64 (Q-SYS version 9.7 and later) or 64 x 64 (Q-SYS version 9.6 and earlier).

[Switching Modes](javascript:void(0))

The Core 110f is configurable in Core Mode or Peripheral Mode. By default, the Core 110f ships from the factory in Core Mode. It's easy to switch modes.

[Core Mode to Peripheral Mode](javascript:void(0))

1. Open [Core Manager](../../Core_Manager/CoreManager_Overview.htm) for the Core 110f.
2. From the Utilities menu, change the Mode property to 'Peripheral'.
3. Click Switch.

Once the device reboots, you can then configure it using [Configurator](../0017_Configurator.htm) > Peripheral Manager. In your design, add the I/O-Core 110f to your design from the Inventory > Audio - Q-LAN menu. Once you save and run your design to the Core, the I/O-Core 110f will then be functional as a peripheral after its firmware updates.

[Peripheral Mode to Core Mode](javascript:void(0))

1. From [Configurator](../0017_Configurator.htm) (Tools > Show Configurator), locate the I/O-Core 110f from the I/O Devices category.
2. Click the device to open Peripheral Manager.
3. From the Utilities tab, change the Mode property to 'Core'.
4. Click Switch.

Once the device reboots, you can then configure it using [Core Manager](../../Core_Manager/CoreManager_Overview.htm). In your design, be sure to change Core Properties > Model to 'Core 110f'. Once you save and run your design to the Core, the Core 110f will then be functional as a Q-SYS Core processor after its firmware updates.

[Design Components](javascript:void(0))

Available Inventory components depend on whether the Core 110f is configured for Core Mode or Peripheral Mode.

[Core Mode](javascript:void(0))

**Core Mode** allows the Q-SYS Core processor to operate as a standalone audio and control processing unit. In Core Mode, this Q-SYS Core functions independently without relying on an external Q-SYS system or design file.

#### Standard Components

* [Status (Core)](../../Schematic_Library/core_status.htm)
* [Mic/Line In (Core 110f, 110c)](../../Schematic_Library/io_card_mic_line_in_core_110i.htm)
* [Flex In (Core 110f, 110c)](../../Schematic_Library/io_card_flex_in_core_110i.htm)
* [Line Out (Core 110f, 110c)](../../Schematic_Library/io_card_line_out_core_110i.htm)
* [Flex Out (Core 110f, 110c)](../../Schematic_Library/io_card_flex_out_core_110i.htm)
* [POTS In](../../Schematic_Library/io_card_pots_input_for_core.htm)
* [POTS Out](../../Schematic_Library/io_card_pots_output_for_core.htm)
* [POTS Controller](../../Schematic_Library/pots_control_status_core.htm)
* [GPIO In (Core 110f, I/O-Core 110f, Core 110c)](../../Schematic_Library/io110_gpio_input.htm) â Not applicable to the Core 110f v2
* [GPIO Out (Core 110f, I/O-Core 110f, Core 110c)](../../Schematic_Library/io110_gpio_output.htm) â Not applicable to the Core 110f v2
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

[Peripheral Mode (I/O-Core 110f](javascript:void(0))

**Peripheral Mode** allows the Q-SYS Core processor to operate as a peripheral device in an AV network rather than the central processing unit. In this mode, this Core can serve as an input/output expander, handling audio and control signals, while the core processing tasks are offloaded to a separate Q-SYS Core processor.

#### Standard Components

* [Status (I/O-Core 110f)](../../Schematic_Library/io_core_110f_status.htm)
* [Mic/Line In (I/O-Core 110f)](../../Schematic_Library/io_card_mic_line_in_io_core_110f.htm)
* [Flex In (I/O-Core 110f)](../../Schematic_Library/io_card_flex_in_io_core_110f.htm)
* [Line Out (I/O-Core 110f)](../../Schematic_Library/io_card_line_out_io_core_110f.htm)
* [Flex Out (I/O-Core 110f)](../../Schematic_Library/io_card_flex_out_io_core_110f.htm)
* [POTS In (I/O-Core 110f)](../../Schematic_Library/io_card_pots_input_for_io_core_110f.htm)
* [POTS Out (I/O-Core 110f)](../../Schematic_Library/io_card_pots_output_for_io_core_110f.htm)
* [POTS Controller (I/O-Core 110f)](../../Schematic_Library/pots_control_status_io_core_110f.htm)
* [GPIO In (Core 110f, I/O-Core 110f, Core 110c)](../../Schematic_Library/io110_gpio_input.htm) â Not applicable to the Core 110f v2
* [GPIO Out (Core 110f, I/O-Core 110f, Core 110c)](../../Schematic_Library/io110_gpio_output.htm) â Not applicable to the Core 110f v2
* [Serial Port (Core and I/O Devices)](../../Schematic_Library/serial_port.htm)
* [Loudspeaker Monitor](../../Schematic_Library/loudspeaker_monitor.htm)
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

### Front Panel â Core 110f

1. OLED Display â displays information about the core's settings and status.
2. Next button â cycles through the information pages
3. ID button â locates the Core in Q-SYS Designer GUI and Configurator
4. Power LED â illuminates blue when the Core is on
5. USB Type A Host connectors (2)

### Front Panel â Core 110f v2

1. Power LED â Illuminates blue when the Q-SYS Core 110 Series processor is powered on
2. ID LED â LED blinks when placed into ID Mode via ID Button or Q-SYS Designer Software
3. ID Button â Locates the Q-SYS Core 110 Series processor in Q-SYS Designer Software

### Rear Panel â Left Side

All audio inputs and outputs use one 3-position, 3.5mm Euro connector for each channel. GPIO uses one 10-position 3.5mm Euro connector for each row. Configure all inputs and outputs in Q-SYS Designer.

**Note:** GPIO connections are not applicable to the Core 110f v2.

1. Mic/Line Inputs â eight channels, balanced or unbalanced, phantom power â orange
2. Flex Channels â eight user-configurable input/output channels, balanced or unbalanced, phantom power on inputs â blue
3. Mic/Line Outputs â eight channels, balanced or unbalanced - green

The following connections use the black Euro plug and are not applicable to the Core 110f v2:

1. 12VDC, 0.2A Outputs + uses connector pins 1 and 11 (not numbered)
2. General-purpose Inputs â 16 inputs, 0-24V analog input, or contact closure (Pins labeled 1â16 equal pins 1â16 in the Q-SYS Designer GPIO Input component)
3. Earth ground â uses pins 10 and 20 (not numbered)
4. General-purpose Outputs â 16 outputs, open collector (24V, 0.2A maximum) with pull up to +3.3V (Pins labeled 1â16 equal pins 1â16 in the Q-SYS Designer GPIO Output component)

### Rear Panel â Right Side

1. Telephone Line â RJ11 (6P2C)
2. Serial Number of the Core 110
3. External Power Input â Auxiliary power, 12VDC, 10A, 2-pin, 5 mm Euro connector.

   **Note:** Auxiliary power and AC power are parallel. They can be used simultaneously. If one source of power fails, it will "fail over" to the other power source without interruption.
4. RS232 â Transmit and receive, 3-pin, 5 mm, Euro connector
5. HDMI â for future use
6. USB Type B Device connector
7. LAN A â Q-LAN, control, VoIP, WAN streaming, AES67 etc., RJ45
8. USB Type A Host connectors (4) for future use
9. LAN-B â Redundancy, control, VoIP, etc.
10. A/C Power Input â IEC connector, 100-240V ~ 50-60 Hz, 150W, universal power supply

[OLED Screens](javascript:void(0))

**Note:** The front panel OLED is not applicable to the Core 110f v2.

### Design Status

* Device â The name of the Core as defined in Q-SYS Designer.
* Design â The name of the currently running design.
* Status â
  + OK â Audio is good, hardware is good.
  + Compromised â Audio is good but a redundancy mechanism is active (one LAN down but the other is still up) or a non-fatal hardware problem exists (fans too slow, temperature higher than expected, etc.)
  + Fault â Audio is not passing, or hardware is malfunctioning or mis-configured
  + Missing â A piece of hardware, defined in the design, has not been discovered. Audio is not passing through that piece of hardware.
  + Initializing â Starting the firmware, configuration update, and the design. Audio is obviously bad.
  + Not Present â A virtual component in the design, that is designated as Dynamically Paired, and Not Required, has no hardware assigned to it.

### System Status

* Firmware â A three-section number identifying the major release, minor release, and maintenance release. For example, 5.0.06.
* Temp â The current chassis temperature of the Core.
  + Compromised threshold = 60Â° C
  + Fault threshold = 70Â° C
* Fan Speed â This number varies with the temperature.

### LAN A

* Static or Auto â Displays next to LAN A, indicates if the Core's IP Address is Static or Automatic.
* IP Address â The IP Address assigned to the Core's LAN A. LAN A is the primary Q-LAN connection to the Core, and is required.
* Net Mask â The Net Mask assigned to the Core.
* Gateway â The Gateway assigned to the Core.

**Note:** You can edit this information in [Core Manager](../../Core_Manager/CoreManager_Overview.htm).

### LAN B

LAN B is used for redundancy, and is not required. The information is the same as LAN A.

### Input / Flex In Channels Status

The Input and Flex Input screens show the Mute, Clip, Signal, and +48V (phantom power) for the eight Mic/Line input channels.

* Mute â Displays a "muted loudspeaker" when the channel is muted.
* Clip â Displays a solid circle under the channel having an input signal that is overdriving the associated channel input.
* Signal â Displays a solid circle when there is a signal present on the associated channel.
* +48V â Displays a solid circle when the phantom power is turned on for the associated channel.

**Note:** If the Flex channel is set to Output, there is no information for that channel on the Flex In screen.

### Output / Flex Out Channels Status

The Output and Flex Output screens show the Mute, Clip, and Signal, for the eight Mic/Line output channels.

* Mute â Displays a "muted loudspeaker" when the channel is muted.
* Clip â Displays a solid circle under the channel having an output signal over driving the associated channel output.
* Signal â Displays a solid circle when there is a signal present on the associated channel.

**Note:** If a Flex channel is set to Input, there is no information shown under the same channel on the Flex Out screen.

[POTS Specifications](javascript:void(0))

The POTS Controller component controls the features of the Q-SYS interface with a Plain Old Telephone Service (POTS).

If you are connecting to an analog phone system, you can connect from the wall RJ-11 jack directly to Q-SYS hardware supporting a POTS connection:

* The [Core 110f](#) and [Core 110c](Core_110c.htm) provide a single RJ-11 telephone connection.
* The [CTEL4 â Analog Telephony Card](../IO_Expanders/CTEL4.htm) provides four RJ-11 telephone connections.

If you are connecting to a digital system, you can use an FXO Gateway that has an analog POTS connection and a network connection. For more information, visit the [POTS Controller](../../Schematic_Library/pots_control_status.htm) topic.

| Technical Specifications | |
| --- | --- |
| Input / Output Impedance | 600 ohms, nominal |
| Frequency Response | 300Hz - 3.3kHz +/- 0.5dB |
| Dynamic Range | 54 dB |
| Station Port Compatibility | Two-wire ring start |
| Ringer Equivalence | CTEL4: 0.0B  Core 110f: 0.1  Core 11c: 0.1 |
| Electronic or 1A2 Line Key | No1 |
| PABX Loop | No1 |
| Trunk Port Compatibility | Two-wire loop start |
| Number of phone lines | CTEL4: 4 lines  Core 110f: 1 line  Core 110c: 1 line |
| Loop Current Interruption (CPC Pulse) | Interpreted as line disconnect |

1. Each Q-SYS phone line is meant to be connected to a single PSTN line (FXO). It does not control a multi-line PBX or interface with an FXS.
