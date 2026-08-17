# NL-C4

> Source: https://help.qsys.com/Content/Hardware/Audio_Network_Loudspeakers/NL-C4.htm

# NL-C4

The Q-SYS NL-C4 is a network PoE loudspeaker that delivers clear speech and music reproduction natively to Q-SYS. The ceiling-mount loudspeaker features a four-inch, full-range driver, and can be integrated into your space with a single Ethernet cable to reduce overall hardware footprint and lower system cost. As a native Q-SYS Product, you can take advantage of the drag-and-drop integration and simple control capabilities offered by Q-SYS.

**Note:** This topic provides an overview of the NL-C4. For specifications and installation documentation, see the [NL-C4 product page](https://www.qsys.com/products-solutions/q-sys/audio-network-loudspeakers/nl-series/nl-c4/) on the QSC website.

[Features](javascript:void(0))

* 4-inch, full-range driver
* Power over Ethernet enables power, data and control over a single cable
* Consistent tonal characteristics across the entire NL Series family let you mix and match enclosure types within a single space
* Ideal for speech and music applications
* Simple drag-and-drop integration and comprehensive management via Q-SYS Designer Software and Q-SYS Reflect
* Q-SYS automatically delivers custom loudspeaker voicings (Intrinsic Correctionâ¢) to simplify the tuning process
* Snap-fit magnetic grille
* Blemish-free removable logo
* Removable conduit cover plate, also available as accessory for pre-install wiring
* Available in white (RAL 9010)

[Design Components](javascript:void(0))

These Inventory components are available for the NL-C4:

* [Status (NL Series, NM Series, QIO Series)](../../Schematic_Library/lcqln_status.htm)
* [Loudspeaker Output (NL Series)](../../Schematic_Library/lcqln_loudspeaker_output.htm)

**Note:** Refer to your [Q-SYS Core processor](../Hardware_Overview.htm#Q-SYS_Cores) "Features" section for the max number of supported Q-SYS peripherals, including NL Series, in a design.

[Connections and Callouts](javascript:void(0))

### Side

1. LAN/PoE: RJ-45 connector for Q-SYS Gigabit Ethernet and Power over Ethernet (PoE). Cat5e cabling or better required. PoE+ Type 2 Class 4 capable.

### Bottom (Under Grille)

1. Status LED: Indicates the current device status:

   * Flashes yellow when the ID button is pressed in Q-SYS Designer Software (QDS)
   * Flashes blue (slow blink) when the loudspeaker is initializing
   * Flashes red (slow blink) when a fault is detected. Refer to the Status component in QDS for details.
2. ID Button: Press to identify this product in QDS. The Status LED blinks when in ID mode. Press again to turn off.
3. Reset Button: Use the Reset button to restore default network settings and recover factory default settings. Before attempting a reset, refer to the [Device Reset](#Device) section.

[Specifications and Dimensions](javascript:void(0))

Product specifications and dimension drawings for the NL-C4 can be found on the [NL-C4 product page](https://www.qsys.com/products-solutions/q-sys/audio-network-loudspeakers/nl-series/nl-c4/).

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
