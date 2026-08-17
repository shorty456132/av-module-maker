# HID Conferencing

> Source: https://help.qsys.com/Content/Schematic_Library/usb_telephony.htm

# HID Conferencing

Use the HID Conferencing component to control a conferencing application, such as Skype for Business or Zoom, on a remote computer connected to a Q-SYS device that supports HID conference control.

**Note:** Skype for Business for Mac computers is currently incompatible with the HID Conferencing component.

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

* You need a USB A/B cable to connect a computer to the Q-SYS device.
* In the Q-SYS device properties, enable USB Audio Bridging and drag the Speakerphone / Sound Card In and Out components into the schematic. The HID controller requires an audio connection to successfully control your conferencing application, and the [USB Audio Bridge](USB_Audio_Bridge.htm) components must be in the schematic for this connection.

  **Note:** Use either Speakerphone or Sound Card. If you use both, the HID Conferencing component defaults to working with the Sound Card.
* HID Conferencing is designed to control a remote computer â connected to a Q-SYS device supporting HID conferencing â from another Q-LAN-connected device, such as a computer or touch screen controller. Do not use the component directly from the computer connected to the Q-SYS device, as unexpected behavior can occur.
* To control a remote computer running Zoom, you must enable 'Zoom Compatibility' mode in the USB Bridging properties. For more information, see [USB Audio Bridge](USB_Audio_Bridge.htm).

[Configuration Overview](javascript:void(0))

1. Connect the USB A/B cable's rectangular 'A' connector to a USB port on a computer.
2. Connect the other end of the cable, the square 'B' connector, to the USB B port on the supported Q-SYS device.
3. On another PC connected to the Q-LAN network, drag the HID Conferencing component into your schematic from the Q-SYS device's inventory tree.
4. Double-click the component to open the control panel. Copy the controls into a User Control Interface (UCI) and configure the UCI to display on a TSC touch screen.
5. In the Q-SYS device's properties, enable Audio Bridging, and configure it for Speakerphone or Sound Card. To see a wiring diagram, refer to the [Example](#Example).

   **Note:** Use either Speakerphone or Sound Card. If you use both, the HID controller defaults to working with the Sound Card.
6. (Optional) If you will be controlling a remote computer running Zoom, enable 'Zoom Compatibility' mode in the USB Bridging properties. See [USB Audio Bridge](USB_Audio_Bridge.htm) for more information.
7. Press F5 to save your design to the Core and run it.
8. On the Core-connected computer, open your conferencing application, such as Skype for Business or Zoom.
9. In the touch screen UCI, use the buttons to remotely control the conferencing application on the Core-connected computer.

[Example](javascript:void(0))

In this example, a design includes:

* A Core 110f with Audio Bridging enabled and configured for Speakerphone. See [USB Audio Bridge](USB_Audio_Bridge.htm) for more information.
* A speakerphone device (or headset with microphone) connected to one of the Core 110f's front USB ports.
* External USB Audio enabled in the Core 110f properties, which is necessary to communicate with the speakerphone device. See [External USB Audio Device](External_USB_Audio_Device.htm) for more information.
* A TSC touch screen configured to run a UCI that contains the HID Conferencing controls.
* An [Acoustic Echo Canceler](acoustic_echo_canceler_simd.htm) component, which is required when routing speakerphone audio.

In the schematic:

* The Ext USB Device In component passes incoming audio from the speakerphone device to the conferencing application (far-end) via the USB EC Speakerphone Out component, allowing conference callers to hear audio from the near-end. An AEC component is used to process speakerphone audio to avoid echo.
* The USB EC Speakerphone In component receives audio from the far-end and sends it to the speakerphone device's speaker via the Ext USB Audio Dev Out component, allowing the near-end to hear far-end conferencing audio.
* The HID Conferencing buttons are used to control the call from the touch screen controller.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### HID Conferencing Properties

#### Enable Call Sync

Use the Call Sync component to simplify the integration of Q-SYS collaboration devices and calling systems. It synchronizes mute state, call controls, and LED light behavior across multiple calling components, including USB HID Conferencing, Softphone, and POTS Controller. See the [Call Sync](call_sync.htm) topic

#### Off Hook Debounce (ms)

The system will wait for a short period to confirm that the Off Hook status has genuinely changed before updating the indicator. The time ranges from 0 (default) to 2,000 ms.

[Controls](javascript:void(0))

The HID Conferencing component includes standard conferencing control functions.

### Indicators

#### Off Hook

Indicates that a call is actively in progress.

#### Mute

Indicates that the Phone Mute control is active, meaning that near-end audio cannot be heard.

#### Ring

Indicates an incoming call.

#### Connected

Indicates that the HID component detects a connection to the Core-connected computer.

### Controls

#### Call Accept

Click to accept an incoming call.

#### Call Decline

Click to decline an incoming call. In some conferencing applications (such as Skype for Business), this button also ends an active call.

#### Phone Mute

Click to mute near-end microphone audio.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| LED | | | | |
| Connected | 0  1 | disabled  enabled | 0  1 | Output |
| Mute | 0  1 | disabled  enabled | 0  1 | Output |
| Off Hook | 0  1 | disabled  enabled | 0  1 | Output |
| Ring | 0  1 | disabled  enabled | 0  1 | Output |
| Call Accept | 0  1 | false  true | 0  1 | Input / Output |
| Call Decline | 0  1 | false  true | 0  1 | Input / Output |
| Phone Mute | 0  1 | false  true | 0  1 | Input / Output |

[Troubleshooting](javascript:void(0))

### Accepting and Ending Calls with Zoom

Zoom Desktop and Zoom Rooms only support Call Accept and Call Decline functionality upon an incoming call. Once the call has started, the call cannot be ended with the Call Decline button provided by Q-SYS HID. It is possible, however, to end a call with *Ctrl*+*Shift*+*E* on the desktop client but not on Zoom Rooms.

### No HID Conferencing Feedback

To ensure your HID Conferencing component works seamlessly with Teams or Zoom, make sure to select the Echo Canceling Speakerphone as both your input and output audio device in the conferencing software.

If you choose any other audio device (such as laptop speakers or soundcard), the HID Conferencing controls (like mute and volume) will not function, as the software can't communicate with the correct device.
