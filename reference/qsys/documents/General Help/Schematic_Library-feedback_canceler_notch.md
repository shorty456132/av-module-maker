# Notch Feedback Controller

> Source: https://help.qsys.com/Content/Schematic_Library/feedback_canceler_notch.htm

# Notch Feedback Controller

The Q-SYS Notch Feedback Controller allows you to set feedback suppression based on the room, and automatically suppress feedback. Notch Feedback Control is the method of feedback control used by the Q-SYS Notch Feedback Controller.

The Notch Feedback Controller reduces the gain at the notch frequency while affecting the gain at surrounding frequencies as little as possible. Audio engineers sometimes insert parametric notch filters manually at peak frequencies, prior to the live event, to help prevent undesirable feedback from occurring. This is called "ringing out the room". Notch Feedback Control is an automated way of "ringing out the room".

The Q-SYS Notch Feedback Controller allows the undesirable feedback to begin, and then detects the frequency at which the undesirable feedback is occurring. The NFC then places a notch filter at this frequency.

[About Filters](javascript:void(0))

There are two types of filters in the NFC: Fixed and Dynamic.

* Typically, you use Fixed Filters for cutting feedback based on the acoustics of the room. You set them when the room is quiet, and leave them there. You use only what you need to cover the room.
* Use Dynamic Filters for feedback spikes that happen during the live event. The system sets them and can move them as needed. The NFC uses Dynamic Filters only when there are no Fixed Filters available for activation. Fixed Filters take precedence over the Dynamic Filters. The NFC will activate a Fixed Filter prior to a Dynamic Filter when both have filters available for use.
* When the NFC activates a Fixed Filter, it stays positioned at the same frequency until you clear it or remove it. The NFC can move a Dynamic Filter as needed.
* The Active number next to the Filter Count changes every time a filter is activated, cleared or removed. The Dynamic Filter has a Standby mode that gives the number of Dynamic Filters that are not currently attenuating a frequency and have passed the Reclaim Time limit.

### General Information

* There are up to 32 filters available for use (refer to the Properties section below). You can divide these filters between Fixed and Dynamic filters using the Filter Count controls.
* The filters can be set to one of four bandwidths: 1/5, 1/10, 1/20, and 1/80 of an octave.
* The absolute minimum bandwidth of any filter is 15 Hz. If you have your Notch Bandwidth set to a narrow setting, for example 1/80th of an octave, then at low frequencies 1/80th of an octave may be less than 15 Hz. In this case the notch filter bandwidth will still be 15 Hz. For example in the octave between 50 and 100 Hz 15 Hz is is about 1/3 of an octave. In this case, the NFC creates a filter with an appropriate Notch Bandwidth greater than 1/80th of an octave.
* The NFC does not create filters below 80 Hz. Generally, undesirable feedback does not happen at this frequency and below.
* When the NFC adds a filter, a small orange (for Fixed) or blue (for Dynamic) marker displays at the top line of the graph. Hover over the marker to see specific information about the filter, including frequency, gain (attenuation), bandwidth, and a Remove or Clear button.
* In order for a frequency to be considered as undesirable feedback, it must exceed the set Threshold.

[Setting Up the Notch Feedback Controller](javascript:void(0))

### In the Venue

Place the microphones and loudspeakers where they will be in the live event.

### Q-SYS Designer

1. With Q-SYS Designer in Design mode, place an NFC in the signal flow just before the signal feeds to the channel of an amplifier. Each channel of each amplifier, used in the room, should have an NFC.  
   In the case of a mono signal, converted to a stereo or multichannel output, place the notch filter on the mono signal before converting it.
2. Run the Q-SYS design.
3. Set the gain structures of the microphones as you normally would.
4. In the NFC control panel, set the Threshold to about -46 dB.
5. Set the Fixed Filter Count to 6. The Dynamic Filter Count should be 0.
6. Make sure the room is as quiet as possible; do not talk into any microphone.
7. Raise the Gain until the system starts to feedback and filters become active.
8. Lower the Gain to where you would normally have it set in the live event.
9. Raise the Threshold to -40 dB.
10. Lower the Fixed Filter Count to the number of filters that were activated (step 7).
11. Set the Dynamic Filter Count to about 6.

[Using the Notch Feedback Controller](javascript:void(0))

When the event starts, the system detects any frequency that exceeds the Threshold, and sets a Dynamic Filter. If you find that there are too many filters being set, raise the Threshold.

[Inputs and Outputs](javascript:void(0))

### Input Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

### Output Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Notch Feedback Controller Properties

#### Max Filter Count

Sets the maximum number of filters that can be used in the Notch Feedback Controller. This number can be divided between Fixed and Dynamic Filters. You can choose between 8 and 32.

[Controls](javascript:void(0))

#### Bypass

