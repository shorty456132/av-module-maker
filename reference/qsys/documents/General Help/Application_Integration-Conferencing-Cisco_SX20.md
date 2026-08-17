# Cisco SX20 Codec

> Source: https://help.qsys.com/Content/Application_Integration/Conferencing/Cisco_SX20.htm

# Cisco SX20 Codec

Follow these recommendations when integrating a Cisco SX20 Codec microphone with Q-SYS.

[Configuration Overview](javascript:void(0))

This diagram shows the common configuration for connections between an SX20 and the Q-SYS Core processor.

[Disable Echo Cancellation](javascript:void(0))

To prevent interference, turn off the EchoControl setting on the SX20 so that the Q-SYS Core's AEC can handle echo cancellation.

In the SX20's web interface > EchoControl section, set Dereverberation, Mode, and NoiseReduction to 'Off'.

[Connect Audio Input to the Core](javascript:void(0))

The Line Out (unbalanced RCA) connection on the Cisco device connects to an input on the Q-SYS Core. This input will be the audio received from the far end that plays out into the room.

Wiring to the Core should be as shown below.

[Build the Design](javascript:void(0))

With the SX20 analog speaker (loudspeaker) output now connected to one of the audio inputs on the Core, now build your design in Q-SYS Designer Software. Note that:

* Any gain control should be done on the audio input channels on the Core.
* The audio input channel should then be connected to an AEC block so that the Core can perform echo cancellation for the SX20 microphones.

For example:

[Set Output Gain on the Core](javascript:void(0))

* On the stereo output channel of the Core, set the gain to -31dB. This ensures that the audio coming from the Core is correctly set to mic level when itâs connected to the SX20 mic input.
* Set the analog ouputs to -51dB to match the signal going to the SX20 Codec.

[Disconnect Speaker Out](javascript:void(0))

If the SX20 is also connected to an HDMI matrix switcher, you must either disconnect the Speaker Out from the SX20 or set its volume to 0 to mute it. This prevents duplicate audio from being sent to the Core causing echo and garbled audio.

[Monitor Clipping](javascript:void(0))

Monitor clipping on the SX20 with a VU-meter:
