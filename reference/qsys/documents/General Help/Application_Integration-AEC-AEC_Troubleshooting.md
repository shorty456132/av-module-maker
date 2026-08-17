# AEC Troubleshooting

> Source: https://help.qsys.com/Content/Application_Integration/AEC/AEC_Troubleshooting.htm

# AEC Troubleshooting

Here are some common AEC problems and solutions.

[If the Far-End Party Hears an "Underwater" Effect from the Conference Room Microphones](javascript:void(0))

* "Underwater" effect almost always comes from one or more conference room mics being fed to the AEC Reference. Double-check that no conferencing mics are routed or mixed into the AEC Reference pin.
* If you are working with a teleconferencing codec, make sure AEC is disabled in the codec and that the Core is not feeding the codec's program input. Also check that the codec is not in "reinforcement mode", which is intended for the codec output to be connected directly to an amplifier input (it loops the mics back to the AEC Reference, which will cause quality issues). The telltale sign is hearing the conference mics in the room when there is local reinforcement.

[If the Far-End Hears an Echo of Their Own Voice](javascript:void(0))

* Confirm that the receive signal from the Far-End, after its processing stages, isn't routed to transmit back to the Far-End.
* This could also mean that the conference mics are picking up more Far-End volume than what is fed to the Reference. To check this, refer to the Reference-to-Microphone Level Ratio (RMLR) meters in the AEC component to ensure the Far-End reference signal is approximately equal to the Near-End microphone signal (indicated by ratio of 0 dB). If adjusting the RMLR does not have enough effect, other corrective measures may be needed:

  + Reduce the affected mic gains until their response to the Far-End signal is about 3 to 6 dB lower than the reference signal. The transmit signal will need to be increased accordingly.
  + Boost the reference signal routed to the AEC Reference pin. If necessary, insert a gain component between the user level control and the Reference pin. Increase the gain so the Far-End signal is about 3 to 6 dB higher than the conference mic response.
  + If the reference to mic signal ratio is correct as they respond but Far-End still experiences echo, the cause may be residual echo. This can be remedied a couple ways.

    1. Enable and adjust the Residual Echo Suppression (RES) setting in the AEC component. This applies additional suppression to any residual echo not removed by the adaptive filter and echo reduction functions of the AEC.

       **Note:** The more this is turned up, the more aggressively the residual echo is suppressed, but at the expense of distorting the Near-End microphone signal.
    2. The Tail Length property of the AEC may need to be increased if the room is especially reverberant. After adjusting and re-deploying the design, have the Far-End speak again to test the settings.

       With the Far-End still speaking, set the gain control in the POTS In or VOIP Gain component (after the EQ component) to maximum. Check that the amplifier is not clipping and adjust if necessary. You may also adjust the maximum output of the Output component channels to below the amp's clipping point. Do the same for each Far-End signal source and calibrate the receive signals to the same level.

       **Note:** Increasing Tail Length doubles DSP usage for each level of increase. This must be accounted for in the total processor usage. (Default setting is 200 ms)
* The Adaptive Filter may need adjustment to compensate for when the AEC adaptation stops. The Hold If Mic Level Below filter sets the threshold, in dB, for when this occurs. Typically, microphone signal will be nonexistent when a mic's mute feature is activated, so the default of -100 dB should suffice. However, some mics may only strongly attenuate signal when muted. This weak signal can cause issues with AEC adaptation. In this case, try adjusting the Hold level to just about the level when the mic is muted.
* As with the Mic Level filter, the same adjustments can be made for the reference signal using the Hold If Ref Level Below filter.
