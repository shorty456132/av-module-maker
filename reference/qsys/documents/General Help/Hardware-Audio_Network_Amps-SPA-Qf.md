# SPA-Qf Series Network Amplifiers

> Source: https://help.qsys.com/Content/Hardware/Audio_Network_Amps/SPA-Qf.htm

# SPA-Qf Series Network Amplifiers

The Q-SYS SPA-Qf Series expands and delivers rightsized amplification to a wide variety of space-types. With available GPIO for control, two flex channels (either mic/line inputs or line outputs), and 60 W per channel, the Q-SYS SPA-Qf 60x2 (two channel) and Q-SYS SPA-Qf 60x4 (four channel) provide the utility to centralize your processorâs connectivity across more spaces, all within a trusted native Q-SYS network amplifier.

**Note:** This topic provides an overview of the SPA-Qf Series. For specifications and installation documentation, see the [SPA-Qf Series product page](https://www.qsys.com/products-solutions/q-sys/audio-network-amplifiers/spa-q-series/) on the Q-SYS website.

[Features](javascript:void(0))

* Two or four output channel models at 60 W per channel
* Two on-board software-definable flex channels (as mic/line inputs with 48V phantom power, or as line level outputs)
* Four bi-directional GPIO connections
* Discrete half-rack, 1RU footprint and included mounting hardware
* Network operability enables close proximity installation to connected loudspeakers and other in-room endpoints

[Design Components](javascript:void(0))

Add an SPA-Qf amplifier model to your design inventory from the Amplifiers - Q-LAN category. The following components are available for the SPA-Qf Series:

* [Status (SPA-Qf Series)](../../Schematic_Library/spaq_status.htm)
* [Flex In (SPA-Qf Series)](../../Schematic_Library/io_card_flex_in_spaq.htm)
* [Flex Out (SPA-Qf Series)](../../Schematic_Library/io_card_flex_out_spaq.htm)
* [Amp Output (SPA-Qf Series)](../../Schematic_Library/spaq_amplifier.htm)
* [GPIO (SPA-Qf Series)](../../Schematic_Library/spaq_4ch_gpio.htm)

[Connections and Callouts](javascript:void(0))

[SPA-Qf 60x2](javascript:void(0))

### Front Panel

1. ID Button â Press to identify this product in Q-SYS Designer Software. (All front panel LEDs will flash.)
2. Limiter / Protect LEDs â The channel limiter is activated on input or output (orange) or in protect mode (red). Protect Mode can be caused by shorts, open circuits, and over-temperature conditions.
3. Input Signal LEDs â A signal exceeding -50 dBFS is present for the channel (blue). If the amplifier is in Bridge or Parallel mode, only the odd channel LED will illuminate.
4. Power LED â The amplifier is on and operational (solid blue) or in standby (slow flashing blue; all amplifier channels are in standby).
5. Fault LED â The amplifier is unable to pass audio or is malfunctioning or not properly configured (fast flashing orange). This could be caused by broken audio streams, amplifier fault, or loudspeaker short circuit. Refer to the [Status (SPA-Qf Series)](../../Schematic_Library/spaq_status.htm) component topic for fault details.

### Rear Panel

1. Output Channels A and B â For connection to loudspeakers. Uses the 4-position green Euro connector.
2. GPIO â Pins 1-4 are user-configurable and bi-directional; one 3.3V 100mA power pin; one ground pin. Uses the 6-position black Euro connector.
3. Flex Channels 1 and 2 â User-configurable audio channels (mic/line input with optional phantom power or line output), balanced or unbalanced. Each channel uses the 2-position blue Euro connector.
4. Reset Button â Use the Reset button to restore default network settings and clear the amplifier's password and log file. Before attempting a reset, see the [Device Reset](#Device) section.
5. LAN â RJ45, 1 Gigabit connection to Q-LAN network.
6. AC Power â 100-240V~ 50/60 Hz

[SPA-Qf 60x4](javascript:void(0))

### Front Panel

1. ID Button â Press to identify this product in Q-SYS Designer Software. (All front panel LEDs will flash.)
2. Limiter / Protect LEDs â The channel limiter is activated on input or output (orange) or in protect mode (red). Protect Mode can be caused by shorts, open circuits, and over-temperature conditions.
3. Input Signal LEDs â A signal exceeding -50 dBFS is present for the channel (blue). If the amplifier is in Bridge or Parallel mode, only the odd channel LED will illuminate.
4. Power LED â The amplifier is on and operational (solid blue) or in standby (slow flashing blue; all amplifier channels are in standby).
5. Fault LED â The amplifier is unable to pass audio or is malfunctioning or not properly configured (fast flashing orange). This could be caused by broken audio streams, amplifier fault, or loudspeaker short circuit. Refer to the [Status (SPA-Qf Series)](../../Schematic_Library/spaq_status.htm) component topic for fault details.

### Rear Panel

1. Output Channels A and B â For connection to loudspeakers. Uses the 4-position green Euro connector.
2. Output Channels C and D â For connection to loudspeakers. Uses the 4-position green Euro connector.
3. GPIO â Pins 1-4 are user-configurable and bi-directional; one 3.3V 100mA power pin; one ground pin. Uses the 6-position black Euro connector.
4. Flex Channels 1 and 2 â User-configurable audio channels (mic/line input with optional phantom power or line output), balanced or unbalanced. Each channel uses the 2-position blue Euro connector.
5. Reset Button â Use the Reset button to restore default network settings and clear the amplifier's password and log file. Before attempting a reset, see the [Device Reset](#Device) section.
6. LAN â RJ45, 1 Gigabit connection to Q-LAN network.
7. AC Power â 100-240V~ 50/60 Hz

[Specifications and Dimensions](javascript:void(0))

Product specifications and dimension drawings for SPA-Qf Series amplifiers can be found on the [SPA-Qf Series product page](https://www.qsys.com/products-solutions/q-sys/audio-network-amplifiers/spa-q-series/) on the Q-SYS website.

[Device Reset](javascript:void(0))

**CAUTION:** This procedure resets the SPA-Qf network settings to Auto, resets the amplifier's host name to default, and deletes its password and log file.

1. Insert a paper clip or similar tool into the Rear Panel > Reset Button pinhole.
2. Press and hold for 5 seconds.
3. Press the Front Panel > ID Button to confirm and reset the amplifier.
