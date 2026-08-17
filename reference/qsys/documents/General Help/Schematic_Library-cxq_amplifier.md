# Amp Output (CX-Q, CXD-Q, DPA-Q Series)

> Source: https://help.qsys.com/Content/Schematic_Library/cxq_amplifier.htm

# Amp Output (CX-Q, CXD-Q, DPA-Q Series)

Use the Amp Output component to send digital audio over Q-LAN to the CX-Q, CXD-Q, or DPA-Q output channels, where it is converted to analog audio and then amplified. This component provides the inputs to the output stage of the amplifier.

The analog audio input to the Line Inputs on the rear of the amplifier is converted to digital audio and sent to the [Mic/Line Input (CX-Q, CXD-Q, DPA-Q Series)](amplifier_cxq_input.htm) component via Q‑LAN. Use the Amp Output control panel for telemetry, as well as amplifier control of On / Standby, Mute, and Gain. The same controls are available on the amplifier's front panel.

[Inputs and Outputs](javascript:void(0))

### Inputs

The inputs are digital audio from any appropriate component within Q-SYS Designer. There can be from one to four inputs (four channel models) or two to eight inputs (eight channel models) and is dependent on the [FAST](amplifier_cxq_status.htm#FAST_Mode) configuration. The eight channel models have two sets of four channels.

### Outputs

The outputs are digital audio connecting to loudspeaker components.

[70V, 100V Mode](javascript:void(0))

Network amplifiers are capable of supplying 70V or 100V outputs. To use this mode, you must connect an appropriate loudspeaker component to the Amp Output component. For QSC loudspeaker components capable of using 70V or 100V, set the Mode Property of the loudspeaker component to either 70V or 100V. Q-SYS sets the amplifier to this mode when the design is deployed.

In addition, when an amplifier is set to either 70V or 100V mode, a 50 Hz high-pass filter is automatically added in line to protect the loudspeakers.

**Note:** To set CXD4.2Q and DPA4.2Q amplifiers to 70V or 100V mode, you must configure the outputs to channels A and B bridged, and channels C and D bridged (A+B C+D).

[Properties](javascript:void(0))

Refer to the [Status (CX-Q, CXD-Q, DPA-Q Series)](amplifier_cxq_status.htm) component topic.

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

#### On / Standby

Toggles the amplifier from Standby to Power On and back. See [Amplifier Power Modes](#Amplifie).

#### Mute All

Mutes all channels of the amplifier. Once Mute All is engaged, you must use the Mute All button to unmute the channels. The individual channel Mute is disabled while the Mute All is engaged. See [Amplifier Power Modes](#Amplifie).

#### Power Meters

This will either show or hide power meters depending if the button is enabled or disabled.

#### Front Panel

This is an inactive area. Instead, it is displaying the items associated to the front panel below it: Gain Lock, Mute Lock, and Disabled.

#### Gain Lock

Disables the gain control on the front panel of the amplifier. (The gain controls in the Q-SYS Designer Software component are not disabled.)

#### Mute Lock

Disables the mute controls on the front panel of the amplifier. (The mute controls in the Q-SYS Designer Software component are not disabled.)

#### Disabled

After choosing to Save to Core & Run, with this mode enabled, the front panel will not show any LED's operating and the LCD screen will not work. Additionally, all buttons and the gain knob will be disabled. When any button is pressed, the signal and power LED's will flash 5 times to indicate that this mode is engaged. When the front panel is disabled, the Factory Reset pinhole button is still active.

#### PSU Temp

Temperature of the amplifier's power supply. Thresholds:

* 55Â° C triggers the Compromised state
* 63Â° C mutes all audio

#### V Rail 1

Internal amplifier voltage monitor. 147VDC +/- 5V typical.

#### V Rail 2

Internal amplifier voltage monitor. -147VDC +/- 5V typical.

#### Fan RPM

The fan speed varies based on the temperatures.

#### Meter Select

Selects either RMS or Peak for the five meters in all channels. Changing the meter type changes the meter readings on the Amp Output component and on the amplifier output gain meters.

#### Standalone (test button)

This control is available only in Standalone mode. Press this button to simulate Standalone mode. You will hear the audio that is played when the amplifier is in the Standalone Mode.

### Power Management

**Tip:** Use the PowerSave controls to reduce amplifier energy usage when input signals drop below the desired threshold level. PowerSave monitoring occurs at the input of the amplifier block. See [Amplifier Power Modes](#Amplifie).

#### AC Voltage

The AC Mains voltage, from 100 VAC to 240 VAC.

#### AC Current

The AC Mains current being drawn by the amplifier.

#### PowerSave Threshold

Select the input dB threshold below which the PowerSave Timeout is triggered, from -99.0dB to -50.0dB (-80.0dB is default).

#### PowerSave Timeout

Once the PowerSave Threshold has been reached, a timer counts down from this value, between 1 and 99 minutes (default is 10). At the end of the countdown, the amplifier goes into a reduced power mode to save energy.

#### Disable PowerSave

When toggled on, the amplifier will not go into PowerSave mode. PowerSave is enabled by default.

### Channel (A, B, C, D), (and E, F, G, H for eight channel) Status

#### Channel

The channel letters change based on the Channel Configuration selection in the Properties:

* Single channels = A (or B, C, D) ( 8CH E, F, G, H)
* Parallel channels = AB (or CD) (8CH EF or GH)
* Bridged channels = A+B (or C+D) (8CH E+F or G+H)

The default is four separate channels â A, B, C, D (and E, F, G, H for 8-channel).

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

LED will illuminate if PowerSave is enabled. PowerSave is enabled by default.

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

#### Output (dBFS)

Measures the digital output to the amplifier output channel, from -120 to 20.

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

[Amplifier](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| AC Current | .*nnn* | .*nnn*A | - | Output |
| AC Mains Voltage | 100 - 240 | 100V - 240V | 0V = 0  120V = .5  240V = 1.00 | Output |
| Disable Powersave Features for All Channels | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Enter Powersave after this many minutes below the threshold | 1.00 to 99.0 | 1.00 to 99.0 | 1.00 to 99.0 | Input / Output |
| Enter Powersave when Peak Input is below this value | -99.0dB to -50.0dB | -99.0dB to -50.0dB | -99.0dB to -50.0dB | Input / Output |
| Fan Speed | *nnnn* | *nnnn* | - | Input / Output |
| Front Panel Disabled | 0  1 | unmute  mute | 0  1 | Input / Output |
| Gain Lockout | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Mute All | 0  1 | unmute  mute | 0  1 | Input / Output |
| Mute Lockout | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Peak/RMS Select | 0  1 | Peak  RMS | 0  1 | Input / Output |
| Power On | 0  1 | Standby  On | 0  1 | Input / Output |
| Power Supply Temperature | *n* | *n* Â°C | 0.000  1.000 | Output |
| Rail 1 Voltage | 142 to 152 | 142V to 152V | 0.000  1.000 | Output |
| Rail 2 Voltage | -142 to -152 | -142V to -152V | 0.000  1.000 | Output |
| Show/Hide Power Meters | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |

[Channel (A, B, C, D) (and for 8-channel E, F, G, H)](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Current | 0 to 70 | 0 A to 70 A | 0.000  1.000 | Output |
| DAC Output Limit | 0  1 | false  true | 0  1 | Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Input / Output |
| Headroom | 0 to 70 | 0 dB to 70 dB | 0.000  1.000 | Output |
| Input Meter | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Output |
| Limit | 0  1 | false  true | 0  1 | Output |
| Monitor Gain | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Input / Output |
| Monitor Listen | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Output Meter, Post Gain | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Output |
| Over Current | 0  1 | false  true | 0  1 | Output |
| Power | 0 to 10000 | 0 W to 10,000 W | 0.000  1.000 | Output |
| PowerSave | 0  1 | false  true | 0  1 | Output |
| Protect | 0  1 | false  true | 0  1 | Output |
| Short | 0  1 | false  true | 0  1 | Output |
| Temperature | Text Field | | |  |
| Voltage | 0 to 150 | V to 150 V | 0.000  1.000 | Output |

[Amplifier Power Modes](javascript:void(0))

Consult this table to understand the behavior of the amplifier in each of its power modes.

| Mode | Amplifier Channel Switching | DSP | Main Power Supply | Description |
| --- | --- | --- | --- | --- |
| On | Active | Active | Active | The amplifier is ready to deliver power. Amplifier output is actively switching. |
| PowerSave | Active (Individual Channel Basis) | Active | Active | This control stops individual amplifier outputs from switching. |
| Mute All | Not Active | Active | Active | This control stops all amplifier channels from switching. |
| Standby | Not Active | Not Active | Not Active | In this mode, some internal low voltage components are still powered. However, when the amplifier comes out of standby, a reboot of the DSP is required. |
| Off | Not Active | Not Active | Not Active | All components of the amplifier are off. |
