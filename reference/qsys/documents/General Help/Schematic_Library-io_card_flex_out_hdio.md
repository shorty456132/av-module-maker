# Flex Out (QIO Series)

> Source: https://help.qsys.com/Content/Schematic_Library/io_card_flex_out_hdio.htm

# Flex Out (QIO Series)

The Flex Channel feature provides four audio channels (QIO-FLEX4A) or eight audio channels (QIO-24f) that can be individually switched between mic/line inputs and line outputs. The Flex Out component provides the control and selection of the line-level outputs on the device. The Flex Out component converts the processed digital signal to analog and provides software controls before and after the convertor. Connections to a single channel are made using a three-terminal 3.5mm Euro style connector.

[Inputs and Outputs](javascript:void(0)) 

### Input Pins

#### Output 1-4 (QIO-FLEX4A) / Channel 1-8 (QIO-24f)

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

### Output Pins

*This component does not have any output pins.*

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### QIO-FLEX4A Properties

#### Amplifier Disabled

Enables deactivation of the amplifier functionality of the device, preventing audio amplification or output. Default is No.

[Controls](javascript:void(0))

Each control listed in the Analog and Digital sections, are one per channel.

### Flex I/O

#### Output

Changes the associated channel to a Flex Output channel.

To switch back to a Flex Input channel, you must enable the channel in the Flex Input component.

### Analog

#### Peak Output Level (dBu)

Measures Peak Output level to the output device.

#### Output Mute

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

#### Gain (dB)

Controls the gain of the digital audio signal prior to the D/A converter.

### Status

#### Status LED

This LED changes color to indicate the current status of the Touchscreen. See Touchscreen Status for the meanings of the various colors.

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

Each channel on the Flex Input component has the following Control Pins with the exception of the Status Control Pin.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Channel 1-4 | | | | |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Flex Output Enable | 0  1 | false  true | 0  1 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Level (dBFS) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Level (dBu) | -120 to +27 | -120 dBu to +27 dBu | 0.000 to 1.00 | Output |
| Max Level (dBu) | -37 to 24 | -37 dBu to 24 dBu | 0 to .988 | Input / Output |
| Mute | 0  1 | false  true | 0  1 | Input / Output |
| Output Gain | -61 to 0 | -61 dB to 0 dB | 0.000 to 1.00 | Input / Output |
| Output Mute | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
