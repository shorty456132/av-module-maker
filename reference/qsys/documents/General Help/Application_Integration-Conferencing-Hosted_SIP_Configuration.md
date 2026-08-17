# Hosted SIP Configuration

> Source: https://help.qsys.com/Content/Application_Integration/Conferencing/Hosted_SIP_Configuration.htm

# Hosted SIP Configuration

Use this topic as a general guide for configuring Q-SYS Softphone to work to with a hosted SIP solution.

**Tip:** To learn about how Q-SYS Softphone works and the basics of SIP, refer to the [Q-SYS Softphone and SIP Overview](Softphone_SIP_Overview.htm) topic. For additional details about configuring softphones in Q-SYS Core Manager, see the [Telephony > Softphones](../../Core_Manager/System_Management/Softphones.htm) topic in Core Manager Help.

[Gather SIP Provider Parameters](javascript:void(0))

To configure the Q-SYS Core processor to work with your hosted SIP provider, you need to gather some key pieces of information. This includes:

* Username
* Password
* Proxy IP address
* SIP signaling port
* DTMF type
* Domain (required or optional, depending on the provider)
* Communication transport protocol - UDP, TCP, or TLS
* Optional features such as SRTP

**Note:** Typically, this information is available from the admin portal for your hosted SIP provider. If not, contact your provider for the configuration parameters. Not all providers support the same features or use the same naming convention.

[Configure Softphone â Shared Settings](javascript:void(0))

In [Core Manager](../../Core_Manager/CoreManager_Overview.htm), open the Telephony > Softphones page and click Edit.

First, configure the parameters in the Shared Settings section. These settings are used for all softphones in the design running on the Q-SYS Core processor. The configuration of most of these settings depends on the requirements of your hosted SIP provider.

* Core Interface â Set this to the LAN interface that the Core will use to reach the internet. This is necessary to reach the proxy server for SIP registration and for placing calls.
* SIP Port â This is the *incoming* network port that the hosted provider will use to talk to the Core. This should always be 5060 unless the provider requires otherwise. The *outgoing* port can be added to the end of the Proxy address, if needed. See the [Troubleshooting](#Troubles) section for more information.
* Logging â Unless you are working with QSC support, leave this disabled.
* SRTP â Optional. RTP is the audio stream of the call. Enabling SRTP will encrypt the audio.
* DTMF INFO â Leave this disabled unless your provider requests it. Leaving it disabled forces the Core to use RFC2833 to transmit DTMF.
* RFC 2833 DTMF Type â This is normally 101, unless your provider requires otherwise.
* STUN â Optional. If you are behind a firewall and the softphone is not working, try enabling this feature. Refer to the [Q-SYS Softphone and SIP Overview](Softphone_SIP_Overview.htm) topic to learn how STUN works.

Example Softphone > Shared Settings

[Configure Softphone â Individual Settings](javascript:void(0))

Next, configure the settings for each softphone in your design. From the Softphones List, select a softphone.

**Note:** Each hosted provider uses different terminology and settings.

* Username â This may be the same as the Authentication ID or it may be the phone number (usually 10 digits).
* CID Name â Optional. This is usually the 10 digit phone number. This is the Caller ID that shows when a call is placed.
* Transport â This can be TCP, UDP, or TLS. If you are unsure, try UDP first.
* Proxy â This is the IP address or domain name where the softphone will register. This should be given to you by your hosting provider.
* Backup Proxy â Optional. If this is needed, your hosting provider should give it to you.
* Register with Proxy â In almost all cases, this should be set to 'Yes'. Hosted SIP providers require the softphone to register in order to function properly.
* Authentication ID â Many providers call this a Username or Authorization ID.
* Password â This is provided by your hosting service.
* Domain â Optional. To register properly, some providers require a domain name to be configured.
* Registration Timeout â Optional. This is usually not necessary with hosted service providers, but in some cases, might need to be configured.

Example Softphone > Individual Settings

[Troubleshooting](javascript:void(0))

### SIP Ports

In some cases, a service provider will not use the default SIP port of 5060 for their proxy. If a different port is required, you can add it to the end of the proxy as shown below.

<*ip address*>:<*port number*>

Example:

10.1.1.1:5090

### Configuring Multiple Softphones

If you are configuring multiple softphones with a service provider, most of the time, the Authentication ID, Password, and Username will be different for each line.
