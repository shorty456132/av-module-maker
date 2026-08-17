# Flex Out (SPA-Qf Series)

> Source: https://help.qsys.com/Content/Schematic_Library/io_card_flex_out_spaq.htm

# Flex Out (SPA-Qf Series)

The Flex Channel feature on SPA-Qf series provide two audio channels that can be individually switched between line inputs and line outputs. The Flex Input Component provides the control and selection of the line-level outputs on the Core. The Flex Input component converts the analog signal to digital and provides software controls before and after the convertor. Connections to a single channel are made using a three-terminal 3.5mm Euro style connector.

**Note:** The Flex Input and Output components are not for use with QSC DataPort amplifiers.

[Inputs and Outputs](javascript:void(0))

### Inputs

#### Channels 1-2

By default, the Flex In component offers 2 Audio Inputs represented by a  circle, and traditional wiring is represented by a thin black line.

### Output

This component does not have any output pins available.

[Properties](javascript:void(0)) 

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### SPA-Qf Amplifier Properties

#### Model

Select the hardware model from the drop-down list.

#### Channel Configuration

Select the configuration needed for your venue.

**Note:** Eight-channel models have two sets of four channels for configuration.

* 4 Channel, A B C D
* 3 Channel, A+B C D | A B Bridged
* 2 Channel, A+B+C+D | A B Bridged C D Bridged

Channel configurations are as follows:

* Space between letters (A B C D) = single channels,
* "+" between letters (A+B) = bridged,
* no space between letters (ABCD) = parallel.

When you make your selection, then run the design, the configuration is made available to the amplifier. Follow the instructions on the amplifier display.

#### Standalone Mode

**Off** â Turns Standalone Mode off.

**One-to-all** â Input Channel 1 is routed to all outputs.

**Note:** See the [Standalone Mode](#Standalone_SPAQ) below for details.

[Controls](javascript:void(0)) 

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

Controls the gain of the digital audio signal prior to the D/A converter

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
| Flex Output Enable | 0  1 | false  true | 0  1 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Level (dBFS) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Level (dBu) | -120 to 23 | -120 dB to 23 dB | 0.000 to 1.00 | Output |
| Max Level (dBu) | -40 to 20 | -40.0 to 20 | 0 to .988 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Output Gain | -31 to 0 | -31 dB to 0 dB | 0.000 to 1.00 | Input / Output |
| Output Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
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
