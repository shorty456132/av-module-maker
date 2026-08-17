# Commands (Administrator)

> Source: https://help.qsys.com/Content/Administrator/Commands.htm

# Commands (Administrator)

Commands control and define various actions or events in the system. There are three general types of Commands you can create: **Public Address (PA) Commands**, **Control Commands** and **Snapshot Commands**.

You can restrict User access to Commands in the User properties, and the Page Station properties.

Commands can be invoked from Page Station **Command Buttons**, through keypad entry of a code on a Page Station or telephone, from GPIO or using the Command Schedule tab.

[PA Commands](javascript:void(0))

* The following are the available PA Commands:
  + **PA Play Messages** This Command plays a selected pre-recorded message.
  + **PA Page** This Command is used for live pages.
* Each PA Command type includes **Destination Zones**, a **Name**, and a numeric **Code**. Other Command parameters are specific to the Command type and are listed in the tables below.
* You can invoke any of the PA Commands from a Page Station. (Can be restricted by other parameters.)
* You can invoke PA Play Messages Commands using the [Command Schedule](Command_Schedule.htm) feature.

[Control Change Commands](javascript:void(0))

* Control Commands specify an action to be performed on controls in the Named Controls list in your design.
* To create a Control Command, you must add at least one Control to the Named Controls list in your design.
* You can invoke Control Commands from the Command Scheduler to schedule a Control change, run a Script, and so on.
* You can invoke a Control Command from a Page Station. (Can be restricted by other parameters.)
* You cannot create a Command using a control typically displayed in the Control Panel of a Component as a drop-down type control. The following is a list of controls, and the components containing them, that cannot be used in a Control Command.

| Control Name | Components |
| --- | --- |
| Type | Crossfade |
| Voicing Filter Type | Custom Voicing |
| Normalization | Custom Voicing, Crossover |
| Filter Order | Custom Voicing |
| Filter Slope | Custom Voicing, Crossover |
| Crossover Type | Custom Voicing, Crossover |
| Gated Mic Mixer Mode | Gated Automatic Mixer |
| GPIO Output Select | GPIO components in Raw mode |
| Low Frequency Shading | Wideline array |
| Peak RMS Select | Various meter selects |
| Side-chain Filter Type | Gated Automatic Mixer |

[Load Snapshot Commands](javascript:void(0))

* Snapshot Commands invoke a specific Snapshot within a Snapshot Bank.
* To create a Snapshot Command you can use the Global Snapshot Bank, or create a new Snapshot Bank.
* Snapshot Commands the same as Control Commands except you can have multiple controls associated with a Snapshot Bank. (If you specify a Snapshot Load button in a Control Command, when invoked, that button uses the Ramp Time specified in the Snapshot Bank.)

[Creating Commands](javascript:void(0))

1. Select the **Commands** tab in the Administrator. (The design must be in the Run or Emulate mode.)
2. Click the plus sign in the upper left corner of the interface. A drop-down list displays listing the types of Commands available to create.
   * For PA Commands, you must have at least one Page Station, and only one PA Router component in the design.
   * For Control Commands, you must have at least one control in the Named Controls list.
   * For Snapshot Commands, the Global Snapshot is defined in the design by default and you can create a Snapshot Command using the Global Snapshot.
