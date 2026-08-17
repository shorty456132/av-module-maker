# Mic/Control (Page Station)

> Source: https://help.qsys.com/Content/Schematic_Library/page_station_hardware_mic_control.htm

# Mic/Control (Page Station)

The Page Station Mic/Control component provides the signal pins to virtually connect the physical Page Station to the PA Router. You must add a Page Station Mic/Control component to your Q-SYS design, and wire it to the PA Router, for each physical Page Station in your system. The Page Station Mic/Control component enables you to control and monitor both digital and analog audio levels.

In order to compile a Q-SYS design containing a Page Station component, you must have a [PA Router](page_system.htm) component in the design.

[Inputs and Outputs](javascript:void(0))

### Inputs

The Page Station component has no inputs. All the inputs are on the physical hardware.

### Outputs

**Microphone** - The audio output from the physical hardware is routed over the **Q-LAN** network to the **Q-SYS Core** and to the Page Station Mic/Control component. The Microphone output of the Page Station Mic/Control component is wired to one of the **PA Router**'s audio inputs. Audio Outputs represented by a  circle, and traditional wiring is represented by a thin black line.

**Station Control** - Control signals are routed over the Q-LAN network to the Q-SYS Core and to the Page Station Mic/Control component. Control signals are sent by pressing one of the buttons on the physical hardware or keying the microphone. The Station Control pin is wired to one of the PA Router's Station Control inputs. The pin is represented by a down-pointing  triangle.

[Properties](javascript:void(0))

### Page Station Properties

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Is Paging Station

(PS-TSCG3 Page Station only)

When set to Yes (default) is selected, Q-SYS recognizes the Paging Station component as a paging station. If set to No, the component is removed from Designer.

#### Orientation

Select the orientation to match the touchscreen physical installation. To prevent the need of reinstalling the unit, you can select one of the "flipped" orientations.

