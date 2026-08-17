# Attero Tech Synapse D32i

> Source: https://help.qsys.com/Content/Schematic_Library/Attero_Tech_extension_D32i.htm

# Attero Tech Synapse D32i

Use this extension to connect to and control the Synapse D32 Danteâ¢/AES67 networked audio interface.

**Note:** See the [Synapse D32i product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/attero-tech/at-rack-mount-network-audio-interfaces/synapse-d32i/) on the QSC website for product information and documentation.

[Compatibility](javascript:void(0))

The extension is compatible with Q-SYS Designer version 8.4 and above and Attero Tech firmware version 1.1.0 and above. For best results, use the latest Attero Tech firmware.

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

### Panel Controls

#### Mute All / Unmute All

Activates or deactivates the mute function on all 32 outputs simultaneously. Individual mute states are not maintained when these functions are used.

#### Front Panel Lock

Prevents users from changing the monitoring settings from the front panel of the D32i. When enabled, the monitor facility is locked to whatever channel was selected when the lock is applied.

#### Display Timeout

Adjusts the time of inactivity before the D32i display goes into sleep mode. The default setting is 30 seconds.

### Input Settings

#### Bank Pad Control

The 32 inputs are split into two banks. Each bank has a pad control to set the input level. The pad setting applies to all inputs in the bank and cannot be set individually for each input. Turn the pad on to set nominal +4dBu (pro) input levels or turn it off for nominal -10dBV (consumer) input levels.

#### Channel Mute

Each output has its own mute. Click the button to change the mute state:

* Dark red indicates the mute is inactive.
* Bright red indicates the mute is active.

#### Metering

The meters show the levels of the audio signals sent via Danteâ¢/AES67 flows.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Bank Pad | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Device | | | | |
| Connected | 0  1 | false  true | 0  1 | Output |
| Dante Lock | 0  1 | false  true | 0  1 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Metering | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Input | | | | |
| Clip | | | | |
| 1-32 | 0  1 | false  true | 0  1 | Output |
| Meter | | | | |
| 1-32 | (indicator) | | | Output |
| Mute | | | | |
| 1-32 | 0  1 | false  true | 0  1 | Input / Output |
| Disable[1](#Use) | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Display Timeout | 10 to 360 | 10 to 360 | 0.00 to 1.00 | Input / Output |
| Front Panel Lock | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Mute All | 0  1 | false  true | 0  1 | Input |
| Unmute All | 0  1 | false  true | 0  1 | Input |

###### 1. Use this control pin to enable or disable the extension in your design. When Disabled is set to enabled (value of 1), the Connection Status changes to "Not Present - Disabled".

[Troubleshooting](javascript:void(0))

### All controls are locked and disabled

If you've successfully connected to the device but all of the controls are locked and disabled, this means that parameter locking is enabled in the unIFY app. To use the extension, disable the parameter lock in unIFY.

### "Missing - Invalid IP" status message

If you see this fault message, check that you've selected the correct NIC and that you've specified the correct IP address of the Attero Tech device.
