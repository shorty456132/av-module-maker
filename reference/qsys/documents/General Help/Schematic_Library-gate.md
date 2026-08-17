# Gate

> Source: https://help.qsys.com/Content/Schematic_Library/gate.htm

# Gate

The Gate Component (short for Noise Gate) is used to either pass or attenuate audio signals based on the RMS level of the input signal. If the signal is above the specified **Threshold**, the signal is passed un-attenuated. If the signal is below the **Threshold**, it is attenuated by the amount specified by the **Depth** control.

The Gate component controls its output based on the input level. If the input is lower than the Threshold level, it is attenuated. If the input is above the Threshold Level, it is amplified. You can use the Gate to prevent open microphones and other types of inputs, from introducing unwanted sounds into your system.

The Gate Component can be **Mono**, **Stereo**, or **Multi-channel**. The **Multi-channel** mode can have from 2 to 256 input/output channels. The Gate has an optional **Side Chain Input** for each input channel. The **Side Chain Input** provides a secondary input to the RMS Detector allowing the **Side Chain** to be used to trigger the Gate to open or close. The main **Input** is then attenuated or un-attenuated based on the **Side Chain Input** signal.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Gate Properties

#### Side Chain Input

For each standard input, an additional input is provided for alternate control of the Gate. When Side Chain is set to yes, the standard inputs have no control over the opening and closing of the gate.

**In Gain** is always applied to the Side Chain input signal, regardless of the state of **Bypass**.

#### Detector Time

Sets one of three pre-set Detector Times, or the Detector Time control in the Control Panel.

The **Detector Time** adjusts the time constant which determines the rate of change of the **Detector** level in response to changes in the input signal.  
This adjustment is to prevent changes (spikes, low frequency signals) in the input from causing unwanted, momentary output.

#### Bypass Gain Meter

When set to **Active**, the **Applied Gain** meter is active regardless of the state of the **Bypass** button. This means you can adjust the Gate in Bypass mode.

When set to **Inactive**, the Applied Gain meter is inactive to indicate that the component is in Bypass mode.

### Channels

#### Type

Sets the type of input and output channels. You can choose from **Mono**, **Stereo**, or **Multi-Channel**.

#### Count

For Multi-Channel, sets the number of channels.

[Controls](javascript:void(0))

### General

#### In Gain (dB)

Sets the Gain of the input. This is added to the level of the input source.

#### Detector (dB)

Measures the level of either the main Input, or the Side Chain Input to determine when the Gate opens or closes. The range of the graphic display is -60 to 20 dB, the text readout is the sum of the Input level plus the In Gain control.

#### Response Panel

The Response panel provides points at the Threshold Level and Depth that give current readings when the mouse passes over them.

#### Bypass

Bypasses the Gate - forces the Gate open regardless of the Input level.

### Gain Calculations

#### Threshold Level

Sets the level at which the Gate opens based on either the main Input level or the Side Chain level. The Threshold level is on the X axis of the graph.

#### Depth (dB)

Sets how much attenuation (Applied Gain) is applied to the inputs when they are below the Threshold Level. This is a negative amount added to the Detector Level. The Depth is on the Y axis of the graph.

### Time Constants

#### Attack Time (seconds)

The **Attack Time** adjusts the time it takes for the output amplitude to rise to equal 63% of the input amplitude once the **Threshold Level** is exceeded. This does not affect the decay of the signal.

#### Hold Time (seconds)

The **Hold Time** determines the minimum time the Gate stays open once it is opened, or the length of time the Gate stays open after the RMS input level drops below the **Threshold Level**. This is to prevent the gate from opening and closing due to momentary pauses in the input.

#### Release Time (seconds)

The **Release Time** adjusts the time it takes for the output to fall to 63% of the level set by the **Depth** control, after the **Detector** level drops below the **Threshold Level** and the **Hold Time** is expired.

#### Detector Time (seconds)

Available only when the **Detector Time Property** is set to **Use Control**.

The **Detector Time** adjusts the time constant which determines the rate of change of the **Detector** level in response to changes in the input signal.  
This adjustment is to prevent changes (spikes, low frequency signals) in the input from causing unwanted, momentary output.

### Gain

#### Open

The green LED **Open** indicator lights when the **Detector** level exceeds the **Threshold** and the Gate is open.

#### Applied Gain (-dB)

The **Applied Gain** meter is a representation of the amount of attenuation ( **Depth**) applied to the input channel.

#### Gain (dB)

Adjusts the output level of the Gate.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Applied Gain | 0 to -40 | 0 dB to -40 dB | 0.000 to 1.00 | Output |
| Attack Time | 0.0001 to 100 | .100 ms to 100 ms | 0.000 to 1.00 | Input / Output |
| Bypass | 0  1 | active  bypass | 0  1 | Input / Output |
| Depth | 0 to 60 | 0 dB to 60 dB | 0.000 to 1.00 | Input / Output |
| Detector Level | -60 to 20 | -60 dB to 20 dB | 0.000 to 1.00 | Output |
| Detector Time | 0.0001 to 100 | .100 ms to 100 ms | 0.000 to 1.00 | Input / Output |
| Hold Time | 0.010 to 10 | 10.0 ms to 10 s | 0.000 to 1.00 | Input / Output |
| Input Gain | -20 to 20 | -20 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Open | 0  1 | false  true | 0  1 | Output |
| Output Gain | -20 to 20 | -20 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Release Time | 0.010 to 10 | 10.0 ms to 10 s | 0.00 to 1.00 | Input / Output |
| Threshold Level | -60 to 20 | -60 dB to 20 dB | 0.000 to 1.00 | Input / Output |
