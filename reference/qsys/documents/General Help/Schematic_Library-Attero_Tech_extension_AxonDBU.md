# Attero Tech Axon DBU

> Source: https://help.qsys.com/Content/Schematic_Library/Attero_Tech_extension_AxonDBU.htm

# Attero Tech Axon DBU

Use this extension to connect to and control an Axon DBU Dante/AES67 network audio interface (Attero Tech by QSC).

**Note:** See the [Axon DBU product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/attero-tech/at-surface-mount-network-audio-interfaces/axon-dbu/) on the QSC website for product information and documentation.

[Compatibility](javascript:void(0))

The extension is compatible with Q-SYS Designer version 8.4 and above. For best results, use the latest [Attero Tech firmware](https://www.qsys.com/index.php?id=16390).

[Connection Setup](javascript:void(0))

1. In the NIC field, select the interface through which the extension will communicate to control the device.
2. In the IP field, specify the IP address of the device and press Enter.

The extension will automatically attempt a connection. The "Connected" LED glows green once a connection is established. If the extension loses its connection to the device, it will attempt to re-establish the connection every 5 seconds.

**Note:** If Dante Lock is active on the connected device, you will see a padlock icon next to the device name.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### USB Mode

Sets the audio configuration of the USB interface: Speakerphone (default), Speakerphone (AEC), Speakerphone (Telephony), Speakerphone (Telephony) (AEC), and 2x2 Line In/Out.

#### USB Priority

Configure whether USB audio is prioritized over Bluetooth. When enabled and while a USB device is connected, Bluetooth audio is automatically muted.

#### BT Enable

Enable or disable (default) the BT interface.

#### BT Profile Mode

Sets the audio profile of the Bluetooth connection: Media Audio (default), Call Bridging, and Media Audio + Call Bridging.

#### BT Connect Mode

Select how previously-paired Bluetooth devices reconnect:

* Basic: (Default) Requires that the DBU is put in pairing mode to reconnect.
* Reconnect: If an external Bluetooth device has connected before, allows that device to reconnect without the DBU to be in pairing mode.
* Exclusive: Allows only a single device to be paired and reconnect. Pairing attempts by other devices will fail.

#### BT Pair Button

Toggles functionality of the front panel Pair button. Disable the Pair button when you require a control system to initiate pairing remotely.

#### Show Debug

Select 'Yes' to show the Debug Output window. For details, see [Debug Output](debug_output.htm).

[Controls](javascript:void(0))

#### Force Config

If the extension detects that the configuration of the device does not match those set in the extension, click the button to update the device settings to match.

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

#### Save as Default

Forces the device to save its current settings as the new power-on defaults.

### Bluetooth Settings

This tab is only visible when Bluetooth is enabled in the Properties pane.

#### Clear Pairings

Click to clear the list of pairings on the device.

#### Pair/Connect or Disconnect

If the Bluetooth interface is idle, click Pair/Connect to initiate a pair cycle. If the device is connected, click Disconnect to end the Bluetooth connection.

#### Friendly Name

While Bluetooth is disconnected, optionally change the device name that is used when pairing, and then click Apply.

#### Signal Strength

Indicates the current Bluetooth signal strength, both in color and value:

* Green = Good
* Yellow = Average
* Red = Poor

#### Status

Text field indicates the current Bluetooth status. Each status also has a numeric value when using the Status control pin â see [Attero Tech Axon DBU](#Control).

* Idle
* Discoverable
* Connected
* Conflict - shows when the USB Priority property is enabled and a USB device is connected.
* Error - shows when an external device that was previously connected to the DBU attempts to reconnect but the DBU no longer has that device in its "previously paired" list.

#### Audio Details

If the connected Bluetooth device supports AVRCP, it will pass certain information to the extension, such as the connected device's friendly name and details of any audio that is currently being played. This information is shown in the Audio Details section.

#### AVCRP Controls

If the connected Bluetooth device supports AVRCP, the extension can control media playing on the connected device. These controls include Pause, Play, Next Track, and Previous Track.

#### Voice Cues

These LEDs indicate when any of the remote Cue events occur:

* Idle: BT interface idle
* Disc: Entering BT discovery mode
* Conn: BT device connected
* Err: Pairing error occurred. This cue fires only if an external device that was previously connected to the DBU attempts to reconnect but the DBU no longer has that device in its "previously paired" list.

### Bluetooth, USB, Net Audio Settings

#### Meters

Only active when metering is enabled. Indicates the levels on each channel.

#### Gain

Sets the gain level on a channel, from -100 to 20.

#### Mute

Mutes the audio for a channel. Click the button to toggle the state.

#### USB Connected

Indicates whether a USB host device is connected to the USB port.

### Mixer

#### Output Knobs

Adjust the output level, from -100 to 0.

#### Tone Gen Enable

Enables or disables the tone generator.

#### Ton Gen Freq

Sets the frequency of the tone generator, from 10 to 20000 Hz.

#### Ton Gen Level

Sets the amplitude of the tone generator signal, from -100 to 0.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Bluetooth | | | | |
| Album | (text) | | | Output |
| Artist | (text) | | | Output |
| AVRCP Next | 0  1 | false  true | 0  1 | Input / Output |
| AVRCP Pause | 0  1 | false  true | 0  1 | Input / Output |
| AVRCP Play | 0  1 | false  true | 0  1 | Input / Output |
| AVRCP Prev | 0  1 | false  true | 0  1 | Input / Output |
| Clear Pairings | 0  1 | false  true | 0  1 | Input / Output |
| Connected Device | (text) | | | Output |
| Pair/Close | 0  1 | false  true | 0  1 | Input / Output |
| RSSI  (Signal Strength Indicator) | (text) | | | Output |
| Signal Strength | 0  1 | false  true | 0  1 | Input / Output |
| Song | (text) | | | Output |
| Status | 0  1  2  3  4 | Idle  Discoverable  Connected  Conflict  Error | - | Output |
| BT Input | | | | |
| Gain | | | | |
| 1, 2 | -100 to 20 | -100 to 20 | 0.00 to 1.00 | Input / Output |
| Meter | | | | |
| 1, 2 | (indicator) | | | Output |
| Mute | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| BT Output | | | | |
| Gain | -100 to 20 | -100 to 20 | 0.00 to 1.00 | Input / Output |
| Meter | (indicator) | | | Output |
| Mute | 0  1 | false  true | 0  1 | Input / Output |
| Device | | | | |
| Connected | 0  1 | false  true | 0  1 | Output |
| Dante Lock | 0  1 | false  true | 0  1 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Metering | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Mixer | | | | |
| BTOut | | | | |
| 1-10 | -100 to 0 | -100 to 0 | 0.00 to 1.00 | Input / Output |
| Net*n*Out | | | | |
| 1-10 | -100 to 0 | -100 to 0 | 0.00 to 1.00 | Input / Output |
| USB*n*Out | | | | |
| 1-10 | -100 to 0 | -100 to 0 | 0.00 to 1.00 | Input / Output |
| Net Input | | | | |
| Gain | | | | |
| 1-4 | -100 to 20 | -100 to 20 | 0.00 to 1.00 | Input / Output |
| Meter | | | | |
| 1-4 | (indicator) | | | Output |
| Mute | | | | |
| 1-4 | 0  1 | false  true | 0  1 | Input / Output |
| Net Output | | | | |
| Gain | | | | |
| 1-4 | -100 to 20 | -100 to 20 | 0.00 to 1.00 | Input / Output |
| Meter | | | | |
| 1-4 | (indicator) | | | Output |
| Mute | | | | |
| 1-4 | 0  1 | false  true | 0  1 | Input / Output |
| Tone Gen | | | | |
| Enable | 0  1 | false  true | 0  1 | Input / Output |
| Frequency | 10 to 20000 | 10 to 20000Hz | 0.00 to 1.00 | Input / Output |
| Level | -100 to 0 | -100 to 0dB | 0.00 to 1.00 | Input / Output |
| USB Input | | | | |
| Gain | | | | |
| 1, 2 | -100 to 20 | -100 to 20 | 0.00 to 1.00 | Input / Output |
| Meter | | | | |
| 1, 2 | (indicator) | | | Output |
| Mute | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| USB Output | | | | |
| Gain | | | | |
| 1, 2 | -100 to 20 | -100 to 20 | 0.00 to 1.00 | Input / Output |
| Meter | | | | |
| 1, 2 | (indicator) | | | Output |
| Mute | | | | |
| 1, 2 | 0  1 | false  true | 0  1 | Input / Output |
| Voice Cue | | | | |
| Connected | 0  1 | false  true | 0  1 | Output |
| Discovery | 0  1 | false  true | 0  1 | Output |
| Error | 0  1 | false  true | 0  1 | Output |
| Idle | 0  1 | false  true | 0  1 | Output |
| Disable[1](#Use) | 0  1 | disabled  enabled | 0  1 | Input / Output |

###### 1. Use this control pin to enable or disable the extension in your design. When Disabled is set to enabled (value of 1), the Connection Status changes to "Not Present - Disabled".
