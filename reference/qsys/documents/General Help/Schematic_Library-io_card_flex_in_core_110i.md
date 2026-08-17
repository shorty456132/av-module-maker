# Flex In (Core 110f, 110c)

> Source: https://help.qsys.com/Content/Schematic_Library/io_card_flex_in_core_110i.htm

# Flex In (Core 110f, 110c)

The Flex Channel feature on Core 110 Series processors provides eight audio channels that can be individually switched between line inputs and line outputs. The Flex Input Component provides the control and selection of the line-level outputs on the Core. The Flex Input component converts the analog signal to digital and provides software controls before and after the convertor. Connections to a single channel are made using a three-terminal 3.5mm Euro style connector.

**Note:** The Flex Input and Output components are not for use with QSC DataPort amplifiers.

[Inputs and Outputs](javascript:void(0))

### Inputs

This component has no inputs available for this component.

### Outputs

#### Channels 1-8

By default, the Flex In component offers 8 Audio Outputs represented by a  circle, and traditional wiring is represented by a thin black line.

[Properties](javascript:void(0))

There are no adjustable properties for the **Flex Input** component aside from what appears the Core [Properties](core_status.htm#Properties).

[Controls](javascript:void(0))

### Input / Output Tab

#### Flex I/O

#### Input (Enable)

Changes the associated channel to a Flex Input channel.

To switch back to a Flex Output channel, you must enable the channel in the Output Component.

#### Mic Detection

#### Enable (Yellow LED)

When the LED is on, the associated channel has Mic Detection enabled. When the LED is off, Mic Detection is disabled.

#### Good (Green LED)

When the LED is green, the mic impedance is within the set thresholds. If the thresholds are exceeded, the green LED is off.

#### Analog

#### Peak Input Level (dB)

Meters for each channel indicating the peak analog input level. The measurement is taken after the A/D converter, but before the Digital Gain. Use this meter in conjunction with the Max Input Level to obtain an input signal as close to 0 dBFS as possible without actually clipping.

#### Clip

Red LED indicating if the signal is being clipped.

#### Clip Hold

Holds the clip indication until manually cleared.

#### Phantom Power

Toggle turning on and off phantom power (+48VDC) to the microphone.

#### Preamp Sensitivity (dBu)

The maximum analog level, coming into the Flex Input component, that can be converted without clipping. This level is typically set slightly higher than the source's output level, so that the Peak Input Level reads about 0 dBFS without actually clipping.

Varies inversely with the Preamp Gain.

#### Preamp Gain (dB)

The amount of Gain applied to the incoming analog signal level.

Varies inversely with the Preamp Sensitivity.

#### Digital

#### Invert

Toggle button to invert the digital output of the Flex Input component.

#### Mute

Mutes the output signal.

#### Gain (dB)

Controls the Gain of the digital output signal.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

### Mic Detection Tab

#### Detection

#### Enable (Toggle Button)

Enables or disables Mic Detection for the associated channel. When Mic Detection is on, the impedance of the mic is measured against the set thresholds.

#### Good (Green LED)

When the LED is green, the mic impedance is within the set thresholds. If the thresholds are exceeded, the green LED is off.

#### Impedance

The measured impedance of the attached microphone.

#### Set Thresholds (Trigger Button)

Sets the high and low thresholds based on the mic impedance at the time the button is pushed.

[Control Pins](javascript:void(0))

Each channel on the Flex Input component has the following Control Pins with the exception of Status.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Digital Level | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Flex Input Enable | 1  0 | enabled  disabled | 1  0 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Mic Detection Enable  (button) | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Mic Detection Enabled  (LED) | 0  1 | no  yes | 0  1 | Output |
| Mic Detection Good | 0  1 | no  yes | 0  1 | Output |
| Mic Detection High Impedance Threshold | 0 to >100001 | --- to >100kÎ© | 0 to 1.00 | Input / Output |
| Mic Detection Impedance |  |  |  | Output |
| Mic Detection low Impedance Threshold | 0 to >100001 | --- to >100kÎ© | 0 to 1.00 | Input / Output |
| Mic Detection Set Thresholds | Trigger | | | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Phantom Power | 0  1 | disable  enable | 0  1 | Input / Output |
| Preamp Gain | 0 to 60 | 0dB to 60dB | 0 to 1.00 | Input / Output |
| Preamp Sensitivity | 21 to -39 | +21dBu to -39dBu | 1.00 to 0 | Input / Output |
| Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
