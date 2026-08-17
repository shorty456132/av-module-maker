# QIO-GP8x8

> Source: https://help.qsys.com/Content/Hardware/IO_Expanders/QIO-GP8x8.htm

# QIO-GP8x8

The Q-SYS QIO-GP8x8 is a network control endpoint native to the Q-SYS Ecosystem, providing General Purpose Input/Output (GPIO) connections that allow the Q-SYS network to interface with miscellaneous outside devices, such as LED indicators, switches, relays, and potentiometers, and with custom or third-party controls. The compact form factor includes surface mounting hardware permitting discreet and strategic mounting while an optional rack kit fits one to four devices into a standard 1U nineteen-inch format. Up to four devices may be daisy-chained off one access switch port, provided 24 VDC power is available. Alternatively, each may be individually powered over Ethernet.

**Note:** This topic provides an overview of the QIO-GP8x8. For specifications and installation documentation, see the [QIO-GP8x8 product page](https://www.qsys.com/products-solutions/q-sys/control-io-controllers/qio-series/qio-gp8x8/) on the QSC website.

[Features](javascript:void(0))

* Native control I/O expander for Q-SYS
* Eight (8) logic inputs and eight (8) logic outputs
* Power-over-Ethernet capable
* Daisy-chain up to four QIO network I/O expanders on a single network run (with local daisy-chained DC power)
* Simple drag-and-drop integration and comprehensive management via Q-SYS Designer Software and Q-SYS Reflect
* Surface- or rack-mountable
* Includes surface mounting hardware
* QIO-RMK rack mounting kit sold separately
* QIO-PSU DC power supply sold separately

[Design Components](javascript:void(0))

These Inventory components are available for the QIO-GP8x8:

* [Status (NL Series, NM Series, QIO Series)](../../Schematic_Library/lcqln_status.htm)
* [GPIO In (QIO Devices)](../../Schematic_Library/lcqln_gpio_in.htm)
* [GPIO Out (QIO Series)](../../Schematic_Library/lcqln_gpio_out.htm)

[Connections and Callouts](javascript:void(0))

### Front Panel

1. Power LED â Illuminates blue when the Q-SYS GP8x8 is powered on
2. ID LED â LED blinks green when placed into ID Mode via ID Button or Q-SYS Designer Software
3. ID Button â Locates the GP8x8 in Q-SYS Designer Software.

### Rear Panel

1. External Power Input 24V DC 2.5 A â Auxiliary power, 24 VDC, 2.5 A, 2-pin Euro connector.
2. Daisy-Chain Power Output 24V DC 2.5 A â Auxiliary power, 24 VDC, 2.5 A 2-pin Euro connector.
3. LAN [PoE] â RJ-45 connector, PoE Type 1 Class 3, Q-LAN.
4. LAN [THRU] â RJ-45 connector, Ethernet daisy-chaining.
5. Device Reset â Use a paperclip or similar tool to restore default network settings and recover factory default settings. Before attempting a reset, refer to the [Device Reset](#Device) section for details.
6. 12V DC .1A Out â For use with General Purpose Inputs and Outputs (GPIO). Uses black connector pins 1 and 11 (not numbered).
7. GPIO Inputs â 8 inputs, 0-24V analog input, digital input, or contact closure (Pins labeled 1â8 equal pins 1â8 in the Q-SYS Designer Software [GPIO In (QIO Devices)](../../Schematic_Library/lcqln_gpio_in.htm) component). Configurable pull-up to +12V.
8. Signal Ground â For use with GPIO. Uses black connector pins 10 and 20 (not numbered).
9. GPIO Outputs â 8 outputs, open collector (24V, 0.2A sink maximum) with pull-up to +3.3V (Pins labeled 1â8 equal pins 1â8 in the Q-SYS Designer Software [GPIO Out (QIO Series)](../../Schematic_Library/lcqln_gpio_out.htm) component).

[Specifications and Dimensions](javascript:void(0))

Product specifications and dimension drawings for the QIO-GP8x8 can be found on the [QIO-GP8x8 product page](https://www.qsys.com/products-solutions/q-sys/control-io-controllers/qio-series/qio-gp8x8/).

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
