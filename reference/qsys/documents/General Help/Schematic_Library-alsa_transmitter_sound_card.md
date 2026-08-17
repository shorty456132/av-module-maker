# External USB Audio Device Out

> Source: https://help.qsys.com/Content/Schematic_Library/alsa_transmitter_sound_card.htm

# External USB Audio Device Out

The External USB Audio Device components allow you to connect a standard USB headset, speakerphone, or similar to a compatible Q-SYS device and process the incoming and outgoing audio streams in the Q-SYS audio DSP. Mono input devices and stereo output devices are supported.

**Tip:** The External USB Audio Device feature is intended for connection of USB headsets, speakerphones, and similar devices. To send and receive audio between a PC and the Q-SYS Ecosystem, use the [USB Audio Bridge](USB_Audio_Bridge.htm) feature.

[Supported Q-SYS Hardware](javascript:void(0))

The following Q-SYS devices can accept a USB connection to an external audio device:

* [Core 110f](../Hardware/Processing/Core_110f.htm) and [Core 110c](../Hardware/Processing/Core_110c.htm)
* [Core Nano](../Hardware/Processing/Core_Nano.htm)
* [Core 8 Flex](../Hardware/Processing/Core_8_Flex.htm)
* [Core 24f](../Hardware/Processing/Core_24f.htm)
* [NV-32-H (Core Capable) Network Video Endpoint](../Hardware/Video/NV-32-H_Core_Capable.htm)
* [I/O-USB Bridge](../Hardware/IO_Expanders/IOUSB_Bridge.htm)

[Supported External USB Audio Devices](javascript:void(0))

For compatibility with Q-SYS, your external USB device (headset, speakerphone, or similar) must support the following specifications.

### Input Devices

* **Sampling rate**: 48k or 16k, mono
* **Resolution**: 8-bit, 16-bit, 24-bit, 32-bit, float
* **Format**: Little-endian, signed or unsigned

### Output Devices

* **Sampling rate**: 48k only, stereo
* **Resolution**: 8-bit, 16-bit, 24-bit, 32-bit, float
* **Format**: Little-endian, signed or unsigned

[Supported Ports](javascript:void(0))

* **USB-A Ports**: Use these ports to connect the External USB audio device.
* **USB-B Ports**: These ports are used for host connections and are not suitable for connecting the External USB audio device.

[Configuration Overview](javascript:void(0))

1. Connect an external USB audio device to a compatible Q-SYS Core or peripheral USB port. See [Supported Q-SYS Hardware](#Supporte).

   **Note:** If you connect multiple USB devices, the External USB Audio components will only detect the last one connected.
2. From your Inventory list, select the Q-SYS Core or peripheral.
3. In the Properties window, set External USB Audio to 'Enabled'.
4. From your Inventory list, drag the External USB Audio Device In and External Audio Device Out components into your schematic.
5. To send monaural audio from your device microphone, connect the External USB Audio Device In mono output pin to the input pin of a downstream component.
6. To send stereo audio to your playback device, connect the External USB Audio Device Out stereo input pins to the output pins of an upstream component.
7. Press F5 to save your design to the Core and run it. (Or, press F6 to emulate your design.)
8. Double-click an External USB Audio Device component to open the component's control panel. See [Controls](#Controls).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

#### Audio Device

A read-only indicator that shows the name of the detected external USB device.

### Input / Channel

#### Peak Input Level (dBFS)

Meter displaying the detected peak level of the audio input or output.

**Note:** The External USB Audio Device In component must be wired to another component for the meter to function.

#### Invert

Click to invert the polarity of the input or output audio signal.

#### Mute

Click to mute the input or output audio signal.

#### Gain (dB)

Click to adjust the gain on the input or output audio signal, from -40 dB to 0 dB.

### Status

#### Connected

LED indicates whether the USB device is connected.

#### Fault

LED indicates whether a problem has been detected with the audio stream. Faults are logged in the Q-SYS Core Manager [Event Log](../Core_Manager/Event_Log.htm).

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Channel *n* | | | | |
| Gain | -40 to 0 | -40dB to 0dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  inverted | 0  1 | Input / Output |
| Mute | 0  1 | unmuted  muted | 0  1 | Output |
| Peak Input Level | -120 to 20 | -120dB to 20dB | 0.000 to 1.00 | Output |
| Active Device | (text) | | | Output |
| Connected | 0  1 | false  true | 0  1 | Output |
| Fault | 0  1 | false  true | 0  1 | Output |
