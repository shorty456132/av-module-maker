# Amp Output (SPA-Qf Series)

> Source: https://help.qsys.com/Content/Schematic_Library/spaq_amplifier.htm

# Amp Output (SPA-Qf Series)

Use the Amp Output component to send digital audio over Q-LAN to the SPA-Qf Series output channels, where it is converted to analog audio and then amplified. This component provides the inputs to the output stage of the amplifier.

[Inputs and Outputs](javascript:void(0))

### Inputs

The inputs are digital audio from any appropriate component within Q-SYS Designer. There can be from one to four inputs (four channel models). Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

### Outputs

The outputs are digital audio connecting to loudspeaker components. Loudspeaker signal pins are represented by a left-pointing () triangle, and the wiring is represented by a thin orange line.

[Properties](javascript:void(0))

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

**Note:** In order to use 70V or 100V (Hi-Z) speakers in the design, the amplifier channel must be set to âBridgedâ (i.e. A+B and/or C+D).

* Space between letters (A B C D) = single channels,
* "+" between letters (A+B) = bridged,
* no space between letters (ABCD) = parallel.

When you make your selection, then run the design, the configuration is made available to the amplifier. Follow the instructions on the amplifier display.

#### Standalone Mode

**Off** â Turns Standalone Mode off.

**One-to-all** â Input Channel 1 is routed to all outputs.

