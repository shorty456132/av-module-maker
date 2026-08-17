# Attero Tech unD6IO-BT

> Source: https://help.qsys.com/Content/Schematic_Library/Attero_Tech_extension_unD6IOBT.htm

# Attero Tech unD6IO-BT

Use this extension to connect to and control a unD6IO-BT Danteâ¢ Networked Audio Wall Plate (Attero Tech by QSC).

**Note:** See the [unD6IO-BT product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/attero-tech/at-wall-mount-network-audio-interfaces/und6io-bt/) on the QSC website for product information and documentation.

[Compatibility](javascript:void(0))

The extension is compatible with Q-SYS Designer version 8.4 and above and Attero Tech firmware version 4.7.0 and above. For best results, use the latest Attero Tech firmware.

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

### Bluetooth Settings

#### Signal Indicator

Shown in top right corner of each Bluetooth channel. Only active when metering is enabled.

* Green = signal
* Grey = no signal (<60dB)
* Red = clipping

#### Dante Tx Name

The name of the channel as displayed in Dante Controller.

#### Clear Pairings

Click to clear the list of pairings on the device.

#### Pair/Connect or Disconnect

If the Bluetooth interface is idle, click Pair/Connect to initiate a pair cycle. If the device is connected, click Disconnect to end the Bluetooth connection.

#### Friendly Name

While Bluetooth is disconnected, optionally change the device name that is used when pairing, and then click Apply.

#### Connect Mode

Select how previously-paired Bluetooth devices reconnect:

* Manual: Requires that the unD6IO-BT is put in pairing mode to reconnect.
* Reconnect: If an external Bluetooth device has connected before, allows that device to reconnect without the unD6IO-BT to be in pairing mode.
* Exclusive: Allows only a single device to be paired and reconnect. Pairing attempts by other devices will fail.

#### Audio Mode

Select the type of audio for the Bluetooth connection:

* Media Bridging: Allows only media audio to pass via the Bluetooth interface. Call audio remains local to the connected device.
* Call Bridging: Allows call audio to pass via the Bluetooth interface while other audio remains local to the device.
* Media and Call Bridging: All audio is allowed to pass via the Bluetooth interface.

#### Front Panel Pair Button

Toggles functionality of the front panel Pair button. Disable the Pair button when you require a control system to initiate pairing remotely.

#### Signal Strength

Indicates the current Bluetooth signal strength, both in color and value:

* Green = Good
* Yellow = Average
* Red = Poor

**Note:** This control only functions with Attero Tech firmware v4.10.0 and later.

#### Status

Text field indicates the current Bluetooth status. Each status also has a numeric value when using the Status control pin â see [Control Pins](#Control).

* Idle
* Discoverable
* Connected (Unknown)
* Connected (No AVRCP)
* Connected (AVRCP)
* Connected (AVRCP + PDU)

#### Audio Details

If the connected Bluetooth device supports PDU data, it will pass certain information to the extension. This includes the device friendly name and the details of any audio that is currently being played.

#### AVCRP Controls

If the connected Bluetooth device supports AVRCP, the extension can control media playing on the connected device. These controls include Stop, Pause, Play, Next Track, Previous Track, Mute, and Volume Up and Down.

### Input Settings

#### Signal Indicator

Shown in top right corner of each channel. Only active when metering is enabled.

* Green = signal
* Grey = no signal (<60dB)
* Red = clipping

#### Dante Tx Name

The name of the channel as displayed in Dante Controller.

#### Input Select

For channels 3 and 4 only, select what unbalanced audio input is made available to the Dante network. You can select the RCA, 3.5mm jack, or a mix of both for left and right audio:

* A [RCA]
* B [3.5mm]
* A+B [Both]

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
| Bluetooth | | | | |
| Album | (text) | | | Output |
| Artist | (text) | | | Output |
| AVRCP Mute | 0  1 | false  true | 0  1 | Input / Output |
| AVRCP Next | 0  1 | false  true | 0  1 | Input / Output |
| AVRCP Pause | 0  1 | false  true | 0  1 | Input / Output |
| AVRCP Play | 0  1 | false  true | 0  1 | Input / Output |
| AVRCP Prev | 0  1 | false  true | 0  1 | Input / Output |
| AVRCP Stop | 0  1 | false  true | 0  1 | Input / Output |
| AVRCP Vol Dn | 0  1 | false  true | 0  1 | Input / Output |
| AVRCP Vol Up | 0  1 | false  true | 0  1 | Input / Output |
| BER  (Bit Error Rate) | (text) | | | Output |
| Clear Pairings | 0  1 | false  true | 0  1 | Input / Output |
| Connected Device | (text) | | | Output |
| Lock | 0  1 | false  true | 0  1 | Input / Output |
| Pair/Close | 0  1 | false  true | 0  1 | Input / Output |
| RSSI[2](#This)  (Signal Strength Indicator) | (text) | | | Output |
| Song | (text) | | | Output |
| Status | 0  1  2  3  4  5 | Idle  Discoverable  Connected (Unknown)  Connected (No AVRCP)  Connected (AVRCP)  Connected (AVRCP + PDU) | - | Output |
| Dante Rx State | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Output |
| Device | | | | |
| Connected | 0  1 | false  true | 0  1 | Output |
| Dante Lock | 0  1 | false  true | 0  1 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Metering | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Input Select | | | | |
| 1, 2 | - | A [RCA]  B [3.5mm]  A+B [Both] | - | Input / Output |
| Input Signal Presence | | | | |
| 1, 2, 3, 4 | 0  1 | false  true | 0  1 | Output |
| Output Mute | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Output Signal Presence | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Output |
| Output Volume | | | | |
| 1, 2 | -60 to 0 | -60dB to 0dB | 0.00 to 1.00 | Input / Output |
| Disable[1](#Use) | 0  1 | disabled  enabled | 0  1 | Input / Output |

###### 1. Use this control pin to enable or disable the extension in your design. When Disabled is set to enabled (value of 1), the Connection Status changes to "Not Present - Disabled".

###### 2. This control pin only functions with Attero Tech firmware v4.10.0 and later.

[Troubleshooting](javascript:void(0))

### All controls are locked and disabled

If you've successfully connected to the device but all of the controls are locked and disabled, this means that parameter locking is enabled in the unIFY app. To use the extension, disable the parameter lock in unIFY.

### "Missing - Invalid IP" status message

If you see this fault message, check that you've selected the correct NIC and that you've specified the correct IP address of the Attero Tech device.
