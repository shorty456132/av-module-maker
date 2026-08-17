# Custom Voicing

> Source: https://help.qsys.com/Content/Schematic_Library/loudspeaker_custom_voicing.htm

# Custom Voicing

Provides custom voice capability for loudspeakers that do not have Intrinsic Correctionâ¢ and that are not Distributed. You can create Custom Voicing one time, and use it for as many loudspeakers that you have that would use the same voicing.

You can assign Custom Voicing to each loudspeaker with the same voicing needs:

* one at a time, or
* select all the desired Loudspeaker Status/Control components in the Schematic and choose the same Custom Voicing for all the selected components.

After you have selected Custom Voicing for a loudspeaker, the Name of the Custom Voicing assigned to that loudspeaker displays, in parentheses, in the title of the Loudspeaker Status/Control component and its control panel.

[FIR Filtering](javascript:void(0))

You can load a custom FIR coefficients file at runtime. Typically, a FIR filter is designed using filter design software that computes the coefficients. After you design the filter, you export the coefficients to a .csv (comma separated value) or .wav file. This file is then loaded at runtime by clicking Load Coefficients - see [Controls](#Controls). The file containing the coefficients is a row of values, separated by commas, representing time from left to right.

**Note:** Ensure that the Coefficient Count equals the number of coefficients (FIR taps) in your FIR coefficients file, and does not exceed the limitations of your hardware. See [Properties](#Properti).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Custom Voicing Properties

#### Coefficient Count

Determines the number of coefficients for the FIR filter. The quantity defined here must match the number of coefficients contained in the .wav or .csv file loaded at runtime, and cannot exceed the limitations of the hardware:

* CXD-Q and CX-Q 4-channel amplifiers: 1,024 taps
* CXD-Q and CX-Q 8-channel amplifiers: 200 taps
* SPA-Q Series: Not Supported
* DataPort cards / amplifiers: 200 taps
* Core: 16,384 taps

#### Channel Index

Select how control indexes are determined for each Custom Voicing component in your design. Choices are 4 to 16,384.

* Auto: (Default) Components in existing designs upgraded to Q-SYS v9.2.0 and later will continue to use a 0-based index. New components use a 1-based index, which matches the functionality of other Q-SYS components.
* 0-Based: The component will use a 0-based index, meaning that control indexing starts at 0. This is useful for maintaining consistency with other components and for re-using control scripts.
* 1-Based: The component will use a 1-based index, meaning that control indexing starts at 1. This matches the functionality of other Q-SYS components.

#### Band Count

The number of bands to which this Custom Voicing will apply. When this Loudspeaker Custom Voicing Component is identified by a Generic Speaker component, the Band Counts must match. Choice provided are 1-8.

[Controls](javascript:void(0))

[Gain](javascript:void(0))

#### Mute

Mutes the output of the associated Band.

#### Invert

Inverts the output signal of the associated Band.

#### Gain (dB)

Sets the output Gain.

[Delay](javascript:void(0))

#### Delay (ms)

Sets the Delay for the associated Band.

**Note:** Entering anything from 0.001Âµs to 0.005Âµs gets interpreted as 1.00 through 5.00 milliseconds. Entering anything greater than 0.005 gets interpreted as the milliseconds as entered (example 0.006 gets interpreted as .006 ms). The basic idea is that the value that you enter is larger than the max value and Q-SYS Designer assumes you want the value to be divided by 1000. If you need to input less than 6ms, you must manually type in ("5us", "4us", etc.). You will then see it convert to .005 ms, .004ms, etc.

[Crossover High and Low-Pass](javascript:void(0))

#### Bypass

Bypasses the High and / or the Low-pass Crossover Filter.

#### Type

Sets the type of filter used for the crossover.

#### Slope

Sets the amplification per octave.

#### Normalization

Sets the type of Normalization for the Bessel-Thomson filter when selected.

#### Frequency (Hz)

Sets the cutoff Frequency for the High and Low-Pass filters.

[Voicing Filters](javascript:void(0))

#### Bypass

Bypasses the associated Voicing Filter for the associated Band.

**Note:** The Bypass button is the small square button to the left side of the Type field for each band.

#### Type

Sets the Type of equalizer for the associated Voicing Filter/ Band. When you select the Type, the availability of the following controls depend on the Type you select.

#### Order

Sets the Order for all of the types of equalizers except the Parametric for the associated Voicing Filter/Band.

#### Gain (dB)

Sets the Gain for the associated Voicing Filter / Band. Type the desired Gain. Not available for the All-Pass filter.

#### Q / Width (octave)

Type the desired width, in octaves. Frequencies within this bandwidth, centered around the Frequency parameter, are amplified.

#### Frequency (Hz)

Sets the frequency point for the equalizers. Type the desired frequency.

For the Parametric this is the center frequency of the bandwidth. The frequencies in this bandwidth are amplified. For the High and Low-Shelf equalizers, it is the cutoff frequency. The frequencies above or below this point are amplified.

[FIR](javascript:void(0))

#### Bypass

Click to bypass the FIR filtering.

#### Response Graph

The scales for the Response Graph vary depending on the measurement method you select, see below.

The vertical line of the crosshair cursor provides a readout of its position on the X axis scale.

The vertical movement of the horizontal crosshair follows the magnitude or amplitude of the signal.

#### Magnitude

Measures the magnitude of the input signal over the audio frequency range. Represented by the blue line.

#### Magnitude / Phase

Same as the Magnitude selection but with the addition of a phase line.

#### Impulse

Measures amplitude (Y axis) vs. time in milliseconds (X axis) of the impulse response.

#### Load Coefficients

Opens a standard Windows "Open" dialog box where you can navigate to, and open either a .csv or .wav file containing the coefficients defining the filter.

[Control Pins](javascript:void(0))

[General](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Alignment Delay | 0 to .005 | 0 ms to 5 ms | 0 to 1.00 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| JSON | (text) | | | Input / Output |

[Crossover High and Low-Pass](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Bypass | 0  1 | no  bypassed | 0  1 | Input / Output |
| Frequency | 10 to 12000 | 10 Hz to 12 kHz | 0 to 1.00 | Input / Output |
| Normalization | 0  1  2  3 | -3 dB Mirror Mag  -3 dB Flat Group Delay  Natural Mirror Mag  Natural Phase Match | 0  .333  .667  1.00 | Input / Output |
| Slope | 6  12  18  24  30  36  42  48 | 6 dB/Oct  12 dB/Oct  18 dB/Oct  24 dB/Oct  30 dB/Oct  36 dB/Oct  42 dB/Oct  48 dB/Oct | 0  .143  .286  .429  .571  .714  .857  1.0 | Input / Output |
| Type  (Range is dB/Octave) | 2.00  3.00  4.00 | Butterworth  Linkwitz-Riley  Bessel-Thomson | 0  .500  1.00 | Input / Output |

[Master](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Bypass | 0  1 | no  bypassed | 0  1 | Input / Output |

[Voicing 1 - 9](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Bandwidth  (Parametric Only) | 0.010 to 1.00 | .010 to 1.00 | 0 to 1.00 | Input / Output |
| Bypass | 0  1 | no  bypassed | 0  1 | Input / Output |
| Frequency | 10 to 20000 | 10 Hz to 20 kHz | 0 to 1.00 | Input / Output |
| Gain  (All except All-Pass) | -100 to 20 | -100 dB to 20 dB | 0 to 1.00 | Input / Output |
| Order  (All except Parametric) | 1.00  2.00 | 1st Order  2nd Order | 0  1 | Input / Output |
| Q Factor  (All except Parametric)  (2nd Order only) | .300 to 30.0 | .300 to 30.0 | 0 to 1.00 | Input / Output |
| Type | 0  1.00  2.00  3.00 | Parametric  Low-Shelf  High-Shelf  All-Pass | 0  .333  .667  1.00 | Input / Output |
