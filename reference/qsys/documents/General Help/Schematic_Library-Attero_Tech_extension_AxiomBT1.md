# Attero Tech Axiom BT1

> Source: https://help.qsys.com/Content/Schematic_Library/Attero_Tech_extension_AxiomBT1.htm

# Attero Tech Axiom BT1

Use this extension to connect to and control an Axiom BT1 (Attero Tech by QSC).

**Note:** See the [Axiom BT1 product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/attero-tech/attero-tech-analog-io-extenders/axiom-bt1/) on the QSC website for product information and documentation.

[Compatibility](javascript:void(0))

The extension is compatible with Q-SYS Designer version 8.4 and above. For best results, use the latest [Attero Tech firmware](https://www.qsys.com/index.php?id=16390).

[Connection Setup](javascript:void(0))

To begin using the extension:

1. Drag it into the schematic.
2. Configure the extension properties, including the Connection Mode. See [Properties](#Properti).
3. Press F5 to save your design to the Core and run it.
4. Configure the connection depending on the Connection Mode:
   * Serial â NA. There are no parameters to configure within the extension.
   * Ethernet â In the IP field, specify the IP address of the Global CachÃ© Ethernet-to-serial adapter. The extension attempts to send messages to port 4999 of that address.
   * Proxy Device â In the NIC field, select the interface through which the extension will communicate to control the device. In the IP field, enter the IP address of the proxy device.
   * Proxy Device â In the NIC field, select the interface on the Core that the extension will use to communicate through. In the IP field, enter the IP address of the D2i that the BT1 is connected to.

The extension automatically attempts a connection. The "Connected" LED glows green once a connection is established. If the extension loses its connection to the device, it will attempt to re-establish the connection every 5 seconds.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Connection Mode

Select the interface for communication with the BT1:

* Serial: (Default) Select this option if the BT1 is attached to a serial port on the Q-SYS Core or Q-SYS I/O peripheral. In your design, connect the Serial Port component for the Core or I/O peripheral to the input serial pin of the extension:

  **Tip:** For more information, see the [Serial Port (Core and I/O Devices)](serial_port.htm) component topic.
* Ethernet: Select this option if the BT1 serial port is connected via a Global CachÃ© Ethernet-to-serial adapter.
* Proxy Device: Select this option if the BT1 is connected to a networked device as an AXIOM peripheral.
* Proxy Device: Select this option if the BT1 is connected to a D2i Dante wall plate and the plugin will need to communicate with the BT1 via the D2i.

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

Provides information on the connected device, such as MCU version. In Proxy Device mode, it will also show details of the proxy device.

### Bluetooth Settings

#### Clear Pairings

Click to clear the list of pairings on the device.

#### Pair/Connect or Disconnect

If the Bluetooth interface is idle, click Pair/Connect to initiate a pair cycle. If the device is connected, click Disconnect to end the Bluetooth connection.

#### Friendly Name

While Bluetooth is disconnected, optionally change the device name that is used when pairing, and then click Apply.

#### Connect Mode

Select how previously-paired Bluetooth devices reconnect:

* Manual: Requires that the BT1 is put in pairing mode to reconnect.
* Reconnect: If an external Bluetooth device has connected before, allows that device to reconnect without the BT1 to be in pairing mode.
* Exclusive: Allows only a single device to be paired and reconnect. Pairing attempts by other devices will fail.

#### Audio Mode

Select the type of audio for the Bluetooth connection:

* Media Bridging: Allows only media audio to pass via the Bluetooth interface. Call audio remains local to the connected device.
* Call Bridging: Allows call audio to pass via the Bluetooth interface while other audio remains local to the device.
* Media and Call Bridging: All audio is allowed to pass via the Bluetooth interface.

#### BT Output

Select the desired output type when in âmediaâ mode. Options are Mono or Stereo.

#### Front Panel Pair Button

Toggles functionality of the front panel Pair button. Disable the Pair button when you require a control system to initiate pairing remotely.

#### Signal Strength

Indicates the current Bluetooth signal strength, both in color and value:

* Green = Good
* Yellow = Average
* Red = Poor

#### Status

Text field indicates the current Bluetooth status. Each status also has a numeric value when using the Status control pin â see [Attero Tech Axiom BT1](#Control).

* Idle
* Discoverable
* Connected (No AVRCP)
* Connected (AVRCP)

#### Audio Details

If the connected Bluetooth device supports AVRCP, it will pass certain information to the extension, such as the connected device's friendly name and details of any audio that is currently being played. This information is shown in the Audio Details section.

#### AVCRP Controls

If the connected Bluetooth device supports AVRCP, the extension can control media playing on the connected device. These controls include Stop, Pause, Play, Next Track, Previous Track, Volume Up, and Volume Down.

### Input Settings

#### BT Volume

Sets the maximum level of incoming BT audio, from 0 to 100.

#### Aux Volume

Sets the maximum level of incoming auxiliary 3.5mm connection audio, from 0 to 100.

### Output Settings

#### Aux Volume

Sets the maximum level of any outgoing audio to the auxiliary 3.5mm connection, from 0 to 100.

#### Detect

LED indicates if a cable is plugged into the auxiliary 3.5mm jack connection.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| AXIOM | | | | |
| AUX Volume | 0 to 100 | 0 to 100 | 0.00 to 1.00 | Input / Output |
| BT Volume | 0 to 100 | 0 to 100 | 0.00 to 1.00 | Input / Output |
| Bluetooth | | | | |
| Album | (text) | | | Output |
| Artist | (text) | | | Output |
| AVRCP Next | 0  1 | false  true | 0  1 | Input / Output |
| AVRCP Pause | 0  1 | false  true | 0  1 | Input / Output |
| AVRCP Play | 0  1 | false  true | 0  1 | Input / Output |
| AVRCP Prev | 0  1 | false  true | 0  1 | Input / Output |
| AVRCP Stop | 0  1 | false  true | 0  1 | Input / Output |
| AVRCP Vol Dn | 0  1 | false  true | 0  1 | Input / Output |
| AVRCP Vol Up | 0  1 | false  true | 0  1 | Input / Output |
| Clear Pairings | 0  1 | false  true | 0  1 | Input / Output |
| Connected Device | (text) | | | Output |
| Lock | 0  1 | false  true | 0  1 | Input / Output |
| Pair/Close | 0  1 | false  true | 0  1 | Input / Output |
| RSSI  (Signal Strength Indicator) | (text) | | | Output |
| Song | (text) | | | Output |
| Status | 0  1  2  3 | Idle  Discoverable  Connected (No AVRCP)  Connected (AVRCP) | - | Output |
| Device | | | | |
| Connected | 0  1 | false  true | 0  1 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Aux Detect | 0  1 | false  true | 0  1 | Output |
| Disable[1](#Use) | 0  1 | disabled  enabled | 0  1 | Input / Output |

###### 1. Use this control pin to enable or disable the extension in your design. When Disabled is set to enabled (value of 1), the Connection Status changes to "Not Present - Disabled".

[Troubleshooting](javascript:void(0))

### "Missing - Serial port not assigned" (Serial mode)

* Check that the serial cable is properly connected between the Attero Tech device and the Q-SYS Core or peripheral.
* In Q-SYS Designer, check that the serial Input pin is wired to the Serial Port component of the Q-SYS Core or peripheral. See [Connection Mode](#Connecti).

### "Missing - Invalid IP or NIC" (Ethernet mode or Proxy mode)

Check that you've specified the correct IP address of the Attero Tech device. For Proxy mode, also check that you've selected the correct NIC.
