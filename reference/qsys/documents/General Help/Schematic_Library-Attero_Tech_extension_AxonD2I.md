# Attero Tech Axon D2i

> Source: https://help.qsys.com/Content/Schematic_Library/Attero_Tech_extension_AxonD2I.htm

# Attero Tech Axon D2i

Use this extension to connect to and control the Axon D2i Dante/AES67 network audio I/O wallplate (Attero Tech by QSC).

**Note:** See the [Axon D2i product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/attero-tech/at-wall-mount-network-audio-interfaces/axon-d2i/) on the QSC website for product information and documentation.

[Compatibility](javascript:void(0))

The extension is compatible with Q-SYS Designer version 8.4 and above. For best results, use the latest Attero Tech device firmware.

[Connection Setup](javascript:void(0))

1. In the NIC field, select the interface through which the extension will communicate to control the device.
2. In the IP field, specify the IP address of the device and press Enter.

The extension will automatically attempt a connection. The "Connected" LED glows green once a connection is established. If the extension loses its connection to the device, it will attempt to re-establish the connection every 5 seconds.

**Note:** If Dante Lock is active on the connected device, you will see a padlock icon next to the device name.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### AXIOM Enable

Allows D2i to support additional resources via its AXIOM port connection. Default = No.

#### AXIOM Baud Rate

Set the baud rate for serial communication with the device connected to the AXIOM port. Default = 9600.

#### Status LEDs

Turn on or off the front panel status LEDs. Default = Yes.

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

### Input Settings

#### Phantom Power

Selects the state of phantom power for the input. If the button is purple, the phantom power is inactive. If itâs pink, the phantom power is active. Click the button to toggle between states.

#### Input Gain

Selects the gain level for the input, from -8dB to 36dB.

#### Mute

Selects whether the mute is active on the input. If the button is dark red, the mute is off. If light red, the mute is active. Click the button to toggle between states.

### AXIOM In / AXIOM Out

#### Signal Indicator

LED for each channel. Only active when metering is enabled.

* Green = signal
* Grey = no signal (<60dB)
* Red = clipping

#### Dante Name

The name of the channel as displayed in Dante Controller.

#### Mute

Allows muting of an output. If the button is grey, the mute is inactive. If itâs orange, the mute is active. Click the button to toggle between states.

### Dante Out

#### Dante Name

Indicates the name of the channel as displayed in Dante Controller.

#### Mixer Controls

Allows mixing of the local XLR inputs and audio from the AXIOM input. Values are from -100dB to 0dB.

#### Signal Indicator

LED for each Dante output. Only active when metering is enabled.

* Green = signal
* Grey = no signal (<60dB)
* Red = clipping

### Device

#### Low Power Mode

Indicator shows the state of the low power mode.

**Note:** The extension loses connection if low power mode is engaged and the unit times out. The connection is restored if an audio signal is detected.

#### Auto Mute

Indicator shows the setting for auto mute.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| AXIOM | | | | |
| Input | | | | |
| Mute | 0  1 | false  true | 0  1 | Input / Output |
| Signal Presence | 0  1 | false  true | 0  1 | Output |
| Output | | | | |
| Mute | 0  1 | false  true | 0  1 | Input / Output |
| Signal Presence | 0  1 | false  true | 0  1 | Output |
| Dante Out | | | | |
| Signal Presence | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Output |
| Device | | | | |
| Connected | 0  1 | false  true | 0  1 | Output |
| Dante Lock | 0  1 | false  true | 0  1 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Metering | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Input | | | | |
| Gain | | | | |
| 1, 2 | -8 to 36 | -8dB to 36dB | 0.00 to 1.00 | Input / Output |
| Mute | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Phantom Pwr | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Mixer |  |  |  |  |
| In1Out1 | -100 to 0 | -100 to 0 | 0.00 to 1.00 | Input / Output |
| In1Out2 | -100 to 0 | -100 to 0 | 0.00 to 1.00 | Input / Output |
| In2Out1 | -100 to 0 | -100 to 0 | 0.00 to 1.00 | Input / Output |
| In2Out2 | -100 to 0 | -100 to 0 | 0.00 to 1.00 | Input / Output |
| InAxiomOut1 | -100 to 0 | -100 to 0 | 0.00 to 1.00 | Input / Output |
| InAxiomOut2 | -100 to 0 | -100 to 0 | 0.00 to 1.00 | Input / Output |
| Auto Mute | (text) | | | Output |
| Disable[1](#Use) | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Low Power Mode | (text) | | | Output |

###### 1. Use this control pin to enable or disable the extension in your design. When Disabled is set to enabled (value of 1), the Connection Status changes to "Not Present - Disabled".
