# Virtual Page Station

> Source: https://help.qsys.com/Content/Schematic_Library/page_station_zone_select.htm

# Virtual Page Station

The Virtual Page Station is designed to be used on a touchscreen, and provides individual Zone selections and Group Zone selections. The Virtual Page Station can be automated by a script, or External Control. The Virtual Page Station component does not have an audio output pin, and does not have any parameters that relate to hardware. The Virtual Page Station's audio comes from an audio source connected directly to the PA Router.

[Inputs and Outputs](javascript:void(0))

### Input Pins

This component has no input pins.

### Output Pins

#### Station Control

Page Station Control pins carry control type signals unique to a Q-SYS Paging System. They are found on Page Station Components (proxies for the hardware), Virtual Page Station Components, and the PA Router to which both of the Page Station Components connect. The pin is represented by a down-pointing  triangle.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Virtual Page Station Properties

#### Hide Zone Buttons

Hides or displays the individual Zone Select buttons. You can use only Select All or Clear if this is set to Yes. Default is No.

#### Command Button Count

Sets the number of Command buttons available in the Virtual Page Station control panel, from 0 to 26 (default is 0).

#### Zone Group Count

Controls how many Zone Groups the page station will have, from 0 to 100 (default is 0).

#### Remote Zone Group Count

Defines the number of Remote Zone Groups available in the Virtual Page Station. Each group corresponds to a Remote Destination Tag configured in Q-SYS Administrator. Setting this property to a non-zero value enables the creation of dedicated buttons in the Virtual Page Station UI. Each button can trigger paging to a specific group of remote zones, allowing simplified cross-core paging.

From the Virtual Page Station Properties window, setting the Remote Zone Group Count to 3 for example, will display three buttons on the Virtual Page Station labeledâGroup 1, Group 2, and Group 3. These buttons can be mapped to Remote Destination Tags such as, Poolside Patios, Lobbies, or Conference Ballrooms.

**Tip:** Ensure the PA Router has a non-zero Remote Destination Count and Remote Destination Tags are properly configured in Q-SYS Administrator. Button labels can be customized using UCI Design Tools.

#### Enable Robot Controls

Enables or disables the Robot Controls. For more information, see the Controls section.

#### Talk Button Latches

Determines the behavior of the Talk button:

* When set to Yes (default), a quick press of the Talk button will start the page and latch the button to the on position. A second quick press will unlatch the button and stop the page.
* When set to No, you must always press and hold the Talk button to open the microphone.

