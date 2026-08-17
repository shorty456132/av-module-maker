# Flex Out (Core 8 Flex)

> Source: https://help.qsys.com/Content/Schematic_Library/io_card_flex_out_core_8flex.htm

# Flex Out (Core 8 Flex)

The Core 8 Flex provides eight audio channels that can be individually switched between line inputs and mic/line outputs. The Flex Out component provides the control and selection of the line-level outputs on the Core 8 Flex. The Flex Out component converts the processed digital signal to analog and provides software controls before and after the convertor. Connections are made using three-terminal 3.5mm Euro style connectors.

**Note:** The Flex In and Out components are not for use with QSC DataPort amplifiers.

[Properties](javascript:void(0))

Flex Out has no configurable properties. For a list of properties applicable to the Core 8 Flex in general, see:

* Core Mode: [Status (Core)](core_status.htm)
* Peripheral Mode: [Status (I/O-Core 8 Flex)](io_core_8_flex_status.htm)

[Controls](javascript:void(0))

#### Channel *n* Flex Output Enable

Changes the associated channel to a Flex Output channel. To switch back to a Flex Input channel, you must enable the channel in the Flex Input component.

#### Channel *n* Level (dBu)

Measures Peak Output level to the output device.

#### Channel *n* Output Mute

Mutes the output after the D-A converter and before the output.

#### Channel *n* Max Level

Controls the maximum analog RMS output level after the D/A converter, from -40 to +20 (default is +20). This level is typically set slightly lower than the destination's sensitivity or maximum input level in order to avoid clipping the signal of a power amplifier. Varies in direct proportion with Output Gain.

#### Channel *n* Output Gain

The amount of gain applied to the outgoing analog signal, from -60 to 0 dB (default is 0). Varies in direct proportion with the Max RMS Output Level.

#### Channel *n* Level (dBFS)

Measures the Digital Signal level prior to the D/A converter.

#### Channel *n* Clip

Red LED indicating if the signal is being clipped.

#### Channel *n* Clip Hold

Holds the clip indication until manually cleared.

#### Channel *n* Invert

Inverts the audio signal.

#### Channel *n* Mute

Mutes the audio signal.

#### Channel *n* Gain

Controls the gain of the digital audio signal prior to the D/A converter, from -100 to 20 dB (default is 0).

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
| Flex Output Enable | 0  1 | false  true | 0  1 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Level (dBFS) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Level (dBu) | -120 to 23 | -120 dB to 23 dB | 0.000 to 1.00 | Output |
| Max Level | -40 to 20 | -40 dBu to 20 dBu | 0.000 to 1.00 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Output Gain | -60 to 0 | -60 dB to 0 dB | 0.000 to 1.00 | Input / Output |
| Output Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
