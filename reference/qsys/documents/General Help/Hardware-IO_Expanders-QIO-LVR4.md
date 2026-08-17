# QIO-LVR4

> Source: https://help.qsys.com/Content/Hardware/IO_Expanders/QIO-LVR4.htm

# QIO-LVR4

The Q-SYS QIO-LVR4 expands your Q-SYS systemâs capabilities to enable streamlined interoperability with non-networked control devices via low-voltage relay connectivity. By separating local I/O from processing hardware, the QIO Series offer modular and easily scalable network I/O to support your desired topology.

[Features](javascript:void(0))

* Native network low-voltage relay connectivity solution for Q-SYS
* Four (4) dry contact closure relay circuits with Normally Open (NO), Common (C), and Normally Closed (NC) connections
* Power-over-Ethernet (PoE) capable
* Daisy-chain up to four QIO expanders on a single network run (with local daisy-chained DC power)
* Simple drag-and-drop integration and comprehensive management via Q-SYS Designer Software and Q-SYS Reflect
* Surface- or rack-mountable (1RU, quarter-width)
* Includes surface mounting hardware
* QIO-RMK rack mounting kit sold separately
* QIO-PSU DC power supply sold separately

[Design Components](javascript:void(0))

#### Inventory Components

These components are available from the Inventory tree once you have added a QIO-LVR4:

* [Status (NL Series, NM Series, QIO Series)](../../Schematic_Library/lcqln_status.htm)
* [Relay Output (QIO-LVR4)](../../Schematic_Library/lcqln_relay_out.htm)

[Connections and Callouts](javascript:void(0))

### Front Panel

1. Power LED â Illuminates blue when the Q-SYS QIO-LVR4 is powered on.
2. ID LED â LED blinks green when placed into ID Mode via ID Button or Q-SYS Configurator.
3. ID Button âLocates the QIO-LVR4 in Q-SYS Designer Software and Q-SYS Configurator.

### Rear Panel

1. External Power Input 24V DC 2.5 A â Auxiliary power, 24 VDC, 2.5 A, 2-pin Euro connector.
2. Daisy-Chain Power Output 24V DC 2.5 A â Auxiliary power, 24 VDC, 2.5 A 2-pin Euro connector.
3. LAN [PoE] â RJ-45 connector, 802.3af PoE Type 1 Class 1 power, Q-LAN.
4. LAN [THRU] â RJ-45 connector, Ethernet daisy-chaining.
5. Device Reset â Use a paperclip or similar tool to restore default network settings and recover factory default settings. Before attempting a reset, refer to the [Device Reset](#DeviceReset) section.
6. Relay Outputs â Four relay circuits, 12-pin Euro connector: Normally Open (NO), Common (C), and Normally Closed (NC).

[Specifications and Dimensions](javascript:void(0)) 

Product specifications and dimension drawings for the QIO-LVR4 can be found on the [QIO-LVR4 Control I/O Expander](https://www.qsys.com/products-solutions/q-sys/control-io-controllers/qio-series/) product page.

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
