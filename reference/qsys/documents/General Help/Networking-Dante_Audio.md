# Dante Audio

> Source: https://help.qsys.com/Content/Networking/Dante_Audio.htm

# Dante Audio

Read this topic to understand the network requirements for Dante hardware and the Software Dante components in Q-SYS Designer Software.

[Clocking Requirements](javascript:void(0))

When using the [Software Dante TX](../Schematic_Library/soft_dante_output.htm) and [Software Dante RX](../Schematic_Library/soft_dante_input.htm) components, observe these clocking requirements, which are all configurable in Design Properties:

* Configure the Software Dante Receive Latency to compensate for network latency variation.
* If you require the Q-SYS Core to be the clocking Preferred Master, you cannot set this flag in Dante Controller. Instead, configure the Q-SYS Designer > Design Properties > PTP Priority 1 property to be <= 127 and ensure that no other devices have 'Preferred Master' checked in Dante Controller.

Refer to the [Design Properties](../Schematic_Library/design_properties.htm) topic for explanations of these properties.

[QoS Requirements](javascript:void(0))

In [Design Properties](../Schematic_Library/design_properties.htm), you can choose DSCP [Quality of Service (QoS)](QoS.htm) markings to apply to various Q-SYS data types. These DSCP markings help the network switch prioritize these data types alongside other network traffic. To assign DSCP values within your Q-SYS design, navigate to File > Design Properties in Q-SYS Designer, where you can select from Q-LAN, Audinate, and Manual presets.

When your network includes Dante traffic, it is strongly recommended to use the Audinate QoS preset (as it tells Q-SYS Designer to align DSCP markings with Audinate's) unless you are using a [Q-SYS NS Series Network Switch](https://www.qsys.com/products-solutions/q-sys/networking/ns-series-network-switches/). For guidance on selecting the appropriate switch for your network, refer to the [Network Switches & Infrastructure](Switches_Infrastructure.htm) documentation.

**Tip:** For further information on integrating Dante into your network and configuring QoS, consult the [documentation on Audinate's website](https://www.getdante.com/support/faq/how-does-dante-use-dscp-diffserv-priority-values-when-configuring-qos/).

[Network Requirements](javascript:void(0))

Software Dante requires the mDNS protocol. This protocol is automatically enabled on the LAN adapter configured for Software Dante (in Design Properties > Software Dante > Interface) whenever Software Dante is included in a running design.

**Tip:** To learn how to configure what LAN interfaces to use for Software Dante, see [Design Properties](../Schematic_Library/design_properties.htm).

[Redundancy Requirements](javascript:void(0))

### Redundancy Requirements for CDN64 Cards

To achieve redundancy with the [CDN64 â Dante Audio Bridge Card](../Hardware/IO_Expanders/CDN64.htm), observe these requirements:

* Ensure that the two CDN64 cards are installed in a redundant pair of Q-SYS Cores or I/O Frames.
* In the Q-SYS Dante components ([Dante In](../Schematic_Library/io_dante_input_card.htm), [Dante Out](../Schematic_Library/io_dante_output_card.htm)), set the External Configuration property to 'No' â i.e., internal control mode.
* Configure all routing, in and out, using the Q-SYS Dante components. If you have a third-party device that receives a Dante stream from the CDN64 card, make that connection as you normally do (for example, with Dante Controller).
* If you have configured a static IP address on the primary card, you must also configure a static IP on the backup card (configurable in Dante Controller). Since only one card is active at a time, a static address can be the same for both cards.

**Note:** Dante Domain Manager version 1.1.0 (supported by Dante firmware 4.2.0) is the first DDM version that is compatible with a redundant CDN64 card configuration.

### Redundancy Requirements for Software Dante

* The Q-SYS Core's primary (LAN A) and secondary (LAN B) network interfaces must be isolated by completely separate network infrastructures or VLANs with no routing between them.
* The Q-SYS Designer > File > Design Properties > Software Dante > Interface property must be set to 'Both'. Refer to the [Design Properties](../Schematic_Library/design_properties.htm) topic.
* If DHCP server IP address assignment is not used on the Q-SYS network, the Q-SYS Core's LAN B network interface must be statically assigned an IP address within 172.31.x.x/16. This is because Dante devices use this IP range for link-local connections on the secondary network. Use Q-SYS Core Manager to configure IP addressing â see the Q-SYS Core Manager > [Network > Basic](../Core_Manager/Core_Management/Network_Settings.htm) topic.
* Each Q-SYS Core must have its own unique Software Dante license installed. Refer to the Q-SYS Core Manager > [Licensing](../Core_Manager/Core_Management/Licensing.htm) topic.

### Failover

When a failover occurs, all the Dante control values are copied to the backup. Any 3rd-party device configured to receive Dante streams automatically reconnects, as the Device Name and Channel names and labels stay the same.
