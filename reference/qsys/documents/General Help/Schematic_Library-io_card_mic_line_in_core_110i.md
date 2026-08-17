# Mic/Line In (Core 110f, 110c)

> Source: https://help.qsys.com/Content/Schematic_Library/io_card_mic_line_in_core_110i.htm

# Mic/Line In (Core 110f, 110c)

The Mic/Line In Core provides eight line-level input for devices with line-level outputs, and inputs for microphones. It is an integral part of the Core 110 Series. The Line Input converts the analog input signal to a processed digital and provides software controls before and after the convertor. Connections are made using eight three-terminal 3.5mm Euro style connectors.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

### Analog

#### Peak Input Level (dBFS)

Meters for each channel indicating the peak analog input level. The measurement is taken after the A/D converter, but before the Digital Gain. Use this meter in conjunction with the Max Input Level to obtain an input signal as close to 0 dBFS as possible without actually clipping.

#### Clip

Red LED indicating if the signal is being clipped.

#### Clip Hold

Holds the clip indication until manually cleared.

#### Phantom Power

Toggle turning on and off phantom power (+48VDC) to the microphone.

#### Preamp Sensitivity (dBu)

The maximum analog level, coming into the Mic/Line Input card, that can be converted without clipping. This level is typically set slightly higher than the source's output level, so that the Peak Input Level reads about 0 dBFS without actually clipping.

You can select the field and enter the value you want, or click and drag the number to the value.

Varies inversely with the Preamp Gain.

#### Preamp Gain

The amount of Gain applied to the incoming analog signal level.

Varies inversely with the Preamp Sensitivity.

### Digital

#### Invert

Toggle button to invert the digital output of the Mic/Line input card.

#### Mute

Mutes the output signal.

#### Gain (dB)

Controls the Gain of the digital output signal.

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

The available **Control Pins** depend on settings in **Properties**. Each channel on the Mic/Line In has the following Control Pins with the exception of Status which covers all channels.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Digital Level | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Digital Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Phantom Power | 0  1 | disable  enable | 0  1 | Input / Output |
| Preamp Gain  (dB) | 0 to 60 | 0dB to 60dB | 0.000 to 1.00 | Input / Output |
| Preamp Sensitivity  (dBu) | +21 to -39 | +21dBu to -39dBu | 0.000 to 1.00 | Input / Output |
| Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
