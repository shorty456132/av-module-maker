# Audio Player

> Source: https://help.qsys.com/Content/Schematic_Library/audio_file_player.htm

# Audio Player

The **Audio Player** plays audio files meeting the following requirements:

* File types: .mp3, .wav, or .flac
* Sample size: 8, 16, 24, 32-bit fixed-point and 32-bit floating-point.
* Sample rate: 48 kHz recommended
* Maximum file size: Supported audio file formats are limited to 4 GB in size.
* Tracks based on the purchased Feature license (16 tracks are standard). See the [Licensing](../Core_Manager/Core_Management/Licensing.htm) topic for MTP upgrade / license information.

The Audio Player features a Control Pin named Location. This Control Pin allows you to enter a number of seconds via Lua script, or a custom control, and move to that spot in the file before pressing the Start button, or during playback.

**CAUTION:** If you upgrade your hard drive, you will lose any files you had on the flash drive. Back up the files prior to upgrading.

The files can be loaded onto the Core using the Q-SYS Core Manager > [Files](../Core_Manager/Core_Management/Audio_Files.htm) page.

When setting the Properties of the Core, you set the maximum number of tracks the design requires, either the default of 16 or, 64, or 128. If the Core has not been upgraded to the number of tracks requested in the Core Properties, the design will fail to compile. Audio tracks can be divided between multiple Audio Players, as the system designer sees fit. The total number of Audio Player tracks in a Q-SYS design cannot exceed 16, 64 or 128 based on the options you have purchased.

**Note:** If you play a multi-track file on the Audio Player, be sure that your **Track Count** for the Audio Player is set to the same number of tracks as your file. If not, the Audio Player plays only the first *n* number of tracks from the file.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Track Count**Property.

### Input Pins

This component does not have any input pins.

### Output Pins

#### Track 1 - n

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Audio Player component is set to allow for 2 Tracks. You can choose between 1 and 128 Tracks.

[Schematic Example](javascript:void(0))

In this example, we have two Audio Players, each playing its own announcement to various loudspeakers within our small venue.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Audio Player Properties

#### Track Count

Sets the number of output tracks for the Component. The maximum number of tracks you can specify is based on purchased options. The standard is feature is 1 - 16 tracks; upgrade to 1 - 64 and upgrade to 1 - 128 tracks.

If you add Audio Players with a total track count greater than this setting, your design will not compile.

If the Track Count is 1, and you play a multi-track audio file, only one track from the audio file is played. The file's tracks are not summed.

If the Track Count is 2 or more, and you play a mono audio file, Track 1 of the Audio Player carries the mono signal, all other tracks are silent.

#### Player Name

User-defined name for the Audio Player.

When the Audio Player component is placed into the Schematic, the default name displayed is "Audio Player". If you enter a name in the Player Name property, for example "First", the name of the component displayed in the Schematic changes to "Audio Player First".

If you select the component in the Schematic and type something, the displayed name changes to what you typed. This has no effect on the Player Name in the Properties.

#### Playlist Capable

Determines if you can play any existing Playlists with this Audio Player.

[Controls](javascript:void(0))

#### Rewind

The Rewind button is a standard audio player type feature. Click and hold to move backwards in the file until you reach the location you want.

#### Play

The Play button starts playing the selected audio file from either the beginning, or from where it was paused. The Play indicator lights green when the file is playing.

**Tip:** While a song is playing, pressing play again restarts playback at the beginning of the current track.

#### Fast Forward

The Fast Forward button is a standard audio player type feature. Click and hold to move forward in the file until you reach the location you want.

#### Stop

The Stop button stops playing the selected audio file. The file is reset to the beginning. The Stop indicator lights red when the file is stopped.

**Tip:** While a song is playing, pressing stop returns to the beginning of the current track and halts playback.

#### Pause

The **Pause** button temporarily stops playing the selected file. The Pause indicator lights yellow when the file is paused. The must be playing (green **Play** indicator is lit) in order to pause the playback. You can resume playing the file by clicking either the Play or Pause buttons.

#### Loop

The Loop button allows continuous playing of the selected file. The Loop indicator illuminates white when the button is engaged. To discontinue the looping, click the Loop button again.

**Note:** Do not use the Loop function in conjunction with a periodically scheduled Event. Doing so will cause the Audio Player to continue playing even though the Event is complete.

#### Auto-Play

Enables the selected file to begin playing when the design is saved to the Core and run.

#### Gain (dB)

The Gain knob controls the output gain of the Audio Player.

#### Mute

The Mute button mutes the output of the Audio Player, the file continues to play.

#### Time

The Time display indicates how long the file has been playing, including any silence at the beginning or end of the file. The format is HH:MM:SS. The Time readout will stop when the **Pause** button is engaged, and is reset to zero when the **Stop** button is engaged.

#### Remaining

The Remaining display indicates the play-time remaining for the current audio file, including any silence at the beginning or end of the file. The format is HH:MM:SS. The Remaining readout will stop when the **Pause** button is engaged, and is reset to the total play-time of the selected file when the **Stop** button is engaged.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### Root

Sets the root directory to any of the existing directories. This restricts the available **Directories** and **Files** to that which exists beneath the selected Root directory.

