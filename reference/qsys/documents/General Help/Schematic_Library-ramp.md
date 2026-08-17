# Gain Ramp Component

> Source: https://help.qsys.com/Content/Schematic_Library/ramp.htm

# Gain Ramp Component

The Gain Ramp provides the capability to ramp an input signal from one level to another in a specified amount of time, and to ramp back to the original level. You can adjust both **Target Gains** individually, as well as the **Ramp Time** in each direction. Once a **Target Gain** is reached, the output remains at that level until it is manually released to ramp to the other **Target Gain**.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Type** Property.

### Input Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Gain Ramp component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

### Output Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Gain Ramp component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Gain Ramp Properties

### Channels

#### Type

Sets the type of input and output channels. You can choose between **Mono**, **Stereo**, or **Multi-Channel**.

#### Count

Only appears when choosing **Multi-Channel** as the **Type**. Sets the number of **Channels** for **Multi-channel**. You can choose between 2 and 256.

[Controls](javascript:void(0))

### Gain Ramp

#### Target A B

This control has no interactive function.

#### Gain (target)

*This control has no interactive function as it is read only.* It is the **Target Gain** when the ramp goes from **Gain B** to **Gain A**.

#### Ramp To A B

The default for this button is **Off**. When it is engaged, or on, the output level ramps from **Gain A** to **Gain B**.

When the button has been engaged, then disengaged, the output level ramps from **Gain B** to **Gain A**.

#### Mute

Mutes the output of the **Gain Ramp** component.

### Configure

#### Target A B

This control has no interactive function.

#### Rate (dB/s)

**Rate A** displays the decibels per second it takes the output level to go from **Gain B** to **Gain A**.

**Rate B** displays the same as above except from **Gain B** to **Gain A**.

**Rate A** or **B** = ((| **Gain A**| - | **Gain B**|)/ **Time A** or **B**)

#### Time (seconds)

Sets the time it takes for ramp **A** (or **B**) to rise to the **Target Gain** set for ramp **A** (or **B**).

#### Gain (target)

**Gain A** adjusts the output level when the **To B** button is disengaged. It is the **Target Gain** when the ramp goes from **Gain B** to **Gain A**.

**Gain B** adjust the output level when the **To B** button is engaged. It is the **Target Gain** when the ramp goes from **Gain A** to **Gain B**.

#### Unmute

This control has no interactive function.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Current Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Mute | 0  1 | unmuted  muted | 0  1 | Input / Output |
| Ramp Rate A | 0 to 1200 | 0 to 1200 | 0.000 to 1.00 | Input / Output |
| Ramp Rate B | 0 to 1200 | 0 to 1200 | 0.000 to 1.00 | Input / Output |
| Ramp time A | 0.100 to 100 | 100 ms to 100 s | 0.000 to 1.00 | Input / Output |
| Ramp Time B | 0.100 to 100 | 100 ms to 100 s | 0.000 to 1.00 | Input / Output |
| Ramp to B | 0  1 | false  true | 0  1 | Input / Output |
| Release Time | 0.100 to 100 | 100 ms to 100 s | 0.000 to 1.00 | Input / Output |
| Target Gain A | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Target Gain B | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |

[Troubleshooting](javascript:void(0)) 

There are some components that are unique in their operation in the **Emulate** mode. Some of these components are the **Audio Player**, **Crossfader**, **Gain Ramp**, and **Listen** buttons. For more information, see [Limitations](../Q-SYS_Designer/003_Emulate_Mode.htm#Limitations).
