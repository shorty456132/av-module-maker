# Network Settings

> Source: https://help.qsys.com/Content/RoomSuite/Network_Settings.htm

# Network Settings

The Network section in the RoomSuite Modular System is your central hub for configuring how the room processor communicates within your organizationâs IT environment. These settings allow you to establish a reliable and secure connection to the corporate network when needed, ensuring that the system integrates seamlessly with existing infrastructure and complies with enterprise security standards.

Using Network Settings, you can:

* Connect the room system to the corporate network by configuring IP addressing, gateways, and DNS resolution.
* Set system time accurately, which is essential for log correlation, certificate validation, and scheduled operations.
* Manage security certificates to enable trusted HTTPS communication and meet organizational security requirements.
* Enable secure communication protocols, such as HTTPS, and configure advanced options like 802.1X for port-based network authentication.

These capabilities are designed primarily for IT, UC, and network administrators who are responsible for deploying and maintaining room systems in enterprise environments. By leveraging these tools, you can ensure that the system operates securely, remains reachable for management tasks, and integrates smoothly with services such as VoIP, UC platforms, and monitoring tools.

Each menu item focuses on a specific aspect of network configuration:

Basic

Displays the current network configuration, including IP addresses, DNS servers, and optional proxy settings. This is the primary page for verifying connectivity and performing initial setup.

Date & Time

Lets you configure the systemâs time zone and NTP servers to ensure accurate time synchronization for logs, certificates, and scheduled operations.

**Note:** Enabling NTP time synchronization is recommended to maintain consistent system time across devices.

Certificates

Provides tools to manage device certificates, upload trusted certificates, and generate Certificate Signing Requests (CSRs) for your corporate Certificate Authority.

Secure Communication

Allows you to enable HTTPS access to the RoomSuite web interface and enforce encryption for management traffic, aligning with corporate security policies.

**802.1X**

Enables port-based network authentication for environments that require secure access control. Here, you can configure authentication methods and upload necessary credentials and certificates.

## Basic

#### Message Banner

Message Banner displays important cautions or alerts that administrators should review before making changes. These messages help prevent misconfiguration that could disrupt network connectivity or security.

#### Edit Button

Located on the far-right side of the panel, when clicked, the page switches to an editable mode where you can update values and enable ID Toggle. After making changes, you can save or cancel returning to the standard view.

#### Hostname Panel

#### Hostname

This is the processorâs network name used for DNS resolution and identification in logs.

#### ID Toggle

When enabled, the processor provides a physical or audible indicator (e.g., LED flash), making it easy to locate in a rack or room during large deployments.

#### AUX A Panel

AUX A is typically the primary corporate network interface, as well as the primary interface to connect to the RMP-100 software and to Reflect.

#### MAC Address

Unique hardware ID for DHCP reservations or whitelisting.

#### LLDP Information

Identifies the connected switch and portâhelpful for remote troubleshooting.

#### Link Speed

Confirms negotiated speed; lower speeds may indicate cabling or switch issues.

#### Mode

Indicates whether the IP configuration is automatic (DHCP), Off, or Static.

#### IP Address

AUX A usually holds the only default gateway.

#### Netmask

Subnet mask for the IP address. Used to determine which addresses are considered local.

#### Gateway

The default gateway used for traffic leaving the local subnet. AUX A is typically where you configure the only default gateway.

#### Static Routes

Viewable when you click the Edit button. Static Routes under AUX A allow you to define specific network paths for traffic originating from the primary interface without adding additional default gateways. This is useful when the processor needs to reach subnets outside its main network while maintaining predictable routing.

Fields:

IP Address â Destination subnet or host you want to reach.

Netmask â Defines the size of the destination network.

Gateway â The next-hop router for that subnet.

AUX A typically holds the only default gateway. Adding static routes here ensures the processor can access additional networks (e.g., VoIP servers, UC platforms) without introducing routing conflicts.

#### AUX B Panel

AUX B is an optional secondary interface and is disabled by default.

#### Status

Indicates no cable or inactive switch port.

#### MAC Address

Unique hardware ID for DHCP reservations or whitelisting.

#### Mode / IP Address / Netmask / Gateway

These fields show how the selected AUX network interface is currently configured. Mode indicates whether the interface is using DHCP, a static assignment, or is turned off. IP Address, Netmask, and Gateway display the resulting network settings assigned to that interface. When all values show Not Assigned, it means the interface is disabled, not linked, or not configured for use.

