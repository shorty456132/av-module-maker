# Band-Pass Filter Component

> Source: https://help.qsys.com/Content/Schematic_Library/filter_bandpass.htm

# Band-Pass Filter Component

The Band-Pass filter amplifies a set band of frequencies, centered around a set frequency, and measured at 3dB below the gain of the center frequency, while not amplifying any frequencies outside that band.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Type** Property.

### Input Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Band-Pass Filter component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

### Output Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Band-Pass Filter component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Band-Pass Filter Properties

### Channels

#### Type

Sets the type of input and output channels

#### Count

For Multi-Channel, sets the number of channels. You can choose between 2 and 256 channels.

### Response Panel

#### Enabled

Determines if the Response Panel is visible in the Control Panel

#### Size

Determines the size of the Response Panel.

[Controls](javascript:void(0))

#### Response Panel

The Response panel provides vertical and horizontal cross-hairs with a dynamic frequency and dB read-out. Place the mouse courser over the graph to activate the cross-hairs. When the Phase control is activated, the horizontal crosshair line to the left of center represents the normal curve, the right side represents the phase curve. The readout is only for the normal curve.

* X-Axis = Freq, 20 Hz to 20 kHz
* Y-Axis Left = dB, -24 dB to 24 dB
* Y Axis Right = Phase, -180Â° to -180Â°

#### Phase

Turns the Phase curve on and off.

#### Bypass

Bypasses the filter.

#### Invert

Inverts the output signal.

#### Mute

Mutes the output signal.

#### Gain (dB)

Sets the output Gain measured at the center frequency of the pass band.

#### Frequency (Hz)

Sets the center frequency of the band of frequencies allowed to pass through the filter.

#### Bandwidth (Octave)

Sets the width of the band of frequencies allowed to pass through the filter. Measured at 3dB below the amplitude of the center frequency.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Bandwidth | 0.010 to 3.00 | .010oct to 3.00oct | 0.000 to 1.00 | Input / Output |
| Bypass | 0  1 | active  bypass | 0  1 | Input / Output |
| Frequency | 10.0 to 20,000 | 10 Hz to 20 kHz | 0.000 to 1.00 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
