# Attero Tech unHX2D

> Source: https://help.qsys.com/Content/Schematic_Library/Attero_Tech_extension_unHX2D.htm

# Attero Tech unHX2D

Use this extension to connect to and control a unHX2D Danteâ¢/AES67 enabled HDMI audio embedder/de-embedder (Attero Tech by QSC).

**Note:** See the [unHX2D product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/attero-tech/at-surface-mount-network-audio-interfaces/unhx2d/) on the QSC website for product information and documentation.

[Compatibility](javascript:void(0))

The extension is compatible with Q-SYS Designer version 8.4 and above and Attero Tech firmware version 1.2.0 and above. For best results, use the latest Attero Tech firmware.

[Connection Setup](javascript:void(0))

To begin using the extension:

1. Drag it into the schematic.
2. Configure the extension properties. See [Properties](#Properti).
3. Press F5 to save your design to the Core and run it.
4. In the NIC field, select the interface through which the extension will communicate to control the device.
5. In the Unit/IP field, specify the IP address of the device and press Enter.

The extension will automatically attempt a connection. The "Connected" LED glows green once a connection is established. If the extension loses its connection to the device, it will attempt to re-establish the connection every 5 seconds.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Show Debug

Select 'Yes' to show the Debug Output window. For details, see [Debug Output](debug_output.htm).

[Controls](javascript:void(0))

#### Refresh

Although the extension monitors the device settings for changes automatically, this button manually triggers the extension to retrieve the current settings and update the extension values to match.

#### Identify

Causes the power LED on the front of the device to start blinking so it can easily be identified. The identify function remains active until manually turned off. Click the button to toggle between states.

#### Status

Normally, this shows "Initializing" for a few moments after starting your design, followed by "OK". If you see a "Fault" status, check your connection parameters. If you see "Missing", ensure that the device is powered on and connected to the network.

#### Details

Provides information on the connected device such as MAC address, IP address, MCU version, and parameter lock state.

#### Save as Default

Forces the device to save its current settings as the new power-on defaults.

### HDMI Setup

The unHX2D allows HDMI audio sources to be de-embedded and re-embedded from/to the HDMI I/O on the device. Use these controls to configure the HDMI setup and status monitoring.

#### HDCP Sink Support

The unHX2D allows HDCP to be disabled on the unHX2D HDMI input. This does not unencrypt copy protected content, but rather is used to signal to source devices that the eventual sink device (monitor, projector) does not support HDCP.

Default = Enabled

#### Ignore Hotplug Detect

HPD (Hot Plug Detect) is used in HDMI repeaters to signal the presence and removal of a connected sink to the original source device. In some cases, it is desirable to de-embed the HDMI audio content without a connected sink device. In this setup, the installer should toggle this control 'on' to ignore the lack of a connected sink device.

Default = Disabled

#### EDID

Use the EDID setting to provide the source device an indication of the acceptable formats for use with the unHX2D. The settings are limited to advertise 2 channel PCM for artifact-free audio de-embedding. Force the EDID to 2 CH PCM modes where possible.

* 1080p / 2 CH PCM (Default)
* 1080i / 2 CH PCM
* 3D / 2 CH PCM
* 4K / 2 CH PCM
* Use Sink (Capabilities described by connected sync device)

**CAUTION:** Use Sink allows compressed multichannel content to be de-embedded; however, the unHX2D cannot decode this content and this will create considerable distortion and possibly damage downstream amplifiers and speakers receiving this errant audio content.

### Input Setup

The unHX2D supports connectivity for 2 analog audio inputs.

#### Input Gain 1, 2 Pro Level

The input sensitivity can be set independently for each channel depending on the connected audio device. Enable this control for Pro line level audio. Disable for Consumer, -10dBV nominal line level. This is the default.

### Output Setup

The unHX2D supports connectivity for analog audio outputs, HDMI audio output, and Dante audio outputs. Each channel features independent volume control and mute functions. These additional options are available for the Dante channels:

#### Mono

Toggle the mono mixdown option.

#### Delay

Toggle and adjust a 400ms lip sync delay.

### Internal Routing Matrix

The unHX2D supports an internal stereo audio routing matrix.

#### Mixer Level

Adjustable from -100 to 0dB from any input to any output.

#### HDMI Direct

Enable this option to remove the ability to embed audio to the HDMI audio output. All associated HDMI Out mix controls will also be disabled.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Analog Out Mixer | | | | |
| 1, 2, 3, 4, 5 | -100 to 0 | -100 to 0 | 0.00 to 1.00 | Input / Output |
| Analog Out Mute | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Analog Out Volume | | | | |
| 1, 2 | -100 to 20 | -100 to 20 | 0.00 to 1.00 | Input / Output |
| Dante 1&2 Out Mixer | | | | |
| 1, 2, 3, 4, 5 | -100 to 0 | -100 to 0 | 0.00 to 1.00 | Input / Output |
| Dante 1&2 Out Mute | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Dante 1&2 Out Volume | | | | |
| 1, 2 | -100 to 20 | -100 to 20 | 0.00 to 1.00 | Input / Output |
| Dante 3&4 Out Mixer | | | | |
| 1, 2, 3, 4, 5 | -100 to 0 | -100 to 0 | 0.00 to 1.00 | Input / Output |
| Dante 3&4 Out Mute | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Dante 3&4 Out Volume | | | | |
| 1, 2 | -100 to 20 | -100 to 20 | 0.00 to 1.00 | Input / Output |
| Device | | | | |
| Connected | 0  1 | false  true | 0  1 | Output |
| EDID | - | 1080p CH2.0  1080i CH2.0  3D CH2.0  4K CH2.0  Use Sink | - | Input / Output |
| HDCP Sink | 0  1 | false  true | 0  1 | Input / Output |
| HDMI Direct | 0  1 | false  true | 0  1 | Input / Output |
| HPD Ignore | 0  1 | false  true | 0  1 | Input / Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Output Delay | 0 to 400 | 0 to 400 | 0.00 to 1.00 | Input / Output |
| Output Delay Enable | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| HDMI Out Mixer | | | | |
| 1, 2, 3, 4, 5 | -100 to 0 | -100 to 0 | 0.00 to 1.00 | Input / Output |
| HDMI Out Mute | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| HDMI Out Volume | | | | |
| 1, 2 | -100 to 20 | -100 to 20 | 0.00 to 1.00 | Input / Output |
| Input Mono | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Input Preamp Control | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Disable[1](#Use) | 0  1 | disabled  enabled | 0  1 | Input / Output |

###### 1. Use this control pin to enable or disable the extension in your design. When Disabled is set to enabled (value of 1), the Connection Status changes to "Not Present - Disabled".
