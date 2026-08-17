# QIO-S4

> Source: https://help.qsys.com/Content/Hardware/IO_Expanders/QIO-S4.htm

# QIO-S4

The Q-SYS QIO-S4 is a network control endpoint native to the Q-SYS Ecosystem, serving as an IP-to-serial bridge that enables network-based control distribution. The compact form factor includes surface mounting hardware permitting discreet and strategic mounting while an optional rack kit fits one to four devices into a standard 1U nineteen-inch format. Up to four devices may be daisy-chained off one access switch port, provided +24 VDC power is available. Alternatively, each may be individually powered over Ethernet.

**Note:** This topic provides an overview of the QIO-S4. For specifications and installation documentation, see the [QIO-S4 product page](https://www.qsys.com/products-solutions/q-sys/control-io-controllers/qio-series/qio-s4/) on the QSC website.

[Features](javascript:void(0))

* Native control I/O expander for Q-SYS
* Four (4) bi-directional RS232 serial ports
* One port includes RS422 and RS485 compatibility
* Power-over-Ethernet capable
* Daisy-chain up to four QIO network I/O expanders on a single network run (with local daisy-chained DC power)
* Simple drag-and-drop integration and comprehensive management via Q-SYS Designer Software and Q-SYS Reflect
* Surface- or rack-mountable
* Includes surface mounting hardware
* QIO-RMK rack mounting kit sold separately
* QIO-PSU DC power supply sold separately

[Design Components](javascript:void(0))

These Inventory components are available for the QIO-S4:

* [Status (NL Series, NM Series, QIO Series)](../../Schematic_Library/lcqln_status.htm)
* [Serial Port (QIO Series)](../../Schematic_Library/lcqln_serial_port.htm)

[Connections and Callouts](javascript:void(0))

### Front Panel

1. Power LED â Illuminates blue when the Q-SYS QIO-S4 is powered on.
2. ID LED â LED blinks green when placed into ID Mode via ID Button or Q-SYS Configurator.
3. ID Button âLocates the QIO-S4 in Q-SYS Designer Software and Q-SYS Configurator.

### Rear Panel

1. External Power Input 24V DC 2.5 A â Auxiliary power, 24 VDC, 2.5 A, 2-pin Euro connector.
2. Daisy-Chain Power Output 24V DC 2.5 A - Auxiliary power, 24 VDC, 2.5 A 2-pin Euro connector.
3. LAN [PoE] â RJ-45 connector, 802.3af PoE Type 1 Class 1 power, Q-LAN.
4. LAN [THRU] â RJ-45 connector, Ethernet daisy-chaining.
5. Device Reset â Use a paperclip or similar tool to restore default network settings and recover factory default settings. Before attempting a reset, refer to the [Device Reset](#Device) section.
6. COM 1 Serial Port â Configurable in Q-SYS Designer Software for RS232, RS485 Half-Duplex TX, RS485 Half-Duplex RX, or RS485/422 Full Duplex. See [QIO-S4 Serial Port Pinouts](#QIO-S4).
7. COM 2, COM 3, COM 4 Serial Ports â Dedicated to RS232 communication. See [QIO-S4 Serial Port Pinouts](#QIO-S4).

[QIO-S4 Serial Port Pinouts](javascript:void(0))

The QIO-S4 features four serial ports:

* COM 1 is configurable in the QIO-S4 Serial Port 1 inventory component Properties for RS232, RS485 Half Duplex TX, RS485 Half Duplex RX, or RS485/422 Full Duplex.
* COM 2-4 ports are dedicated to RS232 communication.

### RS232 Pinout: COM 1 (Configurable), COM 2-4 (Dedicated)

| Pin | Signal Flow | Description |
| --- | --- | --- |
|  | N/A | Signal ground |
| TX | Output | Transmit data |
| RX | Input | Receive data |
| RTS | Output | Ready to Send[1](#When) |
| CTS | Input | Clear to Send[1](#When) |

###### 1. When using hardware flow control.

### RS485 Half Duplex TX or RX Pinout: COM 1 (Configurable)

| Pin | Signal Flow | Description |
| --- | --- | --- |
|  | N/A | Signal ground |
| TX | Input/Output | Differential B- |
| RX | (Unused) | (Unused) |
| RTS | Input/Output | Differential A+ |
| CTS | (Unused) | (Unused) |

### RS485/422 Full Duplex: COM 1 (Configurable)

| Pin | Signal Flow | Description |
| --- | --- | --- |
|  | N/A | Signal ground |
| TX | Output | Differential Z- / Tx- |
| RX | Input | Differential A+ / Rx+ |
| RTS | Output | Differential Y+ / Tx+ |
| CTS | Input | Differential B- / Rx- |

[Specifications and Dimensions](javascript:void(0))

Product specifications and dimension drawings for the QIO-S4 can be found on the [QIO-S4 product page](https://www.qsys.com/products-solutions/q-sys/control-io-controllers/qio-series/qio-s4/).

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
