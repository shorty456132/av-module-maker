# QIO-IR1x4

> Source: https://help.qsys.com/Content/Hardware/IO_Expanders/QIO-IR1x4.htm

# QIO-IR1x4

The Q-SYS QIO-IR1x4 is a network control endpoint native to the Q-SYS Ecosystem, serving as an IP-to-IR bridge that enables network-based infrared control distribution. The compact form factor includes surface mounting hardware permitting discreet and strategic mounting while an optional rack kit fits one to four devices into a standard 1U nineteen-inch format. Up to four devices may be daisy-chained off one access switch port, provided +24 VDC power is available. Alternatively, each may be individually powered over Ethernet.

**Note:** This topic provides an overview of the QIO-IR1x4. For specifications and installation documentation, see the [QIO-IR1x4 product page](https://www.qsys.com/products-solutions/q-sys/control-io-controllers/qio-series/qio-ir1x4/) on the QSC website.

[Features](javascript:void(0))

* Native control I/O expander for Q-SYS
* First native IR connectivity solution for Q-SYS
* One (1) IR receiver input and four (4) IR emitter outputs
* Power-over-Ethernet capable
* Daisy-chain up to four QIO network I/O expanders on a single network run (with local daisy-chained DC power)
* Simple drag-and-drop integration and comprehensive management via Q-SYS Designer Software and Q-SYS Reflect
* Surface- or rack-mountable
* Includes surface mounting hardware
* QIO-RMK rack mounting kit sold separately
* QIO-PSU DC power supply sold separately

[Design Components](javascript:void(0))

#### Inventory Components

These components are available from the Inventory tree once you have added a QIO-IR1x4:

* [Status (NL Series, NM Series, QIO Series)](../../Schematic_Library/lcqln_status.htm)
* [IR Input (QIO-IR1x4)](../../Schematic_Library/lcqln_ir_input.htm)
* [IR Output (QIO-IR1x4)](../../Schematic_Library/lcqln_ir_output.htm)

#### Control Components

These related components are available from the Schematic Elements > Control Components category:

* [IR Driver](../../Schematic_Library/ir_driver.htm)
* [IR Receiver](../../Schematic_Library/ir_receiver.htm)

[Connections and Callouts](javascript:void(0))

### Front Panel

1. Power LED â Illuminates blue when the Q-SYS QIO-IR1x4 is powered on.
2. ID LED â LED blinks green when placed into ID Mode via ID Button or Q-SYS Configurator.
3. ID Button âLocates the QIO-IR1x4 in Q-SYS Designer Software and Q-SYS Configurator.

### Rear Panel

1. External Power Input 24V DC 2.5 A â Auxiliary power, 24 VDC, 2.5 A, 2-pin Euro connector.
2. Daisy-Chain Power Output 24V DC 2.5 A â Auxiliary power, 24 VDC, 2.5 A 2-pin Euro connector.
3. LAN [PoE] â RJ-45 connector, 802.3af PoE Type 1 Class 1 power, Q-LAN.
4. LAN [THRU] â RJ-45 connector, Ethernet daisy-chaining.
5. Device Reset â Use a paperclip or similar tool to restore default network settings and recover factory default settings. Before attempting a reset, refer to the [Device Reset](#Device) section.
6. IR SIG LEDS â Indicate transmit activity for CH/IR Output 1-4.
7. IR Outputs â Configurable in Q-SYS Designer Software as IR or Serial RS232. See the [IR Port Pinouts](#IR) section.
8. IR Input â Provides 3.3VDC and receives IR data. See the [IR Port Pinouts](#IR) section.

[IR Port Pinouts](javascript:void(0))

The QIO-IR1x4 features four IR outputs and one IR input:

* Outputs 1-4 are configurable in Q-SYS Designer Software for IR or Serial RS232 mode.
* Input provides 3.3VDC and receives IR data.

### IR Output 1-4: IR Mode Pinout

| Pin | Signal Flow | Description |
| --- | --- | --- |
| SIG | Output | IR transmit data |
|  | N/A | Signal reference |

### IR Output 1-4: Serial RS232 Mode Pinout

| Pin | Signal Flow | Description |
| --- | --- | --- |
| SIG | Output | RS232 transmit data |
|  | N/A | Signal reference |

### IR Input Pinout

| Pin | Signal Flow | Description |
| --- | --- | --- |
| SIG | Input | IR receive data |
|  | Output | 3.3VDC |
|  | N/A | Signal reference |

[Specifications and Dimensions](javascript:void(0))

Product specifications and dimension drawings for the QIO-IR1x4 can be found on the [QIO-IR1x4 product page](https://www.qsys.com/products-solutions/q-sys/control-io-controllers/qio-series/qio-ir1x4/).

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
