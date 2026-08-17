# Attero Tech unDIO2x2+

> Source: https://help.qsys.com/Content/Schematic_Library/Attero_Tech_extension_unDIO2x2plus.htm

# Attero Tech unDIO2x2+

Use this extension to connect to and control a unDIO2x2+ Danteâ¢ network audio interface (Attero Tech by QSC).

**Note:** See the [unDIO2x2+ product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/attero-tech/at-surface-mount-network-audio-interfaces/undio2x2/) on the QSC website for product information and documentation.

[Compatibility](javascript:void(0))

The extension is compatible with Q-SYS Designer version 8.4 and above and Attero Tech firmware version 4.2.0 and above.

[Connection Setup](javascript:void(0))

1. In the NIC field, select the interface through which the extension will communicate to control the device.
2. In the IP field, specify the IP address of the device and press Enter.

The extension will automatically attempt a connection. The "Connected" LED glows green once a connection is established. If the extension loses its connection to the device, it will attempt to re-establish the connection every 5 seconds.

**Note:** If Dante Lock is active on the connected device, you will see a padlock icon next to the device name.

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

Provides information on the connected device such as MAC address, IP address, MCU version, and parameter lock state.

#### Save as Default

Forces the device to save its current settings as the new power-on defaults.

### Input Settings

#### Signal Indicator

Shown in top right corner of each channel. Only active when metering is enabled.

* Green = signal
* Grey = no signal (<60dB)
* Red = clipping

#### Dante Tx Name

The name of the channel as displayed in Dante Controller.

#### Input Gain

Selects the gain level for the input. Options are:

* Line (0 dB)
* +15 dB
* Low Mic (+30 dB)
* High Mic (+45 dB)

#### Input Pad

Selects whether the input pad is active on the input. If the button is grey, the pad is off. If itâs orange, the pad is active (-12dB attenuation). Click the button to toggle between states.

#### Phantom Power

Selects the state of phantom power for the input. If the button is grey, the phantom power is inactive. If itâs orange, the phantom power is active. Click the button to toggle between states.

### Output Settings

#### Signal Indicator

Shown in top right corner of each channel. Only active when metering is enabled.

* Green = signal
* Grey = no signal (<60dB)
* Red = clipping

#### Dante Rx Name

The name of the channel as displayed in Dante Controller.

#### Volume

Sets the output volume on each output. Click and drag to adjust from a minimum of -60dB to a maximum of 0dB.

#### Mute

Allows muting of an output. If the button is grey, the mute is inactive. If itâs orange, the mute is active. Click the button to toggle between states.

#### Dante Rx Indicator

Active only when metering is enabled. Shows the state of the Dante connection. Use Dante Controller to investigate any errors or warnings.

* Green = connected and OK
* Grey = no connection
* Red = connection error
* Yellow = connection warning

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Dante Rx State | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Output |
| Device | | | | |
| Connected | 0  1 | false  true | 0  1 | Output |
| Dante Lock | 0  1 | false  true | 0  1 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Metering | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Input Gain | | | | |
| 1, 2 | - | Line (0 dB)  +15 dB  Low Mic (+30 dB)  High Mic (+45 dB) | - | Input / Output |
| Input Pad | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Input Signal Presence | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Output |
| Output Mute | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Output Signal Presence | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Output |
| Output Volume | | | | |
| 1, 2 | -60 to 0 | -60dB to 0dB | 0.00 to 1.00 | Input / Output |
| Phantom Power | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Disable[1](#Use) | 0  1 | disabled  enabled | 0  1 | Input / Output |

###### 1. Use this control pin to enable or disable the extension in your design. When Disabled is set to enabled (value of 1), the Connection Status changes to "Not Present - Disabled".

[Troubleshooting](javascript:void(0))

If you've connected to the device but all of the controls are locked and disabled, this means that parameter locking is enabled in the unIFY app. To use the extension, disable the parameter lock in unIFY.
