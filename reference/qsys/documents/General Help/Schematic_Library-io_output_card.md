# Line Out (I/O Card)

> Source: https://help.qsys.com/Content/Schematic_Library/io_output_card.htm

# Line Out (I/O Card)

The Line Out card provides line-level output for devices other than QSC DataPort amplifiers. It is typically installed in an I/O Frame, but can be installed in the Core. The Line Out card converts the processed digital signal to analog and provides software controls before and after the convertor. Connections are made using four three-terminal Euro style connectors.

For hardware information, see [COL4 â Analog Line Output Card](../Hardware/IO_Expanders/COL4.htm).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

Each control listed in the Analog and Digital sections, are one per channel.

### Line

#### Peak Output Level (dBu)

Measures Peak Output level to the output device

#### Relay Mute

Mutes the output after the D-A converter and before the output.

#### Max RMS Output Level (dBu)

Controls the analog RMS output level after the D/A converter. This level is typically set slightly lower than the destination's sensitivity or maximum input level in order to avoid clipping the signal of a power amplifier. Varies in direct proportion with Output Gain.

#### Output Gain (dB)

The amount of gain applied to the outgoing analog signal. Varies in direct proportion with the Max RMS Output Level.

### Digital

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

#### Gain

Controls the gain of the digital audio signal prior to the D/A converter.

### Status

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
| Analog Level  (Peak Output Level (dBu)) meter | -120 to 27 | -120dB to 27dB | 0.000 to 1.00 | Output |
| Clip (LED) | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Digital Level (Peak Output Level (dBFS)) meter | -120 to 43 | -120dB to 43dB | 0.000 to 1.00 | Output |
| Gain | -100 to 20 | -100dB to 20dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Max Level | -40 to 21 | -40.0dBu to +21dBu | 0 to .988 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Output Gain | -31 to 0 | -31 dB to 0 dB | 0.000 to 1.00 | Input / Output |
| Relay Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
