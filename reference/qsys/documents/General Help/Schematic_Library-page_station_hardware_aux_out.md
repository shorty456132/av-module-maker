# Aux Line Out (Page Station)

> Source: https://help.qsys.com/Content/Schematic_Library/page_station_hardware_aux_out.htm

# Aux Line Out (Page Station)

The Page Station Aux Line Out feature allows you to send a line level audio signal to the Page Station for amplification and use. This feature is entirely separate from the Page Station functionality.

The Page Station Aux Line Out component allows you to control and monitor the digital gain, and analog output level going to the Line Out connector on the physical Page Station. In addition, this component supplies the input signal pin to which an audio source is connected in the design. You must drag a Page Station Aux Line Out component into your Q-SYS design to enable this feature.

[Inputs and Outputs](javascript:void(0))

#### Inputs

**Aux Line Out**
- Connect an audio source in your design to this input pin. The signal is processed through the Digital section of the component, then the Analog section, then sent via Q-LAN to the Page Station Line Out connector.

#### Outputs

There are no outputs for this component. The output is the Line Out connector on the physical Page Station.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Is Dynamic

Indicates that this virtual component can be paired with the same type of hardware without changing the network id of the hardware, or the name of this component. Refer to the Q-SYS Core Manager [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm) topic for more information.

#### Model

Selects the Model of the Page Station. Initially, you choose the model when you place the Page Station into the Inventory. You can change it here if needed.

#### Enable Expander

Enables the Page Station to support the use of the Page Station Expander (PS-X ). The PS-X allows you to connect a Q-SYS handheld microphone that can be mounted in the same general area as the Page Station. For example, the Page Station is mounted on the airline gate desk, whereas the PS-X is mounted at the gate itself.

When the Expander is enabled, the Aux Mic, and GPIO components are no longer available.

#### Verbose

Displays the Networking and Audio Stream details for LAN A (and LAN B, if applicable to the device). You must have Is Network Redundant set to Yes to see LAN B details.

[Controls](javascript:void(0))

### Analog

#### Peak Output Level (dBFS)

Graphic display of the **Aux** output indicating the peak analog output level.

#### Analog Mute

Mutes the Auxiliary analog output.

#### Max RMS Output Level (dBu)

Controls the RMS Output level for the **Aux** output.

The maximum level signal that can go out the D to A without clipping is 0 dBFS peak or -3 dBFS RMS. The "Max RMS Output Level (dBu)" control sets the analog level at which the signal will appear at the output.

### Digital

#### Clip

Indicates if the signal is in clipping or not.

#### Clip Hold

Holds the clip indication until manually cleared.

#### Invert

Inverts the output signal.

#### Mute

Mutes the output signal.

#### Gain

Sets the gain of the output signal.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Analog Level | -100 to 27 | -100 dB to 27 dB | 0.000 to 1.00 | Output |
| Analog Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Max Level | -10 to 6 | -10 to 6 | 0 to .988 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
