# Network Redundancy

> Source: https://help.qsys.com/Content/Redundancy/Redundancy_Network.htm

# Network Redundancy

Q-SYS Core processors and many Q-SYS peripheral devices have two LAN ports: LAN A and LAN B. LAN A is the default, primary port. LAN B is the backup or redundant port. Peripherals can be configured in Q-SYS Designer Software to use LAN B as a backup ("Is Network Redundant" property). For each audio peripheral with the "Is Network Redundant" property enabled, the Core establishes redundant Q-LAN audio streams to and from that peripheral. These streams are always active, allowing the Core and peripherals to use the audio streams from LAN B if there is a problem with LAN A.

**Note:** The Core only establishes redundant Q-LAN audio and control streams with those peripherals that are configured in Q-SYS Designer as "Is Network Redundant" (using LAN B). This means that those peripherals not configured and physically wired to use both LAN ports cannot make use of network redundancy.

[Network Failover](javascript:void(0))

If a port, switch, or link is lost, there is no failover time, and no interruption of the audio stream. The control communication streams, while not necessarily constantly replicated over the two ports, will also failover seamlessly.

[Network Requirements for Redundancy](javascript:void(0))

There are network configuration and topology considerations to understand when implementing Q-SYS Network Redundancy. Refer to [Network Switches & Infrastructure](../Networking/Switches_Infrastructure.htm) and [Addressing & Routing](../Networking/Addressing_Routing.htm).

[Stream Usage](javascript:void(0))

Redundant Q-LAN streams are counted as one or two streams depending on the Core model:

| Core Model | Stream Quantity Consumed per Redundant Q-LAN Stream |
| --- | --- |
| Core Nano | 2 |
| Core 8 Flex | 2 |
| NV-32-H (Core Capable) | 2 |
| Core 110f, Core 110c | 2 |
| Core 24f | 2 |
| Core 510i, Core 510c | 2 |
| Server Core X10 | 2 |
| Core 610 | 2 |
| Server Core X20r | 2 |
| Core 5200 | 1 |
| Core 6000 CXR | 1 |
