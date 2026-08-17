# Pitch Shifter Component

> Source: https://help.qsys.com/Content/Schematic_Library/effect_pitch.htm

# Pitch Shifter Component

The Pitch Shifter Component takes an input signal and shifts the frequency of that signal to a specified distance, either up, down or both, from the input signal. The input signal is the dry output, and the shifted frequencies are the wet signal. You can use this to de-tune an instrument to produce a "thicker" sound similar to a chorus effect. In addition, you can take the input signal up / down a full octave to add a different "voice" to the output. The Pitch Shifter can be used on any kind of audio signal.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **I/O Configuration**Property.

### Input Pins

#### Input

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Pitch Shifter Effect component is set to a **Mono In / Stereo Out**, which provides one input. Additionally, you can set the Properties to allow for **Mono In / Mono Out**, which gives you one input, or you can set it to **Stereo In /Stereo** Out which will give you two inputs.

### Output Pins

#### Output

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Pitch Shifter Effect component is set to a **Mono In / Stereo Out**, which provides two outputs (Left and Right). Additionally, you can set the Properties to allow for **Mono In / Mono Out**, which gives you one output, or you can set it to **Stereo In /Stereo Out** which will also give you two outputs (Left and Right).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Pitch Shifter Component Properties

#### I/O Configuration

Sets the configuration of inputs and outputs for the Chorus component. You can choose **Mono In / Mono Out**, **Mono In / Stereo Out**, **Stereo In / Stereo Out**.

#### Max Delay (milliseconds)

Sets the maximum delay allowed for the Delay knob in the component's control panel.

[Controls](javascript:void(0))

#### Master Bypass

Bypasses all of the component's controls.

#### Stereo Spread (%)

Available when the I/O Configuration Property is set to Stereo In/Stereo Out.

Determines the separation spread between the channels. 0% is equal amount of each channel mixed to the other, 100% is complete separation of the channels.

#### Detection Frequency (Hz)

This is the mid-point of the range of frequencies you want to be shifted.

#### Left / Right Detected Pitch (Hz)

Displays the frequency, or pitch, of the input signal. You can use this to assist in setting the Detection Frequency.

When the I/O Configuration is set to Mono In, only one Detected Pitch field is available.

#### Left / Right Pitch Shift (Â¢ cent)

Sets the distance you want to shift the output wet signal from the input dry signal. When the input audio signal changes pitch, the output signal follows the changes directly.

1200 cents is an octave.

When the I/O Configuration is set to Mono Out, only one Pitch Shift field is available.

#### Crossfade Time (ms)

In order to raise or lower the pitch of a signal, the Pitch Shifter speeds up the input, or slows it down. This means you end up with a shorter or longer set of samples than the actual input. The Pitch Shifter either duplicates a set of samples and plays it back again, or truncates the set of samples.

The Crossfade Time adjusts the transition time between sets of samples. A shorter time gives you a more abrupt transition, a longer time produces a smoother transition.

#### Left / Right Delay (ms)

The Delay Time delays the wet signal from the dry signal.

**Note:** Entering anything from 0.001Âµs to 0.005Âµs gets interpreted as 1.00 through 5.00 milliseconds. Entering anything greater than 0.005 gets interpreted as the milliseconds as entered (example 0.006 gets interpreted as .006 ms). The basic idea is that the value that you enter is larger than the max value and Q-SYS Designer assumes you want the value to be divided by 1000. If you need to input less than 6ms, you must manually type in ("5us", "4us", etc.). You will then see it convert to .005 ms, .004ms, etc.

#### High-Pass Frequency (Hz)

Frequencies below this frequency are attenuated. All frequencies above this frequency are amplified based on the setting of the Gain control.

#### Low-Pass Frequency (Hz)

Frequencies above this frequency are attenuated. All frequencies below this frequency are amplified based on the setting of the Gain control.

#### Wet Gain (dB)

Controls the gain of the wet output.

#### Dry/Wet Mix (%)

The percentage of wet to dry signal sent to the output. 0% is all dry signal, and no wet. 100% is all wet, and no dry.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Crossfade Time | 0 to .100 | 0.100ms - 100ms | 0.00 - 1.00 | Input / Output |
| Detection Frequency | 81.4 to 660 | 81.4Hz - 660Hz | 0.00 - 1.00 | Input / Output |
| Dry/Wet Mix | 0.00 to 100 | â | 0.00 - 1.00 | Input / Output |
| High-Pass Frequency | 20.0 to 20,000 | 20Hz - 20kHz | 0.00 - 1.00 | Input / Output |
| Left Delay | 0.000 to 0.100 | 0.00ms - 100ms | 0.00 - 1.00 | Input / Output |
| Left Detected Pitch | 41.4 to 1263 | 41.4Hz - 1.26kHz | 0.013 - 0.803 | Output |
| Left Pitch Shift | -1300 to 1300 | -1300Â¢ - 1300Â¢ | 0.00 - 1.00 | Input / Output |
| Low-Pass Frequency | 20.0 to 20,000 | 20Hz - 20kHz | 0.00 - 1.00 | Input / Output |
| Master Bypass | 0  1 | no  bypassed | 0  1 | Input / Output |
| Right Delay | 0.000 to 0.100 | 0.00ms - 100ms | 0.00 - 1.00 | Input / Output |
| Right Detected Pitch | 41.4 to 1263 | 41.4Hz - 1.26kHz | 0.013 - 0.803 | Output |
| Right Pitch Shift | -1300 to 1300 | -1300Â¢ - 1300Â¢ | 0.00 - 1.00 | Input / Output |
| Stereo Spread | 0.00 to 100 | â | 0.00 - 1.00 | Input / Output |
| Wet Gain | -60 to 10 | -60 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Wet Solo | 0  1.0 | normal  solo | 0.00  1.00 | Input / Output |