**Note:** If your design requires a second network, connect and configure AUXâ¯B according to your IT policies. Do not add a second default gatewayâuse static routes if needed.

#### DNS Panel

Controls how the processor resolves hostnames.

#### DNS Servers

Specifies the IP addresses of DNS servers the system will query. If these are unreachable or incorrect, you may see issues contacting name-based services, such as Reflect or NTP hosts, for example, even if IP connectivity exists.

#### Search Domains

System automatically defines domain suffixes appended to short hostnames. For example, if you enter rm-core01, the system might try rm-core01.qscaudio.com and rm-core01.qsclocal. This helps shorten the URLs and hostnames you need to enter.

#### Proxy Panel

Defines HTTP / HTTPS proxy settings for outbound traffic.

#### Proxy Support

When enabled, you can specify server address, port, and authentication. If your organization requires proxy routing for internet access, configure it here.

## Date & Time

#### Edit Button

Located at the top-right of the page, the Edit button switches the page into an editable mode. In this mode, you can:

* Change the time zone.
* Add or remove NTP servers.
* Enable or disable NTP synchronization.
* Optionally set the date and time manually if NTP is not used.

After making changes, you can Save or Cancel returning to the standard view.

#### Time Settings Panel

Displays the processorâs current date, time, and configured time zone. These values reflect the systemâs active time configuration and help ensure accurate logging, certificate validation, and scheduled operations.

#### Date

Shows the processorâs current calendar date based on the selected time zone.

#### Time

Shows the processorâs current time, including its offset from Coordinated Universal Time (UTC).

#### Time Zone

Indicates the geographic time zone the processor is using to determine local date and time.

## NTP Time Synchronization Panel

The NTP Time Synchronization panel controls whether the processor automatically synchronizes its internal clock with trusted time sources using the Network Time Protocol (NTP). This ensures the system maintains accurate time without manual intervention.

When Enabled

* The processor regularly contacts the configured NTP servers to update its clock.
* Time remains accurate even after reboots or long periods of operation.
* Functions such as certificate validation, 802.1X authentication, and scheduled tasks work reliably because they depend on precise time.
* Event logs across multiple systems align correctly, simplifying troubleshooting.

When Disabled

* The processor does not sync with external time sources.
* Time must be set manually, and it can drift over time.
* Misconfigured or inaccurate time can cause certificate errors (HTTPS or 802.1X failures), scheduling issues for automated tasks, or difficulty correlating logs across systems.

#### NTP Servers

NTP servers are trusted network hosts that provide accurate time information. The processor queries these servers at regular intervals to maintain synchronization.

* These servers can be public, like pool.ntp.org or internal corporate servers for added security and compliance.
* If NTP servers are unreachable or misconfigured, the processor cannot update its clock, which may lead to authentication failures and scheduling problems.

## NTP Authentication Panel

The NTP Authentication panel provides an added layer of security for time synchronization. It allows administrators to configure authentication keys that verify the identity of NTP servers before accepting time updates. This prevents unauthorized or malicious time sources from influencing the processorâs clock, which could otherwise lead to certificate failures, authentication issues, or scheduling errors.

#### Add NTP Authentication Key

When you click Add Key, a pop-up window appears with the following fields:

* Key ID

  A numeric identifier, 0â5 that uniquely identifies the authentication key. The processor uses this ID to match the key with NTP server configurations.
* Encryption Type

  Specifies the algorithm used to secure the key, such as MD5 or SHA1. This ensures the integrity and authenticity of NTP messages.
* Actual Key Value

The secret key string used for authentication. This value must match the key configured on the NTP server. It is typically entered as a secure string and may be masked for privacy.

After entering these details, click Add to save the key. The processor will then use this key to authenticate NTP packets from servers that support secure NTP.

## Secure Communication

Q-SYS communication between Cores and Peripherals can be secured by encryption and mutual authentication using X.509 certificates. Secure mode of communication applies to two types of connections:

â¢ Control connections â Design controls and other control traffic between cores and peripherals.

â¢ Device-to-device web connections â Operations such as design deploy, firmware update, device status, and other web/API based interactions.

[Mutual Authentication and Trust Management Between Cores and Peripherals](javascript:void(0))

[Mutual Authentication](javascript:void(0))

In secure mode, two devices can communicate securely only if they can mutually authenticate each other:

