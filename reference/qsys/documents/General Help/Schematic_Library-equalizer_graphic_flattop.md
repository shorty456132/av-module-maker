# Flattop Graphic Equalizer

> Source: https://help.qsys.com/Content/Schematic_Library/equalizer_graphic_flattop.htm

# Flattop Graphic Equalizer

The Flattop Graphic Equalizer component is similar to the standard Graphic Equalizer, but offers asymmetrical filtering for more precision tuning of loudspeaker responses. It provides from 6 bands with 2 octaves per band up to 61 bands with 1/6th octave per band. Each band can be adjusted from -20dB to +20dB.

Select the transition bandwidth in the component Properties. Responses of adjacent bands with identical gains sum perfectly.

The overall equalizer phase response is minimum-phase.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Type** Property.

### Input Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Flattop Graphic Equalizer component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

### Output Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Flattop Graphic Equalizer component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Flattop Graphic Equalizer Properties

#### Band Count

Sets the number of bands available in the Equalizer. The number of bands defines how many octaves there are per band.

Options:

* 6 bands - 2 Octaves per band
* 11 bands - 1 Octave per band (default)
* 16 bands - 2/3 Octave per band
* 31 bands - 1/3 Octave per band
* 61 bands - 1/6 Octave per band

#### Transition Bandwidth

The Transition Bandwidth determines how quickly the response transitions from the non-gain region to the gain region or vice versa. A wide (1 Octave) transition results in less computational resources being used while a narrow (1/12 Octave) transition results in more computational resources being used. If the default option (1/12 Octave) results in resource usage that is too high and if a wider transition bandwidth is acceptable, select a wider option.

Options: 1, 1/2, 1/3, 1/6, 1/12 Octave (default)

### Channels

#### Type

Sets the type of input/output channels: Mono, Stereo, or Multi-Channel. Multi-Channel enables the Count property.

#### Count

Set the number of input/output channels for Multi-Channel, from 2 to 256.

### Response Panel

#### Enabled

Enables or disables the graphical Response graph.

#### Size

Set the size of the graphical Response graph: Small, Medium, or Large.

[Controls](javascript:void(0))

### Response

#### Response Panel

Graphically displays the output of the bands in the equalizer.

X-Axis = Frequency, 20 Hz to 20 kHz

Y-Axis Left = dB, -20 dB to 20 dB

Y-Axis Right = Phase, -180Â° to 180Â°

#### Phase

Turns the Phase curve display on and off.

### Master

#### Bypass

Click to bypass all bands of the equalizer.

#### Invert

Click to toggle whether the output signal of the equalizer is inverted or normal.

#### Mute

Click to mute the output of the equalizer.

#### Gain

Adjust the overall gain of the equalizer, from -20dB to 20dB (default is 0dB).

### Frequency

#### Bypass

Click to bypass an individual frequency band.

#### Gain

Set the output gain of an individual frequency band, from -20dB to 20dB (default is 0dB).

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| 1kHz, 2kHz, 4kHz, 8kHz, 16Hz, 16kHz, 31.5Hz, 63Hz, 125Hz, 250Hz, 500Hz | | | | |
| Bypass | 0  1 | no  bypassed | 0  1 | Input / Output |
| Gain | -20.0 to 20.0 | -20.0dB to 20.0dB | 0.000 to 1.00 | Input / Output |
| Master | | | | |
| Bypass | 0  1 | no  bypassed | 0  1 | Input / Output |
| Gain | -20.0 to 20.0 | -20.0dB to 20.0dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  inverted | 0  1 | Input / Output |
| Mute | 0  1 | unmuted  mute | 0  1 | Input / Output |
