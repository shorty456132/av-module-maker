# Active Matrix Surround Decoder

> Source: https://help.qsys.com/Content/Schematic_Library/active_matrix_surround_decoder.htm

# Active Matrix Surround Decoder

Use the Active Matrix Surround Decoder to create a 4 channel output with Center and Surround for use with Lt / Rt encoded stereo surround content.

[Schematic Example](javascript:void(0))

In this example, an Active Matrix Surround Decoder is outputting the Lt / Rt / Center / Surround channels into the Amplifiers.

**Tip:** From top to bottom, the Active Matrix Surround Decoder reads: Left, Right, Center, Surround.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### Processing

**Bypass**  When engaged, the processing of the Active Matrix Surround Decoder is bypassed.

#### Autobalance

**Enable** When enabled, the sound will be autobalanced .

**Current Balance** This field is not definable; instead, it is meant to inform you the Center Channel is being balanced depending on the input level of the Lt and Rt inputs.

#### Surround

**7 kHz LPF** When enabled, the Low-Pass Filter amplifies frequencies below 7 kHz and attenuates the frequencies above that set frequency.

**Modified B-Type NR** When enabled, Noise Reduction will be provided.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Autobalance Enable | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Autobalance Level | N/A | text - lists C as Center Channel is balanced | N/A | Output |
| Bypass All Processing | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Status | N / A | text - lists status of decoder | N / A | Output |
| Surround B-Type NR Enable | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Surround LPF Enable | 0  1 | disabled  enabled | 0  1 | Input / Output |
