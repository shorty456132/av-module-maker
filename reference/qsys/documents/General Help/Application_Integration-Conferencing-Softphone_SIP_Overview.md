# Q-SYS Softphone and SIP Overview

> Source: https://help.qsys.com/Content/Application_Integration/Conferencing/Softphone_SIP_Overview.htm

# Q-SYS Softphone and SIP Overview

The Q-SYS Softphone is a great way to integrate a Q-SYS Core processor to a voice over IP (VoIP) telephone system for conferencing and telephone paging.

The terminology around VoIP can seem quite mysterious, so it can often be hard to know if the Q-SYS Softphone is compatible with an end userâs VoIP system. This topic attempts to clarify and simplify these concepts.

[What is the Q-SYS Softphone?](javascript:void(0))

The Q-SYS Softphone is just what the name implies â¦ a phone that is implemented in software. It connects to a VoIP network and can optionally register with a server that is responsible for that systemâs call negotiation. Once registered (if required), the softphone can make and receive calls just like any other VoIP phone.

In most VoIP systems, the server and phones come as a package. The âlanguageâ spoken by the phone system â i.e., the protocol â can vary widely from one system to another. The Q-SYS Softphone, however, does not make use of these many proprietary languages. It uses the Session Initiation Protocol (SIP), a VoIP interoperability standard for controlling and establishing calls. Once the call is established, it uses the Real Time Protocol (RTP) to transmit and receive voice data. Even most proprietary VoIP systems understand SIP or can with a system upgrade.

### Device Types

Basic SIP telephony has two major device types:

#### User Agent Client (UAC)

This device generates requests and directs them to servers.

#### User Agent Server (UAS)

This device receives and processes requests and sends responses to other devices on the network. A UAS device can serve in these roles:

* Proxy server â A proxy server receives SIP commands and forwards them to the appropriate devices on the network. Thus, it is responsible for handling calls on the network.
* Registrar â A UAC may not always stay in the same location, so the registrar detects their locations on the network. Those locations are stored to a third server role, the location server.
* Location Server â The location server keeps a record of all UAC locations, as detected by the registrar.
* Redirect Server â If the intended recipient of a SIP message has moved or is otherwise unreachable, the redirect server will tell the originating UAC that it must try another route.

**Note:** These server roles do not have to be carried out all by different physical devices. In fact, the same device can host all of these functions and serve as a UAC as well.

### User Agents

Most VoIP phones and softphones must act as both UAS and UAC so they can provide all the functionality required of them. A device that combines these duties is referred to as a user agent (UA) or VoIP endpoint.

The Q-SYS Softphone is a simple SIP endpoint or UA device. It is used to make and receive calls through interaction with the various UAS roles.

Simple VoIP network with only user agents and proxy

### SIP Trunks

To make calls outside a local VoIP network, it is often necessary to route them to the Internet or to other local VoIP networks. SIP trunks are often created to accomplish this. One can think of SIP

trunks as virtual wires bridging the expanse between two domains. SIP is used to control the sessions between them.

**Tip:** You can configure a Q-SYS Softphone as a SIP trunk on a PBX. To learn how, see the [Telephony > Softphones](../../Core_Manager/System_Management/Softphones.htm) topic in Core Manager Help.

[Basics of SIP Communication](javascript:void(0))

The primary functions of SIP are the setup, teardown, and modification of calls. SIP is based on the HTTP model and makes use of simple requests and replies. It can use UDP, TCP, or TLS for transport, but all SIP devices on a network must be configured to use the same transport the proxy server uses. Q-SYS Softphone supports TCP, UDP, and TLS SIP communication.

### SIP Ports

SIP typically uses port 5060 for unsecure sessions and 5061 for secure sessions using Transport Layer Security (TLS). In some VoIP systems, this can be changed if necessary.

### SIP Authentication

The vast majority of VoIP systems require some form of authentication from a device on the network before it can make or receive calls.

1. A SIP UA (i.e., an endpoint) sends a Register message with no username or password to the UAS that is serving as registrar.
2. If the system requires authentication, the registrar will reply with a challenge or Unauthorized message. The challenge message will include a nonce, which is an MD5 hash value the endpoint will use to encrypt its credentials when it replies.
3. If the username and password are correct, the registrar will respond with a 200 OK message and the endpointâs location will be updated and stored in the location server. Only then will the endpoint be able to send or receive calls.

Message flow in simple digest authentication

[SIP Call Flow](javascript:void(0))

### Call Setup

With the endpoint registered, calls can then be attempted to or from it. Each call begins with an INVITE message to or from the proxy server. The INVITE message includes information about where the call is to be directed.

INVITE message example

The INVITE also often includes information about the streaming audio formats supported by the caller. The different audio encoding and decoding formats are called codecs. The Session Description Protocol (SDP) advertises what codecs a device supports and typically lists them in preferred order from highest to lowest quality. Including the SDP information in the INVITE message is called âearly offer," which is required by Q-SYS Softphone to successfully receive a phone call.

**Tip:** The range of codecs used by a particular VoIP system will often be based on available network bandwidth and licensing cost. In general, transmitting higher quality audio streams requires more network bandwidth.

The SDP information also details the supported DTMF type and includes contact and port information that tells the far end how to route RTP audio once a codec is chosen.

Simplified codec negotiation

Simplified unsuccessful codec negotiation â there is no codec in common

Content of INVITE SIP message with Session Description

