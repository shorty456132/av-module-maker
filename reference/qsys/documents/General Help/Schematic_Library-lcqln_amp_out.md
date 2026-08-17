# Amp Out (QIO-FLEX4A)

> Source: https://help.qsys.com/Content/Schematic_Library/lcqln_amp_out.htm

# Amp Out (QIO-FLEX4A)

Use the Amp Output component to send digital audio over Q-LAN to the QIO-FLEX4 output channels, where it is converted to analog audio and then amplified. This component provides the inputs to the output stage of the amplifier.

[Inputs and Outputs](javascript:void(0))

### Inputs

The inputs are digital audio from any appropriate component within Q-SYS Designer. Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

### Outputs

*There are no outputs for this component.*

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### QIO-FLEX4A Amplifier Properties

#### Amplifier Disabled

Enables deactivation of the amplifier functionality of the device, preventing audio amplification or output. Default is No.

[Controls](javascript:void(0))

### Amplifier Status

#### Limiter

Yellow LED indicating that the amplifier is in the limiting mode. This occurs if the signal is driving the power, current, or voltage above the amplifier rated values or due to thermal limiting.

#### Temp

Red LED indicating the amplifier is thermally limited.

#### Short

Red LED indicating there is a short in the loudspeaker circuitry.

### Output

#### Peak Output Level (dBFS)

Graphic display of the peak output level, measured in dBFS.

#### Clip

Indicates if the signal is in clipping or not.

#### Clip Hold

Holds the clip indication until manually cleared.

#### Mute

Mutes the associated channel of the amplifier. This is linked to the Mute button on the amplifier itself.

#### Gain

The Gain knob adjusts the digital gain of the associated output channels, from -100dB to 20dB (default is 0 dB).

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
| Channel 1-2 | | | | |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Level (Peak Output Level (dBFS)) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Mute | 0  1 | false  true | 0  1 | Input / Output |
| Short | 0  1 | false  true | 0  1 | Output |
| Temp | Text Field | | | Output |
| Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