â¢ Each device must find the peerâs certificate in its trusted list.

â¢ The peer must prove ownership of the private key associated with the certificate it presents.

This mutual authentication is what ensures that both ends of the connection are who they claim to be.

[Automatic and Manual Certificate Management](javascript:void(0))

Q-SYS manages device trust using three lists: Trusted, Pending, and Declined certificates.

**Trusted**

In typical configurations, certificates can be added to the trusted list automatically. By default:

â¢ The Coreâs trusted list includes all peripheral certificates.

â¢ Each Peripheral automatically trusts the Coreâs certificate (or both certificates in a redundant core pair).

This allows cores and peripherals to establish secure communication seamlessly without user intervention.

**Pending**

If automatic trust is not possibleâfor example, because of a configuration or policy restrictionâthe peerâs certificate is placed on the Pending list for manual approval. Once a Peripheralâs trusted list includes at least one certificate, it switches to secure mode and restricts communication to only the associated core (or core pair).

**Declined Certificates**

Certificates that are on, or that chain to one on, the Declined list are denied communication entirely. They are not allowed onto the Pending list and cannot be used to establish secure communication.

In a redundant Core pairs:

â¢ The two Cores must first establish mutual trust with each other.

â¢ After that trust is in place, both Core certificates are shared with Peripherals.

â¢ Peripherals then add both certificates to their trusted lists, allowing them to maintain secure communication if a failover occurs from the primary Core to the backup.

[Prerequisites](javascript:void(0))

1. Update the firmware on all Q-SYS devices to version 10.0 (or higher) to support secure communication.

2. Install the required certificates on the Core and Peripherals. If no new certificates are installed, the currently installed ones will be used. Refer to [Network > Certificates](../Core_Manager/Core_Management/Certificates.htm) for instructions on installing certificates.

3. Set up Access Control of all Cores and all Peripherals. For more details, see [Access Management > Users](../Core_Manager/Core_Management/Users.htm)in Core Manager and [Device Password](../Peripheral_Manager/Device_Password.htm) in Peripheral Manager.

**Note:** Since primary and backup (redundant) Cores automatically sync, ensure Access Control is enabled on the backup Core.

[Configure Trust Options](javascript:void(0))

**Trust On First Usage (TOFU)**

â¢ Peripheral

A Peripheral with TOFU enabled will automatically add a Core's certificate to its trusted list if the list is empty. Once secured, the Peripheral requires manual approval for any new Core certificates via Peripheral Manager.

â¢ Core

The Core adds each Peripheral's certificate to its trusted list automatically. If a Peripheral device is swapped but retains the same name, manual approval for the new certificate is needed through Core Manager.

**Rollover**

Disabled in the Core by default. This option, enabled by default on Peripherals but not on the Core, facilitates automatic replacement of certificates, avoiding need for manual approvals when a certificate is updated.

[Further Secure Your Q-SYS System](javascript:void(0))

1. Disable Non-Authentication-Supporting Networking Services.

Navigate to Network > Services > Managementt and disable the following services:

â¢ Q-SYS External Control Protocol - ASCII

â¢ Q-SYS Remote Control Protocol - JSONRPC

**Note:** Consider certificate expiration by checking the 'Verify Validity Period' to block expired certificates from authenticating.

[Enable Secure Communication](javascript:void(0))

1. Click the Enable Secure Communication button on the Core to initiate secure mode.

[Disable Secure Communication](javascript:void(0))

1. To disable secure communication, click Disable Secure Communication on the Core. The core attempts to withdraw its certificate from the peripherals. By clearing a peripheralâs trusted list, the device reverts to non-secure mode of communication.

2. If some peripherals do not switch to non-secure mode automatically, manually clear their trusted lists. In scenarios where a peripheral trusts devices beyond the current core (or redundant core pair), the current core does not revoke those certificates. You may need to remove trust for that peripheral from other cores as well to maintain consistent security across different Q-SYS setups.

**Note:** If you plan to downgrade the Q-SYS system to firmware that does not support secure communication, ensure that secure mode is disabled on the core and that all peripheral trusted lists are cleared. A core running firmware that does not support secure communication will fail to connect to peripherals still operating in secure mode.

[Verify Secure Connections](javascript:void(0))

1. Ensure secure connections are established between Cores and Peripherals.

â¢ If automatic trust does not apply, review pending certificates and verify their authenticity by comparing fingerprints. See [Network > Certificates](../Core_Manager/Core_Management/Certificates.htm) for more information.

