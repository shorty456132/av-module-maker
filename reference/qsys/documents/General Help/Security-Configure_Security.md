# How to Configure Q-SYS with Security in Mind

> Source: https://help.qsys.com/Content/Security/Configure_Security.htm

# How to Configure Q-SYS with Security in Mind

QSC recommends taking these steps in order to harden the Q-SYS system.

**Note:** Due to the large variety of use cases and project types for Q-SYS installations, the final security profile of the system is driven by the unique needs of each client and ultimately rests on the installer to meet those needs. As a result, these steps should be considered a collection of best practices that can be selectively used to meet the needs of each project.

[Upgrade the Q-SYS Core Firmware](javascript:void(0))

Q-SYS Core firmware updates are the only mechanism for distributing security patches, security features, and other updates. (Q-SYS devices do not allow for âside-loadingâ firmware.) As a general rule, if security features and patches are important to the project, then the system administrator should keep the Q-SYS Core processors up to date with the latest firmware.

For instructions, see [Installing and Updating Q-SYS Software and Firmware](../Q-SYS_Designer/0015_Installing_Q-SYS.htm).

[Enable Access Control](javascript:void(0))

One of the most effective ways to protect the Q-SYS system is to enable Access Control on all Cores and peripheral devices.

* Refer to Core Manager > [Access Management > Users](../Core_Manager/Core_Management/Users.htm) for instructions on enabling Access Control and adding users.
* Refer to Core Manager > [Access Management > Security](../Core_Manager/Core_Management/Security.htm) for instructions on creating custom role permissions for users.
* Refer to Peripheral Manager > [Device Password](../Peripheral_Manager/Device_Password.htm) for instructions on creating a Device Password, which protects basic settings such as the device's network configuration and host name.

**Note:** For Q-SYS Core processors based on Dell platforms featuring iDRAC (including the Core 610, Core 5200, and Core 6000 CXR), consider changing the default iDRAC root password to comply with your organization's standards.

[Enable Secure Communication](javascript:void(0))

In v10.0.0 and later, Q-SYS communication between Cores and Peripherals can be secured by encryption and mutual authentication using X.509 certificates. For more information, visit [Network > Certificates](../Core_Manager/Core_Management/Certificates.htm).

**Note:** At this time, we do not recommend enabling this feature on systems with more than 64 Peripherals. This limit will be removed in the next patch release.

[Set the Core Date and Time](javascript:void(0))

Accurate time and date are important in secure network environments because security certificates use time and date in the certificate exchange. Incorrect time and date can result in security certificate negotiation failures. While it is possible to manually set the time and date on the Core and let the internal clock run, this is not recommended. Over time, the clock may drift enough to result in certificate negotiation issues.

QSC recommends configuring the Core to synchronize with a trusted NTP server. This can be a local NTP server available on the LAN or a web-based NTP server.

For instructions on setting the Core's time and date and enabling NTP synchronization, see the Core Manager > [Network > Date & Time](../Core_Manager/Core_Management/Date_Time.htm) topic.

[Enable 802.1X](javascript:void(0))

An effective way to protect all network-based resources is to restrict access to the network itself. This can be achieved by enabling 802.1X on the network, which is outside the scope of this document. However, in the event that the network is configured with 802.1X, connected Q-SYS components should be configured so that they can be authenticated and granted access to the network.

* For instructions on enabling 802.1X on the Q-SYS Core, see the Core Manager > [Network > 802.1X](../Core_Manager/Core_Management/8021X.htm) topic.
* For instructions on enabling 802.1X for Q-SYS peripherals, see the Peripheral Manager > [802.1X](../Peripheral_Manager/8021X.htm) topic.

[Harden the Softphone Configuration](javascript:void(0))

If VoIP telephony (Softphone) will be used in the system design, QSC recommends only using encrypted Softphone communications and secure ciphers â assuming the third-party SIP infrastructure supports that. In Q-SYS Core Manager:

* Disable Insecure Ciphers
* Enable SRTP
* Enable TLS

For information about these options, see the Core Manager > [Telephony > Softphones](../Core_Manager/System_Management/Softphones.htm) topic.

[Disable the FTP Server](javascript:void(0))

The optional FTP server on the Q-SYS Core is disabled by default and is not recommend for use in a secure environment. Due to the inherent security concerns with FTP, it is recommended to verify that it is disabled:

1. In a browser, go to http://core-ip-address/storage\_config.html
2. Under the FTP Server section, make sure that the Enabled box is unselected.

