# Reverb Effect Component

> Source: https://help.qsys.com/Content/Schematic_Library/effect_reverb.htm

# Reverb Effect Component

The Reverb Component allows you to add an effect to your audio that simulates the sound in a hall or room where the sound is reflected off the surfaces of the room. There are two types of reverbs to choose from; Lush and Dense, each has their own set of presets or Types.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **I/O Configuration**Property.

### Input Pins

#### Input

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Reverb Effect component is set to a **Mono In / Stereo Out**, which provides one input. Additionally, you can set the Properties to allow for **Mono In / Mono Out**, which gives you one input, or you can set it to **Stereo In /Stereo Out** which will give you two inputs.

### Output Pins

#### Output

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Reverb Effect component is set to a **Mono In / Stereo Out**, which provides two outputs (Left and Right). Additionally, you can set the Properties to allow for **Mono In / Mono Out**, which gives you one output, or you can set it to **Stereo In /Stereo Out** which will also give you two outputs (Left and Right).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Reverb Effect Properties

#### I/O Configuration

Provides a choice of mono or stereo inputs. The output is always stereo. You can choose **Mono In / Stereo Out** or **Stereo In / Stereo Out**.

#### Reverb Type

There are two types of reverbs available. You can choose **Lush** or **Dense**.

[Controls](javascript:void(0))

### Lush Reverb

The following controls, with the exception of the Dry/Wet Mix, have an effect only on the wet (reverberant) signal.

#### Master Bypass

Bypasses the effect. Audio is passed without any change.

#### Low-Cut Frequency (Hz)

Cuts or attenuates frequencies below the set frequency. Used with the High-Cut frequency setting, you can define the range of frequencies you want to be reverberated.

#### High-Cut Frequency (Hz)

Cuts or attenuates frequencies above the set frequency. Used with the Low-Cut frequency setting, you can define the range of frequencies you want to be reverberated.

#### Low Reverb Time (seconds)

The amount of time it takes for the low frequency reflections to decay 60 dB (unable to hear any reflections) from the original source.

#### Crossover Frequency (Hz)

Sets the crossover frequency between the High- and Low-Reverb time.

#### High Reverb Time (seconds)

The amount of time it takes for the high frequency reflections to decay 60 dB from the original source.

#### Pre-Delay (milliseconds)

Sets the time interval between input signal and the first reflection.

#### Size (meters)

Sets the time that it takes for the reverb to decay by 60 dB - to a point where you can no longer hear any reflections. The Range depends on the Type, so the Range shown is the minimum of any type and the maximum of any type.

#### Diffusion (%)

Diffusion is sound bouncing off a multi-faceted wall as opposed to a flat wall. This control sets the amount of reflections from the multi-faceted wall.

#### Dry / Wet Mix (%)

The percentage of wet to dry signal sent to the output. 0% is all dry signal, and no wet. 100% is all wet, and no dry.

#### Type

The Type is a number of pre-defined settings or presets. Refer to the table below for the default settings associated with the presets.

|  | Rich Plate | Vocal Plate | Small Room | Large Room | Large Hall |
| --- | --- | --- | --- | --- | --- |
| Low-Cut Frequency (Hz) | 20 | 60.5 | 20.0 | 20.0 | 48.0 |
| High-Cut Frequency (Hz) | 12.0k | 12.1k | 20.0k | 7.98k | 12.0k |
| Low Reverb Time (seconds) | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Crossover Frequency (Hz) | 1.01k | 8.00k | 4.02k | 3.99k | 3.80k |
| High Reverb Time (seconds) | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Pre-Delay (milliseconds) | 1.33 | 20.0 | 1.33 | 1.33 | 1.33 |
| Size (meters) | 24.2m | 15.8 | 10.0 | 19.1 | 37.1 |
| Diffusion (%) | 42.7 | 100 | 73.8 | 71.0 | 40.5 |
| Dry/Wet Mix (%) | 100 | 100 | 100 | 100 | 100 |

### Dense Reverb

The following controls, with the exception of the Dry/Wet Mix, have an effect only on the wet (reverberant) signal.

#### Master Bypass

Bypasses the effect. Audio is passed without any change.

#### High-Pass Frequency (Hz / kHz)

Passes audio above this frequency setting. Attenuates frequencies below this frequency. Used with the Low-Pass frequency setting, you can define the range of frequencies you want to be reverberated.

#### Low-Pass Frequency (kHz)

Passes audio below this frequency setting. Attenuates frequencies above this frequency. Used with the High-Pass frequency setting, you can define the range of frequencies you want to be reverberated.

#### Reverberation Time (ms / s)

