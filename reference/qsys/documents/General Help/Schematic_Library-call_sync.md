# Call Sync

> Source: https://help.qsys.com/Content/Schematic_Library/call_sync.htm

# Call Sync

Use the Call Sync component to simplify the integration of Q-SYS collaboration devices and calling systems. It synchronizes mute state, call controls, and LED light behavior across multiple calling components, including USB HID Conferencing, Softphone, and POTS Controller.

[Device and Component Support](javascript:void(0))

Each Call Sync component supports connections from up to eight Call Systems to multiple Endpoints, with a single Call System being active at a time.

### Terminology

* A Call System is a Call Sync input having means within Q-SYS to establish and manage a call.
* An Endpoint is a Q-SYS device that is connected to the output of Call Sync and receives synchronized control updates (with other Endpoints) from Call Sync.
* An Active Call is a call that is not in the idle or on-hook state. Once a call is off-hook, or ringing, or any state that does not leave it idle or on-hook, the call is considered active. HID, Softphone, and POTS each have different terminology to describe hook state and call states, so for the purpose of discussing them together, the term "active call" is used in this topic.
* An Active Call System is a call system responsible for controlling and managing the active call, generally meaning the call system is off-hook or ringing from an incoming call.
* An Idle Call System is a call system that is not active, generally meaning that it is on-hook and not experiencing a ring event from an incoming call.

**Note:** Call Sync supports a single Active Call â from any connected supported Call System â at a time.

### Supported Call Systems

* [HID Conferencing](usb_telephony.htm)
* [Status/Control (Softphone)](Softphone.htm)
* [POTS Controller](pots_control_status.htm)

### Supported Endpoints

* [Control (NL-SB42, NM-T1)](lcqln_tym_control_panel.htm)
* [Lightbar (TSC-G3, PS-TSCG3 Series)](lightbar.htm)

[Enabling Call Sync](javascript:void(0))

To use a Call System component or Endpoint component with Call Sync:

1. Select the component in your design.
2. In Properties, set the Enable Call Sync property to 'Yes'.
3. Wire the Call System or Endpoint pin  to the Call Sync component.

[Inputs and Outputs](javascript:void(0))

#### Call System

Connect this input pin to a Call Sync output pin of a supported Call System. The number of Call System pins is determined by the Number of Call Systems property.

**Note:** Only one Call System can be active â i.e., have its call be active â at a time.

#### Endpoints

Connect this output pin to the Call Sync input pin of one or more supported Endpoints.

[Schematic Examples](javascript:void(0))

These examples demonstrate how Call Sync can receive call states (mute, ring, etc.) from one or more Call System components, including HID Conferencing, Softphone, and POTS Controller, and then synchronize those states to multiple devices (Endpoints). The designer can configure the LED colors and patterns to appear for those states, and then send them to the LED light bars on TSC-70-G3 and TSC-101-G3 touch panels, NL-SB42 soundbars, and the LED light ring on NM-T1 microphones. The LEDs of all Endpoints thus behave the same for call mute, ringing status, etc.

[Small room, single Call System](javascript:void(0))

In this example, a small huddle room contains an NM-T1 microphone, a TV with an NL-SB42 soundbar below it, and a TSC-70-G3 touch screen. Call Sync receives call states from a single Call System â in this case, [HID Conferencing](usb_telephony.htm) â and passes those states and their configured behaviors in sync to the Endpoints.

[Large room, multiple Call Systems, LED color customization](javascript:void(0))

This example features a larger conference room with three NM-T1 microphones and multiple Call Systems. In addition, [Color Picker](color_picker.htm) components have been configured to pass custom LED colors for Mute, Unmute, and Ringing states.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Call Sync Properties

#### Number of Call Systems

Specify how many input Call System pins to expose, from 0 to 8 (1 is default).

[Controls](javascript:void(0))

### Button Configuration

#### Mute Mode

Alters the microphone Mute button behavior.

**Toggle**: (Default) When a Mute button is pressed, it toggles between mute and unmute states.

**Note:**  Only Toggle is supported in conjunction with Call Sync. Additionally, if the Mute Button's Toggle control pin is used, the Mute Mode drop-down will be grayed out.

**PTT**: (Push to Talk) To unmute, press and hold the mic mute button.

**PTM**: (Push to Mute) To Mute, press and hold the mic mute button.

**Note:**  PTT (Push to Talk) and PTM (Push To Mute) are supported when using the NM-T1 without Call Sync, and when the Proximity Sensor > Link to Mute control is disabled.

#### Mute Control

This control determines whether audio is muted within the [Mic In (NM-T1)](microphone_beamformer_with_aec.htm) component.

**Local**: (Default) When set to local, any mute button press on the NM-T1 device or virtual mute buttons will cause the audio to be muted within the NM-T1 Mic In component.

