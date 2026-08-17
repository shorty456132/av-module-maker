# Multicast Traffic

> Source: https://help.qsys.com/Content/Networking/Multicast_Traffic.htm

# Multicast Traffic

For Q-SYS to function properly when spread across a layer 3 network, the network must be configured to route Q-SYS unicast traffic packets between subnets (refer to [Addressing & Routing](Addressing_Routing.htm)), but also must be configured to route multicast traffic.

**Note:** Multicast routing may not be supported by some layer 3 switches, or may require additional licensing. Some 3rd-party devices (for example, AES67) may have limitations with layer 3 multicast routed networks. For more information, see [Other Networked Audio](Other_Networked_Audio.htm).

[Multicast Protocols](javascript:void(0))

These Q-LAN protocols require routing of multicast traffic.

#### Q-SYS Discovery Protocol (QDP)

UDP destination IP 224.0.23.175 â registered exclusively to QSC, LLC by IANA on ports 2467-2470 (multicast). This is used to discover Q-SYS products on the network by name regardless of IP address. To advertise network presence, one multicast QDP packet is sent every second from Q-SYS peripherals and the PC running Q-SYS Designer Software.

**Note:** PTZ-IP Series cameras do not use QDP. Instead, they use Web Services Discovery. See [Multicast Addressing](#Multicas).

#### IEEE 1588 PTPv2

UDP Destination IP 224.0.1.129 â registered to NIST/IEEE.

[Multicast Addressing](javascript:void(0))

These Q-SYS devices and streaming I/O peripherals support multicast traffic.

**Note:** All Q-SYS devices support auto-assignment of multicast addresses. 'Auto' mode uses a combination of the device type (Camera, Video Endpoint, AES67) and MAC address of the Core's primary LAN interface to seed addresses. This scheme results in a very low chance of address overlap. However, if your site contains a large quantity of Cores that weren't purchased at the same time, there is a higher chance of address overlap. If this happens, use 'Manual' mode and specify custom addressing. To learn more see the [Network > Multicast](../Core_Manager/Core_Management/Multicast.htm) topic in Core Manager Help.

#### PTZ-IP Series Cameras

* Web Services Discovery: Multicast UDP 239.255.255.250 on Port 3702.
* Video stream multicasting: User-configurable in Q-SYS Core Manager. Use 'Auto' mode in Q-SYS Core Manager > Network > [Network > Multicast](../Core_Manager/Core_Management/Multicast.htm) to allow the system to supply multicast addresses.
* For more information, see [Video Streams](Clocking_Audio_Video_Control.htm#Video).

#### NC Series Cameras

* mDNS: 239.255.255.251 (applicable to all NC Series cameras except NC-Pro15x)
* Q-SYS Discovery Protocol (QDP): Multicast UDP 224.0.23.175 on Ports 2467-2470 and Unicast on Port 6504
* Video stream multicasting: User-configurable in Q-SYS Core Manager. Use 'Auto' mode in Q-SYS Core Manager > Network > [Network > Multicast](../Core_Manager/Core_Management/Multicast.htm) to allow the system to supply multicast addresses.
* For more information, see [Video Streams](Clocking_Audio_Video_Control.htm#Video).

#### Network Video Endpoints

* User-configurable in Q-SYS Core Manager. Use 'Auto' mode to allow the system to supply multicast addresses in the range 233.252.0.0 - 233.252.255.255. To learn more, see the [Network > Multicast](../Core_Manager/Core_Management/Multicast.htm) topic in Core Manager Help.
* For more information, see [Video Streams](Clocking_Audio_Video_Control.htm#Video).

#### AES67 Transmitter

User-configurable in the AES67 Transmitter component, with the range configurable in Q-SYS Core Manager. Use 'Auto' mode to allow the system to supply multicast addresses in the range 233.254.0.0 - 233.254.255.255. To learn more, see the [Network > Multicast](../Core_Manager/Core_Management/Multicast.htm) topic in Core Manager Help.

**Note:** The AES67 Transmitter multicast address range applies to both the AES67 Transmitter component and System Link Transmitter component audio pin connections.

[IGMP Requirements](javascript:void(0))

Q-SYS devices implement Internet Group Management Protocol Version 2 (IGMPv2). IGMP allows Q-SYS devices to register with the switched network to receive specific multicast transmissions. Without IGMP enabled, multicast traffic is treated in the same manner as a broadcast transmission, which forwards packets to all ports on the network. With IGMP enabled, multicast traffic is only forwarded to ports that are members of that Multicast group.

#### IGMP Querier

For IGMP to function properly, an IGMP querier must be present on the VLAN. Otherwise, Q-SYS devices â which depend upon multicast packets for device discovery and sample clock â will cease to function. This is because the IGMP snooping filters in switches belonging to this VLAN restrict multicast transmissions to any switch ports for which it has not detected a Membership Group Report for a period of time (typically two to three minutes).

Q-SYS devices are designed to generate IGMPv2 Multicast Group Requests once at startup, and then only when queried by an IGMP querier somewhere on the VLAN. If no switch or router on a given VLAN has an IGMP querier enabled, IGMP snooping must be disabled on all switches or on ports assigned to VLANs utilizing multicast data.

**Note:** Some switches support only a single VLAN â for example, the Q-SYS NS Series.

#### IGMP Fast-Leave (Required for NV-32-H Multicasting)

If your design contains an NV-32-H Encoder that is multicasting to multiple NV-32-H Decoders, you must enable the IGMP "fast-leave" option on the network switch. This prevents issues with temporary garbled video when switching AV sources.

For an example of a multicasting configuration, see [HDMI I/O (NV-32-H)](../Schematic_Library/streamer_hdmi_switcher.htm).

#### Mixed Multicast Sources

When mixing Q-LAN with other sources of multicast, such as video encoders, IGMP is required to prevent foreign multicasts from being sent to ports used for Q-SYS equipment (and vice-versa).

#### Multiple Network Switches

If your network contains more than one switch:

* Enable the IGMP querier on the switch to which the Q-SYS Core is connected.
* There must only be one querier per physical network or VLAN (if the switch supports a per-VLAN configuration).
* Enable IGMP snooping on all switches.

[PIM-SM Requirements](javascript:void(0))

Protocol Independent Multicast Sparse Mode (PIM-SM) is the most common and recommended protocol for forwarding multicast data across routers, as it is the most efficient on network resources for paths and ports that don't need Q-LAN multicast data.

PIM-SM must be configured properly to maintain network performance.

**Note:** When deploying Q-SYS in a Layer 3 routed environment using PIM-SM, a Rendezvous Point (RP) must be configured within the multicast domain. The RP must be reachable from all multicast senders and receivers to ensure proper group registration and multicast traffic flow.
