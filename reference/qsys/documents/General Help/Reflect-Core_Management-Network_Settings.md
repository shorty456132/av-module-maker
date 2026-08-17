# Network > Basic

> Source: https://help.qsys.com/Content/Reflect/Core_Management/Network_Settings.htm

# Network > Basic

View and configure how the Q-SYS Core connects to the network. Click Edit to change these settings.

**CAUTION:** A Gateway (also known as the Default Gateway) is used to route network data to devices outside of the local subnets configured on the Q-SYS Core's LAN adapters. You should only configure the Q-SYS Core with a single Gateway, either through Static or Auto (DHCP) addressing. Configuring a Gateway on more than one LAN adapter causes negative and unpredictable behavior. If you need to communicate with multiple remote networks, use one Gateway and then Static Routes for all other LAN adapters.

## Hostname

* Hostnames may contain ASCII letters 'a' through 'z' (case-insensitive), the digits '0' through '9', and the hyphen. (The hostname cannot begin or end with a hyphen, however.) Core names are limited to 63 characters.
* Hostnames must be unique on the network.
* Click ID to display the hostname on Core's front panel display, which makes it easy to identify the Core in a rack.

## LAN A, LAN B, LAN AUX

Select how each of the Core's LAN adapters connects to your network. Depending on your Core model, only a subset of the LAN adapters may be available â for example, your Core model may not have 'AUX LAN'. For each LAN adapter, its MAC Address and connected Link Speed (for example, "1000 Mbps") are indicated.

[Mode](javascript:void(0))

* Auto: Obtain the network settings automatically from a DHCP server or a link-local address if a DHCP server is unavailable.
* Static: Manually specify the IP Address, Net Mask, and default Gateway. You may need to obtain this information from a network administrator.
* Off: Disable this network adapter.

  **Note:** 'LAN A' cannot be turned off.

[Operate with any PoE Power Sourcing Equipment](javascript:void(0))

Select this option to allow an NV-32-H (Core Capable) to boot and run when connected to a switch port that technically supplies adequate power for PoE++ (802.3bt Type 4) but does not correctly negotiate this capability with the NV-32-H. This is the case for some network switch power sourcing equipment (PSE).

* Unselected (default): If the switch port does not negotiate PoE++ (802.3bt Type 4) capability, the NV-32-H reports a "Missing - Insufficient PoE power" fault.
* Selected: If the switch port does not negotiate PoE++ (802.3bt Type 4) capability, the NV-32-H attempts to boot and run with the connected power. Only select this option if you are certain that the switch port supplies adequate power despite not negotiating this capability.

[Static Routes](javascript:void(0))

Configure static routes for remote networks that need to be reached via the LAN adapter.

Click + Add to specify an IP Address, Net Mask, and Gateway of a new static route for this LAN adapter.

**Note:** When defining static routes for a LAN adapter, do not specify a default Gateway value. Each static route definition uses its own Gateway value.

## DNS

When the LAN Mode is set to 'Auto', the DNS section shows the read-only DNS Servers and Search Domains that the Core has been assigned by the DHCP server. If there are additional DNS servers you wish to use, or if the LAN Mode is set to 'Static', you can optionally add up to 16 DNS Servers and Search Domains. Click Edit to modify the DNS configuration.

A DNS server entry is required if:

* The Core will be monitored remotely with Q-SYS Reflect.
* The Core must resolve DNS hostnames â for example, a SIP proxy address given as a name instead of an IP address.
* The Core must communicate with an LDAP server, in which case you must specify the LDAP server's IP address as a DNS address. This is typically a Microsoft AD DNS server.

**Tip:** DNS servers and search domains are available from the site IT administrator, or you can use public DNS servers such as those provided by Google (8.8.8.8 and 8.8.4.4).

## Proxy

In some corporate environments, a dedicated proxy server must be specified to reach the internet. If required by your site:

1. Select Enabled.
2. specify a Host name and Port (Optional).
3. If the proxy server requires login credentials, select 'Yes' for Authentication and specify a Username and Password.
4. Click Test Connection.

**Tip:** Proxy requirements are available from the site IT administrator.
