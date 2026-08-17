# White Noise Generator

> Source: https://help.qsys.com/Content/Schematic_Library/white.htm

# White Noise Generator

The White Noise Generator produces random frequencies across the audio spectrum on 1 to 256 output channels.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Type** Property.

### Input Pins

This component does not have any input pins available.

### Output Pins

#### Output

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the White Noise Generator component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### White Noise Properties

### Channels

#### Type

Sets the type of **Channel** available for **Inputs** and **Outputs**.

#### Count

Only appears when choosing **Multi-Channel** as the **Type**. Sets the number of **Channels** for **Multi-channel**. You can choose between 2 and 256.

[Controls](javascript:void(0))

#### Mute

Mutes the output for the associated band.

#### RMS Level (dB)

Adjusts the output gain for all channels.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| RMS Level | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Input / Output |
