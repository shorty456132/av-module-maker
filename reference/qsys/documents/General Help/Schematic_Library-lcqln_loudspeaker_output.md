# Loudspeaker Output (NL Series)

> Source: https://help.qsys.com/Content/Schematic_Library/lcqln_loudspeaker_output.htm

# Loudspeaker Output (NL Series)

Use the Loudspeaker Output component to route an audio signal from another Q-SYS component to an [Q-SYS Products](../Hardware/Hardware_Overview.htm#NL) network loudspeaker.

[Inputs and Outputs](javascript:void(0))

### Input Pins

#### Fullrange

This pin receives a single incoming audio signal from the audio output pin of another Q-SYS component. (Audio to NL Series loudspeakers is unicast only.)

### Output Pins

This component has no output pins.

[Schematic Example](javascript:void(0))

In this example, six NL Series loudspeakers are installed in a large space with three speakers on the left side of the room and three on the right. An Audio Player outputs stereo audio to a Matrix Mixer that sends the left and right signals to the appropriate loudspeaker groups.

**Tip:** Because NL Series loudspeakers are PoE-powered, no amplifier component is needed.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

### Output

#### Clip

LED indicates if the incoming signal is being clipped.

#### Peak Output Level (dBFS)

Measures the peak digital audio signal output to the loudspeaker, from -120 to 20 dB.

#### Clip Hold

Holds the Clip indication until manually cleared.

#### Mute

Mutes the audio signal to the loudspeaker.

#### Gain

Use the Gain control to adjust the the gain level to the loudspeaker, from -100 to 20 dB.

**Tip:** Increasing the gain level can be useful if the source signal is especially low. The on-board limiter in the loudspeaker will protect the device from any PoE overcurrent conditions due to audio signal peaks in the source content. Clipping can still occur, however, and will be indicated by the Clip LED.

### Amplifier Status

#### Limiter

The Limiter LED glows yellow when the output level exceeds the compressor/limiter threshold. This means that the loudspeaker is operating in a non-linear, degraded state. In such a condition, try reducing the amount of Gain. Normally, this LED should be off.

#### Temp

The Temp LED glows red when the loudspeaker is either operating at a higher than normal temperature (Compromised status) or a critical temperature (Fault status). Check the Status component for details if this LED is on. Normally, this LED should be off.

#### Short

The Short LED glows red when the loudspeaker detects a shorted amplifier output. Normally, this LED should be off.

#### Open

The Open led glows red if the loudspeaker detects an open circuit condition within the amplifier output. Normally, this LED should be off.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Gain | -100 to 20 | -100dB to 20dB | 0.00 to 1.00 | Input / Output |
| Level (dBFS) | -120 to 20 | -120dB to 20.0dB | - | Output |
| Limiter State | 0  1 | false  true | 0  1 | Output |
| Mute | 0  1 | false  true | 0  1 | Input / Output |
| Open | 0  1 | false  true | 0  1 | Output |
| Short | 0  1 | false  true | 0  1 | Output |
| Temp | 0  1 | false  true | 0  1 | Output |
