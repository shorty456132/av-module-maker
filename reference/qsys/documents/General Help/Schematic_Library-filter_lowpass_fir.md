# FIR Low-Pass Filter Component

> Source: https://help.qsys.com/Content/Schematic_Library/filter_lowpass_fir.htm

# FIR Low-pass Filter Component

The FIR Low-pass Filter amplifies frequencies below a set frequency, and attenuates the frequencies above that frequency. The FIR filter offers a steeper cutoff slope than IIR filters, and can be configured to have a linear phase response.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Type** Property.

### Input Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the FIR Low-Pass Filter component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

### Output Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the FIR Low-Pass Filter component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### FIR Low-Pass Filter Properties

#### Transition Bandwidth (Octave)

Sets the bandwidth of the transition between the stopped frequencies and the passed frequencies.

#### Stopband Attenuation

Sets the attenuation level for the frequencies that are not passed.

#### Phase Response

Linear Phase - The delay is the same for all frequencies.

Minimum Phase - There is a minimal delay that varies with frequency.

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

**Note:** When controls are changed on a design in Run mode, the output is muted (approximately 1 second) while the new coefficient set is loaded.

#### Response Graph

The scales for the Response Graph vary depending on the measurement method you select.

The vertical line of the crosshair cursor provides a readout of its position on the X axis scale.

The vertical movement of the horizontal crosshair follows the magnitude or amplitude of the signal.

#### Phase

The phase difference between the output of the filter and its input.

#### Bypass

Bypasses the filter.

#### Invert

Inverts the audio signal through the filter.

#### Mute

Mutes the output of the filter.

#### Gain (dB)

Controls the gain of the audio signal for the frequencies passed through the filter.

#### Frequency (Hz)

Sets the low end of the frequencies passed through the filter. Frequencies above this setting are passed.

#### Group Delay (ms)

The time it takes for an audio signal to travel through the filter.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Bypass | 0  1 | active  bypass | 0  1 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Frequency | 10.0 to 20,000 | 10 Hz to 20 kHz | 0.000 to 1.00 | Input / Output |
| Group Delay | 0.250 to 240 | .250 ms to 240 ms | 0.000 to 1.00 | Output |
