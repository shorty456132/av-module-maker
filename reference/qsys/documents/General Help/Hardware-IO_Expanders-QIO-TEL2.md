# QIO-TEL2

> Source: https://help.qsys.com/Content/Hardware/IO_Expanders/QIO-TEL2.htm

# QIO-TEL2

The Q-SYS QIO-TEL2 is a network audio endpoint native to the Q-SYS Ecosystem, serving as a POTS FXO device, that enables network-based audio distribution. The compact form factor includes surface mounting hardware permitting discreet and strategic mounting while an optional rack kit fits one to four devices into a standard 1U nineteen-inch format. Two POTS interfaces provide the right amount of connectivity in desired locations without bulk or waste. Up to four devices may be daisy-chained off one access switch port, provided +24 VDC power is available. Alternatively, each may be individually powered over Ethernet.

**Note:** This topic provides an overview of the QIO-TEL2. For specifications and installation documentation, see the [QIO Series Network Audio Expanders product page](https://www.qsys.com/products-solutions/q-sys/audio-io-peripherals/qio/) on the QSC website.

[Features](javascript:void(0))

The Q-SYS QIO Series network audio I/O expanders include these features:

* Native audio I/O expanders for Q-SYS
* QIO-ML4i: Four (4) mic/line inputs
* QIO-L4o: Four (4) line outputs
* QIO-ML2x2: Two (2) mic/line inputs and two (2) line outputs
* QIO-AES8x8: Four (4) AES3 Inputs and four (4) AES3 Outputs
* QIO-TEL2: Two (2) PSTN (POTS) interfaces
* Professional mic/line level inputs with +48 VDC phantom power and/or line outputs
* Microphone detection on inputs enables monitoring, usage statistics, and failure notifications
* Power-over-Ethernet capable
* Daisy-chain up to four QIO network I/O expanders on a single network run (with local daisy-chained DC power)
* Simple drag-and-drop integration and comprehensive management via Q-SYS Designer Software and Q-SYS Reflect
* Surface- or rack-mountable
* Includes surface mounting hardware
* QIO-RMK rack mounting kit sold separately
* QIO-PSU DC power supply sold separately

[Design Components](javascript:void(0))

These Inventory components are available for the QIO-TEL2:

* [Status (NL Series, NM Series, QIO Series)](../../Schematic_Library/lcqln_status.htm)
* [POTS In](../../Schematic_Library/io_card_pots_input_for_core.htm)
* [POTS Out](../../Schematic_Library/io_card_pots_output_for_core.htm)
* [POTS Controller](../../Schematic_Library/pots_control_status.htm)

[Connections and Callouts](javascript:void(0))

### Front Panel

1. Power LED â Illuminates blue when the Q-SYS QIO-TEL2 is powered on.
2. ID LED â LED blinks green when placed into ID Mode via ID Button or Q-SYS Configurator.
3. ID Button â Locates the QIO-TEL2 in Q-SYS Designer Software and Q-SYS Configurator.

### Rear Panel

1. External Power Input 24V DC 2.5 A â Auxiliary power, 24 VDC, 2.5 A, 2-pin Euro connector.
2. Daisy-Chain Power Output 24V DC 2.5 A - Auxiliary power, 24 VDC, 2.5 A 2-pin Euro connector.
3. LAN [PoE] â RJ-45 connector, 802.3af Type 1 Class 1 power, Q-LAN.
4. LAN [THRU] â RJ-45 connector, Ethernet daisy-chaining.
5. Device Reset â Use a paperclip or similar tool to restore default network settings and recover factory default settings. Before attempting a reset, refer to the [Device Reset](#Device) section for details.
6. POTS Lines â Two FXO interfaces. Note: Each Q-SYS phone line is meant to be connected to a single PTSN line (FXO). It does not control a multi-line PBX or interface with an FXS.

[Specifications and Dimensions](javascript:void(0))

Product specifications and dimension drawings for the QIO-TEL2 can be found on the [QIO Series Network Audio Expanders product page](https://www.qsys.com/products-solutions/q-sys/audio-io-peripherals/qio/).

[Device Reset](javascript:void(0))

You can perform either a short reset or long reset:

* Use a Short Reset to restore connectivity to a device in the event that unintended network settings were specified in Q-SYS Peripheral Manager or the device is otherwise unreachable. A short reset will restore device IP settings back to Auto mode (DHCP) and delete all Static Routes. The configured hostname is retained.
* Use a Long Reset to restore the device to factory condition. This is useful for deeper troubleshooting, or when preparing the device for decommissioning or transfer.

  **CAUTION:** A Long Reset clears all network settings (including hostname), disables 802.1x, deletes user-installed device certificates, deletes all logs, and clears the device password.

### Performing a Short Reset

1. Press and hold the Reset Button until the Status LED (NL, NM Series) or Power LED (QIO Series) begins flashing blue slowly â approximately 10 seconds.
2. Release the button before 20 seconds elapse.
3. The device performs its prescribed Short Reset and reboots.

**Note:** To cancel the Short Reset, release the button before 10 seconds has elapsed.

### Performing a Long Reset

1. Press and hold the Reset Button until the Status LED (NL, NM Series) or Power LED (QIO Series) begins flashing blue rapidly â approximately 20 seconds.
2. Release the button when the LED begins flashing rapidly.
3. Within 30 seconds, press the Reset Button again to confirm the reset.
4. The device performs its prescribed Long Reset and reboots.

**Note:** To cancel the Long Reset, do not press the Reset Button again during the 30 second confirmation period.
