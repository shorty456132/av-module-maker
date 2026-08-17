# VOIP In

> Source: https://help.qsys.com/Content/Schematic_Library/telephony_receiver.htm

# VOIP In

The VOIP In component controls the input signal level for the incoming call. Refer to the [Softphone](Softphone.htm) topic for complete details.

[Inputs and Outputs](javascript:void(0))

### Input Pins

This component does not have any input pins.

### Output Pins

#### Output

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the VoIP In component allows for only one audio output. If **Tone Output**  is set to **Yes**, then two audio outputs are available.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Softphone Properties

#### Tone Output

When 'Yes' is selected, the Ring, Entry, Exit, and DTMF tones are fed to a separate output channel (Tone Output) on the VOIP In component. These tones can now be routed independent of the voice audio.

#### Enable Call Sync

When 'Yes' is selected, the Softphone VoIP In will be enabled for Call Sync. For more information, please visit [Call Sync](call_sync.htm).

[Controls](javascript:void(0))

#### Peak Level (dBFS)

Measures the digital input signal.

#### Invert

Toggle button to invert the digital output of the Softphone In.

#### Mute

Mutes the output signal.

#### Gain (dB)

Controls the Gain of the digital output signal.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Input Gain  (level knob) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Input Invert  (toggle button) | 0  1 | normal  invert | 0  1 | Input / Output |
| Input Mute  (toggle button) | 0  1 | unmute  mute | 0  1 | Input / Output |
| Input Peak Level  (level meter) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
