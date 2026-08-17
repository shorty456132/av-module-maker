# Q-SYS Core Redundancy

> Source: https://help.qsys.com/Content/Redundancy/Redundancy_Core.htm

# Q-SYS Core Redundancy

A second or Backup Core can be paired with the Primary Core in an installation. Initially, the Primary Core is the Active Core, and the Backup Core is the Standby Core.

In a Core-redundant system, the Standby Core is responsible for constantly communicating with the Active Core so as to verify the health of the Active Core, and to synchronize its control settings, snapshots and event schedules with the Active Core. The Standby Core also communicates with the peripherals so as to verify its readiness to take over.

[Failover Process](javascript:void(0))

If the Standby Core detects a fault with the Active Core, it establishes full audio streaming and control communications with peripherals and becomes the "active" Core. If the Primary, for whatever reason, does not actually go into standby during a failover, the Backup has priority and remains the Active Core.

During a failover, the audio peripherals are muted, and are then un-muted once the backup becomes active. An automatic failover, in which the backup must automatically decide to go active, takes about 10 seconds. If the backup is manually instructed to go active, the process takes about 3 seconds.

After a failover, Q-SYS does not automatically change back to the failed Core when the Core recovers. This is to prevent additional audio gaps. You can manually change back at an appropriate time.

Note that:

* The Core with the most connected peripherals will become active.
* If there are no peripheral devices the primary Core will become active after a network failure.
* If there are no peripheral devices the longest-running Core will become active after a Core reboot.
* If the Primary Core is set to the highest-priority clock master and the backup Core set to the second highest-priority, there is a short audio stream dropout if the Primary Core loses connection to the network or is rebooted.
* Failover time has not yet been tested with large systems.

[Requirements](javascript:void(0))

To enable Core redundancy in your design, set the **Is Redundant** property in Core Properties to 'Yes', and then specify the Backup Core name. Both the primary and backup Cores must be present and online during system installation so that both get configured with the proper design data. Additional requirements are listed below.

**Note:** The NV-32-H (Core Capable) does not support Core Redundancy.

[Licensing Requirements](javascript:void(0))

If a Feature License is required, it must be installed on both the Primary and Backup Q-SYS Core processor.

To learn more about Q-SYS Feature Licensing requirements, see the [Licensing](../Core_Manager/Core_Management/Licensing.htm) topic in Core Manager Help.

[Network Services Requirements](javascript:void(0))

A Core-redundant system requires proper configuration in Q-SYS Core Manager > [Network > Services](../Core_Manager/Core_Management/Network_Services.htm):

* Ensure that the Q-SYS Core Redundancy network service is enabled on both the Primary Core and Backup Core. This service is required if Core Redundancy is configured in the Q-SYS design file.
* Ensure that all network services for both the Primary Core and Backup Core are configured the same.

**Tip:** For a description of all network services, see the [Network Interfaces, Services, & Protocols](../Networking/Interfaces_Services.htm) topic.

[Core 110f Requirements](javascript:void(0))

If you are configuring a Core 110f processor for redundancy, note the following:

* Mic/Line Inputs â Wire the inputs in parallel, for active circuitry devices requiring phantom power, and devices not requiring phantom power such as dynamic microphones.
* Mic/Line Outputs â Redundant connections are not supported.
* Flex Inputs â Wire the inputs in parallel, for active circuitry devices requiring phantom power, and devices not requiring phantom power such as dynamic microphones.
* Flex Outputs â Redundant connections are not supported.
* **RS232** â Redundant connections are not supported by RS232 technology.
* USB â Redundant connections are not supported by USB technology.
* Telephone (POTS) â Redundant connections are not supported by POTS technology.
* GPIO Inputs and Outputs â See [GPIO Requirements](#GPIO).

**Note:** Redundant configurations can include Core 110f v1 and v2 models. However, it is crucial to ensure that GPIO is disabled in such designs to ensure proper functionality.

[Core 8 Flex Requirements](javascript:void(0))

* **Flex Inputs** â Wire the inputs in parallel, for active circuitry devices requiring phantom power, and devices not requiring phantom power such as dynamic microphones.
* **Flex Outputs** â Redundant connections are not supported.
* **USB** â Redundant connections are not supported by USB technology.
* **RS232** â Redundant connections are not supported by RS232 technology.
* **GPIO Inputs and Outputs** â See [GPIO Requirements](#GPIO).

[GPIO Requirements](javascript:void(0))

**GPIO Inputs** â For GPIO inputs that do not rely on the +12v power output or internal pull-up resistors, wire the GPIO pins in parallel except when you are using a high impedance analog source such as a potentiometer.

**GPIO Outputs** â Redundant connections are not supported.

[Script Requirements](javascript:void(0))

Currently, scripts are only executed on the active Core, and not on the standby Core. Additionally, read-only controls are not synchronized between the Cores.
