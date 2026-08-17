# SMPTE Linear Timecode Encoder

> Source: https://help.qsys.com/Content/Schematic_Library/linear_timecode_encoder.htm

# SMPTE LTC Generator

The SMPTE LTC Generator component generates a Linear Timecode (LTC) audio signal, per the SMPTE 12M specification.

A start time can be entered into the Hours, Minutes, Seconds and Frames fields. Drop Frame mode can be enabled and the OTWP button can be used to Output Timecode While Paused. The generator stops when the time reaches 23:59:59:29. When stopped, the time fields return to the most recently entered start time.

Connect the generator output to one or more local or networked Q-SYS SMPTE LTC Readers, analog and/or digital output(s), or directly to the [Timeline [BETA]](timeline.htm) component.

Connect the Control Pins of the generator to a [Control Script](control_script_2.htm) component with an appropriate [Lua script](../Control_Scripting/Using_Lua_in_Q-Sys/01_Using_Lua_in_Q-Sys_Overview.htm) to control the generator.

[Inputs and Outputs](javascript:void(0))

### Input Pins

This component does not have any input pins available.

### Output Pins

#### Output

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the SMPTE LTC Generator component only has one output pin available.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### SMPTE LTC Generator Properties

This component has no configurable properties.

[Controls](javascript:void(0))

#### Frame Rate (fps)

Sets the number of frames per second: 24 Pulldown, 24, 25, 30 Pulldown (default), or 30.

#### Hours

Counts the number of elapsed hours and allows for manually entering the hours, from 0-23.

#### Minutes

Counts the number of elapsed minutes and allows for manually entering the minutes, from 0-59.

#### Seconds

Counts the number of elapsed seconds and allows for manually entering the seconds, from 0-59.

#### Frames (fps)

Counts the number of elapsed Frames and allows for manually entering the frames, from 0-29.

#### Drop Frame

The Drop Frame toggle button enables "drop-frame" mode in which frames are periodically dropped to stay in sync with wall clock time.

#### Start

Starts the timecode count from the numbers entered, or from zero if nothing has been entered.

#### Stop

Stops the timecode count. After stopping the count, if the Start button in pressed, the timecode count starts at the numbers originally entered or zero if nothing was entered.

#### Pause

Pauses the timecode count. When restarted the count resumes at the time it was stopped.

#### OTWP

The Output Timecode When Paused (OTWP) toggle button causes the timecode, at which the Writer was stopped, to be repeatedly output when the counter is paused.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Drop Frame | 0  1 | disabled  enabled | 0  1.00 | Output |
| Frames In 1 | 0 -29 | 0 - 29 | 0.00 to 1.00 [2](#Increments) | Input/Output |
| Frames Out 1 | 0 - 29 | 0 - 29 | 0.00 to 1.00 2 | Output |
| Hours In 1 | 0 - 23 | 0 - 23 | 0.00 to 1.00 2 | Input/Output |
| Hours Out 1 | 0 - 23 | 0 - 23 | 0.00 to 1.00 2 | Output |
| Minutes In 1 | 0 - 59 | 0 - 59 | 0.00 to 1.00  (0.017 increments) | Input/Output |
| Minutes Out 1 | 0 - 59 | 0 - 59 | 0.00 to 1.00  (0.017 increments) | Output |
| Output Timecode When Paused | 0  1 | disabled  enabled | 0  1.00 | Input/Output |
| Pause | trigger | | | Input/Output |
| Paused | 0  1 | false  true | 0  1.00 | Output |
| Seconds In 1 | 0 - 59 | 0 - 59 | 0.00 to 1.00 (0.017 increments) | Input/Output |
| Seconds Out 1 | 0 - 59 | 0 - 59 | 0.00 to 1.00  (0.017 increments) | Output |
| Start | trigger | | | Input/Output |
| Started | 0  1 | false  true | 0  1.00 | Output |
| Stop | trigger | | | Input/Output |
| Stopped | 0  1 | false  true | 0  1.00 | Output |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1. Frames, Hours, Minutes, and Seconds each have an "In" control pin for setting the time, and each have "Out" control pins for reading the output of the counter.2. The increments in the position control depend on the number of frames per second. | | | | |
