# Core 610

> Source: https://help.qsys.com/Content/Hardware/Processing/Core_610.htm

# Core 610

The Q-SYS Core 610 represents the next-generation of Q-SYS processing, pairing the Q-SYS OS with enterprise-grade Dell COTS server hardware to deliver a flexible and scalable audio, video and control solution for a vast range of larger scale applications. It is a fully networked AV&C processor, letting you distribute network I/O where itâs most convenient. The Core 610 is equally suited for centralized processing for multiple meeting rooms in enterprise applications, as well as handling larger spaces or venues in hospitality, entertainment, or transit hubs.

**Note:** This topic provides an overview of the Q-SYS Core 610. To see a list of related documentation and specifications, see the [Specifications and Documentation](#Specific) section.

[Features](javascript:void(0))

| Feature | Core 610 |
| --- | --- |
| Total network I/O | 256 x 256 |
| Onboard I/O | N/A |
| Software-based Dante capacity | 8 x 8 included, upgradeable to 256 x 256[1](#With) |
| USB audio channel count | N/A |
| AEC processors | 64 |
| VoIP instances | 64 |
| Onboard AV bridging (USB) | N/A |
| Onboard GPIO | N/A |
| Onboard RS232 control ports | 1 |
| Q-SYS peripheral limit | It is recommended not to exceed 128 NL, NM, or QIO Series peripherals in a design in any combination. |
| Size | 1RU |

###### 1. With optional feature license. See the [Licensing](../../Core_Manager/Core_Management/Licensing.htm) topic for more information.

[Design Components](javascript:void(0))

The following Q-SYS Designer Software components are available for the Core 610:

* [Status](../../Schematic_Library/core_status.htm)
* [Loudspeaker Monitor](../../Schematic_Library/loudspeaker_monitor.htm)
* [Serial Port](../../Schematic_Library/serial_port.htm)

[Connections and Callouts](javascript:void(0))

### Front Panel

1. Status and ID indicator â Enabled via Q-SYS Designer Software
2. Bezel lock
3. Removable active bezel
4. LCD navigation buttons
5. LCD â Displays Q-SYS Core processor name, status, and health alerts.
6. Power button
7. USB port â Not supported
8. Information tag â Includes the product serial number and Q-SYS Support contact information
9. Q-SYS Media Drive â One 2.5-inch, 480 GB, SATA 6 Gb SSD drive. Additional drives not supported.

### Rear Panel

1. Serial communications RS232 (male DE-9) â For connection to serial devices
2. On-board LAN ports â Not supported
3. Q-SYS LAN ports (RJ45, 1000 Mbps) â From left to right: LAN A, LAN B, AUX A, AUX B
4. Power supply unit (PSU) â 450W
5. ID button and indicator â Press to identify the device in Q-SYS Designer Software
6. CMA jack â For connection to a cable management ar
7. USB ports â Not supported
8. iDRAC dedicated port (RJ45) â For remote iDRAC access:

   Default IP = 192.168.0.120, Default username = root, Default password = calvin
9. VGA video output (female HD15) â Not supported

[Configuring and Using iDRAC](javascript:void(0))

The Core 610 comes with Integrated Dell Remote Access (iDRAC). Refer to the Dell Server documentation.

### Configuring iDRAC

1. Connect the dedicated management Ethernet port to the Ethernet switch.
2. During boot hit F10 to enter Lifecycle Controller setup.
3. Under "Things to do" select "Configure server for remote access (iDRAC)".
4. Select Network.
5. Under "IPv4 settings" enable IPv4, DHCP and "Use DHCP to obtain DNS server address".
6. Select Back, Finish and Exit.

### Using iDRAC

1. Using the front panel LCD navigation buttons and display, obtain the iDRAC IP address.
2. Launch a web browser and enter the iDRAC IP address as the URL.
3. Log in with default user name "root" and password "calvin".

**Tip:** The Dell EMC OpenManage Mobile smartphone app can also be used to access iDRAC.

[Specifications and Documentation](javascript:void(0))

* See the [Core 610](https://www.qsys.com/products-solutions/q-sys/processing/core-610/) product page on the Q-SYS website for Q-SYS documentation and resources, including the Quick Start Guide and Specifications Sheet.
* Refer to the Dell [Specification Sheet](https://i.dell.com/sites/csdocuments/Product_Docs/en/dell-emc-poweredge-r250-spec-sheet.pdf) and [Technical Guide](https://i.dell.com/sites/csdocuments/Product_Docs/en/dell-emc-poweredge-r250-technical-guide.pdf) for detailed information from Dell.
* For additional information regarding hardware specifications, regulatory compliance, or iDRAC, go to the Dell server website at: [dell.com/servers](http://www.dell.com/servers).
* The Core 610 comes with the static ReadyRails (A4) kit for square hole racks (EIA-310-E compliant).

**Note:** Refer to the [Server Rack Rails â Information and Resources](https://www.dell.com/support/kbdoc/en-us/000139234/server-rack-rails-information-and-resources?lang=en) page and the [Dell Enterprise Systems Rail Sizing and Rack Compatibility Matrix](https://i.dell.com/sites/doccontent/business/solutions/engineering-docs/en/Documents/rail-rack-matrix.pdf) on the Dell website for detailed information on rack-mounting combinations and adapters.
