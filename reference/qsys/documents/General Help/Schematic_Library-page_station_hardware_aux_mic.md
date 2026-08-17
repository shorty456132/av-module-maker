# Aux Mic/Line In (Page Station)

> Source: https://help.qsys.com/Content/Schematic_Library/page_station_hardware_aux_mic.htm

# Aux Mic/Line In (Page Station)

The Page Station Aux Mic feature allows you to connect a microphone or other line level device to the Page Station and send the output of the connected device to the Q-SYS Core for processing. This feature is entirely separate from the Page Station functionality.

The Page Station Aux Mic component allows you to control the analog input level and digital gain of an auxiliary microphone or other line level device connected to the physical Page Station. In addition, this component supplies the output signal pin, carrying the auxiliary device's signal, which can then be processed as desired.

You must drag a Page Station Aux Mic component into your Q-SYS design to enable this feature.

[Inputs and Outputs](javascript:void(0))

#### Inputs

The Page Station Aux Mic component has no inputs. All the inputs are on the physical hardware.

#### Outputs

**Aux Mic/Line** - The audio from the auxiliary microphone or other line level device connected to the physical hardware is routed over the **Q-LAN** network to the **Q-SYS Core** and to the Page Station Aux Mic component. The output (Aux Mic/Line) of the Page Station's Aux Mic/Line In component is typically wired to one of the **PA Router**'s audio inputs. Audio Outputs represented by a  circle, and traditional wiring is represented by a thin black line.

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

#### Peak Input Level (dBFS)

Graphic display of the Auxiliary **Mic Line**input indicating the peak analog input level in dBFS.

#### Clip

Red LED indicating if the signal is being clipped.

#### Clip Hold

Holds the clip indication until manually cleared.

#### Max RMS Input Level (dBu)

Controls the RMS Input level for the **Aux Mic** input. This is the level prior to the A to D converter.

The maximum level signal that can go to the A to D converter without clipping is 0 dBFS peak or -3 dBFS RMS. The "Max RMS Input Level (dBu)" control sets the analog level at which the audio signal will appear at the input.

### Digital

#### Invert

Inverts the input signal.

#### Mute

Mutes the input signal.

#### Gain

Sets the gain of the input signal.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Peak Input Level  (dBFS) | -120 to 20 | -120 dB to 20 dB | 0.000 to 1.00 | Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Max Level | 12.0 to -56 | 12.0 to -56 | 0 to .988 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
