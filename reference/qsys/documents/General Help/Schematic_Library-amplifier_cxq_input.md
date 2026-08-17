# Mic/Line Input (CX-Q, CXD-Q, DPA-Q Series)

> Source: https://help.qsys.com/Content/Schematic_Library/amplifier_cxq_input.htm

# Mic/Line Input (CX-Q, CXD-Q, DPA-Q Series)

This topic covers the Mic/Line Input components for CX-Q, CXD-Q, and DPA-Q network amplifiers with line-level inputs.

**Note:** "Qn" models do not have analog inputs, and do not use this component.

The inputs on the rear panel of the amplifier provide line-level input to Q-SYS for line-level output devices and microphones. The Line Inputs are converted from the analog input signal to a processed digital signal. The Mic/Line Input component provides software controls in Q-SYS before (analog) and after (digital) the convertor.

Connections to the physical Line Inputs are made using four three-terminal Euro style connectors. These physical connectors are represented by the amplifier Input component in Q-SYS Designer.

Once the inputs are sent to Q-SYS, you can route them as needed, they do not have to go to the amplifier output. If you want these inputs sent back to the amplifier, you must connect the outputs of the input component to the inputs of the Amp Output component.

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

Toggle turning on and off phantom power to the microphone.

#### Preamp Sensitivity (dBu)

The maximum analog level, coming into the Flex Input component, that can be converted without clipping. This level is typically set slightly higher than the source's output level, so that the Peak Input Level reads about 0 dBFS without actually clipping.

Varies inversely with the Preamp Gain.

#### Preamp Gain (dB)

The amount of Gain applied to the incoming analog signal level.

Varies inversely with the Preamp Sensitivity.

### Digital

#### Invert

Toggle button to invert the digital output of the Input components.

#### Mute

Mutes the output signal.

#### Gain (dB)

Controls the Gain of the digital output signal.

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
| Clip | 0  1 | false  true | 0  1 | Input / Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Gain (Digital) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert (Digital) | 0  1 | normal  invert | 0  1 | Input / Output |
| Mute (Digital) | 0  1 | unmute  mute | 0  1 | Output |
| Peak Input Level (meter) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Phantom Power | 0  1 | disable  enable | 0  1 | Input / Output |
| Preamp Gain | 0 to 83 | 0 dB to 83 dB |  |  |
| Preamp Sensitivity | +27.0 to -56 | 27.0 to -56 | 0 to .988 | Input / Output |
| Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
