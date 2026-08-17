# Attero Tech Axon A4FLEX

> Source: https://help.qsys.com/Content/Schematic_Library/Attero_Tech_extension_AxonA4Flex.htm

# Attero Tech Axon A4FLEX

Use this extension to connect to and control the Axon A4FLEX AES67 scalable mic/line connectivity interface (Attero Tech by QSC).

**Note:** See the [Axon A4FLEX product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/attero-tech/at-surface-mount-network-audio-interfaces/axon-a4flex/) on the QSC website for product information and documentation.

[Compatibility](javascript:void(0))

The extension is compatible with Q-SYS Designer version 8.4 and above and Attero Tech firmware version 2.1.1.0 and above. For best results, use the latest Attero Tech firmware.

[Connection Setup](javascript:void(0))

1. In the NIC field, select the interface through which the extension will communicate to control the device.
2. In the IP field, specify the IP address of the device and press Enter.

The extension will automatically attempt a connection. The "Connected" LED glows green once a connection is established. If the extension loses its connection to the device, it will attempt to re-establish the connection every 5 seconds.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

Select if the flex I/O 3 is an audio input (default) or output.

#### Flex I/O 4

Select if the flex I/O 4 is an audio input (default) or output.

#### Show Debug

Select 'Yes' to show the Debug Output window. For details, see [Debug Output](debug_output.htm).

[Controls](javascript:void(0))

#### Device Name

Appears just below the company logo, if available from the connected device. If the extension cannot retrieve the name, the field remains blank.

#### Force Config

If the extension detects that the configuration of the device does not match those set in the extension, click the button to update the device settings to match.

**Note:** A configuration mismatch would be indicated in the extension by the following message*:* **Fault - Invalid I/O cfg**. Before forcing config, ensure the extension is communicating with the correct unit, and also verify if the device has had the I/O configured in unIFY Control Panel.

#### Refresh

Although the extension monitors the device settings for changes automatically, this button manually triggers the extension to retrieve the current settings and update the extension values to match.

#### Meters

Toggles metering functionality on or off. Metering packets are only sent when metering is enabled.

**Note:** Metering should only be used for diagnostics and disabled during normal operation. Metering quickly consumes significant bandwidth if enabled on multiple devices simultaneously.

#### Identify

Causes the power LED on the front of the device to start blinking so it can easily be identified. The identify function remains active until manually turned off. Click the button to toggle between states.

#### Status

Normally, this shows "Initializing" for a few moments after starting your design, followed by "OK". If you see a "Fault" status, check your connection parameters. If you see "Missing", ensure that the device is powered on and connected to the network.

#### Details

Provides information on the connected device such as MAC address, IP address, and MCU version..

#### Save as Default

Forces the device to save its current settings as the new power-on defaults.

### Input Settings

The controls in this section relate to the analog inputs on the A4FLEX. The number of shown inputs (from two to four) varies depending on the Flex I/O 3 and 4 properties.

#### Peak Input

Only active if metering enabled. Indicates the level of signal on each input.

#### Phantom Pwr

Indicates and sets the phantom power state for each input. When enabled, phantom power is turned on.

#### Pad

Button for indicates and sets the pad state. Padding adds additional attenuation to the input signal, which allows the input to accept a larger analog signal.

#### Invert

Applies or removes a 180 degree phase adjustment to the audio signal.

#### Preamp Gain

Knob indicates and sets the current hardware preamp gain level for each input, from -8dB to +36dB.

#### Mute

Button indicates and sets the mute state for each input. When enabled, the mute is active.

### Flex I/O Settings

Controls in this section relate to the Flex I/O on the A4FLEX. The text in parentheses after the channel number indicates if the channel is configured as an input (In) or an output (Out).

#### Peak Output

Only active if metering is enabled. Indicates the level of signal on each output.

#### Phantom Pwr

Only visible for channels set as inputs. Button indicates and sets the phantom power state for each input.

#### Input Pad

For Flex inputs only, this button indicates and sets the pad state. Padding adds attenuation to the input signal to a Line level, which allows the input to accept a larger analog signal.

#### Output Pad

For Flex outputs only, this button indicates and sets the pad state. Activating the output pad attenuates the output to a mic level.

#### Invert

For Flex inputs only, applies or removes a 180 degree phase adjustment to the audio signal.

#### Gain/Volume

Knob indicates and sets the current volume or gain.

* If the channel is an input, the knob represents gain so is colored dark blue and has a range from -8 to +36dB.
* If the channel is an output, the knob represents volume so is colored light blue and has a range from 0 to -100dB.

#### Mute

Button indicates and sets the mute state for each channel. When enabled, the mute is active.

### Amplifier Settings

Controls in this section relate to the speaker outputs on the A4FLEX.

