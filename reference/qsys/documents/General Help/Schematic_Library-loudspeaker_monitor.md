# Loudspeaker Monitor

> Source: https://help.qsys.com/Content/Schematic_Library/loudspeaker_monitor.htm

# Loudspeaker Monitor

When loudspeakers are connected to a CXD-Q, CX-Q, DPA-Q, or DataPort amplifier, you have the capability to monitor the output of the amplifier connected to a particular band of the loudspeaker (the direct input to the loudspeaker band). The Loudspeaker Monitor component provides the means to get the signal from the monitored loudspeaker to an output suitable for monitoring. For example, in your Schematic, you can connect the Loudspeaker Monitor's audio Output to a Line Out card, then to an amplifier that powers loudspeakers in a control room. Once the connections are made, you can control the Gain or Mute the signal to the "monitor" loudspeakers.

**Note:** You must have the Loudspeaker Monitor component in your design for the monitor functions on any of the loudspeakers to operate.

[Inputs and Outputs](javascript:void(0))

### Inputs

There are no configurable inputs for this component.

### Outputs

The Loudspeaker Monitor component only has one Audio output represented by a  circle, and traditional wiring is represented by a thin black line.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

#### Mute

Mutes the output of the Loudspeaker Monitor component.

#### Gain (dB)

Controls the Gain of the Loudspeaker Monitor component.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Gain | -100 to 10 | -100 dB to 10 dB | 0.000 to 1.00 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
