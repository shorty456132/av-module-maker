# Delay Matrix Mixer Component

> Source: https://help.qsys.com/Content/Schematic_Library/delay_matrix.htm

# Delay Matrix Mixer Component

The Delay Matrix component receives an audio input and distributes the audio signal to each of the component's **Outputs**. For each Output, you can control the **Delay** time, **Gain**, and **Mute** condition of the Input. Likewise, a single Output has a Delay, Gain and Mute control for each Input. In addition, you can select the type of delay. The Delay Type you select affects all outputs

[Inputs and Outputs](javascript:void(0))

### Inputs

**Audio** - Any audio you wish to delay. Up to 512 **Inputs** with up to 256 **Channels** per Input.

### Outputs

**Audio** - The audio input modified by the **Delay**, **Gain**, and/or **Mute** controls. Up to 512 **Outputs** with up to 256 **Channels** per Output.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Delay Matrix Mixer Properties

#### Input Count

Defines the number of **Inputs** available to the Matrix Delay.

#### Output count

Defines the number of **Outputs** available to the Matrix Delay.

#### Max Delay (Seconds)

Sets the upper limit of delay time for the **Delay** control.

#### Delay Type

Selects the type of [Delay](delay.htm) to use with the Delay Matrix.

#### Gain Type

Select the type of gain:

* **Standard**: (Default) A standard, logarithmic dB gain.
* **Linear**: Internal, direct-access representation of the gain.
* **X-Fade -3dB**: Special gain type. -3dB is a constant power cross-fade.
* **X-Fade -6dB**: Special gain type. -6dB is a constant voltage cross-fade.

### Options

#### Label Controls

Provides the ability to give custom names to each output and input.

#### Input Gain

Provides input gain faders.

### Channels

#### Type

Determines the Crossover Component's channel type.

**Note:** Stereo = two mono channels

#### Count

When you choose Multi-channel, you can specify from 2 to 256 for the Count.

[Controls](javascript:void(0))

#### Mute

Mutes the audio at a single **Input**/ **Output** intersection. One Mute button is available for each intersection.

#### Gain (dB)1

Controls the gain at a single **Input**/ **Output** intersection. One Gain control is available for each intersection.

#### Delay (Seconds)1

Controls the amount of delay at a single **Input**/ **Output** intersection. One Delay control is available for each intersection.

**Note:** Entering anything from 0.001Âµs to 0.005Âµs gets interpreted as 1.00 through 5.00 milliseconds. Entering anything greater than 0.005 gets interpreted as the milliseconds as entered (example 0.006 gets interpreted as .006 ms). The basic idea is that the value that you enter is larger than the max value and Q-SYS Designer assumes you want the value to be divided by 1000. If you need to input less than 6ms, you must manually type in ("5us", "4us", etc.). You will then see it convert to .005 ms, .004ms, etc.

###### 1. The control can be changed by selecting it and moving the mouse in a horizontal or vertical direction, or by selecting it and entering the new value on your keyboard, pressing Enter or clicking off of the control.

[Control Pins](javascript:void(0))

### Input *<n>*

There is one set of **Control Pins** ( **Delay**, **Gain**, **Mute**) for each **Input**/ **Output** intersection.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Output *<n>* Delay | 0.000 to 60.0 | 0 ms to 60.0 s | 0.000 to 1.00 | Input / Output |
| Output *<n>* Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Output *<n>* Mute | 0  1 | unmute  mute | 0  1 | Input / Output |

### Label Controls

There is one **Control Pin** for each **Input Label** and each **Output Label** when the **Label Controls** Property is set to Yes.

| Pin Name | String | Pins Available |
| --- | --- | --- |
| Input *<n>* Label | Text Edit Field | Input / Output |
| Output *<n>* Label | Text Edit Field | Input / Output |

### Input Gain

There is one **Control Pin** for each **Input Mute** button and each **Input Gain** fader when **Input Gain** Property is set to Yes.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Input *<n>* Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Input *<n>* Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
