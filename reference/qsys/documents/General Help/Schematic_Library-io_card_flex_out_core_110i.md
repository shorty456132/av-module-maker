# Flex Out (Core 110f, 110c)

> Source: https://help.qsys.com/Content/Schematic_Library/io_card_flex_out_core_110i.htm

# Flex Out (Core 110f, 110c)

The Flex Channel feature on Core 110 Series processors provides eight audio channels that can be individually switched between line inputs and line outputs. The Flex Output Component provides the control and selection of the line-level outputs on the Core. The Flex Output component converts the processed digital signal to analog and provides software controls before and after the convertor. Connections are made using three-terminal 3.5mm Euro style connectors.

**Note:** The Flex Input and Output components are not for use with QSC DataPort amplifiers.

[Inputs and Outputs](javascript:void(0))

### Inputs

#### Channels 1-8

By default, the Flex In component offers 8 Audio Inputs represented by a  circle, and traditional wiring is represented by a thin black line.

### Outputs

This component has no outputs available for this component.

[Properties](javascript:void(0))

There are no adjustable properties for the **Flex Output** component, other than what appears in the Core [Properties](core_status.htm#Properties).

[Controls](javascript:void(0))

Each control listed in the Analog and Digital sections, are one per channel.

### Flex I/O

#### Output

Changes the associated channel to a Flex Output channel.

To switch back to a Flex Input channel, you must enable the channel in the Flex Input component.

### Analog

#### Peak Input Level (dB)

Measures Peak Output level to the output device.

#### Output Mode

Mutes the output after the D-A converter and before the output.

#### Max RMS Output Level (dBu)

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

#### Gain (dB)

Controls the gain of the digital audio signal prior to the D/A converter.

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
| Analog Level  (Peak Output Level (dBu)) meter | -120 to 20 | -120 dB to 20 dB | 0.000 to 1.00 | Output |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Digital Level (Peak Output Level (dBFS)) meter | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Flex Output Enable | 0  1 | false  true | 0  1 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Max Level (dBu) | -40 to 20 | -40.0 to 20 | 0 to .988 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Output Gain | -31 to 0 | -31 dB to 0 dB | 0.000 to 1.00 | Input / Output |
| Output Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
