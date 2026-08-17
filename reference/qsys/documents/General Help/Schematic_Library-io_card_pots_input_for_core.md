# POTS In

> Source: https://help.qsys.com/Content/Schematic_Library/io_card_pots_input_for_core.htm

# POTS In

The POTS In component receives the incoming audio from a telephone call, converts the analog signal to digital, and monitors and modifies the audio using the controls listed below.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

[Line](javascript:void(0))

#### Peak Input Level (dBFS)

Measures the analog input signal.

#### Clip

Red LED indicating if the signal is being clipped.

#### Clip Hold

Holds the clip indication until manually cleared by pressing this button to the Off position.

[Digital](javascript:void(0))

#### Invert

Toggle button to invert the digital output of the POTS In.

#### Mute

Mutes the output signal.

#### Gain (dB)

Controls the Gain of the digital output signal.

[Status](javascript:void(0))

#### Status LED

This LED changes color to indicate the current status of the Core. See Status for the meanings of the various colors.

#### Status

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
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Status | Text | | | Output |
