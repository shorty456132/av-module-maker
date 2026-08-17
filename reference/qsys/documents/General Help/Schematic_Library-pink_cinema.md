# Cinema Pink Noise Generator

> Source: https://help.qsys.com/Content/Schematic_Library/pink_cinema.htm

# Cinema Pink Noise Generator

The Cinema Pink Noise Generator produces random frequencies distributed uniformly in each octave band throughout the audio spectrum. At reference, D-Cinema pink noise level is set for 85 dBC at -20 dBFS signal resulting in a 20 dBFS headroom. Standard reference listening position is at about 2/3 of the way back in the auditorium. The resulting constrained dynamic range allows for optimum listening pleasure. Crest factor is around 2 db higher than with the regular [Pink Noise Generator](pink.htm).

[Schematic Example](javascript:void(0))

In this example, a Cinema Pink Noise Generator is plugged into an Amplifier which is sending the signal to Surround Sound Speakers. The Surround Sound Speakers will then generate Pink Noise.

**Note:** Using Cinema Pink Noise Generator is a helpful troubleshooting step when used in conjunction with the Signal Injector tool. This enables you to take the Cinema Pink Noise Generator and inject it at a component's audio input or output. For more information, see the [Signal Injector](injector.htm) topic.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Type** Property.

### Input Pins

This component does not have any input pins available.

### Output Pins

#### Channels 1 - n

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Cinema Pink Noise component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Cinema Pink Noise Generator Properties

### Channels

#### Type

Selects the range for the audio type of inputs. You can choose **Mono**, **Stereo**, or **Multi-Channel**.

#### Count

Only available when **Multi-Channel** is selected as the **Type**. Sets the number of channels. You can choose between 2 and 256 channels.

[Controls](javascript:void(0))

#### Mute

Mute the output of the Cinema Pink Noise Generator.

#### RMS Level (dBFS)

Controls the output level. You can also manually enter values for each, from -100 to 20 dB.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| RMS Level (dBFS) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
