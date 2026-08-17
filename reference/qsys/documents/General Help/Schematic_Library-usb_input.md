# USB Input

> Source: https://help.qsys.com/Content/Schematic_Library/usb_input.htm

# USB Input

Use the USB Input component to see information for [HID Human Interface Device Class](javascript:void(0)) devices connected to the USB-A ports on a supported Q-SYS Core processor or peripheral and to route HID signals to either the [USB Router](usb_router.htm) component or directly to the [USB Output](usb_output.htm) component of another Q-SYS Core processor or peripheral.

[Supported Q-SYS Hardware, HID Devices, and Connections](javascript:void(0))

These Q-SYS devices support the ability to connect and route USB HID device signals.

| Q-SYS Core or Peripheral | USB-A Ports | USB-B Ports | USB-C Ports |
| --- | --- | --- | --- |
| [Core Nano](../Hardware/Processing/Core_Nano.htm)[1](#The) | 4 | 1 | 1 |
| [Core 8 Flex](../Hardware/Processing/Core_8_Flex.htm)[1](#The) | 4 | 1 | 1 |
| [Core 110f](../Hardware/Processing/Core_110f.htm)[1](#The) and [Core 110c](../Hardware/Processing/Core_110c.htm) | 6[2](#On) | 1 | N/A |
| [NV-32-H (Core Capable) Network Video Endpoint](../Hardware/Video/NV-32-H_Core_Capable.htm) | 4 | 1 | N/A |
| [NV-21-HU Network Video Endpoint](../Hardware/Video/NV-21-HU.htm) | 1 | N/A | 1 |
| [Core 24f](../Hardware/Processing/Core_24f.htm) | 2 | N/A | 1 |
| [I/O-USB Bridge](../Hardware/IO_Expanders/IOUSB_Bridge.htm) | 3 | 1 | N/A |

###### 1. The USB Input and USB Output components are not supported in Peripheral Mode (I/O Mode) for these devices.

###### 2. On the Core 110f v2, the two front panel USB-A ports are not present. These correspond to Port 1 and Port 2 in the USB Input component and are not applicable to the Core 110f v2.

### Supported HID Devices

* QSC has tested and supports the direct connection of driverless USB HID devices. These include keyboards, mice, and "smart display" touch screen interfaces (single-touch support only) connected directly to the Q-SYS hardware without a USB hub.
* QSC has not tested and does not support connection and routing of other USB devices and signals, including USB hubs, faders, joysticks, music keyboards, UVC signals (such as webcams), USB storage (flash drives, external drives), and other non-HID USB signals. Keyboard custom/special keys are not supported.
* Supported Operating Systems: Our support is limited to Windows and macOS environments.

**Note:** The mouse function through USB HID routing is currently not supported on ChromeOS.

### USB Connections

* Connect USB HID devices to the Q-SYS Core or peripheral's USB-A and USB-C ports.
* Connect a USB host to either the USB-B or USB-C port.

**Note:** The USB-C port can connect to either a device or a host. However, only one host connection is supported at a time. If both the USB-C and USB-B ports are connected to hosts, the USB-B port takes priority â the USB-B port connects to a host while the USB-C port connects to a device.

[Routing USB Signals in Q-SYS](javascript:void(0))

In Q-SYS, you can route HID signals in addition to audio and video signals. A common application is extending a keyboard & mouse or touch screen to networked devices.

### Components

[USB Input](javascript:void(0))

[USB Input](#) is an Inventory component for supported Q-SYS hardware. It provides a visual representation of what is connected to the USB-A ports on the Q-SYS device. The information is provided by the connected USB HID device.

For example, here is a Q-SYS Core 110f processor with a keyboard and mouse connected to two of its six USB-A ports:

[USB Output](javascript:void(0))

[USB Output](usb_output.htm) is an Inventory component for supported Q-SYS hardware. It provides a visual representation of the USB-B or USB-C connector on a given device, and indicates any issues or missing connections between the Q-SYS device and the connected host. For example:

[USB Router](javascript:void(0))

USB Router is a Schematic Elements component (available from the Control Components category) that routes input signals from one or more peripherals to one or more destination peripherals.

**Note:** While you can route multiple inputs to a single output, you cannot route a single input to multiple outputs.

For example, here is a USB Router component configured to route USB HID signals from four NV-32-H devices:

* A keyboard and mouse (connected to NV-1) and a touch screen device (connected to NV-2) are routed to a PC connected to a Core 110f.
* A keyboard and mouse (connected to NV-3) and a touch screen device (connected to NV-4) are routed to a second PC connected to another NV-32-H (NV-5).

### Use Cases and Schematic Examples

[Remote PC Keyboard + Mouse (PC in the room)](javascript:void(0))

In this application, a user connects a keyboard and mouse to the NV-32-H Encoder at the table location. The HID signals from the keyboard and mouse are routed to the NV-32-H Decoder (via Q-SYS) and sent to the PC that is attached via USB. Hereâs what that looks like in the Q-SYS Design:

[Remote PC Keyboard + Mouse (PC in remote location)](javascript:void(0))

In this application, a user chooses to collocate the room PC in an [IDF Intermediate Distribution Frame](javascript:void(0)) with the AV equipment. The video signal for the PC connects to an NV-32-H Encoder to route back into the room (to be displayed on the monitor, via an NV-32-H Decoder). For USB routing, the Encoder or Core 110f could be used to deliver the remote (in-room) keyboard and mouse to the PC in the IDF location. Hereâs what that looks like in the Q-SYS Design:

**Note:** This design allows for either the Core 110f or rack Encoder to deliver the keyboard and mouse to the rack PC. Note, however, that the signal cannot be routed to both peripherals at the same time.

[Touch screen with Local PC](javascript:void(0))

In this application, the touch screen monitor, as well as the keyboard and mouse in the room, is able to route HID signals over the Q-LAN network to the room PC. The PC receives its USB connection from the room Decoder. Hereâs what it looks like in Q-SYS Designer:

[Touch screen with Remote PC](javascript:void(0))

In this application, the touch screen monitor, as well as the keyboard and mouse in the room, is able to route HID signals over the Q-LAN network to the remote PC located in the IDF. The PC receives its USB connection from the Core 110f, but could just as easily receive it from the Encoder that is routing the video signal. Hereâs what it looks like in Q-SYS Designer:

**Note:** As drawn, the input signal from the touch screen can be routed across the Q-LAN network to either the Encoder or Core 110f, but only one of those two outputs can be active at a time.

[Touch screen with Multiple PCs (remote or local)](javascript:void(0))

In this application, a touch screen monitor can send USB events to either the rack PC (in the IDF, connected to the Core 110f) or the laptop on the table (connected to the NV-32-H Encoder). Hereâs what it looks like in Q-SYS Designer:

**Note:** Since USB events cannot be sent to two different hosts at the same time, the USB Router directs the output to one host or the other. This could even be automated based on what source is visible on the screen. For example, as drawn, a user could use the Active source control pin to tie the video source on the screen to the destination for the USB signals (keyboard and mouse + touchscreen). This does not require a scripting license.

[Inputs and Outputs](javascript:void(0))

### Input Pins

This component has no input pins.

### Output Pins

#### USB Input

This pin represents incoming HID signals from a USB device connected to Q-SYS hardware that supports USB routing. Wire this pin to a USB Input pin on the [USB Router](usb_router.htm) component or directly to the USB Output pin of the [USB Output](usb_output.htm) component of another Q-SYS hardware device.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

This component has no configurable properties.

[Controls](javascript:void(0))

#### Port *n* Device Connected

LED indicates whether a connection to the USB HID device is present.

#### Port *n* Device Name

Text field indicates the name of the USB HID device. This information comes directly from the HID device.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Port *n* | | | | |
| Device Connected | 0  1 | false  true | 0  1 | Output |
| Device Name | (text) | | | Output |

[Frequently Asked Questions](javascript:void(0))

[What signal types and protocols are supported by the USB routing feature?](javascript:void(0))

The USB Input and Output components support USB HID signals. This includes support for keyboard, mouse, and touch screen devices. You can also use the [External USB Audio Device In](alsa_receiver_sound_card.htm) and [External USB Audio Device Out](alsa_transmitter_sound_card.htm) components to route USB audio signals.

[Can I use USB hubs when routing USB HID signals?](javascript:void(0))

No. Connect the HID device directly to the USB-A port on the Q-SYS device.

[Can I use the USB routing feature for a webcam?](javascript:void(0))

No. You can only route signals from USB HID devices â keyboards, mice, and touch screens. Use the [External USB Audio Device In](alsa_receiver_sound_card.htm) and [External USB Audio Device Out](alsa_transmitter_sound_card.htm) components to route USB audio signals.

[Can I change the host to which USB HID devices are routed?](javascript:void(0))

Yes, use the [USB Router](usb_router.htm) component to configure routing in your schematic.

[Can I route USB devices from more than one peripheral to a single host?](javascript:void(0))

Yes, the [USB Router](usb_router.htm) component allows for multiple devices to be routed to a single output/host. For example, a keyboard and mouse on a table, as well as a touch screen monitor on a wall, can be routed to a single remote PC.

[Can I route a USB device to more than one host simultaneously?](javascript:void(0))

No, an input device can only be routed to a single output (host) at a time. You can use the [USB Router](usb_router.htm) component's control panel to dynamically switch the routing from device to host, but cannot route to multiple outputs simultaneously.
