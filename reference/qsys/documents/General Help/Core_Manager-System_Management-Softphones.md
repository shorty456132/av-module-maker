# Telephony > Softphones

> Source: https://help.qsys.com/Content/Core_Manager/System_Management/Softphones.htm

# Telephony > Softphones

Configure Softphone global parameters and individual Softphone parameters. Click Edit to change the Softphone settings.

**Note:** Softphone configuration is only available if the design running on the Q-SYS Core contains one or more Softphones.

## Prerequisites

Use the Q-SYS Softphone to connect to VoIP (Voice over IP) telephone systems, including IP-PBX and SIP-based devices (for example, Cisco CUCM and FreeSwitch). The Softphones page facilitates registration with these systems. Before configuring the Softphone:

* Add at least one Softphone component in to the design.
* Have the SIP or IP/PBX information ready to enter.
* Know which audio codecs you are going to use.
* Know which Q-SYS Core LAN interface you want to use for the Softphone connection.

**Tip:** You can also use the Softphone component in unregistered mode, which allows making ad-hoc IP-to-IP calls (for example, Core-to-Core) and connecting to other non-registered SIP-compatible equipment.

[VoIP Provider Compatibility](javascript:void(0))

These VoIP providers and versions are known to work with Q-SYS Softphone:

| Provider | Model | Software Versions |
| --- | --- | --- |
| Avaya | IP Office | 9.0 |
| Avaya | Session Manager | 7.0, 8.1 |
| Cisco | CUCM | 10.5, 11.0, 11.5, 12.0, 12.5 |
| ShoreTel / Mitel | Connect | - |
| RingCentral | Cloud-based | - |
| Jive | Cloud-based | - |
| Vonage | Cloud-based | - |
| Nextiva | Cloud-based | - |

[SIP Port Restrictions](javascript:void(0))

5060 is the official port number for SIP signaling. If you choose to assign a different port number, it can generally be within the range 1 to 65535, but you must avoid the following port numbers to prevent communication conflicts:

* Ports 16384-32768, which are used by Q-SYS Softphone for RTP/RTCP communication.
* Any port number used by the Q-SYS Core. For a listing of these port numbers, click Summary View within the Network Services page. For more information, see [Network > Services](../Core_Management/Network_Services.htm).

If you are unsure about what port number to use for SIP signaling, contact your IT administrator.

[SIP Trunk Support](javascript:void(0))

You can configure a Q-SYS Softphone as a SIP trunk on a PBX. Because the trunk will not consume any third party SIP licenses on most PBXs, you are limited only by the maximum number of Softphones allowed for your Core model: Core 110f = 4; all other Cores = 64.

To configure Q-SYS Softphone as a SIP trunk, observe the following guidelines:

1. A SIP trunk will typically have a group or range of extensions assigned to it. From this group, configure a Softphone component for an extension.
2. Configure the individual Softphone parameters to support trunking:
   * Username and CID Name: Typically the extension number assigned to the SIP trunk on the PBX.
   * Proxy: The IP address of the PBX where the trunk is hosted.
   * Transport: Select 'UDP' or 'TCP'.
   * Authenticate With Proxy: Do not select.
3. In your PBX administrator, configure the trunk to receive the OPTIONS ping. The Softphone will periodically send an OPTIONS ping to the trunk IP address to check for SIP connectivity.

## Shared Settings

These settings apply to all Softphones.

#### Core Interface

Select the LAN interface to use for all SIP traffic, which must have a route to the SIP device to which you want to connect.

#### SIP Port

