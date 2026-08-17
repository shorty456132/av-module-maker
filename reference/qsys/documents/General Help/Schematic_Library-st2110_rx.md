# ST 2110 Audio Receiver

> Source: https://help.qsys.com/Content/Schematic_Library/st2110_rx.htm

# ST 2110 Audio Receiver

The Q-SYS ST 2110 Audio Receiver is designed to receive SMPTE ST 2110-compliant audio streams with optional network redundancy over IP networks. It supports both manual and Networked Media Open Specifications (NMOS) connection modes, allowing for flexible configuration and seamless integration with third-party devices. QSC only supports ST 2110-30, Conformance Level A at this time.

[NMOS Implementation for Q-SYS](javascript:void(0))

### Overview

The NMOS implementation for Q-SYS enhances the system's capabilities by integrating NMOS standards for media transport and session management. This integration ensures seamless communication and synchronization between Q-SYS components and NMOS-enabled devices.

**IS-04 Discovery and Registration**: Allows control and monitoring applications to find the resources on a network, specifically the Node API.

**IS-05 Device Connection Management Specification**: Provides a transport-independent way of connecting Media Nodes, specifically the Connection API.

**BCP-002-02 Asset Distinguishing Information**: Provides unique asset tags for each device, including manufacturer, product name, instance identifier, and function.

To use the NMOS terminology, an NMOS-enabled Core is a Node containing one Device that in turn contains zero or more Senders and/or Receivers. An NMOS Sender is implemented as an ST 2110 Transmitter; an NMOS Receiver is implemented as an ST 2110 Receiver.

Our NMOS implementation has been tested using the AMWA NMOS Test tool and EVSâs Cerebrum as a registry service.

### NMOS Server

Each Core hosts an HTTP server providing the NMOS REST APIs mentioned above, at:

`http://<core IP>:8085/x-nmos`

Weâll refer to this server as the âNMOS Server.â

The NMOS server will run automatically if a Design is being deployed which includes at least one ST 2110 audio component (Transmitter or Receiver) that has its Connection Mode property set to âNMOSâ (as opposed to âManualâ).

### NMOS Server Configuration Support Page

**Tip:** Support pages are protected by bearer-auth tokens if access controls are enabled. Therefore, you may need to log in as an admin level user before you can access the support pages.

The NMOS Server Configuration support page is available at:

`http://core IP/support/nmos`

This page allows the NMOS Node registration method to be configured.

* Unicast DNS-SD (default registration). To ensure successful DNS-SD registration, visit the [NMOS Implementation Guide for DNS-SD](https://specs.amwa.tv/info-004/branches/main/docs/Introduction.html).
* mDNS-SD
* Manual

If unicast DNS-SD is selected, the domain (e.g., mycompany.com) in which the registry service resides may be specified. If nothing is specified, the Coreâs default domain will be used. If that default domain isnât the same as the registry serviceâs domain, the Core (Node) will be unlikely to find the registry.

If mDNS-SD or a Manual configuration method is required, then visit the support page.

[Inputs and Outputs](javascript:void(0))

### Input Pins

This component does not have any input pins.

### Output Pins

#### Channel 1 - n

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the ST 2110 Audio Receiver is set to 8 audio output channels. You can choose between 1 through 8.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Connection Mode

*Manual*: Manually configure the network settings for the ST 2110 Audio Receiver.

*NMOS*: The receiver will use the Networked Media Open Specifications (NMOS) protocol for automatic discovery and connection management.

#### Channel Count

The number of input channels: 1 through 8 (default).

[Controls](javascript:void(0))

### Flow (Tab)

#### Peak Input Level (dBFS)

Measures the received audio peak input level, from -120 dB to 20 dB.

### Digital

#### Invert

Inverts the polarity of the audio signal.

#### Mute

Mutes the digital audio signal.

#### Gain

Controls the gain of the digital audio signal, from -100 dB to 20.0 dB (default is 0).

### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

### Connection

#### Global Enable

Activates or deactivates the Primary and Secondary Leg of the Rx.

#### Flow Label

Shows a specific label to the media flow for identification purposes.

#### Flow Channels

*(Read-only field)*: Specifies the number of audio channels in the media flow.

#### Media Clock Offset

Adjusts the timing offset of the media clock to synchronize audio streams.

#### Additional Network Rx Latency

Sets extra latency to account for network delays in receiving media packets. Options include None, 1, 2, or 5 extra milliseconds.

#### Packet Time

*(Read-only field)*: Defines the duration of each media packet in milliseconds.

#### Media Type

Defines the encoding name of the audio stream. Options are L16 or L24.

#### Payload Type

Specifies the RTP payload type for the media stream.

### Primary Leg / Secondary Leg

**Note:** Secondary Leg only appears when the **Is Redundant** Property is set to **Yes**.

#### RTP Enable

Activates or deactivates the Primary/Secondary Leg of the Rx.

#### Primary OK / Secondary OK (LED)

This LED indicator shows the status of the Primary/Secondary network connection.

#### Multicast IP

Sets the multicast IP address for receiving the media stream.

#### Destination Port

Specifies the port number to which the media stream is received.

#### Source IP

Indicates the IP address from which the media stream is sent.

#### Interface IP

*(Read-only field)*: Indicates the IP address of the network interface receiving the media stream.

#### Interface

*(Read-only field)*: Indicates the network interface used for receiving the media stream.

### Details (Tab)

**Note:** Secondary Leg only appears when the **Is Redundant** Property is set to **Yes**.

#### Details

The Details section displays cumulative information for audio being received from the source.

#### Reset Details

The information in the Details section resets during a design restart on the Q-SYS Core or whenever you click Reset Details.

#### Raw SDP

*(Read-only field)*: Displays the SDP associated with the stream being received.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Channel *n* | | | | |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  inverted | 0  1 | Input / Output |
| Level | -120 to 20 | -120 dB to 20 dB | 0.000 to 1.00 | Output |
| Mute | 0  1 | unmuted  muted | 0  1 | Input / Output |
| Connection | | | | |
| Additional Network Rx Latency | None  Extra 1 ms  Extra 2 ms  Extra 5 ms | | | Input / Output |
| Flow Channels | 1 to 8 | 1 to 8 | 0.00 to 1.00 | Output |
| Flow Label | (text) | | | Output |
| Global Enable | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Media Clock Offset | 0 to *nnn* | 0 to *nnn* | 0 to 1.00 | Output |
| Media Type | L16  L24 | L16  L24 | N/A | Output |
| Packet Time | (text) | | | Output |
| Payload Type | 96 to 127 | 96 to 127 | 0.00 to 1.00 | Output |
| Details | | | | |
| Primary / Secondary Leg | | | | |
| Details | (text) | | | Output |
| Reset Details | 0  1 | false  true | 0  1 | Input / Output |
| Raw SDP | (text) | | | Output |
| Primary / Secondary Leg | | | | |
| Destination Port | 1 to 65535 | 1 to 65535 | 0.00 to 1.00 | Input / Output |
| Interface | LAN A (Blue) - Primary Leg  LAN B (Red) - Secondary Leg | | | Output |
| Interface IP | *nnn*.*nnn*.*nnn*.*nnn* | | | Output |
| Multicast IP | *nnn*.*nnn*.*nnn*.*nnn* | | | Input / Output |
| Primary OK | 0  1 | false  true | 0  1 | Output |
| RTP Enable | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Source IP | *nnn*.*nnn*.*nnn*.*nnn* | | | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
