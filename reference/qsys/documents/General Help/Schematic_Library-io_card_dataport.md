# DataPort Out

> Source: https://help.qsys.com/Content/Schematic_Library/io_card_dataport.htm

# DataPort Out

The DataPort component is the Q-SYS Designer virtual component representing the [DataPort card](../Hardware/IO_Expanders/CODP4.htm). DataPort cards can be installed in a Core or an I/O Frame. (For more information, refer to the Core and I/O Frame User Guides.) The Q-SYS Designer design must match the physical hardware. The DataPort card provides control capability for connected amplifiers and loudspeakers. The controls for the amplifiers and loudspeakers are found in their corresponding control panels, not the DataPort control panel. The DataPort card:

* Works only with QSC DataPort amplifiers in a Q-SYS system.
* Converts the audio signal from digital to analog for the amplifier/loudspeakers, and analog to digital for audio monitoring.
* For QSC DataPort amplifiers, provides:
  + Four audio channels, two from each connector,
  + Telemetry (remote monitoring of critical parameters), including: status for protection, clipping, temperature, voltage, current, power, headroom, and open or shorted conditions on the outputs,
  + Standby/normal power control and status,
  + Gain and Mute functions,
  + Input signal presence status.
* For QSC loudspeakers connected to QSC DataPort amplifiers, Q-SYS provides:
  + Intrinsic Correctionâ¢
  + Telemetry, including: temperature, voltage, current, impedance, peak level, limiter reduction, and power compression.
  + Pilot Tone, including: enable for low and high and impedance for each.

**Note:** DataPorts on multi-port amplifiers must be wired to DataPorts on the same I/O Frame or Core. You cannot wire some of the amplifier's DataPorts to a Core and others, on the same amplifier, to an I/O Frame. You cannot wire some of the amplifier's DataPorts to one I/O Frame and others, on the same amplifier, to another I/O Frame.

## Type 2 Hardware

Type 2 hardware provides new cables and connectors between the I/O cards and main boards in Cores and I/O Frames. Due to this change, the Type 2 hardware is not physically compatible with the older hardware. You can still integrate the new I/O Frames and Cores in the same system with older hardware, but the I/O cards are not interchangeable. Type 2 hardware can be identified by a yellow label on the back of the Core and I/O Frame, and the bottom of the I/O cards.

[Properties](javascript:void(0))

The Properties displayed when the DataPort component is selected are for the [Core](core_status.htm) or the I/O Frame in which it is installed.

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

#### Peak output Level (dBFS)

Graphic Meter displays the Peak output level of the DSP prior to the DataPort card. The actual output of the DataPort card expressed in dBV can be viewed in the corresponding DataPort [Amplifier](amplifier_dataport.htm) control panel.

#### Mute

LED indicates if the output is muted or not. Red = Mute. This indicates that the "master" mute in the Loudspeaker Status/Control component is engaged.

#### Gain (dB)

Text readout indicates the RMS gain at the output of the DataPort card. The Gain for this meter is controlled in the master section of the Loudspeaker Status/Control component associated with the DataPort channel.

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

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Channel # Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Channel # Level | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Channel # Mute | 0  1 | unmuted  muted | 0  1 | Output |
| Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
