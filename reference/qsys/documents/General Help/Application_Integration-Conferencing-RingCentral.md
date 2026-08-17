# RingCentral

> Source: https://help.qsys.com/Content/Application_Integration/Conferencing/RingCentral.htm

# RingCentral

Use this topic to aid in configuring Q-SYS Softphone for RingCentral.

[Obtain the RingCentral SIP Registration Information](javascript:void(0))

1. Navigate to <http://www.ringcentral.com/>
2. In the upper-right corner, click Login.
3. Click Admin Portal.
4. Log in with your RingCentral credentials.
5. On the Phone System page, click Phones & Devices from the left side menu.
6. For an existing phone, click Setup & Provision from the Operation column.
7. In the Setup & Provisioning screen, click Select Device from the top menu.
8. Click Other Phones from the sub-menu.
9. Under Existing Phone, click Select.
10. The next screen contains the SIP registration details. There is no need to make any changes. Copy this information to use when configuring Q-SYS Softphone in the next section.

    **Note:** Although multiple outbound proxies are available for selection, SIP10.ringcentral.com or SIP20.ringcentral.com are the ones to use for North America when configuring Q-SYS Softphone.

[Configure Q-SYS Softphone for RingCentral](javascript:void(0))

Refer to the [Hosted SIP Configuration](Hosted_SIP_Configuration.htm) topic as a general guide for configuring Q-SYS Softphone for a hosted SIP provider. Use the following parameters to configure for compatibility with RingCentral.

### Terminology Cross-Reference

Use this table as a guide for converting RingCentral terms to those that Q-SYS Softphone uses.

| RingCentral | Q-SYS Softphone |
| --- | --- |
| SIP Domain | Domain |
| Outbound Proxy | Proxy |
| Username | Username |
| Password | Password |
| Authorization ID | Authentication ID |

RingCentral field names

Q-SYS Softphone field names

### Configuration Notes

|  |  |
| --- | --- |
| Username | âUser Nameâ is equal to the âPhone Numberâ.  **Note:** âUser Nameâ is not equal to the âAuthentication IDâ. |
| Multiple Extensions | RingCentral does not lock down third-party SIP devices to a MAC address. This allows multiple RingCentral extensions to be configured per Q-SYS Core processor. |
| DTMF | RFC2833 is supported. |
| Domain | Required. Adding the port to the Domain is not needed. |
| Outbound SIP Ports | Are nonstandard. (Standard is UDP and TCP 5060, TLS 5061) |
| TLS/SRTP | TLS requires SRTP.  TLS uses port 5096 and it needs to be added to the end of the proxy for outbound traffic: |
| UDP and TCP | TCP/UDP use port 5090 and it needs to be added to the end of the proxy for outbound traffic: |
| Audio Codecs | RingCentral supports the following:   * G.711 ulaw * G.711 alaw * G.722 * G.729 |
