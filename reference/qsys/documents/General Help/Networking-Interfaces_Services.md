# Network Interfaces, Services, & Protocols

> Source: https://help.qsys.com/Content/Networking/Interfaces_Services.htm

# Network Interfaces, Services, & Protocols

Q-SYS provides many network-related services and functions across multiple network adapters (interfaces). Q-SYS Core processors, peripherals, and some I/O cards include network interfaces.

**Note:** Many network services on the Q-SYS Core can be enabled or disabled on a per-adapter basis in Q-SYS Core Manager or Q-SYS Reflect. For more information, see Q-SYS Core Manager > [Network > Services](../Core_Manager/Core_Management/Network_Services.htm).

[Network Interfaces](javascript:void(0))

### Q-SYS Core Processors

Q-SYS Core processors include at least two network interfaces.

* LAN A: Included on all Q-SYS Core processors, LAN A is required for use with the primary Q-LAN network. (If the Q-LAN network is not redundant, LAN A must be used for Q-LAN.) LAN A can also be used for other functionality.
* LAN B: Included on all Q-SYS Core processors, LAN B is required for use with the secondary Q-LAN network. It can also be used for other functionality.
* AUX LAN / AUX A, B: Some Q-SYS Core processor models include one or more AUX ports that can be used for non-time-sensitive networking applications.

**Note:** Q-SYS does not support routing between LAN interfaces (also known as inter-NIC-routing).

### Q-SYS Peripherals

Some Q-SYS peripherals have both LAN A and LAN B interfaces. Connect each interface to the network corresponding to the same interface on the Q-SYS Core processor.

**Note:** Q-SYS peripherals cannot be placed on LAN A and LAN B when there is only a single network.

### Q-SYS I/O Cards

Some Q-SYS I/O cards include network interfaces, which are used exclusively for the card's intended purpose. These include:

* Danteâ¢ audio bridge card (CDN64)
* AVB bridge card (CAN32)
* CobraNetâ¢ digital input/output card (CCN32).

**Note:** Although the AES/EBU digital input card (CIAES-16) includes RJ-45 connectors, it does not support Ethernet in any context.

[Network Services and Protocols](javascript:void(0))

These high-level network services and their underlying protocols can be enabled or disabled on the Q-SYS Core processor on a per-adapter basis (except as noted) in Q-SYS Core Manager or Q-SYS Reflect.

**Note:** See Q-SYS Core Manager > [Network > Services](../Core_Manager/Core_Management/Network_Services.htm) for more information.

= Can be enabled on the LAN adapter.

