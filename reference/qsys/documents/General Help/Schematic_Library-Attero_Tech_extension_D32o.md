# Attero Tech Synapse D32o

> Source: https://help.qsys.com/Content/Schematic_Library/Attero_Tech_extension_D32o.htm

# Attero Tech Synapse D32o

Use this extension to connect to and control the Synapse D32o Danteâ¢/AES67 Networked Audio Interface (Attero Tech by QSC).

**Note:** See the [Synapse D32o product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/attero-tech/at-rack-mount-network-audio-interfaces/synapse-d32o/) on the Attero Tech website for product information and documentation.

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

Prevents users from changing the monitoring settings from the front panel of the D32o. When enabled, the monitor facility is locked to whatever channel was selected when the lock is applied.

#### Meter Mode

Click to set the metering point for the output meters:

* Pre-: Meter indicates the audio level before output control settings are applied.
* Post: Meter indicates the audio level after the output control settings are applied.

#### Display Timeout

Adjusts the time of inactivity before the D32o display goes into sleep mode. The default setting is 30 seconds.

### Output Settings

#### Metering

The D32o extension reflects the pre-output metering. The pre-metering shows the levels of the audio signals received directly from the Danteâ¢ flows prior to any level adjustments made in the extension.

#### Channel Invert

Each output has its own invert option. Dark yellow means the signal is not inverted and bright yellow indicates the signal is inverted. Click the button to change the invert state.

#### Channel Mute

Each output has its own mute. Click the button to change the mute state:

* Dark red indicates the mute is inactive.
* Bright red indicates the mute is active.

#### Channel Volume

Each output has its own volume control. Click and drag to adjust from a minimum of -60dB to a maximum of 0dB.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Device | | | | |
| Connected | 0  1 | false  true | 0  1 | Output |
| Dante Lock | 0  1 | false  true | 0  1 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Metering | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Meter | | | | |
| 1-32 | (indicator) | | | Output |
| Output Clip | | | | |
| 1-32 | 0  1 | false  true | 0  1 | Output |
| Output Invert | | | | |
| 1-32 | 0  1 | false  true | 0  1 | Input / Output |
| Output Mute | | | | |
| 1-32 | 0  1 | false  true | 0  1 | Input / Output |
| Volume |  | | | |
| 1-32 | -60 to 0 | -60 to 0 | 0.00 to 1.00 | Input / Output |
| Disable[1](#Use) | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Display Timeout | 10 to 360 | 10 to 360 | 0.00 to 1.00 | Input / Output |
| Front Panel Lock | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Meter Mode | - | Pre-  Post | - | Input / Output |
| Mute All | 0  1 | false  true | 0  1 | Input |
| Unmute All | 0  1 | false  true | 0  1 | Input |

###### 1. Use this control pin to enable or disable the extension in your design. When Disabled is set to enabled (value of 1), the Connection Status changes to "Not Present - Disabled".

[Troubleshooting](javascript:void(0))

### "Missing - Invalid IP" status message

If you see this fault message, check that you've selected the correct NIC and that you've specified the correct IP address of the Attero Tech device.