This is the listening (source) UDP port of Q-SYS Softphones. The default is 5060. See [SIP Port Restrictions](#SIP). (Outbound calls always use port 5060.)

#### Logging

Select to enable SIP logging. This log can be used by Q-SYS Support to troubleshoot problems you may be experiencing.

#### SRTP

Select to enable the SRTP (Secure RTP) protocol, which encrypts the RTP voice / media payload. Some phone systems may require SRTP â for example, Avaya IP Office.

#### DTMF INFO

Select to enable DTMF to be sent as SIP INFO requests. When enabled, DTMF is not sent via RFC 2833.

#### RFC2833 DTMF Type

This number is the 'RTP Event' Payload Type Number that indicates that the transmitted packet contains DTMF digits. The default is 101, but you can enter any number from 96 to 127. On the remote SIP device, RX and TX DTMF Payload Types must match this value.

**Note:** Some SIP devices can specify separate RX and TX DTMF Payload Types and some, such as Q-SYS, cannot. On systems that cannot have separate values, RX and TX DTMF Payload Types must both match this value.

#### STUN

Select to enable the STUN (Session Traversal Utilities for NAT) feature, which allows you to communicate with a cloud-based PBX. STUN is a protocol that finds the public IP of a service (Q-SYS) that is behind a firewall or network address translator. A STUN packet is sent to a publicly accessible STUN server, which responds with the public-to-private IP address. Once Q-SYS receives the public address, it uses that address to communicate with a cloud-based PBX.

**Note:** If you enable STUN, all Softphones in your Q-SYS design use STUN.

#### STUN Server (Optional)

If STUN is enabled, Q-SYS uses STUN server stun.freeswitch.org by default, but you can specify a different server here. A listing of free STUN servers is available via the internet.

#### Hold

Some phone systems do not properly re-enable call audio after taking a call off hold. This can be due to changes in the RTP port used during the connection. Deselect this option to allow compatibility with these phone systems. This option is enabled by default.

#### Insecure Ciphers

You might need to enable this option for compatibility with VoIP services that still use deprecated (and insecure) ciphers. This option is disabled by default for new designs in Q-SYS 9.1.0 and later. To maintain compatibility with existing systems, it is enabled by default when upgrading from Q-SYS 9.0.1 and earlier.

**Note:** If Access Control is enabled on the Core, changing this setting requires Technician-level access or higher.

#### Domain Based Calling

Select whether to enforce using a domain name for SIP authentication â as specified in the Domain field for each Softphone â instead of the Proxy IP address. For many cloud-based PBX services, this is useful for white-listing a single domain name instead of multiple proxy IP addresses. This option is disabled by default.

**Note:** Domain Based Calling is required by NuWave, Momentum Telecom, Zoom, and Broadworks.

## Audio Codecs

Select all supported audio codec types to be available for use and order them by preference of connection. Click and drag a codec to change the connection order.

## Softphones List

This list contains all Softphone components from your design inventory. Select a Softphone to change its settings.

#### Username

This is the number or name you use to call the Softphone. For Softphones registered to a SIP or IP-PBX, the provider supplies this name (typically an extension number), along with a Password. For unregistered Softphones, the Username can be anything â for example, the local portion of an email address (before the @ sign).

#### CID Name

(Optional) This is the name to use for caller ID.

#### Transport

Select the transport protocol - UDP, TCP, or TLS.

**Note:** Q-SYS supports TLS version 1.2. TLS (Transport Layer Security) is a protocol that runs over TCP and provides end-to-end security for SIP signaling by encrypting SIP messages that are exchanged between Q-SYS SIP Softphones and far end SIP endpoints or PBXs.

#### Proxy

The destination IP address (or hostname) and port number of the SIP provider, IP-PBX, or SIP gateway. For example, 192.168.1.205:15060.

#### Backup Proxy

(Optional) The IP address or resolvable name of the SIP provider, IP-PBX, or SIP gateway to use if a connection to the primary proxy cannot be established.

#### Register with Proxy

Select 'Yes' to register the Softphone with a proxy. Enter an Authentication ID and Password, both supplied by the SIP or IP-PBX provider.

#### Domain

Enter the Domain name of the PBX's network, if required. This field is required when the Domain Based Calling option is enabled in Shared Settings.

#### Registration Timeout

(Optional) Set the expiration interval, in seconds, for this registration at the VoIP PBX. The default is 3600 seconds (1 hour) if you leave this field blank or enter an invalid parameter. This is typically used on some cloud-based PBXs that use a smaller interval to keep firewalls open.
