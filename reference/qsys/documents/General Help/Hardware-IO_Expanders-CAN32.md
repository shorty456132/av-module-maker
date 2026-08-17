# CAN32 â AVB Audio Video Bridge Card

> Source: https://help.qsys.com/Content/Hardware/IO_Expanders/CAN32.htm

# CAN32 â AVB Audio Video Bridge Card

The CAN32 card provides a digital bridge between any 100mb AVB 1722.1 compliant edge network and the Q-SYS Eco system. The CAN32 will support 32 total channels at 48 kHz in three available operating modes: 0/32, 32/0 or 16x16.

For configuration information, see [Status (AVB)](../../Schematic_Library/io_avb_card_status.htm), [AVB In](../../Schematic_Library/io_avb_input_card.htm), and [AVB Out](../../Schematic_Library/io_avb_output_card.htm). For documents and other information, see the [I/O Cards product page](https://www.qsys.com/products-solutions/q-sys/audio-io-peripherals/io-cards/).

[About Type 2 Hardware](javascript:void(0))

The CAN32 card is Type 2 hardware.

Type 2 hardware provides new cables and connectors between the I/O cards and main boards in Cores and I/O Frames. Due to this change, the Type 2 hardware is not physically compatible with the older hardware. You can still integrate the new I/O Frames and Cores in the same system with older hardware, but the I/O cards are not interchangeable. Type 2 hardware can be identified by a yellow label on the back of the Core and I/O Frame, and the bottom of the I/O cards.

[Specifications](javascript:void(0))

| CAN32 Card | |
| --- | --- |
| Description | AVB network audio input and output card |
| Maximum audio channel capacity: | 0x32, 32x0 or 16x16 channels |
| Also configurable as | 8x8, 4x4 and 2x2 |
| Stream configurations limited by AVB, from <https://abc.statusbar.com/:>  Network Speed:  AVB BW Allocation:  Stream format:  Sample rate:  Bits/Sample:  AAF Samples/Frame: | 100 baseT  90% [1](#Most_switches)  AM824 (non-blocking)  48 kHz  24  default |
| Card I/O |  |
| Sample Rate | 48 kHz only |
| SRC (Sample Rate Converter) | Between AVB and Q-SYS (always)  There is an SRC on the inputs and outputs, with a delay of 2 ms each. |
| Configurable AVB clock | Internally generated (not related to Q-SYS clock)  Recovered clock from one of the AVB input streams |
| Network data rate: 100 Mbps |  |
| Indicators  Yellow      Green | "SPEED" LED indicates connection to 100 Mbps link partner (network switch or end point) when illuminated    "LINK/ACT" LED indicates network link established when illuminated solid and indicates network transmit and/or receive activity when blinking |
| Connectors | Two female RJ-45 connectors |
|  |  |
| --- | --- |
| 1. Most switches will be set to 75% by default to allow for other traffic.) | |

[Card I/O](javascript:void(0))

| Card I/O | Valid Streams / Channels |
| --- | --- |
| 2x2 | 1 / 2  2 / 1 |
| 4x4 | 1 / 4  2 / 2  4 / 1 |
| 8x8 | 1 / 8  2 / 4  4 / 2  8 / 1 |
| 16x16 | 1 / 16  2 / 8  4 / 4  8 / 2  14 / 1 |
| 32x0 or 0x32 | 1 / 32  2 / 16  4 / 8  8 / 4  12 / 2 |

[Connect an AVB Listener to an AVB Talker](javascript:void(0))

* AVDECC (aka 1722.1) (see https://avb.statusbar.com/article/1722.1-features/): This is what is normally done, and it involves some third-party software. We've been using Riedel AVB Manager, but there are others such as Pivitec's AVDECC Controller
* "Directly" via "Full Stream ID": Each AVB stream on the network has a unique 64-bit stream ID (Full Stream ID). Rather than using AVDECC software that discovers what AVB devices are out on the net, if you know the Full Stream ID you can just tell your Listener to listen to that stream and bypass AVDECC (and related third-party software)

[Configure the AVB I/O Card](javascript:void(0))

The Q-SYS CAN32 AVB I/O Card is user configurable via Q-SYS Designer version 4.2.x or greater, including ability to make Direct connections via Full Stream ID (no AVDECC in Q-SYS)

Configurable via third-party software applications supporting the AVDECC control protocol as defined in IEEE 1722.1

[IEEE 1722.1 AVDECC Descriptors](javascript:void(0))

The Q-SYS CAN32 AVB I/O Card supports the following IEEE 1722.1 AVDECC descriptors:

* ENTITY
* CONFIGURATION
* AUDIO\_UNIT
* STREAM\_INPUT
* STREAM\_OUTPUT
* JACK\_INPUT
* JACK\_OUTPUT
* AVB\_INTERFACE
* CLOCK\_SOURCE
* LOCALE
* STRINGS
* STREAM\_PORT\_INPUT
* STREAM\_PORT\_OUTPUT
* AUDIO CLUSTER
* AUDIO\_MAP
* CLOCK\_DOMAIN
* EXTERNAL\_PORT\_INPUT
* EXTERNAL\_PORT\_OUTPUT

[IEEE 1722.1 AVDECC commands](javascript:void(0))

The Q-SYS CAN32 AVB I/O Card supports the following IEEE 1722.1 AVDECC commands:

* GET\_NAME
* SET\_NAME
* ACQUIRE\_ENTITY
* LOCK\_ENTITY
* START\_STREAMING
* STOP\_STREAMING
* AVDECC = Audio Video Discovery, Enumeration, Connection management and Control (aka 1722.1)
