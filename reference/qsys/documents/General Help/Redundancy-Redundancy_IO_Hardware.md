# I/O Hardware Redundancy

> Source: https://help.qsys.com/Content/Redundancy/Redundancy_IO_Hardware.htm

# I/O Hardware Redundancy

Requirements for specific I/O hardware compatibility with a redundant configuration are listed below.

[QIO High Density Series: QIO-24f, QIO-ML24i, QIO-L24o](javascript:void(0))

A QIO High Density Series model can be made redundant with another device of the same model. Q-SYS offers a redundant cabling kit (QIO-CK) for this purpose. Information about wiring for redundancy can be found in the QIO High Density Series user manual at qsys.com.

**Note:** Only identical peripheral models can be a redundant pair. For example, you canât join a QIO-24f and a QIO-ML24i into a redundant pair.

If a condition is detected on an audio channel that requires a failover, the entire device (all audio channels) fails over to the backup device.

[AES-3 Digital Input/Output Card (CAES4)](javascript:void(0))

AES3 Outputs do not wire together - you must physically switch the output cabling on failover.

For hardware information, see [CAES4 â AES-3 Digital Input/Output Card](../Hardware/IO_Expanders/CAES4.htm).

[Analog Line Output Card (COL4)](javascript:void(0))

Wire the outputs in parallel with the corresponding card in the I/O Frame or Core.

For hardware information, see [COL4 â Analog Line Output Card](../Hardware/IO_Expanders/COL4.htm).

[Analog Telephony Card (CTEL4)](javascript:void(0))

CTEL4 card redundancy is not supported. (POTS technology does not support redundant connections.)

For hardware information, see [CTEL4 â Analog Telephony Card](../Hardware/IO_Expanders/CTEL4.htm).

[AVB Audio Video Bridge Card (CAN32)](javascript:void(0))

CAN32 card redundancy is not supported.

For hardware information, see [CAN32 â AVB Audio Video Bridge Card](../Hardware/IO_Expanders/CAN32.htm).

[CobraNet Digital Input/Output Card (CCN32)](javascript:void(0))

A CobraNet card installed in a Q-SYS Core which is in standby is not automatically suppressed from transmitting and receiving. This might affect your ability to use a redundant pair of Cores populated with CobraNet cards.

For hardware information, see [CCN32 â CobraNet Digital Input/Output Card](../Hardware/IO_Expanders/CCN32.htm).

[Dante Audio Bridge Card (CDN64)](javascript:void(0))

See [Dante Audio](../Networking/Dante_Audio.htm) for Dante redundancy requirements.

[DataPort Output Card (CODP4)](javascript:void(0))

You must use the [DataPort Amplifier Backup](Redundancy_Amplifier.htm) panel and have redundant amplifiers. The DataPort card outputs cannot be wired in parallel.

For hardware information, see [CODP4 â DataPort Output Card](../Hardware/IO_Expanders/CODP4.htm).

[Mic/Line Analog Input Card (CIML4, CIML4-HP)](javascript:void(0))

Wire the inputs in parallel with the corresponding card in the redundant I/O Frame or Core, for both active circuitry devices requiring phantom power and devices not requiring phantom power such as dynamic microphones.

**Note:** When phantom power is used, the active circuitry device gets the average of both Mic/Line In card's phantom power, which is +48 VDC. When a failover occurs, the device again gets the average of both Mic/Line In card's phantom power (+48 VDC and 0 VDC) + 24 VDC which should be enough to operate the device.

For hardware information, see:

* [CIML4 â Mic/Line Analog Input Card](../Hardware/IO_Expanders/CIML4.htm)
* [CIML4-HP â High Performance Mic/Line Analog Input Card](../Hardware/IO_Expanders/CIML4-HP.htm)
