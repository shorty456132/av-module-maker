# Gain-Sharing Automatic Mic Mixer

> Source: https://help.qsys.com/Content/Schematic_Library/auto_mixer.htm

# Gain-Sharing Automatic Mic Mixer

The Gain-Sharing Automatic Mic Mixer takes a number of audio inputs, allowing one or more of the inputs to pass while attenuating others based on the level and, if Side Chain filters are used, the frequency of the input.

The Gain-Sharing Automatic Mic Mixer is primarily used for multiple live microphones operating in the same room together as a system â for example, in boardrooms, classrooms, churches, and courtrooms. The Gain-Sharing Automatic Mic Mixer controls the live microphones by turning up microphones when someone is talking and turning down microphones that are not used. It is a voice-activated, real-time process without an operator. The Gain-Sharing Automatic Mic Mixer controls the additive effect of multiple microphones being on at the same time and adapts to changing background noise conditions. The gain of each microphone input is calculated as the ratio of its RMS level to the combined RMS levels of all inputs. This ensures unity system gain at all times.

[Inputs and Outputs](javascript:void(0))

### Input Pins

#### Channels 1-*n*

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

The wiring between audio signal pins are the means by which the audio signal is passed from one DSP component to another. The number of signal pins is variable and set in the component's Properties. You can choose between 2 and 512 input channels. Input (sink) pins are on the left, output (source) pins are on the right.

### Output Pins

#### Audio Output

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

The wiring between audio signal pins are the means by which the audio signal is passed from one DSP component to another. The number of signal pins is variable and set in the component's Properties. You can choose **Mix-Only**, **Channel Only**, and **Mix and Channel**.

**Mix Only** gives a mix of all channels.

**Channel** only gives individual channel outputs.

**Mix and Channel** gives a combination.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Gain-Sharing Automatic Mic Mixer Properties

#### Channels

Determines the number of audio channels available.

#### Outputs

Determines the type of output available.

**Mix Only** gives a mix of all channels.

**Channel** only gives individual channel outputs.

**Mix and Channel** gives a combination.

#### Side-Chain Filter

When set to 'Yes', the internally-routed side-chain signal that controls the gate is modified by the filter settings you select in the Side-Chain section of the control panel. This affects the control of the gate, not the actual audio output.

When set to 'No', the actual input signals are used to control the gates.

**Note:** There is no dedicated side-chain input. The side-chain is routed internally from all inputs.

#### Detector Time

Sets one of three fixed Detector Times, or makes a variable control available in the Control Panel. All of these affect all of the channels.

[Controls](javascript:void(0))

[Setup](javascript:void(0))

#### Open Indicator Threshold (dB)

Sets the **Applied Gain** amount above which the **Open** indicator shows that the **Input** channel is open.

#### Depth (dB)

Sets the minimum amount of **Applied Gain** applied to the **Input** channels.

#### Rest Gain (dB)

Sets the amount of **Applied Gain** for all **Input** channels when none are open. When one or more channels are open, **Applied Gain** is being distributed towards the open channels, away from the closed channels.

#### Threshold Level (dBFS)

Sets the **Input** RMS level at which the **Applied Gain** begins to move away from the **Rest Gain**. Use this setting to control background noise (such as side conversations) when a mic is not in use.

#### Attack Time (seconds)

Determines how quickly **Applied Gain** moves towards 0 dB (unity gain) once the **Input** level exceeds the **Threshold Level**.

#### Hold Time (seconds)

Sets the minimum time an **Input** channel stays open once it is opened, or the length of time an **Input** channel stays open after the **Input** RMS level drops below the **Threshold Level**. Use this control to prevent the gate from opening and closing due to momentary pauses in the input.

#### Release Time (seconds)

Determines how quickly **Applied Gain** moves away from 0 dB once the **Input** level drops below the **Threshold Level** and the **Hold Time** has expired.

#### Detector Time (seconds)

Only available if **Detector Time** in [Properties](#Properti) is set to **Use Control**. This control determines the rate of change of the **Input** RMS detector output in response to changes in the **Input** signal. Use this adjustment to prevent abrupt changes in the input signal from causing unwanted, momentary output.

[Input](javascript:void(0))

#### Open (Indicator)

Indicates if the associated channel is open or not.

#### Applied Gain (dB)

Measures the attenuation applied to a particular **Input** channel. The gain is either zero or a negative value. Graphically the meter starts from the top, displaying attenuation in red going down.

#### Priority Gain (dB)

Adjusts the gain or attenuation applied to a particular **Input** channel. For example, you can boost the gain of a mic being used by a soft spoken person and attenuate the gain of a louder person so they can be heard equally in the room.

[Mix](javascript:void(0))

#### Mute (button)

Mutes the **Mix** channel output. This mutes all **Input** channels for the **Mix** output but does not affect the individual Output Channels.

#### Gain (dB)

Adjusts the **Mix** output channel gain. This applies to all **Input** channels on the **Mix** output, but does not affect the individual output channels.

[Side Chain](javascript:void(0))

**Note:** These controls are only available when **Side-Chain** Filter in [Properties](#Properti) is set to **Yes**.

#### Bypass (button)

Bypasses the **Side Chain** controls

#### Type (drop-down list)

Selects the **Side Chain** filter **Type.**

#### Bandwidth (octave)

Sets the bandwidth of the **Band-Pass**, **Band-Stop**, and **Parametric Side Chain** filters.

#### Frequency (Hz)

Sets the frequency parameter for all of the **Side Chain** filters.

#### Gain (dB)

Sets the gain parameter for the **Parametric**, **Low-Shelf** and **High-Shelf** filters.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Attack Time | 0.0001 to 100 | .100 ms to 100 ms | 0 to 1.00 | Input / Output |
| Bandwidth | .010 to 1.00 | .010 to 1.00 | 0 to 1.00 | Input / Output |
| Bypass | 0  1 | active  bypass | 0  1 | Input / Output |
| Depth | -40 to 0 | -40 dB to 0 dB | 0.000 to 1.00 | Input / Output |
| Detector Time | 0.0001 to 100 | .100 ms to 100 ms | 0.000 to 1.00 | Input / Output |
| Frequency | 10 to 20000 | 10 Hz to 20 kHz | 0.000 to 1.00 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Gain (Priority Gain) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Hold Time | 0.010 to 10 | 10.0 ms to 10 s | 0.000 to 1.00 | Input / Output |
| Meter (Applied Gain) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Mix Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Mix Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Open | 0  1 | false  true | 0  1 | Input / Output |
| Open Threshold | -40 to 0 | -40 dB to 0 dB | 0.000 to 1.00 | Input / Output |
| Release Time | 0.010 to 10 | 10.0 ms to 10 s | 0.000 to 1.00 | Input / Output |
| Rest Gain | -40 to 0 | -40 dB to 0 dB | 0.000 to 1.00 | Input / Output |
| Threshold Level | -80 to 0 | -80 dB to 0 dB | 0.000 to 1.00 | Input / Output |
| Type | 1.00  2.00  3.00  4.00  5.00  6.00  7.00 | Low-Pass  High-Pass  Band-Pass  Band-stop  Parametric  Low-Shelf  High-Shelf | 0  .167  .333  .500  .667  .833  1.00 | Input / Output |

[Troubleshooting](javascript:void(0)) 

There are some components that are unique in their operation in the **Emulate** mode. Some of these components are the **Audio Player**, **Crossfader**, **Gain Ramp**, and **Listen** buttons. For more information, see [Limitations](../Q-SYS_Designer/003_Emulate_Mode.htm#Limitations).
