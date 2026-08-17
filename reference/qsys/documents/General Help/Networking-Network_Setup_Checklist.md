# Q-SYS Network Setup Checklist for Designers and Integrators

> Source: https://help.qsys.com/Content/Networking/Network_Setup_Checklist.htm

# Q-SYS Network Setup Checklist for Designers and Integrators

To help ensure a smooth and successful implementation of a Q-SYS network, please follow this checklist throughout the planning, design, and installation phases.

[Planning](javascript:void(0))

* Before starting a Q-SYS network project, make sure at least one Q-SYS certified person will be involved from start to finish.
* Gather information:
  + If the Q-SYS system is to be added to an existing network, gather information about the network from the client.
  + If the Q-SYS system is to be a new network, gather information about its intended scope, location, etc., from the client.
* Review the [Network Switch Requirements](Switches_Infrastructure.htm#NS-Requirements) to ensure all necessary information for the setup is obtained.
* Check the [Known Issues](https://support.qsys.com/en_US/known-issues) page prior to deployment.
* Configure and bench test the switches before bringing them on site, if possible. Be sure to follow the QoS configuration steps in the setup guides closely.

### Bench Testing

1. On the switch, attach all options (SFP and/or SFP+ modules, power supplies, stacking cables, etc.).
2. Turn on the switch and make sure the boot process completes and the POST (Power On Self-Test) shows no errors. To view POST results, you may need an RS232 console connection.
3. Inspect the switch for normal fan performance (e.g., air flow, no unusual fan noise once the switch finishes its boot cycle, etc.) and no unusual electronic odor.
4. Document the MAC addresses, serial numbers, and product numbers. Take photos, if that will help.
5. Configure the IP address on the switch and update its firmware if needed. If you are upgrading the switch firmware, please read the switch manufacturerâs release notes carefully to understand the upgrade process.
6. Label each switch with its intended on-site deployment location.
7. Configure QoS in the switch per the Q-SYS switch configuration guides.
8. Connect the Q-SYS Core to the Q-SYS I/O peripherals to the switch or switches to verify the basic operation of the QoS configuration. To verify QoS, go into Q-SYS Designer and enable Verbose Mode in the Status Core block. The overrun and timeout counts should be zero.
9. If the Status Core block shows non-zero overrun and timeout counts, check the following:
   * Verify that the ports are 1 Gbps.
   * Verify that the switch is one of the models qualified by QSC.
   * Try a different Ethernet cable (Cat6A type).
   * Try a different switch port.

10. If you have enabled and configured IP IGMP snooping and/or multicast routing (PIM spares mode) on the network switches, verify that all the Q-SYS products can be seen in Q-SYS Designer.
11. If possible, allow the Q-SYS and network devices to run for at least two hours, and up to 24 hours, as a basic burn-in period. After burn-in, view the Status Core block in Q-SYS Designer and verify that the overrun and timeout counts are both zero. Also, go into the switch interface (this will vary among brands and models) and check the statistics to see if any errors have been detected on switch ports and if any other items (fans, power supplies, SFP, etc.) are faulty.
12. Document the bench test results, including any anomalies discovered and the corrective actions taken. Save all the running configuration in each device and back them all up.
13. Package the Q-SYS and network equipment in their original boxes. Label each box with its intended on-site deployment location.

Notes:

* Keep your system documentation up to date, including system testing, equipment labeling, and cabling.
* Back up all device configurations to your computer or other accessible storage.
* Calculate network bandwidth based on the expected traffic used in bench testing. To avoid issues, do this prior to deployment.

[Deployment](javascript:void(0))

* Deploy equipment on site and test it.
  1. Inspect the customer site and make sure it is ready for installation (cleanliness, power, security, equipment racks in place, patch panel and cabling completed, etc.).
  2. Inspect the rack clearances in front and in back and make sure they will be adequate for good airflow and cable management.
  3. Using the rack elevation drawings, make sure that you, the allied trade personnel, and the customer agree on equipment position in the rack or racks.
  4. Install the rack mounting hardware on the pieces of equipment and install them into the rack or racks.
  5. Connect all the cables to the switch or switches and also connect the Q-SYS equipment to the network. Dress the cabling neatly and orderly following best practices established by InfoComm.
  6. Turn on the switch or switches. Verify that all complete their boot up processes.
  7. Log into each switchâs interface and verify that its Ethernet ports are operational and that those in use have valid links. On ports connected to Q-SYS devices, verify also that the correct MAC address for each device is on each one. On ports connected to non-Q-SYS devices, you might be able to use CDP or LLDP to discover what devices are connected. Verify that the switch has detected no errors.
  8. Verify that each Q-SYS device can be seen by Q-SYS Designer.
  9. Test the Q-SYS equipment by running various types of audio program that the customer will be using) on the network. In Q-SYS Designer, view the Status Core block and make sure the overrun and timeout counts are both zero.
  10. Document the test results as well as any changes made on site.
  11. Back up all the running configurations.

* Document any issues discovered, as well as changes to the design to the design.

* Tune the equipment as needed, and back up all final configurations. Examples of equipment tuning include:
  + Correcting improper cable management: For example, aggressively bending optical fiber cables beyond the recommended minimum bend radius can cause errors on the fiber links. To correct, re-route the cables.
  + Correcting fiber signal levels: If a single-mode fiber link runs too hotâe.g., the light signal is too strongâinsert an appropriate attenuator to bring the signal to within the receiverâs specifications. Fiber attenuators are cataloged in dB of light attenuation.
  + Altering a touch screen layout, per the customerâs wishes.
  + Adding a UPS to the equipment rack because of frequent power failures.

* Conduct appropriate training of the clientâs personnel.
