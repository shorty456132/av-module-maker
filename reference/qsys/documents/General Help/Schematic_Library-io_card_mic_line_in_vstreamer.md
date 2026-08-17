# Mic/Line In (NV-32-H)

> Source: https://help.qsys.com/Content/Schematic_Library/io_card_mic_line_in_vstreamer.htm

# Mic/Line In (NV-32-H)

The NV-32-H includes a 3.5mm phone-style (round) Audio In jack for connecting stereo analog audio sources â such as a microphone or computer Line Out (or headphone) audio â for conversion to a digital signal that can then be routed and processed by Q-SYS.

Use the Mic/Line In component to configure both the incoming source analog signal and the outgoing digital signal to Q-SYS.

[Inputs and Outputs](javascript:void(0))

The Mic/Line In component represents the AUDIO IN jack on the rear of the NV-32-H.

### Input Pins

This component has no input pins.

### Output Pins

#### Channel 1, 2

Each pin represents one channel of stereo audio that you can route to other Q-SYS audio components:

* Channel 1: Left side audio.
* Channel 2: Right side audio.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

### Analog

#### Peak Input Level (dBFS)

The peak level of the input signal for each channel, from -120 to 20 dBFS. The measurement is taken after the A/D converter, but before the Digital Gain.

#### Clip

LED indicates if the incoming signal is being clipped.

#### Clip Hold

Click to hold the clip indication until you manually clear it.

#### Mic Bias Voltage

If your connected condenser microphone requires it, click to apply mic bias voltage (2.8V DC) to the analog audio channels. This control is similar to Phantom Power, but provides less voltage. Note that this control is linked to both audio channels.

#### Preamp Sensitivity

Set the incoming maximum analog level that can be converted without clipping, from -38 to +22 dBu (default is +22). You typically set this level slightly higher than the source's output level so that the Peak Input Level reads approximately 0 dBFS with no clipping.

This value varies inversely with Preamp Gain.

#### Preamp Gain

Select the amount of gain to apply to the incoming analog signal level, from 0 to 60 dB (default is 0).

### Digital

#### Invert

Click to invert the polarity of the digital audio signal output to Q-SYS.

#### Mute

Click to mute the digital audio signal output to Q-SYS.

#### Gain

Click to adjust the gain of the audio signal output to Q-SYS, from -100 dB to 20 dB (default is 0).

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
| Level (dBFS) | -120 to 20 | -120dB to 20dB | 0.000 to 1.00 | Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Mic Bias Voltage | 0  1 | disable  enable | 0  1 | Input / Output |
| Preamp Gain | 0 to 60 | 0dB to 60dB | 0.000 to 1.00 | Input / Output |
| Preamp Sensitivity | -38 to 22 | -38dBu to +22dBu | 0.000 to 1.00 | Input / Output |
