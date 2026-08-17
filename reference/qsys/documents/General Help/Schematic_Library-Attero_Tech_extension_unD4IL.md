# Attero Tech unD4I-L

> Source: https://help.qsys.com/Content/Schematic_Library/Attero_Tech_extension_unD4IL.htm

# Attero Tech unD4I-L

Use this extension to connect to and control a unD4I-L Danteâ¢/AES67 network audio interface (Attero Tech by QSC).

**Note:** See the [unD4I-L product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/attero-tech/at-surface-mount-network-audio-interfaces/und4i-l/) on the QSC website for product information and documentation.

[Compatibility](javascript:void(0))

The extension is compatible with Q-SYS Designer version 8.4 and above and Attero Tech firmware version 4.4.0 and above. For best results, use the latest Attero Tech firmware.

[Connection Setup](javascript:void(0))

1. In the NIC field, select the interface through which the extension will communicate to control the device.
2. In the Receive Port field, specify the receiving port number to which logic input event messages are sent on the Q-SYS Core processor.

**Note:** If your design uses multiple unD4I-L extensions, each **MUST** be configured with a unique port number.

1. In the IP field, specify the IP address of the device and press Enter.

The extension will automatically attempt a connection. The "Connected" LED glows green once a connection is established. If the extension loses its connection to the device, it will attempt to re-establish the connection every 5 seconds.

**Note:** If Dante Lock is active on the connected device, you will see a padlock icon next to the device name.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Show Debug

Select 'Yes' to show the Debug Output window. For details, see [Debug Output](debug_output.htm).

[Controls](javascript:void(0))

**Note:** To ensure that device settings persist after a device power cycle, use the Save as Default control.

#### Refresh

Although the extension monitors the device settings for changes automatically, this button manually triggers the extension to retrieve the current settings and update the extension values to match.

#### Identify

Causes the power LED on the front of the device to start blinking so it can easily be identified. The identify function remains active until manually turned off. Click the button to toggle between states.

#### Status

Normally, this shows "Initializing" for a few moments after starting your design, followed by "OK". If you see a "Fault" status, check your connection parameters. If you see "Missing", ensure that the device is powered on and connected to the network.

#### Details

Provides information on the connected device such as MAC address, IP address, MCU version, and parameter lock state.

#### Save as Default

Forces the device to save its current settings as the new power-on defaults.

### Audio Configuration

#### Gain

Selects the gain level for the input. Options are:

* -12dB
* 0dB
* +3dB
* +15dB
* +18dB
* +30dB
* +33dB
* +45dB

#### Phantom

Selects the state of phantom power for the input. If the button is grey, the phantom power is inactive. If itâs orange, the phantom power is active. Click the button to toggle between states.

### Logic Monitor

#### Logic Inputs 1-4

Indicates the active logic input states. If an input is active, the indicator turns green.

#### Logic Outputs 1-4

Indicates the active logic output states. If an output is active, the indicator turns green.

**Note:** There is no "test" function for the outputs. If this is required for your configuration, use the Logic Out control pins.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Device | | | | |
| Connected | 0  1 | false  true | 0  1 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Input Gain | | | | |
| 1, 2, 3, 4 | - | -12dB  0dB  +3dB  +15dB  +18dB  +30dB  +33dB  +45dB | - | Input / Output |
| Logic In | | | | |
| 1, 2, 3, 4 | 0  1 | false  true | 0  1 | Output |
| Logic Out | | | | |
| 1, 2, 3, 4 | 0  1 | false  true | 0  1 | Input |
| Phantom Power | | | | |
| 1, 2, 3, 4 | 0  1 | false  true | 0  1 | Input / Output |
| Disable[1](#Use) | 0  1 | disabled  enabled | 0  1 | Input / Output |

###### 1. Use this control pin to enable or disable the extension in your design. When Disabled is set to enabled (value of 1), the Connection Status changes to "Not Present - Disabled".

[Troubleshooting](javascript:void(0))

### "Missing - Invalid IP" status message

If you see this fault message, check that you've selected the correct NIC and that you've specified the correct IP address of the Attero Tech device.
