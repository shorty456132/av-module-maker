# Flex In (I/O-Core 8 Flex)

> Source: https://help.qsys.com/Content/Schematic_Library/io_card_flex_in_io_core_8_flex.htm

# Flex In (I/O-Core 8 Flex)

The [Core 8 Flex](../Hardware/Processing/Core_8_Flex.htm) provides eight audio channels that can be individually switched between mic/line inputs and line outputs. The Flex Input component provides the control and selection of the mic/line-level inputs on the Core 8 Flex. The Flex Input component converts the analog signal to digital and provides software controls before and after the convertor. Connections to a single channel are made using a three-terminal 3.5mm Euro style connector.

**Note:** The Flex Input and Output components are not for use with QSC DataPort amplifiers.

[Properties](javascript:void(0))

Flex In has no configurable properties. For a list of properties applicable to the Core 8 Flex in general, see:

* Core Mode: [Status (Core)](core_status.htm)
* Peripheral Mode: [Status (I/O-Core 8 Flex)](io_core_8_flex_status.htm)

[Controls](javascript:void(0))

### Input / Output

#### Channel *n* Flex Input Enable

Changes the associated channel to a Flex Input channel. To switch back to a Flex Output channel, you must enable the channel in the Output component.

#### Channel *n* Mic Detection Enabled

When the yellow LED is on, the associated channel has Mic Detection enabled. When the LED is off, Mic Detection is disabled.

#### Channel *n* Mic Detection Good

When the green LED is on, the mic impedance is within the set thresholds. If the thresholds are exceeded, the LED is off.

#### Channel *n* Level (dBFS)

Meters for each channel indicating the peak analog input level, from -120 to 20 dBFS.The measurement is taken after the A/D converter, but before the Digital Gain. Use this meter in conjunction with the Max Input Level to obtain an input signal as close to 0 dBFS as possible without actually clipping.

#### Channel *n* Clip

Red LED indicating if the signal is being clipped.

#### Channel *n* Clip Hold

Holds the clip indication until manually cleared.

#### Channel *n* Phantom Power

Toggle turning on and off phantom power (+48VDC) to the microphone.

#### Channel *n* Preamp Sensitivity

The maximum analog level coming into the Flex In component that can be converted without clipping, from +24 to -40 dBu (default is +24). This level is typically set slightly higher than the source's output level, so that the Peak Input Level reads about 0 dBFS without actually clipping. Varies inversely with the Preamp Gain.

#### Channel *n* Preamp Gain

The amount of Gain applied to the incoming analog signal level, from 0 to 64 dB (default is 0). Varies inversely with the Preamp Sensitivity.

#### Channel *n* Invert

Toggle button to invert the digital output of the Flex In component.

#### Channel *n* Mute

Mutes the output signal.

#### Channel *n* Gain

Controls the Gain of the digital output signal, from -100 to 20 dB (default is 0).

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

### Mic Detection

#### Channel n Mic Detection Enable

Enables or disables Mic Detection for the associated channel. When Mic Detection is on, the impedance of the mic is measured against the set thresholds.

#### Channel n Mic Detection Good

When the LED is green, the mic impedance is within the set thresholds. If the thresholds are exceeded, the green LED is off.

#### Channel n Mic Detection Impedance

The measured impedance of the attached microphone.

#### Channel n Mic Detection Set Thresholds

Sets the high and low thresholds based on the mic impedance at the time the button is pushed.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Channel *n* | | | | |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Flex Input Enable | 1  0 | enabled  disabled | 1  0 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Level (dBFS) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Mic Detection Enable (button) | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Mic Detection Enabled (LED) | 0  1 | no  yes | 0  1 | Output |
| Mic Detection Good | 0  1 | no  yes | 0  1 | Output |
| Mic Detection High Impedance Threshold | 0 to >100001 | --- to >100kÎ© | 0 to 1.00 | Input / Output |
| Mic Detection Impedance |  |  |  | Output |
| Mic Detection low Impedance Threshold | 0 to >100001 | --- to >100kÎ© | 0 to 1.00 | Input / Output |
| Mic Detection Set Thresholds | Trigger | | | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Phantom Power | 0  1 | disable  enable | 0  1 | Input / Output |
| Preamp Gain | 0 to 64 | 0dB to 64dB | 0 to 1.00 | Input / Output |
| Preamp Sensitivity | -40 to +24 | -40dBu to +24dBu | 1.00 to 0 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
