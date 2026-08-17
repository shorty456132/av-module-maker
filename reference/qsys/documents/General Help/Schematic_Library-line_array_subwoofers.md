# Loudspeakers

> Source: https://help.qsys.com/Content/Schematic_Library/line_array_subwoofers.htm

# Loudspeakers

Q-SYS supports several groups of loudspeaker types. Although the groups are different, the majority of Controls, Properties, and Control pins are identical. In this topic, the Controls, Properties, and Control Pins are listed together, and noted where they differ between loudspeakers. Each loudspeaker needs to be configured based on its model, specific hardware configuration, and venue considerations. The following is a listing of the groups of loudspeaker components available in Q-SYS Designer Software.

Q-SYS allows the addition of loudspeakers and loudspeaker systems other than those manufactured by QSC. This Generic and Generic 70V/100V (distributed audio) Speaker components allow you to configure Q-SYS to meet the specifications of other, or generic, loudspeakers or loudspeaker systems.

Inline Processing allows you to apply the Intrinsic Correction or Basic Correction settings for a QSC loudspeaker even if you're using an amplifier that is not directly supported by Q-SYS.

[Properties](javascript:void(0))

[Common](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

These Properties are common to many loudspeaker models.

#### Mode

Not all of the loudspeakers have the Mode property. For those that have a Mode Property, the selections vary:

* Low-Z: Indicates a low impedance system.
* 70 V / 100 V: Indicates a distributed system.
* 2-Way, 3-Way, 4-Way: Indicates the number of separate amplifier channels.

#### Inline Processing

Inline processing allows you to apply the Intrinsic Correction or Basic Correction settings for a QSC loudspeaker even if you're using an amplifier that is not directly supported by Q-SYS. With Inline Processing, the correction is accomplished in the Core.

Notes:

* Inline Processing is not applicable for DataPort amplifiers (CX & DCA series), as loudspeaker processing is accomplished by the [CODP4 â DataPort Output Card](../Hardware/IO_Expanders/CODP4.htm).
* Inline Processing is not applicable to network amplifiers (CXD-Q, CX-Q, and DPA-Q series), as loudspeaker processing is accomplished by the amp's internal processor.

#### External Prefix

*(ILA, WideLine, PL-LA, WL, and GP loudspeakers only)*: Specify a prefix that is applied to external channel names when they are brought into the system.

[E-Series](javascript:void(0))

#### Contours

This property determines the EQ filter for the loudspeaker:

* Normal : (Default) The basic voicing of the loudspeaker. Intended to operate over the full bandwidth of the loudspeaker.
* Normal Xover : Intended to operate the loudspeaker with a high pass filter optimized for use with a subwoofer.
* Dance : Equalized (low and high frequency emphasis) for modern, electronic dance music.
* Dance Xover : Equalized for modern, electronic dance-type playback with a high pass filter optimized for use with a subwoofer.

[Line Arrays](javascript:void(0))

#### Box Count

The total number of loudspeaker Boxes in the array. This field is the sum of the Boxes in each segment.

#### Splay

The splay angle of the entire array, from 0Â° to 90Â°. Available only with more than one segment.

#### Segments

Boxes are grouped into segments, from 1 to 8.

#### Legacy Voicing

For WideLine-8 arrays only:

* Select 'No' to use the newer voicing that offers improved balance. This is the default in Q-SYS version 8.3 and later for new WideLine-8 loudspeaker components.
* Select 'Yes' to use the older voicing profile. This is the default for designs with existing WideLine-8 components that have been upgraded to version 8.3 and later. For existing components, you can optionally switch to the newer voicing.

[PL-Series](javascript:void(0))

PL Series voicings use an advanced form of intrinsic correction.

Q-SYS Acoustic Linear Phase design employs a combination of FIR, IIR and all-pass filters, overcoming typical phase related shortcomings found in many loudspeakers.

* Provides a uniform listening experience and the best sound reproduction possible for the entire audience, in any application.
* Allows for improved systemâs frequency response consistency within the coverage angle by ensuring that each loudspeaker achieves an acoustic output that maintains the phase relationship of the input signal.
* PL Series loudspeakers and subwoofers display a consistent phase relationship, leading to seamless deployment and combination of such models. All the different voicings and crossovers are sharing the same phase reference. The only phase adjustment that the user has to take care of is the physical distance between the loudspeakers.

#### Crossover

When used with a subwoofer the PL Series loudspeakers offer 3 cut-off frequencies. The acoustic summation of subwoofers and loudspeakers will be the same for each of those frequencies (assuming that the same frequency is chosen in the Low-Pass filter of the Subwoofer and the High-Pass of the Loudspeaker). The selection of the frequency depends on personal taste, subwoofer location, or the sharing of the power between subwoofer and loudspeakers.

Choosing different frequencies for subwoofers and loudspeakers will result in an overlap or a hole in the frequency range.

The subwoofer shares the same phase and amplitude characteristics, the only difference being the LF extension and the maximum Sound Pressure Level.

#### Low Pass Filter

*(For PL-SUB speakers only)*: The Low Pass filter amplifies frequencies below a set frequency, and attenuates the frequencies above that set frequency. You can choose 80Hz, 100Hz, or 125Hz.

#### Contour

Custom-tailored frequency response adjustments, allowing precise tuning to achieve optimal sound quality for specific speaker models.

There are two sets of Contour, the âDefaultâ one has been voiced to provide an out-of-the-box optimum result. The âflatâ contour is provided without the additional EQ and is a technically neutral contour (but still featuring Intrinsic Correction) that will can be voiced to different tastes.

**PL-CA Coaxial**

* Default: This is the default option and will use the default contour settings for the speaker.

* Flat: Provides a frequency response that is uniform across the audio spectrum. This will reproduce audio content without emphasizing or attenuating specific frequency ranges.

**PL-Line Array**

* Default: This is the default option and will use the default contour settings for the speaker.

* Flat: Provides a frequency response that is uniform across the audio spectrum. This will reproduce audio content without emphasizing or attenuating specific frequency ranges.

**PL-DC26 PLDC8**

It is important to select the voicing that correspond to the physical directivity of the Loudspeaker. (A sticker in the input cup generally indicates the directivity if different than the one delivered by the factory).

* 120x50 (Default for PL-DC26 and PL-DC8): Indicates the horizontal and vertical coverage angles of the speaker in degrees. The speaker has a horizontal dispersion of 120 degrees and a vertical dispersion of 50 degrees.

* 90x50: Indicates the horizontal and vertical coverage angles of the speaker in degrees. The speaker has a horizontal dispersion of 90 degrees and a vertical dispersion of 50 degrees.

* 120x50 Flat: The speaker is configured with a flat frequency response pattern of 120 degrees in the horizontal plane and 50 degrees in the vertical plane.

* 90x50 Flat: The speaker is configured with a flat frequency response pattern of 90 degrees in the horizontal plane and 50 degrees in the vertical plane.

**PL-DC12**

It is important to select the voicing that correspond to the physical directivity of the Loudspeaker. (A sticker in the input cup generally indicates the directivity if different than the one delivered by the factory).

* 110x50

* 90x50 (default)

* 70x50

* 110x50 flat

* 90x50 flat

* 70x50 flat

**PL-SUB**

* Omni (Default): Provides a configuration that optimizes the speaker for omnidirectional sound dispersion. This contour will radiate sound in a 360-degree pattern

**PL-SUB18**

* Omni (Default), setting
* CardioBack: Needed when two or more subwoofer are deployed in a cardioid configuration when the subwoofer are deployed back to back. Apply this contour to the PL-SUB facing backward.
* CardioStack: Needed when two or more subwoofer are deployed in a cardioid configuration and the subwoofer are stacked (flown in the array or ground-Stacked). Apply this contour to the PL-SUB facing backward.

#### UseArrayCorrection

*(For PL-Line Array speakers only)*: One of the advantages of line arrays is their predictable array behavior. As length of array and splay angle increase, frequency response increasingly tilts downward towards the high frequencies. This tilt is easily calculated and is correctable using DSP filters. Array correction is similar to the HF boost typically applied to constant directivity horn and compression driver systems. For line array loudspeakers, Q-SYS automatically applies Array Correction based on the Box Count and Total Splay properties of a speaker component. Splay should be the sum of the splay between boxes for the entire array. For example, a four-box array with 5 degrees between each box would have a 15 degree Splay.

#### High Pass Filter

*(For PL-Line Array speakers only)*: You can choose 80Hz, 100Hz, or 125Hz and âNo Subâ that allows the loudspeaker to work to its maximum LF extension. Note that on some of the smaller speakers such as PL-DC24, some of those choices are not available as the loudspeaker bandwidth does not allow it.

For PL-DC24 and PL-DC26, an âUnderbalconyâ choice at 300Hz is also available for situations where the LF part of the signal is provided by a Front of House system. The Underbalconny setting is not meant to be used with a corresponding subwoofer Low pass filter.

**Note:** In v10.0.1 and later, adjustment of High Pass Filter settings for the PL Series is no longer performed in Properties prior to saving to the Core, but directly within the loudspeaker Status/Control component of the running design. See the Controls section.

#### Model

*(For PL-DC**, PL-CA,* *and PL-SUB speakers only*): Offers a selection menu for choosing an alternative speaker model.

[Generic Loudspeakers](javascript:void(0))

**Note:** Consult the loudspeaker manufacturer to obtain limiter values for RMS Threshold, RMS Attack, RMS Release, Peak Voltage, Peak Attack, and Peak Release.

#### Band Count

The number of frequency bands available, from 1 to 8. If you are using Custom voicing, the band count of the loudspeaker and the Loudspeaker Custom Voicing Component must match.

#### RMS Threshold (V)

This limits the output RMS signal to below the specified voltage level, between 3 and 220 (default is 22).

#### RMS Attack (s)

This adjusts the time it takes for the output amplitude to fall once the RMS Threshold is exceeded, from 0.1 to 18 (default is 3.5).

#### RMS Release (s)

This adjusts the time it takes for the output to rise after dropping below the RMS Threshold, from 0.4 to 72 (default is 14).

#### Peak Voltage

This limits the output peak signal to below the specified voltage level, from 8 to 566 (default is 56.5).

#### Peak Attack (ms)

This adjusts the time it takes for the output amplitude to exceed the Peak Voltage, from 0.01 to 500 (default is 0.05).

#### Peak Release (ms)

This adjusts the time it takes â after the limiter has been engaged â for the peak output to stop limiting, from 1 to 10,000 (default is 2).

[AD-C, AD-S (except AD-S282H), Generic, and Generic 70V/100V Loudspeakers](javascript:void(0))

#### Contour

(Default): the âDefaultâ one has been voiced to provide an out-of-the-box optimum result.

#### High Pass Filter

(Shows for the AD-C8T-ZB and AD-C10T-HPZB) This setting allows you to change the crossover frequency of the loudspeaker when used in tandem with a subwoofer â No Sub, 80 Hz HP, or 100 Hz HP.

**Note:** In v10.0.1 and later, adjustment of High Pass Filter settings for the AD-C8T-SWZB, AD-C8T-ZB and AD-C10T-HPZB is no longer performed in Properties prior to saving to the Core, but directly within the loudspeaker Status/Control component of the running design. See the Controls section.

#### Low Pass Filter

(Shows for the AD-C8T-SWZB) This setting allows you to change the crossover frequency of the selected subwoofer â DEFAULT 180 Hz LP or 120 Hz LP. The DEFAULT setting is the standard crossover frequency, and it depends on the loudspeaker model.

#### Line Voltage

For Generic 70/100 V Speakers only, this sets the amplifier's gain to output the specified voltage when an input voltage is applied at input sensitivity â 100V or 70V (default).

#### Custom Voicing

The user-defined name of the [Loudspeaker Custom Voicing](loudspeaker_custom_voicing.htm) component that will be used with this loudspeaker (and others using the same voicing) to adjust the loudspeaker voicing. The text entered here must match the text in the Loudspeaker Custom Voicing component's Custom voicing Property. The number of bands in the Custom Voicing component and the loudspeaker must also match.

[Creating Multiple Generic Speakers with Custom Voicing](javascript:void(0))

To safely create multiple Generic Speaker Components when the loudspeakers are the same, and are using Loudspeaker Custom Voicing:

1. Add a single Generic Speaker to the Inventory and drag its component into the design.
2. Add a Loudspeaker Custom Voicing component to the Inventory and drag its component into the design.
3. Duplicate the Generic Speaker Component the desired number of times. This automatically adds Generic Speakers with default settings to the Inventory.
4. Select all of the Generic Speaker components you want to share the same Custom Voicing. Assign the Custom Voicing component to all of the Generic Loudspeakers at once. While you have all the Loudspeaker Status/Control components selected, you may also set the remainder of the loudspeaker properties that match.
5. Run or Emulate the Design and adjust the Loudspeaker Custom Voicing controls as required. All of the loudspeakers that have this Custom Voicing assigned to them are affected.

[Controls](javascript:void(0))

[Loudspeaker Status](javascript:void(0))

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### Input - Mute

Mutes the input to the loudspeaker. When this mute button is on, the associated channel in the DataPort component indicates muted.

#### Input - Gain (dB)

Sets the gain for the loudspeaker, from -100 to 20 (default is 0).

#### Delay (Architectural)

Architectural Delay is a single delay time that is applied equally to all bands of a loudspeaker component, from 0.001ms to 2.0s (default is 0). This allows you to time-align this loudspeaker component in relation to other loudspeakers components in the same architectural (or acoustic) space. The Architectural Delay variable ensures that the time alignment of the loudspeaker is consistent both when the source to the amp is via the Q-LAN network or via the analogue inputs when the amplifier is in Standalone mode. The Architectural Delay is also preserved when switching between DataPort enabled amplifiers using the DAB-801.

#### Meter Select

Selects the type of metering for all three meters, either RMS or Peak (default).

#### High Pass Filter

You can choose 80Hz, 100Hz, or 125Hz and âNo Subâ that allows the loudspeaker to work to its maximum LF extension. Note that on some of the smaller speakers such as PL-DC24, some of those choices are not available as the loudspeaker bandwidth does not allow it.

On PL-DC24 and PL-DC26, an âUnderbalconyâ choice at 300Hz is also available for situation where the LF part of the signal is provided by a Front of House system. The Underbalconny setting is not meant to be used with a corresponding subwoofer Low pass filter.

**Note:** In v10.0.1 and later, adjustment of High Pass Filter settings for the PL Series and AD-C8T-SWZB, AD-C8T-ZB and AD-C10T-HPZB is no longer performed in Properties prior to saving to the Core, but directly within the loudspeaker Status/Control component of the running design.

#### Monitor - Listen

This is a radio type button and is linked to all other Listen buttons in your design. When this button is engaged:

* the loudspeaker must have more than one band to have this button.
* any other Listen button in other loudspeakers that may be engaged is disengaged,
* all the bands in the selected loudspeaker have the Listen button engaged automatically
* the Listen buttons for the associated channels in the amplifier are engaged automatically,
* you can turn on and off any combination of the individual band Listen buttons in the loudspeaker.

When this button is not engaged, you can only select one band at a time. You must have the Loudspeaker Monitor component in the Schematic and properly connected to make use of the monitoring capability.

**Note:** The Monitor buttons are not linked in Emulate mode. Your design must be in Run mode for the functionality described above to operate.

[Inline Processing](javascript:void(0))

The Inline Processing property must be set to 'Yes' for these controls to appear. Available controls and options depend on the loudspeaker model.

#### Mute

Mutes the audio output of the speaker.

#### Invert

Inverts the polarity of the audio signal.

#### Gain

Adjusts the amplification or attenuation of the audio signal.

#### Delay

Applies a time delay to the audio signal.

#### User High Pass

This setting allows you to change the crossover frequency of the loudspeaker when used in tandem with a subwoofer â DEFAULT, 80 Hz HP, or 100 Hz HP. The DEFAULT setting is the standard crossover frequency, and it depends on the loudspeaker model.

#### User Low Pass

This setting allows you to change the crossover frequency of the selected subwoofer â DEFAULT, 100 Hz LP, 80 Hz LP, or 140 Hz LP. The DEFAULT setting is the standard crossover frequency, and it depends on the loudspeaker model.

[Band](javascript:void(0))

Depending on the loudspeaker, the Band count can be Full Range or multiple bands. Available controls and options depend on the loudspeaker model.

**Note:** When Q-SYS detects an amplifier attenuator at -20 dB (20 dB below full output) or below, Pilot Tones and Impedance readings are disabled. In addition, if Pilot Tones are enabled when the amplifier attenuator is turned to -20dB or below, the loudspeaker Status will indicate a compromised state.

#### Mute

Mutes the input to the loudspeaker. When this mute button is on, the associated channel in the DataPort amplifier component is muted.

#### Invert

When enabled, the amplifier output to the loudspeaker is inverted â i.e., the positive signal becomes negative and vice versa. This has no effect on the perceived sound. Enabling this control might be useful in special cases when two loudspeakers are playing the same audio at high output power. Inverting the output to one of the two loudspeakers balances the draw on the amplifierâs positive and negative power supplies so that a higher sustained output power is possible.

#### Open

LED indicating if the speaker circuit is open. On or Red = Open.

#### Short

LED indicating if the speaker circuit is shorted. On or Red = Short.

#### Threshold, Open (Ohms)

Sets impedance threshold (< 150, default is 100) for reporting open circuit faults. Open circuit detection can be disabled by setting a value greater than 150 Ohms.

#### Threshold, Short (Ohms)

Sets impedance threshold for reporting short circuit faults. Short circuit detection can be disabled by setting a value of 0 Ohms. The default is 1.

#### Impedance (Full)

Displays the average value of the loudspeaker impedance, in ohms, based on all the frequencies present in the program material. This information is not updated unless the signal is at a sufficient level.

#### Pilot Tone: Low Enable

Enables or disables the Low Pilot Tones.

#### Pilot Tone: Low Impedance

The impedance of the loudspeaker when the 20 Hz Pilot Tone is on.

#### Pilot Tone: High Enable

Enables or disables the High Pilot Tones.

#### Pilot Tone: High Impedance

The impedance of the loudspeaker when the 22 kHz Pilot Tone is on.

#### Voltage

Graphic display of the voltage in the speaker circuit. Based on the Meter Select, this can be Peak or RMS.

#### Current

Graphic display of the current in the speaker circuit. Based on the Meter Select, this can be Peak or RMS.

#### Power

Graphic display of the power in the speaker circuit. Based on the Meter Select, this can be Peak or RMS.

#### Limiter

Amount of attenuation applied to prevent damage to the loudspeaker. Graphic and text display of the amount of limiting, in dB, for the associated band.

#### High Pass Freq

For Generic 70/100 V Speakers, a high-pass filter is used for amplifier and transducer protection and cannot be disabled. The range is 30.0 Hz to 300.0 Hz (default is 50.0 Hz). Consult the speaker manufacturer to obtain the appropriate high-pass frequency value. Note that when this high-pass frequency value and the Custom Voicing high-pass filter value differ, Q-SYS uses the highest frequency of the two.

**WARNING:** To prevent transformer overheating and potential damage, you must consult the speaker manufacturer to obtain the appropriate high-pass frequency value.

#### Listen

Enables you to listen to the loudspeaker input for the associated band. This is a radio type button and is linked to all other Listen buttons in your design. When this is engaged, any other Listen button that may be on is disengaged. When engaged, the associated amplifier channel Listen button is automatically engaged. (The exception is when the master Listen button for this loudspeaker is on, you can listen to one, all, or any combination of bands in this loudspeaker.)

You must have the loudspeaker Monitor Component in the Schematic and properly connected to make use of the monitoring capability.

#### Gain (dB)

Controls the Monitor gain, from -100 to 20 (default is 0).

#### User High Pass

The User High Pass setting allows you to change the crossover frequency of the selected loudspeaker when used in tandem with a subwoofer â DEFAULT, 80 Hz HP, or 100 Hz HP. The DEFAULT setting is the standard crossover frequency, and it depends on the loudspeaker.

#### User Low Pass

The User Low Pass setting allows you to change the crossover frequency of the selected subwoofer â DEFAULT, 100 Hz LP, 80 Hz LP, or 140 Hz LP. The DEFAULT setting is the standard crossover frequency, and it depends on the loudspeaker.

[Control Pins](javascript:void(0))

### Status Control Pins

The following control pins are associated with the Status section of the Control Panel. Not all pins are available on all loudspeakers, or in all modes.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Gain (Input) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Monitor Listen | 0  1 | disable  enable | 0  1 | Input / Output |
| Mute (Input) | 0  1 | unmute  mute | 0  1 | Input / Output |
| Peak/RMS Select | 0  1 | Peak  RMS | 0  1 | Input / Output |
| Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |

### Band Control Pins

The following Control Pins are associated with the frequency bands. Each band has its own set of control pins.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Current | 0 to *n* | 0 A to *n* A | 0.000 to 1.00 | Output |
| High Pilot Impedance | 0 to *n* | 0 Ohms to *n* Ohms | 0.000 to 1.00 | Output |
| High Pilot Tone Enable | 0  1 | Disable  Enable | 0  1 | Input / Output |
| Impedance | 0 to *n* | 0 Ohms to *n* Ohms | 0.000 to 1.00 | Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Limiter Reduction | 0 to 60 | 0 dB to 60 dB | 0.000 to 1.00 | Output |
| Low Pilot Impedance | 0 to *n* | 0 Ohms to *n* Ohms | 0.000 to 1.00 | Output |
| Low Pilot Tone Enable | 0  1 | disable  enable | 0  1 | Input / Output |
| Monitor Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Monitor Listen | 0  1 | disable  enable | 0  1 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Narrowband Limiter Attenuation | (text) | | | Output |
| Narrowband Limiter Frequency | (text) | | | Input / Output |
| Open | 0  1 | false  true | 0  1 | Output |
| Open Threshold | 0 to 150 | 0W to 150W | 0.000 to 1.00 | Input / Output |
| Power | 0 to *n* | 0 W to *n* W | 0.000 to 1.00 | Output |
| Short | 0  1 | false  true | 0  1 | Output |
| Short Threshold | 0 to 150 | 0W to 150W | 0.000 to 1.00 | Input / Output |
| Gain (Input) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Voltage | 0 to *n* | 0 V  to *n* V | 0.000 to 1.00 | Output |
| Architectural Delay | 0.000 to 2.00 | 0 ms to 2.00 ms | 0.000 to 2.00 | Input / Output |
| **Line Arrays, AD-S Series (except AD-S28Tw), and AP Series** | | | | |
| Selectable Filter Profile | N / A | Default  80 Hz  100 Hz | N / A | Input / Output |
| **Line Array Subwoofers and AD-S28Tw** | | | | |
| Selectable Filter Profile | N / A | 80 Hz  100 Hz  125 Hz | N / A | Input / Output |

[Loudspeaker Reference](javascript:void(0))

### Intrinsic Correctionâ¢

Intrinsic Correction is an advanced and proprietary voicing algorithm that spatially averages more than a thousand measurements to achieve the ideal power response and phase correlation of the system. Protection filters are included to prevent excess of the systems mechanical and thermal limitations. This highly refined loudspeaker voicing is built into all powered loudspeaker systems. Passive loudspeakers may also obtain Intrinsic Correction via model-specific presets within Q-SYS and processing amplifiers.

### Loudspeakers - High-Z and PoE

[QLAN Network Loudspeakers](javascript:void(0))

| Name | Intrinsic Correction? | Configuration | Options |
| --- | --- | --- | --- |
| NL-SB42 | No | 2-way Network Soundbar | N/A |
| NL-C4 | No | Full-range, Low-profile Ceiling-mount Network Loudspeaker | N/A |
| NL-P4 | No | Full-range, Pendant-mount Network Loudspeaker | N/A |

[AcousticDesign â Ceiling Mount](javascript:void(0))

| Name | Intrinsic Correction? | Configuration | Options |
| --- | --- | --- | --- |
| AD-C.SUB | Yes | Sub 6" LF | 70/100V X-former/Low-Z |
| AD-C4T | Yes | 2-way 4.5" LF | 70/100V X-former/Low-Z |
| AD-C4T-LP | Yes | 2-way 4.5" LF low profile | 70/100V X-former/Low-Z |
| AD-C4T-LPZB | Yes | Zero bezel, 2-way 4.5" LF low profile | 70/100V X-former/Low-Z |
| AD-C4T-ZB | Yes | Zero bezel, 2-way 4.5" LF | 70/100V X-former/Low-Z |
| AD-C6T | Yes | 2-way 6.5" LF | 70/100V X-former/Low-Z |
| AD-C6T-HC | Yes | 2-way 6.5" High Ceiling Hi-Z/Low-Z | 70/100V X-former/Low-Z |
| AD-C6T-HP | Yes | 2-way 6.5" High Power Hi-Z/Low-Z | 70/100V X-former/Low-Z |
| AD-C6T-LP | Yes | 2-way 6.5" LF low profile | 70/100V X-former/Low-Z |
| AD-C6T-LPZB | Yes | Zero bezel, 2-way 6.5" LF low profile | 70/100V X-former/Low-Z |
| AD-C6T-ZB | Yes | Zero bezel, 2-way 6.5" LF | 70/100V X-former/Low-Z |
| AD-C8T-SWZB | Yes | Zero bezel, Sub 8" | 70/100V X-former/Low-Z |
| AD-C8T-ZB | Yes | Zero bezel, 2-way, 8" | 70/100V X-former/Low-Z |
| AD-C10T-HPZB | Yes | Zero bezel, 2-way, 10" | 70/100V X-former/Low-Z |
| AD-C820 | No | 2-way 8" LF | 70/100V X-former/Low-Z |
| AD-C821 | No | 2-way 8" LF | 70/100V X-former/Low-Z |
| AD-C1200 | No | 2-way 12" LF | 70/100V X-former/Low-Z |
| AD-C81Tw | No | Sub 8" LF | 70/100V X-former/Low-Z |

[AcousticDesign â Outdoor](javascript:void(0))

| Name | Intrinsic Correction? | Configuration | Options |
| --- | --- | --- | --- |
| AD-DWL.180 | Yes | Full Range 2-way w/180Â° coverage | 70/100V X-former/Low-Z |
| AD-DWL.360 | Yes | Full Range 2-way w/360Â° coverage | 70/100V X-former/Low-Z |
| AD-DWL.SUB | Yes | Sub w/Dual 5.25" | 70/100V X-former/Low-Z |

[AcousticDesign â Pendant Mount](javascript:void(0))

| Name | Intrinsic Correction? | Configuration | Options |
| --- | --- | --- | --- |
| AD-P.HALO | Yes | 2-way 6.5" omni | 70/100V X-former/Low-Z |
| AD-P.SUB | Yes | Sub 6" LF | 70/100V X-former/Low-Z |
| AD-P4T | Yes | 2-way 4.5" LF | 70/100V X-former/Low-Z |
| AD-P6T | Yes | 2-way 6.5" LF | 70/100V X-former/Low-Z |

[AcousticDesign â Surface Mount](javascript:void(0))

| Name | Intrinsic Correction? | Configuration | Options |
| --- | --- | --- | --- |
| AD-S.SAT | Yes | 2.75" FR | 70/100V X-former/Low-Z |
| AD-S.SUB | Yes | Sub 6" LF | 70/100V X-former/Low-Z |
| AD-S4T | Yes | 2-way 4" LF | 70/100V X-former/Low-Z |
| AD-S5T | Yes | 2-way 5.25" LF | 70/100V X-former/Low-Z |
| AD-S6 | Yes | 2-way 6.5" FR | Passive |
| AD-S6T | Yes | 2-way 6" LF | 70/100V X-former/Low-Z |
| AD-S8T | Yes | 2-way 8" LF | 70/100V X-former/Low-Z |
| AD-S10T | Yes | 2-way 10" LF | 70/100V X-former/Low-Z |
| AD-S12 | Yes | 2-way 12" LF | Passive |
| AD-S112sw | Yes | 12" direct-radiating subwoofer | Passive |
| AD-S162T | Yes | Column 16 x 2.5" | 70/100V X-former/Low-Z |
| AD-S402T | Yes | Column 4 x 2.5" | 70/100V X-former/Low-Z |
| AD-S802T | Yes | Column 8 x 2.5" | 70/100V X-former/Low-Z |

[AcousticCoverage â Ceiling Mount](javascript:void(0))

| Name | Intrinsic Correction? | Configuration | Options |
| --- | --- | --- | --- |
| AC-C2T | Yes | 2.75" Full Range | 70/100V X-former/Low-Z |
| AC-C2T-LP | Yes | 2.75" Full Range | 70/100V X-former/Low-Z |
| AC-C4T | Yes | 4" Full Range | 70/100V X-former/Low-Z |
| AC-C6T | Yes | 2-way 6" LF | 70/100V X-former/Low-Z |
| AC-C8T | Yes | 2-way 8" LF | 70/100V X-former/Low-Z |

[AcousticCoverage â Surface Mount](javascript:void(0))

| Name | Intrinsic Correction? | Configuration | Options |
| --- | --- | --- | --- |
| AC-S4T | Yes | 2-way 4" LF | 70/100V X-former/Low-Z |
| AC-S6T | Yes | 2-way 6" LF | 70/100V X-former/Low-Z |

### Loudspeakers - Performance

[AcousticPerformance](javascript:void(0))

| Name | Intrinsic Correction? | Configuration | Options |
| --- | --- | --- | --- |
| AP-212sw | Yes | Sub 2 x 12" | Passive |
| AP-4122m FOH | Yes | 2-way 12" LF Front of House | Passive |
| AP-4122m MON | Yes | 2-way 12" LF Monitor | Passive |
| AP-5102 | Yes | 2-way 10" LF | Passive / Bi-amp |
| AP-5122 | Yes | 2-way 12" LF | Passive / Bi-amp |
| AP-5122m FOH | Yes | 2-way 12" LF Front of House | Passive / Bi-amp |
| AP-5122m MON | Yes | 2-way 12" LF Monitor | Passive / Bi-amp |
| AP-5152 | Yes | 2-way 15" LF | Passive / Bi-amp |

[E Series](javascript:void(0))

| Name | Intrinsic Correction? | Configuration | Options |
| --- | --- | --- | --- |
| E110 | Yes | 2-way 10" LF | Passive |
| E112 | Yes | 2-way 12" LF | Passive |
| E115 | Yes | 2-way 15" LF | Passive |
| E118 | Yes | Sub 18" | Passive |
| E215 | Yes | 2-way 2x15" LF | Passive |

[PL-CA Coaxial](javascript:void(0))

| Name | Intrinsic Correction? | Configuration | Options |
| --- | --- | --- | --- |
| PL-CA5 | Yes | 2-way 5" | Passive |
| PL-CA6 | Yes | 2-way 6" | Passive |
| PL-CA8 | Yes | 2-way 8" | Passive / Bi-amp |
| PL-CA12 | Yes | 2-way 12" | Passive / Bi-amp |
| PL-CA15 | Yes | 2-way 15" | Passive / Bi-amp |

[PL-DC Directivity Control](javascript:void(0))

| Name | Intrinsic Correction? | Configuration | Options |
| --- | --- | --- | --- |
| PL-DC8 | Yes | 2-way 8" | Passive / Bi-amp |
| PL-DC12 | Yes | 2-way 12" | Passive / Bi-amp |
| PL-DC24 | Yes | 2-way 2x4" | Passive |
| PL-DC26 | Yes | 2-way 2x6" | Passive / Bi-amp |

[PL-SUB Subwoofers](javascript:void(0))

| Name | Intrinsic Correction? | Configuration | Options |
| --- | --- | --- | --- |
| PL-SUB10 | Yes | SUB 10" | Passive |
| PL-SUB12 | Yes | SUB 12" | Passive |
| PL-SUB15 | Yes | SUB 15" | Passive |
| PL-SUB18 | Yes | SUB 18" | Passive |

[Line Array](javascript:void(0))

| Name | Intrinsic Correction? | Configuration | Options |
| --- | --- | --- | --- |
| ILA (WL2082-i) | Yes | 2-way / 3-way 8" x 2 LF | Bi -amp / Tri-amp |
| WideLine-10 (WL2102-w) | Yes | 2-way / 3-way 10" x 2 LF | Bi -amp / Tri-amp |
| WideLine-8  (WL3082) | Yes | 2-way 8" x 2 LF | Tri-amp |
| PL-LA8 | Yes | 2-way 8" line array | Passive / Bi-amp |
| PL-LA12 | Yes | 2-way 12" line array | Passive / Bi-amp |

[Subwoofers](javascript:void(0))

| Name | Intrinsic Correction? | Configuration | Options |
| --- | --- | --- | --- |
| WL118-sw | Yes | Sub 18" LF | Passive |
| WL212-sw | Yes | Sub 12" x 2 LF | Passive |
| WL218-sw | Yes | Sub 18" x 2 LF | Passive |
| GP212-sw | Yes | Sub 12" x 2 LF | Passive |
| GP218-sw | Yes | Sub 18" x 2 LF | Passive |

### Loudspeakers - Cinema

[Cinema Screen](javascript:void(0))

| Name | Intrinsic Correction? | Configuration | Options |
| --- | --- | --- | --- |
| RMS | Yes | 4-way speaker system RSC-112 & RSB-212 | Quad-amp |
| SC-222 | Yes | 2-way 2 x 15 | Bi-amp |
| SC-222X | Yes | 2-way 2 x 15 LF Passive | Passive |
| SC-223 | Yes | 3-way 15" x 2 LF | Bi-amp |
| SC-223X | Yes | 3-way 15" x 2 LF | Passive / Bi-amp |
| SC-412C | Yes | 2-way 1 x 15 | Bi-amp |
| SC-413C | Yes | 3-way 15" LF | Bi-amp / Tri-amp |
| SC-414 | Yes | 4-way 15" x 1 LF | Tri-amp / Quad-amp |
| SC-422C | Yes | 2-way 2 x 15 LF | Bi-amp |
| SC-423C | Yes | 3-way 15" x 2 LF | Bi-amp / Tri-amp |
| SC-423CF | Yes |  | Bi-amp / Tri-amp |
| SC-424 | Yes | 4-way 15" x 2 LF | Tri-amp / Quad-amp |
| SC-424-8F | Yes |  | Tri-amp / Quad-amp |
| SC-433C | Yes | 3-way 15" x LF | Bi-amp / Tri-amp |
| SC-434 | Yes | 4-way 15" x 3 LF | Tri-amp / Quad-amp |
| SC-443C | Yes | 3-way 15" x 4 LF | Bi-amp / Tri-amp |
| SC-444 | Yes | 4-way 15" x 4 LF | Tri-amp / Quad-amp |
| SC-1120 | Yes | 2-way 12" LF | Passive |
| SC-1150 | Yes | 2-way 15" LF | Passive |
| SC-2150 | Yes | 3-way 15" x 2 LF | Passive / Bi-amp |

[Cinema Surround](javascript:void(0))

| Name | Intrinsic Correction? | Configuration | Options |
| --- | --- | --- | --- |
| SR-800 | Yes | 2-way 8" LF | Passive |
| SR-1000 | Yes | 2-way 10" LF | Passive |
| SR-1020 | Yes | 2-way 10" LF | Passive |
| SR-1030 | Yes | 2-way 10" LF | Passive |
| SR-1290 | Yes | 2-way 12" LF | Passive |
| SR-1590 | Yes | 2-way coax 15" LF | Passive |
| SR-5152 | Yes | 2-way 15" LF | Passive / Bi-amp |
| SR-8101 | Yes | 2-way 8" LF | Passive |
| SR-8200 | Yes | 2-way 8" LF | Passive |

[Cinema Subwoofer](javascript:void(0))

| Name | Intrinsic Correction? | Configuration | Options |
| --- | --- | --- | --- |
| GP118Cine-sw | No | Sub 18" LF | Passive |
| GP218Cine-sw | No |  | Passive |
| RSB-212 | Yes | Standalone RSB-212 subwoofer | Passive |
| SB-118F | Yes | Sub 18" | Passive |
| SB-218F | Yes | Sub 18" | Passive |
| SB-1180 | No |  | Passive |
| SB-2180 | No |  | Passive |
| SB-7118 | No |  | Passive |
| SB-7218 | No |  | Passive |
| SB-15121 | No |  | Passive |

### Loudspeakers - Custom

[Custom](javascript:void(0))

| Name | Intrinsic Correction? | Configuration | Options |
| --- | --- | --- | --- |
| [Loudspeakers](loudspeaker_generic_low_impedance.htm) | User-defined low impedance (16, 8, or 4â¦) loudspeaker. | | |
| [Loudspeakers](loudspeaker_generic_high_impedance.htm) | User-defined high impedance (with transformer) loudspeaker. | | |
| [Custom Voicing](loudspeaker_custom_voicing.htm) | Virtual, user-defined DataPort-based processing for loudspeakers. | | |
