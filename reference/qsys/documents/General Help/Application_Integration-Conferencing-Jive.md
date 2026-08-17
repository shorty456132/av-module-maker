# Jive

> Source: https://help.qsys.com/Content/Application_Integration/Conferencing/Jive.htm

# Jive

Use this topic to aid in configuring Q-SYS Softphone for Jive.

[Obtain the Jive SIP Registration Information](javascript:void(0))

1. Navigate to <https://my.jive.com/pbx/>.
2. Log in with your account credentials. The Jive dashboard and menu appear.

   **Note:** Unfortunately, the Jive dashboard does not provide information for registering a softphone. Contact Jive support to obtain your authentication credentials and proxy address.
3. From the Dashboard, select Devices.
4. The extensions in use are shown, as well as the Device Model. For example:
5. For the Device Model, select "None (Softphone)".
6. Select one of the existing extensions.
7. In the hardware details, note that the MAC address shown is irrelevant, and does not need to match the Q-SYS Core's LAN interface MAC address. For example:

[Configure Q-SYS Softphone for Jive](javascript:void(0))

Refer to the [Hosted SIP Configuration](Hosted_SIP_Configuration.htm) topic as a general guide for configuring Q-SYS Softphone for a hosted SIP provider. Use the following parameters to configure for compatibility with Jive.

### Configuration Notes

|  |  |
| --- | --- |
| Multiple Extensions | Jive does not lock down third-party SIP devices to a MAC address. This allows multiple extensions to be configured per Q-SYS Core. |
| DTMF | RFC2833 and DTMF INFO are both supported. |
| Outbound SIP Ports | All traffic uses port 5060. |
| TLS / SRTP | Not supported. |
| UDP and TCP | Use port 5060. |
| Audio Codecs | Jive supports these codecs:   * G.711 ulaw * G.711 alaw * G.722 * G.729 |
