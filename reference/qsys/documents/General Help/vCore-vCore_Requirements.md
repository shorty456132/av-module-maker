# vCore Requirements

> Source: https://help.qsys.com/Content/vCore/vCore_Requirements.htm

# vCore Requirements

Read this topic to understand what platforms are supported for vCore and their requirements, licensing requirements, as well as the hardware and schematic elements that are supported with vCore.

[Supported Platforms](javascript:void(0))

[Windows](javascript:void(0))

**CAUTION:** Windows 'Sleep Mode' will interrupt communication between a Virtual Core and its Q-SYS Designer Software instances. When hosting a Virtual Core on a Windows PC, be sure to disable Sleep Mode in Windows Settings.

* 64-bit Processor with Second Level Address Translation (SLAT)
* CPU support for VM Monitor Mode Extension (VT-c on Intel CPU)
* Minimum 8 GB memory with 2 GB assigned to each vCore VM image
* Minimum 2 GB disk space
* Must be enabled in BIOS:
  + Virtualization Technology

    **Note:** May have different labelling depending on motherboard manufacturer
  + Hardware Enforced Data Execution Prevention
* Supported Windows Operating Systems
  + Windows 11 Enterprise, Pro, Education
  + Windows Server 2022
  + Windows Server 2019
  + Microsoft Hyper-V Server 2019

[Linux KVM](javascript:void(0))

* x86 System running recent Linux kernel with:
  + Intel Processor with VT (virtual technology) extensions
  + AMD Processor with SVM extensions (also called AMD-V)
  + More Xen supported processors available at <https://wiki.xenproject.org/wiki/VTd_HowTo>
* Balanced memory for guest and host OS (1GB minimum for host)

[VMware ESXi](javascript:void(0))

* See [VMware Compatibility Guide - System Search](https://www.vmware.com/resources/compatibility/search.php) for full list of supported systems
* Supported server platform
* Multi-core 64-bit x86 processors with at least 2 CPU cores
* NX/XD bit enabled for the CPU in the BIOS
* Minimum 4 GB physical memory; providing at least 8 GB to run virtual machines in typical production environments
* Support for hardware virtualization (Intel-VT-x or AMD RVI) must be enabled
* One or more Gigabit or faster Ethernet controllers
* Boot disk with minimum 32 GB persistent storage such as HDD, SSD, or NVMe
  + Use USB, SD and non-USB flash media devices only for ESXi boot bank partitions

  **Note:** Boot device must not be shared between ESXi hosts
* SCSI disk or local, non-network RAID LUN with unpartitioned space for virtual machines

**Note:** For Serial ATA (SATA), a disk connected through supported SAS controllers or supported on-board SATA controllers. SATA disks are considered remote, not local. These disks are not used as a scratch partition by default because they are seen as remote.

[Licensing Requirements](javascript:void(0))

Like other features in the Q-SYS Platform, the vCore requires a license for use. An internet connection is required to verify the license every 30 days.

For more information about vCore licensing, see the Core Manager > [Licensing](../Core_Manager/Core_Management/Licensing.htm) topic.

[Supported Hardware and Functions](javascript:void(0))

**Note:** vCore supports control of a maximum of 16 devices. Designs can include up to 32 scripting components, including plugins, Block Controller, Text Controller, and Control Script.

[Supported Devices](javascript:void(0))

|  |  |  |
| --- | --- | --- |
| QIO-GP8x8 | QIO-IR1x4 | QIO-S4 |
| TSC-55-G2 | TSC-80-G2 | TSC-116-G2 |
| TSC-50-G3 | TSC-70-G3 | TSC-101-G3 |
| Axon C1 | Monitoring Proxy | MTR |
| UCI Viewer |  |  |

[Supported Schematic Elements](javascript:void(0))

|  |  |  |
| --- | --- | --- |
| Astronomical Clock | Blinking LED | Color Picker |
| Command Buttons | Contact List | Control Delay |
| Control Function | Control Link | Control Router |
| Custom Controls | Date/Time | E-mailer |
| Envelope Generator | Event Log | Event Logger |
| Flip Flop | GPS Info | IR Driver |
| IR Receiver | LFO | Pinpad |
| Press and Hold | Selector | Status Combiner |
| UCI Layer Controller | UCI Style Controller | Value Stepper |
| Ping | SNMP Query | Block Controller |
| Control Script | Text Controller | Layout |
| Popup Button | Signal Snake Input | Signal Snake Output |
| Clean Screen Button | Log Off Button | Navigation Button |
| URL Button |  |  |

[Unsupported Features](javascript:void(0))

|  |  |  |
| --- | --- | --- |
| Shift AV | Q-LAN RX/TX | USB Audio Bridging |
| USB Video Bridging | USB HID | Mediacast to HDMI |
| Audio DSP (CAT1 or CAT2) | Call Sync | AES67 RX/TX |
| System Link RX/TX | ATMOS Digital Interface | Media Stream RX/TX |
| WAN RX/TX | Softphone / VOIP | Software-Based Dante RX/TX |
| Loudspeakers | Amplifiers | Microphones |
