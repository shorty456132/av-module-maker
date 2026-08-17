# Graphic Equalizer

> Source: https://help.qsys.com/Content/Schematic_Library/equalizer_graphic.htm

# Graphic Equalizer

The Graphic Equalizer provides from 6 bands with 2 octaves per band up to 61 bands with 1/6th octave per band. Each band can be adjusted from -20dB to +20 dB.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Type** Property.

### Input Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Graphic Equalizer component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

### Output Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Graphic Equalizer component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Graphic Equalizer Properties

#### Band Count

Sets the number of bands available in the Equalizer. The number of bands defines how many octaves there are per band.

### Channels

#### Type

Sets the type of **Channel** available for **Inputs** and **Outputs**.

#### Count

Only appears when choosing **Multi-Channel** as the **Type**. Sets the number of **Channels** for **Multi-channel**. You can choose between 2 and 256.

### Response Panel

#### Enabled

Enables or disables the graphical Response graph.

#### Size

Sets the size of the graphical Response graph.

[Controls](javascript:void(0))

### Response

#### Response Panel

Graphically displays the output of the bands in the equalizer.

#### Type

Turns the Phase curve display on and off.

### Master

#### Bypass

Bypasses all bands of the equalizer.

#### Invert

Inverts the output signal of the equalizer.

#### Mute

Mutes the output of the equalizer

#### Gain (dB)

Sets the gain of the output of the equalizer.

### Frequency (band)

#### Bypass

Bypasses an individual frequency band.

#### Gain (dB)

Controls the output gain of an individual frequency band.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

Each band in the Crossover can have High and Low settings. The following table lists the duplicated settings only once.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| (band) Bypass | 0  1 | active  bypass | 0  1 | Input / Output |
| (band) Gain | -20 to 20 | -20 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Master Bypass | 0  1 | active  bypass | 0  1 | Input / Output |
| Master Gain | -20 to 20 | -20 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Master Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Master Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
