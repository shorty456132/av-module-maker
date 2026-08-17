# Gain

> Source: https://help.qsys.com/Content/Schematic_Library/gain.htm

# Gain

The Gain Component is used to increase or attenuate the audio signal of up to 256 Channels simultaneously. You can simultaneously Bypass, Invert, and Mute all the Channels as well.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Type** Property.

### Input Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Gain component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

### Output Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Gain component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

[Schematic Example](javascript:void(0))

In this example, we have all of our audio channels routed through a series of Equalizers and Filters before being delivered to our Amplifiers. The Gain component provides attenuation to the audio signal(s) simultaneously.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Gain Properties

#### Max Gain (dB) [1](#min-max)

Sets the maximum gain setting for this Gain component.

#### Min Gain (dB) [1](#min-max)

Sets the minimum gain setting for this Gain component.

#### Enable Ramp Controls

Select whether to expose Increase, Decrease, Hold Off, and Time controls.

#### Mode

With Enable Ramp Controls set to 'Yes', select whether the gain is adjusted in continuous fashion or in a discrete number of steps.

#### Number of Steps

With Mode set to 'Discrete', set how many steps it takes to go from the minimum gain value to the maximum gain value.

###### 1. You can lock the Gain setting by setting the Min and Max settings to the same value. If you specify a greater minimum than the maximum, the control simply works backwards within the limits you set.

### Channels

#### Type

Determines the Gain Component's channel type.

#### Count

Determines the number of channels for **Multi-channel**.

[Controls](javascript:void(0))

#### Bypass

Bypasses the Gain Component for all channels.

#### Invert

Inverts the polarity of the output signal for all channels.

#### Mute

Mutes the output for the all channels.

#### Gain (dB)

Adjusts the output gain for all channels. The range depends on the Min Gain and Max Gain settings in the Properties.

### Ramp Controls

**Note:** These controls only appear when **Enable Ramp Controls** are set to **Yes**.

#### Increase

Click to increase the gain. Click and hold to continuously increase the gain according to the Hold Off and Time controls.

#### Decrease

Click to decrease the gain. Click and hold to continuously decrease the gain according to the Hold Off and Time controls.

#### Hold Off

When clicking and holding the Increase or Decrease buttons, this is the amount of time it takes before the gain value starts to ramp.

#### Time

When clicking and holding the Increase or Decrease buttons, this is the amount of time it takes to ramp from the minimum gain value to the maximum gain value.

#### Step Meter

If Mode is set to 'Discrete', this meter indicates the level of gain.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Bypass | 0  1 | active  bypass | 0  1 | Input / Output |
| Decrease | 0  1 | false  true | â | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Hold Off | 0.000 to 60.0 | 0ms to 60.0s | 0.000 to 1.00 | Input / Output |
| Increase | 0  1 | false  true | â | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Time | 0.000 to 60.0 | 0ms to 60.0s | 0.000 to 1.00 | Input / Output |
