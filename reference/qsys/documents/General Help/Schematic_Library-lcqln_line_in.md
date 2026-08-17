# Mic/Line In (QIO Series)

> Source: https://help.qsys.com/Content/Schematic_Library/lcqln_line_in.htm

# Mic/Line In (QIO Series)

Use the Mic/Line In component to convert analog line-level audio to digital and then route it within your Q-SYS design. For [Q-SYS Products](../Hardware/Hardware_Overview.htm#QIO) that include audio inputs, the Mic/Line In component is available within the device's Inventory tree. You can configure audio parameters both before and after the analog-to-digital converter. And, if a microphone is connected to the QIO Series device, you can optionally toggle Mic Detection.

[Inputs and Outputs](javascript:void(0))

### Input Pins

This component has no input pins.

### Output Pins

#### Input 1-24

For each Input Channel supported by the QIO device, this pin sends audio from the connected source (such as a media player or microphone) to the input pins of another Q-SYS component.

[Schematic Example](javascript:void(0))

In this example, audio from an analog device (or perhaps two different devices) connected to a QIO-ML2x2 peripheral's two Mic/Line Input channels is routed to two pairs of [Q-SYS Products](../Hardware/Hardware_Overview.htm#NL).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

[Inputs](javascript:void(0))

### Mic Detection

#### Enabled

When the yellow LED is on, the associated channel has Mic Detection enabled. When the LED is off, Mic Detection is disabled.

#### Good

When the green LED is on, the mic impedance is within the set thresholds. If the thresholds are exceeded, the LED is off.

### Analog

#### Peak Input Level (dBFS)

Meters for each channel indicating the peak analog input level, from -120 to 20 dBFS.The measurement is taken after the A/D converter, but before the Digital Gain.

#### Clip

Red LED indicating if the signal is being clipped.

#### Clip Hold

Holds the clip indication until manually cleared.

#### Phantom Power

Toggle turning on and off phantom power (+48VDC) to the microphone.

#### Preamp Sensitivity

The maximum analog level coming into the Mic/Line In component that can be converted without clipping, from +24 to -36 dBu (default is +24). This level is typically set slightly higher than the source's output level, so that the Peak Input Level reads about 0 dBFS without actually clipping. Varies inversely with the Preamp Gain.

#### Preamp Gain

The amount of Gain applied to the incoming analog signal level, from 0 to 60 dB (default is 0). Varies inversely with the Preamp Sensitivity.

### Digital

#### Invert

Toggle button to invert the digital output of the Mic/Line In component.

#### Mute

Mutes the output signal.

#### Gain

Controls the Gain of the digital output signal, from -100 to 20 dB (default is 0).

### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

[Mic Detection](javascript:void(0))

### Detection

#### Enable

Enables or disables Mic Detection for the associated channel. When Mic Detection is on, the impedance of the mic is measured against the set thresholds.

#### Good

When the LED is green, the mic impedance is within the set thresholds. If the thresholds are exceeded, the green LED is off.

#### Impedance

The measured impedance of the attached microphone.

#### Set Thresholds

Click to sets the high and low thresholds based on the mic impedance at the time the button is pushed.

### Thresholds

#### High Impedance

Manually adjust the mic detection high impedance threshold for each channel, from none to >100kÎ© (default is none).

#### Low Impedance

Manually adjust the mic detection low impedance threshold for each channel, from none to >100kÎ© (default is none).

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Channel *n* | | | | |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Level (dBFS) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Mic Detection Enable (button) | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Mic Detection Enabled (LED) | 0  1 | no  yes | 0  1 | Output |
| Mic Detection Good | 0  1 | no  yes | 0  1 | Output |
| Mic Detection High Impedance Threshold | 0 to >100001 | --- to >100kÎ© | 0 to 1.00 | Input / Output |
| Mic Detection Impedance |  |  |  | Output |
| Mic Detection Low Impedance Threshold | 0 to >100001 | --- to >100kÎ© | 0 to 1.00 | Input / Output |
| Mic Detection Set Thresholds | Trigger | | | Input / Output |
| Mute | 0  1 | false  true | 0  1 | Input / Output |
| Phantom Power | 0  1 | false  true | 0  1 | Input / Output |
| Preamp Gain | 0 to 60 | 0dB to 60dB | 0 to 1.00 | Input / Output |
| Preamp Sensitivity | -36 to +24 | -36dBu to +24dBu | 1.00 to 0 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
