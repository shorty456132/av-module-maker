# Automatic Gain Control (AGC) Component

> Source: https://help.qsys.com/Content/Schematic_Library/leveler.htm

# Automatic Gain Control (AGC) Component

The purpose of the Automatic Gain Control is to control the overall dynamic range of the **Output** when the **Input** level changes.

The AGC can be adjusted from unity (1:1) with the **Input**, to an almost flat (100:1 - very little amplitude variation) **Output**. The AGC automatically adjusts the **Gain** to compensate for high or low **Inputs**. The control settings for the AGC Component affect all the **Input Channels** based on calculations made using the highest **Input** level. If you want to separately control the AGC for multiple **Channels**, simply add more AGC Components.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Type** Property.

### Input Pins

#### Input

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Automatic Gain Control component is set to a **Mono** channel, which provides one input. Additionally, you can set the Properties to allow for **Stereo**, which gives you 2 inputs (Right and Left for each input); or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs.

### Output Pins

#### Output

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Automatic Gain Control component is set to a **Mono** channel, which provides 1 output. Additionally, you can set the Properties to allow for **Stereo**, which gives you 2 outputs (Right and Left); or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 outputs.

[Schematic Example](javascript:void(0))

In this example, we have the phone in our conference room routed through an Automatic Gain Control before reaching our Line Out component. The Automatic Gain Control will control the overall dynamic range of the **Output** when the **Input** level changes.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Automatic Gain Control Properties

#### Side Chain Input

Provides one **Side Chain** input per **Channel**. The Side Chain allows you to filter a signal before using it to control the **Gain** of the unfiltered audio **Input**.

**In Gain** is always applied to the Side Chain input signal, regardless of the state of **Bypass**.

**Note:** If you select Side Chain Input = Yes, and don't use the Side Chain Inputs, you will not have any AGC.

#### Detector Time

Sets one of four pre-set times, or enables the **Detector Time** control in the Control Panel. If one of the four pre-set times is chosen, the control is not available in the Control Panel.

Adjusts the time constant that determines the rate of change of the **Detector** level in response to changes in the **Input** signal.
This adjustment is to prevent changes (spikes, low frequency signals) in the **Input** from causing unwanted, momentary output. A fast **Detector Time** may result in an **Output** that rapidly fluctuates.

#### Bypass Gain Meter

When set to **Active**, the **Applied Gain** meter is active regardless of the state of the **Bypass** button. This means you can adjust the AGC in Bypass mode.

When set to **Inactive**, the Applied Gain meter is inactive to indicate that the component is in Bypass mode.

### Channels

#### Type (Channel)

Determines the Crossover Component's channel type - Mono, Stereo, or Multi-Channel. (Stereo = two mono channels)

#### Count (Multi-Channel)

When you choose Multi-Channel, you can specify from 2 to 256 for the Count.

[Controls](javascript:void(0))

[General Controls](javascript:void(0))

#### In Gain (dB)

The Input Gain adds to the level of the Input source.

#### Detector (dB)

Graphically and numerically displays the RMS level of the highest **Input**.

#### Response Panel

Graphically represents the **Gain Calculations** for the **Channel** having the highest **Input** RMS level.

X axis represents the **Input**

Y axis represents the **Output**

The red dot represents the **Output Level**. Below the **Threshold Level** the **Output** is equal to the **Input**, above the **Threshold level** it is adjusted by the AGC.

#### Bypass

Bypasses the AGC functionality.

#### Applied Gain (dB)

Graphically and numerically displays the amount of **Gain** applied to the **Channel** with the highest RMS **Input** level. The same amount of Gain, calculated on the highest Channel, is applied to all other channels that are above the Threshold Level regardless of their relation to the Target Level.

Graphically the meter starts in the middle, displaying attenuation in red going down from center, and gain in green going up from center.

#### Out Gain (dB)

Controls the output level.

[Gain Calculations](javascript:void(0))

#### Threshold Level (dBFS)

The level at which the AGC Component becomes active. This should be set at a level so that the anticipated background noise does not activate the AGC. When an **Input** exceeds the **Threshold Level**, the **Gain** for that input is adjusted to calculated level based on the **Ratio** and the **Target Level**.

If there is more than one **Input** that exceeds the **Threshold Level**, the **Gain** is calculated using the **Channel** with the highest RMS level. The other **Channel**(s) have the same amount of **Gain** applied to them as the **Channel** with highest RMS **Input** level.

#### Ratio

The ratio between the **Input** and the **Output** as measured from the **Target Level**. The closer the **Ratio** is to 100, the closer the **Output** will be to the **Target Level**, which also means smaller dynamic changes in the **Output** level.

When the **Input** is below the **Target Level** and the **Gain** applied by the **Ratio** setting is greater than the **Maximum Gain** setting, the **Output** is clipped per the **Maximum Gain** setting.

#### Target Level (dB)

Sets the point from which the **Gain** is calculated based on the **Ratio** setting. Assuming only one **Input**, a level below the **Target Level** has a positive **Gain** applied, a level above the **Target Level** has a negative **Gain** (attenuation) applied.

