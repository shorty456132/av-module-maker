# Audio Recorder

> Source: https://help.qsys.com/Content/Schematic_Library/audio_file_recorder2.htm

# Audio Recorder

The Audio File Recorder Component allows you to record from 1 to 4 tracks of audio. You can build a file name consisting of a prefix that you enter, then select from several combinations of prefix, time, date, and sequence. In addition, you can select the file format, bitrate / resolution and sample rate.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Track Count** Property.

### Input Pins

#### Track 1 - n

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Audio Recorder component is set to allow for 2 Tracks. You can choose between 1 and 4 Tracks.

### Output Pins

This component does not have any output pins.

[Schematic Example](javascript:void(0))

In this example, we have four Mics open at once. Through the [Gating Automatic Mic Mixer](auto_mixer_gating_adaptive.htm), those signals are attenuated and then mixed out to an Audio Recorder.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Audio Recorder Properties

#### Track Count

Specifies the number of tracks recorded. The maximum number of tracks in a design is 4.

[Controls](javascript:void(0))

#### Record

Starts the recording.

#### Stop

Stops the recording.

#### Root

Sets the root directory to any of the existing directories on the Core. This restricts the available Directories and Files to that which exists beneath the selected Root directory.
There is a blank line at the top of the Root drop-down to remove the filter for the Directory drop-down. When the filter is removed, the Directory drop-down displays all directories and sub-directories.
If for some reason, the Root directory specified by the Audio File Recorder no longer exists, this field turns red, along with the Directory and File fields.

#### Directory

With nothing selected in Root, this drop-down list displays all available directories and sub-directories on the Core. The Audio Files directory is selected by default.

If you select a different directory when a file is recording, and the file is not in the selected sub-directory, the file stops playing and the Status displays "Missing file". If the file is in the newly selected directory, the file stops playing, Status is OK, you must click the Play button to continue playing the file.

If for some reason, the Directory specified in this field by the Audio File Player no longer exists, this field turns red.

#### Prefix

User-defined prefix for the filename. Do not use any of the following in the filename:

* / slash
* \ backslash
* ? question mark
* % percent
* \* Asterisk
* : Colon
* | vertical bar (or pipe)
* " quote
* < less than
* > Greater than

#### Include

Includes the **Date**, **Time**, or **Sequence** as preferred.

#### Filename

Displays the result of the Recipe selections.

#### Format

Select the format of the recorded file.

* MP3 â lossy compression
* FLAC â lossless compression
* WAV â uncompressed

#### Bitrate / Resolution (kbit per second)

Sets the number of bits transferred in one second.

* MP3 Default = 128 Range = 16 to 320
* WAV Default = 16 bit fixed Range = 16 bit fixed, 24 bit fixed, 32 bit float
* FLAC = 16 bit fixed to 24 bit fixed

#### Sample rate (kHz)

Sets the average number of samples obtained in one second.

#### Length

Displays the length of the recording. HH:MM:SS

#### Time available

The time available on the Core for recording. HH:MM:SS The available time depends on the size of the hard drive installed on the Core and the type of file selected.

#### Space available

The space available on the Core for recording. The available space depends on the size of the hard drive installed on the Core.

#### Life file length

Select a length of time to which a recording is limited.

#### Continuous recording mode

Continues recording until the Limit file length

#### Quantize rollover time

Time starts the new "rolled over" file on a multiple of the Limit Length selection. Minute long files start on the minute, hour long files start on the hour, and so on.

#### Cleanup files

Indicates which files are to be removed when they reach the selected age and/or size.

#### Maximum age

Files are deleted when the age limit you select is reached.

Selections range from 1 day to unlimited.

Must have something other than "never" selected in the Cleanup files field.

#### Total size Limit

Files are deleted when the age limit you select is reached.

Selections range from 100MB to 100GB, and space available.

Must have something other than "never" selected in the Cleanup files field.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

**Note:** Text inputs are case sensitive and must be the entire string.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Bitrate/resolution [1](#Bit_rate) | varies | example:  (MP3) 128kbit/sec  (WAV / FLAC) 16 bit fixed | N / A | Input / Output |
| Cleanup files | never  in directory  matching prefix | | | Input / Output |
| Continuous | 0  1 | false  true | 0  1.00 | Input / Output |
| Directory | example: mydirectory/ | | | Input / Output |
| Format | MP3  WAV  FLAC | | | Input / Output |
| Include Date | 0  1 | false  true | 0  1.00 | Input / Output |
| Include Sequence | 0  1 | false  true | 0  1.00 | Input / Output |
| Include Time | 0  1 | false  true | 0  1.00 | Input / Output |
| Length | accumulated seconds | HH:MM:SS | N / A | Output |
| Length limit [2](#Text_input_only) | varies | max supported  to  2 hours | N / A | Input / Output |
| Maximum Age | varies | 1 day  to  unlimited | N / A | Input / Output |
| Name (filename) | text (based on Recipe) | | | Output |
| Prefix | text | | | Input / Output |
| Quantize rollover time | 0  1 | false  true | 0  1 | Input / Output |
| Record | 0  1 | false  true | 0  1 | Input / Output |
| Root | text | | | Input / Output |
| Sample rate | text | | | Input / Output |
| Space available |  |  |  | Output |
| Stop | 1  0 | true  false | 1  0 | Input / Output |
| Time available | text (HH:MM:SS) | | | Output |
| Total size limit | text (100MB)  Case Sensitive | | | Input / Output |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1. The value output is equal to the number of bits. For example, 128kbit/sec gives a value of 128000.2. Text input only, output can be text or numeric. Numeric is the number associated with the selection, for example, 1 minute = 1, and 1 hour = 1. | | | | |
