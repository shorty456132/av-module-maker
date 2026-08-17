# Security Tools

> Source: https://help.qsys.com/Content/Security/Security_Tools.htm

# Security Tools

The Q-SYS suite of software includes many tools for configuring a Q-SYS system for a security-focused environment.

[Q-SYS Core Manager](javascript:void(0))

Use Q-SYS [Core Manager](../Core_Manager/CoreManager_Overview.htm) to configure access to Q-SYS Core processors.

* Enable Access Control, configure the root Administrator account, and configure additional Users and Roles for managing the Core.
* Use the Network Services Manager to disable unused network services on a per-network adapter level. Network Services provides the broadest visibility and control over the security of the Q-SYS Core. To learn more, and to see a list of use cases, see the Core Manager > [Network > Services](../Core_Manager/Core_Management/Network_Services.htm) topic.
* Install a CA-signed certificate.
* Enable 802.1X port-based authentication.
* Configure the Q-SYS Core's network adapter settings, including its hostname, IP address, netmask, and gateway.
* Use the Security tab under Access Management to manage sign in behavior, password requirements, and file upload permissions.

**CAUTION:** By default, the Q-SYS Core is unprotected and all network services are enabled. Enabling Access Control is one of the most important steps you can take to tighten the security of the Q-SYS system. To restrict access to the Q-SYS Core, you must create users and assign permissions in Q-SYS Core Manager. QSC recommends disabling network services that are not required by the system design running on the Core.

[Q-SYS Reflect](javascript:void(0))

[Q-SYS Reflect](../Reflect/reflect_overview.htm) includes multiple areas for defining access control.

* The Organization Owner is the only user role at the Organization level in Q-SYS Reflect and manages all Sites, Subscriptions, and API access to the Organization. This user has Administrator-level access to all Q-SYS systems registered with the Organization and can manage access control for other users. The Organization Owner also creates and manages tokens for access to the Q-SYS Reflect API.
* The Site Manager and Site Member roles are set on a site-by-site basis and determine access rights to those Cores registered to the associated Site. A Site Manager automatically has Administrator-level rights to all Cores within a Site, while a Site Member can have either Administrator, Technician, or Viewer permissions to those Cores. To learn more, see the [Reflect Users and Roles](../Reflect/Reflect_Sites/Users_Roles.htm) topic in the Q-SYS Reflect Help online.
* The Maximum Reflect Access Level setting, configured for each Core within Core Manager during the registration process, allows the Administrator to determine the maximum permissions allowed to that Core from Q-SYS Reflect. This setting supersedes the permission level of any Q-SYS Reflect user. For example, if a Core is registered with Reflect with a Maximum Reflect Access Level of 'Viewer', then Technicians and Administrators will only have Viewer-level access to that Core. To learn more, see the Core Manager > [Reflect](../Core_Manager/Core_Management/Reflect.htm) topic.

**Note:** Each Q-SYS Reflect user must have a QSC account, also known as a [QSC ID](https://id.qsc.com/).

[Q-SYS Peripheral Manager](javascript:void(0))

Use [Peripheral Manager](../Peripheral_Manager/PeripheralManager_Overview.htm) to configure access to Q-SYS peripherals.

* Configure device passwords to prevent unauthorized access to basic device settings, including network settings.
* Enable 802.1X port-based authentication.
* Install CA-signed device certificates.
* Configure the peripheral's network adapter settings, including its hostname and IP address, netmask, and gateway.

[Q-SYS Administrator](javascript:void(0))

Use Q-SYS [Administrator](../Administrator/AdministrationInterface.htm) to create PINs specifically for:

* External Control (using the External Control Protocol).
* Page Stations and various functions within the PA System, including which paging commands are available to each user.

**Note:** Access to Q-SYS Administrator is governed by Q-SYS Core Manager users and user roles.

[Q-SYS Configurator](javascript:void(0))

Use Q-SYS [Configurator](../Hardware/0017_Configurator.htm) to discover all Q-SYS networked Cores and peripheral devices. Q-SYS Configurator is part of Q-SYS Designer Software and uses unencrypted QDP to discover all Q-SYS devices on the network.
