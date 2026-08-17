# Nextiva

> Source: https://help.qsys.com/Content/Application_Integration/Conferencing/Nextiva.htm

# Nextiva

Use this topic to aid in configuring Q-SYS Softphone for Nextiva.

[Obtain the Nextiva SIP Registration Information](javascript:void(0))

1. Navigate to <https://np3.nextiva.com/NextOSPortal/ncp/login>
2. Log in with your account credentials. The NextOS menu appears.
3. Navigate to the Voice & Analytics section.
4. In the bottom left corner, click Users.
5. From the Users menu, click Manage Users.
6. On the Manage Users page, hover over an existing user and click the edit icon -OR- if a new user is needed, click Add Users from the menu.
7. From the Manage Users options, click Device.
8. On the Device screen:

   * Set Available Devices to "Generic SIP Phone".
   * The SIP Username and Domain should already be filled in.
   * Type the Authentication Name and password, and then click Save.

[Configure Q-SYS Softphone for Nextiva](javascript:void(0))

Refer to the [Hosted SIP Configuration](Hosted_SIP_Configuration.htm) topic as a general guide for configuring Q-SYS Softphone for a hosted SIP provider. Use the following parameters to configure for compatibility with Nextiva.

### Terminology Cross-Reference

Use this table as a guide for converting Nextiva terms to those that Q-SYS Softphone uses.

| Nextiva | Q-SYS Softphone |
| --- | --- |
| SIP Username | Username |
| Domain | Proxy |
| Authorization Name | Authentication ID |
| Password | Password |

### Configuration Notes

|  |  |
| --- | --- |
| Multiple Extensions | Nextiva does not lock down third-party SIP devices to a MAC addresses. This allows multiple extensions to be configured per Q-SYS Core processor. |
| CID Name | This should be the phone number of the extension. |
| DTMF | RFC2833 is supported. DTMF INFO is not supported. |
| Outbound SIP Ports | All traffic uses port 5060. |
| TLS/SRTP | TLS and SRTP are not supported. |
| UDP and TCP | Use port 5060. |
| Audio Codecs | Nextiva supports these codecs:   * G.711 ulaw * G.711 alaw * G.722 * G.729 * G.726 |
