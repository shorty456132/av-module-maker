# Weighting Filter A or C

> Source: https://help.qsys.com/Content/Schematic_Library/filter_weighting.htm

# Weighting Filter A or C

You can use this filter to apply an A or C Weighted curve to audio. This filter can be used with the [SPL Meter / Leq Meter](meter_SPL.htm).

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Type** Property.

### Input Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Weighting Filter component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

### Output Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Weighting Filter component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Weighting Filter Properties

#### Weighting

Sets the type of weighting for the filter.

### Channels

#### Type

Sets the type of **Channel** available for **Inputs** and **Outputs**.

#### Count

Only appears when choosing **Multi-Channel** as the **Type**. Sets the number of **Channels** for **Multi-channel**. You can choose between 2 and 256.

### Response Panel

#### Enabled

Enables or disables the graphical Response graph.

#### Size

Sets the size of the graphical Response graph.

[Controls](javascript:void(0))

#### Response Panel

The Response panel provides vertical and horizontal cross-hairs with a dynamic frequency and dB read-out. Place the mouse courser over the graph to activate the cross-hairs. When the Phase control is activated, the horizontal cross-hair line to the left of center represents the normal curve, the right side represents the phase curve. The readout is only for the normal curve.

#### Phase

Turns the Phase curve on and off.

#### Bypass

Bypasses the filter.

#### Mute

Mutes the output signal.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Bypass | 0  1 | active  bypass | 0  1 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
