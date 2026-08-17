# HID Media

> Source: https://help.qsys.com/Content/Schematic_Library/usb_ccontrols.htm

# HID Media

Use the HID Media component to control media application playback, including volume level, on a remote PC or Mac computer connected to a Q-SYS device that supports the HID Media component.

[Q-SYS Device Support](javascript:void(0))

HID Keyboard, HID Media, and HID Conferencing are inventory components included with these Q-SYS devices:

* [Core Nano](../Hardware/Processing/Core_Nano.htm)
* [Core 8 Flex](../Hardware/Processing/Core_8_Flex.htm)
* [Core 24f](../Hardware/Processing/Core_24f.htm)
* [Core 110f](../Hardware/Processing/Core_110f.htm) and [Core 110c](../Hardware/Processing/Core_110c.htm)
* [NV-21-HU Network Video Endpoint](../Hardware/Video/NV-21-HU.htm)
* [NV-32-H (Core Capable) Network Video Endpoint](../Hardware/Video/NV-32-H_Core_Capable.htm)
* [I/O-USB Bridge](../Hardware/IO_Expanders/IOUSB_Bridge.htm)
* [TSC-70-G3](../Hardware/Control_IO/TSC-70-G3.htm)
* [TSC-101-G3](../Hardware/Control_IO/TSC-101-G3.htm)

[Requirements](javascript:void(0))

* You need a USB A/B cable to connect a PC or Mac computer to the Q-SYS device.
* HID Media is designed to control a remote computer â connected to a Q-SYS device supporting the HID Media component â from another Q-LAN-connected device, such as a computer or touch screen controller. Do not use the component directly from the computer connected to the Q-SYS device, as unexpected behavior can occur.

[Configuration Overview](javascript:void(0))

1. Connect the USB A/B cable's rectangular 'A' connector to a USB port on a PC or Mac computer.
2. Connect the other end of the cable, the square 'B' connector, to the **USB B** port on the rear panel of the Q-SYS Core 110f processor.
3. On another PC connected to the Q-SYS network, drag the HID Media component into your schematic from the Core 110f inventory tree.
4. Press F5 to save your design to the Core and run it.
5. Double-click the component to open the control panel. Use the buttons to remotely control playback within a Core-connected computer media application.

**Note:** The Core-connected computer's OS determines which media application is controlled.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

The HID Media component includes standard media control functions:

|  |  |
| --- | --- |
|  | Scan Previous Key |
|  | Play Pause Key |
|  | Scan Next Key |
|  | Volume Mute Key |
|  | Volume Down Key |
|  | Volume Up Key |
|  | Eject Key |

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Connected LED | 0  1 | disabled  enabled | 0  1 | Output |
| Eject Key | 0  1 | false  true | 0  1 | Input / Output |
| Play Pause Key | 0  1 | false  true | 0  1 | Input / Output |
| Scan Next Key | 0  1 | false  true | 0  1 | Input / Output |
| Scan Previous Key | 0  1 | false  true | 0  1 | Input / Output |
| Volume Down Key | 0  1 | false  true | 0  1 | Input / Output |
| Volume Mute Key | 0  1 | false  true | 0  1 | Input / Output |
| Volume Up Key | 0  1 | false  true | 0  1 | Input / Output |
