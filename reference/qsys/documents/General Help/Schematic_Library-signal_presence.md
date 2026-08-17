# Signal Presence Component

> Source: https://help.qsys.com/Content/Schematic_Library/signal_presence.htm

# Signal Presence Component

The **Signal Presence** component detects the existence of an output signal based on an adjustable **Peak Threshold** and **Hold Time** for the peak.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Type** Property.

### Input Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Signal Presence component is set to a **Mono** channel, which provides one input. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs.

### Output Pins

This component does not have any output pins available.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Signal Presence Properties

This component has no configurable properties, other than Channels.

### Channels

#### Type

Sets the **Type** of **Channel** available.

#### Count

Sets the number of **Channels** available for **Multi-channel**.

[Controls](javascript:void(0))

#### Input Indicators 1 to*n*

The indicator(s) turn green when the input signal reaches the **Peak Threshold**, and will stay green until the input signal drops below the **Peak Threshold**, and the **Hold Time** expires.

#### Peak (dB)

Sets the peak value of the **Input** signal that will cause the **Input** indicator(s) to turn to green.

#### Hold Time

Sets the time that the indicator(s) will stay green after the peak value of the **Input** signal drops below the **Peak Threshold** setting.

#### Infinite Hold

Causes the **Input** indicator(s) to stay green, after the peak value of the **Input** signal reaches the **Peak Threshold** setting, until the button is released. This is useful when you want to leave the component unattended for a period of time and want to know if the **Peak Threshold** is reached during that period.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Hold Time | 0.010 to 10 | 10 ms to 10 s | 0.000 to 1.00 | Input / Output |
| Infinite Hold | 0  1 | false  true | 0  1 | Input / Output |
| Peak Threshold | -60 to 20 | -60 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Signal Presence | 0  1 | false  true | 0  1 | Output |