Bypasses the Notch Filter Controller.

When the component is bypassed, audio is passed through without any change. The word "BYPASSED" is displayed in red in the control panel.

#### Mute

Mutes the audio signal at the input of the component.

No audio is passed. Any Dynamic Filters are put in Standby based on the Reclaim Time.

#### Gain (dB)

Controls the overall gain through the Notch Filter Controller component.

#### Clear All

Clears all Fixed and Dynamic Filters.

#### Clear Dynamic

Clears only the Dynamic Filters.

#### Clear

This button is found when you hover over a Dynamic Filter's blue marker. It Clears the associated Dynamic Filter. The filter is not active, and is available for use.

#### Remove

This button is found when you hover over a Fixed Filter's orange marker. It Removes the associated Fixed Filter. The filter is not active, and is no longer available for use - the Fixed Filter Count is decremented by one.

#### Fixed Filter Count (whole number)

The maximum number of Fixed Filters that can be activated.

If the total number of Fixed and Dynamic is at the Maximum limit as set in the Properties, the Fixed Filter Count can be raised which will automatically reduce the number of Dynamic Filters.

#### Fixed Filter count Active (whole number)

The number of Fixed Filters currently active. Cannot exceed the Fixed Filter Count.

#### Dynamic Filter Count (whole number)

The maximum number of Dynamic Filters that can be activated.

If the total number of Fixed and Dynamic is at the Maximum limit as set in the Properties, the Dynamic Filter Count cannot be raised unless the Fixed Filter Count is lowered.

#### Dynamic Filter Count Active / Standby (whole number)

The number of Dynamic Filters currently active. Cannot exceed the Fixed Filter Count.

When the need for a Dynamic Filter is removed (no undesirable feedback at that frequency) the attenuation is removed, but the blue marker is still visible, that Dynamic Filter is in Standby. If feedback is detected, the filter is removed from Standby and made active at the feedback frequency. After the Dynamic Filter has been in Standby for 140 seconds it returns to the inactive state. While in Standby a dynamic filter is more sensitive to the need for feedback suppression at its frequency then when it is inactive.

#### Notch Bandwidth (octave)

Sets the bandwidth of the notch filters. A narrower bandwidth attenuates the feedback frequency without attenuating the surrounding frequencies as much as a wider bandwidth. A bandwidth that is too narrow becomes less effective because of the feedback frequency detection.

The Bandwidth is measured from -3 dB to -3 dB points of the notch filter.

#### Feedback Threshold (dB)

When a frequency's amplitude exceeds this level, a filter is activated. in addition to exceeding the Feedback Threshold the amplitude at a particular frequency must exceed the average amplitude of the audio spectrum by an internally defined amount.

#### Min & Max Dynamic Frequency (Hz / kHz)

These two parameters set the frequency range where Dynamic Filters can be activated.

#### Dynamic Filter Reclaim Time (seconds)

The Reclaim Time is the time between when the feedback, being suppressed by a Dynamic Filter, drops below the Threshold, and when the attenuation of the filter is removed. You can adjust this time to avoid Dynamic Filters "popping" in and out for recurring feedback.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Active Dynamic-Filter Count | 0 - 32 | 0 to 32 | 0 to 1.00 | Output |
| Active Fixed-Filter Count | 0 - 32 | 0 to 32 | 0 to 1.00 | Output |
| Bandwidth  (octave) | N / A | 1/5, 1/10, 1/20, 1/80 | N / A | Input / Output |
| Bypass | 0  1 | no / bypassed | 0  1.00 | Input / Output |
| Clear All | (trigger) | | | Input / Output |
| Clear Dynamic | (trigger) | | | Input / Output |
| Dynamic Filter Count | 0 - 32 | 0 to 32 | 0 to 1.00 | Input / Output |
| Dynamic-Filter Info | (text) | | | Output |
| Dynamic Filter Reclaim Time | 5.00 - 120 | 5.00 s to 120 s | 0 to 1.00 | Input / Output |
| Fixed Filter Count | 0 - 32 | 0 to 32 | 0 to 1.00 | Input / Output |
| Fixed-Filter Info | (text) | | | Output |
| Gain | 0 - 32 | 0 to 32 | 0 to 1.00 | Input / Output |
| Max Dynamic Frequency | 80 - 20,000 | 80 Hz to 20 kHz | 0 to 1.00 | Input / Output |
| Min Dynamic Frequency | 10 - 20,000 | 10 Hz to 20 kHz | 0 to 1.00 | Input / Output |
| Mute | 0  1 | unmuted / muted | 0  1.00 | Input / Output |
| Standby Dynamic-Filter Count | 0 - 32 | 0 to 32 | 0 to 1.00 | Output |
| Threshold | N / A | -70 dB to -20 dB | 0 to 1.00 | Input / Output |
