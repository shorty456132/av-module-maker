# Analog In â DCIO/DCIO-H

> Source: https://help.qsys.com/Content/Schematic_Library/io_analog_in_card_dcio.htm

# Analog In â DCIO/DCIO-H

The Analog Input for the DCIO (and DCIO-H) has two line-level inputs and an input for a microphone. The connectors are physically part of the DCIO. The Analog Input converts the input signal to processed digital and provides software controls before and after the convertor. Connection for the Mike / Line input is provided via a standard three-conductor XLR connector with balanced input, phantom power available in Q-SYS Designer. Used for: mono, non-sync sources including microphone for in-auditorium announcements, and SPL metering. In addition to the XLR, a standard 3.5mm TRS jack, unbalanced, stereo, analog, line-input.

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

Toggle turning on and off phantom power (+15VDC) to the microphone. Not available for the Line Inputs.

#### Preamp Sensitivity (dBu)

The maximum analog level, coming into the Analog Input, that can be converted without clipping. This level is typically set slightly higher than the source's output level, so that the Peak Input Level reads about 0 dBFS without actually clipping.

You can select the field and enter the value you want, or click and drag the number to the value.

Varies inversely with the Preamp Gain.

#### Preamp Gain knob (Mic Only) (dB)

The amount of Gain applied to the incoming analog signal level. Varies inversely with the Preamp Sensitivity.

#### Preamp Gain Buttons (Line Only)

The amount of Gain applied to the incoming analog signal level.

Left and Right toggle buttons toggle the Preamp Gain between 0dB when Off, and 12dB when On. this results in a change in Preamp Sensitivity.

|  |  |  |
| --- | --- | --- |
| Toggle Button | Preamp Gain | Preamp Sensitivity |
| Off | 0dB | 15dBu |
| On | 12dB | 3dBu |

The values of 0dB and 12dB can be seen by connecting a Custom Controls "Text Display" to the Preamp Gain control pin output.

### Digital

#### Invert

Toggle button to invert the digital output of Analog Input.

#### Mute

Toggle button to mute and unmute the output signal.

#### Gain (dB)

Controls the Gain of the digital output signal. Range is between -100 and 20 dB.

### Status

#### Status LED

This LED changes color to indicate the current status of the Core. See Status for the meanings of the various colors.

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

[Control Pins](javascript:void(0))

The Analog Input has the following Control Pins.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Level | â -100 to 20 | â -100 dB to 20 dB | 0 to 1.00 | Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0. to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Phantom Power | 0  1 | disable  enable | 0  1 | Input / Output |
| Preamp Gain  Mic Channel  Left / Right Channel  (dB) | 0 to 58  0 or 12 | 0dB to 58dB  0dB or 12dB | 0 to 1.00  0 to 1.00 | Input / Output  Input / Output |
| Preamp Sensitivity  (dBu) | +26 to -32 | +26dBu to -32dBu | 0 to 1.00 | Input / Output |
| Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