**Remote**: When set to Remote and mute buttons are pressed, audio is not muted within the NM-T1 Mic In component. In this mode, the Mute State output control pin can be used to control muting in the Q-SYS design.

#### Mute

(NM-T1 Control component only) Mute or unmute audio within the NM-T1 Mic In component, depending on the Mute Control setting.

#### Mute Buttons

This control enables or disables the four Mute buttons on the NM-T1 device. When set to Disabled, the Mute button backlights on the control ring turn off. The default is Enabled.

#### Call Button

This control enables or disables the Call button on the NM-T1 device. When set to Disabled, the Call button backlight on the control ring turns off. The default is Disabled.

#### User Button

This control enables or disables the User button on the NM-T1 device. When set to Disabled, the User button backlight on the control ring turns off. The default is Disabled.

### Proximity Sensor

#### Sensitivity

(NM-T1 Control component only) This control sets the sensitivity of the NM-T1 proximity sensor: Low (default), Medium, or High.

#### Hold Time

(NM-T1 Control component only) This control sets the amount of time, from 1 to 5 seconds, that a user's hand must be within range of the proximity sensor to trigger a state change. The default is 1 second.

#### Sensor

This control enables or disables the proximity sensor on the NM-T1 device. The default is Disabled

#### Fuel Gauge

This control enables or disables the fuel gauge pattern when the proximity sensor is activated on the NM-T1 device. The default is Enabled.

#### Link to Mute

When enabled, a proximity sensor event will toggle the mute state of the NM-T1 microphone. The default is Enabled.

### Call Control

#### Call Accept

Triggers the active call to be accepted and taken Off Hook.

#### Call Decline

Triggers the active call to be declined and forced On Hook.

#### Mute

Toggles the mute state for all Call Sync-connected devices and components.

#### Off Hook

LED indicates the connected calling system is Off Hook.

#### Ring

LED indicates the connected calling system is ringing.

#### Idle Options

For a full description, see below.

* Show Mute - When Show Mute is selected, the mute status is shown instead of the Idle Mode color during Idle Mode. This is the default option.* Flash on Mute - When you pres the mute button while in Idle Mode, the ring will flash quickly 3 times with the assigned Mute / Unmute state color. When the flashing is complete, it will return to the assigned Idle Mode color.
  * Ignore Mute - When Ignore Mute is selected, the mic buttons pressed are ignored when the system is in Idle state.

### LED Configuration

Use this section to configure the Unmute, Mute, Ringing, and Idle states of supported Q-SYS collaboration Endpoints with integrated LEDs and how those states are indicated to the user on the LED light bar or ring.

**Tip:** When connected to a running system, any change to the color, pattern, or speed controls will preview the combination for 5 seconds regardless of the current state of the Endpoint.

#### Light Ring / Light Bar States

The corresponding LED will light up when the Unmute, Mute, Ringing, and Idle states are changed. These states are managed automatically when used in conjunction with Call Sync. When Mute Control is configured for Remote mode, the system designer may override the LED states directly using the Idle State LED control pins.

Unmute - Device is in an unmuted state

Mute - Device is in a muted state

Ringing - Device is in ringing state

Idle - This functionality only applies when the mic is using Call Sync. The virtual mute button of the NM-T1 follows the behavior defined for the physical buttons in the Idle mode options. For other devices connected to Call Sync (NL-SB42 and TSCs), their LEDs will mirror the NM-T1 when you are operating the NM-T1 mute button as described for Idle Mode.

* Show Mute - When Show Mute is selected, the mute status is shown instead of the Idle Mode color during Idle Mode. This is the default option.
* Flash on Mute - When you pres the mute button while in Idle Mode, the ring will flash quickly 3 times with the assigned Mute / Unmute state color. When the flashing is complete, it will return to the assigned Idle Mode color.
* Ignore Mute - When Ignore Mute is selected, the mic buttons pressed are ignored when the system is in Idle state.

#### Color

For each state, select what color appears in the light bar or light ring:

* <Color Name>: Select from 16 color names in the list.
* Off: The LED will turn off for this state.
* Custom: For greater color capability, wire a [Color Picker](color_picker.htm) component to the Color input control pin for each state.

#### Pattern

For each state, select a pattern for LED colors to appear: Breathing, Chasing, Chasing w/Tails, Flashing, or Solid (default).

#### Speed

For each state, select the speed of the selected pattern animation: Slow, Standard, Fast, or None.

#### User Button Color

Similar to the Color control for call states, you can also configure the color for the NM-T1 User button.

#### LED Brightness

Select the brightness level of the light bar or ring, from 1 (dimmest) to 10 (brightest). The default is 5. On the NM-T1, this also adjusts the brightness of the Mute, Call, and User button backlights.

[Control Pins](javascript:void(0))

