# Automatic Camera Preset Recall (Q-SYS VisionSuite Plugin)

> Source: https://help.qsys.com/Content/VisionSuite/VisionSuite_ACPR.htm

# Automatic Camera Preset Recall (Q-SYS VisionSuite Plugin)

Use the Automatic Camera Preset Recall (ACPR) plugin to configure camera position preset recall for conferencing solutions using the Sennheiser TCC2 and TCCM, Shure MXA920, Audio-Technica ATND1061, Yamaha RM-CG, CQ-SYS NM-T1, or with discreet, individual microphones.

**Note:** Sample designs included with the ACPR plugin feature all mic types and signal wiring that meets the design requirements mentioned in this topic. Additionally, the sample design includes signal wiring for discreet microphones with multiple channels.

[Compatibility](javascript:void(0))

* Designer: This Version of the plugin was developed and tested with Q-SYS Designer Software version 9.10.
* Cameras: The plugin supports up to sixteen QSC NC-IP Conference Cameras. Third-party cameras are not supported.
* Microphones: The plugin supports up to ten Sennheiser TCC2 or TCCM microphones, ten Shure MXA920 microphones, ten Audio Technica ATND1061 Microphones, ten Yamaha RM-CG Microphones, 16 Q-SYS NM-T1 microphones or 90 channels of individual microphones.

**Note:** When using the Audiotechnica ATND1061, make sure to enable "Camera Control Notification" in the network settings.

[Design Requirements](javascript:void(0))

Follow these requirements when configuring your design.

**Tip:** Refer to the ACPR sample designs for examples of these requirements. We recommend using the sample designs as the basis for your design. Go to File > Open Sample Design and select "Automatic Camera Preset Recall\_vX.X \_Your Microphone Type\_.qsys".

