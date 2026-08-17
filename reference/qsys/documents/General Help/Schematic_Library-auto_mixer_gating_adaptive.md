# Gating Automatic Mic Mixer Component (Relative Threshold)

> Source: https://help.qsys.com/Content/Schematic_Library/auto_mixer_gating_adaptive.htm

# Gating Automatic Mic Mixer

The Gating Automatic Mic Mixer (Relative Threshold) is typically used in applications with multiple microphones, and at times, multiple microphones being used at the same time. The channels open and close based on Threshold levels set for each channel, and optional Side Chain filters, or manual control. Attenuation controls help control feedback based on the number of microphones open at one time.

**Noise Floor Tracking**: Tracks the steady or slowly changing noise of equipment fans or HVAC. Instead of having to (repeatedly) adjust an absolute gate threshold that depends on the (varying) noise floor, a new relative threshold allows the gate to ride a (slowly) changing noise floor.

[Inputs and Outputs](javascript:void(0))

The Gating Automatic Mixer is capable of up to 512 channels:

* **Input**
   - 2 to 512 audio inputs, typically from microphones
* **Output**
   - three audio output modes
  + Channel Only - 2 to 512 channels directly from the associated input channel
  + Mix Only - 1-channel mix of all the input channels
  + Channel and Mix - both of the above.

[Schematic Example](javascript:void(0))

In this example, we have four Mics open at once. Through the Gating Automatic Mic Mixer, those signals are attenuated and then mixed out to an [Audio Recorder](audio_file_recorder2.htm).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Gating Automatic Mic Mixer Properties

The properties of a component are used in the Design phase to establish the size and characteristics of the component. They can be changed only in the Design Mode when the component is selected. Select and drag the Gating Automatic Mic Mixer component from the Schematic Library into the Schematic.

#### Channels

Sets the number of input and output channels for the Component.

#### Outputs

All inputs mixed into one output

One output channel per input channel, no mix is provided

Both

#### Side Chain Filter

**Yes** allows you to select various types of **Side Chain** filters in the Control Panel.

When you select **Side Chain**, the signal that controls the gate is filtered by the **Side Chain** settings. When **Side Chain** is not selected, the actual input signals are used to control the gates. The **Side Chain** filters do not affect the audio output, only the control of the gate.

#### Show Advanced Controls

Select 'Yes' to enable NOM Attenuation Type, Attenuation Step, and Max Attenuation controls in the control panel.

[Controls](javascript:void(0))

Controls are used during the design phase of a system to establish initial settings, and during normal system operation to make adjustments for different events. The controls can be adjusted only in Emulate or Run mode. Only Run mode actually processes audio. The controls listed below are divided into sections to match the Control Panel sections.

[Side Chain Controls](javascript:void(0))

The Side-Chain Filter is available only when Side-Chain Filter is set to Yes in the Properties.

#### Bypass (button)

Bypasses any **Side Chain** filtering effects.

#### Type (drop-down)

**Low-Pass** - Allows frequencies below the **Frequency** setting to pass unattenuated.

**High-Pass** - Allows frequencies above the **Frequency** setting to pass unattenuated.

**Band-Pass** - Allows frequencies within the **Bandwidth** to pass unattenuated. The **Bandwidth** is centered on the **Frequency** setting,

**Band-Stop** - Allows all frequencies to pass unattenuated except those within the **Bandwidth**. The **Bandwidth** is centered on the **Frequency** setting. Sometimes known as a Notch Filter.

**Parametric** - Allows control of all three parameters: Bandwidth, Frequency, and Gain.

**High-Shelf** - Allows you to boost or attenuate signals above the set **Frequency**. Frequencies below the set **Frequency** are not affected.

**Low-Shelf** - Allows you to boost or attenuate signals below the set **Frequency**. Frequencies above the set **Frequency** are not affected.

#### Bandwidth (octave)

Sets the bandwidth of the filter.

The control is available with the **Band-Pass**, **Band-Stop**, **Parametric Side Chain** filters.

#### Frequency (Hz)

Sets the upper, lower, or center frequency, depending on the filter.

The control is available with all filter types.

#### Gain (dBFS)

Controls the gain of the **Side Chain** signal.

The control is available with the **Parametric**, **Low-Shelf**, **High-Shelf** filters.

[Gate Controls](javascript:void(0))

#### Last Mic On (button)

Leaves the last microphone that was used in the open condition, until another microphone exceeds the **Threshold**.

#### Threshold Level Above Noise (dB)

**Noise Floor Tracking** follows the steady or slowly changing noise of equipment fans, HVAC, and so on. In order for a channel to open its gate, the signal must exceed the noise floor by the amount set by the **Threshold Level Above Noise** control.

#### Depth (dB)

The **Depth** knob sets the amount of attenuation applied to any input channel when the channel's gate is closed.

#### Hold Time (seconds)

The **Hold Time** knob the sets minimum time an input stays open once it is opened, or the length of time an input stays open after the RMS input level drops below the **Threshold Level**. This is to prevent the gate from opening and closing due to momentary pauses in the input.

[Channel Controls](javascript:void(0))

#### Open

Indicates if the associated channel is passing audio.

The Open LED is always on when the channel is in Manual Mode, and is always off when the **Post-Gate Mute** is enabled.

#### Default

The **Default** button allows a channel's gate to be forced open when no signals exceed the threshold level. The **Default** and **Last Mic On** controls are mutually exclusive, and only one channel **Default** can be enabled at a time.

#### Manual

The channel **Manual** control allows a channel to be removed from the auto-mix logic and excluded from **NOM**. The channel does not affect other channels and is always mixed, regardless of signal level.

