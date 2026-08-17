# POTS Out

> Source: https://help.qsys.com/Content/Schematic_Library/io_card_pots_output_for_core.htm

# POTS Out

The POTS Out component converts the processed digital signal to analog and provides software controls before and after the convertor. The output is sent to the POTS telephone system servicing the call.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

[Line](javascript:void(0))

#### Peak Line Level (dBm @600Î©)

Measures Peak Output level to the RJ11 output.

[Digital](javascript:void(0))

#### Peak Output Level (dBFS)

Measures the Digital Signal level prior to the D/A converter.

#### Clip

Red LED indicating if the signal is being clipped.

#### Clip Hold

Holds the clip indication until manually cleared.

#### Invert

Inverts the audio signal.

#### Mute

Mutes the digital audio signal.

**Note:** Note: Dialing is enabled regardless of the Mute state.

#### Gain

Controls the gain of the digital audio signal prior to the D/A converter.

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
| Peak Line Level (dBm @ 600Î©) | -120 to 27 | -120 dB to 27 dB | 0.000 to 1.00 | Output |
| Status | Text | | | Output |