| Network Service / Function | Description / Protocols Used | LAN A | LAN B | AUX LAN |
| --- | --- | --- | --- | --- |
| Q-LAN | Required when using Q-SYS Audio Enabled Peripherals for audio streaming.  Protocols: Real-time audio streaming is handled using RTP (Real-time Transport Protocol) and RTCP (Real-time Transport Control Protocol): Unicast UDP Ports 6518-7030  **Note:** Q-LAN audio is not encrypted at this time. Q-LAN audio is highly time-sensitive and requires a network with low latency and low jitter to ensure high-quality audio delivery. It is strongly recommended to configure QoS on your network to prioritize Q-LAN audio traffic, ensuring timely and reliable delivery. |  |  |  |
| Q-SYS Device Discovery | Required to allow Q-SYS software applications, such as Q-SYS Designer, to automatically discover the Core on a LAN. If disabled, then Hard Links must be used to locate the Core on the network.  Protocols: Q-SYS Discovery Protocol (QDP): Multicast UDP 224.0.23.175 on Ports 2467-2470 and Unicast on Port 6504 |  |  |  |
| Q-SYS Designer Communications - Secure | This required service allows secure connection, design file load, and control communications with the Core when using Q-SYS Designer Software version 7.1 or higher. Requires that either Q-SYS Device Discovery is enabled or Hard Links are used to locate the Core on the network.  Protocols: Hypertext Transfer Protocol Secure (HTTPS): TCP Port 443  **Note:** This service cannot be disabled. |  |  |  |
| Q-SYS Core Redundancy | Required to use the Core with another in a redundant pair.  Protocols:   * Hypertext Transfer Protocol Secure (HTTPS): TCP Port 443 * Transport Layer Security (TLS): TCP Port 1704 * Q-SYS Discovery Protocol (QDP): Multicast UDP 224.0.23.175 on Ports 2467-2470 and Unicast on Port 6504 * Q-SYS Control Binary Secure (QCBS): TCP Port 1704 |  |  |  |
| Q-SYS Audio Enabled Peripherals | Required when using any Q-SYS peripheral device that provides audio streaming.  Protocols:   * See [Q-LAN](#Q-LAN) |  |  |  |
| Q-SYS Control Peripherals | Required when using the Core with any Q-SYS TSC touch screen control device.  Protocols:   * Q-SYS Discovery Protocol (QDP): Multicast UDP 224.0.23.175 on Ports 2467-2470 and Unicast on Port 6504 * Q-SYS Control Binary Secure (QCBS): TCP Port 1704 * Hypertext Transfer Protocol Secure (HTTPS): TCP Port 443 |  |  |  |
| Q-SYS Control for Microsoft Teams | Required when using the Core with any Q-SYS UCI Viewer application. Requires that either Q-SYS Device Discovery is enabled or Hard Links are used to locate the Core on the network.  Protocols:   * Q-SYS Control Binary Secure (QCBS): TCP Port 1704 * Hypertext Transfer Protocol Secure (HTTPS): TCP Port 443 * Secure Transport Layer Security (TLS): TCP Port 2112 |  |  |  |
| Q-SYS UCI Viewers - Windows and iOS | Required when using the Core with any Q-SYS UCI Viewer application. Requires that either Q-SYS Device Discovery is enabled or Hard Links are used to locate the Core on the network.  Protocols:   * Q-SYS Control Binary Secure (QCBS): TCP Port 1704 * Hypertext Transfer Protocol Secure (HTTPS): TCP Port 443 * Unicast on Port 6504 |  |  |  |
| Q-SYS NC Series Cameras | Required to use Q-SYS NC Series Cameras with the Q-SYS Core.  Protocols: Q-SYS Discovery Protocol (QDP): Multicast UDP 224.0.23.175 on Ports 2467-2470 and Unicast on Port 6504 |  |  |  |
| Q-SYS External Control Protocol - ASCII | Required to allow control of the Core from a third-party control system using the ASCII-based Q-SYS External Control Protocol.  Protocols: TCP Port 1702 |  |  |  |
| Q-SYS Remote Control Protocol - JSONRPC | Required to allow control of the Core from a third-party control system using the JSONRPC-based Q-SYS Remote Control Protocol.  Protocols: TCP Port 1710 |  |  |  |
| Q-SYS Remote WebSocket Control (BETA) | Required to allow control of this Core from a 3rd party control system using a WebSocket connection via QRWC. (API is in BETA and subject to change.)  **Protocols**: TCP Port 443 |  |  |  |
| Secure Maintenance & Support | Allows secure communications for diagnostics by QSC engineering if remote support is requested, authorized, and provided by the user. This can safely be disabled in most situations.  Protocols: Secure Shell (SSH): TCP Port 22 |  |  |  |
| Enabled for all NICs | | | | |
| Q-SYS Device Discovery via mDNS / Bonjour | Allows accessing the Core on a LAN via hostname â rarely used in normal operation. Note that some Q-SYS Plugin developers leverage the mDNS service for various functions so disabling this service could impact the performance of some plugins.  **Note:** The use of Software Dante in your Design will automatically enable its required mDNS functionality on the LAN(s) to which Software Dante is deployed.  Protocols: Multicast Domain Name Service (mDNS): Multicast UDP 224.0.0.251 on Port 5353 |  | | |
| Hovermon Audio | Allows the Q-SYS Designer Software application to listen to audio throughout the DSP design for troubleshooting purposes. Can be disabled for security reasons if desired.  Protocols: Outbound from Q-SYS Core: UDP Ephemeral Port |  | | |
| Clock Synchronization (PTPv2) | Allows devices on the network to maintain a unified time reference.  Protocols: IEEE 1588-2008 Precision Time Protocol (PTPv2); Multicast IP: 224.0.1.129on on UDP Port 319 and 320 |  |  |  |
| VoIP (SIP and RTP) | Allows Q-SYS to function as a VoIP endpoint, routing audio into and out of conference rooms, paging systems, or other AV environments over standard IP-based telephony/  Protocols:   * UDP/TCP 5060 (unencrypted) * TCP 5061 (TLS encrypted) * UDP 10,000â30,000 (dynamic range) |  |  |  |
| ICMP (Ping) | Internet Control Message Protocol (ICMP) allows the use of testing network connectivity and device availability.  Protocols: ICMP (for network diagnostics) |  |  |  |

[Multicast and Time-Sensitive Protocols](javascript:void(0))

Of the protocols and functions supported by Q-SYS, some require the transmission and reception of multicast packets, while others (such as Q-LAN) are time sensitive, requiring guaranteed and timely delivery of packets through the network.

In the following tables:

* **Multicast** protocols require that multicast traffic is allowed on the network. If the total bandwidth of traffic on the network exceeds 1Gbps, you must configure IGMP snooping on the network switch. See [Network Switches & Infrastructure](Switches_Infrastructure.htm) and [Addressing & Routing](Addressing_Routing.htm).
* **Time-sensitive** protocols require a network that can deliver packets with low latency and low jitter. For these protocols and functions, QSC recommends that you configure Quality of Service (QoS). See [Network Switches & Infrastructure](Switches_Infrastructure.htm).

[Q-SYS Core Network Connections](javascript:void(0))

| Protocol | Multicast | Time-sensitive |
| --- | --- | --- |
| Q-SYS Discovery |  |  |
| Q-SYS Control |  |  |
| Audio Clocking (PTPv2) |  |  |
| Q-LAN Audio |  |  |
| Q-LAN Video |  |  |
| AES67 |  |  |
| Dante Audio |  |  |
| VoIP Telephony Control (SIP/TLS) |  |  |
| VoIP Telephony Audio (RTP/SRTP) |  |  |
| Other Media Streaming |  |  |

[CDN64 (Dante Card) Network Connections](javascript:void(0))

| Protocol / Function | Multicast | Time-sensitive |
| --- | --- | --- |
| mDNS |  |  |
| Audio Clocking (PTPv1) |  |  |
| Dante Audio |  |  |

[CAN32 (AVB Card) Network Connections](javascript:void(0))

The CAN32 is a 100 Mbps device. IGMP snooping is not required on AVB-compliant networks.

| Protocol / Function | Multicast | Time-sensitive |
| --- | --- | --- |
| IEEE1722.1 (Device discovery, control, connection) |  |  |
| MSRP (Stream Reservation Protocol) |  |  |
| Audio Clocking (PTPv2) |  |  |
| AVB Audio (QoS handled by IEEE802.1Qat in switch) |  |  |

[CCN32 (CobraNet Card) Network Connections](javascript:void(0))

The CCN32 is a 100 Mbps device. CobraNet devices do not support IGMP snooping. CobraNet Audio packets are usually unicast, but can be configured as multicast.

| Protocol / Function | Multicast | Time-sensitive |
| --- | --- | --- |
| Conductor Beat Packets |  |  |
| Discovery and Device Connection (SNMP) |  |  |
| CobraNet Audio |  |  |

[Other Network Interface Traffic](javascript:void(0))

These are the other network functions on the Q-SYS network and the Q-SYS Core network adapters they use.

| Function | LAN A | LAN B | AUX LAN |
| --- | --- | --- | --- |
| Audio Clocking (PTPv2) |  |  |  |
| Q-SYS Control Scripting |  |  |  |
| Q-SYS Softphone Control - SIP/TLS |  |  |  |
| Q-SYS Softphone Audio - RTP/SRTP |  |  |  |
| AES67 Streaming Audio |  |  |  |
| Dante Streaming Audio |  |  |  |
| Media Streaming, Rx/Tx |  |  |  |
| WAN Streaming, Rx/Tx |  |  |  |
