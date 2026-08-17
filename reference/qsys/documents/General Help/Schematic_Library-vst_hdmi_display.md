# Generic HDMI Display

> Source: https://help.qsys.com/Content/Schematic_Library/vst_hdmi_display.htm

# Generic HDMI Display

Use the Generic HDMI Display component to configure the audio and video received from an NV-32-H or NV-21-HU for output to an HDMI display.

[Inputs and Outputs](javascript:void(0))

### Input Pins

#### HDMI AV Input

This pin represents the incoming HDMI audio and video to display. Connect this pin to an [HDMI I/O (NV-32-H)](streamer_hdmi_switcher.htm) or [AV I/O (NV-21-HU)](av_io.htm) component HDMI AV Output pin.

**Note:** You cannot wire a [Generic AV Source](vst_hdmi_source.htm) component directly a Generic HDMI Display component.

#### Breakaway Channel

When 'Audio Input Pins' is enabled in the Properties, each pin represents one channel of audio from a Q-SYS audio source that replaces the audio from the HDMI signal. This is useful, for example, if you want to display HDMI video but use the display's speakers (or connected speaker bar) to play independent audio, such as a music track, PA system pages, etc.

### Output Pins

This component has no output pins.

[Schematic Examples](javascript:void(0))

**Note:** For additional schematic examples, see the [HDMI I/O (NV-32-H)](streamer_hdmi_switcher.htm) and [AV I/O (NV-21-HU)](av_io.htm) topics.

[Example 1: Single display with audio from selected AV source](javascript:void(0))

In this example, three HDMI sources can be encoded and decoded, and the selected source's HDMI audio and video is sent to the display. (The display component's Audio Source property is set to 'Selected Source'.)

**Note:** To see video but ignore the embedded audio in the HDMI signal, set the display component's Audio Source property to 'None'.

[Example 2: Dual displays, one with mixed replacement audio](javascript:void(0))

