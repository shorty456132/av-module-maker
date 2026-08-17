# Gating Automatic Mic Mixer Component (Legacy)

> Source: https://help.qsys.com/Content/Schematic_Library/auto_mixer_gated.htm

# Gating Automatic Mic Mixer (Legacy)

The Gated Automatic Mixer (Absolute Threshold - Legacy) is typically used in applications with multiple microphones, and at times, multiple microphones being used at the same time. The microphones in use can be prioritized using three different modes: Auto, Priority, and Filibuster or combinations of these. The channels open and close based on Threshold levels set for each channel, and optional Side Chain filters, or manual control. Attenuation controls help control feedback based on the number of microphones open at one time.

[Inputs and Outputs](javascript:void(0))

The Gated Automatic Mixer is capable of up to 512 channels:

* **Input**
   - 2 to 512 audio inputs, typically from microphones
* **Output**
   - three audio output modes
  + Channel Only - 2 to 512 channels directly from the associated input channel
  + Mix Only - 1-channel mix of all the input channels
  + Channel and Mix - both of the above.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Gating Automatic Mic Mixer (Legacy) Properties

The properties of a component are used in the Design phase to establish the size and characteristics of the component. They can be changed only in the Design Mode when the component is selected. Select and drag the Gated Automatic Mixer component from the Schematic Library into the Schematic.

#### Channels

Sets the number of input and output channels for the Component.

#### Outputs

All inputs mixed into one output

One output channel per input channel, no mix is provided

Both

#### Side Chain Filter

'Yes' allows you to select various types of **Side Chain** filters in the Control Panel.

When you select **Side Chain**, the signal that controls the gate is filtered by the **Side Chain** settings. When **Side Chain** is not selected, the actual input signals are used to control the gates. The **Side Chain** filters do not affect the audio output, only the control of the gate.

#### Show Advanced Controls

Select 'Yes' to enable NOM Attenuation Type, Attenuation Step, and Max Attenuation controls in the control panel.

[Controls](javascript:void(0))

Controls are used during the design phase of a system to establish initial settings, and during normal system operation to make adjustments for different events. The controls can be adjusted only in **Emulate** or Run mode. Only Run mode actually processes audio. The controls listed below are divided into sections to match the Control Panel sections.

[Input](javascript:void(0))

#### Open (indicator)

Indicates if the associated channel is open or closed.

**Note:** The Depth knob sets the amount of attenuation applied to any input channel when the channel's Gate is closed.

#### Manual (button)

Opens the channel until manually closed.

#### Mode (drop-down)

You can choose one of three modes for the channel.

**Auto Mode** opens the channel when the RMS input level exceeds the **Threshold**.

**Priority Mode** opens the channel when the RMS input level exceeds the **Threshold** and the **Priority** set for the channel is higher than any other **Priority** channel currently open.

**Filibuster Mode** opens the channel when the RMS input level exceeds the **Threshold** no other channels are open.

When the **Side Chain** is active, these modes are additionally modified by the selected filter.

#### Priority (integer)

Used to set the priority order of the channels. All inputs with the same priority can be open at the same time. This setting has no effect when the channel is not in Priority Mode.

**Note:** The higher the number, the higher the Priority.

**Tip:** Leave gaps in your priority lists so you can easily change the priority of one mic without having to shift other priorities to make room for a single change.

#### Threshold (dB)

Sets the peak level at which the gate opens and allows audio to pass on this channel.

[How Modes Interact](javascript:void(0))

| |  |  |  |  | | --- | --- | --- | --- | | **Is Open First** | Exceeds Threshold While Another Channel is Already Open | | | | Auto | Priority | Filibuster | | Auto | Open | Open | Open | | Priority | Open | Higher Priority - 1st is attenuated, 2nd is opened  Lower Priority - 1st stays open, 2nd is attenuated | Open | | Filibuster | Open | Open | 1st stays open  2nd is attenuated | | | |

[Mix](javascript:void(0))

#### Mute (button)

Mutes the **Mix** channel output. This mutes all **Input** channels for the **Mix** output but does not affect the individual **Output** channels.

#### Gain (dB)

Adjusts the **Mix** output channel gain. This applies to all **Input** channels for the **Mix** output, but does not affect the individual **Output** Channels.

