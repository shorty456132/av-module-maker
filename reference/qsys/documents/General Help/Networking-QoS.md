# Quality of Service (QoS)

> Source: https://help.qsys.com/Content/Networking/QoS.htm

# Quality of Service (QoS)

Q-SYS is a live audio, video, and control system, so real-time performance is critical within the network environment. QoS is required in the Q-LAN network to prevent non-real-time control and bulk communications from affecting performance of time-sensitive clocking, audio, and video traffic.

Q-SYS uses the DSCP field in the IP header to specify traffic priority to the network. The network must inspect, distinguish, and prioritize the following traffic classes. System administrators may choose to trust the DSCP values transmitted by Q-SYS or alternatively reassign new DSCP values based on these values or other distinguishing traffic characteristics. As long as traffic is properly prioritized, it is not necessary to preserve these exact DSCP values through the network.

To assign DSCP values in your Q-SYS design, go to File > Design Properties in Q-SYS Designer. You can select from Q-LAN, Audinate, and Manual presets.

[Prioritization for Q-LAN Traffic Only](javascript:void(0))

Select the Q-LAN preset for Q-LAN traffic optimization.

| Priority | DSCP Value | Binary Equivalent | Meaning | Traffic Type |
| --- | --- | --- | --- | --- |
| Highest | 46 | 101 110 | High Priority, Expedited Forwarding (EF) | PTPv2 clock distribution |
| Second Highest | 34 | 100 010 | AF41 | Q-SYS audio streams |
| Third Highest | 26 | 011 010 | AF31 | Q-SYS video streams |
| Lowest | 0 | 000 000 | Best Effort | Q-SYS control and management traffic (everything else) |

[Prioritization for Audinate Traffic](javascript:void(0))

Select the Audinate preset for Audinate (Dante) traffic optimization. Refer to the [Dante Audio](Dante_Audio.htm) topic for Dante networking requirements.

**Note:** Selecting the Audinate preset tells Q-SYS Designer to align DSCP markings with Audinate's.

| Priority | DSCP Value | Binary Equivalent | Meaning | Traffic Type |
| --- | --- | --- | --- | --- |
| Highest | 56 | 111 000 | CS7 | PTPv2 clock distribution |
| Second Highest | 46 | 101 110 | High Priority, Expedited Forwarding (EF) | Q-SYS audio streams |
| Third Highest | 26 | 011 010 | AF31 | Q-SYS video streams |
| Lowest | 0 | 000 000 | Best Effort | Control and management traffic (everything else) |

[Custom Prioritization](javascript:void(0))

You can change the DSCP settings for PTPv2, Q-SYS audio, and Q-SYS video to allow custom QoS mapping. You must, however, maintain the priority hierarchy of:

* PTPv2 highest
* Q-SYS Audio second highest
* Q-SYS Video third highest

**Note:** PTP, Audio, and Video queue priorities must also be maintained across any uplinks and cannot be shared with any identically-queued packets from other VLANs being sent via the same uplinks in a VLAN trunk.

[Troubleshooting QoS Issues](javascript:void(0))

Q-LAN audio packets must pass from source to destination within 280 Î¼s or less or they are considered too late. You can see detailed network performance statistics by enabling Verbose mode in Q-SYS Core and peripheral Status components in Q-SYS Designer:

1. Drag a Q-SYS Core or peripheral Status component into the schematic.
2. In the component Properties pane, set the Verbose property to 'Yes'.
3. Save and run the design to the Core.
4. Double-click the Status component to see statistics information:
   * "drop\_count" shows the number of packets that were delivered too late (outside of the 280 Î¼s time allowed on the network) and have therefore been disregarded by the destination Q-SYS device. This also applies to packets received out of sequential order.
   * "missing\_count" is a count of expected packets which were not received by the destination Q-SYS Device.
