# Server Core X20r

> Source: https://help.qsys.com/Content/Hardware/Processing/Server_Core_X20r.htm

# Server Core X20r

The Q-SYS Server Core X20r represents the next-generation of Q-SYS processing, pairing the Q-SYS OS with enterprise-grade Dell COTS server hardware to deliver a flexible and scalable audio, video and control solution for a vast range of larger scale applications. It is a fully networked AV&C processor, letting you distribute network I/O where itâs most convenient. The Server Core X20r is equally suited for centralized processing for multiple meeting rooms in enterprise applications, as well as handling larger spaces or venues in hospitality, entertainment, or transit hubs.

**Note:** This topic provides an overview of the Server Core X20r. To see a list of related documentation and specifications, see the [Specifications](#Specifications) section.

[Features](javascript:void(0))

* 384 x 384 Network Audio Channels
* Up to 256 x 256 Software Dante audio channels (8 x 8 included)
* 128 AEC processors
* Up to 256 Multitrack audio players (16 channels by default)
* 64 VoIP instances

[Design Components](javascript:void(0))

The following Q-SYS Designer Software components are available for the Server Core X20r:

* [Status (Core)](../../Schematic_Library/core_status.htm)
* [Loudspeaker Monitor](../../Schematic_Library/loudspeaker_monitor.htm)
* [Serial Port (Core and I/O Devices)](../../Schematic_Library/serial_port.htm)

[Connections and Callouts](javascript:void(0))

### Front Panel

1. **Status and ID indicator** â Enabled via Q-SYS Designer Software
2. **Bezel lock**
3. **Removable active bezel**
4. **LCD navigation buttons**
5. **LCD** â Displays Q-SYS Core processor name, status, and health alerts.
6. **Power button**
7. **USB port** â Not supported
8. **Information tag** â Includes the product serial number and Q-SYS Support contact information
9. **Q-SYS Media Drive** â (Behind bezel) One 2.5-inch, 480 GB, SATA SSD drive. Additional drives not supported.

### Rear Panel

1. **Serial communications RS232 (male DE-9)** â For connection to serial devices
2. **On-board LAN ports** â Not supported
3. **Q-SYS LAN ports (RJ45, 1000 Mbps)** â From left to right: LAN A, LAN B, AUX A, AUX B
4. **Dual redundant power supply units (PSUs)** â 600W each
5. **ID indicator** â Enabled via Q-SYS Designer Software
6. **USB ports** â Not supported
7. **iDRAC dedicated port (RJ45)** â For remote iDRAC access: Default IP = 192.168.0.120, Default username = root, Default password = calvin
8. **VGA video output (female HD15)** â Not supported

[Configuring and Using iDRAC](javascript:void(0))

The Core X20r comes with Integrated Dell Remote Access (iDRAC). Refer to the Dell Server documentation.

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

[Specifications](javascript:void(0))

* For complete product specs, refer to the Specifications Sheet on the Server Core X20r product page at qsys.com.
* Refer to the Dell [Specification Sheet](https://i.dell.com/sites/csdocuments/Product_Docs/en/dell-emc-poweredge-r250-spec-sheet.pdf) and [Technical Guide](https://i.dell.com/sites/csdocuments/Product_Docs/en/dell-emc-poweredge-r250-technical-guide.pdf) for detailed information from Dell.
* For additional information regarding hardware specifications, regulatory compliance, or iDRAC, go to the Dell server website at: [dell.com/servers](http://www.dell.com/servers).
* The Server Core X20r comes with the static ReadyRails (A4) kit for square hole racks (EIA-310-E compliant).

**Note:** Refer to the [Server Rack Rails â Information and Resources](https://www.dell.com/support/kbdoc/en-us/000139234/server-rack-rails-information-and-resources?lang=en) page and the [Dell Enterprise Systems Rail Sizing and Rack Compatibility Matrix](https://i.dell.com/sites/doccontent/business/solutions/engineering-docs/en/Documents/rail-rack-matrix.pdf) on the Dell website for detailed information on rack-mounting combinations and adapters.
