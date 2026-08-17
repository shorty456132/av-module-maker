# Attero Tech unD3IO

> Source: https://help.qsys.com/Content/Schematic_Library/Attero_Tech_extension_unD3IO.htm

# Attero Tech unD3IO

Use this extension to connect to and control a unD3IO Dante in-wall I/O interface (Attero Tech by QSC).

**Note:** See the [Attero Tech Discontinued Products page](https://www.qsys.com/systems/support/discontinued-products/attero-tech/) on the QSC website for product information and documentation.

[Compatibility](javascript:void(0))

The extension is compatible with Q-SYS Designer version 8.4 and above and Attero Tech firmware version 4.4.0 and above. For best results, use the latest Attero Tech firmware.

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

#### Identify

Causes the power LED on the front of the device to start blinking so it can easily be identified. The identify function remains active until manually turned off. Click the button to toggle between states.

#### Status

Normally, this shows "Initializing" for a few moments after starting your design, followed by "OK". If you see a "Fault" status, check your connection parameters. If you see "Missing", ensure that the device is powered on and connected to the network.

#### Details

Provides information on the connected device such as MAC address, IP address, and MCU version.

#### Save as Default

Forces the device to save its current settings as the new power-on defaults.

### Input Settings

#### Input Gain

For channel 1 only, selects the gain level for the XLR input. Options are:

* Line (0dB)
* Low Mic (+25dB)
* High Mic (+40dB)

#### Phantom Power

For channel 1 only, selects the state of phantom power for the input. If the button is grey, the phantom power is inactive. If itâs orange, the phantom power is active. Click the button to toggle between states.

#### Input Select

Each unbalanced source is mixed down to mono. For channel 2 only, select what unbalanced audio input is made available to the Dante network. You can select the RCA, 3.5mm jack, or a mix of both:

* A [RCA]
* B [3.5mm]
* A+B [Both]

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Device | | | | |
| Connected | 0  1 | false  true | 0  1 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Disable[1](#Use) | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Input Gain | - | Line (0dB)  Low Mic (+25dB)  High Mic (+40dB) | - | Input / Output |
| Input Select | - | A [RCA]  B [3.5mm]  A+B [Both] | - | Input / Output |
| Phantom Power | 0  1 | false  true | 0  1 | Input / Output |

###### 1. Use this control pin to enable or disable the extension in your design. When Disabled is set to enabled (value of 1), the Connection Status changes to "Not Present - Disabled".
