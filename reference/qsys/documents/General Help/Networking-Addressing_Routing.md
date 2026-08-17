# Addressing & Routing

> Source: https://help.qsys.com/Content/Networking/Addressing_Routing.htm

# Addressing & Routing

Read this topic to understand the IP addressing and routing requirements for a Q-SYS network.

**Tip:** QSC recommends that you deploy Q-SYS on a dedicated network to reduce risk and improve stability.

[Q-SYS Core Configuration](javascript:void(0))

* Use Q-SYS Core Manager or Q-SYS Reflect to configure the Q-SYS Core's network settings, including hostname, IP address, default gateway, and static routing. See [Network > Basic](../Core_Manager/Core_Management/Network_Settings.htm) in the Core Manager Help for more information.
* Use Q-SYS Core Manager or Q-SYS Reflect to manage the Q-SYS Core's ability to communicate with devices through its network interfaces â for example, to "lock down" Q-SYS devices from the corporate network. See [Network > Services](../Core_Manager/Core_Management/Network_Services.htm) in the Core Manager Help for more information, including use cases.

[General Requirements](javascript:void(0))

### Device Limit

* Do not exceed 510 devices (/23) per IP subnet. For the best performance, limit the IP subnet to 254 devices (/24).
* The limit for static routes is 128.

### IP Address Assignment

Q-LAN supports IPv4 address assignment using either Static (recommended) or Auto (DHCP) methods. If a Q-SYS device is configured for DHCP and cannot receive an address from a DHCP server, the device uses Auto-IP (IPv4LL) to obtain an address from the range 169.254.xx.xx.

**Note:** DHCP is not recommended due to the potential for IP addresses to change, which can cause a disruption in audio and video streaming.

### Routing

**CAUTION:** A Gateway (also known as the Default Gateway) is used to route network data to devices outside of the local subnets configured on the Q-SYS Core's LAN interfaces. You should only configure the Q-SYS Core with a single Gateway, either through Static or Auto (DHCP) addressing. Configuring a Gateway on more than one LAN interface causes negative and unpredictable behavior. If you need to communicate with multiple remote networks, use one Gateway and then Static Routes for all other LAN interfaces.

**Note:** Q-SYS does not support routing between LAN interfaces (also known as inter-NIC-routing).

[Redundant Routed Network Requirements](javascript:void(0))

In very large Q-SYS networks, multiple subnets may be desired, requiring the use of routers for successful communication between different network segments. If the redundant network connections on Q-SYS devices (LAN A and LAN B) are being used in this model, two independent routed networks may exist. Observe these requirements and examples.

### Requirements

* LAN interfaces must not use overlapping IP networks.
* LAN interfaces must be on different VLANs or switches.
* Peripherals cannot be connected on a single network with a mixture of LAN A and LAN B connections to the same switch.
* A Gateway (also known as the Default Gateway) is used to route network data to devices outside of the local subnets configured on the Q-SYS Core's LAN interfaces. You should only configure the Q-SYS Core with a single Gateway, either through Static or Auto (DHCP) addressing. Configuring a Gateway on more than one LAN interface causes negative and unpredictable behavior. If you need to communicate with multiple remote networks, use one Gateway and then Static Routes for all other LAN interfaces.

### Configuration Examples

These examples show proper and improper Q-SYS Core network settings for LAN A and LAN B redundancy. For topology examples showing redundant configurations, see [Network Switches & Infrastructure](Switches_Infrastructure.htm).

[Dual Default Gateways (Improper)](javascript:void(0))

In this example, both LAN A and LAN B are set to Auto (DHCP) mode. Both interfaces are on the same subnet, so both use the same Gateway (also called the Default Gateway). This configuration may result in LAN A or LAN B communication faults.

[Single Default Gateway (Proper)](javascript:void(0))

In this example, LAN A and LAN B are using Static IP address assignment (preferred), with each on a separate subnet and with only a single Default Gateway assigned. This is a proper configuration.

[Static Routing (Preferred)](javascript:void(0))

Configure Static Routes to reach other subnets. This results in much more robust communication between Q-SYS devices. Static Routes represent a mask of addresses to be contacted (outside of the device's subnet) and the gateway to use for contacting them.

IP Address: Inserting a â0â indicates that all hosts within that subnet should follow that Static Route. All hosts on the same subnet of a given interface are always contacted directly. In this example, the Static Route contacts the specified gateway when contacting any address beginning with 192.168 that is outside the 192.168.1.0 subnet.

Net Mask: This sets the mask for the Static Route. Any 0 in the IP Address field needs the corresponding 0 in the Netmask. Else, this entry follows the standards of subnet masking.

Gateway: Sets the gateway for the hosts within this Static Route.
