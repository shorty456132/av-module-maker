# Chorus Component

> Source: https://help.qsys.com/Content/Schematic_Library/effect_chorus.htm

# Chorus Component

The Chorus mixes two identical signals, with one of the signals delayed by a small, slowly modulated amount. The Chorus produces peaks and notches in the output frequency spectrum, related to one another in a linear harmonic series. Modulating the delay time causes the peaks and notches to sweep up and down the frequency spectrum. The Chorus splits the input signal, delays and filters one of the signals (wet) then mixes it with the other signal (dry) to produce the effect.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **I/O Configuration**Property.

### Input Pins

#### Input

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Chorus component is set to a **Mono In / Mono Out**, which provides one input. Additionally, you can set the Properties to allow for **Mono In / Stereo Out**, which gives you one input, or you can set it to **Stereo In /Stereo** Out which will give you two inputs.

### Output Pins

#### Output

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Chorus component is set to a **Mono In / Mono Out**, which provides one output. Additionally, you can set the Properties to allow for **Mono In / Stereo Out**, which gives you two outputs (Left and Right), or you can set it to **Stereo In /Stereo Out** which will also give you two outputs (Left and Right).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Chorus Component Properties

#### I/O configuration

Sets the configuration of inputs and outputs for the Chorus component.

#### Max Delay (seconds)

Sets the maximum delay allowed for the Delay knob in the component's control panel.

[Controls](javascript:void(0))

#### Master Bypass

Bypasses all of the Chorus' controls.

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

You can select one of 4 different waveforms.

#### LFO Left / Right Phase (degrees - Â°)

Available when the I/O Configuration Property is set to Mono In / Stereo Out, or Stereo In / Stereo Out.

In either of the Stereo modes, the LFO produces two synchronized waveforms, one for each channel. The LFO Spread determines the phase shift between these two LFO waveforms. 0Â° is in phase, 180Â° is out of phase.

#### Delay (ms)

* The amount of time the wet signal is delayed from the dry signal.
* The center delay of the modulation, or Depth â the delay time is modulated around this time amount.
* Sets the maximum modulation Depth. If you set the Depth to it's maximum (100 ms) then the Delay amount will control the Depth amount.

#### Depth (%)

The amount or Depth of the delay modulation. The Depth control is limited by the Delay control setting.

#### Wet Solo

When engaged, allows you to listen to the wet signal by itself.

#### Wet Gain (dB)

Controls the gain of the wet output.

#### Dry / Wet Mix (%)

The percentage of wet to dry signal sent to the output. 0% is all dry signal, and no wet. 100% is all wet, and no dry

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Delay | 0.000 0.50 | .083ms â 50ms | 0.00 â 1.00 | Input / Output |
| Depth | 0.000 â 1.00 | 0.100 â 3.50ms | 0.00 â 1.00 | Input / Output |
| Dry/Wet Mix | 0.00 â 100 | â | 0.00 â 1.00 | Input / Output |
| High-Pass Frequency | 20.0 â 20,000 | 20Hz â 20kHz | 0.00 â 1.00 | Input / Output |
| LFO Frequency | 0.350 â 5.0 | 0.35Hz â 5Hz | 0.00 â 1.00 | Input / Output |
| LFO Left / Right Phase | 0.00 â 180 | â | 0.00 â 1.00 | Input / Output |
| LFO Shape | 1 â 4 | Sine  Saw Up  Saw Down  Triangle | 0  .333  .666  1.00 | Input / Output |
| Low-Pass Frequency | 20.0 â 20,000 | 20Hz â 20kHz | 0.00 â 1.00 | Input / Output |
| Master Bypass | 0  1 | no  bypassed | 0  1 | Input / Output |
| Stereo Spread | 0.00 â 100 | â | 0.00 â 1.00 | Input / Output |
| Wet Gain | -60 to 10 | -60 dB to 10 dB | 0.000 to 1.00 | Input / Output |
| Wet Solo | 0  1.0 | normal  solo | 0.00  1.00 | Input / Output |