#### Signal Level Above Noise (dB)

The **Signal Level Above Noise** meter indicates the signal level above the noise floor. It can be used as an aid in adjusting the **Threshold Level Above Noise** control.

#### Post-Gate Mute

The **Post-Gate Mute** button allows a channel to be included in the auto-mix logic but excluded from **NOM**. The channel is also excluded from the mix and its direct output is muted as well.

#### Post-Gate Gain (dB)

The **Post-Gate Gain** control adjusts the post-gate direct output level and mix level. It does not affect the auto-mix logic.

#### Name

The **Name** field allows the channel to have a user-defined name.

[NOM (Number of Open Mics)](javascript:void(0))

#### Max NOM

NOM is counted beginning at input 1 and once the maximum NOM has been reached gates will be closed for the remaining inputs. If you want a limited NOM to always contain the highest priority (open) inputs, assign input 1 the highest priority, and assign the rest of the inputs in descending priority order.

#### Direct Outs NOM Atten.

Normally, the NOM attenuation is applied to the mix output only, not the direct outputs. However,you may want to process and/or mix the direct outputs externally and not use the built-in NOM-attenuated mix output. "Direct Outs NOM Atten." allows you to get NOM attenuation to an external non-NOM mixer.

The default is ON, which applies the NOM attenuation to the direct outputs. In the OFF position, no attenuation is applied to the outputs.

#### NOM Attenuation Type[1](#Availabl)

When **Logarithmic** is selected, the output is attenuated by the amount specified by the Attenuation Step control for each open channel every time NOM is doubled.

Assuming an Attenuation Step of 1 dB

|  |  |
| --- | --- |
| NOM | Attenuation |
| 1 | 0 dB |
| 2 | 1 dB |
| 4 | 2 dB |
| 8 | 3 dB |

When **Linear** is selected, the output is attenuated by the amount specified by the **Attenuation Step** control for each open channel every time NOM increases by 1.

Assuming an Attenuation Step of 1 dB:

|  |  |
| --- | --- |
| NOM | Attenuation |
| 1 | 0 dB |
| 2 | 1 dB |
| 3 | 2 dB |
| 4 | 3 dB |

#### Attenuation Step (dB)[1](#Availabl)

The amount of attenuation added every time another mic opens, excluding the first mic opened.

#### Max Attenuation (dB)[1](#Availabl)

Sets the maximum amount of attenuation that can be applied to the output regardless of the NOM.

#### Response Time (seconds)

Adjusts the time constant that determines the time it takes for the attenuation to be applied to the output when there is a change in the NOM.

#### NOM (display)

The total number of open microphones.

#### Gain (dB)

Measures the output gain with respect to the amount of attenuation applied. For example, 40 dB of applied attenuation would result in a -40 dB change in the output gain.

###### 1. Available only when the Show Advanced Controls property is enabled.

[Mix](javascript:void(0))

#### Mute (button)

Mutes the **Mix** channel output. This mutes all **Input** channels for the **Mix** output but does not affect the individual Output Channels.

#### Gain (dB)

Adjusts the **Mix** output channel gain. This applies to all **Input** channels on the **Mix** output, but does not affect the individual output channels.

[Control Pins](javascript:void(0))

### Per Channel

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Default | 0  1 | disable  enable | 0  1 | Input / Output |
| Manual | 0  1 | disable  enable | 0  1 | Input / Output |
| Name | user-defined text | | | Input / Output |
| Open | 0  1 | false  true | 0  1 | Output |
| Post-Gate Gain | -100 to 10 | -100 dB to 10 dB | 0.000 to 1.00 | Input / Output |
| Post-Gate Mute | 0  1 | unmuted  muted | 0  1 | Input / Output |
| Signal Level Above Noise |  |  |  | Output |

### General

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Bandwidth | .010 to 1.00 | .010 to 1.00 | 0 to 1.00 | Input / Output |
| Bypass | 0  1 | active  bypass | 0  1 | Input / Output |
| Direct Outputs NOM Attenuation |  |  |  |  |
| Frequency | 10 to 20000 | 10 Hz to 20 kHz | 0.000 to 1.00 | Input / Output |
| Gain (Side Chain) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Gate Depth | 0 to 20 | 0 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Hold Time | 0.00 to 10 | 0ms to 10.0s | 0.000 to 1.00 | Output |
| Last Mic On | 0  1 | disable  enable | 0  1 | Input / Output |
| Linear NOM Attenuation | 0  1 | disable  enable | 0  1 | Output |
| Maximum NOM | 1 - *n* | 1 to *n* | 0.00 to 1.00 | Input / Output |
| Maximum NOM Attenuation | 0 to 20 | 0 dB to 40 dB | 0.000 to 1.00 | Input / Output |
| Mix Gain | -100 to 10 | -100 dB to 10 dB | 0.000 to 1.00 | Input / Output |
| Mix Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| NOM Response Time | 0.0001 to 1 | .100 ms to 1 s | 0.000 to 1.00 | Input / Output |
| NOM Attenuation Step | 0 to 20 | 0 dB to 40 dB | 0.000 to 1.00 | Input / Output |
| NOM Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Number of Open Mics | 0 to *n* | 0 to *n* | 0 to 1.00 | Output |
| Threshold Level Above Noise | 0.00 to 50 | 0dB to 50.0dB | 0.000 to 1.00 | Input / Output |
| Type | 1.00  2.00  3.00  4.00  5.00  6.00  7.00 | Low-Pass  High-Pass  Band-Pass  Band-stop  Parametric  Low-Shelf  High-Shelf | 0  .167  .333  .500  .667  .833  1.00 | Input / Output |
