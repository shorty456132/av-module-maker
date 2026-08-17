# Core Manager

> Source: https://help.qsys.com/Content/Core_Manager/CoreManager_Overview.htm

# Core Manager

Q-SYS Core Manager contains a set of tools for managing Q-SYS Core processors. Beginning with Q-SYS version 8.0, it replaces many of the configuration and management functions formerly found in Q-SYS Administrator and Q-SYS Configurator.

## Accessing Q-SYS Core Manager

Q-SYS Core Manager is accessible from Q-SYS Designer or from a browser.

[From Q-SYS Designer](javascript:void(0))

* While connected to a design running on the Core, click the Core name hyperlink under the menu bar or click Tools > Show Core Manager. (Core Manager is not accessible from Q-SYS Designer when running a design in Emulation mode.)
* You can also access Core Manager from within Q-SYS Configurator by selecting any Core running Q-SYS 8.0 or higher.

**Note:** Because Core Manager uses self-signed certificates, you may see a "connection is not private" or similar warning in your browser. You may safely ignore this warning.

[From a Browser](javascript:void(0))

Navigate to your Core's IP address. If you do not know the IP address, you can obtain it from the Q-SYS Core's front panel. Press the Next button until you see the IP address.

**Note:** If Access Control is enabled, a login username and password are required to log in to Q-SYS Core Manager. For more information, see [Access Management > Users](Core_Management/Users.htm).

## Q-SYS Core Manager Pages

### Monitoring

#### [Status](Status.htm)

Provides an overview of the health of the Q-SYS system, including a list of all devices in the running design and their statuses.

#### [Event Log](Event_Log.htm)

View a list of logged Core events. Easily filter by severity, category, source, and date.

### Core Management

#### [Network > Basic](Core_Management/Network_Settings.htm)

View and configure how the Q-SYS Core connects to the network.

#### [Network > Date & Time](Core_Management/Date_Time.htm)

Adjust the Q-SYS Core's date, time, and time zone.

#### [Network > Services](Core_Management/Network_Services.htm)

Disable unused network services on a per-network adapter level. See a summary of all enabled network services and protocols.

#### [Network > SNMP](Core_Management/SNMP.htm)

Configure SNMP access on the Q-SYS Core processor.

#### [Network > Certificates](Core_Management/Certificates.htm)

Install device certificates on the Q-SYS Core processor to meet organization security requirements and allow web browsers to trust connections to the Core.

#### [Network > Secure Communication](Core_Management/Secure_Communication.htm)

Enable encrypted communication for device and control connections.

#### [Network > 802.1X](Core_Management/8021X.htm)

Enable or disable 802.1X for each LAN interface to comply with network security requirements.

#### [Network > Multicast](Core_Management/Multicast.htm)

Configure the IP address ranges used for multicast address assignment for the Q-SYS cameras, video endpoints, and AES67 transmitters in your design.

#### [Access Management > Users](Core_Management/Users.htm)

Enable Access Control, add users, and assign user roles.

#### [Access Management > Roles](Core_Management/Roles.htm)

View role permissions and create custom user roles for Core management.

#### [Access Management > Security](Core_Management/Security.htm)

Enable and configure security policies.

#### [Licensing](Core_Management/Licensing.htm)

Activate, back up, and restore QSC Feature Licenses on the Q-SYS Core processor.

#### [Files](Core_Management/Audio_Files.htm)

Manage audio content stored on the Q-SYS Core processor for use by the Audio Player component, Public Address (PA) system, and Softphones in your design.

#### [Utilities](Core_Management/Utilities.htm)

Download the Q-SYS log file (if requested by Q-SYS Support), change the Core 510i operation mode, and reboot the Q-SYS Core processor.

#### [Reflect](Core_Management/Reflect.htm)

Register the Core with Q-SYS Reflect and test your Core's ability to connect to the Reflect servers.

### System Management

#### [User Control Interfaces](System_Management/User_Control_Interfaces.htm)

Manage access to the UCIs contained in your design.

#### [Telephony > Softphones](System_Management/Softphones.htm)

Configure Softphone global parameters and individual Softphone parameters.

#### [Telephony > Contacts](System_Management/Contacts.htm)

Create Local and LDAP contact books for use by the Contact List component, which you can then use to feed dial strings into a Softphone.

#### [Video > Cameras](System_Management/Cameras.htm)

View and set properties for all Q-SYS cameras in your design.

#### [Video > Video Endpoints](System_Management/Video_Endpoints.htm)

Manage network settings, image content, and EDID files for the NV Series Network Video Endpoints in your design.

#### [Dynamic Pairing](System_Management/Dynamic_Pairing.htm)

Pair a virtual Q-SYS hardware component in your design with a matching physical hardware device on the network.
