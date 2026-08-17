# Vonage

> Source: https://help.qsys.com/Content/Application_Integration/Conferencing/Vonage.htm

# Vonage

Use this topic to aid in configuring Q-SYS Softphone for Vonage.

[Obtain the Vonage SIP Registration Information](javascript:void(0))

1. Navigate to <https://app.vonage.com/login>
2. Log in with your account credentials.
3. From the menu on the left, click Admin.
4. From the Admin Dashboard, scroll down to the Extensions section and click View All Extensions.
5. Hover over an existing extension and click Edit.

   **Note:** The Extension Type must be "Unlimited Extension". The type "Mobile Unlimited Extension" will not pair with Q-SYS Softphone.
6. From the menu on the left, click Devices. In the upper right, click Add Device.

   **Tip:** While you can edit an existing device, we recommend adding a new device because it allows multiple endpoints (i.e., Q-SYS Cores) to use the same extension.
7. Fill out the Add Device fields:

   * Device Name: Your choice.
   * e911 Location: Your choice.
   * Provisioning Model: Softphone
   * SIP/Authorization ID: Defined by the Vonage account. Note this information for later.
   * SIP Password: Create a new SIP password. Note that the password is unreadable and can only be changed.
   * MAC Address: Type a bogus address, such as the one shown in the image below. However, note that you cannot reuse a MAC address already being used by another extension in the Vonage account.
   * Registrar / Proxy: This is related to the Vonage account. For example: aXXXXXX.ac1.vbspbx.com, where XXXXXX is the account. Note this information for later.
8. Delete any previously existing devices for the extension you are using, if needed.

[Configure Q-SYS Softphone for Vonage](javascript:void(0))

Refer to the [Hosted SIP Configuration](Hosted_SIP_Configuration.htm) topic as a general guide for configuring Q-SYS Softphone for a hosted SIP provider. Use the following parameters to configure for compatibility with Vonage.

### Terminology Cross-Reference

Use this table as a guide for converting Vonage terms to those that Q-SYS Softphone uses.

| Vonage | Q-SYS Softphone |
| --- | --- |
| N/A | Domain |
| Registrar/Proxy | Proxy |
| Authorization ID | Username\* |
| Password | Password |
| Authorization ID | Authentication ID\* |

\* Username and Authentication ID are the same. Set both to the Vonage Authorization ID.

### Configuration Notes

|  |  |
| --- | --- |
| Username | Authorization ID (this is not the subscriber number)  Username and Authentication ID are not unique. |
| Multiple Extensions | Vonage does not lock down third-party SIP devices to a MAC address. This allows multiple Vonage Softphones per Core. |
| DTMF | RFC2833 is supported. DTMF INFO is not supported. |
| Outbound SIP Ports | All traffic uses port 5060. |
| TLS/SRTP | * TLS is supported. * SRTP is supported with both UDP and TCP.   TLS and SRTP can be used together or individually. |
| UDP and TCP | Use port 5060. |
| Domain | Not required. |
| Audio Codecs | Vonage supports the following:   * G.711 ulaw * G.711 alaw * G.722 * G.729 |