3. Select the type of Command you wish to create. A dialog box displays with controls relating to the type of Command selected.
4. Define the Command according to the information listed in the Command Controls tables in this topic.
5. Add and assign Tags as desired. Refer to [Assigning Tags to Commands](#Assigning_Tags_to_Commands) for details.
6. When you are finished, click the OK button to save the Command, or the Delete button to discard the Command and exit the dialog box.

[Assigning Tags to Commands](javascript:void(0))

You may wish to establish a group of Commands that all perform the same or similar functions. To form a group of Commands:

1. Create the Commands you are going to add to the group. Each Command must have a unique Code.
2. Select the Commands you want in the group. Ctrl+click for one Command at a time, or Shift-click for a contiguous group of Commands.
3. Create a [Tag](Tags.htm) to identify the group. When you create the Tag, and have the Commands selected, the Tag is applied to all the selected Commands.
4. With the Commands still selected, double-click one of the Commands. **Do not use Ctrl+click or Shift-click at this point as it will change your selection.** The Command Settings dialog box displays.
5. The Code is not accessible at this point. Make selections, from the items that are accessible. Refer to the Controls table below. Any changes you make, with multiple Commands selected, are applied to all selected Commands.
6. When you edit the properties for a Page Station, or User, you can select the entire group of Commands to make them available for the Page Station or User simply by selecting the Tag you assigned to them.

To add another Command to the group, select the Command, and click the checkbox next to the group Tag in the Tags list.

**Note:** The assigned Tags are listed alphabetically from left to right next to the Commands.

### Filter the Commands by Tags

You can filter the list of Commands based on the Tags you assign.

1. Click the filter icon in the top left corner (next to the plus sign). A list of Tags displays.
2. Click the checkbox of the Tag or Tags you wish to filter by. Only the Commands assigned the selected Tags display.
3. Click the filter icon again and uncheck any or all of the Tags to remove or modify the filter.

[Controls](javascript:void(0))

Controls are available in a dialog box depending on the type of Command, and the Priority Mode set in the PA Global Settings.

[Common](javascript:void(0))

Applies to all Command types

#### Name

Text name identifying the item.

[PA Page Commands](javascript:void(0))

Create a Page Command for each paging scenario your system will encounter.

#### Override Source Priority Level

When the PA Global Settings **Priority Mode** is **Station/User Priority**, this is used to give this **PA Page Command** precedence over the Station's priority.

When this is set to Yes, the Priority Level setting becomes available.

#### Priority Level

Used to determine the priority of a page relative to other PA events. Priority Levels are defined in the **PA Global Settings** tab.

Priority Levels are available when the **Priority Mode** is **Command Priority**, and also when the Priority Mode is **Station/User Priority** and the **Override Source Priority Level** is set to Yes.

#### Queuing Mode

Determines the method by which a page is placed in the queue. There are three types: **Live**, **Delayed**, and **Automatic**.

**Live** means the page will not be **Recorded**. If the **PA Zones** are in use by a page of equal or higher **Priority**, the request will be queued up behind other queued pages of equal or higher Priority, but before pages of lower priority. PA Zones that are in use by pages of lower priority will be interrupted. When the page request reaches the front of the queue, the preamble (if configured) plays and the operator can speak.

**Delayed** means the page will always be **Recorded**. After the recording is complete, and a five second interval has passed (to give you time to cancel the page before it begins), the playback either begins or is queued according to the same rules as a **Live** page. When playback begins, you can cancel it, select a **Command** button (A-D), or enter a **Command Code** to initiate a new page while the recorded page completes in the background.

**Automatic** stores the page in memory as it is going out live. If the page is completed, the memory is cleared. If the page is interrupted, the remainder of the page will continue to be stored. Once the page is complete, it is played out like a Delayed page, and the memory is cleared.

#### Preamble

Select one of the available .wav files to be played prior to a page. Click the arrow (play button) to the right of the selected file to start playback, and the red square (stop button) to end playback.

You can manage the Preamble files in the Q-SYS Core Manager > Audio Files page.

QSC supplies a number of pre-recorded preamble audio files with Q-SYS Designer Software. These files are typically chimes, tones, and so on.

#### Preamble Gain (dB)

The Preamble Gain control is used to compensate for variations in the recording level of audio files. You can adjust this gain for each **PA Page Command** and keep the gain for the **PA Zone** in the **PA Router** at a consistent level.

This Gain interacts cumulatively with the Message Gain control in the PA Router.

**Note:** This gain does not affect the level of the preamble preview when you click the play button next to the Preamble field.

#### Destination Zones

Used to select the **PA Zones** affected by the **Command**. You can select one zone at a time or multiple zones at once by selecting a **Tag** defined in the [PA Zones](PA_Zones.htm) tab. You can expand the Tag to see which zones are included with the Tag. The default is none selected.

**Note:** If no PA Zones are selected, the Command is not usable.

[PA Play Message Commands](javascript:void(0))

#### Message File

An .mp3 file played when a Message type Command is invoked. You can manage the Message files in the Q-SYS Core Manager > Audio Files page.

Click the arrow (play button) to the right of the selected file to start playback, and the red square (stop button) to end playback.

#### Override Source Priority Level

When the PA Global Settings **Priority Mode** is **Station/User Priority**, this is used to give this **PA Play Message Command** precedence over the Station's priority.

When this is set to Yes, the Priority Level setting becomes available.

#### Priority Level

Used to determine the priority of a message relative to other PA events. Priority Levels are defined in the **PA Global Settings** tab.

Priority Levels are available when the **Priority Mode** is **Command Priority**, and also when the Priority Mode is **Station/User Priority** and the **Override Source Priority Level** is set to Yes.

#### Gain (dB)

The Gain control is used to compensate for variations in the recording level of audio files. You can adjust this gain for each **Message Command** and keep the **Message Gain** for the **PA Zone** in the **PA Router** at a consistent level.

This Gain interacts cumulatively with the Message Gain control in the PA Router.

#### Mode

**Queued Mode** â you invoke the message command, and when its turn comes, it is played.

**Looped Mode** â you invoke the message command, and it repeats as long as you hold the Talk button down.

#### Preamble

Select one of the available .wav files to be played prior to a pre-recorded PA message. Click the arrow (play button) to the right of the selected file to start playback, and the red square (stop button) to end playback.

You can manage the Preamble files in the Q-SYS Core Manager > Audio Files page.

QSC supplies a number of pre-recorded preamble audio files with Q-SYS Designer Software. These files are typically chimes, tones, and so on.

#### Preamble Gain

The Preamble Gain control is used to compensate for variations in the recording level of audio files. You can adjust this gain for each **PA Play Message Command** and keep the gain for the **PA Zone** in the **PA Router** at a consistent level.

This Gain interacts cumulatively with the Message Gain control in the PA Router.

**Note:** This gain does not affect the level of the preamble preview when you click the play button next to the Preamble field.

#### Destination Zones

Used to select the **PA Zones** affected by the **Command**. You can select one zone at a time or multiple zones at once by selecting a **Tag** defined in the [PA Zones](PA_Zones.htm) tab. You can expand the Tag to see which zones are included with the Tag. The default is none selected.

**Note:** If no PA Zones are selected, the Command is not usable.

[Control Change Commands](javascript:void(0))

#### Control

Select a control from the drop-down list. The list displays all of the **Named Controls** defined in the Q-SYS design.

Anything in a **Control Panel** is referred to as a "control". Controls that you cannot operate, such as a **Meter**, do not display in the list. Exceptions to this are, for example, a Meter from the **Custom Controls** component.

You cannot create a Command using a control designated as "**enum**" or an enumerated control. This is a control that typically displays as a drop-down type control. An example is the **Slope** control in the **Crossover Component**.

#### Value

Enter the target numeric value of a variable control. You can enter the value using your keyboard, or the spinner. The values you can enter are limited by the range and precision of the control.

If you select a toggle type control, for example a Mute button, the Values available are **On**, **Off**, and **Toggle**.

This field is not displayed for trigger type buttons. The Value drop-down menu is replaced by "**Control will be triggered**".

#### Ramp Time (seconds)

The time it takes to get from the current position to the defined **Value**.

This field does not display for momentary, text edit, toggle, or trigger type controls.

[Snapshot Load Commands](javascript:void(0))

#### Snapshot Bank

Select a Snapshot Bank from the drop-down list. The list displays all of the Snapshot Banks defined in the Q-SYS design.

The Global Snapshot Bank is defined in the design by default and can be used in a Snapshot Command.

#### Snapshot Number

Enter the target Snapshot Number in the selected Snapshot Bank.

The number of Snapshots defined in the selected Snapshot Bank sets the number of Snapshots available for selection in the Snapshot Command.

#### Ramp Time (seconds)

The time it takes to get from the current position to the defined Value. This value overrides the Ramp Time value set in the Snapshot Bank.

If there are buttons or other discrete type controls, they will change state at 50% through the Ramp Time.