**Note:** See the [Standalone section](#Standalone_Mode) below for details.

[Controls](javascript:void(0))

### Amplifier Status

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### On/Standby

Toggles the amplifier from Standby to Power On and back. See [Amplifier Power Modes](#Amplifier.SPA-q).

#### Mute All

Mutes all channels of the amplifier. Once Mute All is engaged, you must use the Mute All button to unmute the channels. The individual channel Mute is disabled while the Mute All is engaged. See [Amplifier Power Modes](#Amplifier.SPA-q).

#### PSU Temp

Temperature of the amplifier's power supply. Thresholds:

* 60Â° C triggers the Compromised state
* 73Â° C mutes all audio

#### V Rail 1

Internal amplifier voltage monitor. +80VDC and -80VDC +/3V typical.

#### V Rail 2

Internal amplifier voltage monitor. +80VDC and -80VDC +/3V typical.

#### Standalone (test button)

This control is available only in Standalone mode. Press this button to simulate Standalone mode. You will hear the audio that is played when the amplifier is in the Standalone Mode.

### Power Management

**Tip:** Use the PowerSave controls to reduce amplifier energy usage when input signals drop below the desired threshold level. PowerSave monitoring occurs at the input of the amplifier block. See [Amp Output (SPA-Qf Series)](#Amplifie).

#### AC Voltage

The AC Mains voltage, âOKâ / âLOWâ (below 90V) / âHIGHâ (above 260V) indicator for AC voltage.

#### AC Current

The AC Mains current being drawn by the amplifier.

#### PowerSave Threshold

Select the input dB threshold below which the PowerSave Timeout is triggered, from -99.0dB to -50.0dB (-80.0dB is default).

#### PowerSave Timeout

Once the PowerSave Threshold has been reached, a timer counts down from this value, between 30 and 120 minutes (default is 30). At the end of the countdown, the amplifier goes into a reduced power mode to save energy.

### Channel (A, B, C, D) Status

#### Channel

The channel letters change based on the Channel Configuration selection in the Properties:

* Single channels = A (or B, C, D)
* Parallel channels = AB (or CD)
* Bridged channels = A+B (or C+D)

The default is four separate channels â A, B, C, D

#### Output Config

Displays the connected output.

#### Gain

The Gain knob adjusts the digital gain of the associated output channels, from -100dB to 20dB (default is 0 dB).

#### Mute

Mutes the associated channel of the amplifier. This is linked to the Mute button on the amplifier itself.

#### Over Current

Red LED indicating an over current condition exists in the associated amplifier channel.

#### DAC Limit

Red LED indicating that signal to the D to A Converter is larger than can be reproduced and a limiter has been engaged to prevent clipping. This is an indication that the gain structure is not correct.

#### Protect

Red LED indicating that the channel is in Protect Mode. Usually due to attempting to drive too low an impedance for too long.

#### PowerSave

Red LED indicating that the channel is in PowerSave mode. PowerSave is enabled by default.

#### Limit

Red LED indicating that the amplifier is in the limiting mode. This occurs if the signal is driving the power, current, or voltage above the amplifier rated values or due to thermal limiting.

#### Short

Red LED indicating there is a short in the loudspeaker circuitry.

#### Temp

Displays the temperature, in Centigrade, of the associated channel.

### Channel (A, B, C, D) Meter

These readings can be RMS or Peak depending on the Meter Select setting.

#### Input (dBFS)

Measures the digital input to the amplifier output channel, from -120 to 20.

#### Voltage (V)

Measures the voltage of the amplifier / loudspeaker circuit, from 0 to 150.

#### Current (A)

Measures the current of the amplifier / loudspeaker circuit.

#### Power (W)

Measures the power of the amplifier / loudspeaker circuit.

#### Headroom (dB)

Measures the amount of headroom left before reaching the amplifier's maximum capabilities.

### Monitor

There is one Listen button and one Gain control for each channel.

#### Listen

The Listen button activates the Loudspeaker monitor for the associated channel.

#### Gain

The Gain knob controls the output gain to the Loudspeaker Monitor component, from -100 to 20dB.

### Standalone

There is one Mute button and one Gain control for each channel.

#### Mute

Mutes the output of the amplifier channel when in Standalone Mode.

#### Gain

Controls the Gain of the amplifier's output when in Standalone mode, from -100 to 20dB.

[Control Pins](javascript:void(0))

[Channel (A, B, C, D)](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Current Peak | 0 to 70 | 0 A to 70 A | 0.000  1.000 | Output |
| Current RMS | 0 to *n* | O A to *n* A | 0.000 to 1.00 | Output |
| DAC Output Limit | 0  1 | false  true | 0  1 | Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Input / Output |
| Headroom | 0 to 70 | 0 dB to 70 dB | 0.000  1.000 | Output |
| Input Meter | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Output |
| Input RMS Meter | 0 to *n* | O A to *n* A | 0.000 to 1.00 | Output |
| Limit | 0  1 | false  true | 0  1 | Output |
| Monitor Gain | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Input / Output |
| Monitor Listen | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| outputmode | Text Field | | | Output |
| Over Current | 0  1 | false  true | 0  1 | Output |
| Power Peak | 0 to *n* | O W to *n* W | 0.000 to 1.00 | Output |
| Power RMS | 0 to *n* | O W to *n* W | 0.000 to 1.00 | Output |
| PowerSave | 0  1 | false  true | 0  1 | Output |
| Protect | 0  1 | false  true | 0  1 | Output |
| Short | 0  1 | false  true | 0  1 | Output |
| Standalone Gain | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Input / Output |
| Standalone Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Temperature | Text Field | | | Output |
| Voltage Peak | 0 to 150 | V to 150 V | 0.000  1.000 | Output |
| Voltage RMS | 0 to *n* | O V to *n* V | 0.000 to 1.00 | Output |

[Amplifier](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| AC Current | .*nnn* | .*nnn*A | - | Output |
| AC Voltage Status | 100 - 240 | 100V - 240V | 0V = 0  120V = .5  240V = 1.00 | Output |
| Mute All | 0  1 | unmute  mute | 0  1 | Input / Output |
| Power On | 0  1 | Standby  On | 0  1 | Input / Output |
| Power Supply Temperature | *n* | *n* Â°C | 0.000  1.000 | Output |
| Powersave Threshold (dB) | -99.0 to -50.0 | -99.0dB to -50.0dB | 0.000  1.000 | Input / Output |
| Powersave Timeout (min) | 1 to 99 | 1 to 99 | 0.000  1.000 | Input / Output |
| Rail 1 Voltage | 142 to 152 | 142V to 152V | 0.000  1.000 | Output |
| Rail 2 Voltage | -142 to -152 | -142V to -152V | 0.000  1.000 | Output |
| Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |

[Amplifier Power Modes](javascript:void(0))

Consult this table to understand the behavior of the amplifier in each of its power modes.

| Mode | Amplifier Channel Switching | DSP | Main Power Supply | Description |
| --- | --- | --- | --- | --- |
| On | Active | Active | Active | The amplifier is ready to deliver power. Amplifier output is actively switching. |
| PowerSave | Active (Individual Channel Basis) | Active | Active | This control stops individual amplifier outputs from switching. |
| Mute All | Not Active | Active | Active | This control stops all amplifier channels from switching. |
| Standby | Not Active | Not Active | Not Active | In this mode, some internal low voltage components are still powered. However, when the amplifier comes out of standby, a reboot of the DSP is required. |
| Off | Not Active | Not Active | Not Active | All components of the amplifier are off. |

[Standalone Mode](javascript:void(0))

Standalone Mode provides the capability to connect the inputs of an amplifier to the outputs when connection to the Core is lost. In addition you can boot the amplifier without a connection to the Core.

Two ways to engage the Standalone Mode. For either way you must enable the Standalone Mode in the Q-SYS Designer Properties for the amplifier.

1. Amplifier Loses Network Connection to the Core:
   1. When connection to the Core is lost, audio is interrupted, and the amplifier counts down the number of seconds (15-60) specified in the amplifier's Properties in the Q-SYS design.
   2. After the timeout period, the inputs of the amplifier are sent directly to the outputs either one-to-one (each input goes to its corresponding output), or one-to-all (one input goes to all the outputs). While in Standalone mode, the front panel display of the amplifier displays OK in the Status field.
   3. When the connection to the Core is restored, the original audio streams are restored. There will be a short drop in audio while the amplifier is re-initialized.
2. Boot the Amplifier Without a Connection to the Core
   1. The amplifier waits 10 seconds to determine if the connection to the Core can be made.
   2. The amplifier then launches the last design run if it had the Standalone Mode enabled. During this time, the amplifier front-panel Status field displays OK, and the Design field displays "Stand-alone".
   3. When the amplifier re-connects to the Core, the Core pushes the design to the amplifier and the original audio is restored. There is a short loss of audio while the amplifier is initialized.

**Note:** Standalone Mode is not supported by CXD-Qn, CX-Qn, and DPA-Qn series amplifiers. Qn series amplifiers only support network connectivity and do not have line inputs.
