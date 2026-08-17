# Cisco CUCM â Single Extension

> Source: https://help.qsys.com/Content/Application_Integration/Conferencing/Cisco_CUCM-Single.htm

# Cisco CUCM â Single Extension

Follow the instructions in this topic to set up Q-SYS Softphone for Cisco Unified Communication Manager (CUCM) in a single extension configuration.

[Prerequisites](javascript:void(0))

When you add users and extensions to the Cisco Unified Communications Management (CUCM) system, make sure you have adequate licensing to proceed. The Q-SYS Core is a third-party SIP endpoint in the CUCM system, and therefore each extension may require available licenses. Purchase any needed licenses from Cisco.

Concepts in this procedure can be applied also to other versions of CUCM.

**Note:** In Q-SYS Designer Software, either "early offer" or "late offer" can be used to negotiate media parameters in SDP such as codecs.

[Security Profile](javascript:void(0))

You must first have a Security Profile set up in Cisco Unified CM Administration. To create one or to verify that you have an existing one, select System > Security Profile > Phone Security Profile.

1. To find an existing profile, enter the search parameters, patterns, and text, if there are any. Click Find. Click on the record that you need to view.
2. To add a new profile, click Add New. Select Phone Security Profile Type. Then select Third-party SIP Device (Basic).
3. In the Phone Security Profile Configuration page, enter the information as shown in the screenshot below. Click Apply Config, and then click Reset and then Save.

[Add an End User](javascript:void(0))

1. Next, configure the End User account. Select User Management > End User > Add New.
2. In End User Configuration, enter the information shown in the below screenshots. When you have completed the settings, click Save.

**Note:** What CUCM calls User ID, a Q-SYS softphone calls Authentication ID, and what CUCM calls Digest Â­Credentials, a Q-SYS softphone calls Password.

[SIP Profile](javascript:void(0))

1. Next, configure the SIP profile for Q-SYS. Select Device > Device Settings. Click Sip Profile.
2. Find "Standard SIP Profile" in the list. Click its Copy icon.
3. In the SIP Profile Configuration window, give the configuration a new Name that describes its status as both a standard SIP profile and a Q-SYS softphone (such as Standard SIP Profile Q-SYS).
4. Configure the SIP profile as shown in the screen shots below. When you have completed the settings, click Apply Config. Then, click Reset, and then Save.

**Note:** Q-SYS softphone allows both SIP Early Offerâwith or without Media Termination Point (MTP)âwith Session Description Protocol (SDP) and SIP Late Offer. However, if DTMF or other problems arise with SIP Early Offer and without MTP, try enabling MTP.

[Add and Configure a Softphone in CUCM](javascript:void(0))

1. Select Device > Phone. Click Add New. In Phone Type, select Third-party SIP Device (Basic) and click Next.
2. Configure the settings as shown in the screenshots below. When you have completed the settings, click Apply Config. Then, click Reset and then Save.

**Note:** Media Termination Point is optional and can be checked if you experience problems with DTMF or if transcoding between audio codecs is needed. This setting makes a media resource required on CUCM for every call. This feature can be expensive and should only be used if needed.

**Note:** Require DTMF Reception might be necessary if dialing 9 for outbound PSTN calling does not work.

[Add a Directory Number](javascript:void(0))

1. Click Add a New DN.

1. Configure the settings as shown in the below screenshots. When you have completed the settings, click Apply Config. Then, click Reset and then Save.

**Note:** The Directory Number is the same as the Username field in Q-SYS Core Manager > Softphone settings.

[Set Up Softphone for CUCM in Q-SYS](javascript:void(0))

1. Open Q-SYS Designer Software. Go to File > Load from Core & Connect and then select the Core processor.
2. Go to Tools > Show Core Manager. Select Softphones. Click Softphone-1, and then click Edit.
3. Configure the parameters for the softphone. Of note:
   * Core Interface - Select the LAN interface to use for VoIP traffic. This interface must be able to reach CUCM.
   * Audio Codecs - Select only G.722 and either G.711 ulaw or G.711 alaw (largely depending on the systemâs location). In North America, G.711 ulaw is prevalent; outside North America, G.711 alaw is more common. Contact your phone system admin if you are not sure.
   * Username - This usually matches the Directory Number in CUCM.
   * Transport - Use the setting that matches the Transport Type in the Phone Security Profile in CUCM.
   * Proxy - This is the IP address of the CUCM server. If you are using a cluster of CUCM servers with a publisher and multiple subscribers, the proxy IP should be one of the servers that allows registration.
   * Authentication ID - This is the same as the User ID on the End User screen in CUCM.
   * Password - This is the same as the Digest Credentials.

1. Click Save. Registration may take from a few seconds up to a few minutes to complete.

**Note:** If registration fails, enable the Logging option in Shared Settings, and then click Save again. Use a web browser to view the Q-SYS Core processorâs SIP web page at http://<IP address of Q-SYS Core>/sip.txt. The SIP response codes listed should help indicate the type of issue occurring with registration.

[View the Registered Phones in CUCM](javascript:void(0))

1. Cisco Unified CM will list the phones that are successfully registered. To view the list in CUCM, go to Device > Phone. The phones will be listed by device name.
2. The Q-SYS softphone should appear in the list. Its Status should be "Registered with pub" as shown in the screenshot.

1. Click on the Q-SYS Softphoneâs Device Name. Its Phone Configuration page appears, which shows the real-time device status and the details of the phoneâs registration with CUCM.

[Check Gateway and DNS Configuration](javascript:void(0))

1. Go to Q-SYS Designer Software and open Q-SYS Core Manager (Tools > Show Core Manager).
2. Click Network Settings.

1. If you are using only one LAN port, configure one gateway, as shown. Additional static routes are not needed.
2. If you are using more one LAN port, configure only one gateway but add Static Routes for the second LAN port.

[SIP Response Codes for Troubleshooting](javascript:void(0))

| SIP Response Code | Description |
| --- | --- |
| 401 | SIP/2.0 401 Unauthorized  Typically caused by incorrect credentials from the calling user agent (Q-SYS Softphone), and/or misconfigured CUCM end user settings, and/or 3rd party SIP Phone settings. |
| 404 | SIP/2.0 404 Not Found  Typically has the same causes as SIP code 401 (see above). |
| 503 | Registration Failed with status Service Unavailable [503]  Typically caused by CUCM CallManager service not being enabled. Seen in clustered CUCM environments where only certain CUCM servers run the CallManager service.  Remedy: Make sure the Q-SYS Softphone is configured with the correct CUCM server (i.e., one running CallManager service).  Other common causes:  Having the wrong IP address configured in Q-SYS softphone for the CUCM server. Network issues preventing communication with CUCM. |

**Note:** The content in this topic is current through CUCM version 12.5.1.
