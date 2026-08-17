# Delay Component

> Source: https://help.qsys.com/Content/Schematic_Library/delay.htm

# Delay

The Delay introduces a delay in the audio signal in order to compensate for the placement of speakers.

[Overview](javascript:void(0))

The Delay Component is capable of up to 256 Channels and 512 Taps. For each Channel, there are *n*Taps. For example, if you selected 100 Channels and 5 Taps, the result would be 5 Taps per Channel, or 500 total Taps.

You can Bypass, Mute, Invert and control the Gain for all Taps/Channels. For the individual Taps and associated Channels, you have the same controls provided at the Master, with the addition of a control for the Delay time. You can control overall maximum delay for all Taps in the Component Properties.

There are three Delay types available in Q-SYS Designer Software: Standard Delay, Fractional Delay, and Crossfaded Delay. You can select which type of Delay you want to use from the Properties.

* Standard Delay
  + Rounds the Delay time to the nearest whole number of samples
  + Ramps the signal level down to -20 dB then ramps back to the original signal level but at the new delay time
  + Use the Standard Delay if a level dip during delay changes is acceptable. This Delay uses the least Signal Processing resources.
* Crossfaded Delay
  + Rounds the Delay time to the nearest whole number of samples
  + Maintains two delay lines for each tap. When the Delay time changes, one of the delay lines is updated with the new delay time, the other uses the original delay time. The output signal changes to the new time by fading from the original Delay time completely to the new Delay time.
  + Use the Crossfaded Delay if the aforementioned level dip is unacceptable. This Delay uses a medium amount of Signal Processing resources.
* Fractional Delay
  + Interpolates the audio signal between samples if the Delay time is not equal to a whole number of samples
  + Ramps the Delay time to the new Delay time, the signal level is not changed
  + Use the Fractional Delay if you need sub-sample delay resolution. This Delay uses the most Signal Processing resources.

**Tip:** For all delay types, you can optionally configure delay calculation based on distance and temperature, which is especially useful for outdoor venues. Refer to the [Distance Controls](#Distance) property.

[Schematic Example](javascript:void(0))

In this example, we have our channel outputs routing through a Delay component to impose an audio delay before reaching our surround speakers.

[Inputs and Outputs](javascript:void(0))

### Inputs

Up to 256 channels of audio.

### Outputs

There is a minimum of one audio-delay Tap for each Input Channel, a maximum of 512 Taps per Input Channel. The outputs. on the component, are arranged by Tap then Channel. For example Tap 1 Channel 1, Tap 2 Channel 1.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Delay Properties

#### Tap Count

Determines how many taps per channel there are, from 1 to 32.. Choose the number of Taps to equal the maximum number of delays needed for any one channel.

#### Max Delay (seconds)

Limits the Delay time range for the controls in the Control Panel, from 0.001 to 60. Choose this number based on calculations to determine the Channel/Tap combination requiring the most delay. This setting affects all Taps.

#### Delay Type

Changes the component to one of three types of Delays - Standard, Crossfaded, and Fractional. The Delay types are explained in the introduction section of this topic.

#### Linear Tap Gain

Provides a linear gain for each Tap in support of acoustic positioning control.

#### Distance Controls

When set to 'Yes', and for each Tap, you can enter a distance (in meters or feet, depending on the selected Units in the Configuration tab) between the listening location and the speaker. This value, combined with the current temperature specified in the Configuration tab (in either Celsius or Fahrenheit), are used to calculate the Delay.

### Channels

#### Type (Channel)

Determines the Crossover Component's channel type - Mono, Stereo, or Multi-Channel. (Stereo = two mono channels)

#### Count (Multi-Channel)

When you choose Multi-Channel, you can specify from 2 to 256 for the Count.

[Controls](javascript:void(0))

### Delay Tab

#### Bypass

Master - bypasses all Taps and the Gain control

Tap - affects only that Tap and all associated Channels.

#### Mute

Master - mutes the audio signal for all Taps

Tap - affects only that Tap and all associated Channels.

#### Invert

Master - inverts the signal for all Taps

Tap - inverts the signal for only that Tap and all associated Channels.

#### Gain

Master - controls the overall gain for all Taps, from -100 to 20 (default is 0)

Tap - affects only that Tap and all associated Channels.

#### Delay (milliseconds)

Master - N / A

Tap - controls the delay time of the audio signal for an individual Tap, and all Channels for that Tap, from 0 to 100 (default is 0). The Max Delay setting, in the Component Properties, sets the maximum delay for all Taps.

**Note:** Entering anything from 0.001Âµs to 0.005Âµs gets interpreted as 1.00 through 5.00 milliseconds. Entering anything greater than 0.005 gets interpreted as the milliseconds as entered (example 0.006 gets interpreted as .006 ms). The basic idea is that the value that you enter is larger than the max value and Q-SYS Designer assumes you want the value to be divided by 1000. If you need to input less than 6ms, you must manually type in ("5us", "4us", etc.). You will then see it convert to .005 ms, .004ms, etc.

#### Distance

This control only appears if the Distance Controls property is set to 'Yes'. Specify the distance value, in meters (default) or feet, between the speaker and the listener, from 0 to 229 meters or 0 to 653 feet. This value, combined with the specified Temperature on the Configuration tab, calculates the Delay.

### Configuration Tab

#### Units

Specify either Metric (SI) or US (USCS). This determines whether the Temperature value Celsius or Fahrenheit, and whether the Distance control is in meters or feet.

#### Temperature

Specify the current temperature of the environment in which the speakers are placed, from -100 Â°C or Â°F to 250 Â°C or Â°F.

**Tip:** For a long-duration event, as with an outdoor concert, consider exposing and wiring the input Temperature control pin to a script that receives regular temperature updates.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Master Bypass | 0  1 | active  bypass | 0  1 | Input / Output |
| Master Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Master Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Master Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Temperature | -100 to 250 | -100Â°C to 250Â°C  100Â°F to 250Â°F | 0.00 to 1.00 | Input / Output |
| Units | - | Metric (SI)  US (USCS) | - | Input / Output |
| Bypass | 0  1 | active  bypass | 0  1 | Input / Output |
| Delay | 0.000 to 60.0 | 0 ms to 60.0 s | 0.000 to 1.00 | Input / Output |
| Distance | 0 to 229  0 to 653 | 0 to 229m  0 to 653ft | 0.00 to 1.00 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