**Note:** When installing a touchscreen in portrait orientation, the Orientation property in the touchscreen Status/Control component and the [User Control Interface (UCI) Design Overview](user_control_interface.htm#Web_Control_Interface_Properties) must both be set to 'Portrait'.

#### UCI Assignment

The choices are Static, only the specified UCI is used, and Dynamic you can select the UCI when the UCI is running.

#### UCI

This field can be edited only when the UCI Assignment is set to Dynamic. With the UCI Assignment set to Static, the name of the assigned UCI displays in this field, but cannot be changed.

Use the pull-down list to select the UCI assigned to this TSC component.

#### Hide Zone Buttons

Hides or displays the individual Zone Select buttons. You can use only Select All or Clear if this is set to Yes. Default is No.

#### Command Button Count

Sets the number of Command buttons available in the Virtual Page Station control panel, from 0 to 26 (default is 0).

#### Zone Group Count

Controls how many Zone Groups the page station will have, from 0 to 100 (default is 4).

#### Remote Zone Group Count

Specifies the number of Remote one Groups available in the PS-TSCG3 Mic / Control component. Each group corresponds to a Remote Destination Tag configured in Q-SYS Administrator. Setting this property to a non-zero value enables the creation of dedicated buttons in the touchscreen UI. Each button can trigger paging to a specific group of remote zones, allowing simplified cross-core paging.

From the PS-TSCG3 Properties window, setting the Remote Zone Group Count to 3 for example, will display three buttons labeledâGroup 1, Group 2, and Group 3. These buttons can be mapped to Remote Destination Tags such as Poolside Patios, Lobbies, or Conference Ballrooms.

**Tip:** Ensure the PA Router has a non-zero Remote Destination Count and Remote Destination Tags are properly configured in Q-SYS Administrator. Button labels can be customized using UCI Design Tools.

#### Talk Button Latches

Determines the behavior of the Talk button:

* When set to Yes, a quick press of the Talk button will start the page and latch the button to the on position. A second quick press will unlatch the button and stop the page.
* When set to No (default), you must always press and hold the Talk button to open the microphone.

**Note:** When set to Yes, a long press is interpreted as press-and-hold-to-talk, and the page ends when the button is released. The difference between what is a "quick" and "long" press is determined by the Delay control. See the [Mic/Control (Page Station)](#Controls) section for more information.

**Tip:** The **Talk button Latch** operation only works for the button and not the control pin; however, you can use a Flip-Flop component to control the Talk pin. For more information, see [Mic/Control (Page Station)](#Using_Talk_Control_Pin).

#### PTT Button Latches

Determines the behavior of the Push-To-Talk (PTT) button:

* When set to Yes, a quick press of the PTT button will start the page and latch the button to the on position. A second quick press will unlatch the button and stop the page.
* When set to No (default), you must always press and hold the PTT button to open the microphone.

[Controls](javascript:void(0))

## Paging Control

These [Controls](page_station_zone_select.htm#Controls) are the same found in the Virtual Page Station topic.

## Microphone

### Input

#### Peak Input Level (dBFS)

Graphic display of the **Mic** input indicating the peak analog input level.

#### Invert

Inverts the input signal for the Input channel. The signal is inverted for all Output channels.

#### Mute

Mutes the input signal for the Input channel. The signal is muted for all Output channels.

#### Gain

The Fader adjusts the gain of the signal for the Input channel. The gain of the Input channel is adjusted for all Output channels.

### Status

#### Connected

LED indicates whether a connection to the microphone is present.

#### Fault

LED indicates a connected microphone is present but failing.

### Digital

#### Invert

Toggle button to invert the digital output of the Input components.

#### Mute

Mutes the output signal.

#### Gain

Sets the gain of the output signal.

[Page Station Controls](javascript:void(0))

**Note:** These controls are exclusive to the PS-1600 and PS-1650.

### Analog

#### Peak Input Level (dBFS)

Graphic display of the **Mic** input indicating the peak analog input level.

#### Clip

Red LED indicating if the signal is being clipped.

#### Clip Hold

Holds the clip indication until manually cleared.

#### Max RMS Input Level (dBu)

Controls the Maximum RMS Input level for the **Mic** input.

### Digital

#### Invert

Inverts the input or output signal.

#### Mute

Mutes the input or output signal.

#### Gain

Sets the gain of the input or output signal.

[PS-TSCG3 Page Station Controls](javascript:void(0))

**Note:** These controls are exclusive to the PS-TSCG3 Page Station.

## Paging Control

These [Controls](page_station_zone_select.htm#Controls) are the same found in the Virtual Page Station topic.

## Microphone

### Input

#### Peak Input Level (dBFS)

Graphic display of the **Mic** input indicating the peak analog input level.

#### Invert

Inverts the input signal for the Input channel. The signal is inverted for all Output channels.

#### Mute

Mutes the input signal for the Input channel. The signal is muted for all Output channels.

#### Gain

The Fader adjusts the gain of the signal for the Input channel. The gain of the Input channel is adjusted for all Output channels.

### Status

#### Connected

LED indicates whether a connection to the microphone is present.

#### Fault

LED indicates a connected microphone is present but failing.

### Digital

#### Invert

Toggle button to invert the digital output of the Input components.

#### Mute

Mutes the output signal.

#### Gain

Sets the gain of the output signal.

[Control Pins](javascript:void(0))

[Page Station Control Pins](javascript:void(0))

**Note:** These control pins are exclusive to the PS-1600 and PS-1650.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Max RMS Input Level | 12.0 to -56 | 12.0 to -56 | 0 to .988 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Peak Input Level  (dBFS) | -120 to 20 | -120 dB to 20 dB | 0.000 to 1.00 | Output |
| Select A | trigger | | | Input |
| Select B | trigger | | | Input |
| Select C | trigger | | | Input |
| Select D | trigger | | | Input |
| Translation | trigger | | | Input / Output |

[PS-TSCG3 Page Station Control Pins](javascript:void(0))

**Note:** These control pins are exclusive to the PS-TSCG3 Page Station.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Channel 1 | | | | |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Mute | 0  1 | unmuted  mute | 0  1 | Input / Output |
| Peak Input Level | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Command Key A-H | 0  1 | false  true | 0  1 | Input / Output |
| Command Key Busy A-H | 0  1 | false  true | 0  1 | Output |
| Command Key Ready D-H | 0  1 | false  true | 0  1 | Output |
| Group Active (1-*n*) [1](#Group_Indicators) | 0  1 | false  true | 0  1.00 | Output |
| Group Match (1-*n*) [1](#Group_Indicators) | 0  1 | false  true | 0  1.00 | Output |
| Group Select (1-*n*) [1](#Group_Indicators) | trigger button | | | Input |
| Group Tag (1-*n*) | user-defined string | | | Input / Output |
| *Robot* Cancel | trigger button | | | Input / Output |
| Active Device | 0  1 | false  true | 0  1 | Output |
| Ad Hoc | (trigger) | | | Input / Output |
| Archive | 0  1 | off  on | 0  1.00 | Input / Output |
| Busy | 0  1 | false  true | 0  1.00 | Output |
| Cancel | trigger button | | | Input / Output |
| Clear All | trigger button | | | Input / Output |
| Connected | 0  1 | false  true | 0  1 | Output |
| Delay | 0.000 to 60.0 | 0 ms to 60.0 s | 0.000 to 1.00 | Input / Output |
| Fault |  |  |  |  |
| Max Page Duration | 0 to 3600 | 0 seconds to 3600 seconds | 0  1.00 | Input / Output |
| Message (file) | The user-defined text string identifying message files. The filename does not need the file-type extension in this field. | | | Input / Output |
| Mode  case sensitive text input | System-defined case-sensitive text string:  Live  Auto  Delay  Message | | | Input / Output |
| Preamble (file) | The user-defined text string identifying preamble files. The filename does not contain/need the file-type extension in this field. | | | Input / Output |
| Preamble Directory | The case-sensitive name of the directory where the Preamble (file) is stored.  The default directory name is Preamble, indicated by a blank.  Use "/" forward slashes between directories.  **Note:** You must have the correct type of audio files present in a directory to access it. | | | Input / Output |
| Priority | 1 - *n* | User-defined text name of the Priority. The numeric values associated with the Priorities depend on how many Priorities you set, and their order. | 1 - 1.00 | Input / Output |
| PTT Button | (trigger button) | | | Output |
| Ready | 0  1 | false  true | 0  1.00 | Output |
| Record | 0  1 | false  true | 0  1.00 | Output |
| Retry | 0  1 | off  on | 0  1.00 | Input / Output |
| Retry Count | 1 to 4 | 1 to 4 | 0  1.00 | Input / Output |
| Select All | trigger button | | | Input / Output |
| Speak Now [2](#Speak_Now) | 0  1 | false  true | 0  1.00 | Output |
| Split | 0  1 | off  on | 1  1.00 | Input / Output |
| Status | text field | | | Output |
| Talk (in Live and Auto)  Record (in Delay)  Play (in Message) [3](#Play) | 0  1  (Play N / A) | false  true | 0  1.00  (Play N / A) | Input / Output |
| Translation | (trigger) | | | Input / Output |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1. Group Active is the red LED indicating paging activity on that group, Group Select is the trigger button, Group Match is the state (color) of the trigger button. Bright is match, dark green is no match.2. Speak Now is tied to the Status field. When the Status field reaches the status of "Speak now! (seconds)" this Control pin goes to true. The Mode must be Live, Auto or Record.3. In the Message Mode, the Play button is a momentary button that activates the message playback by clicking and releasing, or clicking and holding. Either method causes the button itself to be disabled (grayed out). | | | | |
