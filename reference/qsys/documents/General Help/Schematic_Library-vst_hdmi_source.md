# Generic AV Source

> Source: https://help.qsys.com/Content/Schematic_Library/vst_hdmi_source.htm

# Generic AV Source

Use the Generic AV Source component to configure the audio and video of a source HDMI device that is wired to an NV Series device.

[Inputs and Outputs](javascript:void(0))

In an AV distribution topology using Q-SYS network video endpoints, the Generic AV Source component represents the beginning of the HDMI signal chain.

### Input Pins

This component has no input pins.

### Output Pins

#### AV Output

This pin represents the audio and video signals from the HDMI source. Connect this pin to one of the HDMI input pins of the NV Series device. HDMI video and embedded audio signals are routed directly through the NV Series device without the need for Q-SYS Core processing. Additionally, this pin can be connected to the USB-C input of the [AV I/O (NV-21-HU)](av_io.htm) component.

**Note:** You cannot wire a Generic AV Source component directly to a [Generic HDMI Display](vst_hdmi_display.htm) component.

#### Breakaway Channel

When 'Breakaway Audio' is enabled in Properties (after connecting the Generic AV Source to an Encoder/Decoder), each pin represents one channel of audio that you can route to other Q-SYS audio components, such as a network amplifier. This audio is a copy of the audio embedded within the HDMI stream, and is sent over the network to the Q-SYS Core for processing. Enable breakaway channels if you always want to hear audio from an HDMI source regardless of which output signal the HDMI I/O Decoder component is sending to a [Generic HDMI Display](vst_hdmi_display.htm) component.

[Schematic Examples](javascript:void(0))

**Note:** For more NV Series device schematic examples showing different configurations for Encoders, Decoders, and displays, see [HDMI I/O (NV-32-H)](streamer_hdmi_switcher.htm), [AV I/O (NV-21-HU)](av_io.htm), [AV I/O (NV-1-H-WE)](vstreamer_nv1wp_av_io.htm), and [Generic HDMI Display](vst_hdmi_display.htm).

[Example 1: Single HDMI source using NV-32-H](javascript:void(0))

A single HDMI source signal (audio and video) is encoded by one NV-32-H network endpoint, decoded by another NV-32-H network endpoint, and sent to an HDMI display device.

[Example 2: Single HDMI source using NV-21-HU](javascript:void(0))

A single HDMI source signal (audio and video) is encoded by one NV-21-HU network endpoint, decoded by another NV-21-HU network endpoint, and sent to an HDMI display device.

[Example 3: Single USB-C source using NV-21-HU](javascript:void(0))

A single USB-C AV source signal (video) is encoded by one NV-21-HU network endpoint, decoded by another NV-21-HU network endpoint, and sent to an HDMI display device.

[Example 4: Single HDMI source using NV-1-H-WE](javascript:void(0))

A single HDMI source signal (audio and video) is encoded by an NV-1-H-WE network endpoint, decoded by an NV-32-H network endpoint, and sent to an HDMI display device.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Audio Channels

*This property only appears when connected to an Encoder/Decoder AV input (not USB-C).*

Specify up to 8 audio channels to use for HDMI AV audio and Breakaway Audio, if enabled. The default is '2'. When set to '0', Breakaway Audio is automatically disabled. ('1' is not selectable since HDMI audio does not support a single channel.)

This property overwrites the number of audio channels specified in the input EDID. The EDID is altered to only support LPCM audio, with sampling rates from 32 KHz to 48 KHz. (NV Series device inputs do not support compressed audio sources.)

**Tip:** For example, to pass 8-channel LPCM audio from a Blu-ray player through an NV Series device to a surround sound receiver, you would need to set this property to '8'.

#### Breakaway Audio

*This property only appears when connected to an Encoder/Decoder AV input (not USB-C).*

