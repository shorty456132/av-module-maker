# USB Endpoints

> Source: https://help.qsys.com/Content/Schematic_Library/usb_endpoints.htm

# USB Endpoints

The topic provides a comprehensive overview of various devices and their maximum allowed USB endpoints, detailing both input and output counts.

[Q-SYS Devices that Support USB Endpoints](javascript:void(0))

* [NV-32-H (Core Capable) Network Video Endpoint](../Hardware/Video/NV-32-H_Core_Capable.htm)
* [I/O-USB Bridge](../Hardware/IO_Expanders/IOUSB_Bridge.htm)
* [Core Nano](../Hardware/Processing/Core_Nano.htm)
* [Core 110f](../Hardware/Processing/Core_110f.htm)
* [TSC-50-G3](../Hardware/Control_IO/TSC-50-G3.htm)
* [TSC-70-G3](../Hardware/Control_IO/TSC-70-G3.htm)
* [TSC-101-G3](../Hardware/Control_IO/TSC-101-G3.htm)
* [Core 8 Flex](../Hardware/Processing/Core_8_Flex.htm)
* [NV-21-HU Network Video Endpoint](../Hardware/Video/NV-21-HU.htm)

[USB Endpoint Input and Output Counts](javascript:void(0))

* USB Video Bridging = 2 inputs
* HID Conferencing = 1 input and 1 output
* HID Keyboard = 1 input and 1 output
* HID Media = 1 input and 1 output

  **Note:** When adding HID media or keyboard functionality, the USB endpoint input count will not increase if USB output is already in the design.
* USB EC Speakerphone 1 In = 1 input
* USB Sound Card 2 In = 1 Input
* USB In = 1 Input
* USB Output - counted as 2 inputs and 2 outputs

[Allowed Inputs and Outputs per Device](javascript:void(0))

This table represents the max allowed USB Endpoints of the following devices that support USB Endpoints.

| Device | Mode[1](#1.Mode) | Allowed Inputs | Allowed Outputs |
| --- | --- | --- | --- |
| [NV-32-H (Core Capable) Network Video Endpoint](../Hardware/Video/NV-32-H_Core_Capable.htm) | Core Mode | 9 | 7 |
| Peripheral Mode | 9 | 7 |
| Encoder / Decoder | 9 | 7 |
| [I/O-USB Bridge](../Hardware/IO_Expanders/IOUSB_Bridge.htm) |  | 8 | 5 |
| [Core Nano](../Hardware/Processing/Core_Nano.htm) | Core Mode | 8 | 5 |
| Peripheral Mode | 8 | 5 |
| [Core 110f](../Hardware/Processing/Core_110f.htm) | Core Mode | 10 | 7 |
| Peripheral Mode | 10 | 7 |
| [TSC-50-G3](../Hardware/Control_IO/TSC-50-G3.htm)  [TSC-70-G3](../Hardware/Control_IO/TSC-70-G3.htm)  [TSC-101-G3](../Hardware/Control_IO/TSC-101-G3.htm) |  | 5 | 4 |
| [Core 8 Flex](../Hardware/Processing/Core_8_Flex.htm) | Core Mode | 9 | 6 |
| Peripheral Mode | 7 | 6 |
| [NV-21-HU Network Video Endpoint](../Hardware/Video/NV-21-HU.htm) | Encoder / Decoder | 5 | 5 |

###### 1. Mode is only applicable for those Cores that can switch between Core and Peripheral Mode or Encoder / Decoders.
