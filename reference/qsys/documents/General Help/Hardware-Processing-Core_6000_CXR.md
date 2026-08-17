# Core 6000 CXR

> Source: https://help.qsys.com/Content/Hardware/Processing/Core_6000_CXR.htm

# Core 6000 CXR

The Q-SYS Core 6000 CXR processor is an industry-first solution that combines the processing capabilities of the Q-SYS realtime operating system with the compact, ruggedized, MIL-STD, NEBS and Marine compliant Dell PowerEdge XR11 server. Core 6000 CXR is the only IT-grade solution that brings audio, video, and control processing into marine applications.

This topic provides an overview of the Q-SYS Core 6000 CXR. These resources provide additional detailed information:

* [Specifications Sheet](https://www.qsys.com/resource-files/productresources/dn/dsp_cores/core_6000_cxr/Q_dn_core_6000_CXR_spec.pdf)
* [Architect & Engineering Specifications](https://www.qsys.com/resource-files/productresources/dn/dsp_cores/core_6000_cxr/q_dn_core_6000_cxr_archengspecs.txt)
* [Quick Start Guide](https://www.qsys.com/resource-files/productresources/dn/dsp_cores/core_6000_cxr/q_dn_core_6000_cxr_quickstartguide.pdf)

**Note:** For hardware specifications, regulatory compliance, or iDRAC information, visit the Dell server website at: [dell.com/servers](http://www.dell.com/servers).

[Features](javascript:void(0))

**Note:** Q-SYS Scaling Licenses expand the capabilities of the Core 6000 CXR. Refer to the [Licensing](../../Core_Manager/Core_Management/Licensing.htm) topic for more information.

| Feature | Core 6000 CXR |
| --- | --- |
| Total network I/O | 256 x 256, upgradeable to 512 x 512[1](#With2) |
| Onboard I/O | N/A |
| Software-based Dante capacity | 8 x 8 included, upgradeable to 512 x 512[2](#With) |
| USB audio channel count | N/A |
| AEC processors | 80, upgradeable to 160[2](#With) |
| VoIP instances | 64 |
| Onboard AV bridging (USB) | N/A |
| Onboard GPIO | N/A |
| Onboard RS232 control ports | 1 |
| Q-SYS peripheral limit | N/A |
| Size | 1RU |

###### 1. With optional scaling license. See the [Licensing](../../Core_Manager/Core_Management/Licensing.htm) topic for more information.

###### 2. With optional feature license. See the [Licensing](../../Core_Manager/Core_Management/Licensing.htm) topic for more information.

[Design Components](javascript:void(0))

The following Q-SYS Designer Software components are available for the Core 6000 CXR:

* [Status](../../Schematic_Library/core_status.htm)
* [Loudspeaker Monitor](../../Schematic_Library/loudspeaker_monitor.htm)
* [Serial Port](../../Schematic_Library/serial_port.htm)

[Connections and Callouts](javascript:void(0))

### Front Panel

1. Status and ID indicator â Enabled via Q-SYS Designer Software
2. Removable filtered bezel â Refer to Dell documentation for maintenance requirements
3. Power button
4. Q-SYS media drive (under bezel) â One 2.5-inch, 960 GB, SATA 6 Gb SSD drive. Additional drives not supported.
5. Information tag (under bezel) â Includes the product serial number and Q-SYS Support contact information
6. USB port â Not supported

### Rear Panel

1. PCIe expansion card riser 1 (slot 1) â Not supported
2. Serial communications RS232 (male DE-9) â For connection to serial devices
3. iDRAC dedicated port (RJ45) â For remote iDRAC access:

   Default IP = 192.168.0.120, Default username = root, Default password = calvin
4. LAN ports (four RJ45, 1000 Mbps) â From left to right: LAN A multimedia, LAN B multimedia, AUX A, AUX B
5. Power supply unit 1 (PSU1) â 1400 W, hot-plug, universal input
6. Power supply unit 2 (PSU2) â 1400 W, hot-plug, universal input
7. ID button â Press to identify the device in Q-SYS Designer Software
8. SFP ports (Quad Port 25GbE SFP28) â Not supported
9. VGA video output (female HD15) â Not supported
10. USB ports â Not supported
11. PCIe expansion card riser 3 (slot 3) â Not supported

[Configuring and Using iDRAC](javascript:void(0))

The Core 6000 CXR comes with Integrated Dell Remote Access (iDRAC). Refer to the Dell Server documentation.

### Configuring iDRAC

**Note:** The default iDRAC IP is 192.168.0.120.

1. Connect the dedicated management Ethernet port to the Ethernet switch.
2. During boot hit F10 to enter Lifecycle Controller setup.
3. In the left pane of the Home page, click Hardware Configuration.
4. In the right pane, click Configuration Wizards.
5. On the System Configuration Wizards page, click iDRAC Settings.
6. From the System Summary, select Network.
7. Enable IPv4, DHCP, and "Use DHCP to obtain DNS server address".
8. Select Back, Finish, and Exit.

### Using iDRAC

1. Launch a web browser and enter the iDRAC IP address as the URL.
2. Log in with default user name "root" and password "calvin".

**Tip:** The Dell EMC OpenManage Mobile smartphone app can also be used to access iDRAC.