The FTP server was deprecated in v9.3. See the [Release Notes](../Release_Notes.htm#Deprecat) section for details.

[Harden the SNMP Server](javascript:void(0))

By default, the SNMP server on the Core is disabled. In situations where SNMP monitoring of the Core and its attached peripherals is required, the user should consider implementing only SNMPv3 and follow the guidance of the InfoSec team responsible for the client network.

For instructions on configuring the SNMP server, see the Core Manager > [Network > SNMP](../Core_Manager/Core_Management/SNMP.htm) topic.

[Install a CA-signed Device Certificate](javascript:void(0))

A Device Certificate allows other network resources (for example, web browsers) to confirm that the Q-SYS device is authorized by the IT department to be on the network.

* For instructions on installing Device Certificates on Q-SYS Cores, see the Core Manager > [Network > Certificates](../Core_Manager/Core_Management/Certificates.htm) topic.
* For instructions on installing Device Certificates on Q-SYS peripherals, see the Peripheral Manager > [Certificates](../Peripheral_Manager/Certificates.htm) topic.

[Configure DNS](javascript:void(0))

Domain Name System (DNS) allows network devices to determine the IP address of a network resource derived from the URL (for example, www.qsys.com). DNS redirects can be used by bad actors to redirect traffic to compromised network resources. Therefore, it is important that only trusted DNS servers â provided by the client IT team â are specified in the Q-SYS Core's network configuration.

**Note:** DNS is required for access to Q-SYS Reflect, as well as online activation of perpetual software licenses on the Q-SYS Core.

For instructions on configuring DNS, see the Core Manager > [Network > Basic](../Core_Manager/Core_Management/Network_Settings.htm) topic.

[Configure External Control](javascript:void(0))

In situations where an external control system is used to control or monitor the Q-SYS system, it is highly recommended that this integration leverages only secure methods. External control system access should also be protected by configuring a PIN for external control.

* Secure, encrypted external control of the Q-SYS Core is currently scope-limited to the [Management APIs](../Management_APIs/Management_APIs_Overview.htm) over HTTPS. All other external control communications are currently unencrypted.
* Create users (with PINs) in Q-SYS Administrator to control access for External Control. For instructions, see the [Users (Administrator)](../Administrator/Users.htm) topic.

[Configure UCI PIN Protection](javascript:void(0))

For systems using Q-SYS User Control Interfaces (UCIs) where security is a high priority, it is recommended that UCI PINs be configured to ensure that only authorized users are able to access the UCIs. As an added layer of protection, a UCI can also be made private, which hides it from Windows and iOS UCI viewer applications.

* For instructions on setting up UCI PINs, see the Core Manager > [User Control Interfaces](../Core_Manager/System_Management/User_Control_Interfaces.htm) topic.
* To flag a UCI as private, set the Private property to 'Yes' in the User Control Interface Properties in Q-SYS Designer Software. To learn more, see the [User Control Interface (UCI) Design Overview](../Schematic_Library/user_control_interface.htm) topic.

  **Note:** Q-SYS Core Manager and Q-SYS Reflect do not currently honor the Private setting, so all UCIs will be available through those web interfaces.

[Configure Paging User PIN Protection](javascript:void(0))

If the system is leveraging the PA Paging functionality, particularly with Paging Stations that are installed in public spaces, it is highly recommended to set up PIN-based user access to the Paging Stations. Not only does this ensure that access to the PA system is restricted to authorized users, this also allows the system designer to tailor access to available paging commands based on the user.

Use Q-SYS Administrator to configure users for the PA system, including assigning PA system paging capabilities. For instructions, see the [Users (Administrator)](../Administrator/Users.htm) topic.

[Disable Unused Network Services](javascript:void(0))

In consultation with the system designer, determine which network services are not required by the design running on the Core processor and can therefore be disabled on the Core. Use the Network Services manager in Core Manager to configure what network services are enabled or disabled for each of the Core's LAN adapters.

* To review a list of network services and their details, including ports and protocols, see the [Network Interfaces, Services, & Protocols](../Networking/Interfaces_Services.htm) topic.
* See the Core Manager > [Network > Services](../Core_Manager/Core_Management/Network_Services.htm) topic for instructions and use cases for disabling unneeded network services.

[Register with Q-SYS Reflect](javascript:void(0))

Registering the Q-SYS Core processor with Q-SYS Reflect will facilitate aggregated visibility and remote monitoring and management of all Q-SYS-based AV systems, including third-party devices.

During the registration process, consider the appropriate setting for the Maximum Reflect Access Level based on the risk profile of the customer and the amount of value desired from the Q-SYS Reflect service. As a general rule, the more restrictive this setting is, the better the Core is protected but the value of the service will be diminished. For the best experience, QSC recommends granting Q-SYS Reflect 'Administrator' access to the Core. It is then possible to use Q-SYS Reflect Users and Roles to define who has access to each Core and with what permission level.

* To get started with Q-SYS Reflect, see the [Q-SYS Reflect](../Reflect/reflect_overview.htm) topic.
* To learn how to register the Core with Q-SYS Reflect, including setting the Maximum Reflect Access Level, see the Core Manager > [Reflect](../Core_Manager/Core_Management/Reflect.htm) topic.
* To learn about access control in Reflect, see the [Reflect Users and Roles](../Reflect/Reflect_Sites/Users_Roles.htm) topic in the Q-SYS Reflect Help online.
