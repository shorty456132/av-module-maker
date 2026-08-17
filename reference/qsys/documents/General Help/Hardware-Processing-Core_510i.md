# Core 510i

> Source: https://help.qsys.com/Content/Hardware/Processing/Core_510i.htm

# Core 510i

The Q-SYS Core 510i represents the second generation of QSCâs Integrated Core Platform. It features eight I/O card slots, which can be populated with any combination of Q-SYS I/O cards allowing for up to 128x128 local channels plus a total of 256x256 network channels for diverse connectivity options.

**Note:** This topic provides an overview of the Core 510i. For installation instructions and other documentation, see the [Core 510i product page](https://www.qsys.com/products-solutions/q-sys/processing/core-510i/) online.

[Features](javascript:void(0))

|  |  |
| --- | --- |
| Local I/O Channels | Up to 32 analog, up to 128x128 AES/CobraNet/Dante/AVB |
| Network Audio Channels | 256 x 256 |
| AEC Processors | 64 |
| Multitrack Audio Players | 16 (upgradable to 128) |
| Local I/O Card Capacity | 8 |
| VoIP Instances | 64 |
| Q-SYS peripheral limit | It is recommended not to exceed 128 NL, NM, or QIO Series peripherals in a design in any combination. |

* Q-SYS Core processing in a flexible chassis featuring 8 onboard I/O card slots
* Install any combination of Q-SYS [Q-SYS Products](../Hardware_Overview.htm#IO_Cards) for maximum flexibility
* Audio, video and control processing on a dedicated Linuxâ¢ realtime OS
* Software configurable as either a Core 510i processor, or an I/O-510i expander
* Built using standard computer industry hardware and IT industry networking protocols
* Control and integrate external devices using TCP/IP, RS232 and GPIO
* Design with powerful and intuitive Q-SYS Designer Software application
* Seamlessly integrates with Q-SYS AV-to-USB bridging peripherals
* Provides simple integration with QSC amplifiers and loudspeakers
* Multiple levels of system redundancy

[Switching Modes](javascript:void(0))

The Core 510i is configurable in Core Mode or Peripheral Mode. By default, the Core 510i ships from the factory in Core Mode. It's easy to switch modes.

**Core Mode** allows the Q-SYS Core processor to operate as a standalone audio and control processing unit. In Core Mode, this Q-SYS Core functions independently without relying on an external Q-SYS system or design file.

**Peripheral Mode** allows the Q-SYS Core processor to operate as a peripheral device in an AV network rather than the central processing unit. In this mode, this Core can serve as an input/output expander, handling audio and control signals, while the core processing tasks are offloaded to a separate Q-SYS Core processor.

[Core Mode to Peripheral Mode](javascript:void(0))

1. Open [Core Manager](../../Core_Manager/CoreManager_Overview.htm) for the Core 510i.
2. From the Utilities menu, change the Mode property to 'Peripheral'.
3. Click Switch.

Once the device reboots, you can then configure it using [Configurator](../0017_Configurator.htm) > Peripheral Manager. In your design, add the I/O-510i to your design from the Inventory > Audio - Q-LAN menu. Once you save and run your design to the Core, the I/O-510i will then be functional as a peripheral after its firmware updates.

[Peripheral Mode to Core Mode](javascript:void(0))

1. From [Configurator](../0017_Configurator.htm) (Tools > Show Configurator), locate the I/O-510i from the I/O Devices category.
2. Click the device to open Peripheral Manager.
3. From the Utilities tab, change the Mode property to 'Core'.
4. Click Switch.

Once the device reboots, you can then configure it using [Core Manager](../../Core_Manager/CoreManager_Overview.htm). In your design, be sure to change Core Properties > Model to 'Core 510i'. Once you save and run your design to the Core, the Core 510i will then be functional as a Q-SYS Core processor after its firmware updates.

[Design Components](javascript:void(0))

The following Q-SYS Designer components are available for the Core 510i, depending on its Properties:

#### Standard Components

* [Status (Core)](../../Schematic_Library/core_status.htm)
* [GPIO (Core 510i)](../../Schematic_Library/gpio.htm)
* [Loudspeaker Monitor](../../Schematic_Library/loudspeaker_monitor.htm)
* [Serial Port (Core and I/O Devices)](../../Schematic_Library/serial_port.htm)

#### I/O Card Components

For a description of individual I/O card hardware, see [Q-SYS Products](../Hardware_Overview.htm#IO_Cards).

* [Line Out (I/O Card)](../../Schematic_Library/io_output_card.htm)
* [Mic/Line In (I/O Card)](../../Schematic_Library/io_input_card.htm)
* [DataPort Out](../../Schematic_Library/io_card_dataport.htm)
* [AES3 In / Out](../../Schematic_Library/io_aes_card.htm)
* [CobraNet In](../../Schematic_Library/io_cobranet_input_card_core.htm)
* [CobraNet Out](../../Schematic_Library/io_cobranet_output_card_core.htm)
* [Dante In](../../Schematic_Library/io_dante_input_card_core.htm)
* [Dante Out](../../Schematic_Library/io_dante_output_card_core.htm)
* [Status (AVB)](../../Schematic_Library/io_avb_card_status_core.htm)
* [AVB In](../../Schematic_Library/io_avb_input_card_core.htm)
* [AVB Out](../../Schematic_Library/io_avb_output_card_core.htm)
* [16-Channel AES3 In](../../Schematic_Library/io_aes_16_input_card_core.htm)
* [POTS In](../../Schematic_Library/io_card_pots_input_for_core.htm)
* [POTS Out](../../Schematic_Library/io_card_pots_output_for_core.htm)
* [POTS Controller](../../Schematic_Library/pots_control_status_core.htm)

[Connections and Callouts](javascript:void(0))

### Front Panel

1. OLED Display â Displays information about the Core's settings and status.
2. NEXT button â Cycles through the OLED information pages
3. ID button â Locates the Core in Q-SYS Designer GUI and Configurator
4. POWER LED â Illuminates blue when the Core is on
5. USB Ports â USB Type A Host connectors (2)

### Rear Panel

1. Eight Audio I/O Card Bays â Accept Q-SYS Type 2 Audio I/O Cards (supports up to 128x128 local audio channels)
2. GPIO A and GPIO B â Female DA-15 connectors for Q-SYS control I/O
3. RS232 â Male DE-9 serial communications interface
4. HDMI â Video Output
5. AC Mains â IEC 60320 C14 receptacle
6. AUX LAN â RJ45: Data, VoIP, WAN streaming, management Auxiliary Ports â USB Type A Host Ports
7. LAN A â RJ45: Q-LAN, AES67, Audio, VoIP, management Auxiliary Ports â USB Type A Host Ports
8. LAN B â RJ45: Q-LAN, AES67, Audio, VoIP, management

[OLED Screens](javascript:void(0))

### Design Status

* Device â The name of the Core as defined in Q-SYS Designer.
* Design â The name of the currently running design.
* Status â Indicates health of Core in design:
  + OK â Audio, Video and Control (AVC) engine is good.
  + Compromised â AVC engine is good, but a redundancy mechanism is active (one LAN down but the other is still up) or a non-fatal hardware problem exists (fans too slow, temperature higher than expected, etc.)
  + Fault â AVC engine is stopped, or hardware is malfunctioning or mis-configured
  + Missing â A piece of hardware, defined in the design, has not been discovered. AVC engine is not communicating with that piece of hardware.
  + Initializing â Starting the firmware, configuration update, or design update.
  + Not Present â A virtual component in the design, that is designated as Dynamically Paired, and Not Required, has no hardware assigned to it.

### System Status

* Firmware â A three-section number identifying the major release, minor release, and maintenance release. For example, 6.0.0.
* Temp â The current chassis temperature of the Core.
* Fan Speed â This number varies with the temperature.

### LAN A

* Static or Auto â Displays next to LAN A, indicates if the Core's IP Address is Static or Automatic.
* IP Address â The IP Address assigned to the Core's LAN A. LAN A is the primary Q-LAN connection to the Core, and is required.
* Net Mask â The Net Mask assigned to the Core.
* Gateway â The Gateway assigned to the Core.

**Note:** You can edit this information in [Core Manager](../../Core_Manager/CoreManager_Overview.htm).

### LAN B

LAN B is used for redundancy or segregation of various data types on to different networks but is not required for device operation. The information is displayed in the same format as LAN A.

### LAN AUX

LAN AUX is used for remote monitoring, WAN and VOIP connectivity, and is not required. The information is displayed in the same format as LAN A.

### Slots A - H

There is a total of 8 slots that can accommodate any combination of Q-SYS I/O Cards that are Type 2 format. The status for these cards are shown on the front panel by pressing the NEXT button.

[Mic/Line In H.P. card Status (CIML4-HP)](javascript:void(0))

The Mic/Line In H.P. card status screen shows the Mute state, Signal presence, Clip indication and +48V state of each of the 4 input channels.

* Mute â Displays a "muted loudspeaker" when the channel is muted.
* Signal â Displays a solid circle when there is a signal present on the associated channel.
* Clip â Displays a solid circle under the channel having an output signal over driving the associated channel output.
* +48V - Displays a sold circle when phantom power is active on the associated channel.

[Mic/Line In Std. card Status (CIML4)](javascript:void(0))

The Mic/Line In Standard card status screen shows the Mute state, Signal presence, Clip indication and +48V state of each of the 4 input channels.

* Mute â Displays a "muted loudspeaker" when the channel is muted.
* Signal â Displays a solid circle when there is a signal present on the associated channel.
* Clip â Displays a solid circle under the channel having an output signal over driving the associated channel output.
* +48V - Displays a solid circle when phantom power is active on the associated channel.

[Line Out card Status (COL4)](javascript:void(0))

The Line Out card status screen shows the Mute state, Signal presence, and Clip status of each of the 4 output channels.

* Mute â Displays a "muted loudspeaker" when the channel is muted.
* Signal â Displays a solid circle when there is a signal present on the associated channel.
* Clip â Displays a solid circle under the channel having an output signal over driving the associated channel output.

[Dataport Out card Status (CODP4)](javascript:void(0))

The Dataport Out card status screen shows the Mute state, Signal presence, and connected amplifier status for both ports.

* Mute â Displays a "muted loudspeaker" when the channel is muted.
* Signal â Displays a solid circle when there is a signal present on the associated channel.
* Amp 1 â Displays the status of the connected amplifier.
* Amp 2 - Displays the status of the connected amplifier.

[AES3 card Status (CAES4)](javascript:void(0))

The AES3 card status screen shows the Mute state, Signal presence, and Lock state for 4 input and 4 output channels.

* Mute â Displays a "muted loudspeaker" when the channel is muted.
* Signal â Displays a solid circle when there is a signal present on the associated channel.
* Lock â Displays a solid circle when the AES3 clock is in sync and locked.

[16 channel AES3 In card Status (CIAES16)](javascript:void(0))

The AES3 16 channel card status screen shows the Signal presence, and Lock state for all 16 input channels.

* Signal â Displays a solid circle when there is a signal present on the associated channel.
* Lock â Displays a solid circle when the AES3 clock is in sync and locked for the associated channel.

[AVB card Status (CAN32)](javascript:void(0))

The AVB card status screen shows the Status of the card, Link state and speed of the network connection, and the MAC address of the card itself.

* Status â Displays the status of the AVB card.
* Link â Displays a solid circle when there is a valid connection with an AVB network or device and indicates the network connection speed in Mbps.
* MAC â Displays the MAC (Media Access Control) address of the AVB card.

[CobraNet card Status (CCN32)](javascript:void(0))

The CobraNet card status screen shows the Activity state, Fault state, In Use state and Conductor state of the Primary and Secondary network ports.

* Activity â Displays a solid circle when the Primary or Secondary port is active.
* Fault â Displays a solid circle under the channel having a communication fault while sending or receiving a bundle.
* In Use â Displays a solid circle when there is an active connection to a CobraNet network or device on the associated LAN port (primary or secondary.) The image shows that the secondary port is active.
* Conductor - Displays a solid circle when the Primary or Secondary port is the Conductor.

[Dante card Status (CDN64)](javascript:void(0))

The Dante card status screen shows the Status of the card, Link state and connection speed of the Primary and Secondary network ports, and the Name of the device as seen by other Dante devices on the network.

* Status â Displays the status of the Dante card.
* Link â Displays a solid circle when there is a valid connection with a Dante network or device. The image shows that the Primary port has established a link at 1000 Mbps.
* Name â Displays the name of the Dante device that will be seen by other connected Dante devices.

[GPIO](javascript:void(0))

### GPIO Pin Assignments

| DB15 Pin | Signal Name | Signal Type | Description |
| --- | --- | --- | --- |
| 1 | RNO | Relay Contact | Relay - normally open |
| 2 | RNC | Relay Contact | Relay - normally closed |
| 3 | GPIO 1 | GPIO Current | GPIO pin |
| 4 | GPIO 3 | GPIO Current | GPIO pin |
| 5 | POWER | Power | + 12V DC |
| 6 | GPIO 5 | High Current | GPIO pin -high current capable |
| 7 | GPIO 7 | High Current | GPIO pin -high current capable |
| 8 | GND | Ground | Ground |
| 9 | RC | Relay Contact | Relay - common |
| 10 | GND | Ground | Ground |
| 11 | GPIO 2 | GPIO Current | GPIO pin |
| 12 | GPIO 4 | GPIO Current | GPIO pin |
| 13 | POWER | Power | + 12V DC |
| 14 | GPIO 6 | High Current | GPIO pin -high current capable |
| 15 | GPIO 8 | High Current | GPIO pin -high current capable |

### GPIO Specifications

|  |  |
| --- | --- |
| Input Type | Range |
| Maximum Input Range | 0 V to 32 V |
| Analog Input Range | O V to 24 V |
| Digital Input: Low | 0 V to 0.8 V |
| Digital Input: High | O V to 2.0 V |
| Output Type |  |
| Digital Output: Low | 0 V to 0.4 V |
| Digital Output: High | 2.4 V to 3.3 V |
| Digital Output Impedance | 1K Ohm |
| High Current Output: Low | 0 V to 0.4 V |
| High Current Output: High | 11 V to 13 V |
| High Current Output: Sink or Source | 280 mA |
| Relay Input and Output | 0 V to 30 V; 1 Amp |

**Note:** The maximum current sourced by one GPIO connector (including both High Current and Power Pins) is 400mA.

### GPIO Examples

[Button or Contact Closure](javascript:void(0))

[Potentiometer](javascript:void(0))

[0-24 V Input, Low-Z](javascript:void(0))

[LED â Light â Motor, Q-SYS Powered](javascript:void(0))

[LED â Light â Motor, External Powered](javascript:void(0))

[Directional Motor Control](javascript:void(0))

[Rotary Encoder](javascript:void(0))

[Rotary Switch](javascript:void(0))

[Specifications](javascript:void(0))

Refer to the Specifications Sheet on the [Core 510i product page](https://www.qsys.com/products-solutions/q-sys/processing/core-510i/) at qsys.com.
