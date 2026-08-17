# Network Settings

> Source: https://help.qsys.com/Content/Peripheral_Manager/Network_Settings.htm

# Network Settings

View and configure how the Q-SYS peripheral connects to the network. Click Edit to change these settings.

**CAUTION:** A Gateway (also known as the Default Gateway) is used to route network data to devices outside of the local subnets configured on the Q-SYS peripheral's LAN adapters. You should only configure the Q-SYS peripheral with a single Gateway, either through Static or Auto (DHCP) addressing. Configuring a Gateway on more than one LAN adapter causes negative and unpredictable behavior. If you need to communicate with multiple remote networks, use one Gateway and then Static Routes for all other LAN adapters.

## Hostname

* Hostnames support between 5 to 15 ASCII characters in length.
* Hostnames may contain ASCII letters 'a' through 'z' (case-insensitive), the digits '0' through '9', and the hyphen. (The hostname cannot begin or end with a hyphen, however.)
* Hostnames must be unique on the network.
* Click ID to display the hostname on peripheral's front panel display, which makes it easy to identify the peripheral in a rack.

## LAN Adapters â LAN A, LAN B

Select how each of the peripheral's LAN adapters connects to your network. Depending on your peripheral, only a subset of the LAN adapters may be available â for example, your peripheral model may not support LAN B functionality. For each LAN adapter, its MAC Address and connected Link Speed (for example, "1000 Mbps") are indicated.

[Mode](javascript:void(0))

* Auto: Obtain the network settings automatically from a DHCP server or a link-local address if a DHCP server is unavailable.
* Static: Manually specify the IP Address, Net Mask, and default Gateway. You may need to obtain this information from a network administrator.
* Off: Disable this network adapter.

  **Note:** 'LAN A' cannot be turned off.

[Operate with any PoE Power Sourcing Equipment](javascript:void(0))

Select this option to allow an NV-32-H or NV-21-HU to boot and run when connected to a PoE switch port that technically supplies adequate power (90W, Class 8 for NV-32-H or 45W, Class 5 for NV-21-HU) but does not correctly negotiate this capability with the device. This is the case for some network switch power sourcing equipment (PSE).

* Unselected (default): If the switch port does not correctly negotiate power capability, the NV-32-H or NV-21-HU reports a "Missing - Insufficient PoE power" fault.
* Selected: If the switch port does not correctly negotiate power capability, the NV-32-H or NV-21-HU attempts to boot and run with the connected power. Only select this option if you are certain that the switch port supplies adequate power despite not negotiating this capability.

[Static Routes](javascript:void(0))

Configure static routes for remote networks that need to be reached via the LAN adapter.

Click + Add to specify an IP Address, Net Mask, and Gateway of a new static route for this LAN adapter.

**Note:** When defining static routes for a LAN adapter, do not specify a default Gateway value. Each static route definition uses its own Gateway value.
