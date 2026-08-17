# QIO-FLEX4A

> Source: https://help.qsys.com/Content/Hardware/IO_Expanders/QIO-FLEX4A.htm

# QIO-FLEX4A

The QIO-FLEX4A is an all-in-one network I/O peripheral for presentation, discussion, and connected collaboration spaces.

**Note:** This topic provides an overview of the QIO-FLEX4A. For specifications and installation documentation, see the [FLEX4A product page](https://www.qsys.com/products/q-sys/control-io-controllers/qio-series/qio-flex4a/).

[Features](javascript:void(0))

The Q-SYS QIO Series network audio I/O expanders include these features:

* Native audio I/O expanders for Q-SYS
* QIO-ML4i: Four (4) mic/line inputs
* QIO-L4o: Four (4) line outputs
* QIO-ML2x2: Two (2) mic/line inputs and two (2) line outputs
* QIO-AES8x8: Four (4) AES3 Inputs and four (4) AES3 Outputs
* QIO-TEL2: Two (2) PSTN (POTS) interfaces
* QIO-FLEX4A: Four (4) Flex I/O Audio Channels, 4x8 GPIO Ports, two (2) Amplifier Outputs, one (1) RS232.
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
* [Flex In (QIO Series)](../../Schematic_Library/lcqln_flex_in.htm)
* [Flex Out (QIO Series)](../../Schematic_Library/lcqln_flex_out.htm)
* [GPIO In (QIO Devices)](../../Schematic_Library/lcqln_gpio_in.htm)
* [GPIO Out (QIO Series)](../../Schematic_Library/lcqln_gpio_out.htm)
* [Serial Port (QIO Series)](../../Schematic_Library/lcqln_serial_port.htm)
* [Amp Out (QIO-FLEX4A)](../../Schematic_Library/lcqln_amp_out.htm)

[Connections and Callouts](javascript:void(0))

### Front Panel

1. Power LED â Illuminates blue when the Q-SYS QIO-FLEX4A is powered on.
2. ID LED â LED blinks green when placed into ID Mode via ID Button or Q-SYS Configurator.
3. ID Button â Locates the QIO-FLEX4A in Q-SYS Designer Software and Q-SYS Configurator.

### Rear Panel

1. External Power Input 24V DC 3.7 A â Auxiliary power, 24V DC, 3.7 A, 2-pin Euro connector.
2. Daisy-Chain Power Output 24V DC 1.9 A â Auxiliary power, 24V DC, 1.9 A 2-pin Euro connector.
3. LAN [PoE] â RJ-45 connector, 802.3at Type 2 power, Q-LAN.
4. LAN [THRU] â RJ-45 connector, Ethernet daisy-chaining.
5. Device Reset â Use a paperclip or similar tool to restore default network settings and recover factory default settings. Before attempting a reset, refer to the Q-SYS Help for details.
6. RS232 â COM: TX pin (output, transmit data), RX pin (input, receive data), Ground pin (signal ground), WT pin (5.5V DC 70 mA max).
7. AMP Out â 2 channels, 5W per channel (PoE+) or 9W per channel (Aux power).
8. Signal Ground â For use with General Purpose Inputs and Outputs (GPIO). Uses connector pin 14 (not numbered).
9. GPIO Outputs â 8 outputs, open collector (24V, 0.2A sink maximum) with pull up to +3.3V (pins labeled 1â8 equal pins 1â8 in the Q-SYS Designer GPIO Output component).
10. GPIO Inputs â 4 inputs, 0-24V analog input, digital input, or contact closure (pins labeled 1â4 equal pins 1â4 in the Q-SYS Designer GPIO Input component). Configurable pull-up to +12V.
11. 12V DC .1A Out â For use with GPIO. Uses connector pin 1 (not numbered).
12. FLEX Channels â 4 user-configurable audio channels (mic/line input with optional phantom power, or line output), balanced or unbalanced.

[Specifications and Dimensions](javascript:void(0))

Product specifications and dimension drawings can be found on the [QIO-FLEX4A product page](https://www.qsys.com/products/q-sys/control-io-controllers/qio-series/qio-flex4a/).

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
