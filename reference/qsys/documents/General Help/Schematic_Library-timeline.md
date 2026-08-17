# Timeline

> Source: https://help.qsys.com/Content/Schematic_Library/timeline.htm

# Timeline [BETA]

The Timeline allows you to stage audio files to play at specific times in relation to one another. You can place the files on separate tracks; each track going to a different output, or you can place the files end-to-end on the same track. You can choose WAV audio files (.wav) from those stored on the Q-SYS Core processor in the Messages, Preambles, and Audio subdirectories. Manage files in these directories using the Q-SYS Core Manager > [Files](../Core_Manager/Core_Management/Audio_Files.htm) page.

**Note:** This is a BETA component. Though it is functional, it is not feature complete and is subject to change.

[Inputs and Outputs](javascript:void(0))

### Input Pins

This component does not have any input pins available.

### Output Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Timeline [BETA] component is set to 8 output Tracks. This is configurable between 0 and 128.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Timeline [BETA] Properties

#### Output Count

Select the number of outputs (tracks) for playback, from 0 to 128 (default is 8).

#### Time Source

Select whether to enable an input pin for syncing with an LTC time source:

[None](javascript:void(0))

Hides the External LTC Input pin and enables the External Time control for selection in the Control Pins list. If you have External Sync enabled, use the External Time input pin to inject the time to use. This is the legacy, pre-version 8.3 behavior.

[LTC](javascript:void(0))

Selecting this option:

* Exposes the External LTC Input pin. Connect this pin directly to the [SMPTE LTC Generator](linear_timecode_encoder.htm) component's output and turn on the External Sync Enable button.
* Enables the External LTC Time control for selection in the Control Pins list. This control is read-only, and outputs the time value in seconds.

**Tip:** The LTC frame rate (fps) is automatically detected from the incoming source.

#### Pulldown Correction

This property is available only when LTC is selected as the Time Source. Select 'Yes' to allow the current time display to align with incoming 29.97 NDF (30 pull-down) LTC frame rates. Otherwise, select 'No' (default).

[Controls](javascript:void(0))

|  | Control | Function |
| --- | --- | --- |
| 1 | Rewind button | Moves the time cursor back to the beginning of time â 00:00:00.0 (hh:mm:ss.frames) and stops. |
| 2 | Play button | Starts or restarts the time cursor moving forward. As it passes over an audio file, that file begins to play. |
| 3 | Pause button | Stops the time cursor at the point on timeline where Pause button is pressed. |
| 4 | Digital Readout | Indicates the position of the time cursor in hh:mm:ss.frames |
| 5 | External Sync Enable button | Click to enable time syncing with an external clocking source. Enable External Sync when:   * The Time Source property is set to 'LTC' and you have connected the LTC pin to the SMPTE LTC Generator component. * The Time Source property is 'None' but you want to feed time into the External Time control. |
| 6 | Add Control Track | Adds a control track below the Tracks. |
| 7 | â button | Zooms the tracks out |
| 8 | + button | Zooms the tracks in |
| 9 | Timeline | Horizontal marks indicating the position of the time cursor, and the position and length of the audio files placed in the tracks.  Double click the timeline, or click Pause to pause the playback, and control the time cursor with your mouse â your mouse pointer must be on the timeline itself. |
| 10 | Markers | Double-click the Marker row to place a Marker. After the Marker is in the row, you can move it (click and drag) as needed. The Markers allow you to Jump to another Marker, Pause, or load a Snapshot.  Hover over the Marker to display the Name and time position of the Marker. Click the Marker to open the Marker Dialog.  To delete a marker, click either the marker itself or the marker text label, then drag it off the marker area. |
| 11 | Marker Row | This row is used for adding Markers. |
| 12 | Time Cursor | Shows the current position of playback / pause in the timeline. |
| 13 | Fade In Marker | Indicates the end position of the clip's Fade In. |
| 14 | Track Name | Click the Track Name (default Track #) to enter a new name. |
| 15 | Clip | Representation of a Clip on the timeline. |
| 16 | â Track minimize /  + maximize | Click the â to minimize the vertical size of the track, or the + to maximize the vertical size of the Track. |
| 17 | Control Selection | Allows you to choose which Named Conrol is being adjusted by the Control Track. |
| 18 | Fade Out Marker | Indicates the start position of the clip's Fade Out. |
| 19 | Clip Gain Line | Graphic representation of the Clip Gain. Click and drag up / down to adjust the clip's gain level. |
| 20 | Fade In / Out | Graphic representation of the Fade In / Out points on the Clip. |
| 21 | Clip Info | Opens the Clip Info Dialog |
| 22 | Volume Handle | Double click on the Volume Line to add Handles. The Handles allow you to change the volume of the audio at the spot of the Handle. You can position the Handle horizontally (time) or vertically (volume). |
| 23 | Volume Control Line | Double click in the Volume Track to display the Volume Line with a single "handle". |
| 24 | Marker Name | User-defined name for the Marker |
| 25 | Marker Color | User-selected color for the Marker |
| 26 | Marker Time | Indicates the position of the Marker in hh:mm:ss.frames |
| \* | Marker Function | Defines what is going to happen when the time cursor reaches the Marker. Choices are None, Jump, Pause, Load Snapshot. |
| \* | Marker Jump To | When the Marker Function is set to Jump.  This is a drop-down list showing all Markers currently defined. When the time cursor reaches this marker, it moves to the Marker selected here. |
| \* | Marker Bank | When the Marker Function is set to Load Snapshot.  This is a drop-down list showing all Snapshot Banks currently defined in the design. When the time cursor reaches this Marker, the Snapshot is initiated. |
| \* | Marker Index | When the Marker Function is set to Load Snapshot.  This allows selection of the available snapshots based on the selected Snapshot Bank. |
| 27 | Marker Ramp Time | When the Marker Function is set to Load Snapshot.  This sets the amount of time (in seconds) for the selected snapshot to load. Value 0 - 200 |
| 28 | Clip Start Time | Indicates the position of the Clip start in hh:mm:ss.frames |
| 29 | Clip Gain | Indicates the Clip Gain as set by the Clip Gain Line. |
| 30 | Fade In Time / Type | Indicates the end position of the clip's Fade In. Selectable fade types are: Linear, S-Curve (default), 3dB, -3dB. |
| 31 | Fade Out Time / Type | Indicates the start position of the clip's Fade Out. Selectable fade types are: Linear, S-Curve (default), 3dB, -3dB. |
|  |  |  |
| --- | --- | --- |
| \* These properties are part of the Marker dialogs and not shown in the example. | | |

[Control Pins](javascript:void(0))

The following **Control Pins** are available in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Data | *Text - Tracks, Clip Info, Control Tracks, Markers* | | | Output |
| Enable External Sync | 0  1 | false  true | 0  1 | Input / Output |
| External Time  External LTC Time (when set to LTC in **Properties**) | 0 - 24\*60\*60 (one day in seconds) | | | Input \ Output  Output only |
| Frame Offset  (Available when Time Source set to LTC in **Properties**) | 0 - 10 | | | Input \ Output |
| Is Playing | 0  1 | false  true | 0  1 | Output |
| Reload | 0  1 | false  true | 0  1 | Input \ Output |
| Reset Trigger | 0  1 | false  true | 0  1 | Input \ Output |
| Start Trigger | 0  1 | false  true | 0  1 | Input \ Output |
| Stop Trigger | 0  1 | false  true | 0  1 | Input \ Output |
| Time | 0 - 24\*60\*60 (one day in seconds) | | | Output |