When the INVITE message is received, the proxy server will have the location server determine how to route the call to the appropriate party. If it is an internal call, it might be to another phone or softphone on the same network. It may be to a peer on the other side of a SIP trunk (on another VoIP network). It may be to a phone connected to the public switched telephone network (PTSN), in which case the VoIP call is established to a media gateway that will provide the appropriate signaling to the analog telephony network.

Simple VoIP Network with Media Gateway to PSTN

Once the proxy knows where to direct the INVITE message, it will forward the message to the appropriate device in the appropriate manner. The softphone or phone being called will respond to the proxy and then the proxy will in turn respond to the caller. When the details of the upcoming call are established, the proxyâs response to the caller will be a RINGING message.

Once the call is answered at the far end, the session initiation protocol has done its job and the peers now set up the call, with the two parties now directly exchanging the audio streams necessary for communication. The proxy server may establish a session timer, a SIP-based method of periodically checking the status of the call. If not, the SIP is finished until itâs time to tear down the call.

SIP, RTP/RTCP message flow for simple SIP call

### The Call Itself

To send and receive streaming audio, the call uses another set of protocols: Real Time Protocol (RTP) and Real Time Control Protocol (RTCP). They are used to send and supervise the audio streams to each device participating in the call. As noted before, each device lists the audio codecs it supports in a preferred order, and the call will use the highest priority format common to both devices. If they have no codecs in common, the call cannot take place.

### DTMF Considerations

Sometimes the caller must negotiate voice prompts or conference call codes using the keypad. In VoIP telephony, the calling device typically does not play these tones and send them via RTP to the far end. Instead, control commands that identify the keys pressed are sent to the far end. This is called âout-of-bandâ DTMF. The Q-SYS softphone supports two common formats for out-of-band DTMF: RFC2833 and SIP INFO. RFC2833 uses Event messages in the RTP stream to convey DTMF signals, while SIP INFO sends INFO messages in the SIP flow. If the call goes to the PTSN through a media gateway, the gateway is responsible for converting the tones into analog audio.

**Note:** A VoIP device sending actual audio tones within the RTP stream is called âin-bandâ DTMF. Q-SYS Softphone supports out-of-band DTMF.

### Tearing Down the Call

When the call is finished, of course, someone hangs up. The device that does so sends a BYE message to signal the end of the call. Each peer responds appropriately and the RTP streams stop.

[Secure SIP (TLS)](javascript:void(0))

Some VoIP systems require Transport Layer Security (TLS). This form of secure SIP takes extra care to confirm endpoints are authorized and in turn encrypts the SIP and RTP traffic on the VoIP network. This makes it virtually impossible to intercept and decode with network tools used by would-be hackers.

[Hosted SIP Solutions](javascript:void(0))

With a hosted or cloud-based SIP solution, the SIP registrar and proxy lie on the Internet side of the typical router or firewall that sits between a local area network (LAN) and the Internet itself. While the basic SIP exchange for registration and call flow remain the same, the introduction of the router or firewall can complicate matters.

Simple diagram of a hosted SIP proxy solution

### Firewalls

A firewallâs job is to protect a network from outside attacks and unauthorized access to internal resources. It typically works by allowing traffic to flow only on UDP/TCP ports that are known to be used for necessary services and blocking all others. Although the port used for SIP is static (typically 5060), the ports used for the audio portion of the call (RTP/RTCP) are dynamic. This requires that the firewall opens a wide range of ports, which can compromise the security of the network.

### Network Address Translation (NAT)

Routers typically employ Network Address Translation (NAT) when forwarding network packets from the LAN to outside networks. When doing so, the router replaces the IP address of a computer on the LAN with its own public IP address so hosts on the Internet know where to reply. The router is responsible for recording what packets were forwarded and then making sure any replies make it back to the originator on the LAN. If the NAT router receives an unsolicited packet, however, it may not know what local device should receive it. For example, a call into the LAN from a cloud-based proxy may not reach the intended recipient. Even if the call is negotiated properly from the SIP perspective, the router still may not know how to forward the resulting RTP/RTCP traffic, resulting in a call with no audio.

In addition to NAT, some routers employ port address translation (PAT), meaning the UDP or TCP port number may change as a message moves from the public to the private side of the router. This, of course, can compound the problem. The Q-SYS Softphone offers STUN support to help get around these issues.

### STUN

Session Transversal Utilities for NAT (STUN) is a simple mechanism to help a peer on a private network discover its public IP address. In this case, the Q-SYS Softphone would periodically contact a STUN server on the Internet (public side of the NAT router) on a known UDP port. The STUN server sends a response to the softphone that includes the IP address presented to the STUN server (the softphoneâs public address) as well as the originating port number (the public port number in the case of PAT). The Q-SYS Softphone can then write the public IP address into the SDP contact information. The originating port number is used for the RTP and RTCP, which has already been âpunchedâ through the NAT router or firewall.

**Note:** While Q-SYS Softphone can be configured to enable STUN support to accommodate connection to SIP proxies on the public Internet, it may not be required for your site. Check with your IT administrator if you are unsure.

[VLAN Tagging Concerns](javascript:void(0))

Many VoIP or SIP endpoints support attachment to the general data network for some functions (such as DHCP addressing, passing data to a secondary Ethernet port, etc.) while applying a âtagâ to the SIP and RTP traffic. This allows the tagged traffic to be prioritized and handled in different ways by the IT infrastructure. Note that the Q-SYS Softphone does not offer this option to tag its transmissions. If a tag is required, the switch port to which the Q-SYS Softphone is connected must be configured to add the tag upon ingress. Egress traffic should present to the Q-SYS Softphone untagged.
