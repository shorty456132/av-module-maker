# CCN32 â CobraNet Digital Input/Output Card

> Source: https://help.qsys.com/Content/Hardware/IO_Expanders/CCN32.htm

# CCN32 â CobraNet Digital Input/Output Card

The CCN32 card provides input/output interfacing with legacy CobraNet-based audio networks. In an I/O Frame, the CobraNet card can be used in 4x4, 8x8, and 16x16 mode, whereas inserting it into a Core allows all these as well as the additional 32x32 mode.

For configuration information, see [CobraNet In](../../Schematic_Library/io_cobranet_input_card.htm) and [CobraNet Out](../../Schematic_Library/io_cobranet_output_card.htm). For documents and other information, see the [I/O Cards product page](https://www.qsys.com/products-solutions/q-sys/audio-io-peripherals/io-cards/).

[About Type 2 Hardware](javascript:void(0))

The CCN32 card is Type 2 hardware.

Type 2 hardware provides new cables and connectors between the I/O cards and main boards in Cores and I/O Frames. Due to this change, the Type 2 hardware is not physically compatible with the older hardware. You can still integrate the new I/O Frames and Cores in the same system with older hardware, but the I/O cards are not interchangeable. Type 2 hardware can be identified by a yellow label on the back of the Core and I/O Frame, and the bottom of the I/O cards.

[Specifications](javascript:void(0))

| CCN32 Card | |
| --- | --- |
| Description | Up to 32 input and 32 output channels of CobraNet digital audio |
| Performance |  |
| Dynamic Range A-weighted | > 140 dB |
| Frequency Response 20 Hz - 20 kHz | Â± 0.2 dB |
| THD+N | -130 dB (typ) |
| Group Delay | Selectable: |
|  | modeRate = 0x400: 1.479 mS (2.812 mS w/SRC enabled) |
|  | modeRate = 0x500: 2.813 mS (4.146 mS w/SRC enabled) |
|  | modeRate = 0x600: 5.479 mS(6.812 mS w/SRC enabled) |
| I/O Capacity | Selectable: |
|  | 4 x 4 |
|  | 8 x 8 |
|  | 16 x 16 |
|  | 32 x 32 (Core only) |
| Bundle Packing | 0 to 8 channels |
| CobraNet Network Transmitters | 16 |
| CobraNet Network Receivers | 16 |
| Configuration Management | Simple Network Management Protocol v1 |
| Mute | Infinite attenuation (via digital mute) |
| Connectors | Two female RJ-45 connectors |