In this example, three HDMI sources can be encoded and decoded, while two displays can display independent sources (Decoder's HDMI Output Mode property set to 'HDMI1 + HDMI 2'). Display 1 is connected to a speaker bar, which serves as the audio amplification system for this room. Audio from the two AV sources is mixed with Q-SYS PA system pages and the mixed audio is sent to Display 1's audio input pins. (The display component's Audio Source property is set to 'Audio Input Pins'.) This audio replaces the embedded HDMI audio.

**Note:** For more NV-32-H and NV-21-HU schematic examples showing different configurations for encoders, decoders, and sources, see [HDMI I/O (NV-32-H)](streamer_hdmi_switcher.htm), [AV I/O (NV-21-HU)](av_io.htm), and [Generic AV Source](vst_hdmi_source.htm) topics.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Generic HDMI Display Properties

#### Audio Source

This property determines what audio, if any, is sent to the display. To see this property, you must wire the Generic HDMI Display component to an HDMI I/O component's HDMI Output pin. There are three choices:

* Selected Source: (Default) Audio from the selected AV source is sent to the display over HDMI. In this mode, audio is not processed in the Q-SYS Core's DSP, so no network audio channels are consumed. This option exposes HDMI Audio controls for a maximum of 8 audio channels, depending on the audio capability reported by the display's EDID, as specified in the Generic AV Source properties.
* None: No audio is sent to the display over HDMI.
* Audio Input Pins: Audio from the selected AV source is removed and replaced with audio connected to the Breakaway Channel pins. This audio is routed through the Q-SYS Core's DSP, consuming network audio channels. This option exposes HDMI Audio controls for the number of configured Audio Channels in the component properties, up to 8 maximum, depending on the audio capability reported by the display's EDID.

#### Audio Channels

When the Audio Source property is set to 'Audio Input Pins', this determines the number of audio input pins and corresponding audio controls to show. You can specify 0, or 2 to 8. The default is '2'.

**Note:** To avoid a "Compromised" status for the Generic HDMI Display, ensure that the number of Audio Channels matches what is supported in the display's EDID.

#### CEC

Select whether to enable Consumer Electronics Control (CEC) support for the HDMI display, which allows you to control the display's power directly from Q-SYS. The default is 'Disabled'. CEC is supported only by NV Series devices. When CEC is enabled, a CEC tab appears in the component's control panel. See the [CEC](#CEC) section for control definitions.

**Note:** CEC support is dependent on the display manufacturer's adherence to CEC specifications. Before using CEC in a production environment, you should validate that the CEC commands operate as desired on each display device in your system.

### Identification

#### Custom CEC Commands

This property determines how many custom CEC command controls are available in the Generic HDMI Display component. Allows up to 8.

[Controls](javascript:void(0))

**Note:** You must wire the display's HDMI AV Input pin to a NV-32-H or NV-21-HU HDMI AV Output pin to expose the display controls.

### Video

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### EDID: Name, Serial Number, Audio Channels

These values are obtained from the display's EDID, with the Audio Channels value being the maximum number of PCM audio channels supported by the display. If the EDID cannot be read, these fields are blank.

#### Save EDID to Core

Click this button to save the display's EDID file to the EDID folder on the Q-SYS Core. Each button press adds an incrementing filename number suffix â for example, VA2246SERIES.bin, VA2246SERIES(1).bin, VA2246SERIES(2).bin.

**Tip:** Use Q-SYS Core Manager to manage EDID files - see [Video > Video Endpoints](../Core_Manager/System_Management/Video_Endpoints.htm).

#### Connected (HPD)

This LED glows green if the HDMI Hot-Plug Detect (HPD) signal is active, indicating that the display is connected to the NV-32-H or NV-21-HU.

#### HDMI Enable

This enables or disables the NV-32-H or NV-21-HU HDMI output, with a default of 'Enabled'. Setting this control to 'Disabled' produces the same result as unplugging the HDMI cable to the display:

* HDMI output is immediately turned off.
* No idle screen is shown.
* The display's Status control changes to "Not Present - HDMI Disabled - Display status unknown".

#### Auto Power

*This is only available when the CEC Property is set to **Enabled**.* When set to **Enabled**, it allows the HDMI Enable button to turn on/off the Displayâs power.

It uses the *on* and *off* command from the CEC tab to issue these commands.

The **HDMI Enable** control will hold the expected state, and its Input/Output pins can be used to receive/send control commands via the wiring domain to other Q-SYS Components.

#### Video Mute

Click to replace video output with a black screen while still maintaining sync with the display. This is useful, for example, if a user is presenting content from a PC and wants to briefly black the screen while preparing new content to show. When Video Mute is engaged, HDMI audio continues normal playback.

**Note:** Video Mute is automatically toggled off if HDMI Enable is toggled on, or if Video Freeze is toggled on, or if Idle or Sleep modes are triggered or toggled on.

#### Video Freeze

When enabled, the HDMI output will constantly replay the current video frame regardless of its source. When disabled, the HDMI output will resume showing full frame rate video.

Audio functionality is not affected by the Video Freeze state; therefore, if you wish to have the audio mute and video mute states in sync, you should do so with control wiring through the corresponding Control Pin:*HDMI AV Input* hierarchy and choose *Video Freeze*.

**Note:** Video Freeze is automatically toggled off if Video Mute is toggled on, HDMI Enable is toggled on, or if Idle or Sleep modes are triggered or toggled on. Video Freeze is only supported on NV series decoder HDMI outputs. It is not supported via the local HDMI output when an NV is acting as an encoder.

#### Idle Mode

Determine what content is displayed, if any, after a pre-set amount of time has elapsed â for example, between meetings.

* Source Content: Select whether to show the Idle Screen (default), Black Video, or Graphic 1-3. Upload custom idle screen and graphic content using Q-SYS Core Manager - see [Video > Video Endpoints](../Core_Manager/System_Management/Video_Endpoints.htm).
* Timer: Select the amount of time to elapse (with no HDMI signal and black screen) before triggering display of Source Content: 15s, 30s (default), 60s, 120s.
* Trigger: Click this button to force Idle Mode to begin immediately.
* Idle State (LED): Glows green when Idle Mode is active. Use the associated control pin to trigger events (for example, UCI page changes) based on the LED state.

#### Sleep Mode

Determine what content is displayed, if any, after a pre-set amount of time has elapsed in Idle Mode â for example, at the end of the business day.

* Source Content: Select whether to Disable HDMI (default), or show Black Video, the Idle Screen, or Graphic 1-3. Upload custom idle screen and graphic content using Q-SYS Core Manager - see [Video > Video Endpoints](../Core_Manager/System_Management/Video_Endpoints.htm).
* Timer: Select the amount of time to elapse in Idle Mode before triggering Sleep Mode: 1s, 5s, 30s, 1m, 10m (default), 30m, 60m, 8hr.
* Trigger: Click this button to force Sleep Mode to begin immediately.
* Sleep State (LED): Glows green when Sleep Mode is active. Use the associated control pin to trigger events (for example, UCI page changes) based on the LED state.

#### Video Format, Status

This control sets the HDMI video format (resolution and frame rate) the NV-32-H or NV-21-HU sends to the display. This setting is independent of the source â the format you select is applicable to both network AV and local HDMI sources connected to the NV-32-H or NV-21-HU. Incoming source signals are scaled to match the output Video Format. The status text box indicates the current format being sent to the display.

* Auto: (Default) The display uses the highest priority format (as communicated in the display's EDID) that is compatible with the NV-32-H or NV-21-HU HDMI output. If a display's EDID cannot be read, the universally-supported format of 640x480p60 is used.

  **Tip:** Auto mode negotiates the highest resolution of the display and scales any source up to that format. For example, a 1080p60 source and a 4K60 source would produce the same output resolution. This mode eliminates the need to save a display's EDID file and apply it to sources.
* Forced (listed format): To force a particular resolution (horizontal size and vertical size) and frame rate for the display, select a format in the list. The list includes only formats that the NV-32-H and NV-21-HU supports.
  + An asterisk (\*) indicates a format included within the display's EDID. These are the resolutions that the display prefers.
  + The (preferred) label indicates the display's preferred format. For example â 1920x1080p60 (preferred)\*

  **Tip:** When you select (force) an output format, corrupt source EDID files are less likely to cause issues.

#### HDCP Mode, Status

HDCP authenticates and encrypts content, and is required by many HDMI sources. This control defines how HDCP authentication is negotiated with the connected display. The status text box indicates the HDMI output's current HDCP status.

* Auto: (Default) HDCP is enabled on the HDMI output connected to the display whenever HDCP-protected source content is detected. There is a time delay of a few seconds when changing AV sources while the negotiation process determines if HDCP encryption is required by the source.
* Off: No HDCP authentication or encryption is attempted. Protected content cannot be displayed. If you attempt to display protected content, you will see an HDCP error screen.

#### HDCP Encryption

This LED glows green whenever the HDMI content being received by the display is protected by HDCP.

#### HDMI or DVI, Status

Use this control to override the type of display reported in the display's EDID. The status text box indicates the mode currently driving the display.

* Auto: (Default) The display type (HDMI or DVI) is determined by the display's EDID.
* Force DVI: This option disables embedded audio and InfoFrames (metadata about the video signal). You can use this option to troubleshoot video issues with the connected display. Because embedded audio is not passed to the display, the audio controls are disabled.

#### Color Format, Status

Use this control to override the color format as reported in the display's EDID. This can be useful for correcting displays with incorrect color format processing. The status text box indicates the current color format being sent to the display.

* Auto: (Default) The display's EDID and video resolution determine the color mode and data range (quantization).
* Force YCbCr 444: Change the output format to [YCbCr 4:4:4 You can force YCbCr 4:4:4 but not YCbCr 4:2:2. This is because NV-32-H outputs do not support YCbCr 4:2:2.](javascript:void(0)).
* Force RGB: Change the output format to RGB and use the HDMI defaults for setting the pixel data range (quantization).
* Force RGB Full Range: Change the output format to RGB data and full-range (0-255) component pixel values.
* Force RGB Limited Range: Change the output format to RGB data and limited-range (16-235) component pixel values.

**Note:** When the HDMI-DVI Status control is 'DVI' (either forced or auto-detected), the Color Format control is preset to 'Auto' and grayed out. (The output color format cannot be changed for DVI displays.)

The Color Format Status box indicates the color format being output to the display, RGB or YCbCr. Each color format has additional detected parameters:

* RGB indicates the supported pixel component quantization range, Full or Limited. For example: "RGB Limited"
* YCbCr indicates the supported color sub-sampling mode (444 or 422), color space (BT.601 or BT.709), and pixel component quantization range (Full or Limited). For example: "YCbCr 444 BT.709 Limited"

#### Aspect Ratio, Status

Select how the source content is shown on the HDMI display if the source and display's aspect ratio differ. The status text box indicates the video format aspect ratio being sent to the display â for example, "16:9".

* Maintain Aspect Ratio: (Default) The source content is scaled up or down to exactly match one dimension of the output resolution without cropping the other dimension. The resulting image is centered over a black background.
* Stretch to Fit: The source content is stretched or compressed to fit the aspect ratio of the display.
* 1:1 Pixel Mapping: The source content is not scaled, but is centered on the output display over a black background. If the source is smaller in any dimension, black bars appear around the image. If the source is larger, then the image is cropped to fit the display.

**Note:** The display may perform additional aspect ratio processing of the image. It may be necessary to adjust the display's aspect ratio settings.

### Audio

The HDMI Audio section of the control panel only appears when the Audio Source property is set to 'Selected Source' or 'Audio Input Pins':

* When set to 'Selected Source' (the default setting), eight channels are shown. However, only the number of supported channels (as dictated by the display's EDID) are active and the rest are disabled.
* When set to 'Audio Input Pins', the number of Audio Channels (as configured in Properties) determines how many channels are shown.

**Note:** If an HDMI source has fewer audio channels than the display supports, the display only receives the number of channels sent by the source.

#### Valid

LED glows green when the embedded audio for a channel is currently being sent to the display.

#### Peak Input Level (dBFS)

Indicates the peak level of the audio signal for each channel, from -120 to 20 dBFS.

#### Clip

LED indicates if the audio signal is being clipped.

#### Clip Hold

Click to hold the clip indication until you manually clear it.

#### Invert

Click to invert the polarity of the digital audio signal sent to the display.

#### Mute

Click to mute the digital audio signal sent to the display.

#### Gain

Click to adjust the gain of the audio signal sent to the display, from -100 dB to 20 dB (default is 0).

### CEC

**Note:** The CEC tab only appears when the CEC property is set to 'Enabled'.

#### Status

Displays the status of the CEC commands. Errors can include "Command not acknowledged" (if the last command was not properly received by the display) and "Compromised - The connected *NV Series device* does not support CEC".

#### On (One Touch Play)

Click to turn on the connected display via HDMI.

#### Off (Standby)

Click to turn off the connected display via HDMI.

#### Display Power Status

Indicates whether the connected display is on or off.

#### Polling Interval

Select how often to query the display's power status: 5 seconds (default), 10 seconds, or 30 seconds.

#### Up (Volume Up)

Increases the volume of the connected video source.

#### Down (Volume Down)

Decreases the volume of the connected video source.

#### Input 1-6

Selects the input of the connected video source.

#### Cmd 1-8

Leverages CEC commands to drive other system automation. Allows custom CEC commands to be sent from Generic HDMI Display component. Custom commands can be stored in the text box control and sent by clicking the trigger button. Commands must use colon separated format (Ex: 4F:82:20:00).

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Audio Channel *n* | | | | |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Gain | -100 to 20 | -100dB to 20dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  inverted | 0  1 | Input / Output |
| Level | -120 to 20 | -120dB to 20dB | 0.000 to 1.00 | Output |
| Mute | 0  1 | unmuted  muted | 0  1 | Input / Output |
| Valid | 0  1 | false  true | 0  1 | Output |
| CEC | | | | |
| Custom Command *n* | | | | |
| String | (text) | | | Input / Output |
| Trigger | (text) | | | Input / Output |
| Input *n* | (trigger) | | | Input / Output |
| One Touch Play | (trigger) | | | Input / Output |
| Polling Interval | - | 5 seconds  10 seconds  30 seconds | - | Input / Output |
| Power Status | 0  1 | false  true | 0  1 | Output |
| Standby | (trigger) | | | Input / Output |
| Status | (text) | | | Output |
| Volume Down | 0  1 | false  true | 0  1 | Input / Output |
| Volume Up | 0  1 | false  true | 0  1 | Input / Output |
| EDID | | | | |
| Audio Channels | (text) | | | Output |
| Name | (text) | | | Output |
| Save EDID | 0  1 | false  true | 0  1 | Input / Output |
| Serial Number | (text) | | | Output |
| HDMI AV Input | | | | |
| Aspect Ratio Mode | - | Maintain Aspect Ratio  Stretch to Fit  1:1 Pixel Mapping | - | Input / Output |
| Aspect Ratio Status | (text) | | | Output |
| Auto Power | 0  1 | false  true | 0  1 | Input / Output |
| Color Format | - | Auto  Force YCbCr 444  Force RGB  Force RGB Full Range  Force RGB Limited Range | - | Input / Output |
| Color Format Status | (text) | | | Output |
| Connected | 0  1 | false  true | 0  1 | Output |
| Enable | 0  1 | false  true | 0  1 | Input / Output |
| HDCP Encryption | 0  1 | false  true | 0  1 | Output |
| HDCP Mode | - | Auto  Off | - | Input / Output |
| HDCP Status | (text) | | | Output |
| HDMI-DVI Mode | - | Auto  Force DVI | - | Input / Output |
| HDMI-DVI Status | (text) | | | Output |
| Idle Mode | - | Idle Screen  Black Video  Graphic 1  Graphic 2  Graphic 3 | - | Input / Output |
| Idle State | 0  1 | false  true | 0  1 | Output |
| Idle Timer | - | 15s  30s  60s  120s | - | Input / Output |
| Idle Trigger | (trigger) | | | Input / Output |
| Sleep Mode | - | Disable HDMI  Idle Screen  Black Video  Graphic 1  Graphic 2  Graphic 3 | - | Input / Output |
| Sleep State | 0  1 | false  true | 0  1 | Output |
| Sleep Timer | - | 1s  5s  30s  1m  10m  30m  60m  8hr | - | Input / Output |
| Sleep Trigger | (trigger) | | | Input / Output |
| Video Format Mode | - | (Multiple - See control panel) | - | Input / Output |
| Video Format Status | (text) | | | Output |
| Video Freeze | 0  1 | false  true | 0  1 | Input / Output |
| Video Mute | 0  1 | false  true | 0  1 | Input / Output |
| Status | (text) | | | Output |

[Troubleshooting](javascript:void(0))

### Status: "Not Present - HDMI Disabled - Display status unknown"

If you see this status, check that the [HDMI Enable](#HDMI) control is toggled on.

### Display device doesn't acknowledge CEC commands

If you experience this issue, note the following:

* If you are sending CEC commands in rapid succession, try waiting a few seconds between commands. Some devices require a delay between commands.
* Some display devices require that the intended AV source device is the current, actively selected device shown on the display for CEC commands to be recognized.
* The display device might not be fully compatible with the CEC specification.
