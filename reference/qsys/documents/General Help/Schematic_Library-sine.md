# Sine Generator

> Source: https://help.qsys.com/Content/Schematic_Library/sine.htm

# Sine Generator

The Sine Generator provides a sine wave with variable frequency from 10 Hz to 22 kHz and output level of -100 dB to 20 dB. The outputs are the same for all channels.

[Inputs and Outputs](javascript:void(0))

### Input Pins

This component does not have any input pins available.

### Output Pins

#### Output

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Sine Generator component only has one output pin available.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Sine Properties

This component has no configurable properties.

### Channels

#### Type

Sets the type of **Channel** available for **Inputs** and **Outputs**.

#### Count

Only appears when choosing **Multi-Channel** as the **Type**. Sets the number of **Channels** for **Multi-channel**. You can choose between 2 and 256.

[Controls](javascript:void(0))

#### Mute

Mutes the output for the associated band.

#### Frequency (Hz)

Controls the output frequency for all output channels.

#### RMS Level (dB)

Adjusts the output gain for all channels.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Frequency | 10.0 to 22,000 | 10 Hz to 22 kHz | 0.000 to 1.00 | Output |
| RMS Level | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Input / Output |
