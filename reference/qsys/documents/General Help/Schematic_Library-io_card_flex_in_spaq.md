# Flex In (SPA-Qf Series)

> Source: https://help.qsys.com/Content/Schematic_Library/io_card_flex_in_spaq.htm

# Flex In (SPA-Qf Series)

The Flex Channel feature on SPA-Qf series provide two audio channels that can be individually switched between line inputs and line outputs. The Flex Input Component provides the control and selection of the line-level outputs on the Core. The Flex Input component converts the analog signal to digital and provides software controls before and after the convertor. Connections to a single channel are made using a three-terminal 3.5mm Euro style connector.

**Note:** The Flex Input and Output components are not for use with QSC DataPort amplifiers.

[Inputs and Outputs](javascript:void(0))

### Inputs

This component does not have any input pins available.

### Output

#### Channels 1-2

By default, the Flex In component offers 2 Audio Outputs represented by a  circle, and traditional wiring is represented by a thin black line.

[Properties](javascript:void(0)) 

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### SPA-Qf Amplifier Properties

#### Model

Select the hardware model from the drop-down list.

#### Channel Configuration

Select the configuration needed for your venue.

* 2 Channel, A B Single Channels
* 1 Channel, A + B Bridged

Channel configurations are as follows:

* Space between letters (A B C D) = single channels,
* "+" between letters (A+B) = bridged

When you make your selection, then run the design, the configuration is made available to the amplifier. Follow the instructions on the amplifier display.

#### Standalone Mode

**Off** â Turns Standalone Mode off.

**One-to-all** â Input Channel 1 is routed to all outputs.

**Note:** See the [Standalone Mode](#Standalone_SPAQ) below for details.

[Controls](javascript:void(0)) 

### Input / Output Tab

#### Flex I/O

#### Input (Enable)

Changes the associated channel to a Flex Input channel.

To switch back to a Flex Output channel, you must enable the channel in the Output Component.

#### Mic Detection

#### Enable (Yellow LED)

When the LED is on, the associated channel has Mic Detection enabled. When the LED is off, Mic Detection is disabled.

#### Good (Green LED)

When the LED is green, the mic impedance is within the set thresholds. If the thresholds are exceeded, the green LED is off.

#### Analog

#### Peak Input Level (dB)

Meters for each channel indicating the peak analog input level. The measurement is taken after the A/D converter, but before the Digital Gain. Use this meter in conjunction with the Max Input Level to obtain an input signal as close to 0 dBFS as possible without actually clipping.

#### Clip

Red LED indicating if the signal is being clipped.

#### Clip Hold

Holds the clip indication until manually cleared.

#### Phantom Power

Toggle turning on and off phantom power (+48VDC) to the microphone.

#### Preamp Sensitivity (dBu)

The maximum analog level, coming into the Flex Input component, that can be converted without clipping. This level is typically set slightly higher than the source's output level, so that the Peak Input Level reads about 0 dBFS without actually clipping.

Varies inversely with the Preamp Gain.

#### Preamp Gain (dB)

The amount of Gain applied to the incoming analog signal level.

Varies inversely with the Preamp Sensitivity.

#### Digital

#### Invert

Toggle button to invert the digital output of the Flex Input component.

#### Mute

Mutes the output signal.

#### Gain (dB)

Controls the Gain of the digital output signal.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

### Mic Detection Tab

#### Detection

#### Enable (Toggle Button)

Enables or disables Mic Detection for the associated channel. When Mic Detection is on, the impedance of the mic is measured against the set thresholds.

#### Good (Green LED)

When the LED is green, the mic impedance is within the set thresholds. If the thresholds are exceeded, the green LED is off.

#### Impedance

The measured impedance of the attached microphone.

#### Set Thresholds (Trigger Button)

Sets the high and low thresholds based on the mic impedance at the time the button is pushed.

#### Thresholds

#### High Impedance

Manually adjust the mic detection high impedance threshold for each channel, from none to >100kÎ© (default is none).

#### Low Impedance

Manually adjust the mic detection low impedance threshold for each channel, from none to >100kÎ© (default is none).

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Channel 1 - 2 | | | | |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Flex Input Enable | 1  0 | enabled  disabled | 1  0 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Level (dBFS) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Mic Detection Enable  (button) | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Mic Detection Enabled  (LED) | 0  1 | no  yes | 0  1 | Output |
| Mic Detection Good | 0  1 | no  yes | 0  1 | Output |
| Mic Detection High Impedance Threshold | 0 to >100001 | --- to >100kÎ© | 0 to 1.00 | Input / Output |
| Mic Detection Impedance |  |  |  | Output |
| Mic Detection Low Impedance Threshold | 0 to >100001 | --- to >100kÎ© | 0 to 1.00 | Input / Output |
| Mic Detection Set Thresholds | Trigger | | | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Phantom Power | 0  1 | disable  enable | 0  1 | Input / Output |
| Preamp Gain | 0 to 60 | 0dB to 60dB | 0 to 1.00 | Input / Output |
| Preamp Sensitivity | 21 to -39 | +21dBu to -39dBu | 1.00 to 0 | Input / Output |
| Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |

[Standalone Mode](javascript:void(0))

Standalone Mode provides the capability to connect the inputs of an amplifier to the outputs when connection to the Core is lost. In addition you can boot the amplifier without a connection to the Core.

Two ways to engage the Standalone Mode. For either way you must enable the **Standalone Mode** in the Q-SYS Designer Properties for the amplifier.

1. Amplifier Loses Network Connection to the Core:
   1. When connection to the Core is lost, audio is interrupted, and the amplifier counts down the number of seconds (15-60) specified in the amplifier's Properties in the Q-SYS design.
   2. After the timeout period, the inputs of the amplifier are sent directly to the outputs either one-to-one (each input goes to its corresponding output), or one-to-all (one input goes to all the outputs). While in Standalone mode, the front panel display of the amplifier displays OK in the Status field.
   3. When the connection to the Core is restored, the original audio streams are restored. There will be a short drop in audio while the amplifier is re-initialized.
2. Boot the Amplifier Without a Connection to the Core
   1. The amplifier waits 10 seconds to determine if the connection to the Core can be made.
   2. The amplifier then launches the last design run if it had the Standalone Mode enabled. During this time, the amplifier front-panel Status field displays OK, and the Design field displays "Stand-alone".
   3. When the amplifier re-connects to the Core, the Core pushes the design to the amplifier and the original audio is restored. There is a short loss of audio while the amplifier is initialized.

**Note:** Standalone Mode is not supported by CXD-Qn, CX-Qn, and DPA-Qn series amplifiers. Qn series amplifiers only support network connectivity and do not have line inputs.
