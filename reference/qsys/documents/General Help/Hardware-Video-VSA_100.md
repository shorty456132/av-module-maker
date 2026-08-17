# VisionSuite VSA-100 AI Accelerator

> Source: https://help.qsys.com/Content/Hardware/Video/VSA_100.htm

# VisionSuite VSA-100 AI Accelerator

The VSA-100 is a dedicated Q-SYS peripheral crafted to serve as an AI accelerator for VisionSuite applications. To
utilize this device, a VisionSuite software license is necessary - see [Licensing](../../Core_Manager/Core_Management/Licensing.htm). When paired with VisionSuite software, the VSA-100
unlocks features including presenter tracking, AI-driven room awareness, and the capability to automatically capture
the active speaker in the room, regardless of their seating position.

**Note:** The VSA-100 AI Accelerator requires Q-SYS Designer Software (QDS) for configuration and operation. Visit [Q-SYS Compatibility](../../Q-SYS_Compatibility/Q-SYS_Compatibility_Overview.htm) for QDS version compatibility information.

[Features](javascript:void(0))

* Speaker Spotlight technology: The active speakerâs voice drives camera framing without the need for presets, while voice activity detection protects against false audio triggers.
* Presenter Spotlight technology: Advanced computer vision drives full-body presenter tracking.
* Computer vision models analyze full-body characteristics to create unique digital identifiers, enabling full room automations.
* Integrates with Q-SYS using an Ethernet connection and without affecting the video signal chain.
* Design, configure, calibrate, and commission all through VisionSuite Designer software, an easy-to-use, native tool within Q-SYS Designer.
* Supported by Q-SYS NC Series network PTZ cameras

  + Presentation Space Tracking: NC-12x80 / NC-20x60
  + Conductor Camera: NC-12x80 / NC-20x60 / NC-110
  + Static View: Any Q-SYS Camera (Does not require a channel of analytics)
* 1 RU form factor

[Design Components](javascript:void(0))

Add the VSA-100 to your design Inventory from the Video category. The following components are related to the VSA-100:

* [Status (VisionSuite Accelerator)](../../Schematic_Library/vision_suite_accelerator_status.htm)
* [VisionSuite (VisionSuite Designer)](../../Schematic_Library/vision_suite_designer.htm)

[Connections and Callouts](javascript:void(0))

### Front Panel

1. **Power light**: lights up blue when the unit is powered on.
2. **Front-panel display**: displays pertinent information about the core, such as its network configuration, the system it is running, active faults, etc.
3. **Navigation buttons (up, down, left, right)**: allows the user to navigate through the menus on the front-panel display:
   1. Both the up and right buttons advance to the next menu item.
   2. Both the down and left buttons go back to the previous menu item.
4. **ID/Select button**: press the center button to put the Core into ID mode for identification within Q-SYS Designer Software. Press again to turn off ID mode.

### Rear Panel

1. **DisplayPorts**: not supported.
2. **HDMI port**: not supported.
3. **USB A and USB C ports**: not supported.
4. **Serial communications RS232 (male DB-9)**:not supported.
5. **Q-SYS LAN ports (RJ45)**: from left to right; top row is LAN A and LAN B, bottom row is LAN C and LAN D. (Only LAN A is supported.)
6. **Power supply unit (PSU)**.

[Specifications](javascript:void(0))

For complete product specs, refer to the Specifications Sheet on the [VisionSuite](https://www.qsys.com/products/q-sys/video/q-sys-visionsuite/) product page at qsys.com.
