# NC-12x80, NC-20x60 PTZ Conference Cameras

> Source: https://help.qsys.com/Content/Hardware/Video/NC-PTZ.htm

# NC-12x80, NC-20x60 PTZ Conference Cameras

The Q-SYS NC Series PTZ conference cameras deliver high-quality video feeds natively to the Q-SYS Platform. The Q-SYS NC-12x80 and Q-SYS NC-20x60 both offer motorized pan, tilt, and zoom (PTZ) functionality to enable a more broad range of room layouts, sizes and purpose.

**Note:** This topic provides an overview of the NC-12x80 and NC-20x60 cameras. For related documentation, including installation instructions, see the [NC Series PTZ product page](https://www.qsys.com/products-solutions/q-sys/video/nc-series/nc-series-ptz-conference-cameras/) on the QSC website. For information about the NC-Pro15x camera, see [NC-Pro15x Network PTZ Camera](NC-Pro15x.htm).

[Features](javascript:void(0))

* NC-12x80: 12x optical zoom, 80Â° horizontal field of view
* NC-20x60: 20x optical zoom, 60Â° horizontal field of view
* Distribute video via the Q-LAN network anywhere it is needed
* Power over Ethernet (PoE)
* Complete camera imaging controls, including white balance, focus and exposure
* User-configurable resolution and quality for IP streams (up to 1080p), providing greater flexibility for a wide variety of use cases
* Image Rotation control to allow for inverted mounting (optional ceiling mount accessory is the PTZ-CMB1)
* Local 12 V connection for PTZ models (power supply not included)
* PTZ models include PTZ-WMB1 wall mount bracket for simple installation
* Comprehensive management via Q-SYS Designer Software and Q-SYS Reflect
* Auto-Framing, when enabled, tightly frames the faces found within the camera's actual field of view.

[Design Components](javascript:void(0))

The following components are available for the NC-12x80 and NC-20x60:

#### Standard Components

* [Status/Control (Cameras)](../../Schematic_Library/onvif_camera_operative.htm)

#### Related Components

* [USB Video Bridge](../../Schematic_Library/usb_uvc.htm)
* [Mediacast Router](../../Schematic_Library/video_router.htm)
* [VisionSuite (VisionSuite Designer)](../../Schematic_Library/vision_suite_designer.htm)

[Connections and Callouts](javascript:void(0))

### Front Panel â NC-12x80 and NC-20x60 PTZ

1. Status LED (Green)
   * Off indicates the camera is in standby mode; network streams are off.
   * On indicates the camera is streaming video over the network.
   * Blinking indicates the ID mode is on.
2. Power LED (Blue)
   * On indicates the camera has power applied.
   * Off indicates the camera has no power applied.

### Rear Panel â NC-12x80 and NC-20x60 PTZ

1. Product Label
   * Identifies product model: NC-12x80 or NC-20x60
   * Identifies the product serial number
   * Identifies the product MAC address
2. ID Button: Press to identify this product in Q-SYS Designer Software and Q-SYS Configurator. The green STATUS LED on the front panel blinks when in ID mode. Press again to turn off.
3. Factory Reset pin-hole: Use a paperclip or similarly sized object to insert. Press and hold the reset button for 5 seconds. This resets all parameters to the factory defaults.
4. Kensingtonâ¢ Lock Slot: for use with a security cable (not supplied).
5. DC 12 V: Connect an external power supply (not included). Supply must be rated at 12VDC 1A, EIAJ-04, center pin positive, outside barrel negative. Use only a class 2/LPS power supply.
6. LAN/PoE: RJ-45 connector for Q-SYS Gigabit Ethernet and Power over Ethernet. Cat5e cabling or better required.
7. 3G-SDI: 3G-SDI output via various video formats. Video formats can be changed via Q-SYS Designer Software or a Q-SYS User Control Interface (UCI). Maximum video format is 1080p60.
8. HDMI: HDMIÂ® 1.4b output via various video formats. Video formats can be changed via Q-SYS Designer Software or a Q-SYS UCI. Maximum video format is 4K30.

   **Note:** NC Series PTZ cameras support the usage of either HDMI or SDI, but not both simultaneously.

[Specifications](javascript:void(0))

Refer to the [NC Series PTZ Conference Cameras product page](https://www.qsys.com/products-solutions/q-sys/video/nc-series/nc-series-ptz-conference-cameras/) for product specifications.
