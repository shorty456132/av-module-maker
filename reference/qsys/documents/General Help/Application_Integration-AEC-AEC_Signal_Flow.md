# AEC Best Practices: Signal Flow

> Source: https://help.qsys.com/Content/Application_Integration/AEC/AEC_Signal_Flow.htm

# AEC Best Practices: Signal Flow

Properly configuring AEC signal flow comprises several basic principles.

**Note:** For examples of these best practices in AEC setup, look to the sample conference room designs available to download in Q-SYS Library. These sample designs may be use as examples, or as a base or starting point to build your own project.

[Best Practices](javascript:void(0))

[Compose the Correct Reference Signal](javascript:void(0))

In a conference system without in-room reinforcement ("voicelift"), everything routed to the loudspeakers should also be sent to the Reference pin.

* All far-end audio sources, as well as program material heard in the room should be routed to the Reference.
* A mic signal should NEVER go into it's own AEC Reference.
* A mic should NEVER got to the AEC Reference of another mic if they are both likely to pick up the same voices or sounds.

[Use a Separate AEC Channel for Each Conferencing Mic](javascript:void(0))

If there are several Mics in the same environment, use a multichannel AEC component with a single reference pin.

[Mic Processing Should Be AFTER the AEC Component](javascript:void(0))

The AEC algorithm works best on signals with processing paths similar to the Reference signal.

[Place End-User Level Controls AHEAD of the Reference Pin](javascript:void(0))

This applies to any signal mixed into the Reference pin.

[Schematic Example](javascript:void(0))

The POTS conference room sample design properly locates mic processing and user level controls (the gain controls in the POTS or VoIP inputs, on the USB endpoint, and the flex stereo input pairs), and also properly mixes signals into the AEC block reference pin.
