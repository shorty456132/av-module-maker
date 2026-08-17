# Attero Tech Axon A8Mio

> Source: https://help.qsys.com/Content/Schematic_Library/Attero_Tech_extension_AxonA8Mio.htm

# Attero Tech Axon A8Mio

Use this extension to connect to and control the Axon A8Mio AES67 network audio I/O endpoint (Attero Tech by QSC).

**Note:** See the [Axon A8Mio product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/attero-tech/at-surface-mount-network-audio-interfaces/axon-a8mio/) on the QSC website for product information and documentation.

[Compatibility](javascript:void(0))

The extension is compatible with Q-SYS Designer version 8.4 and above and Attero Tech firmware version 2.2.1.1 and above. For best results, use the latest Attero Tech firmware.

[Connection Setup](javascript:void(0))

1. In the NIC field, select the interface through which the extension will communicate to control the device.
2. In the IP field, specify the IP address of the device and press Enter.

The extension will automatically attempt a connection. The "Connected" LED glows green once a connection is established. If the extension loses its connection to the device, it will attempt to re-establish the connection every 5 seconds.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Show Debug

Select 'Yes' to show the Debug Output window. For details, see [Debug Output](debug_output.htm).

[Controls](javascript:void(0))

#### Refresh

Although the extension monitors the device settings for changes automatically, this button manually triggers the extension to retrieve the current settings and update the extension values to match.

#### Meters

Enables metering within the extension. The extension polls for metering information once a second and updates signal presence indicators and Dante Rx status for each channel accordingly. The metering function remains active until manually turned off. Click the button to toggle between states.

#### Identify

Causes the power LED on the front of the device to start blinking so it can easily be identified. The identify function remains active until manually turned off. Click the button to toggle between states.

#### Status

Normally, this shows "Initializing" for a few moments after starting your design, followed by "OK". If you see a "Fault" status, check your connection parameters. If you see "Missing", ensure that the device is powered on and connected to the network.

#### Details

Provides information on the connected device such as MAC address, IP address, firmware version, power type, and the data model version.

#### Save as Default

Forces the device to save its current settings as the new power-on defaults.

### Input Settings

The controls in this section relate to the eight analog inputs on the A8Mio.

#### Peak Input

Only active if metering enabled. Indicates the level of signal on each input.

#### Clip

Only active if metering enabled. Indicates if input is clipping.

#### Phantom Power

Indicates and sets the phantom power state for each input. When enabled, phantom power is turned on.

#### Pad

Button for indicates and sets the pad state. Padding adds additional attenuation to the input signal, which allows the input to accept a larger analog signal.

#### Preamp Gain

Knob indicates and sets the current hardware preamp gain level for each input, from -8dB to +36dB.

#### Mute

Button indicates and sets the mute state for each input. When enabled, the mute is active.

### Output Settings

Controls in this section relate to the eight analog outputs on the A8Mio.

#### Peak Output

Only active if metering enabled. Indicates the level of signal on each output.

#### Clip

Only active if metering is enabled. Indicates if output is clipping.

#### Pad

Button indicates and sets the pad state for outputs 1 and 2 only. The button legend indicates âMicâ and activates the output pad, which attenuates the output to a mic level.

#### Gain

Knob indicates and sets the current gain, from 0 to -100dB.

#### Mute

Button indicates and sets the mute state for each channel. When enabled, the mute is active.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Device | | | | |
| Connected | 0  1 | false  true | 0  1 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Metering | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Input | | | | |
| Clip | | | | |
| 1-8 | 0  1 | false  true | 0  1 | Output |
| Gain | | | | |
| 1-8 | -8 to 36 | -8dB to 36dB | 0.00 to 1.00 | Input / Output |
| Meter | | | | |
| 1-8 | (indicator) | | | Output |
| Mute | | | | |
| 1-8 | 0  1 | false  true | 0  1 | Input / Output |
| Pad | | | | |
| 1-8 | 0  1 | false  true | 0  1 | Input / Output |
| Phantom Pwr | | | | |
| 1-8 | 0  1 | false  true | 0  1 | Input / Output |
| Output |  | | | |
| Clip |  | | | |
| 1-8 | 0  1 | false  true | 0  1 | Output |
| Gain |  | | | |
| 1-8 | 0 to -100 | 0 to -100dB | 0.00 to 1.00 | Input / Output |
| Meter |  | | | |
| 1-8 | (indicator) | | | Output |
| Mute |  | | | |
| 1-8 | 0  1 | false  true | 0  1 | Input / Output |
| Pad | | | | |
| 1-2 | 0  1 | false  true | 0  1 | Input / Output |
| Disable[1](#Use) | 0  1 | disabled  enabled | 0  1 | Input / Output |

###### 1. Use this control pin to enable or disable the extension in your design. When Disabled is set to enabled (value of 1), the Connection Status changes to "Not Present - Disabled".
