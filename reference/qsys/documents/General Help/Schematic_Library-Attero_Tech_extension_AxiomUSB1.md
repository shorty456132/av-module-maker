# Attero Tech Axiom USB1

> Source: https://help.qsys.com/Content/Schematic_Library/Attero_Tech_extension_AxiomUSB1.htm

# Attero Tech Axiom USB1

Use this extension to connect to and control an Axiom USB1 (Attero Tech by QSC).

**Note:** See the [Axiom USB1 product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/attero-tech/attero-tech-analog-io-extenders/axiom-usb1/) on the QSC website for product information and documentation.

[Compatibility](javascript:void(0))

The extension is compatible with Q-SYS Designer version 8.4 and above. For best results, use the latest [Attero Tech firmware](https://www.qsys.com/index.php?id=16390).

[Connection Setup](javascript:void(0))

To begin using the extension:

1. Drag it into the schematic.
2. Configure the extension properties, including the Connection Mode. See [Properties](#Properti).
3. Press F5 to save your design to the Core and run it.
4. Configure the connection depending on the Connection Mode:
   * Serial â NA. There are no parameters to configure within the extension.
   * Ethernet â In the IP field, specify the IP address of the Ethernet-to-serial adapter. The extension attempts to send messages to port 4999 of that address.
   * Proxy Device â In the NIC field, select the interface through which the extension will communicate to control the device. In the IP field, enter the IP address of the proxy device.

The extension automatically attempts a connection. The "Connected" LED glows green once a connection is established. If the extension loses its connection to the device, it will attempt to re-establish the connection every 5 seconds.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Connection Mode

Select the interface for communication with the USB1:

* Serial: (Default) Select this option if the USB1 is attached to a serial port on the Q-SYS Core or Q-SYS I/O peripheral. In your design, connect the Serial Port component for the Core or I/O peripheral to the input serial pin of the extension:

  **Tip:** For more information, see the [Serial Port (Core and I/O Devices)](serial_port.htm) component topic.
* Ethernet: Select this option if the USB1 serial port is connected via an Ethernet-to-serial adapter.
* Proxy Device: Select this option if the USB1 is connected to a networked device as an AXIOM peripheral.

#### Control Mode

Configure how the USB1 uses control messages such as volume and mute commands.

* In Standalone (default) mode, playback controls are applied to the USB1 itself while record controls are handled by host device.
* In Passthrough mode, playback controls are passed through to third party control system while record controls are handled by host device.

#### Audio Mode

Select what audio channels the device uses:

* 1x1 (Host AEC) (default)
* 1x1 (No Host AEC)
* 2x0
* 1x0

#### USB Name

The USB1 uses this name to enumerate itself to the connected device.

#### Show Debug

Select 'Yes' to show the Debug Output window. For details, see [Debug Output](debug_output.htm).

[Controls](javascript:void(0))

#### Force Config

If the extension detects that the configuration of the device does not match that of the extension, click the button to update the device settings to match.

#### Refresh

Although the extension monitors the device settings for changes automatically, this button manually triggers the extension to retrieve the current settings and update the extension values to match.

#### Identify

Causes the power LED on the front of the device to start blinking so it can easily be identified. The identify function remains active until manually turned off. Click the button to toggle between states.

#### Status

Normally, this shows "Initializing" for a few moments after starting your design, followed by "OK". If you see a "Fault" status, check your connection parameters. If you see "Missing", ensure that the device is powered on and connected to the network.

#### Details

Provides information on the connected device, such as MCU version. In Proxy Device mode, it will also show details of the proxy device.

### Audio Controls

#### Playback Master Volume

Sets the overall volume of the incoming USB audio, from -100 to 0.

#### Playback Volume Limit

Sets the maximum audio level for playback, from -100 to 0. This is available per channel when the mode allows.

#### Playback Mute

Sends a mute command to the USB1 for the playback audio.

#### Record Master Volume

When available based on the configured properties, indicates the set recording level on the USB host device, from -100 to 0.

#### Record Mute

Sends a mute command to the USB1 for the recording volume.

### Status Indicators

#### Connected

Indicates whether a host is connected to the USB interface.

#### Call State

Indicates whether a telephony application on the USB host device has been configured to use the USB1 and has established a voice connection with a third party.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Device | | | | |
| Connected | 0  1 | false  true | 0  1 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Disable[1](#Use) | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Master Volume | -100 to 0 | -100 to 0 | 0.00 to 1.00 | Input / Output |
| Playback Limit-Left, Right | -100 to 0 | -100 to 0 | 0.00 to 1.00 | Input / Output |
| Playback Mute | 0  1 | false  true | 0  1 | Input / Output |
| Record Mute | 0  1 | false  true | 0  1 | Input / Output |
| Record Volume | -100 to 0 | -100 to 0 | 0.00 to 1.00 | Output |
| USB Call State | 0  1 | false  true | 0  1 | Output |
| USB Connected | 0  1 | false  true | 0  1 | Output |

###### 1. Use this control pin to enable or disable the extension in your design. When Disabled is set to enabled (value of 1), the Connection Status changes to "Not Present - Disabled".

[Troubleshooting](javascript:void(0))

### "Missing - Serial port not assigned" (Serial mode)

* Check that the serial cable is properly connected between the Attero Tech device and the Q-SYS Core or peripheral.
* In Q-SYS Designer, check that the serial Input pin is wired to the Serial Port component of the Q-SYS Core or peripheral. See [Connection Mode](#Connecti).

### "Missing - Invalid IP or NIC" (Ethernet mode or Proxy mode)

Check that you've specified the correct IP address of the Attero Tech device. For Proxy mode, also check that you've selected the correct NIC.
