# Q-SYS Redundancy

> Source: https://help.qsys.com/Content/Redundancy/Redundancy.htm

# Q-SYS Redundancy

Well-designed products and proper installation is required to ensure basic reliability, but faults eventually occur. Assuming faults are rare, it is sufficient for the system to back up a single major fault if this condition is flagged for immediate service. In addition, fault-tolerant systems must be monitored and tested periodically to ensure that all parts, including the backup devices, are working. Q-SYS covers these needs automatically.

Fault tolerance in Q-SYS is achieved by redundancy. The Q-SYS Core, I/O peripherals, network, and amplifiers can be redundant, and will automatically failover if any of the components fail. In less critical applications, only the elements of most concern need be duplicated.

[Configurations](javascript:void(0))

Q-SYS is capable of several redundant configurations to ensure a high level of overall system reliability.

* 2N Core redundancy - Two Cores, primary and redundant, communicating with each other and peripherals to verify system health, and to synchronize control settings.
* 2N I/O redundancy - For each peripheral, you can have a backup peripheral.
* N1 Amplifier redundancy - One amplifier can back up from one to eight amplifiers with the Q-SYS DataPort Amplifier Backup Panel.
* 2N Network redundancy - Two separate networks - In this configuration, you can have each Q-SYS Core and/or I/O Frame connected to both networks.

[Network Redundancy](javascript:void(0))

Both the Core and the I/O Frame have two network ports, LAN A (primary), and LAN B (backup). The LAN B port on I/O Frame becomes active when it is configured in Q-SYS Designer as "Is Network Redundant" and connected. Because the I/O Frame is configured in the design file, the Core recognizes it as being on LAN B as well as LAN A. During operation, the Core routes audio and control signals to both ports, so if LAN A, or a part of LAN A fails, the Core switches to LAN B with no failover time.

To learn more, see [Network Redundancy](Redundancy_Network.htm).

[Q-SYS Hardware Redundancy](javascript:void(0))

The Q-SYS Core processor and supported devices can have backups connected to the network. These are identified in Q-SYS Designer Software as being redundant. The backup Core communicates with the primary to ensure it is up to date with any changes made on the primary, and to monitor the primary Core's health.

To learn more about Q-SYS hardware redundancy, see:

* [Q-SYS Core Redundancy](Redundancy_Core.htm)
* [I/O Hardware Redundancy](Redundancy_IO_Hardware.htm)
* [Amplifier Redundancy](Redundancy_Amplifier.htm)