**Note:** When set to Yes, a long press is interpreted as press-and-hold-to-talk, and the page ends when the button is released. The difference between what is a "quick" and "long" press is determined by the Delay control. See the [Controls](#Controls) section for more information.

**Tip:** The **Talk button Latch** operation only works for the button and not the control pin; however, you can use a Flip-Flop component to control the Talk pin. For more information, see [Using the Talk Control Pin](#Using_Talk_Control_Pin).

[Controls](javascript:void(0))

### Control

#### Busy

The red Busy LED is intended to indicate that a Page Station cannot perform a live page at the priority level, and to the zone(s), specified in the currently selected Command.

#### Ready

Green LED indicating that the selected Zones, at the selected Priority, are available for a Live page.

#### Record

If the Mode drop down is set to Delay and the Record button is clicked, the green Record LED is on to indicate the page is being recorded. In addition, the Ready LED flashes. Once you have completed recording the page, and the required Zones are available, the page is played.

#### Status

Displays the current paging status. Possibilities include:

* Live: Ready to page - Press TALK to issue
* Live: Paging - Speak now! (seconds)
* Live: Page Complete
* Live: Busy - Press TALK to enter queue
* Auto: Ready to page - Press TALK to issue
* Auto: Ready to record - Press TALK to issue
* Auto: Paging - Speak now! (seconds)
* Auto: Recording - Speak now! (seconds)
* Auto: Playing Message - Press CLEAR to Cancel
* Auto: Page Complete
* Auto: Playback Complete
* Delay: Ready to record - Press TALK to issue
* Delay: Recording - Speak Now! (seconds)
* Delay: Waiting to Playback - Press CLEAR to Cancel
* Delay: Playing Message - Press CLEAR to Cancel
* Delay: Playback Complete
* Message: Message not Ready
* Message: Ready to Play Message - Press TALK to issue
* Message: Playing Message - Press CLEAR to Cancel
* Message: Playback Canceled
* Message: Waiting to Playback - Press CLEAR to Cancel

#### Delay

Determines the threshold between "quick" and "long" presses of the Talk button, from 10.0ms to 1.00s (default is 300ms). For example, if set to 500ms (or a half a second), pressing the Talk button for 500ms or longer would be interpreted as a long press / press-and-hold-to-talk. For more information, see the Talk Button Latches description in [Properties](#Properti).

**Tip:** Increasing the Delay time can mitigate issues with Talk button presses being inadvertently interpreted as press-and-hold-to-talk. This is especially true with large designs with heavy CPU or network utilization.

#### Talk / Record / Play / Loop

This button initiates the action indicated by a Command button or an Ad Hoc page (Configuration controls). Depending on the Mode selected, the name of the button changes. If there is a preamble assigned to the command, the main part of the command does not start until the preamble is complete.

**Talk** opens the microphone to enable voice paging.

* Click and hold the button - the microphone stays open until you release the button,
* Click (and release) the button - the microphone stays open until you click the button again.

**Note:** The "latch" feature only works for the button and not the control pin; however, you can use a Flip-Flop component to control the Talk Pin. For more information, see [Using the Talk Control Pin](#Using_Talk_Control_Pin).

**Record** opens the microphone to record a page.

* Click and hold the button - the microphone stays open while the message is recorded and you release the button,
* Click (and release) the button - the microphone stays open while recording and stops when you click the button again.

**Play** begins playing a specified message.

* Click (and release) the button - the message plays until the message is over, the max message length is reached, or you click the button again.

**Loop** begins playing a specified message.

* The message continues to play all the way through until you click the Loop button again or the Max Page Duration is reached.

**Note:** When an action is activated, all other controls in the Control Panel are disabled. These buttons (configuration controls) can still be controlled via Control Pins. When a page is in progress, the configuration controls do not affect the in-progress page. The configuration controls, if set during a page, affect the subsequent page.

#### Cancel

Click this button to end a Recording or Message without completing the action.

### Command Buttons

#### Group (A-*n*)

The Command Button Count in the Properties must be greater than zero to enable this feature. Options are from 0 to 26 (default is 0), which will define the Command Button as **A**, **B**, **C**, etc.

**Tip:** To program Command Buttons, please visit [Page Stations (Administrator)](../Administrator/Page_Stations.htm).

#### Ad Hoc

When you have the Virtual Page Station wired to a [PA Router](page_system.htm), the Virtual Page Station will have  Zone Selection buttons at the bottom, one for each Zone in the PA Router.

The Ad Hoc button will create a page in the zones selected by those buttons.

**Note:** The Ad Hoc Button and Command Buttons are an either / or situation.

#### Example

### Configuration

#### Mode

Determines the method by which a page is placed in the queue. There are five types:

* Live : means the page will not be Recorded. If the PA Zones are in use by a page of equal or higher Priority, the request will be queued up behind other queued pages of equal or higher Priority, but before pages of lower priority. PA Zones that are in use by pages of lower priority will be interrupted. When the page request reaches the front of the queue, the preamble (if configured) plays and the operator can speak.
* Auto : is a combination of Live and Delay where a decision is made, at the time Talk is pressed or the microphone is keyed, to page Live if all of the PA Zones are available, otherwise the page is Recorded as a Delay page.
* Delay : means the page will always be Recorded. After the recording is complete, and a five second interval has passed (to give you time to cancel the page before it begins), the playback either begins or is queued according to the same rules as a Live page. When playback begins, you can cancel it by clicking the Cancel button.
* Message : Plays the preamble (if a preamble is selected) and the message selected from the Messages directory. The Talk button changes to the Play button which, when pressed, starts the message playback. The message plays only once.
* Loop Message : Loops the selected message for the Max Page Duration. The Talk button changes to the Loop button which, when pressed, begins looping the selected preamble (if a preamble is selected) and the message. Pressing the loop button again cancels the looping.

#### Priority

Determines the Priority of the Page or Message. The priorities are defined in [Administrator](../Administrator/AdministrationInterface.htm).

#### Preamble (Directory)

Select the directory in which the Preamble files are located. By default, this is the Preambles directory, which you can manage within the Q-SYS Core Manager > [Files](../Core_Manager/Core_Management/Audio_Files.htm) page.

**Note:** If you create a subdirectory under the Preambles directory, you must add files to that subdirectory in order for the Virtual Page Station to recognize it.

#### Preamble (File)

Select the file you want to play for the Preamble.

#### Message (Directory)

Select the directory in which the Message files are located. By default, this is the Message directory, which you can manage within the Q-SYS Core Manager > [Files](../Core_Manager/Core_Management/Audio_Files.htm) page.

**Note:** If you create a subdirectory under the Message directory, you must add files to that subdirectory in order for the Virtual Page Station to recognize it.

#### Message (File)

Select the file you want to play for the Message.

#### Max Page Duration

The longest page you want to allow on this Page Station, in seconds. You can select from Not Limited, 30, 60 (default), 90, 120, and 240.

#### Split

For Pages and Messages, clicking this button means that page or message (command) will not wait for all Page Zones to be available to start; only one zone needs to be available.

If one or more, but not all, zones are interrupted during the "splitable" page, the command for those zones is discontinued, but the command continues on the available zones. If retry is enabled and any of the zones had been interrupted or were not available when the command was issued, those zones will be retried. This will continue until all of the zones have succeeded, the retry count is exhausted, the command is canceled or the queue timeout expires.

**Tip:** Typically, the Split mode would be used for low priority, non-essential, background messages that go to a large number of zones.

#### Split on Interrupt

This works similarly to the Split command; however, once the paging command is being played, if one or more zones are interrupted by another higher priority command, then the zone that is not interrupted should continue playing.

#### Archive

Checkbox to indicate whether or not pages of the associated Priority level are Archived. Archive does not apply to Play Message commands.

A compressed mp3 file of the page audio is saved in the media/Page Archives folder. In the Event Log, there is a play button, next to the page event, to listen to the archive.

The pages are stored until they meet the purge deadline - 31 days, or when the directory reaches 10MB. Oldest files get deleted first.

#### Retry

Check-box indicating whether or not a page (except Live pages), of the associated Priority, gets retried. Retry does not apply to live pages.

#### Count

The number of times you want the page retried, from 1 to 4.

### Zone Selection

All of the Zones defined in the PA Router display as individual buttons below the Select All and Clear All buttons.

#### Select All

Selects all the Zones defined in the [PA Router](page_system.htm).

#### Clear All

Clears any and all Zones you have selected.

#### Zone (1 - *n*)

One Zone select button for each Zone defined in the PA Router. Click once to select, again to deselect. When a Zone is selected, the Page or Message is played in that Zone. You can select multiple zones.

### Zone Groups

#### Group (1-*n*)

The Zone Group Count in the Properties must be greater than zero to enable this feature.

Groups of Zones are based on how you **[Tag the PA Zones](../Administrator/PA_Zones.htm)** in the Q-SYS Administrator. When you click a Group button, all the PA Zones assigned to that Tag are selected.

#### Group tag (1 - *n*)

One tag for each Group. Enter the Tag name you want to define the Group. All the Zones tagged with that Tag are now part of the Group. You can also select a single zone by the default zone number, or by the name given it in [PA Zones](../Administrator/PA_Zones.htm) in the Administrator.

### Robot Controls

The Robot controls are an alternate way of controlling the Page Station using a Lua script or external control. They allow reliable machine control of the station without risk of race conditions or having to detect blinking lights or having to parse status sentences.

#### Reset / Submit

These buttons are mutually exclusive. When Reset is on, the State will be "reset". In this state, the Configuration and Zone Selection controls are used to configure a page event. Once configured, press the Submit button to on (the Reset button turns off). If the configuration is invalid (such as no zones are selected or no priority is selected), the State will remain "reset", otherwise the State will change to "ready". This does not mean that the zones that are selected are available, only that what has been entered is meaningful.

#### Start

When in the "ready" state, the Start trigger is used to issue the page. The State will transition to "wait" until the requested zones are available (at the selected priority) and the preamble has played (if applicable). The State then transitions to "input" which means the PA Router has routed the corresponding input to the selected zones, the recorder, or both (depending on Mode) and the operator should speak. If Mode is "Message", the "input" State is skipped and State transitions directly to "output".

#### Stop

When the operator has completed speaking, the Stop trigger is used to stop the page. If this is a delayed page (or an Automatic page that was not completed live), the State will transition to "output" and the recorded message will be played in the selected zones, otherwise the State will transition to "done".

#### Cancel

The Cancel trigger stops the recording or playback of the current page and State transitions to "done".

#### State

Displays the state of a paging operation. It's possible values are reset, ready, wait, input, output, "done".

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Group Active (1-*n*) [1](#Group_Indicators) | 0  1 | false  true | 0  1.00 | Output |
| Group Match (1-*n*) [1](#Group_Indicators) | 0  1 | false  true | 0  1.00 | Output |
| Group Select (1-*n*) [1](#Group_Indicators) | trigger button | | | Input |
| Group Tag (1-*n*) | user-defined string | | | Input / Output |
| *Robot* Cancel | trigger button | | | Input / Output |
| *Robot* Reset | 0  1 | false  true | 0  1.00 | Input / Output |
| *Robot* Start | trigger button | | | Input / Output |
| *Robot* State | text field  ready  output  reset  done | | | Output |
| *Robot* Stop | trigger button | | | Input / Output |
| *Robot* Submit | 0  1 | false  true | 0  1.00 | Input / Output |
| Archive | 0  1 | off  on | 0  1.00 | Input / Output |
| Busy | 0  1 | false  true | 0  1.00 | Output |
| Cancel | trigger button | | | Input / Output |
| Clear All | trigger button | | | Input / Output |
| Max Page Duration | 0 to 3600 | 0 seconds to 3600 seconds | 0  1.00 | Input / Output |
| Message (file) | The user-defined text string identifying message files. The filename does not need the file-type extension in this field. | | | Input / Output |
| Message Directory | The case-sensitive name of the directory where the Message (file) is stored.  The default directory name is Message, indicated by a blank.  Use "/" forward slashes between directories.  **Note:** You must have the correct type of audio files present in a directory to access it. | | | Input / Output |
| Mode  case sensitive text input | System-defined case-sensitive text string:  Live  Auto  Delay  Message | | | Input / Output |
| Preamble (file) | The user-defined text string identifying preamble files. The filename does not contain/need the file-type extension in this field. | | | Input / Output |
| Preamble Directory | The case-sensitive name of the directory where the Preamble (file) is stored.  The default directory name is Preamble, indicated by a blank.  Use "/" forward slashes between directories.  **Note:** You must have the correct type of audio files present in a directory to access it. | | | Input / Output |
| Priority | 1 - *n* | User-defined text name of the Priority. The numeric values associated with the Priorities depend on how many Priorities you set, and their order. | 1 - 1.00 | Input / Output |
| Ready | 0  1 | false  true | 0  1.00 | Output |
| Record | 0  1 | false  true | 0  1.00 | Output |
| Retry | 0  1 | off  on | 0  1.00 | Input / Output |
| Retry Count | 1 to 4 | 1 to 4 | 0  1.00 | Input / Output |
| Select All | trigger button | | | Input / Output |
| Speak Now [2](#Speak_Now) | 0  1 | false  true | 0  1.00 | Output |
| Split | 0  1 | off  on | 1  1.00 | Input / Output |
| Status | text field | | | Output |
| Talk (in Live and Auto)  Record (in Delay)  Play (in Message) [3](#Play) | 0  1  (Play N / A) | false  true | 0  1.00  (Play N / A) | Input / Output |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1. Group Active is the red LED indicating paging activity on that group, Group Select is the trigger button, Group Match is the state (color) of the trigger button. Bright is match, dark green is no match.2. Speak Now is tied to the Status field. When the Status field reaches the status of "Speak now! (seconds)" this Control pin goes to true. The Mode must be Live, Auto or Record.3. In the Message Mode, the Play button is a momentary button that activates the message playback by clicking and releasing, or clicking and holding. Either method causes the button itself to be disabled (grayed out). | | | | |

[Using the Talk Control Pin](javascript:void(0))

There is a difference in operation between the talk button on the Virtual Page Station and its control pin when the âLatch Talkâ button property is enabled. The "latch" feature allows a quick press of the button to latch the button on and a second quick press to unlatch it. If the Page is activated by the Talk button's Control Pin, you can use a Flip-Flop component between the control signal and the Talk pin to control the latch and unlatch.
