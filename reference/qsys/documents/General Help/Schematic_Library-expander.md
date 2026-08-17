# Expander

> Source: https://help.qsys.com/Content/Schematic_Library/expander.htm

# Expander

The purpose of the Expander is to control the dynamic range of the **Output** below a set **Threshold Level**.

You can specify the maximum attenuation applied by adjusting the **Depth** setting. You can also set the proportion ( **Input** to **Output**) of attenuation that is applied to the **Input** by adjusting the **Ratio**. The **Ratio** allows adjustments from 1 (1:1 - unity with the Input) to 100 (100:1 - very close to the **Threshold Level**).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Expander Properties

#### Side Chain Input

Provides one **Side Chain** input per **Channel**. The **Side Chain** allows you to filter a signal before using it to control the dynamic range of the unfiltered **Inputs**.

**In Gain** is always applied to the Side Chain input signal, regardless of the state of **Bypass**.

**Note:** If you select Side Chain Input = Yes, and don't use the Side Chain Inputs, you will not have any expansion control.

#### Detector Time

Sets one of three pre-set times, or enables the **Detector Time** control in the Control Panel. If one of the three pre-set times is chosen, the control is not available in the Control Panel.

Adjusts the time constant that determines the rate of change of the **Detector** level in response to changes in the **Input** signal.
This adjustment is to prevent changes (spikes, low frequency signals) in the **Input** from causing unwanted, momentary output. A fast **Detector Time** may result in an **Output** that rapidly fluctuates.

#### Bypass Gain Meter

When set to **Active**, the **Applied Gain** meter is active regardless of the state of the **Bypass** button. This means you can adjust the Expander in Bypass mode.

When set to **Inactive**, the Applied Gain meter is inactive to indicate that the component is in Bypass mode.

### Channels

#### Type

Sets the type of **Channel** available for **Inputs** and **Outputs**.

#### Count

Sets the number of **Channels** for **Multi-channel**.

[Controls](javascript:void(0))

[Response Panel and Detector](javascript:void(0))

#### In Gain (dB)

The Input Gain adds to the level of the Input source.

#### Detector (dB)

Graphically and numerically displays the RMS level of the **Input**.

#### Response Panel

Graphically represents the **Gain Calculations** for the **Channel** having the highest **Input** RMS level.

X axis represents the **Input**

Y axis represents the **Output**

The red dot represents the **Output Level**. Below the **Threshold Level** the **Output** is equal to the **Input**, above the **Threshold level** it is adjusted by the Compressor.

#### Bypass

Bypasses the Compressor functionality.

#### Applied Gain (dB)

Graphically and numerically displays the amount of **Gain** applied to the **Channel** with the highest RMS **Input** level. The same amount of Gain, calculated based on the highest Channel, is applied to all other channels that are above the Threshold Level regardless of their relation to the Target Level.

Graphically the meter starts in the middle, displaying attenuation in red going down from center, and gain in green going up from center.

#### Out Gain (dB)

Controls the output level.

[Gain Calculation](javascript:void(0))

#### Threshold Level (dBFS)

Sets the point from which the attenuation is calculated based on the **Ratio** setting. This is where the Expander starts working. Assuming only one **Input**, a level below the **Threshold Level** is attenuated, anything above the Threshold Level is not attenuated.

[Example](javascript:void(0))

If the:

* Threshold Level is -15 dB
* Ratio is 2.5
* Input level is -25 dB

Then the Adjusted Output is:

(((Input Level - Threshold Level) \* Ratio) + Threshold Level) = Output Level

((-25 dB - (-15 dB) \* 2.5) + (-15 dB)) = -40 dB

#### Ratio ( *n*:1)

The ratio between the **Input** and the **Output** as measured from the **Threshold Level**.

The closer the **Ratio** is to 100, the closer the **Output** will be to the **Threshold Level**.

#### Depth (dB)

The maximum amount of attenuation that can be applied.

#### Soft Knee (dB)

Provides a smooth transition for the **Output** during the transition from above the **Threshold Level** to the expanded **Output**, below the **Threshold Level**.

The **Soft Knee** begins adding attenuation before the Threshold Level as the **Input** decreases then continues to increase attenuation until the **Input** level decreases by the amount set by the **Soft Knee**. At that point, the **Soft Knee** has no effect.

[Time Constants](javascript:void(0))

#### Attack Time (seconds)

Sets the time it takes for the output amplitude to rise to 63% of the specified Ratio of the input amplitude once the Threshold Level is exceeded.

#### Release Time (seconds)

Sets the time it takes for the output to fall to 63% of the level set by the Depth control after the Detector level drops below the Threshold Level.

#### Detector Time (seconds)

Available only when **Detector Time Property** is set to **Use Control**.

Sets the time it takes for the Detector level to reach 63% of a change in the input signal.
This adjustment is to prevent changes (spikes, low frequency signals) in the input from causing unwanted, momentary output.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Applied Gain | -20 to 20 | -20 dB to 20 dB | 0.000 to 1.00 | Output |
| Attack Time | .0001 to 60 | 0.100 ms to 100 ms | 0.000 to 1.00 | Input / Output |
| Bypass | 0  1 | active  bypass | 0  1 | Input / Output |
| Depth | 0 to 60 | 0 dB to 60 dB | 0.000 to 1.00 | Input / Output |
| Detector Level | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Detector Time | .0001 to 60 | 0.100 ms to 100 ms | 0.000 to 1.00 | Input / Output |
| Input Gain | -20.0 to 20.0 | -20.0 dB to 20.0 dB | 0.000 to 1.00 | Input / Output |
| Output Gain | -20.0 to 20.0 | -20.0 dB to 20.0 dB | 0.000 to 1.00 | Input / Output |
| Ratio | 1.00 to 100 | 1.00 to 100 | 0.000 to 1.00 | Input / Output |
| Release Time | 0.01 to 10 | 10.0 ms to 10 s | 0.000 to 1.00 | Input / Output |
| Soft Knee | 0.00 to 24.0 | 0 dB to 24 dB | 0.000 to 1.00 | Input / Output |
| Threshold Level | -60 to 20 | -60 dB to 20 dB | 0.000 to 1.00 | Input / Output |
