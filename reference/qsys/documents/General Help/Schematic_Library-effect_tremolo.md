# Tremolo Component

> Source: https://help.qsys.com/Content/Schematic_Library/effect_tremolo.htm

# Tremolo Component

The Tremolo Component allows you to modulate the gain of a mono input to get a mono or stereo output, or a stereo input to a stereo output. You can control the speed and amount of modulation along with the other parameters listed below.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **I/O Configuration**Property.

### Input Pins

#### Input

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Tremolo Effect component is set to a **Mono In / Mono Out**, which provides one input. Additionally, you can set the Properties to allow for **Mono In / Stereo Out**, which gives you one input, or you can set it to **Stereo In /Stereo** Out which will give you two inputs (Left and Right).

### Output Pins

#### Output

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Tremolo component is set to a **Mono In / Mono Out**, which provides one output. Additionally, you can set the Properties to allow for **Mono In / Stereo Out**, which gives you two outputs (Left and Right), or you can set it to **Stereo In /Stereo Out** which will also give you two outputs (Left and Right).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Tremolo Effect Properties

#### I/O Configuration

Sets the configuration of inputs and outputs for the Echo component. You can select **Mono In / Mono Out**, **Mono In / Stereo Out**, or **Stereo In / Stereo Out**.

[Controls](javascript:void(0))

#### Master Bypass

When engaged, this button bypasses all of the Tremolo's controls.

#### Stereo Spread (%)

Available when the I/O Configuration Property is set to Stereo In / Stereo Out.

Determines the separation spread between the channels. 0% is equal amount of each channel mixed to the other, 100% is complete separation of the channels.

#### High-Pass Frequency (Hz)

Frequencies below this frequency are attenuated. All frequencies above this frequency are amplified based on the setting of the Gain control.

#### Low-Pass Frequency (Hz)

Frequencies above this frequency are attenuated. All frequencies below this frequency are amplified based on the setting of the Gain control.

#### LFO Frequency (Hz)

The frequency at which the LFO produces the waveform, or LFO Shape. The LFO Frequency controls the frequency, or speed, at which the Delay is modulated.

#### LFO Shape

You can select one of 4 different waveforms.

#### LFO Stereo Spread (%)

The LFO produces two synchronized waveforms, one for each output channel. The LFO Spread determines the phase shift between these two waveforms. 0% is in phase, 100% is 180Â° out of phase.

When the waveforms are in phase, left audio gain is up and the right audio gain is up. When the waveforms are out of phase, the left audio gain is up, and the right audio gain is down.

#### Depth (%)

The amount or Depth of the gain modulation. When the Depth control is at 0%, the gain of both channels is not modulated. When the control is at 100%, the gain of both channels is modulated from no output to the Output Gain level.

#### Wet Solo

When engaged, allows you to listen to the wet signal by itself.

#### Wet Gain (dB)

Controls the gain of the wet output.

#### Dry/Wet Mix (%)

The percentage of wet to dry signal sent to the output. 0% is all dry signal, and no wet. 100% is all wet, and no dry.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Depth | 0.000 - 1.00 | .083ms - 1.00s | 0.00 - 1.00 | Input / Output |
| Dry/Wet Mix | 0.00 - 100 | â | 0.00 - 1.00 | Input / Output |
| High-Pass Frequency | 10.0 - 20,000 | 10Hz - 20kHz | 0.00 - 1.00 | Input / Output |
| LFO Frequency | 0.00 - 120 | .010Hz - 120Hz | 0.00 - 1.00 | Input / Output |
| LFO Stereo Spread | 0.00 - 100 | â | 0.00 - 1.00 | Input / Output |
| LFO Waveform | 1 - 14 | 1 - 14 | 0, .077, .154, .231, .308, .385, .462, .538, .615, .692, .769, .846, .923, 1.00 | Input / Output |
| Low-Pass Frequency | 10.0 - 20,000 | 10Hz - 20kHz | 0.00 - 1.00 | Input / Output |
| Master Bypass | 0  1 | no  bypassed | 0  1 | Input / Output |
| Modulation Depth | 0.000 - 100 | â | 0.00 - 1.00 | Input / Output |
| Output Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Stereo Spread | 0.00 - 100 | â | 0.00 - 1.00 | Input / Output |
| Wet Solo |  | normal  solo |  | Input / Output |