When enabled, exposes Breakaway Channel output audio pins that can be used to route a copy of the HDMI audio to Q-SYS. The default is 'Disabled'. For more information, see [Inputs and Outputs](#Inputs).

#### Video Format Error

Controls the level of Fault status reports for AV Source components. This is particularly useful for scenarios where devices go to sleep or reboot nightly. You can choose between **Fault - Unsupported**, **Fault - Unsupported / No Format**, or **Ignore**.

**Fault - Unsupported**

* This is the default setting for all Generic AV Source components.
* A Fault status will be reported when an Unsupported Format or Interlaced Format is detected - permissible faults include:
  + Fault - Video format error (Unsupported Format).
  + Fault - Video format error (Interlaced Video Format).

**Note:** This setting is like the one below, except it does not create a Fault when the source devices stops sending TMDS video.

**Fault - Unsupported / No Format**

* A Fault status will be reported when an Unsupported Format, Interlaced Format or No Format is detected - permissible faults include:
  + Fault - Video format error (No Format Detected).
  + Fault - Video format error (Unsupported Format).
  + Fault - Video format error (Interlaced Video Format).

**Note:** This is how the Source components operate in 9.7 and below, throwing a fault when +5v is on but a valid video format is not detected.

**Ignore**

* Ignores all HDMI source faults - Generic AV Source component will show OK status regardless of the Video Format.

[Controls](javascript:void(0))

**Note:** You must wire the source's HDMI AV Output pin to an NV Series device HDMI AV Input pin to expose the source controls.

### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

### HDMI AV Output / AV Output

**Note:** AV Output will appear when connecting a Generic AV source to an NV-21-HU (HDMI or USB-C input) and NV-1-H-WE (HDMI input). HDMI AV Output will appear when connecting to an NV-32-H.

#### Cable Detect / Valid Format

LED indicates whether the HDMI input is receiving video that is compatible with Q-SYS. If this LED is not lit, it means that video is not detected on the input, is present but corrupt, or the video format is incompatible with the current operating mode - for example, a 4K60 signal is detected but 1080p60 is configured as the maximum format.

**Tip:** "Auto selection" scripts can use this LED as an indication that an input is active and usable.

#### Video Format

Displays the detected HDMI source resolution and frame rate. If the video format is incompatible (for example, interlaced input), invalid, or unrecognizable, the status indicates "Invalid".

#### Color Format

Indicates the detected color format, RGB or YCbCr. Each color format has additional detected parameters from the HDMI source:

* RGB indicates the supported pixel component quantization range, Full or Limited. For example: "RGB Limited"
* YCbCr indicates the supported color sub-sampling mode (444 or 422), color space (BT.601 or BT.709), and pixel component quantization range (Full or Limited). For example: "YCbCr 444 BT.709 Limited"

**Note:** YCbCr 4:2:0 (420) is not supported.

#### Aspect Ratio

Displays the detected aspect ratio of the source video â for example, "16:9".

#### Active Audio Channels

Displays the number of active, valid, and usable embedded audio channels detected in the HDMI source video.

#### EDID

EDID files include properties for supported video resolutions, frame rates, number of audio channels, and audio formats. Select an EDID file to apply to the HDMI source, which is then sent to the NV Series device Encoder input. Q-SYS uses standard EDID files (with file extension .qedid) to tell HDMI sources what audio and video formats are compatible with the NV Series device. If you save a display's EDID file to the Q-SYS Core (using the [Generic HDMI Display](vst_hdmi_display.htm) component's 'Save EDID to Core' control) or upload an EDID file in the Q-SYS Core Manager [Video > Video Endpoints](../Core_Manager/System_Management/Video_Endpoints.htm) page, those EDID files also appear in this list and use the .bin file extension.

**Note:** Settings within EDIDs can be dynamically changed on the NV Series device inputs depending on how you configure the NV Series device â see the 'Max Supported Format' control and the 'Audio Channels' property.

#### Max Supported Format

Indicates the maximum video format supported in the current operating mode. There are two configuration scenarios in which the NV Series device cannot accept video formats that exceed 1920x1080p60:

* If you set the NV-32-H I/O Decoder design property HDMI Output Mode to 'HDMI 1 + HDMI 2', both HDMI outputs are limited to 1920x1080p60 and smaller resolutions.
* If you set the NV Series device I/O Encoder control Encoder Mode to '1080p60 max - No Hot Plug Events', all HDMI inputs wired to the Encoder are limited to 1920x1080p60 and smaller resolutions.

#### Enable Output

Click to toggle Hot-Plug Detection (HPD) from the HDMI source. This is enabled by default. When Enable Output is toggled off, HDMI signals from the source are disabled and its status changes to "Not Present", which is the same behavior as physically disconnecting the source's HDMI cable.

**Tip:** Toggling Enable Output is useful, for example, if you have a PC with two HDMI outputs connected to an NV-32-H and you want to force the PC to use either single display mode (toggle off Enable Output on one of the outputs) or dual display mode (toggle on Enable Output on both outputs).

#### Hot-Plug Trigger

This resets the HDMI interface without having to physically disconnect and reconnect the source's HDMI cable. If you are experiencing HDMI signal issues, try pressing this button.

#### HDCP Mode

Select whether the NV Series device HDMI input negotiates and authenticates HDCP with the source:

* Auto: (Default) Allows the source to negotiate HDCP 1.4 or 2.2 with the NV Series device HDMI input. Note that when a source sends protected content, authentication can interrupt the video signal for up to 30 seconds.
* Off: The NV Series device HDMI input does not negotiate HDCP with its source. The source cannot send protected content to the input.

**CAUTION:** Many sources do not provide notification of HDCP authentication failures and instead send black video, making it difficult to diagnose video issues. Use the 'Off' mode with care.

#### HDCP Status

Displays the HDMI input's HDCP negotiated state.

#### HDCP Encryption

LED indicates whether HDCP encryption is active on the source's HDMI output..

### Audio

**Note:** This section will not appear if the Generic AV Source is connected via USB-C to an NV-21-HU.

This section shows information for all HDMI source audio channels, as configured in the 'Audio Channels' property.

#### Valid

LED glows green when the embedded audio for a channel is currently being sent from the Generic AV Source component.