There is a blank line at the top of the Root drop-down to remove the filter for the Directory drop-down. When the filter is removed, the Directory drop-down displays all directories and sub-directories containing audio files.

If for some reason, the Root directory specified by the Audio File Player no longer exists, this field turns red, along with the Directory and File fields.

#### Directory

With nothing selected in **Root**, this drop-down list displays all directories and sub-directories on the Core containing valid audio files. The Audio Files directory is selected by default.

When you select a directory from the list, the **File** drop-down list is filtered to display only the files in the selected subdirectory.

If you select a different directory when a file is playing, and the file is not in the selected subdirectory, the file stops playing and the Status displays "Missing file". If the file is in the newly selected directory, the file stops playing, Status is OK, you must click the Play button to continue playing the file.

If for some reason, the Directory specified in this field by the Audio File Player no longer exists, this field turns red, along with the File field.

#### File

Enter the name of the file you wish to play - *filename.ext* or use the drop-down list to display the available files, and select the one you want to play. The drop-down list displays any audio files in selected **Directory**.

If you select a new file during playback of another, playback stops. The new file does not begin to play until the **Play** button is clicked.

If a file is playing, and the name of the file is changed, or the file is deleted or corrupted, the Audio Player stops playback and the File field turns red. The Audio Player continues to look for the file, and if it is found, the status is updated, but playback does not start until the Play button is pressed.

### Additional Controls

**Note:** The following controls are only available when the **Playlist Capable** Property is set to **Yes**.

#### Playlist

Use the drop-down list to display the available Playlists, and select the one you want to play. You must click the **Play** button to begin playback.

In addition to selecting Playlists, you can select **<All Files>** or **<None>**.

**<All Files>** plays all the files in the directory selected in the **Directory** field and in any subdirectories of the selected directory.

**<None>** allows you to select a file in the **File** field. When you select anything other than **<None>**, the **File** field is not accessible.

To create a Playlist, refer to the Q-SYS Core Manager > [Files](../Core_Manager/Core_Management/Audio_Files.htm) topic.

#### Shuffle

Click this button if you want the files in the Playlist played in a random order. If the Repeat button is selected, when all the files in a Playlist have been played, they are re-shuffled and played again. If you do not click the Shuffle button, the files play in the order they are listed in the Playlist. When you change the playlist, a different random sequence is used.

#### Repeat

Click this button if you want the Playlist to repeat playback in the order in which the files are listed. The repeat playback continues until you stop it.

#### First

Click this button to go to the first file in the Playlist order or Shuffle order.

#### Prev

Click this button to play the previous file in Playlist order or Shuffle order. If the current song is the first in either order, this button is inactive.

#### Next

Click this button to play the next file in Playlist order or Shuffle order. If the current song is the last in either order, this button is inactive.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| All Files | N / A | text array of all files [1](#Array) | N / A | Output |
| Auto Play on Startup | 0  1 | false  true | 0  1 | Input / Output |
| Directory | N / A | text - list of directories and subdirectories | N / A | Input / Output |
| Fast Forward |  |  |  | Input / Output |
| File Name | N / A | text - name and path of file | N / A | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Input / Output |
| Location [2](#Location_Pin) | Input values are in seconds. Maximum number depends of audio file size. | | | Input |
| Loop | 0  1 | false  true | 0  1 | Input / Output |
| Mute | 0  1 | unmute mute | 0  1 | Input / Output |
| Pause Trigger | trigger | | | Input / Output |
| Paused LED | 0  1 | false  true | 0  1 | Output |
| Play Trigger | trigger | | | Input / Output |
| Playing LED | 0  1 | false  true | 0  1 | Output |
| Playlist | N / A | text - name of playlist | N / A | Input / Output |
| Playlist First | trigger | | | Input / Output |
| Playlist Next | trigger | | | Input / Output |
| Playlist Previous | trigger | | | Input / Output |
| Playlist Repeat | 0  1 | false  true | 0  1 | Input / Output |
| Playlist Shuffle | 0  1 | false  true | 0  1 | Input / Output |
| Remaining | N / A | HH:MM:SS  (total length of selected file) | N / A | Output |
| Root | N / A | text - lists available subdirectories | N / A | Input / Output |
| Status | N / A | text - lists status of player | N / A | Output |
| Stop Trigger | trigger | | | Input / Output |
| Stopped LED | 0  1 | false  true | 0  1 | Output |
| Time | N / A | HH:MM:SS | N / A | Output |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1. This is an array control that contains a list of all of the files under the Root Directory. It is intended to be wired to a Control Script component to create scripts for play lists, and so on. In the script you use Controls.Inputs[1].Strings. (Note that "Strings" is plural because it returns an array rather than " String", which returns just one string).2. Connect a script or custom control to the Location Control pin. The input is the total number of seconds from the beginning of the file to the point you want to start playing the file, then press Start. If the file is playing, you can move to that point and the file continues to play. If you enter a number of seconds that exceeds the playtime of the file, an error message is displayed. | | | | |

[Troubleshooting](javascript:void(0)) 

There are some components that are unique in their operation in the **Emulate** mode. Some of these components are the **Audio Player**, **Crossfader**, **Gain Ramp**, and **Listen** buttons. For more information, see [Limitations](../Q-SYS_Designer/003_Emulate_Mode.htm#Limitations).
