# High-Pass Filter

> Source: https://help.qsys.com/Content/Schematic_Library/filter_highpass.htm

# High-Pass Filter

The High-Pass filter amplifies frequencies above a set frequency, and attenuates the frequencies below that set frequency. You can control the slope at which the gain rises from the attenuated frequencies to the set Gain of the passed (or amplified) frequencies.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Type** Property.

### Input Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the High-Pass Filter component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

### Output Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the High-Pass Filter component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

[Schematic Example](javascript:void(0))

In this example, we have all of our audio channels routed through a series of Equalizers and Filters before being delivered to our Amplifiers. The High-Pass Filter provides loudspeaker protection from subsonic frequencies, typically around 15-20Hz.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### High-Pass Filter Properties

#### Max Slope

Sets the maximum Slope allowable in the Control Panel for all of the filters.

### Channels

#### Type

Sets the type of **Channel** available for **Inputs** and **Outputs**.

#### Count

Only appears when choosing **Multi-Channel** as the **Type**. Sets the number of **Channels** for **Multi-channel**. You can choose between 2 and 256.

### Response Panel

#### Enabled

Determines if the Response Panel is visible in the Control Panel

#### Size

Determines the size of the Response Panel.

[Controls](javascript:void(0))

#### Response Panel

The Response panel provides vertical and horizontal cross-hairs with a dynamic frequency and dB read-out. Place the mouse courser over the graph to activate the cross-hairs. When the Phase control is activated, the horizontal cross-hair line to the left of center represents the normal curve, the right side represents the phase curve. The readout is only for the normal curve.

#### Phase

Turns the Phase curve on and off.

#### Bypass

Bypasses the filter.

#### Invert

Inverts the output signal.

#### Mute

Mutes the output signal.

#### Frequency (Hz)

Sets the frequency at which the gain of the output reaches a point 3 dB below the maximum as set by the Gain control. Frequencies below this frequency are attenuated. All frequencies above this frequency are amplified based on the setting of the Gain control.

#### Q-factor

The Q-factor determines the sharpness of the gain slope as it rises to meet the cutoff frequency.

A Q of 1.00 causes a constant slope directly to the maximum Gain at the cutoff frequency, a slight rise above the maximum Gain, then gradually falls back to the maximum Gain as frequency increases. The result is an even rise in gain to the cutoff frequency, and a fairly flat amplification of the frequencies from the cutoff frequency and higher.

A Q of 10 causes a sharp spike of 20 dB higher than the maximum Gain at the cutoff frequency, then a sharp decline to the maximum gain as the frequency increases. The result is the frequencies in a fairly narrow band around the cutoff frequency are amplified above the maximum Gain.

A Q of 0.100 causes a very slow, curved slope beginning right at the cutoff frequency up to the maximum Gain. The result is that the frequencies below the cutoff frequency are completely attenuated and the Gain above the cutoff frequency is slowly increased as frequency increases.

#### Gain (dB)

Sets the output Gain.

#### Slope (dB per Octave)

Sets the slope at which the gain rises from -100 dB to the level set by the Gain control. You can set the maximum allowed slope in the Properties.

The Linkwitz-Riley adjusts in 12 dB per Octave steps, all others adjust in 6 dB per Octave steps.

#### Type

Selects the type of filter.

#### Bessel Normalization

Sets the type of normalization for the Bessel-Thomson filter.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Bypass | 0  1 | active  bypass | 0  1 | Input / Output |
| Filter Type | 1.00  2.00  3.00  4.00  5.00 | Variable Q  Butterworth  Linkwitz-Riley  Bessel-Thomson  Chebyshev | 0  .25  .50  .75  1.0 | Input / Output |
| Frequency | 10.0 to 20,000 | 10 Hz to 20 kHz | 0.000 to 1.00 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| High-Pass (Bessel-Thomson) Normalization | 0  1  2  3 | -3 dB Flat Group Delay  -3 dB Mirror Magnitude  Natural Mirror Magnitude  Natural Phase Match | 0  .333  .667  1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Q | .100 to 10.0 | .100 to 10.0 | 0.000 to 1.00 | Input/Output |
| Slope | 6.0  12.0  18.0  24.0  30.0  36.0  42.0  48.00  54.0  60.0  66.0  72.0  78.0  84.0  90.0  96.0 | 6 dB/Oct  12 dB/Oct  18 dB/Oct  24 dB/Oct  30 dB/Oct  36 dB/Oct  42 dB/Oct  48 dB/Oct  54 dB/Oct  60 dB/Oct  66 dB/Oct  72 dB/Oct  78 dB/Oct  84 dB/Oct  90 dB/Oct  96 dB/Oct | 0.00  .067  .133  .200  .267  .333  .400  .467  .533  .600  .667  .733  .800  .867  .933  1.00 | Input / Output |
