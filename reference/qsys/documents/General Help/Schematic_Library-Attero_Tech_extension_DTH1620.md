# Attero Tech DTH1620

> Source: https://help.qsys.com/Content/Schematic_Library/Attero_Tech_extension_DTH1620.htm

# Attero Tech DTH1620

Use this extension to connect to and control the DTH1620 Dante/AES67 network amplifier (Attero Tech by QSC).

**Note:** See the [Axon DTH1620 product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/attero-tech/attero-tech-network-amplifiers/axon-dth1620/) on the QSC website for product information and documentation.

[Compatibility](javascript:void(0))

The extension is compatible with Q-SYS Designer version 8.4 and above. For best results, use the latest [Attero Tech firmware](https://www.qsys.com/index.php?id=16390).

[Connection Setup](javascript:void(0))

1. In the NIC field, select the interface through which the extension will communicate to control the device.
2. In the IP field, specify the IP address of the device and press Enter.

The extension will automatically attempt a connection. The "Connected" LED glows green once a connection is established. If the extension loses its connection to the device, it will attempt to re-establish the connection every 5 seconds.

**Note:** If Dante Lock is active on the connected device, you will see a padlock icon next to the device name.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Headphone Limit

Set the maximum volume for headphone output, from -103 to 24dB.

#### Show Debug

Select 'Yes' to show the Debug Output window. For details, see [Debug Output](debug_output.htm).

[Controls](javascript:void(0))

#### Device Name

Appears just below the company logo, if available from the connected device. If the extension cannot retrieve the name, the field remains blank.

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

Provides information on the connected device such as MAC address, IP address, and MCU version.

### Common Settings

These controls relate to the eight analog inputs on the DTH1620.

#### Temp

Shows the values of the internal temperature sensors in degrees Celsius.

#### Fan

Toggles the cooling fan on or off.

#### Master Mute

Toggles muting of the master output.

#### Master Volume

Knob indicates and sets the current master volume, from -103 to 24.

### Output Settings

These controls relate to the eight analog outputs on the DTH1620.

#### Channel Name

Read-only field show the current Dante receive channel name.

#### Meter

Only active if metering enabled. Indicates the level of signal on each output.

#### Gain

Knob indicates and sets the output gain, from -127 to 0.

#### Mute

Mutes the audio for a channel. Click the button to toggle the state.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Device | | | | |
| Connected | 0  1 | false  true | 0  1 | Output |
| Dante Lock | 0  1 | false  true | 0  1 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Metering | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Gain |  |  |  |  |
| 1-16 | -127 to 0 | -127 to 0 | 0.00 to 1.00 | Input / Output |
| Meter | | | | |
| 1-16 | (indicator) | | | Output |
| Mute | | | | |
| 1-16 | 0  1 | false  true | 0  1 | Input / Output |
| Disable[1](#Use) | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Fan Enable | 0  1 | false  true | 0  1 | Input / Output |
| Master Mute | 0  1 | false  true | 0  1 | Input / Output |
| Master Volume | -103 to 24 | -103 to 24 | 0.00 to 1.00 | Input / Output |

###### 1. Use this control pin to enable or disable the extension in your design. When Disabled is set to enabled (value of 1), the Connection Status changes to "Not Present - Disabled".