â¢ To ensure Cores and Peripherals engage in a trusted relationship, visit the Troubleshooting section below.

[Advanced Secure Communication Behaviors and Best Practices](javascript:void(0))

**Behavior in Special Scenarios**

â¢ Once secure mode is activated, you cannot remove the device password without first disabling secure mode.

â¢ Automatic rollover may fail if a device installs a new certificate while its peer is offline. When rollover fails, manual approval of the certificate is required.

â¢ For inter-design communications, manual certificate exchanges are necessary to gain trust.

â¢ In a setup with two Cores where Secure Communication is enabled on only one, if a Peripheral is added to both designs, the core with Secure Communication will establish a connection, while the other core will show Authentication failure.

â¢ Security configuration options are synced between active and backup Cores: you can change the security configuration only on the active core. Trusted lists of certificates are also synced between active and backup cores; only the certificates of the currently running design are exchanged between the cores. At all times, the active Core ensures that trusted Peripherals also trust the backup Core.

**Security Best Practices**

â¢ Disabling both TOFU and Rollover is advised if there is any perceived security threat during deployment.

[Secure Communication Page](javascript:void(0))

The Secure Communication page in the side navigation lets you configure these behaviors and manage certificate trust:

â¢ The Security Options section controls how trust is established and maintained.

â¢ The Trusted Certificates, Pending Certificates, and Declined Certificates tabs show the current trust state for connected devices and let you upload, approve, or decline certificates.

The following sections describe each security option and certificate list in more detail.

Enable Secure Communication Button

Allows administrators to enforce HTTPS and related secure protocols for management traffic.

Security Options

Defines how trust and certificate validation are handled.

â¢ Trust On First Use

Automatically establishes trust with a remote device the first time it connects.

â¢ Rollover

Enables automatic replacement of an existing trusted certificate with the new one.

â¢ Verify Validity Period

Stop trusting devices with expired certificates.

â¢ Control Server Authentication

Requires the client to provide a certificate and verify it against the trusted list.

Certificate Management

Below the security options, there are three tabs for managing certificates:

â¢ Trusted Certificates

Displays certificates that have been accepted and are currently trusted.

â¢ Pending Certificates

Shows certificates awaiting approval.

â¢ Declined Certificates

Lists certificates that were explicitly rejected to communicate with this device.

Upload Certificate Button

Allows you to manually add a certificate to the trusted list. This is useful for preloading certificates before deployment.

Decline Button

Allows you to reject a pending certificate request.

[Troubleshooting Authentication Failures](javascript:void(0))

When devices do not trust each other, a control connection cannot be established. In this case, the device status shows Fault â Authentication Failure. You can examine the Coreâs log for error messages that describe the cause of the authentication failure for each device.

Common causes and resolutions:

**Device password not set**

Secure mode is not available for devices without a user password.

â¢ Ensure Access Control is enabled on both Cores in a redundant pair.

â¢ Verify that all peripherals have a user password set.

**Certificate pending manual approval**

The offered certificate may be on the Pending list in the core or peripheral.

â¢ In Core Manager and Peripheral Manager, review the list of pending certificates.

â¢ Approve the certificate only after confirming that its fingerprint is correct.

**Certificate declined**

The offered certificate may be on the Declined list.

â¢ In Core Manager and Peripheral Manager, review declined certificates.

â¢ Remove any declined certificate that was added by mistake so it can move to Pending or Trusted.

**Certificate expired**

The offered certificate may have expired.

â¢ Regenerate and install a new certificate on the device whose certificate has expired.

**Redundant cores not trusted by each other**

In a redundant system, the two Cores must first trust each other before Peripherals can fully establish trust.

â¢ Verify that primary and backup Core certificates are on each otherâs trusted lists.

â¢ Once mutual trust is established between the Cores, trust establishment with peripherals is unblocked.

## 802.1X

#### 2 Ports (AUX A and AUX B)

Indicates whether the physical network link is active.

Link Up: Cable connected and switch port active.

Link Down: Cable not connected and switch port inactive.

#### 802.1X Status (Enabled / Disabled)

Shows whether 802.1X authentication is currently active on the interface.

Enabled: The processor will attempt to authenticate using configured credentials and certificates.

Disabled: The processor will not perform 802.1X authentication.

#### Edit Button

Allows you to change the 802.1X settings for the selected port.
