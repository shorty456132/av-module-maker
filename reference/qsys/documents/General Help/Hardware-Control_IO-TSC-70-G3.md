# TSC-70-G3

> Source: https://help.qsys.com/Content/Hardware/Control_IO/TSC-70-G3.htm

# TSC-70-G3

The Q-SYS TSC Series Gen 3 are high-performance network touch screen controllers native to Q-SYS. The TSC-70-G3 is a 7-inch, PoE-capable (power over Ethernet) device that supports a wide range of fully-customizable user control interface applications for any space.

**Note:** This topic provides an overview of the TSC-70-G3. For specifications and installation documentation, see the [TSC-70-G3 product page](https://www.qsys.com/products-solutions/q-sys/control-io-controllers/q-sys-touch-screen-controllers/tsc-70-g3/) on the QSC website.

[Features](javascript:void(0))

* High performance 7-inch network touch screen controller native to the Q-SYS Platform
* Enhanced onboard processor with increased resolution and significantly improved screen transitions on all models
* Customizable RGB LED status indicators
* Integrated proximity sensor wakes the screen on approach while an ambient light sensor adjusts screen brightness
* Build intuitive and scalable UCIs in the same software program as your DSP and control programming for a streamlined design and deployment process
* Supports CSS-based styling letting users build more dynamic UCI themes and apply global styles across multiple UCIs
* [UCI Controller](../../Schematic_Library/device_controller_proxy.htm)  is an alternative method of building UCIs from a template of control types to simplify deployment and scalability of multiple UCIs
* Supports Power over Ethernet to allow for power and data on a single cable for simple, single cable installation
* Supports landscape or portrait orientation when wall-mounted
* Optional table top mount accessory available
* Universal mounting options: Included accessories for mounting to US standard and European wall and junction boxes

[Q-SYS Design Components](javascript:void(0))

These Inventory components are available for the TSC-70-G3:

#### Standard Components

* [Status/Control (Touch Screen)](../../Schematic_Library/touch_screen_status.htm)
* [Lightbar (TSC-G3, PS-TSCG3 Series)](../../Schematic_Library/lightbar.htm)
* [Sensors](../../Schematic_Library/touchscreen_sensors.htm)
* [HID Keyboard](../../Schematic_Library/usb_keyboard.htm)
* [HID Media](../../Schematic_Library/usb_ccontrols.htm)
* [HID Conferencing](../../Schematic_Library/usb_telephony.htm)

#### USB Video Bridge

* [USB Video Bridge](../../Schematic_Library/usb_uvc.htm)

#### USB Audio Bridge

* [USB Audio Bridge â Speakerphone / Sound Card In](../../Schematic_Library/usb_receiver.htm)
* [USB Audio Bridge â Speakerphone / Sound Card Out](../../Schematic_Library/usb_transmitter.htm)

[TSC-G3 Q-SYS AV Bridging](javascript:void(0))

Q-SYS AV Bridging is a new licensed feature paradigm to the Q-SYS ecosystem. This new type of feature license allows flexibility in pricing and deployment by allowing Q-SYS to price the TSC-G3 competitively without the price of USB bridging baked in. If you donât need bridging, you donât need to pay for the license. If you do need bridging, you can pay for the license for each bridging device required.

To learn more about feature licensing in Q-SYS, see [Licensing](../../Core_Manager/Core_Management/Licensing.htm).

**Note:** By default, USB 2.0 connections are not supported for TSC Series Gen 3 USB video bridging. There are two possible orientations for the TSC side of a USB-C cable and currently only one orientation is supported for USB 3.0 connections. The supported orientation for USB 3.0 depends on the type of USB cable and/or adapter used. The simplest method to quickly determine the correct USB cable orientation is to deploy a video bridging design with USB 2.0 disabled (set the TSCâs USB 2.0 Support property to âDisabledâ) then connect a USB 3.0 capable Host device to the TSC through the USB 3.0 cable and/or adapter that will be used. If the TSC status indicates it is âCompromisedâ, flip the cable connection at the TSC connector. Once the TSC is not in a Compromised state, USB 2.0 can be re-enabled (set the TSCâs USB 2.0 Support property to âEnabledâ). For more information, see the [USB Video Bridge](../../Schematic_Library/usb_uvc.htm) topic.

**Tip:** For most USB-C cables, orientation 1 is seen while the cable is connected with the logo side facing the RJ45 connection. QSC recommends using a USB-C to USB-A cable for most host PCs. USB-C only hosts should then use a common USB-C to USB-A adapter.

### Supported TSC-G3 Series Models

Q-SYS AV Bridging applies to the TSC-70-G3 and the TSC-101-G3. You will see new USB Video Bridge and USB Audio Bridge Inventory items for both touch screen controller models.

### Licensing Requirements

Adding any of these components to the schematic will trigger a Q-SYS AV Bridging license requirement:

* 2ch Sound Card Input/Output
* 1ch Speakerphone Input/Output
* USB Video Bridge
* HID Conferencing

[Connections and Callouts](javascript:void(0))

### Front Panel

1. Proximity sensor. Refer to the [Sensors](../../Schematic_Library/touchscreen_sensors.htm) topic.
2. Ambient light sensor. Refer to the [Sensors](../../Schematic_Library/touchscreen_sensors.htm) topic.
3. NFC antenna. Refer to the [Sensors](../../Schematic_Library/touchscreen_sensors.htm) topic.
4. 7 in. 1280 x 800 display

### Rear Panel

1. Docking magnet
2. RJ45, PoE/+ in
3. LAN LEDs
   * Left: Link/Activity
   * Right: Speed
4. USB Type C

**Note:** By default, USB 2.0 connections are not supported for TSC Series Gen 3 USB video bridging. There are two possible orientations for the TSC side of a USB-C cable and currently only one orientation is supported for USB 3.0 connections. The supported orientation for USB 3.0 depends on the type of USB cable and/or adapter used. The simplest method to quickly determine the correct USB cable orientation is to deploy a video bridging design with USB 2.0 disabled (set the TSCâs USB 2.0 Support property to âDisabledâ) then connect a USB 3.0 capable Host device to the TSC through the USB 3.0 cable and/or adapter that will be used. If the TSC status indicates it is âCompromisedâ, flip the cable connection at the TSC connector. Once the TSC is not in a Compromised state, USB 2.0 can be re-enabled (set the TSCâs USB 2.0 Support property to âEnabledâ). For more information, see the [USB Video Bridge](../../Schematic_Library/usb_uvc.htm) topic.

**Tip:** For most USB-C cables, orientation 1 is seen while the cable is connected with the logo side facing the RJ45 connection. QSC recommends using a USB-C to USB-A cable for most host PCs. USB-C only hosts should then use a common USB-C to USB-A adapter.

1. Exhaust vents

### Profile

1. Mounting point for wall-mount bracket
2. Regulatory markings
3. Model identification
4. Programmable RGB LEDs. Refer to the [Lightbar (TSC-G3, PS-TSCG3 Series)](../../Schematic_Library/lightbar.htm) topic.

[Specifications and Dimensions](javascript:void(0))

Product specifications and dimension drawings for the TSC-70-G3 can be found on the [TSC-70-G3 product page](https://www.qsys.com/products-solutions/q-sys/control-touchwall-controllers/q-sys-touch-screen-controllers/tsc-70-g3/) on the QSC website.