**Note:** Available control pins depend on the component: NL-SB42 Control, NM-T1 Control, or Call Sync.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Idle State | | | | |
| Active | 0  1 | false  true | 0  1 | [Output Changed from Input / Output to Output only in Q-SYS Designer 9.9.0 to improve customizability.](javascript:void(0)) |
| Color | - | [Color List Aquamarine, Blue, Blue Violet, Coral, Custom, Cyan, Green, Green Yellow, Lime, Magenta, Off, Orange, Orchid, Pink, Red, Sky Blue, White, Yellow](javascript:void(0)) | - | Input/Output |
| Pattern | - | Solid  Flashing  Breathing  Chasing  Chasing with Tails | - | Input/Output |
| RGB | - | #*nnnnnn* | - | Input/Output |
| Speed | - | Slow  Standard  Fast  None | - | Input/Output |
| Mute Buttons | | | | |
| Control | - | Local  Remote | - | Input/Output |
| Enable | 0  1 | false  true | 0  1 | Input/Output |
| Mode | - | Toggle  PTT  PTM | - | Input/Output |
| State | 0  1 | false  true | 0  1 | Output |
| Toggle | 0  1 | false  true | 0  1 | Input |
| Mute State | | | | |
| Active | 0  1 | false  true | 0  1 | Output |
| Color | - | [Color List Aquamarine Blue Blue Violet Coral Custom Cyan Green Green Yellow Lime Magenta Off Orange Orchid Pink Red Sky Blue White Yellow](javascript:void(0)) | - | Input/Output |
| Pattern | - | Solid  Flashing  Breathing  Chasing  Chasing with Tails | - | Input/Output |
| RGB | - | #*nnnnnn* | - | Input/Output |
| Speed | - | Slow  Standard  Fast  None | - | Input/Output |
| Proximity Sensor | | | | |
| Enable | 0  1 | false  true | 0  1 | Input/Output |
| Fuel Gauge Enable | 0  1 | false  true | 0  1 | Input/Output |
| Fuel Gauge State | 0  1 | false  true | 0  1 | Input/Output |
| Mute Link Enable | 0  1 | false  true | 0  1 | Input/Output |
| Trigger | (trigger) | | | Output |
| Ringing State | | | | |
| Active | 0  1 | false  true | 0  1 | Input/Output |
| Color | - | [Color List Aquamarine Blue Blue Violet Coral Custom Cyan Green Green Yellow Lime Magenta Off Orange Orchid Pink Red Sky Blue White Yellow](javascript:void(0)) | - | Input/Output |
| Pattern | - | Solid  Flashing  Breathing  Chasing  Chasing with Tails | - | Input/Output |
| RGB | - | #*nnnnnn* | - | Input/Output |
| Speed | - | Slow  Standard  Fast  None | - | Input/Output |
| Unmute State | | | | |
| Active | 0  1 | false  true | 0  1 | Input/Output |
| Color | - | [Color List Aquamarine Blue Blue Violet Coral Custom Cyan Green Green Yellow Lime Magenta Off Orange Orchid Pink Red Sky Blue White Yellow](javascript:void(0)) | - | Input/Output |
| Pattern | - | Solid  Flashing  Breathing  Chasing  Chasing with Tails | - | Input/Output |
| RGB | - | #*nnnnnn* | - | Input/Output |
| Speed | - | Slow  Standard  Fast  None | - | Input/Output |
| User Button | | | | |
| Color | - | [Color List Aquamarine Blue Blue Violet Coral Custom Cyan Green Green Yellow Lime Magenta Off Orange Orchid Pink Red Sky Blue White Yellow](javascript:void(0)) | - | Input/Output |
| Enable | 0  1 | false  true | 0  1 | Input/Output |
| RGB | - | #*nnnnnn* | - | Input/Output |
| State | 0  1 | false  true | 0  1 | Output |
| Trigger | (trigger) | | | Input/Output |
| Call Accept  (Call Sync) | (trigger) | | | Input/Output |
| Call Button Enable | 0  1 | false  true | 0  1 | Input/Output |
| Call Decline | (trigger) | | | Input/Output |
| Call Button State | 0  1 | false  true | 0  1 | Output |
| Call Button Trigger | (trigger) | | | Input/Output |
| Hold Time | 1-5 | 1-5 | 0.00 to 1.00 | Input/Output |
| LED Brightness | 1 to 10 | 1 to 10 | 0.00 to 1.00 | Input/Output |
| LED Color | - | #*nnnnnn* | - | Output |
| LED Off Hook  (Call Sync) | 0  1 | false  true | 0  1 | Output |
| LED Ring  (Call Sync) | 0  1 | false  true | 0  1 | Output |
| Mute  (NM-T1 Control) | (trigger) | | | Input/Output |
| Mute  (Call Sync) | 0  1 | unmuted  muted | 0  1 | Input/Output |
| Sensitivity | - | Low  Medium  High | - | Input/Output |