Sets the time that it takes for the reverb to decay by 60 dB - to a point where you can no longer hear any reflections.

#### High Ratio

Changes the amount of high frequency reflections.

#### Initial Delay (ms)

Sets the time interval between input signal and the first reflection.

#### Diffusion (%)

Diffusion is sound bouncing off a multi-faceted wall as opposed to a flat wall. This control sets the amount of reflections from the multi-faceted wall.

#### Reverberation Delay (ms)

Changes the delay time between the reflections.

#### Early Reflections Level

Changes the amplitude of the Early Reflections.

#### Dry / Wet Mix (%)

The percentage of wet (reverberant) to dry (no effects) signal sent to the output. 0% is all dry signal, and no wet. 100% is all wet, and no dry.

#### Type

The Type is a number of pre-defined settings or presets. Refer to the table below for the default settings associated with the presets.

|  | Wood Room | Vocal Plate | Thin Plate | Concert Hall |
| --- | --- | --- | --- | --- |
| High-Pass Frequency | 80.8 Hz | 20.0 Hz | 80.8 Hz | 50.2 Hz |
| Low-Pass Frequency | 20.0 kHz | 20.0 kHz | 20.0 kHz | 20.0 kHz |
| Reverberation Time | 1.50 s | 2.40 s | 1.90 s | 3.50 s |
| High Ratio | 0.700 | 1.00 | 0.800 | 0.800 |
| Initial Delay | 20 ms | 35.2 ms | 31.0 ms | 80.5 ms |
| Diffusion | 30.0% | 57.6% | 82.9% | 50.5 % |
| Reverberation Delay | 0 ms | 0 ms | 0 ms | 0 ms |
| Early Reflections Level | 0.629 | 0.189 | 0.097 | 0.499 |
| Dry/Wet Mix (%) | 100 % | 100 % | 100 % | 100 % |

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

### Lush Reverb

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Crossover Frequency | 100 - 8000 | 100 Hz to 8 kHz | 0 - 1.00 | Input / Output |
| Diffusion | 0 - 100 | â | 0 - 1.00 | Input / Output |
| Dry/Wet Mix | 0 - 100 | â | 0 - 1.00 | Input / Output |
| High Reverb Time | .200 - .4.00 | .200 to .4.00 | 0 - 1.00 | Input / Output |
| High-Cut Frequency | 100 - 20000 | 100 Hz to 20.0 kHz | 0 - 1.00 | Input / Output |
| Low Reverb Time | .200 - .4.00 | .200 to .4.00 | 0 - 1.00 | Input / Output |
| Low-Cut Frequency | 20 - 1000 | 20.0 Hz to 1.0 kHz | 0 - 1.00 | Input / Output |
| Master Bypass | 0  1.00 | no  bypassed | 0  1.00 | Input / Output |
| Pre-Delay | .001 - .200 | 1.33 ms to 200 ms | 0 - 1.00 | Input / Output |
| Selector |  |  |  | Input / Output |
| Size | 4.00 - 39.4 | 4.00 m to 39.4 m | 0 - 1.00 | Input / Output |
| Type | 1.00  2.00  3.00  4.00  5.00 | Rich Plate  Vocal Plate  Small Room  Large Room  Large Hall | .571  2.50  5.00  7.50  1.00 | Input / Output |

### Dense Reverb

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Diffusion | 0 - 100 | â | 0 - 1.00 | Input / Output |
| Dry/Wet Mix | 0 - 100 | â | 0 - 1.00 | Input / Output |
| Early Reflections Level | 0 - 1.00 | 0 to 1.00 | 0 - 1.00 | Input / Output |
| High Ratio | .100 - 1.00 | .100 to 1.00 | 0 - 1.00 | Input / Output |
| High-Pass Frequency | 20 - 1000 | 20.0 Hz to 1.00 kHz | 0 - 1.00 | Input / Output |
| Initial Delay | 0 - .200 | 0 ms to 200 ms | 0 - 1.00 | Input / Output |
| Low-Pass Frequency | 1000 - 20000 | 1 kHz to 20 kHz | 0 - 1.00 | Input / Output |
| Master Bypass | 0  1.00 | no  bypassed | 0  1.00 | Input / Output |
| Reverberation Delay | 0 - .100 | 0 ms to 100 ms | 0 - 1.00 | Input / Output |
| Reverberation Time | .366 - 10.0 | 336 ms - 10.0 s | 0 - 1.00 | Input / Output |
| Selector |  |  |  | Input / Output |
| Type | 1.00  2.00  3.00  4.00 | Wood Room  Vocal Plate  Thin Plate  Concert Hall | 0  .333  .667  1.00 | Input / Output |
