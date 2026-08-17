# VOIP Out

> Source: https://help.qsys.com/Content/Schematic_Library/telephony_transmitter.htm

# VOIP Out

VOIP Out component controls the outgoing call signal level. Refer to the [Softphone](Softphone.htm) topic for details.

[Inputs and Outputs](javascript:void(0))

### Input Pins

#### Input

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the VoIP Out component allows for only one audio input.

### Output Pins

This component does not have any output pins.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Tone Output

When 'Yes' is selected, the Ring, Entry, Exit, and DTMF tones are fed to a separate output channel (Tone Output) on the VOIP In component. These tones can now be routed independent of the voice audio.

#### Enable Call Sync

When 'Yes' is selected, the Softphone VoIP Out will be enabled for Call Sync. For more information, please visit [Call Sync](call_sync.htm).

[Controls](javascript:void(0))

#### Peak Output Level (dBFS)

Measures the digital output signal level.

#### Clip

Red LED indicating if the signal is being clipped.

#### Clip Hold

Holds the clip indication until manually cleared.

#### Invert

Inverts the audio signal.

#### Mute

Mutes the digital audio signal.

#### Gain

Controls the gain of the digital audio signal.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Clip  (LED) | 0  1 | false  true | 0  1 | Input / Output |
| Clip Hold  (toggle) | 0  1 | false  true | 0  1 | Input / Output |
| Output Gain  (level knob) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Output Invert  (toggle button) | 0  1 | normal  invert | 0  1 | Input / Output |
| Output Mute  (toggle button) | 0  1 | unmute  mute | 0  1 | Input / Output |
| Output Peak Level  (level meter) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