[Gate](javascript:void(0))

#### Last Mic On (button)

Leaves the last microphone that was used in the open condition, until another microphone exceeds the **Threshold**.

#### ID Gating

When the ID Gating button is on, Q-SYS prevents multiple gates from opening if they are fed by the same source such as a talker who is positioned between two microphones.

#### Background Percentage (%)

This control provides adaptive threshold functionality.

This feature allows you to set the microphone **Threshold** levels fairly low for rapid response, but prevents the gates from opening when the background noise level rises.

The background signal is the sum of all the microphone input signals. The Background Percentage knob determines the percentage of background signal used to raise the **Threshold** levels.

**Tip:** Set the Threshold levels when the room is quiet, if the gates open when the room gets noisy, increase the Background Percentage until the gates close.

The following example uses a 5 dB difference between the **Threshold** level, and the background noise level, and shows the effective Threshold level compared to the Background Percentage knob setting.

**Threshold** level set at: -30dB

Background signal level from microphones: -25 dB

| Effective Threshold Level | Background % Knob |
| --- | --- |
| -30 dB | 0% |
| -26.8 dB | 25% |
| -24.5 dB | 50% |
| -22.6 dB | 75% |
| -21.1 dB | 100% |

#### Depth (dB)

The knob sets the amount of attenuation applied to any input channel when the channel's Gate is closed.

#### Hold Time (seconds)

The knob the sets minimum time an input stays open once it is opened, or the length of time an input stays open after the RMS input level drops below the **Threshold Level**. This is to prevent the gate from opening and closing due to momentary pauses in the input.

[NOM (Number of Open Mics)](javascript:void(0))

#### Max NOM

NOM is counted beginning at input 1 and once the maximum NOM has been reached gates will be closed for the remaining inputs. If you want a limited NOM to always contain the highest priority (open) inputs, assign input 1 the highest priority, and assign the rest of the inputs in descending priority order.

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

[Side Chain](javascript:void(0))

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

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

### Per Channel

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Manual | 0  1 | disable  enable | 0  1 | Input / Output |
| Mode | 0  1  3 | Auto  Prior  Filib (Filibuster) | 0  .500  1.00 | Input / Output |
| Open | 0  1 | false  true | 0  1 | Output |
| Priority Level | 1 to 10000 | 1 to 10000 | 0 to 1.00 | Input / Output |
| Threshold | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |

### General

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Default Settings | | | | |
| Background Percentage | 0.0 to 100 |  | 0.000 to 1.00 | Input / Output |
| Gate Depth | 0 to 20 | 0 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Hold Time | 0.00 to 10 | 0 ms to 1 s | 0.000 to 1.00 | Output |
| ID Gating | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Last Mic On | 0  1 | disable  enable | 0  1 | Input / Output |
| Linear NOM Attenuation | 0  1 | disable  enable | 0  1 | Output |
| Max NOM Attenuation | 0 to 20 | 0 dB to 40 dB | 0.000 to 1.00 | Input / Output |
| Maximum NOM | 1 - *n* | 1 to *n* | 0.00 to 1.00 | Input / Output |
| Mix Gain | -100 to 10 | -100 dB to 10 dB | 0.000 to 1.00 | Input / Output |
| Mix Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| NOM | 0 to *n* | 0 to *n* | 0 to 1.00 | Output |
| NOM Attenuation Step | 0 to 20 | 0 dB to 40 dB | 0.000 to 1.00 | Input / Output |
| NOM Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| NOM Response Time | 0.0001 to 1 | .100 ms to 1 s | 0.000 to 1.00 | Input / Output |
| Available with Side Chain | | | | |
| Bandwidth | .010 to 1.00 | .010 to 1.00 | 0 to 1.00 | Input / Output |
| Bypass | 0  1 | active  bypass | 0  1 | Input / Output |
| Frequency | 10 to 20000 | 10 Hz to 20 kHz | 0.000 to 1.00 | Input / Output |
| Gain (Side Chain) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Type | 1.00  2.00  3.00  4.00  5.00  6.00  7.00 | Low-Pass  High-Pass  Band-Pass  Band-stop  Parametric  Low-Shelf  High-Shelf | 0  .167  .333  .500  .667  .833  1.00 | Input / Output |