If the

* Target Level is -15 dB
* Ratio is 2.5
* Input level is 10 dB
* Adjusted Output is   
  (((Input level - Target Level) / Ratio) + Target Level) = Output Level  
  ((10 dB - (-15 dB) / 2.5) + (-15 dB)) = -5 dB

#### Maximum Gain (dB)

Sets the maximum amount of gain provided to an **Input** when the **Input** is above the **Threshold Level**, but below the **Target Level**. The **Maximum Gain** is not used when the gain applied by the **Ratio** setting is less than the **Maximum Gain** setting.

**Ratio** calculation used

* **Threshold Level** is -50 dB
* **Target Level** is -15 dB
* **Ratio** is 2 (2:1)
* **Maximum Gain** is 10 dB
* **Input** is -20 dB
* Adjusted **Output** is -17.5 dB  
  ((( **Input** level - **Target Level**) / **Ratio**) + **Target Level**) = **Output** Level  
  ((-20 dB - (-15 dB) / 2) + (-15 dB)) = -17.5 dB  
  The applied gain is 2.5 dB, which is less than the 10 dB **Maximum Gain**.

**Maximum Gain** used

* **Maximum Gain** is 10 dB
* **Input** is -40 dB  
  ((( **Input** level - **Target Level**) / **Ratio**) + **Target Level**) = **Output** Level  
  ((-40 dB - (-15 dB) / 2) + (-15 dB)) = -27.5 dB  
   would be a gain of 12.5 dB based on the **Ratio**
* Adjusted **Output** is actually -30 dB a gain of 10 dB, which is equal to the **Maximum Gain** setting of 10 dB. The same calculation is used, but the **Output** is clipped at the **Maximum Gain** setting.

[Time Constants](javascript:void(0))

#### Detector Time (milliseconds)

Available only when **Detector Time Property** is set to **Use Control**.

Adjusts the time constant that determines the rate of change of the **Detector** level in response to changes in the **Input** signal.
This adjustment is to prevent changes (spikes, low frequency signals) in the **Input** from causing unwanted, momentary output. A fast **Detector Time** may result in an **Output** that rapidly fluctuates.

#### Response Time (seconds)

Adjusts the time constant that determines the time it takes for the **Gain** to go from its current level to the new level when there is a change in the **Input** RMS level.

#### Hold Time (seconds)

When the **Recovery** button is engaged, **Hold Time** sets minimum time the applied **Gain** stays at the calculated level after the RMS **Input** level drops below the **Threshold Level**. This is to prevent the **Output** from fluctuating due to momentary pauses in the **Input**.

If there is another **Channel** in use with a lower RMS **Input** level, above the **Threshold Level**, the **Hold Time** does not apply. The applied **Gain** changes to the proper level for the new **Channel** based on the **Response Time**.

#### Recovery Time (seconds)

When the **Recovery** button is engaged, **Recovery Time** sets the time it takes for the applied **Gain** to return to zero.

If there is another **Channel** in use with a lower RMS **Input** level, above the **Threshold Level**, the **Recovery Time** does not apply. The applied **Gain** changes to the proper level for the new **Channel** based on the **Response Time**.

#### Recovery Enable

Turns on and off the **Recovery Time Enable** functionality. In the Off position, the **Hold Time** and **Recovery Time** do not apply.

If there is only one **Channel** above the **Threshold Level**, and the **Recovery** button is in the Off position, when that **Channel** drops below the **Threshold Level,** the **Gain** stays at the last calculated level before the **Channel** dropped below the **Threshold Level**.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Applied Gain | -20 to 20 | -20 dB to 20 dB | 0.000 to 1.00 | Output |
| Bypass | 0  1 | active  bypass | 0  1 | Input / Output |
| Detector Level | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Detector Time | 0.100 to 60 | 100 ms to 60 s | 0.000 to 1.00 | Input / Output |
| Hold Time | 0.000 to 10 | 100 ms to 10 s | 0.000 to 1.00 | Input / Output |
| Input Gain | -20.0 to 20.0 | -20.0 dB to 20.0 dB | 0.000 to 1.00 | Input / Output |
| Maximum Gain | 0.000 to 20.0 | 0 dB to 20.0 dB | 0.000 to 1.00 | Input / Output |
| Output Gain | -20.0 to 20.0 | -20.0 dB to 20.0 dB | 0.000 to 1.00 | Input / Output |
| Ratio | 1.00 to 100 | 1.00 to 100 | 0.000 to 1.00 | Input / Output |
| Recovery | 0  1 | active  bypass | 0  1 | Input / Output |
| Recovery Time | 0.100 to 10 | 100 ms to 10 s | 0.000 to 1.00 | Input / Output |
| Response Time | 0.100 to 10 | 100 ms to 10 s | 0.000 to 1.00 | Input / Output |
| Target Level | -60 to 20 | -60 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Threshold Level | -60 to 20 | -60 dB to 20 dB | 0.000 to 1.00 | Input / Output |