**Note:** Speaker output controls are only available if the device is powered using either an external supply or PoE+ (IEEE 802.3at). If the device is powered using standard PoE (IEEE802.3af), the amplifier outputs are shut off and the controls in the extension are disabled.

#### Peak Output

Only active if metering enabled. Indicates the level of signal on each output.

#### Fault

Indicates that the A4FLEX has detected an amplifier fault on one or more of its amplifier channels, such as over-temperature or a short.

#### Volume

Knob indicates and sets the current input gain level for each input, from 0 to -100dB.

#### Mute Button

Indicates and sets the mute state for each input. When enabled, the mute is active.

### Logic Setup

The state of each logic input and output are shown in this section. The input state is passed from the unit to the extension, which drives the state of the extension's Logic In control pins. Conversely, the logic output pins drive the state of the outputs on the unit.

#### Inputs

Indicates of current input states.

#### Output A

Indicates the current state of all output As.

#### Output B

Indicates the current state of all output Bs.

### USB Settings

The USB tab includes sections for controlling the USB inputs and outputs.

#### Peak Input/Peak Output

Only active if metering is enabled. Indicates the level of signal on each channel.

#### Clip

Only active if metering is enabled. Indicates if the channel is clipping.

#### Invert

For USB input only, applies or removes a 180 degree phase adjustment to the audio signal.

#### Gain

Knob indicates and sets the current gain level for each USB input and output channel, from +20 to -100dB.

**Note:** The USB gain controls do not change any settings on the device to which the USB port is connected. These controls set internal values within the the A4FLEX only.

#### Mute

Button indicates and sets the mute state for each USB input and output channel. When enabled, the mute is active.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Amp | | | | |
| Gain | | | | |
| 1, 2 | -100 to 20 | -100dB to 20dB | 0.00 to 1.00 | Input / Output |
| Meter | | | | |
| 1, 2 | (indicator) | | | Output |
| Mute | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Fault | 0  1 | false  true | 0  1 | Output |
| Device | | | | |
| Connected | 0  1 | false  true | 0  1 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Metering | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Flex | | | | |
| In Gain | | | | |
| 3, 4 | -8 to 36 | -8dB to 36dB | 0.00 to 1.00 | Input / Output |
| In Pad | | | | |
| 3, 4 | 0  1 | false  true | 0  1 | Input / Output |
| Invert | | | | |
| 3, 4 | 0  1 | false  true | 0  1 | Input / Output |
| Meter | | | | |
| 3, 4 | (indicator) | | | Output |
| Mute | | | | |
| 3, 4 | 0  1 | false  true | 0  1 | Input / Output |
| Out Gain | | | | |
| 3, 4 | -100 to 0 | -100dB to 0dB | 0.00 to 1.00 | Input / Output |
| Out Pad | | | | |
| 3, 4 | 0  1 | false  true | 0  1 | Input / Output |
| Phantom Pwr | | | | |
| 3, 4 | 0  1 | false  true | 0  1 | Input / Output |
| Input | | | | |
| Gain | | | | |
| 1, 2 | -8 to 36 | -8dB to 36dB | 0.00 to 1.00 | Input / Output |
| Invert | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Meter | | | | |
| 1, 2 | (indicator) | | | Output |
| Mute | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Pad | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Phantom Pwr | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Logic In |  |  |  |  |
| 1-4 | 0  1 | false  true | 0  1 | Output |
| Logic Out A |  |  |  |  |
| 1-4 | 0  1 | false  true | 0  1 | Input |
| Logic Out B |  |  |  |  |
| 1-4 | 0  1 | false  true | 0  1 | Input |
| USB Input |  |  |  |  |
| Gain | | | | |
| 1, 2 | -100 to 20 | -100dB to 20dB | 0.00 to 1.00 | Input / Output |
| Invert | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Meter | | | | |
| 1, 2 | (indicator) | | | Output |
| Mute | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| USB Output | | | | |
| Gain | | | | |
| 1, 2 | -100 to 20 | -100dB to 20dB | 0.00 to 1.00 | Input / Output |
| Meter | | | | |
| 1, 2 | (indicator) | | | Output |
| Mute | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Disable[1](#Use) | 0  1 | disabled  enabled | 0  1 | Input / Output |

###### 1. Use this control pin to enable or disable the extension in your design. When Disabled is set to enabled (value of 1), the Connection Status changes to "Not Present - Disabled".

[Troubleshooting Tips](javascript:void(0))

See the Q-SYS Knowledge Base for A4FLEX troubleshooting information:

[Troubleshooting: A4FLEX Extension Error - Fault - Invalid I/O CFG](https://support.qsys.com/troubleshooting/troubleshooting-a4flex-extension-error-fault-invalid-i-o-cfg)
