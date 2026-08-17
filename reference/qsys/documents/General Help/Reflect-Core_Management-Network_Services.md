# Network > Services

> Source: https://help.qsys.com/Content/Reflect/Core_Management/Network_Services.htm

# Network > Services

Manage the Q-SYS Core processor's ability to communicate with devices through its network interfaces. System administrators can:

* Disable unused network services on a per-network adapter level (LAN A, LAN B, AUX LAN, etc.). Disabling unused network services can increase the security of the Q-SYS system and help to satisfy customer-specific security requirements.
* Easily see a summary of all currently-enabled network services and protocols, per network adapter, on the Core.

**CAUTION:** By default, all network services are enabled on the Core. QSC recommends disabling unneeded network services.

## Audit

The Audit tab provides a read-only listing of all active network protocols on the Core and the network adapters on which they are enabled.

For any active network protocol, click + to see a list of the network services using that particular protocol.

## Management

The Management tab provides a list of high-level network services on the Core. A check mark indicates if a network service is active for a particular LAN adapter.

* Click Edit to enable or disable (select or deselect) a network service for a LAN adapter, and then click Save.

  **Note:** Some network services can only be toggled on or off for all LAN adapters at once.
* Click + to expand a high-level network service to see a list of protocols used by that service.
* In the Filter by Protocol section, you can easily see a summary of protocol usage on the Core. The number next to the protocol name indicates how many network services are using that protocol across all LAN adapters. For example:

  **Tip:** Click a protocol name to filter the High-Level Network Services list to show only those services that use the selected protocol. To turn the filter off, click the protocol name again.

## Use Cases and Recommendations

[Solving PTP Syncing Issues](javascript:void(0))

In situations where multiple Cores are connected to the corporate network for control and monitoring only, Q-SYS Audio Enabled Peripherals should be disabled on LAN B. This will stop the Core from behaving as a PTP boundary clock and will solve problems related to Cores attempting to PTP sync over a potentially non-real-time-capable network infrastructure.

#### Running older designs with the 'PTPv2 Disable LAN B' design property enabled

The Q-SYS Audio Enabled Peripherals network service includes the PTPv2 protocol. In Q-SYS Designer versions prior to 7.1, this protocol could be disabled for LAN B in the Design Properties. If you attempt to save a design to the Core with this property enabled, you will be prompted to disable Q-SYS Audio Enabled Peripherals for LAN B in the Network Services manager if this network service is currently enabled on LAN B.

**Note:** Alternatively, you can choose to clear the PTPv2 Disable design property and run your design without configuring Network Services. Doing so is not recommended unless you explicitly require the design to allow PTPv2 traffic on both LAN A and LAN B â for example, for redundant networking, or third party devices configured for LAN A and LAN B connections.

[Securing Q-SYS Devices from the Corporate Network](javascript:void(0))

If LAN B (or AUX) is connected to the corporate network, you may want to disable Q-SYS Device Discovery, Q-SYS Audio Enabled Peripherals, and Q-SYS Control Peripherals for LAN B / AUX to "lock down" Q-SYS devices from the corporate network. However, to still allow UCI viewers (Windows and iOS) to communicate with the Core from the corporate network, you could enable Q-SYS UCI Viewers for LAN B / AUX exclusively.

**Note:** If device discovery is disabled, Hard Links must be used to locate the Core on the network.

[Disabling Unneeded Peripheral Audio](javascript:void(0))

If you have a Core and touchscreen and are only using the built-in audio on the Core, you could disable Q-SYS Audio Enabled Peripherals for all network adapters but keep Q-SYS Control Peripherals enabled.

[Restricting Third-Party Control](javascript:void(0))

If your system does not require control from a third-party control system, consider disabling the Q-SYS External Control Protocol (ASCII and JSONRPC) on all network interface ports.

[Configuring for Network Redundancy](javascript:void(0))

If your design does not use Network Redundancy, you could disable LAN B / AUX for all network services.

[Configuring for Core Redundancy](javascript:void(0))

If your design uses Core Redundancy:

* Ensure that the Q-SYS Core Redundancy network service is enabled on both the Primary Core and Backup Core. This service is required if Core Redundancy is configured in the Q-SYS design file.
* Ensure that all network services for both the Primary Core and Backup Core are configured the same.

If your design does not use Core Redundancy, you could disable the Q-SYS Core Redundancy network service for all LAN interfaces.

## Notes

* Some protocols are used by multiple network services â for example, Q-SYS Discovery Protocol (QDP). A protocol remains active on the Core until all network services using it are disabled for a particular LAN adapter.
* The Q-SYS Designer Communications - Secure network service uses self-signed, encrypted HTTPS communications between the Core and Q-SYS Designer, so is active on all network ports at all times.
* To avoid issues, ensure that design-specific settings (such as Core Redundancy) are compatible with the Core's Network Services configuration.
