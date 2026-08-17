# Compressor

> Source: https://help.qsys.com/Content/Schematic_Library/compressor.htm

# Compressor

The purpose of the Compressor is to control the dynamic range of the **Output** above a set **Threshold Level**.

The Compressor can be adjusted from unity (1:1) with the **Input**, to an almost flat (100:1 - very little amplitude variation) **Output**. Using the **Depth** control, you can control the point at which compression stops increasing, even though the **Input** level continues to increase.

The control settings for the Compressor Component affect all the **Input Channels** based on calculations made using the highest **Input** level. If you want to separately control the compression for multiple **Channels**, simply add more Compression Components.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Type** Property.

### Input Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Compressor component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

### Output Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Compressor component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Compressor Properties

#### Side Chain Input

Provides one **Side Chain** input per **Channel**. The **Side Chain** allows you to filter a signal before using it to control the dynamic range of the unfiltered **Inputs**.

**In Gain** is always applied to the Side Chain input signal, regardless of the state of **Bypass**.

**Note:** If you select Side Chain Input = Yes, and don't use the Side Chain Inputs, you will not have any compression control.

#### Detector Time

Sets one of three pre-set times, or enables the **Detector Time** control in the Control Panel. If one of the three pre-set times is chosen, the control is not available in the Control Panel.

Sets the time it takes for the **Detector** level to reach 63% of a change in the **Input** signal.

This adjustment is to prevent changes (spikes, low frequency signals) in the input from causing unwanted, momentary output.

#### Bypass Gain Meter

When set to **Active**, the **Applied Gain** meter is active regardless of the state of the **Bypass** button. This means you can adjust the Compressor in Bypass mode.

When set to **Inactive**, the Applied Gain meter is inactive to indicate that the component is in Bypass mode.

### Channels

#### Type

Sets the type of **Channel** available for **Inputs** and **Outputs**.

#### Count

Only appears when choosing **Multi-Channel** as the **Type**. Sets the number of **Channels** for **Multi-channel**. You can choose between 2 and 256.

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

Graphically the meter starts from the top, displaying attenuation in red going down.

#### Out Gain (dB)

Controls the output level.

[Gain Calculation](javascript:void(0))

#### Threshold Level (dBFS)

Sets the level where compression begins. This is the point from which the amount of attenuation is calculated based on the **Ratio** setting.

Assuming only one **Input**, a level below the **Threshold Level** is not compressed, anything above the **Threshold Level** attenuation is applied.

[Example](javascript:void(0))

If the:

* Threshold Level is -15 dB
* Ratio is 2.5
* Input level is 10 dB

Then the Adjusted Output is:

(((Input Level - Threshold Level) / Ratio) + Threshold Level) = Output Level

((10 dB - (-15 dB) / 2.5) + (-15 dB)) = -5 dB

#### Ratio ( *n*:1)

The ratio between the **Input** and the **Output** as measured from the **Threshold Level**.

The closer the **Ratio** is to 100, the smaller dynamic changes in the **Output** level. As the **Ratio** is adjusted closer to 1, the dynamic range of the **Output** increases.

#### Depth (dB)

Sets the maximum amount of attenuation applied to the **Input**.

As the **Input** increases, the Compressor applies more attenuation based on the **Ratio** setting. When the amount of attenuation applied reaches the **Depth** setting, no more attenuation is added.

#### Soft Knee (dB)

Provides a smooth transition, in the **Output**, from the uncompressed level to the compressed level.

The **Soft Knee** slowly adds attenuation, as the **Input** increases, until the attenuation added by the **Soft Knee** is equal to the attenuation added by the **Ratio** setting.

[Time Constants and Gain Meter](javascript:void(0))

#### Attack Time (seconds)

Sets the time it takes for the **Input** to drop to 63% of the **Depth** level.

A long **Attack Time** causes the **Output** to stay closer to unity with the **Input** as the **Input** increases, then slowly drop to the desired **Output** level. A fast **Attack Time** causes the **Output** to get to the desired level faster without getting as close to unity with the **Input**.

#### Release Time (seconds)

Sets the time it takes for the **Output**
to reach 63% of the **Threshold** Level.

This prevents the **Output** from dropping to quickly when the **Input** drops. Provides a smoother transition from a high **Output** to a lower **Output**.

#### Detector Time (seconds)

Available only when **Detector Time Property** is set to **Use Control**.

Sets the time it takes for the **Detector** level to reach 63% of a change in the **Input** signal.

This adjustment is to prevent changes (spikes, low frequency signals) in the input from causing unwanted, momentary output.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Applied Gain | -20 to 20 | -20 dB to 20 dB | 0.000 to 1.00 | Output |
| Attack Time | 0.0001 to 100 | .100 ms to 100 ms | 0.000 to 1.00 | Input / Output |
| Bypass | 0  1 | active  bypass | 0  1 | Input / Output |
| Depth | 0 to 60 | 0 dB to 60 dB | 0.000 1.000 | Input / Output |
| Detector Level | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Detector Time | 0.0001 to 100 | .100 ms to 100 ms | 0.000 to 1.00 | Input / Output |
| Input Gain | -20.0 to 20.0 | -20.0 dB to 20.0 dB | 0.000 to 1.00 | Input / Output |
| Output Gain | -20.0 to 20.0 | -20.0 dB to 20.0 dB | 0.000 to 1.00 | Input / Output |
| Ratio | 1.00 to 100 | 1.00 to 100 | 0.000 to 1.00 | Input / Output |
| Release Time | 0.010 to 10 | 10.0 ms to 10 s | 0.000 to 1.00 | Input / Output |
| Soft Knee | 0 to 24.0 | 0 dB to 24 dB | 0.000 to 1.00 | Input / Output |
| Threshold Level | -60 to 20 | -60 dB to 20 dB | 0.000 to 1.00 | Input / Output |
