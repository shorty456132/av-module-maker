# True Peak/RMS Meter

> Source: https://help.qsys.com/Content/Schematic_Library/meter2.htm

# True Peak/RMS Meter

The Meter is an RMS meter used to measure audio signal loudness, expressed in dB. **RMS Response Time**, **Peak Decay Time**, **Max Hold Time**, and **Infinite Hold** controls are available to change how the readings are displayed. The Meter is capable of up to 256 inputs.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Type** Property.

### Input Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the True Peak / RMS Meter component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

### Output Pins

This component does not have any output pins available.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Level Meter Properties

#### Meter Type

Selects the type of the meter.

### Channels

#### Type

Sets the type of **Channel** available for **Inputs** and **Outputs**.

#### Count

Only appears when choosing **Multi-Channel** as the **Type**. Sets the number of **Channels** for **Multi-channel**. You can choose between 2 and 256.

[Controls](javascript:void(0))

### Input

#### Peak/RMS Meters (1- *n*) (dBFS)

The meter display has two different readings:

The solid bar represents the RMS or Peak level. The response of this indicator is controlled by the Response Time control.

The thin line represents the maximum level reached by RMS or Peak level indicator. The length of time this indicator stays at the maximum is controlled by the Hold Time control, or the Infinite Hold button.

The display shows from -60 dB to +20 dB, but if you hover the mouse over the meter, the text readout extends from -100 dB to +20 dB.

#### Peak/RMS dB-linear (dBFS)

The meter display has two different readings:

The solid bar represents the RMS or Peak level. The response of this indicator is controlled by the Response Time control.

The thin line represents the maximum level reached by RMS or Peak level indicator. The length of time this indicator stays at the maximum is controlled by the Hold Time control, or the Infinite Hold button.

The scale is linear and displays from -60 dB to +20 dB, but if you hover the mouse over the meter, the text readout extends from -100 dB to +20 dB.

#### Peak Program Meters (1- *n*)

The Peak Program meter registers peaks longer than a few milliseconds in duration, and ignores shorter peaks.

The meter reads 6 to 8 dB below true peak

The meter has a long decay time constant, to allow longer to see the peaks.

The meter has a logarithmic scale giving 4 decibels per division, and a standard reference level of 4 corresponding to 0 dBu.

### Configure

#### Type

Selects the meter type: RMS or Peak.

Available only in True Peak/RMS and True Peak/RMS dB-linear modes as set in the Properties.

#### Response Time (seconds)

Sets the Level Detector time constant for both attack and decay. This controls how quickly the meters respond to changes in the input levels.

Available only in True Peak/RMS mode as set in the Properties.

#### Hold Time (seconds)

Sets how long the maximum level marker is held.

#### Infinite Hold (button)

Keeps the maximum level marker (thin line) at the maximum value reached, until the button is disengaged.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Hold Time | 0.010 to 10 | 10 ms to 10 s | 0.000 to 1.00 | Input / Output |
| Infinite Hold | 0  1 | false  true | 0  1 | Input / Output |
| Peak Level | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Output |
| Peak Max | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Output |
| Peak/RMS Select [1](#True_Peak_RMS) | 0  1 | Peak  RMS | 0  1 | Input / Output |
| Response Time [1](#True_Peak_RMS) | 0.010 to 1.00 | 10 ms to 1 s | 0.000 to 1.00 | Input / Output |
| RMS Level [1](#True_Peak_RMS) | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Output |
| RMS Max [1](#True_Peak_RMS) | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Output |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1. Available only in True Peak/RMS and True Peak/RMS dB-linear mode as set in the Properties. | | | | |