#### Peak Input Level (dBFS)

Meter displaying the detected peak level of the HDMI audio, from -120 dB to 20 dB.

#### Invert

Click to invert the polarity of the audio signal.

#### Mute

Click to mute the audio signal.

#### Gain

Click to adjust the gain of the audio signal, from -100 dB to 20 dB (default is 0).

[Control Pins](javascript:void(0))

[NV-32-H HDMI Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Breakaway Audio Channel *n* | | | | |
| Gain | -100 to 20 | -100dB to 20dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  inverted | 0  1 | Input / Output |
| Level | -120 to 20 | -120dB to 20dB | 0.000 to 1.00 | Output |
| Mute | 0  1 | unmuted  muted | 0  1 | Input / Output |
| Valid | 0  1 | false  true | 0  1 | Output |
| HDMI AV Output | | | | |
| 5v | 0  1 | false  true | 0  1 | Output |
| Aspect Ratio | (text) | | | Output |
| Audio Channels Active | (text) | | | Output |
| Color Format Status | (text) | | | Output |
| EDID Filename | (text) | | | Input / Output |
| Enable Output | 0  1 | false  true | 0  1 | Input / Output |
| HDCP Encryption | 0  1 | false  true | 0  1 | Output |
| HDCP Mode | - | Off  Auto | - | Input / Output |
| HDCP Status | (text) | | | Output |
| Hot-Plug Trigger | 0  1 | false  true | 0  1 | Input / Output |
| Max Format | (text) | | | Output |
| Valid Format | 0  1 | false  true | 0  1 | Output |
| Video Format Status | (text) | | | Output |
| Status | (text) | | | Output |

[NV-21-HU HDMI Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| AV Output | | | | |
| Aspect Ratio | (text) | | | Output |
| Audio Channels Active | (text) | | | Output |
| Cable Detect | 0  1 | false  true | 0  1 | Output |
| Color Format Status | (text) | | | Output |
| EDID Filename | (text) | | | Input / Output |
| Enable Output | 0  1 | false  true | 0  1 | Input / Output |
| HDCP Encryption | 0  1 | false  true | 0  1 | Output |
| HDCP Mode | - | Off  Auto | - | Input / Output |
| HDCP Status | (text) | | | Output |
| Hot-Plug Trigger | 0  1 | false  true | 0  1 | Input / Output |
| Max Format | (text) | | | Output |
| Valid Format | 0  1 | false  true | 0  1 | Output |
| Video Format Status | (text) | | | Output |
| Breakaway Audio Channel *n* | | | | |
| Gain | -100 to 20 | -100dB to 20dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  inverted | 0  1 | Input / Output |
| Level | -120 to 20 | -120dB to 20dB | 0.000 to 1.00 | Output |
| Mute | 0  1 | unmuted  muted | 0  1 | Input / Output |
| Valid | 0  1 | false  true | 0  1 | Output |
| Status | (text) | | | Output |

[NV-21-HU USB-C Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| AV Output | | | | |
| Aspect Ratio | (text) | | | Output |
| Audio Channels Active | (text) | | | Output |
| Cable Detect | 0  1 | false  true | 0  1 | Output |
| Color Format Status | (text) | | | Output |
| EDID Filename | (text) | | | Input / Output |
| Enable Output | 0  1 | false  true | 0  1 | Input / Output |
| HDCP Encryption | 0  1 | false  true | 0  1 | Output |
| HDCP Mode | - | Off  Auto | - | Input / Output |
| HDCP Status | (text) | | | Output |
| Hot-Plug Trigger | 0  1 | false  true | 0  1 | Input / Output |
| Max Format | (text) | | | Output |
| Valid Format | 0  1 | false  true | 0  1 | Output |
| Video Format Status | (text) | | | Output |
| Status | (text) | | | Output |

[NV-1-H-WE HDMI Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| AV Output | | | | |
| Aspect Ratio | (text) | | | Output |
| Audio Channels Active | (text) | | | Output |
| Cable Detect | 0  1 | false  true | 0  1 | Output |
| Color Format Status | (text) | | | Output |
| EDID Filename | (text) | | | Input / Output |
| Enable Output | 0  1 | false  true | 0  1 | Input / Output |
| HDCP Encryption | 0  1 | false  true | 0  1 | Output |
| HDCP Mode | - | Off  Auto | - | Input / Output |
| HDCP Status | (text) | | | Output |
| Hot-Plug Trigger | 0  1 | false  true | 0  1 | Input / Output |
| Max Format | (text) | | | Output |
| Valid Format | 0  1 | false  true | 0  1 | Output |
| Video Format Status | (text) | | | Output |
| Breakaway Audio Channel *n* | | | | |
| Gain | -100 to 20 | -100dB to 20dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  inverted | 0  1 | Input / Output |
| Level | -120 to 20 | -120dB to 20dB | 0.000 to 1.00 | Output |
| Mute | 0  1 | unmuted  muted | 0  1 | Input / Output |
| Valid | 0  1 | false  true | 0  1 | Output |
| Status | (text) | | | Output |
