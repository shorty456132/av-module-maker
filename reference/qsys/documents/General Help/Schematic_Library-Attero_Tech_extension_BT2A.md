# Attero Tech unBT2A

> Source: https://help.qsys.com/Content/Schematic_Library/Attero_Tech_extension_BT2A.htm

# Attero Tech unBT2A

Use this extension to connect to and control a unBT2A BluetoothÂ® in-wall audio interface (Attero Tech by QSC).

**Note:** See the [unBT2A product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/attero-tech/at-wall-mount-network-audio-interfaces/unbt2a/) on the QSC website for product information and documentation.

[Compatibility](javascript:void(0))

The extension is compatible with Q-SYS Designer version 8.4 and above and Attero Tech firmware version 1.2 and above. For best results, use the latest Attero Tech firmware.

[Connection Setup](javascript:void(0))

To begin using the extension:

1. Drag it into the schematic.
2. Configure the extension properties, including the Control Mode. See [Properties](#Properti).
3. Press F5 to save your design to the Core and run it.
4. Configure the connection depending on the Control Mode:
   * Serial â NA. There are no parameters to configure within the extension.
   * Ethernet â In the IP field, specify the IP address of the Global CachÃ© Ethernet to serial adapter. The extension attempts to send messages to port 4999 of that address.
   * Proxy Device â In the NIC field, select the interface through which the extension will communicate to control the device. In the IP field, enter the IP address of the proxy device.

The extension automatically attempts a connection. The "Connected" LED glows green once a connection is established. If the extension loses its connection to the device, it will attempt to re-establish the connection every 5 seconds.

**Note:** If Dante Lock is active on the connected device, you will see a padlock icon next to the device name.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Control Mode

Select the interface for communication with the unBT2A:

* Serial: (Default) Select this option if the unBT2A is attached to a serial port on the Q-SYS Core or Q-SYS I/O peripheral. In your design, connect the Serial Port component for the Core or I/O peripheral to the input serial pin of the extension:

  **Tip:** For more information, see the [Serial Port (Core and I/O Devices)](serial_port.htm) component topic.
* Ethernet: Select this option if the unBT2A serial port is connected via a Global CachÃ© Ethernet to serial adapter.
* Proxy Device: Select this option if the unBT2A is connected to a networked device as an AXIOM peripheral.

#### Audio Mode

Select whether the unBT2A outputs stereo or mono audio:

* Stereo: (Default) The two analog outputs represent either the left or right channel of the stereo audio from the paired device.
* Mono: Each output is a mix of the left and right audio from the paired device.

#### Audio Level

Select the sensitivity for the audio input:

* +4dBu (Pro) (Default)
* -10dBV (Consumer)

#### Show Debug

Select 'Yes' to show the Debug Output window. For details, see [Debug Output](debug_output.htm).

[Controls](javascript:void(0))

#### Force Config

By default, the extension checks the settings on the unBT2A to see if they match those of the extension. If the settings do not match, the connection fails, which prevents you from accidentally overwriting device settings. Use this control to force the extension to overwrite the settings on the unBT2A.

#### Refresh

Although the extension monitors the device settings for changes automatically, this button manually triggers the extension to retrieve the current settings and update the extension values to match.

#### Status

Normally, this shows "Initializing" for a few moments after starting your design, followed by "OK". If you see a "Fault" status, check your connection parameters. If you see "Missing", ensure that the device is powered on and connected to the network.

#### Details

Provides information on the connected device, such as MCU version. In Proxy Device mode, it will also show details of the proxy device.

### Bluetooth Settings

#### Clear Pairings

Click to clear the list of pairings on the device.

#### Pair/Connect or Disconnect

If the Bluetooth interface is idle, click Pair/Connect to initiate a pair cycle. If the device is connected, click Disconnect to end the Bluetooth connection.

#### Friendly Name

While Bluetooth is disconnected, optionally change the device name that is used when pairing, and then click Apply.

#### Front Panel Pair Button

Toggles functionality of the front panel Pair button. Disable the Pair button when you require a control system to initiate pairing remotely.

#### Signal Strength

Indicates the current Bluetooth signal strength, both in color and value:

* Green = Good
* Yellow = Average
* Red = Poor

**Note:** This control only functions with Attero Tech firmware v1.4 (when available) and later.

#### Status

Text field indicates the current Bluetooth status. Each status also has a numeric value when using the Status control pin â see [Control Pins](#Control).

* Idle
* Discoverable
* Connected (Unknown)

### Device Settings

#### Mute

Allows muting of the audio. If the button is grey, the mute is inactive. If itâs orange, the mute is active. Click the button to toggle between states.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Device | | | | |
| Bluetooth BER[2](#This)  (Bit Error Rate) | (text) | | | Output |
| Bluetooth Clear Pairings | 0  1 | false  true | 0  1 | Input / Output |
| Bluetooth Lock | 0  1 | false  true | 0  1 | Input / Output |
| Bluetooth Pair/Close | 0  1 | false  true | 0  1 | Input / Output |
| Bluetooth RSSI[2](#This)  (Signal Strength Indicator) | (text) | | | Output |
| Bluetooth Status | 0  1  2 | Idle  Discoverable  Connected (Unknown) | - | Output |
| Connected | 0  1 | false  true | 0  1 | Output |
| Mute | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Disable[1](#Use) | 0  1 | disabled  enabled | 0  1 | Input / Output |

###### 1. Use this control pin to enable or disable the extension in your design. When Disabled is set to enabled (value of 1), the Connection Status changes to "Not Present - Disabled".

###### 2. This control pin only functions with Attero Tech firmware v1.4 (when available) and later.

[Troubleshooting](javascript:void(0))

### "Missing - Serial port not assigned" (Serial mode)

* Check that the serial cable is properly connected between the Attero Tech device and the Q-SYS Core or peripheral.
* In Q-SYS Designer, check that the serial Input pin is wired to the Serial Port component of the Q-SYS Core or peripheral. See [Control Mode](#Control2).

### "Missing - Invalid IP" (Ethernet mode or Proxy mode)

Check that you've specified the correct IP address of the Attero Tech device. For Proxy mode, also check that you've selected the correct NIC.
