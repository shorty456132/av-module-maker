# Line Out (NV-32-H)

> Source: https://help.qsys.com/Content/Schematic_Library/io_card_line_out_vstreamer.htm

# Line Out (NV-32-H)

The NV-32-H includes a 3.5mm phone-style (round) Audio Out jack for connection of stereo audio equipment, such as a computer's Line In jack. The Line Out component converts the processed digital signal from Q-SYS to analog audio.

Use the Line Out component to configure both the source digital signal from Q-SYS and the outgoing analog signal to connected equipment.

[Inputs and Outputs](javascript:void(0))

The Line Out component represents the AUDIO OUT jack on the rear of the NV-32-H.

### Input Pins

#### Channel 1, 2

Each pin represents one channel of stereo audio to send from Q-SYS to connected analog equipment:

* Channel 1: Left side audio.
* Channel 2: Right side audio.

### Output Pins

This component has no output pins.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

### Analog

#### Peak Output Level (dBu)

The peak audio level to the output device, from -120 to 24 dBu.

#### Output Mute

Click to mute the output after the D-A converter and before the output to the device.

#### Max RMS Output Level

Set the analog RMS output level after the D/A converter, from -60 to +4 dBu (default is +4). To avoid clipping the signal of a power amplifier, you typically set this level slightly lower than the destination's sensitivity or maximum input level.

This level varies in direct proportion with Output Gain.

#### Output Gain

Adjust the amount of gain applied to the outgoing analog signal, from -64 to 0 dB (default is 0).

This level varies in direct proportion with Max RMS Output Level.

### Digital

#### Peak Output Level (dBFS)

Measurement of the digital signal level prior to the D/A converter, from -120 to 43 dB.

* Green = good
* Yellow = close to clipping
* Red = clipping

#### Clip

LED indicates if the incoming signal is being clipped.

#### Clip Hold

Click to hold the clip indication until you manually clear it.

#### Invert

Click to invert the polarity of the incoming digital audio signal from Q-SYS.

#### Mute

Click to mute the incoming digital audio signal from Q-SYS.

#### Gain

Click to adjust the gain of the audio signal from Q-SYS, from -100 dB to 20 dB (default is 0).

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
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Channel 1, 2 | | | | |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Gain | -100 to 20 | -100dB to 20dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Level (dBFS) | -120 to 43 | -120dB to 43dB | 0.000 to 1.00 | Output |
| Level (dBu) | -120 to 24 | -120dB to 24dB | 0.000 to 1.00 | Output |
| Max Level | -60 to 4 | -60dBu to +4dBu | 0 to .988 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Output Gain | -64 to 0 | -64dB to 0dB | 0.000 to 1.00 | Input / Output |
| Output Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
