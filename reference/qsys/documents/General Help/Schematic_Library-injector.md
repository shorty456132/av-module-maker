# Signal Injector

> Source: https://help.qsys.com/Content/Schematic_Library/injector.htm

# Signal Injector

The Signal Injector enables you to take an audio signal of your choice (for example, from the [White Noise Generator](white.htm), [Pink Noise Generator](pink.htm), or [Sine Generator](sine.htm)) and inject it at a component's audio input or output.

* If you inject the signal at a component's output, the signal goes downstream to the input to which the output is connected.
* If you inject the signal at a component's input, the signal goes both downstream through the component's outputs as well as upstream to connected outputs.

**Note:** When you place the Signal Injector at an input, audio is injected across the entire signal path. All outputs downstream and upstream of the insertion point will receive the injected audio.

The Signal Injector has one audio input, and no standard outputs. Its output is the Injector.

[Inputs and Outputs](javascript:void(0))

### Input Pins

#### Input

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Signal Injector component only has one input pin available.

### Output Pins

This component does not have any output pins available.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Signal Injector Properties

This component has no configurable properties.

[Controls](javascript:void(0))

#### Valid

Lights when the Injector is connected to a valid connection point.

#### Injector

Injects the signal, connected to the Signal Injector Input, at the point where you connect it. The Injector effectively blocks any standard input connected to that point.

In the Signal Injector Control Panel, click the Injector one time, then move it to the connector to which you want to connect it and click that connector. The Injector is attached to that connector. To remove or move it, simply click the Injector and click in a blank area of the Schematic, or in the Signal Injector Control Panel, or a different connector.

#### Mute

Mutes the output signal of the Injector.

#### Gain (dB)

Sets the output Gain of the Injector.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Valid | 0  1 | false  true | 0  1 | Output |
