# CTEL4 â Analog Telephony Card

> Source: https://help.qsys.com/Content/Hardware/IO_Expanders/CTEL4.htm

# CTEL4 â Analog Telephony Card

The CTEL4 card provides four RJ-11 interfaces to connect the Q-SYS Core or I/O Frame to analog telephony (POTS) environments.

For configuration information, see [POTS Controller](../../Schematic_Library/pots_control_status.htm), [POTS In](../../Schematic_Library/io_card_pots_input_for_core.htm), and [POTS Out](../../Schematic_Library/io_card_pots_output_for_core.htm). For documents and other information, see the [I/O Cards product page](https://www.qsys.com/products-solutions/q-sys/audio-io-peripherals/io-cards/).

#### Product Identification Numbers

US: 6M2BR01ACTEL4

IC: 20383-CTEL4

[About Type 2 Hardware](javascript:void(0))

The CTEL4 card is Type 2 hardware.

Type 2 hardware provides new cables and connectors between the I/O cards and main boards in Cores and I/O Frames. Due to this change, the Type 2 hardware is not physically compatible with the older hardware. You can still integrate the new I/O Frames and Cores in the same system with older hardware, but the I/O cards are not interchangeable. Type 2 hardware can be identified by a yellow label on the back of the Core and I/O Frame, and the bottom of the I/O cards.

[Installation Limitations](javascript:void(0))

Due to electrical current limitations imposed on telephony devices, there is a limit to the number of CTEL4 cards that can be installed in Q-SYS host hardware.

| Host Hardware | Available I/O Slots | Max CTEL4 Cards Allowed |
| --- | --- | --- |
| Q-SYS Core 510 Series | 8 | 3 |

**Note:** The CTEL4 card limits do not affect other Q-SYS I/O cards. All other Q-SYS I/O cards (in any combination) may be installed into a host product alongside the supported CTEL4 maximums.

[POTS Specifications](javascript:void(0))

The POTS Controller component controls the features of the Q-SYS interface with a Plain Old Telephone Service (POTS).

If you are connecting to an analog phone system, you can connect from the wall RJ-11 jack directly to Q-SYS hardware supporting a POTS connection:

* The [Core 110f](../Processing/Core_110f.htm) and [Core 110c](../Processing/Core_110c.htm) provide a single RJ-11 telephone connection.
* The [CTEL4 â Analog Telephony Card](#) provides four RJ-11 telephone connections.

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
