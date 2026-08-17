# Attero Tech Synapse D16Mio

> Source: https://help.qsys.com/Content/Schematic_Library/Attero_Tech_extension_D16Mio.htm

# Attero Tech Synapse D16Mio

Use this extension to connect to and control a Synapse D16Mio Danteâ¢/AES67 networked audio interface (Attero Tech by QSC).

**Note:** See the [Synapse D16Mio product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/attero-tech/at-rack-mount-network-audio-interfaces/synapse-d16mio/) on the QSC website for product information and documentation.

[Compatibility](javascript:void(0))

The extension is compatible with Q-SYS Designer version 8.4 and above and Attero Tech firmware version 1.1.0 and above. For best results, use the latest Attero Tech firmware.

[Connection Setup](javascript:void(0))

To begin using the extension:

1. Drag it into the schematic.
2. Configure the extension properties. See [Properties](#Properti).
3. Press F5 to save your design to the Core and run it.
4. In the NIC field, select the interface through which the extension will communicate to control the device.
5. In the IP field, specify the IP address of the device and press Enter.

The extension automatically attempts a connection. The "Connected" LED glows green once a connection is established. If the extension loses its connection to the device, it will attempt to re-establish the connection every 5 seconds.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Show Debug

Select 'Yes' to show the Debug Output window. For details, see [Debug Output](debug_output.htm).

[Controls](javascript:void(0))

#### Refresh

Although the extension monitors the device settings for changes automatically, this button manually triggers the extension to retrieve the current settings and update the extension values to match.

#### Meters

Enables metering within the extension. The extension polls for metering and clipping information 10 times per second for each channel. The metering function remains active until manually turned off. Click the button to toggle between states.

#### Identify

Causes the power LED on the front of the device to start blinking so it can easily be identified. The identify function remains active until manually turned off. Click the button to toggle between states.

#### Status

Normally, this shows "Initializing" for a few moments after starting your design, followed by "OK". If you see a "Fault" status, check your connection parameters. If you see "Missing", ensure that the device is powered on and connected to the network.

#### Details

Provides information on the connected device such as IP address, MCU version, and the FPGA version.

### Panel Controls

#### Mute All / Unmute All

Click Mute All to activate the mute function on all 16 inputs and 16 outputs simultaneously. Click Unmute All to deactivate muting. Note that individual mute states are not maintained when using these functions.

#### Front Panel Lock

Click to prevent users from changing the monitoring settings from the D16Mio front panel. The monitor facility is then locked to whatever channel is selected when the lock is applied.

#### Meter Mode

Click to set the metering point for the output meters:

* Pre-: Meter indicates the audio level before output control settings are applied.
* Post: Meter indicates the audio level after the output control settings are applied.

#### Display Timeout

Adjust the time of inactivity before the D16Mio display goes into sleep mode, from 10 to 360 seconds. Default = 30 seconds.

### Inputs

#### Channel Mute

Each input has its own mute. Click the button to change the mute state:

* Dark red indicates the mute is inactive.
* Bright red indicates the mute is active.

#### P48V Phantom Power

Each input has its own P48V phantom power option. Click the button to change the state:

* Dark red indicates that phantom power is inactive.
* Pink indicates that phantom power is active.

#### Mic/Line Level Input Selector

Each input has its own mic/line level input selector. Click the button to change the state:

* Dark blue indicates that the Mic input is selected.
* Light blue indicates that the Line input is selected.

#### Pre-amp Gain

Each input has its own gain control. From the drop-down menu, select the desired input level. The pre-amp gain is adjustable from a minimum of 0dB to a maximum of 51dB in 3dB increments.

### Outputs

#### Channel Invert

Click to apply a 180Â° phase shift to the output signal.

* Dark yellow indicates the invert is inactive.
* Bright yellow indicates the mute is active.

#### Channel Mute

Click to change the mute state:

* Dark red indicates the mute is inactive.
* Bright red indicates the mute is active.

#### Channel Volume

Adjust the volume from a minimum of -60dB to a maximum of 0dB.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Device | | | | |
| Connected | 0  1 | false  true | 0  1 | Output |
| Dante Lock | 0  1 | false  true | 0  1 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Metering | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Input | | | | |
| Clip | | | | |
| 1-16 | 0  1 | false  true | 0  1 | Output |
| Gain | | | | |
| 1-16 | - | 0dB, 3dB, 6dB, 9dB, 12dB, 15dB, 18dB, 21dB, 24dB, 27dB, 30dB, 33dB, 36dB, 39dB, 42dB, 45dB, 48dB, 51dB | - | Input / Output |
| Meter | | | | |
| 1-16 | (indicator) | | | Output |
| Mic Mode | | | | |
| 1-16 | 0  1 | false  true | 0  1 | Input / Output |
| Mute | | | | |
| 1-16 | 0  1 | false  true | 0  1 | Input / Output |
| Phantom Power | | | | |
| 1-16 | 0  1 | false  true | 0  1 | Input / Output |
| Output |  | | | |
| Clip |  | | | |
| 1-16 | 0  1 | false  true | 0  1 | Output |
| Invert |  | | | |
| 1-16 | 0  1 | false  true | 0  1 | Input / Output |
| Meter |  | | | |
| 1-16 | (indicator) | | | Output |
| Mute |  | | | |
| 1-16 | 0  1 | false  true | 0  1 | Input / Output |
| Volume |  | | | |
| 1-16 | -60 to 0 | -60 to 0 | 0.00 to 1.00 | Input / Output |
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
