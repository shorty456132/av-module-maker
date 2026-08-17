# Peak Limiter

> Source: https://help.qsys.com/Content/Schematic_Library/limiter_peak.htm

# Peak Limiter

The Peak Limiter limits the output level to the Threshold Level plus the Applied Gain (attenuation). You can have from 1 to 256 Input channels collectively controlled by the Peak Limiter.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Type** Property.

### Input Pins

#### Input

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Peak Limiter component is set to a **Mono** channel, which provides one input. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs.

### Output Pins

#### Output

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Peak Limiter component is set to a **Mono** channel, which provides one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 outputs.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Peak Limiter Properties

#### Side Chain Input

For each standard input, an additional input is provided for an alternate control of the Peak Limiter. When the Side Chain is set to yes, the standard inputs have no control over the limiter.

**In Gain** is always applied to the Side Chain input signal, regardless of the state of **Bypass**.

The output is limited by the Side Chain Input level and its relation to the Threshold Level regardless of the level of the main Input.

#### Detector Time

Sets one of three pre-set Detector Times, or the Detector Time control in the Control Panel.

The **Detector Time** adjusts the rate of change of the **Detector** level in response to changes in the input signal.  
This adjustment is to prevent changes (spikes, low frequency signals) in the input from causing unwanted, momentary output.

#### Bypass Gain Meter

When set to **Active**, the **Applied Gain** meter is active regardless of the state of the **Bypass** button. This means you can adjust the Peak Limiter in Bypass mode.

When set to **Inactive**, the Applied Gain meter is inactive to indicate that the component is in Bypass mode.

### Channels

#### Type

Sets the type of input and output channels. You can select between **Mono**, **Stereo**, and **Multi-Channel**.

#### Count

For Multi-Channel, sets the number of channels.

[Controls](javascript:void(0))

### General

#### In Gain (dB)

Sets the Gain of the Input. This is added to the output Gain when the Input Level is below the Threshold Level, and added to the level of the Applied Gain or attenuation when the Input signal is above the Threshold Level.

#### Detector (dB)

Measures the level of either the main Input, or the Side Chain Input to determine when the Peak Limiter begins limiting.

#### Response Panel

The Response Panel graphically shows the Input Gain, the Threshold Level.

#### Bypass

Bypasses the Peak Limiter - regardless of the Input level.

#### Applied Gain (dB)

The **Applied Gain** meter is a representation of the amount of attenuation applied to the input channel. The Applied Gain is always either zero or negative.

#### Out Gain (dB)

Adjusts the output level of the Gate.

### Gain Calculations

#### Threshold Level

Sets the level at which the Peak Limiter has an effect, and the level at which the output is held.

### Time Constants

#### Detector Time (seconds)

Available only when **Detector Time Property** is set to **Use Control**.

The **Detector Time** adjusts the rate of change of the **Detector** level in response to changes in the input signal.  
This adjustment is to prevent changes (spikes, low frequency signals) in the input from causing unwanted, momentary output.

#### Attack Time (seconds)

The **Attack Time** adjusts the time it takes for the output amplitude to rise to equal 63% of the input amplitude once the **Threshold Level** is exceeded. This does not affect the decay of the signal.

#### Release Time (seconds)

The **Release Time** adjusts the time it takes for the output to fall to 63% of unity with the **Input**, after the **Detector** level drops below the **Threshold Level**.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Applied Gain | 0 to -40 | 0 dB to -40 dB | 0.000 to 1.00 | Output |
| Attack Time | 0.0001 to 100 | .100 ms to 100 ms | 0.000 to 1.00 | Input / Output |
| Bypass | 0  1 | active  bypass | 0  1 | Input / Output |
| Detector Level | -60 to 20 | -60 dB to 20 dB | 0.000 to 1.00 | Output |
| Detector Time | 0.0001 to 100 | .100 ms to 100 ms | 0.000 to 1.00 | Input / Output |
| Input Gain | -20 to 20 | -20 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Output Gain | -20 to 20 | -20 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Release Time | 0.010 to 10 | 10.0 ms to 10 s | 0.00 to 1.00 | Input / Output |
| Threshold Level | -60 to 20 | -60 dB to 20 dB | 0.000 to 1.00 | Input / Output |
