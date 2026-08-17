# Responsalyzer Component

> Source: https://help.qsys.com/Content/Schematic_Library/responsalyzer.htm

# Responsalyzer

The Responsalyzer is used to measure the system response. This can be in any venue, or the response of components in a Q-SYS design.

There is a limit of four Responsalyzers in a design.

There are two inputs to the Responsalyzer, and no outputs:

* **Measurement** - This is usually a microphone placed somewhere in the venue, or the output of one or a series of components in a Q-SYS design.
* **Reference** - This is a constant input containing all the frequencies of the audio band (20 Hz to 20 kHz), usually white or pink noise. The Reference signal is not used for RTA measurements.

[Inputs and Outputs](javascript:void(0))

### Input Pins

#### Measurement

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Responsalyzer component only has two input pins available.

### Output Pins

This component does not have any output pins available.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Responsalyzer Properties

#### RTA Bandwidth

Sets the bandwidth for the RTA measurements. The default is 1/12 Octave.

This sets the resolution logarithmically and should be adjusted along with the FFT size. You can choose from the following:

* 1 Octave
* 1/3 Octave
* 1/6 Octave
* 1/12 Octave
* 1/24 Octave

#### FFT Size

Sets the resolution and response of the RTA measurements linearly.

The larger the FFT bin, the slower the response with greater resolution. A smaller FFT bin size gives faster response with less resolution. You can choose from the following:

* 512
* 1024
* 2048
* 4096
* 8192
* 16384 (Default)
* 32768
* 65536

#### Time Constant Controls

Enable or disable the RTA Time Constant and Response Time Constant controls.

[Controls](javascript:void(0))

There are two inputs to the Responsalyzer: Measurement, and Reference.

### Measurement

#### Gain Bypass

Bypasses the Measurement Gain control when engaged.

#### Gain (dB)

Sets the Gain for the Measurement input signal.

### Reference

#### Delay Bypass

Bypasses the Reference Delay when engaged.

#### Auto Set Delay

This trigger button sets the delay based on the conditions when the button was clicked

#### Delay (ms / seconds)

Manually sets the delay of the Reference signal.

### Response

#### Response Graph

The scales for the Response Graph vary depending on the measurement method you select, see below.

When the X axis is frequency, the horizontal movement of the vertical crosshair cursor snaps to the bandwidth setting in the Responsalyzer Properties, 1 octave, 1/3 octave, and so on.

The vertical movement of the horizontal crosshair follows the magnitude or amplitude of the signal at the point of intersection with the vertical crosshair.

There are 10 octaves spanning the audio frequency range. The frequency is doubled (or halved) for each octave.

When Mag or Mag/Phase is selected, there is an orange line visible at the top of the graph. This line represents the Coherence of the Measurement signal compared to the Reference signal. The range is zero (at the bottom of the graph) to one at the top of the graph. Any coherence signal below 50% should be considered not usable.

#### Magnitude

Measures the magnitude of the Measurement input signal compared to the Reference Input signal over the audio frequency range. The green line is the Measurement Input signal.

Requires a Reference Input, typically the same source as the Measurement Input but prior to any EQ other DSP.

#### Magnitude / Phase

Same as the Magnitude selection but with the addition of a phase line (magenta) to compare the phase of the Measurement Input to the Reference Input. When both lines are the same across the frequency range, the phase is the same.

Requires a Reference Input, typically the same source as the Measurement Input but prior to any EQ other DSP.

#### Impulse

Measures the time difference of the energy pulse of the Measurement Input compared to the Reference Input. The Reference Input is at 0.0 on the X axis (not shown), and the Measurement Input pulse is displayed at the point on the X axis representing the time difference.

The Y axis displays the amplitude of the Measurement Input.

Requires a Reference Input, typically the same source as the Measurement Input but prior to any EQ other DSP.

**Note:** These two buttons display when Impulse is selected. Click the plus button to zoom in to display a range of 0 to 10.7 ms, and the â button to zoom out to display a range of 0.0 to 341.3 ms.

#### RTA

Measures the Measurement Input signal's magnitude over the audio frequency range. The RTA function does not use a Reference Signal.

### Averaging

#### RTA Time Constant

Available only when Properties > Time Constant Controls is set to 'Yes'. Controls how quickly the RTA graph responds to changes in the signal.

#### Response Time Constant

Available only when Properties > Time Constant Controls is set to 'Yes'. Controls how quickly the Magnitude, Magnitude/Phase, and Impulse graphs respond to changes in the signal.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Auto Set Delay | Trigger | | | Input / Output |
| Clear [1](#clear) | Trigger | | | Input / Output |
| Coherence | This control pin is a vector type output for use with a [Control Script](control_script_2.htm). | | | Output |
| Delay Bypass | 0  1 | no  bypassed | 0  1 | Input / Output |
| Frequencies | This control pin is a vector type output for use with a [Control Script](control_script_2.htm). | | | Output |
| Gain Bypass | 0  1 | no  bypassed | 0  1 | Input / Output |
| Impulse Response | This control pin is a vector type output for use with a [Control Script](control_script_2.htm). | | | Output |
| Impulse Response Length | This control pin is a vector type output for use with a [Control Script](control_script_2.htm). | | | Output |
| Magnitude Response | This control pin is a vector type output for use with a [Control Script](control_script_2.htm). | | | Output |
| Measurement Gain | -100 to 100 | -100dB to 100dB | 0 to 1.00 | Input / Output |
| Phase Response | This control pin is a vector type output for use with a [Control Script](control_script_2.htm). | | | Output |
| Reference Delay | 0 to 1.50 | 0ms to 1.5s | 0 to 1.00 | Input / Output |
| Response Averaging Time Constant | 400 to 10 | 400ms to 10.0s | 0 to 1.00 | Input / Output |
| RTA | This control pin is a vector type output for use with a [Control Script](control_script_2.htm). | | | Output |
| RTA Averaging Time Constant | 40.0 to 10 | 40.0ms to 10.0s | 0 to 1.00 | Input / Output |
| Short Impulse Response | This control pin is a vector type output for use with a [Control Script](control_script_2.htm). | | | Output |
| Update | This control pin is a vector type output for use with a [Control Script](control_script_2.htm). | | | Output |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1. The Clear trigger is used to clear the graph when you change or mute the input. | | | | |
