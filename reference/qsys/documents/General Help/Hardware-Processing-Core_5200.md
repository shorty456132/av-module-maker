# Core 5200

> Source: https://help.qsys.com/Content/Hardware/Processing/Core_5200.htm

# Core 5200

For large installations or for IT customers wishing to deploy audio, video and control (AV&C) solutions as a building-wide service throughout the enterprise, QSC has partnered with Dellâ¢ to bring an industry-first integration combining the processing capabilities of the Q-SYS realtime operating system with the world-class Dell R740 server platform resulting in the only IT grade AV&C solution available today, built on standard, off-the-shelf IT hardware.

**Note:** This topic provides an overview of the Q-SYS Core 5200. To see a list of related documentation and specifications, see the [Specifications and Documentation](#Specific) section.

[Features](javascript:void(0))

| Feature | Core 5200 |
| --- | --- |
| Local I/O Channels | N/A |
| Network Audio Channels | 512 x 512 |
| AEC Processors | 160 |
| Multitrack Audio Players | 16 (upgradable to 128) |
| Local I/O Card Capacity | N/A |
| VoIP Instances | 64 |
| Q-SYS peripheral limit | It is recommended not to exceed 128 NL, NM, or QIO Series peripherals in a design in any combination. |

[Design Components](javascript:void(0))

The following Q-SYS Designer components are available for the Core 5200:

* [Status](../../Schematic_Library/core_status.htm)
* [Loudspeaker Monitor](../../Schematic_Library/loudspeaker_monitor.htm)
* [Serial Port](../../Schematic_Library/serial_port.htm)

[Connections and Callouts](javascript:void(0))

### Front Panel

1. Power Button
2. ID Indicator (enabled via Q-SYS Designer)
3. VGA Video Output (female HD-15)
4. LCD Navigation Buttons
5. Slide-Out Information Tag: Provides Q-SYS contact information for support and the QSC product serial number.
6. LCD (displays Q-SYS Core name, status or health alerts)
7. Q-SYS High Capacity 960GB Media Drive

   **Note:** The Q-SYS Core 5200 comes standard with an MTP-16, 16-track player. 32, 64 and 128-track upgrades are available.
8. USB 3.0 Host Ports

### Rear Panel

1. ID Indicator (enabled via Q-SYS Designer)
2. iDRAC8 Enterprise Port (RJ45)

   **Note:** The iDRAC8 port is configured with a static IP address by default (192.168.0.120)
3. Serial Communications/RS232 (male DE-9)
4. VGA Video Output (female HD-15)
5. USB 2.0 Host Ports
6. Q-SYS LAN A and LAN B Multimedia Ports (RJ45 x2)
7. Q-SYS AUX Ports (RJ45 x 2)
8. Power Supply Unit 1 (universal input, 750W)
9. Power Supply Unit 2 (universal input, 750W)

[Configuring and Using iDRAC](javascript:void(0))

The Core 5200 comes with Integrated Dell Remote Access (iDRAC). Refer the Dell Server documentation.

### Configuring iDRAC

1. Connect the dedicated management Ethernet port to the Ethernet switch
2. During boot hit F10 to enter Life Cycle Controller setup
3. Under "Things to do" select "Configure server for remote access (iDRAC)"
4. Select Network
5. Under "IPv4 settings" enable IPv4, DHCP and "Use DHCP to obtain DNS server address"
6. Select Back, Finish and Exit

### Using iDRAC

1. Launch an Internet browser and enter idrac-<service tag> as the URL
2. (Replace <service tag> with the actual service tag that can be located on the Core 5200 chassis)
3. The default login user name is root
4. The default login password is calvin

**Tip:** The Dell EMC OpenManage Mobile smartphone app can be used to access iDRAC.

[Specifications and Documentation](javascript:void(0))

* See the [Core 5200](https://www.qsys.com/systems/products/q-sys-platform/products-peripherals-accessories/q-sys-cores/core-5200/) product page on the Q-SYS website for documentation and resources, including the Quick Start Guide, Specifications Sheet, and documentation from Dell.
* For additional information regarding hardware specifications, regulatory compliance, or iDRAC8, go to the Dell server website at: [www.dell.com/servers](http://www.dell.com/servers).
* The Core 5200 comes with the sliding ReadyRails (B6) kit for square hole racks (EIA-310-E compliant).

**Note:** Refer to the [Server Rack Rails â Information and Resources](https://www.dell.com/support/kbdoc/en-us/000139234/server-rack-rails-information-and-resources?lang=en) page and the [Dell Enterprise Systems Rail Sizing and Rack Compatibility Matrix](https://i.dell.com/sites/doccontent/business/solutions/engineering-docs/en/Documents/rail-rack-matrix.pdf) on the Dell website for detailed information on rack-mounting combinations and adapters.
