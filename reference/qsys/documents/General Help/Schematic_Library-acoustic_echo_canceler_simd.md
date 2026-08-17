# Acoustic Echo Canceler

> Source: https://help.qsys.com/Content/Schematic_Library/acoustic_echo_canceler_simd.htm

# Acoustic Echo Canceler

The QâSYS multiâchannel Acoustic Echo Canceler (AEC) component is used in conference rooms (Near-End) and other installations where people call in from remote locations. The remote caller's (Far-End caller's) voice is broadcast over loudspeakers in the conference room. The sound is picked up by microphones in the conference room and echoed back to the Far-End caller. The purpose of the AEC is to eliminate these echoes while at the same time allowing the Far-End caller to hear clearly, what people in the room are saying.

Each microphone in the conference room is plugged into one channel of the Q-SYS AEC component. Each channel also receives the loudspeaker signal that carries the remote talker's voice. This is called the AEC reference signal. To remove the echoes, the AEC subtracts a filtered version of the reference signal from the microphone signal.

**Tip:** To learn more about AEC, see the [Acoustic Echo Cancellation (AEC) Application](../Application_Integration/AEC/Acoustic_Echo_Cancellation.htm) topic. For AEC best practices, refer to the [QSC Quantum Level 1 Training Online](https://training.qsc.com/course/view.php?id=87).

[Core Processing](javascript:void(0))

### Max AEC Channels per Core by Tail Length

**Note:** Q-SYS Scaling Licenses expand the capabilities of some Q-SYS Core processor models. Refer to the [Licensing](../Core_Manager/Core_Management/Licensing.htm) topic for more information.

| Tail Length > | 100 ms | 200 ms | 300 ms | 400 ms |
| --- | --- | --- | --- | --- |
| NV-32-H (Core Capable) | 12 | 8 | 6 | 4 |
| Core Nano | 12 | 8 | 6 | 4 |
| Core 8 Flex | 12 | 8 | 6 | 4 |
| Core 24f | 36 | 24 | 16 | 12 |
| Core 110f | 24 | 16 | 12 | 8 |
| Core 510i | 96 | 64 | 48 | 32 |
| Server Core X10 | 96 | 64 | 48 | 32 |
| Server Core X20r | 192 | 128 | 96 | 64 |
| Core 610 | 96 | 64 | 48 | 32 |
| Core 5200 | 240 | 160 | 120 | 80 |
| Core 6000 CXR | 120 | 80 | 60 | 40 |

### AEC Signal Delays

Most modern AEC systems, including Q-SYS AEC, process the signal in many narrow frequency bands. This introduces a delay in the signal:

| AEC Delay Type > | Input-to-conference-output | Input-to-reinforcement-output |
| --- | --- | --- |
| Core 8 Flex  Core Nano  NV-32-H (Core Capable)  Core 110f  Core 24f | 32 milliseconds | 21.4 milliseconds |
| All other Cores | 26.7 milliseconds | 10.7 milliseconds |

[Inputs and Outputs](javascript:void(0))

### Input Pins

#### Microphone

Connect to the Near-End conference room microphones.

#### Reference

This pin receives a single incoming audio signal from a Far-End audio source, such as a Speakerphone In component (USB Audio Bridge), VoIP In (Softphone), or POTS In component. The Reference is then used for AEC processing.

### Outputs

#### Conference

Output to the Far-End phone. Connect this pin to audio processing components (equalizers, mixers, etc.) and finally to an audio output, such as Speakerphone Out, VoIP Out, or POTS Out, depending on the conferencing solution within the design.

#### Reinforcement

Optional. If enabled in Properties, this pin outputs to the Near-End conference room loudspeakers. See Properties > [Reinforcement Output](#Reinforc)  for more information.

[Schematic Example](javascript:void(0)) 

In this example, there are 8 microphones routed through an Acoustic Echo Canceler to eliminate echos for the remote caller's (Far-End caller's).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Acoustic Echo Canceler Properties

#### Tail Length ms

Tail length is the maximum room impulse response that the adaptive filter can model.

Typically, you would use 200 ms, but for exceptionally reverberant rooms, you may want to use 400 ms.

When the Tail Length is set to 400 ms, the channel count is doubled when calculating AEC Processing in Check Design (Shift+F6), which effectively cuts the number of available channels in half.

#### Channel Count

Selects the number of input channels available for the AEC. Each Core has a set limit of channels you can use in a design. Note that an AEC channel with a Tail Length of 200ms requires double the processing of one with a Tail Length of 100ms. Likewise, an AEC channel with a Tale Length of 400ms requires four times the processing of one with a Tail Length of 100ms.

#### Shared Reference

Select Yes to have one input Reference signal shared by all channels.

#### Reinforcement Output

Select Yes to make a Reinforcement output pin available for each channel. No is the default. When enabled, connect the Reinforcement pin to the Near-End conference room loudspeakers.

[About Sound Reinforcement (SR)](javascript:void(0))

Sound Reinforcement (SR), also known as "voice-lift", is typically enabled in larger conference rooms, where it is desirable to have the Near End talkerâs voice amplified over the room's loudspeakers. When the Reinforcement Output property is enabled and the Reinforcement pin is connected to the Near-End conference room loudspeakers, Q-SYS takes the output of the AEC after the adaptive filter subtraction operation but before the non-linear processor (NLP). The SR output is then mixed with the Far End reference and sent to the loudspeaker. Enabling and wiring the Reinforcement pin is usually more desirable than other sound reinforcement applications, which can suffer from acoustic feedback (howling) problems in the Near End room due to the direct path from loudspeaker to microphone.

**Tip:** Additional system and component latency combined with the Reinforcement Output latency can increase the total delay from microphone to loudspeaker. This can be excessive in some live sound situations. In these cases, it may be preferable to use a direct connection from microphone to loudspeaker rather than the Reinforcement Output pin.

#### Max Noise Reduction

Select the maximum level of noise reduction allowed with the Noise Reduction (NR) control.

**Note:** In most cases, this should be left at the default of 10dB to avoid distorting sound quality.

[Controls](javascript:void(0))

[Canceler](javascript:void(0))

#### Echo Return Loss Enhancement (ERLE)

This meter indicates how much, in dB, the Far-End echo arriving at the Near-End microphone is attenuated by the AEC adaptive filter once the filter has converged.

The ERLE meter is used to indicate how effective the AEC is in terms of suppressing the acoustic echo. A reading below 10 dB during Far-End only talk may indicate that the room tail is longer than the AEC tail property. Readings above 20 dB during Far-End only talk indicate that the AEC is working properly.

#### Bypass

Bypasses the AEC function, including its latency, when activated. The default is Off.

#### Reference-to-Microphone Level Ratio (RMLR)

This meter indicates how much, in dB, the Far-End reference signal level exceeds the Near-End microphone signal level.

The RMLR meter is used to adjust the reference signal level during Far-End only talk. In general, the Far-End reference signal level should approximately equal the Near-End microphone signal level, as indicated by a ratio of 0dB. The ratio can be adjusted using the Reference Gain knob.

#### Target 0dB

Adjust the Reference Gain until the RMLR is at the target of 0dB.

#### Reference Gain

This knob adjusts, in dB, the Far-End reference signal level. The default is 0.

In general, the Far-End reference signal level should approximately equal the Near-End microphone signal level, as indicated by 0dB on the Reference-to-Microphone Level Ratio meter.

[Adaptive Filter](javascript:void(0))

#### Hold If Mic Level Below

Sets the threshold, in dB between -100 and 0, below which AEC adaptation stops. The default is -100dB. In most cases, the microphone signal will be nonexistent when the mic's mute feature is activated, so this level should be left at the default of -100 dB. However, if your microphone only strongly attenuates the signal when muted, this weak signal can cause issues with AEC adaptation. In this case, try adjusting the Hold level to just above the level when the mic is muted.

**Tip:** For example, if your microphone signal is -80 dB when the mute feature is activated, try adjusting the Hold level to -60 dB.

#### Hold If Ref Level Below

Sets the threshold, in dB between -100 and 0, below which the AEC adaptation stops. The default is -100dB. In most cases, the Far-End reference signal is clean and of sufficiently high level, so this level should be left at the default. However, if the Far-End reference signal has elevated background noise, this noise can cause issues with AEC adaptation. In this case, try adjusting the Hold level to just above the Far-End background noise level.

[Post-Processor](javascript:void(0))

#### Residual Echo Suppression (RES) %

Residual Echo Suppression applies additional suppression to any residual echo that was not removed by the adaptive filter and echo reduction functions of the AEC component.

This control determines how much any residual echo is suppressed. The more you turn it up, the more aggressively the residual echo is suppressed at the expense of distorting the Near-End microphone signal.

#### RES Enable

Enables and disables Residual Echo Suppression functionality of the AEC.

#### Noise Reduction (NR) dB

Noise Reduction reduces the level of relatively steady state noises like fans, lawn mowers, wind, and mains electrical hum. The goal is to reduce these noises without affecting the desired speech.

This control determines how much, in dB, these steady-state noises are reduced. The more you turn it up, the more aggressively the noise is removed at the expense of distorting the Near-End microphone signal.

#### NR Enable

Enables and disables the noise reduction functionality of the AEC.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| For Each Channel | | | | |
| AEC Bypass | 0  1 | no  bypassed | 0  1 | Input / Output |
| Echo Return Loss Enhancement | 0 to 20 | 0 dB to 20 dB | 0  1 | Output |
| Hold If Microphone Level Below | -100 to 0 | -100dB to 0dB | 0.000 to 1.00 | Input / Output |
| Hold if Reference Level Below | -100 to 0 | -100 to  0dB | 0.000 to  1.0 | Input / Output |
| Reference Gain | -40 to 0 | -40dB to 0dB | 0.00 to 1.00 | Input / Output |
| Reference-to-Microphone Level Ratio | -10 to 10 | -10 dB to 10 dB | 0  1 | Output |
| For Component | | | | |
| Noise Reduction | 0.0 to 30.0 | 0 dB to 30.0 dB | 0.000 to 1.00 | Input / Output |
| Noise Reduction Enable | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Residual Echo Suppression | 0 to 100 | 0% to 100% | 0.000 to 1.00 | Input / Output |
| Residual Echo Suppression Enable | 1  0 | enabled  disabled | 1  0 | Input / Output |
