# USB Audio Bridge â Speakerphone / Sound Card Out

> Source: https://help.qsys.com/Content/Schematic_Library/usb_transmitter.htm

# USB Audio Bridge â Speakerphone / Sound Card Out

The USB Audio Bridge allows you to send and receive 48 kHz, 16-bit PCM audio between a computer and Q-SYS using a UAC-compliant (driverless) USB connection. You can configure the USB Audio Bridge to behave as:

1. An **Echo Canceling (EC) Speakerphone**
2. A **Non-Echo Canceling (NEC) Speakerphone**
3. A **Sound Card**
4. or **Speakerphone (EC or NEC) & Sound Card** simultaneously
5. An **Advanced** mode with up to 4 unique USB Audio Bridges, each configured as a Speakerphone or Sound Card

This enables the Q-SYS device to act as an endpoint for web conferencing and music playback to and from a computer.

**Tip:** You can also connect to some Windows-based tablets. Tablets require an on-the-go cable.

[Q-SYS Devices that Support Audio Bridging](javascript:void(0))

These devices support USB audio bridging from Q-SYS to a connected PC:

| Q-SYS Device | Max Audio Bridges | Max Speakerphone Inputs/Outputs per Bridge | Max Sound Card Inputs/Outputs per Bridge |
| --- | --- | --- | --- |
| [Core Nano](../Hardware/Processing/Core_Nano.htm) | 4 (Any combination) | 1 | 8 |
| [Core 8 Flex](../Hardware/Processing/Core_8_Flex.htm) | 4 (Any combination) | 1 | 8 |
| [NV-21-HU Network Video Endpoint](../Hardware/Video/NV-21-HU.htm) | 2 (Speakerphone + Sound Card) | 1 | 2 |
| [NV-32-H (Core Capable) Network Video Endpoint](../Hardware/Video/NV-32-H_Core_Capable.htm) | 2 (Speakerphone + Sound Card) | 1 | 2 |
| [Core 110f](../Hardware/Processing/Core_110f.htm), [Core 110c](../Hardware/Processing/Core_110c.htm) | 4 (Any combination)[1](#Core) | 1 | 8 |
| [Core 24f](../Hardware/Processing/Core_24f.htm) | 4 (Any combination)[2](#2.24f) | 1 | 8 |
| [I/O-USB Bridge](../Hardware/IO_Expanders/IOUSB_Bridge.htm) | 2 (Speakerphone + Sound Card) | 1 | 2 |
| [TSC-70-G3](../Hardware/Control_IO/TSC-70-G3.htm) | 2 (Speakerphone + Sound Card) | 1 | 2 |
| [TSC-101-G3](../Hardware/Control_IO/TSC-101-G3.htm) | 2 (Speakerphone + Sound Card) | 1 | 2 |

###### 1. Core 110f supports up to 16x16 USB audio channels total, configurable across a maximum of 4 USB audio devices, each having a maximum of 8x8 USB audio channels.

###### 2. Core 24f supports up to 16x16 USB audio channels total, configurable across a maximum of 3 USB audio devices, each having a maximum of 8x8 USB audio channels.

[USB Connection Requirements](javascript:void(0))

* For most Q-SYS hardware, connect your PC or Mac host to the Q-SYS Core or peripheral's USB-B port or, if supported, the USB-C port.
* A USB 3.0 or USB-C cable must be 6 feet in length or less. Cables longer than 6 feet may have undetermined results.
* For the TSC-7t touch screen only, connect your PC or Mac to the TSC-7t's Micro-B port.
* If the Q-SYS device has both USB-B and USB-C ports, only one can be used at a time to connect to a PC or Mac host. If both are connected to hosts, the USB-B port takes priority.
* QSC has not tested third-party USB extension products. For the best experience, only direct USB connections are supported. If a long distance USB bridging solution is required, we recommend the [I/O-USB Bridge](../Hardware/IO_Expanders/IOUSB_Bridge.htm), which can easily be extended to the desired location via network cabling.

[Configuration Overview](javascript:void(0))

The USB Audio Bridge (Speakerphone or Sound Card) is a component within the inventory tree of a supported Q-SYS device.

1. Add a Q-SYS device that supports audio bridging to your inventory.
2. From the Q-SYS device's properties, set the USB Audio Bridge property to Speakerphone or Sound Card (or both). Some devices support 'Advanced' mode â for more information on all modes, see [Properties](#Properti).
3. Drag the USB In and Out components into your schematic, and then wire them to other Q-SYS audio components.

   **Note:**  If you are using Speakerphone type, be sure to include the [Acoustic Echo Canceler](acoustic_echo_canceler_simd.htm) component in your design.
4. Run your design.
5. Your computer detects the Q-SYS device as a playback and/or recording audio device. In your computer's audio setup, configure the settings to enable these devices â for example, "Set Default" in Windows.
   * The USB In component receives audio from your computer (for example, from a music player or conferencing software) and sends it to Q-SYS for processing. The USB In component is viewed as an audio output device (Playback' tab in Windows) by your computer.
   * The USB Out component sends audio from Q-SYS to your computer (for example, to conferencing software). The USB Out component is viewed as an audio input device ('Recording' tab in Windows) by your computer.

### Example

In this example, a PC is connected to the USB B port on an I/O USB Bridge. The I/O USB Bridge's USB Audio Bridge is configured as a Sound Card (2 input channels, 2 output channels). Audio from the computer is sent to a Q-SYS network amplifier and speakers. Audio from Q-SYS (in this case, an Audio Player) is sent to the computer for playback.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### USB Bridging â Audio Bridge Properties

These properties are available when the USB Audio Bridge property is set to anything except 'Disabled'.

#### USB Audio Bridge Count

You must have Advanced selected. The number of Speakerphone and / or Sound Cards, from 0 to 4. (Default is 2)

#### Type

You must have Advanced selected. Select the type of USB Bridge: Sound Card or Speakerphone. (Default is Sound Card)

#### Input Mode

Configures the input as a Speaker configuration (stereo, 7.1, etc.) or Line input providing up to 8 channels in pairs. (Default is Line)

#### Input Count

Available only when the Input Mode is set to Line. USB Sound Card In is the input to the Q-SYS device, which is the output from your computer. In the Windows Sound dialog > Playback tab, "*CoreName* Sound Card" displays as Line Out.

You can select up to 8 input channels (in pairs) for each USB Sound Card In component, with a maximum of 16 input channels (Core 110f) or 8 input channels (I/O-8 Flex, Core 8 Flex, Core Nano) in a design.

In the Line mode, Windows uses only the first two channels.

You can use the ASIO4ALL driver to access all channels by ASIO-enabled applications.

#### Speaker Mode

Available only with the Input Mode set to Speaker. Select the speaker configuration: Stereo, Quadraphonic, 5.1, or 7.1. (Default is Stereo)

When you select the speaker mode your computer views the Core as a device having the selected configuration. The outputs are labeled accordingly - left, right, center, and so on. When the media coming into the Core is matches the speaker configuration, the media is played in the correct format.

#### Output Count

The USB Sound Card Out is the output from the Core or I/O-8 Flex â the input to your computer. In the Windows Sound dialog > Recording tab, "*CoreName* Sound Card" displays as Line In.

You can select up to 8 output channels (in pairs) for each USB Sound Card Out component, with a maximum of 16 output channels in a design.

#### Speakerphone Mode

This selection is available only when Speakerphone or Speakerphone and Sound Card is selected in the USB Audio Bridge property. Indicates if the Q-SYS design has Echo Canceling (EC) or Non-Echo Canceling (NEC). This information is provided to the PC or Mac operating system so it can determine whether or not to use its own echo canceling.

[Controls](javascript:void(0))

### Channel *n* Input

#### Peak Level (dBFS)

Meter displaying the Peak Input Level.

#### Invert

Button to invert the input audio signal.

#### Mute

LED indicates whether the input audio signal is muted.

#### Gain (dB)

Indicates the input gain.

### Status

#### Connected

LED indicates whether the USB In component is connected to a computer.

#### Active

LED indicates whether the signal is streaming.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Channel *n* | | | | |
| Gain | -100 to 20 | -100 dB to 20 dB | 0  1 | Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Output |
| Peak Level | -120 to 20 | -120 dB to 20 dB | 0  1 | Output |
| Active | 0  1 | Off  On | 0  1 | Output |
| Connected | 0  1 | Off  On | 0  1 | Output |

[Troubleshooting](javascript:void(0))

### "USB Device Not Recognized"

If you see this Windows pop-up message, it means that you've connected a TSC-G3 Series touch screen to the host PC but do not have the TSC-G3 USB Video Bridge or USB Audio Bridge enabled and included in a running design. To resolve, follow the steps in the [Configuration Overview](#ConfigOverview) section.
