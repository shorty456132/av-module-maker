# Envelope Generator Component

> Source: https://help.qsys.com/Content/Schematic_Library/envelope_generator.htm

# Envelope Generator

The Envelope Generator creates a series of control levels with which you can control another component's control(s), typically a gain type control, to travel through the series of levels that define the envelope. For example, you can cause the gain of a component to go immediately from -100 dB to the Release Level of -20 dB then to the Attack Level of 10 dB in 3 seconds, then fall to the Sustain Level of 0 dB in 5 seconds where it stays for 10 seconds, then goes back to the Release Level of -20 dB in 2 seconds, then immediately back to -100 dB. All of the times and levels are adjustable.

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Envelope Generator Properties

This component has no configurable properties.

[Controls](javascript:void(0))

### Input

#### Key

Clicking this momentary button causes the output level to go from the Release Level to the Attack Level, then to the Sustain Level where it is held until this button is released. When released, the output level goes from the Sustain Level to the Release Level, then to -100 dB. All the time settings are observed for all levels.

#### Trigger

Clicking this trigger button starts the envelope running through one complete cycle.

### Configure

#### Attack Level

The first level of the envelope, from -100 to 20dB (default is 0). The output level, rises or falls from the Release Level setting to the Attack Level setting. Prior to starting the envelope, the output level is at -100 dB, when the envelope is started, the output immediately goes to the Release Level setting then starts moving towards the Attack Level setting.

#### Attack Time

The time it takes for the output level to reach the Attack Level from the Release Level, from 30ms to 10.0s (default is 1.00s).

#### Decay Time

The time it takes for the output level to reach the Sustain Level from the Attack Level, from 30ms to 10.0s (default is 1.00s).

#### Sustain Level

The output level is sustained at this level, from -100 to 20dB (default of -6.00dB), for the time set in Sustain Time.

#### Sustain Time

The length of time, from 30ms to 10.0s (default is 1.00s), the output level is kept at the Sustain Level.

#### Release Level

The last level of the envelope. The level at which the envelope is released at the end of its cycle, from -100 to 20dB (default is -40.0dB). After the envelope reaches this level, the output immediately goes to -100 dB.

#### Release Time

The time it takes for the output level to rise or fall from the Sustain Level to the Release Level, from 30ms to 10.0s (default is 1.00s).

### Output

#### Level

This knob indicates the output level, from -100 to 20dB.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Output Level | -100 to 20 | -100 dB to 20.0 dB | 0.00 to 1.00 | Output |
| Attack Level | -100 to 20 | -100 dB to 20.0 dB | 0.00 to 1.00 | Input / Output |
| Attack Time | 0.030 to 1 | 30.0 ms to 1s | 0.00 to 1.00 | Input / Output |
| Decay Time | 0.030 to 1 | 30.0 ms to 10s | 0.00 to 1.00 | Input / Output |
| Key | 0  1 | false  true | 0  1 | Input / Output |
| Release Level | -100 to 20 | -100 dB to 20.0 dB | 0.00 to 1.00 | Input / Output |
| Release Time | 0.030 to 1 | 30.0 ms to 10s | 0.00 to 1.00 | Input / Output |
| Sustain Level | -100 to 20 | -100 dB to 20.0 dB | 0.00 to 1.00 | Input / Output |
| Sustain Time | 0.030 to 1 | 30.0 ms to 10s | 0.00 to 1.00 | Input / Output |
| Trigger | (trigger) | | | Input / Output |