* Script Access on Components: The plugin requires that any cameras, Mediacast Routers, and the NM-T1 input components are named. This allows the ACPR plugin to access the controls in these components. To name a component, select it and change the Script Access in the Properties to "Script" or "All".
* Mediacast Router: Your design must include a Mediacast Router component, even if you are only using a single camera. Select the Script Access enabled Mediacast Router from the Mediacast Router control. See [Controls](#Controls) for more information.
* Microphone Signal: The plugin requires wiring from an audio input so that it knows when someone is speaking in the room. We recommend that you take the signal from your audio path pre-mixing and AEC.
* Far End Speaker Signal: The plugin also requires wiring from the far end audio so that it knows when the far end is speaking. We recommend that you take the signal from your audio path just before connection to the speakers.

[Configuration Overview](javascript:void(0))

1. In your design, drag the Automatic Camera Preset Recall plugin into the schematic. Or, use the ACPR sample design as a starting point, which already includes the plugin (recommended). Refer to [Design Requirements](#Design) for more information.
2. Configure the ACPR plugin Properties to suit your room. See [Properties](#Properti).
3. Double-click the ACPR plugin to open its control panel.
4. Configure the ACPR plugin controls. See [Controls](#Controls).
5. Run your design. Select File > Save to Core & Run or press F5.

[Properties](javascript:void(0))

### ACPR Properties

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Is Managed

When set to 'Yes', this adds the plugin to your Inventory list, which makes the plugin's Status available for monitoring locally in Core Manager and remotely in Q-SYS Reflect (with a subscription). Status changes (for example, 'OK' to 'FAULT') generate alerts that are displayed in the Event Log.

#### Mode

Set the type of microphone to use, either the Sennheiser TCC2, Sennheiser TCCM, Discrete Mics, NM-T1, Audio Technica ATND1061, Shure MXA920, or Yamaha RM-CG. Refer to the [Compatibility](#Compatib) section for limitations.

#### Microphones

This property is visible only when you have selected any microphone Type other than Discrete or NM-T1. Set how many microphones to use in the room, from 1-10.

#### High Reporting

Available if the selected microphone is a Shure MXA920 or MXA901. This will increase the frequency of positions reported by the microphone.

**Note:** This setting should only be used if the talkers are not reliably detected.

#### Camera Zone Mode

This property is visible only when you have selected Audio-Technica ATND1061 as the Mode. This will allow to use the Camera Zones configured in the Audio-Technica Digital Microphone Manager

#### NM-T1 Count

This property is visible only when you have selected Q-SYS NM-T1 as the Type. Set how many microphones to use in the room, from 1-16.

#### Channels

This property is visible only when you have selected discrete Mics as the Type. Set how many microphones to use in the room, from 10-90.

#### Cameras

If 8 primary cameras are not enough for your use case you can increase the count up to 16.

#### Seervision Integration

Enable to combine ACPR with Seervision Presenter Tracking. Requires Designer 9.10 or higher. Align ACPR Version with SV Plugin Version.

#### SV Plugin Code Name

Only visible if the Seervision Integration property is set to Yes. Enter the code name of the Seervision Plugin for it to show up in the mediacast router selection. Make sure the SV plugin has script access enabled.

#### Camera Preview

Enables the Preview of the currently active camera directly in ACPR. Requires Designer 9.9 or higher.

#### Auto Framing Support

Exposes controls for auto framing settings per zone. When enabled it will toggle all connected cameras into analytics mode via the face count function. Requires Designer 9.10 or higher.

#### Reinforcement Microphones

Reinforcement microphones enable the use of discrete mics alongside beamforming mics within the same plugin for the same cameras.

#### Room Size Units

Choose how to display the room size. Choices are Imperial or Metric units.

#### Room Width

Set the room width size. Will display Imperial or Metric units, depending on choice of Room Size Units.

#### Room Length

Set the room length size. Will display Imperial or Metric units, depending on choice of Room Size Units.

#### Show Debug

Select 'Yes' to show the Debug Output window. For details, see the Debug Output topic in the Q-SYS Help.

[Controls](javascript:void(0))

[Setup Tab](javascript:void(0))

#### Bypass Auto Recall On/Off

Enable or disable camera tracking. Auto = not bypassed.

#### Global Status

Displays a combined state of the microphones and ACPR Setup.

### Global Camera Setup

#### Number of Cameras (1-8)

Specify the number of cameras in your design. The plugin supports up to eight cameras.

**Note:** Wire the cameras to the Mediacast Router with their corresponding numbers. For example, Primary Camera 4 = Camera 4 > Mediacast Router Input 4. Secondary Camera 4 = Camera 12 > Mediacast Router Input 12.This also stays true if more than 8 cameras are used.

#### Primary Camera 1-8

In the drop-down menu for each camera, select a camera name.

#### Home Position Masking

(Optional - the row between Primary and Secondary cameras) If enabled any time the primary or secondary camera has to move the home position will be briefly shown. This requires a camera staying in Home Position as it's only switching mediacast stream. Most useful when no secondary camera is available to hide movement.

#### Secondary Camera 1-8

(Optional) In the drop-down menu for each camera, select a camera name. This camera acts as backup camera to the primary camera and will take over whenever the primary camera's image is already active. This way, the backup camera moves to the new position before the Mediacast Router switches to it, thus hiding any camera movement in the image. The secondary camera always belongs to the set Primary Camera.

#### Mediacast Router

For the plugin to function, you must select a Mediacast Router here. Also, make sure to enable Script Access on the component. ACPR can only control one output at a time.

**Note:** The plugin supports a single Mediacast Router. If you need more routing, you must drag in another instance of the plugin.

**Note:** If Seervision Integration is selected the reference Seervision Plugin will show up instead of media cast routers.

#### PTZ Switch Delay

Set the length of time a signal needs to be present before a zone is triggered, from 1 to 5 seconds. Adjusting this control can help mitigate rapid switching when a call contains a high volume of crosstalk.

### Default Home Position

The Default Home Position feature enables you to set a default camera and home position that can be used in multiple circumstances, such as when the far end talks for a long time, if the meeting is more discussion-based versus lead by an individual, or when there is an extended period of silence.

#### Auto/Off

Click to bypass the default home position. Cameras will then remain in the last triggered zone. (Default is not bypassed.)

#### Camera

Select your default camera. Only primary cameras can be selected.

#### Primary Position

Sets the position of the default camera. To set the position:

1. Double-click camera component to open its control panel.
2. Use the PTZ controls to set a position.
3. In the ACPR plugin, click the Save button. The position coordinates then populate in the Position box.

#### Secondary Position

Identical functionality as the Primary Position control but for the secondary camera instead. If the primary camera has no secondary camera assigned, then the controls are disabled.

#### Save

Click to save the current position of the selected camera.

**Note:** The Position box does not live-update with the current position of the selected camera. It only updates when you click Save.

#### Load

Click to load the currently saved position of the selected camera.

#### Crosstalk Detection

Set the rate at which the plugin sets the default camera to the home position when several people are talking at once: None, Slow, Medium, Fast or Custom. If Custom is used, the parameters are set on the Expert Control page. If crosstalk has been detected, the LED turns on. When this occurs, preset recalling will not happen.

[Microphone *n* Tab](javascript:void(0))

#### PTZ Controls

Control the currently routed Camera directly from the ACPR Plugin when setting up presets.

#### Camera Preview

Displays the same JPEG preview like in the camera block. The currently selected camera will be displayed.

#### IP Address

Enter the IP Address of the Sennheiser TCC2 or TCCM, Shure MXA920, Yamaha RM-CG or the Multicast IP Address that the Audio Technica ATND1061 sends its data.

**Note:** When using the Audio Technica ATND1061, every multicast address must be unique.

#### Port

Only visible if the Mode Property is set to Audio Technica ATND1061. Enter the port where the Audio Technica ATND1061 sends its data to.

**Note:** When using the Audio Technica ATND1061, every port has to be unique.

#### Horizontal Angle

Displays the current horizontal angle from the angle-based microphone. This is the primary value of the microphone that the ACPR plugin uses to determine which zone to activate.

#### Vertical Angle

Displays the current vertical angle from the angle-based microphone. This is the secondary value of the microphone that the ACPR plugin uses to determine which zone to activate.

#### Global Status

Displays a combined state of the microphones and ACPR Setup.

#### Mic Status

Displays the status of the selected microphone.

#### Bypass Auto Recall On/Off

Enable or disable microphone tracking. Auto = not bypassed.

#### Local Mic Signal

LED glows red if there is an active signal being picked up locally by the microphone.

#### Mic Detected

Only visible with Discrete Mics and NM-T1. Shows the current channel of the auto mic mixer that is recognized as open.

#### Far End Talker Signal

LED glows red if there is an active signal from the far end.

#### Use HVAD

Only visible with Yamaha RM-CG. Activate to only switch presets when human voice is detected.

#### HVAD State

Only visible with Yamaha RM-CG. Displays the current state of human voice detection by the microphone. If HVAD use is active this has to be true in addition to Local Mic Signal for a preset to switch.

### Zone Setup

#### Zone Enable

Enables or disables the zone.

#### Zone *n* HA/VA Angles

**Note:** When configuring zone angles in the ACPR plugin, specifically HA/VA angles, ensure that only whole numbers are used. Decimals are not allowed and will cause errors in the system.

Set the boundaries of the zone, which requires both the entry and exit boundary. For example, you might have a zone that starts at 15 degrees and ends at 149. Thus, the control value would be â15 149â. You can separate boundaries with either a space, hyphen, or comma.

#### Zone *n* Active

LED glows red when a speaker gets recognized in the zone.

#### Zone *n* Camera

Set the respective primary camera for that zone. If you have multiple cameras, you would simply assign different cameras to different zones.

#### Zone *n* Primary Position

Set the PTZ coordinates for this zone. Similar to the Default Home Position, this control tracks the PTZ coordinates of the selected camera, but will only adapt the values once you save them.

#### Zone *n* Secondary Position

Identical functionality as the Zone *n* Primary Position control but for the secondary camera if one is selected. If no secondary camera is selected, this control is disabled.

#### Zone *n* Primary Save

Manually save the PTZ coordinates for the selected primary camera.

#### Zone *n* Secondary Save

Manually save the PTZ coordinates for the selected secondary camera if one is selected. If no secondary camera is selected, this control is disabled.

#### Zone *n* Primary Load

Manually recall the PTZ coordinates to the saved values for the selected primary camera.

#### Zone *n* Secondary Load

Manually recall the PTZ coordinates to the saved values for the selected secondary camera.

#### Zone *n* Priority Switch

The default behavior will always try to recall the primary position. If this control is true ACPR will try to recall the secondary position if possible instead of the primary.

#### Zone *n* Auto Framing Enable

Only visible when auto framing integration is enabled. Turns on auto framing upon recall of the preset.

#### Zone *n* Auto Framing Wait for Framing

Only visible when auto framing integration is enabled. Wait for the camera to finish auto framing after physical movement before switching the media cast stream to it. Maximum wait is 2 seconds.

#### Zone *n* Auto Framing Transition Speed

Only visible when auto framing integration is enabled. Sets the transition speed of auto framing on preset lead.

#### Zone *n* Auto Framing Padding

Only visible when auto framing integration is enabled. Sets the Padding of auto framing on preset load.

#### Zone *n* Auto Framing Deadband

Only visible when auto framing integration is enabled. Sets the Deadband of auto framing on preset load.

[NM-T1 *n* Tab](javascript:void(0))

These options are only present when the NM-T1 Microphone is the selected Mode.

#### Choose your NM-T1

Select the NM-T1 input component that has Script Access enabled.

#### Mic Detected

Shows the current channel of the auto mic mixer that is recognized as open.

#### Far End Talker Signal

LED glows red if there is an active signal from the far end.

#### PTZ Controls

Control the currently routed Camera directly from the ACPR plugin when setting up presets.

#### Camera Preview

Displays the same JPEG preview like in the camera block. The currently selected camera will be displayed.

### Zone Setup

#### Zone *n* ID

Press to flash the light on the NM-T1 identifying what position this zone has at the NM-T1.

#### Zone Enable

Enables or disables the zone.

#### Zone *n* Active

LED glows red when a speaker gets recognized in the zone.

#### Zone *n* Camera

Set the respective primary camera for that zone. If you have multiple cameras, you would simply assign different cameras to different zones.

#### Zone *n* Primary Position

Set the PTZ coordinates for this zone. Similar to the Default Home Position, this control tracks the PTZ coordinates of the selected camera, but will only adapt the values once you save them.

#### Zone *n* Secondary Position

Identical functionality as the Zone *n* Primary Position control but for the secondary camera if one is selected. If no secondary camera is selected, this control is disabled.

#### Zone *n* Primary Save

Manually save the PTZ coordinates for the selected primary camera.

#### Zone *n* Secondary Save

Manually save the PTZ coordinates for the selected secondary camera if one is selected. If no secondary camera is selected, this control is disabled.

#### Zone *n* Primary Load

Manually recall the PTZ coordinates to the saved values for the selected primary camera.

#### Zone *n* Secondary Load

Manually recall the PTZ coordinates to the saved values for the selected secondary camera.

#### Zone *n* Priority Switch

The default behavior will always try to recall the primary position. If this control is true ACPR will try to recall the secondary position if possible instead of the primary.

#### Zone *n* Auto Framing Enable

Only visible when auto framing integration is enabled. Turns on auto framing upon recall of the preset.

#### Zone *n* Auto Framing Wait for Framing

Only visible when auto framing integration is enabled. Wait for the camera to finish auto framing after physical movement before switching the media cast stream to it. Maximum wait is 2 seconds.

#### Zone *n* Auto Framing Transition Speed

Only visible when auto framing integration is enabled. Sets the transition speed of auto framing on preset lead.

#### Zone *n* Auto Framing Padding

Only visible when auto framing integration is enabled. Sets the Padding of auto framing on preset load.

#### Zone *n* Auto Framing Deadband

Only visible when auto framing integration is enabled. Sets the Deadband of auto framing on preset load.

[Expert Controls](javascript:void(0))

#### Silence Home Position Trigger Time

This is the time, in seconds, that there must be silence on the local mic and local speakers until a home position call gets executed. The range is 1 to 15. The control background is a meter to indicate how close the detected level is to the threshold.

#### Far End Home Position Trigger Time

This is the time, in seconds, that there must be audio on the local speakers until a home position call gets executed. The range is 1 to 15. The control background is a meter to indicate how close the detected level is to the threshold.

#### Outside Zone Home Position Trigger Time

This is the time, in seconds, that there must be someone speaking outside a defined zone until a home position call gets executed. The range is 1 to 15. The control background is a meter to indicate how close the detected level is to the threshold.

#### Crosstalk Trigger Custom Level

If the preset on the Setup page is set to 'Custom', this is the threshold at which the Crosstalk gets called. The range is 0 to 1.00. The control background is a meter to indicate how close the detected level is to the threshold.

#### Crosstalk Reset Custom Time

This is the minimum time, in seconds, for how long the camera will stay in the home position after a crosstalk event has been triggered. The range is 1.00 to 15.0.

#### Mic Detection Threshold

Sets the Threshold microphone signals have the be above the noise floor to be detected as valid. Lower value means quicker detection but more errors.

#### Far End Detection Threshold

Sets the Threshold far end audio signals have the be above the noise floor to be detected as valid. Lower value means quicker detection but more errors.

#### Zone Hysteresis

This setting allows an error margin for each angle based zone. If for example set to 5 a new zone will only be recalled when the angle of the microphone is delta 5 degree to the current zones.

#### Home Position Masking Time

When Home Position Masking is enabled in the setup page this setting will define how long the home position will be seen minimum before switching back.

#### Camera Recalibration

Ensures that camera presets accurately align with participantsâ positions by using audio data from in-room microphones. The **Recalibrate Now** button initiates an immediate recalibration of the camera presets. The **Recalibrating** LED will light up while recalibration is taking place.

#### Load Settings from other ACPR Plugin

Enter the Script Access name of another ACPR plugin and press Copy to transfer all settings to your plugin.

[Troubleshooting](javascript:void(0))

### Zone *n* HA/VA errors

Solution: Ensure that only whole numbers are used. Decimals are not allowed and will cause errors in the system.

### Camera and Mediacast Router drop-down menus are blank

Solution: Ensure that all PTZ Camera and Mediacast Router components have Script Access enabled (set to 'All') and that the components are named in your design: select each component and type a custom name. Refer to [Design Requirements](#Design).

### Angles are just a single value rather than a range

Solution: Ensure that the angles are always a range. Smaller value first for normal range. Larger value first for range crossing 360/0Â° Axis.

### Incomplete zone setup

Solution: All Controls of a zone except the secondary position need to be defined for it to be taken into account.
