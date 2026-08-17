# AEC Best Practices: Gain Structure

> Source: https://help.qsys.com/Content/Application_Integration/AEC/AEC_Gain_Structure.htm

# AEC Best Practices: Gain Structure

After proper signal flow, we turn our attention to gain structure. This helps ensure a maximal signal-to-noise ratio at each microphone input. We also need to ensure adequate signal levels into the room from the far end or ends and from programs sources.

[Set Microphone Gains](javascript:void(0))

1. In Q-SYS Designer, open the design.
2. Double-click the Mic/Line In component the mics are connected to.
3. Turn on Phantom Power if required by the mics.
4. Have someone speak in a normal voice at a normal level and distance from the nearest mic.
5. Set the channel's input gain so the level registers between -15 and -20 dBFS on the meter (see Figure 2).

**Note:** Some ceiling mics may require relatively high gain settings.

Repeat this process for each microphone in the system. If all mics are the same type and distance from the speaking positions, you may simply set all to the same gain as the first.

[On Ambient Noise and Signal-to-Noise Ratio](javascript:void(0))

Watch the meter while no one is speaking and there is no program material playing. This is the noise floor for the room itself. The generally accepted minimum ratio of speech to ambient noise is 15dB, with 25dB as the desired target. Therefore, the ambient noise in the room should register at most between about -35 and -40 dBFS on the input meters. If it reads higher, you should consider the following solutions.

* Steady-state (constant) noise may be due to the HVAC system. Using noise reduction in the AEC component may reduce the noise enough to get a good signal-to-noise ratio. To configure noise reduction, open the AEC component and enable noise reduction to eliminate as much noise as possible.
* Equalization may help reduce some types of noise but could also have a negative impact on the microphone sound quality. The mic's own self-noise is a physical limitation that cannot be mitigated through gain or EQ adjustment. For example, desensitizing the mic (through gain reduction) to reduce the noise floor will also reduce the level of the spoken voice by the same amount.
* Some types of noise require physical measures such as acoustic treatments or isolation.

[Far-End Gain](javascript:void(0))

1. Turn the all amplifiers for the room all the way down. If they have no gain controls, go to the Q-SYS design and open the Output components feeding them and pull the Max RMS Output settings down to -40 dBFS.
2. Set all user controls to mid position.
3. Make a test call from the room.
4. Open the input component for the Far-End input (i.e. POTS in, VOIP In, Line In from a codec, or USB Bridge).
5. With the Far-End user speaking in a normal voice, adjust the input gain of the far-end signal so it's approximately equal to the microphones (about -15 to -20 dBFS).
6. With the Far-End still speaking, increase the amplifier gains (or coinciding Output components) until the volume in the conference room is a reasonable level (about 65 to 70 dB A-weighted)
7. Also make adjustments to the Reference-to-Microphone Level Ratio (RMLR) to ensure the Far-End reference signal is approximately equal to the Near-End microphone signal (indicated by ratio of 0 dB).
8. Adjust the conferencing transmit level so the Far-End party can hear the in-room participants.

[Set Program Gains](javascript:void(0))

Program sources can vary greatly in level and dynamic range. The key strategy is to set a good normal level and make sure the peak and transient levels do not clip the Core's analog inputs.

1. Start with the level controls at mid position.
2. Play some suitable material from the program sources and set their input gains so the level meters are in the range of -15 to -20 dBFS. With stereo sources, you should set the gains for the left and right channels identically to preserve the stereo image. A stereo program source should sound slightly louder than the Far-End signals.
3. If the program sources have output level controls, you can crank them all the way up to make sure the Core Input components do not clip or reach 0 dBFS.
4. If any do, back off on their preamp gains until the maximum levels on the input component meters do not exceed about -3 dBFS. This ensures the input gain settings are somewhat "foolproof".
5. Turn the program source levels back down till the levels are again about -15 to -20 dBFS.
6. Repeat for each program source.
