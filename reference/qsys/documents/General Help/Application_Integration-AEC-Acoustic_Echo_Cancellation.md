# Acoustic Echo Cancellation (AEC) Application

> Source: https://help.qsys.com/Content/Application_Integration/AEC/Acoustic_Echo_Cancellation.htm

# Acoustic Echo Cancellation (AEC) Application

This content explains how to optimally set up AEC in a Q-SYS design, including best practices for signal flow and setting a useful gain structure. After completing these steps, your conferencing system should be ready for full use, and the AEC should remove echoes superbly enough that the Far-End party or parties can enjoy good intelligibility without distracting effects.

**Note:** This topic primarily applies to designs using the [Acoustic Echo Canceler](../../Schematic_Library/acoustic_echo_canceler_simd.htm) component with third-party microphones. If your design includes the Q-SYS [NM-T1](../../Hardware/Audio_IO/NM-T1.htm) beamforming conferencing microphone, refer to the [Mic In (NM-T1)](../../Schematic_Library/microphone_beamformer_with_aec.htm) topic for schematic examples and control information. (The Mic In component includes integrated AEC processing.)

#### [AEC Best Practices: Signal Flow](AEC_Signal_Flow.htm)

Start here to configure proper AEC signal flow.

#### [AEC Best Practices: Gain Structure](AEC_Gain_Structure.htm)

After configuring proper signal flow, set the proper gain structure.

#### [AEC Troubleshooting](AEC_Troubleshooting.htm)

Hitting a snag? Try these AEC fixes.
