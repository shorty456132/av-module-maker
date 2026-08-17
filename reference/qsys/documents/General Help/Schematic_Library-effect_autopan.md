# Auto-Pan Component

> Source: https://help.qsys.com/Content/Schematic_Library/effect_autopan.htm

# Auto-Pan Component

The Auto-Pan Component allows you to input a mono or stereo signal and automatically pan it between the channels of a stereo output. The stereo input channels can be panned in sync with each other, up to 180Â° out of sync. You can control the speed of the pan, and various other parameters as listed below.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **I/O Configuration**Property.

### Input Pins

#### Input

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Auto-Pan component is set to a **Mono In / Stereo Out**, which provides one input. Additionally, you can set the Properties to allow for **Stereo In / Stereo Out**, which gives you two inputs (Left and Right).

### Output Pins

#### Output

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Auto-Pan component is set to a **Mono In / Stereo Out**, which provides two outputs (Left and Right). Additionally, you can set the Properties to allow for **Stereo In / Stereo Out**, which also gives you two outputs(Left and Right).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Auto-Pan Effect Properties

#### I/O Configuration

Sets the configuration of inputs and outputs for the Auto-Pan component. You can choose between **Mono In / Stereo Out** or **Stereo In / Stereo Out**.

[Controls](javascript:void(0))

#### Master Bypass

Bypasses all of the Auto-Pan's controls.

#### Stereo Spread (%)

Available when the I/O Configuration Property is set to Stereo In/Stereo Out.

Determines the separation spread between the channels. 0% is equal amount of each channel mixed to the other, 100% is complete separation of the channels.

#### High-Pass Frequency (Hz)

Frequencies below this frequency are attenuated. All frequencies above this frequency are amplified based on the setting of the Wet Gain control.

#### Low-Pass Frequency (Hz)

Frequencies above this frequency are attenuated. All frequencies below this frequency are amplified based on the setting of the Wet Gain control.

#### LFO Frequency (Hz)

The frequency at which the LFO produces the waveform, or LFO Shape. The LFO Frequency controls the speed of the pan.

#### LFO Shape

You can select one of 4 different waveforms to control the shape of the pan envelope.

#### LFO Stereo Spread (%)

The LFO produces two synchronized waveforms, one for each output channel. The LFO Spread determines the phase shift between these two waveforms. 0% is in phase, 100% is 180Â° out of phase.

When the waveforms are in phase, left audio is panned hard left and the right audio is panned hard right then both into the middle. When the waveforms are out of phase, the left audio is panned hard left and the right audio panned hard left as well, then both to the right side.

#### Depth (%)

The amount or Depth of the pan modulation. When the Depth control is at 0%, the left input does not pan to the right output, and the right input does not pan to the left. When the control is at 100%, the left input pans fully to the right output, and the right pans fully to the left.

#### Wet Solo

When engaged, allows you to listen to the wet signal by itself.

#### Wet Gain (dB)

Controls the gain of the wet output.

#### Dry / Wet Mix (%)

The percentage of wet to dry signal sent to the output. 0% is all dry signal, and no wet. 100% is all wet, and no dry.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Depth | 0.000 - 100 | .083ms - 1.00s | 0.00 - 1.00 | Input / Output |
| Dry/Wet Mix | 0.00 - 100 | â | 0.00 - 1.00 | Input / Output |
| High-Pass Frequency | 10.0 - 20,000 | 10Hz - 20kHz | 0.00 - 1.00 | Input / Output |
| LFO Frequency | 0.01 - 120 | .010Hz - 120Hz | 0.00 - 1.00 | Input / Output |
| LFO Shape | 1 - 4 | Sine  Saw Up  Saw Down  Triangle | 0  .333  .666  1.00 | Input / Output |
| LFO Stereo Spread | 0.00 - 100 | â | 0.00 - 1.00 | Input / Output |
| Low-Pass Frequency | 10.0 - 20,000 | 10Hz - 20kHz | 0.00 - 1.00 | Input / Output |
| Master Bypass | 0  1 | no  bypassed | 0  1 | Input / Output |
| Stereo Spread | 0.00 - 100 | â | 0.00 - 1.00 | Input / Output |
| Wet Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Wet Solo |  | normal  solo |  | Input / Output |
