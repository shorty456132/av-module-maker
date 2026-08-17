# Dual-Shelf Equalizer Component

> Source: https://help.qsys.com/Content/Schematic_Library/equalizer_shelving_dual.htm

# Dual-Shelf Equalizer Component

The Dual-Shelf Equalizer allows you to control the gain of two groups of frequencies, one above, and one below an adjustable frequency, and also control the slope or transition between the two shelves. The adjustable Frequency is at the mid-point of the Filter Slope. Master controls allow you to Bypass, Invert, Mute, and control the Gain of the output of the equalizer.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Type** Property.

### Input Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Dual-Shelf Equalizer component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

### Output Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Dual-Shelf Equalizer component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Dual-Shelf Equalizer Properties

#### Filter Slope

Sets the slope, or transition between the two shelves. 6 dB per octave provides a slower transition, or softer slope, than 12 dB.

### Channels

#### Type

Sets the type of input and output channels

#### Count

For Multi-Channel, sets the number of channels. You can choose between 2 and 256 channels.

### Response Panel

#### Enabled

Enables or disables the graphical Response graph.

#### Size

Sets the size of the graphical Response graph.

[Controls](javascript:void(0))

#### Response Panel

The Response panel provides vertical and horizontal cross-hairs with a dynamic frequency and level read-out. Place the mouse courser over the graph to activate the cross-hairs. When the Phase control is activated, the horizontal cross-hair line to the left of center represents the normal curve, the right side represents the phase curve. The readout is only for the normal curve.

* X-Axis = 20Hz to 20kHz
* Y-Axis Left = -20dB to 20dB
* Y Axis Right = -180Â° to 180Â°

#### Phase

Turns the Phase curve display on and off.

#### Bypass

Bypasses the equalizer.

#### Invert

Inverts the output signal.

#### Mute

Mutes the output signal.

#### Master Gain (dB)

Controls the gain of the full frequency range.

#### Low Gain (dB)

Controls the gain of the Low shelf.

#### High Gain (dB)

Controls the gain of the High shelf.

#### Frequency (Hz)

Sets the frequency of the 3 dB point of the Filter Slope. The gain of frequencies from this point to the high end of the frequency range is controlled by the Gain knob.

#### Q-Factor

Q-Factor controls how abrupt the change from one shelf level to the other shelf level takes place.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Bypass (Master) | 0  1 | active  bypass | 0  1 | Input / Output |
| Frequency | 10 to 20000 | 10 Hz to 20 kHz | 0.000 to 1.00 | Input / Output |
| High Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert (Master) | 0  1 | normal  invert | 0  1 | Input / Output |
| Low Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Master Gain | -20 to 20 | -20 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Mute (Master) | 0  1 | unmute  mute | 0  1 | Input / Output |
| Q-Factor | 0.100 to 3.0 | .001 to 3.00 | 0.000 to 1.00 | Input / Output |
