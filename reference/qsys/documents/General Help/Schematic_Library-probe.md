# Signal Probe Component

> Source: https://help.qsys.com/Content/Schematic_Library/probe.htm

# Signal Probe Component

The Signal Probe is a tool you can attach to any audio output and measure the signal at that point using various other components such as a [True Peak/RMS Meter](meter2.htm), [Responsalyzer](responsalyzer.htm), [RTA - Band-Pass](rta_bandpass.htm), and so on.

[Inputs and Outputs](javascript:void(0))

### Input Pins

This component does not have any input pins available.

### Output Pins

#### Output

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Signal Probe component only has one output pin available.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Signal Probe Properties

This component has no configurable properties.

[Controls](javascript:void(0))

#### Valid

Indicates if the connector the Signal Probe is connected to has a valid signal present or not.

#### Probe

In the Signal Probe Control Panel, click the Probe one time, then move it to the connector where you want to connect it and click that connector. The Probe is attached to that connector. To remove or move it, simply click the Probe and click in a blank area of the Schematic, or in the Signal Probe Control Panel, or a different connector.

#### Mute

Mutes the output signal of the Probe.

#### Gain (dB)

Sets the output Gain of the Probe.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Valid | 0  1 | unmute  mute | 0  1 | Output |
