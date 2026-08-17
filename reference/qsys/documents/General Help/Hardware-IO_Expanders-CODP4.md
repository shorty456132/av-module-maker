# CODP4 â DataPort Output Card

> Source: https://help.qsys.com/Content/Hardware/IO_Expanders/CODP4.htm

# CODP4 â DataPort Output Card

The CODP4 card provides four audio output channels (2 DataPort connectors) for connection to DataPort equipped QSC amplifiers. The DataPort interface allows audio, status monitoring, and control between Q-SYS and QSC DataPort power amplifiers.

For configuration information, see [DataPort Out](../../Schematic_Library/io_card_dataport.htm). For documents and other information, see the [I/O Cards product page](https://www.qsys.com/products-solutions/q-sys/audio-io-peripherals/io-cards/).

[About Type 2 Hardware](javascript:void(0))

The CODP4 card is Type 2 hardware.

Type 2 hardware provides new cables and connectors between the I/O cards and main boards in Cores and I/O Frames. Due to this change, the Type 2 hardware is not physically compatible with the older hardware. You can still integrate the new I/O Frames and Cores in the same system with older hardware, but the I/O cards are not interchangeable. Type 2 hardware can be identified by a yellow label on the back of the Core and I/O Frame, and the bottom of the I/O cards.

[Connections](javascript:void(0))

* A DataPort card has two female DE-15 connectors with two channels per connector. This means you can connect two 2-channel amplifiers or one 4-channel amp to a single DataPort card. You can also connect two DataPort cards (total of eight channels) to the Q-SYS [DataPort Amplifier Backup Panel (DAB-801)](../Accessories/017_DataPort_Amplifier_Backup_Panel.htm).
* The DataPort card should be installed only by authorized personnel.
* The DataPort card will not pass full-scale audio when there is not a valid amplifier connected to it.
* A QSC DataPort Cable is required for connection from the DataPort card to the DataPort amplifier. These appear to be common VGA cables but they are not. Many off-the-shelf VGA cables MIGHT work with satisfactory results, however it is also quite possible off-the-shelf cables will give less-than-satisfactory results, and could even cause damage to QSC DataPort amplifiers! The QSC DataPort specification requires that all conductors be present, as well as shielding over those conductor pairs used for the audio channels to the amplifier. Therefore, QSC recommends the use of QSC DataPort cables exclusively, which are available in a variety of lengths from QSC. Use of any non-QSC DataPort cable may void the warranty.
* When a DataPort card is used in a redundant Core or I/O Frame, you must use the DataPort Amplifier Backup Panel, and have redundant amplifiers. You can not wire the DataPort card outputs in parallel.

**Note:** DataPorts on multi-port amplifiers must be wired to DataPorts on the same I/O Frame or Core. You cannot wire some of the amplifier's DataPorts to a Core and others, on the same amplifier, to an I/O Frame. You cannot wire some of the amplifier's DataPorts to one I/O Frame and others, on the same amplifier, to another I/O Frame.

[Specifications](javascript:void(0))

| CODP4 Card | | |
| --- | --- | --- |
| Dynamic range | un-weighted | > 114 dB |
| A-weighted | > 117 dB |
|  | | |
| Distortion  (20Hz - 20 kHz) | +4 dBu (max) | â |
| 2 dB below clip (max) | < 0.04% THD+N |
|  | | |
| Crosstalk  (20 Hz - 20 kHz) | Inter-channel (max) | > 95 dB |
| Inter-channel (typ) | > 100 dB |
| Intra-channel (max) | > 100 dB |
| Intra-channel (typ) | > 110 dB |
|  | | |
| Frequency Response | 20Hz - 20 kHz (max) | Â± 0.5 dB |
| 20Hz - 20kHz (typ) | Â± 0.2 dB |
|  | | |
| Input Impedance | Balanced (nominal) | â |
| Unbalanced (nominal) | â |
|  | | |
| Common Mode Rejection | 20Hz - 20kHz (Min) | â |
| 20Hz - 20kHz (Typ) | â |
|  | | |
| Input Sensitivities | Vrms | â |
| dBu | â |
| dBv | â |
|  | | |
| Mute | Electro-mechanical relays | Infinite Attenuation |
|  | | |
| Audio Converters Group Delay (at 48 kHz) | Analog to Digital Conversion (ADCs) | â |
| Digital to Analog Conversion (DACs) | 24-bit delta-sigma at 48 or 96 kHz sample rate |
| Output | 0.25 ms |
|  | | |
| Connectors |  | Two DE-15 (female 15-pin high-density D shell) connectors |
|  | | |
| User-configurable Options (software enabled) | Phantom Power | â |
| Input Sensitivity | â |
| Output Trim  Vrms (max)  dBu (max)  dBv (max) | â  â  â |
| Amplifier Standby | Set or clear amplifier in standby mode |
| Mute | Set or clear individual channel mutes |
| Enable Meters | Enable data collection of meters for each channel |
| Audio Output Levels | Adjust individual audio channel levels |
|  | | |
| Amplifier Model Support |  | CX, PowerLightâ¢ 3 Series, DCA, and legacy V1 models |
