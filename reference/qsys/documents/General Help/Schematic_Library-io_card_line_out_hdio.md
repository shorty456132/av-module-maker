# Line Out (QIO Series)

> Source: https://help.qsys.com/Content/Schematic_Library/io_card_line_out_hdio.htm

# Line Out (QIO Series)

Use the Line Out component to convert digital audio from your Q-SYS design to analog audio for playback on a device wired to the Line Outputs of a QIO peripheral. For [Q-SYS Products](../Hardware/Hardware_Overview.htm#QIO) that include Line Outputs, the Line Out component is available within the device's Inventory tree. You can configure audio parameters both before and after the digital-to-analog converter.

[Inputs and Outputs](javascript:void(0))

### Input Pins

#### Output 1-24

For each Output Channel supported by the QIO device, this pin receives audio from another Q-SYS audio component for output to a connected analog audio device.

### Output Pins

This component has no output pins.

[Schematic Example](javascript:void(0))

In this example, analog audio connected to the line inputs of a QIO-ML2x2 (perhaps from a pair of media players) is equalized and mixed with audio from an Audio Player component. The mixed audio is then sent to the ML2x2's line outputs for playback â for example, to a connected QSC SPA Series amplifier wired to QSC AcousticDesign loudspeakers.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

### Analog

#### Peak Output Level (dBu)

Measures the peak output level to the output device, from -120 to 27 dB.

#### Output Mute

Mutes the output after the D-A converter and before the output.

#### Max RMS Output Level

Controls the maximum analog RMS output level after the D/A converter, from -37 to +24 (default is +24). This level is typically set slightly lower than the destination's sensitivity or maximum input level in order to avoid clipping the signal of a power amplifier. Varies in direct proportion with Output Gain.

#### Output Gain

The amount of gain applied to the outgoing analog signal, from -61 to 0 dB (default is 0). Varies in direct proportion with the Max RMS Output Level.

### Digital

#### Peak Output Level (dBFS)

Measures the digital signal level prior to the D/A converter.

#### Clip

Red LED indicates if the incoming signal is being clipped.

#### Clip Hold

Holds the clip indication until manually cleared.

#### Invert

Inverts the polarity of the audio signal.

#### Mute

Mutes the incoming digital audio signal.

#### Gain

Controls the gain of the digital audio signal prior to the D/A converter, from -100 to 20 dB (default is 0).

### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Channel *n* | | | | |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Level (dBFS) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Level (dBu) | -120 to 27 | -120 dB to 27 dB | 0.000 to 1.00 | Output |
| Max Level | -37 to 24 | -37 dBu to 24 dBu | 0.000 to 1.00 | Input / Output |
| Mute | 0  1 | false  true | 0  1 | Input / Output |
| Output Gain | -61 to 0 | -61 dB to 0 dB | 0.000 to 1.00 | Input / Output |
| Output Mute | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
