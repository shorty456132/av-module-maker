# System Overview

> Source: https://help.qsys.com/Content/Security/Scope_Protocols.htm

# System Overview

Q-SYS is a highly adaptable platform providing audio, video, and control infrastructure for a wide variety of applications. From meeting rooms to stadiums to cruise ships and theme parks, Q-SYS performs audio, video, and control signal input, processing, mixing, routing, distribution, and output within a real-time, network-connected system. The solution comprises native Q-SYS products (including software, cloud services, and hardware designed and delivered by QSC), with each system deployment including some or all of those components. Additionally, the Q-SYS OS includes a large number of optional software capabilities for integration with third-party systems such as SIP for VoIP calling, SNMP for device monitoring, multicast media streaming for audio distribution, as well as third-party Lua scripting and plugins for custom programming.

Here is an example Q-SYS deployment, including the logical signal flow (transported over a Layer 3 network):

[Q-SYS Core Processor and Other Native Devices](javascript:void(0))

[Q-SYS Core processors](javascript:void(0))

The Q-SYS Core is the main system processor for every Q-SYS system. It leverages Intel processing with a custom, highly optimized, real-time Linux operating system. The Core handles all audio and control signal processing and orchestrates the distribution of Q-SYS video signals over the network. Security patches are applied through Q-SYS firmware updates; there are no methods to apply patches outside of a Q-SYS firmware update.

[Native Q-SYS devices](javascript:void(0))

The Q-SYS OS natively supports a broad range of audio, video and control I/O interfaces and endpoints, developed and supported by QSC. The Q-SYS Core processor manages the firmware on its associated Q-SYS peripherals to ensure that they are always running the same compatible firmware as the Core.

Security updates for Q-SYS devices are applied only through firmware updates; there is no mechanism to âside loadâ a patch outside of a Q-SYS firmware update.

[Q-SYS Discovery Protocol (QDP)](javascript:void(0))

To simplify system configuration, Q-SYS uses a multicast-based device discovery protocol to advertise basic device information on the local area network. The content of the packets is benign in nature and dramatically improves the user experience for system design and deployment. To advertise network presence, one multicast QDP packet is sent every second from Q-SYS peripherals and the PC running Q-SYS Designer Software.

**Note:** QDP requires correct IGMP management and multicast routing according to Q-SYS Networking Requirements. For further information, please see [Multicast Traffic](../Networking/Multicast_Traffic.htm).

[Core and peripheral management](javascript:void(0))

Q-SYS Core processors and Q-SYS peripherals both host a native web application for local device management, referred to as Q-SYS [Core Manager](../Core_Manager/CoreManager_Overview.htm) and Q-SYS [Peripheral Manager](../Peripheral_Manager/PeripheralManager_Overview.htm), respectively. Owing to the difference in scope between a Core and a Peripheral, there are subtle differences between the capabilities and communication technologies used for each.

Both web applications support encrypted communications.

For encrypted communications, Q-SYS Core processors and other Q-SYS devices use self-signed certificates that can cause modern web browsers to present a privacy warning. This is expected and, provided the user is confident that they are connecting to the correct device, should not cause alarm. The user can avoid this by installing a Device Certificate â signed by the organization's certificate authority (CA). To learn more, see the Core Manager > [Network > Certificates](../Core_Manager/Core_Management/Certificates.htm) topic or the Peripheral Manager > [Certificates](../Peripheral_Manager/Certificates.htm) topic.

[Core-to-Core communications](javascript:void(0))

Each Q-SYS system requires at least one Core processor. However, depending on the scale, complexity, and desire of the system designer, it is possible to have more than one Core in a Q-SYS deployment. Those options are discussed here.

### Core redundancy

In this case, a pair of identical Q-SYS Core processors are assigned to the same System and are both configured to run the same design file. While both are powered up, connected to the network, and communicating with each other, only one Core (the Active Core) is communicating with connected devices.

If the Active Core fails or is removed, then the Standby Core automatically takes over responsibility for the system. To ensure that the Standby Core is running an identical configuration to the Active Core, the Standby Core continuously synchronizes all system parameters and files from the Active Core so that it is ready to take over at any time.

Q-SYS Core processors use Q-SYS Discovery Protocol (QDP) to identify each other on the network, which is an unencrypted multicast UDP announcement containing basic device information.

**Tip:** Beyond device discovery, all further communication between a redundant pair of Cores is fully encrypted.

Q-SYS Core Redundancy can be enabled or disabled in Core Manager > [Network > Services](../Core_Manager/Core_Management/Network_Services.htm). Refer to the [Network Interfaces, Services, & Protocols](../Networking/Interfaces_Services.htm) topic to see a list of protocols used for this service.

### Distributed systems deployments

In this case, two or more Core processors can be used to serve the needs of a large facility, with each Core (or pair of redundant Cores) responsible for processing and managing its own part of the complete system. In this scenario, each system can largely run independently and there may be no need to share any data between them.

However, if there is a desire to share data between each system (for example, to synchronize startup or shutdown sequences or to facilitate multi-Core paging), then it is possible to use the following native, built-in capabilities:

* Core-to-Core control using Control Link Server and Client components.
* Core-to-Core audio using Q-LAN TX and RX components.
* Core-to-Core audio and video using System Link TX and RX components.
* Users could also create their own custom, encrypted or unencrypted solutions to send data between Cores using the Control Scripting capabilities. This is outside the scope of this document.

Q-LAN TX / RX audio streams, and System Link TX / RX AV streams all use QDP for device discovery and are not currently encrypted. Refer to the [Control Link](../Schematic_Library/project_link.htm), [Q-LAN Transmitter](../Schematic_Library/output_box.htm), [Q-LAN Receiver](../Schematic_Library/input_box.htm), and [System Link](../Schematic_Library/system_link.htm) topics to learn about these components, including their characteristics and controls.

[Core-to-Q-SYS device control and management](javascript:void(0))

The Q-SYS Core processor manages all peripheral devices associated with the running design file. Device management includes configuration settings and real-time health status monitoring. **No personally identifiable information is included in these control data exchanges.**

Cores and peripherals use Q-SYS Discovery Protocol (QDP) to identify each other on the network, which is an unencrypted, multicast UDP announcement containing basic device information. Encrypted HTTPS is used to transfer any device configuration information. Real-time control communications between Cores and peripherals are not currently encrypted.

[Core-to-peripheral audio streaming](javascript:void(0))

The Q-SYS Core processor uses an RTP-based media streaming technology (Q-LAN) for distribution of real-time audio between the Core and all Q-SYS peripheral devices that feature audio I/O.

Q-LAN is not encrypted.

[Q-SYS peripheral-to-peripheral communications](javascript:void(0))

In nearly all cases, Q-SYS peripheral devices do not communicate directly with each other. Instead, they route their audio and control data to the Core, where it is processed and can be distributed to other peripherals on the network. The exception to this signal flow paradigm are Q-SYS NV Series Video Endpoints, where AV data is routed directly from peripheral to peripheral, bypassing the Core.

### Q-SYS video-protected content distribution

Q-SYS offers HDMI I/O distribution through the Q-SYS NV Series Video Endpoints using the Q-SYS Shift codec. For video content distribution, Q-SYS NV Series devices are designed to transmit AV streams over the network directly from Encoder to Decoder. Q-SYS NV Series devices use QDP, just like the other Q-SYS devices on the network, as part of their discovery process.

The video content within the AV streams between Q-SYS NV Series devices is encrypted with AES-128, as required by the HDCP 2.2 standard.

To reduce the chance of multicast IP address overlap, 'Auto' mode (default) seeds addresses in the ranges 233.252.43.0 â233.252.43.255 using a combination of the device type and MAC address of the Core's primary LAN interface. For each Core, the third octet of the range receives the seeded value.

### Q-SYS IP camera video streams

Q-SYS offers a portfolio of IP video cameras to facilitate highly flexible camera distribution and switching for a variety of applications. The IP cameras stream video data across the network before finally being converted to USB using one of the various Q-SYS USB bridging interfaces. The video stream is then input to a PC using built-in UVC and UAC drivers over USB.

* NC Series Cameras: The Q-SYS Core processor uses QDP to discover all Q-SYS NC Series Cameras.

To reduce the chance of multicast IP address overlap, 'Auto' mode (default) seeds addresses in the following ranges 233.253.43.0 â 233.253.43.255, 239.255.255.250, 224.0.23.175 using a combination of the device type and MAC address of the Core's primary LAN interface. For each Core, the third octet of the range receives the seeded value.

**Note:** The network-based camera video streams and control data are not currently encrypted.

#### Q-SYS IP camera video previews

Q-SYS cameras provide a still image preview that is updated once per second. This preview image is useful for aiming the camera, validating recalled presets, and verifying the image being sent to the conferencing system or USB bridging infrastructure. The preview image is available for client devices or software applications to download and display. This preview is often presented on the in-room touch screen controller displaying the User Control Interface (UCI).

In Q-SYS version 9.3.0 and later, Q-SYS cameras offer a lower resolution live video Preview Stream for consumption by third-party devices and applications. This is configured through the [Status/Control (Cameras)](../Schematic_Library/onvif_camera_operative.htm) or [USB Video Bridge](../Schematic_Library/usb_uvc.htm) component, and is an RTSP stream with an H.264 codec.

Q-SYS Reflect allows authorized support personnel to access the Q-SYS Core processors to view and interact with UCIs remotely using a web browser. The camera preview image is therefore viewable if it is placed in the UCI. Users who have access to the Core using Q-SYS Designer Software, either locally or remotely via Q-SYS Reflect, can also view these camera preview images.

**Tip:** If the ability to view camera preview images remotely on a UCI is a security concern, then the camera preview should not be placed on the UCI. Alternatively, if having a camera preview in the UCI is required, it is possible to add PIN protection to the UCI. To learn how, see the Core Manager > [User Control Interfaces](../Core_Manager/System_Management/User_Control_Interfaces.htm) topic.

[Q-SYS Scripting Engine](javascript:void(0))

The Q-SYS OS includes an open scripting environment for custom programming that can be enabled through a perpetual software license or, in the case of some older Core processor models, is included with purchase of the Core. The Q-SYS Scripting Engine allows the user to create scripts to perform any number of tasks that go beyond the native capabilities of the platform.

Common uses of the Scripting Engine are control, management, and monitoring of third-party devices and advanced system automation tasks. The Scripting Engine offers both native Lua libraries and libraries that are customized for Q-SYS. Users can author scripts in a traditional script editor or use a modular, block-based code editor for easier manipulation of the underlying Lua code.

The Q-SYS Scripting Engine facilitates both custom, user-defined scripts as well as plugins that are distributed through Q-SYS Library in Q-SYS Designer Software. The contents of user scripts can optionally be encrypted. They can also be protected from unauthorized changes with the Core's Access Control capabilities.

To learn about how to enable Access Control on the Core, see the Core Manager > [Access Management > Users](../Core_Manager/Core_Management/Users.htm) topic. For details on the full capabilities of the Q-SYS Scripting Engine, see the [Control Scripting](../Control_Scripting/Using_Lua_in_Q-Sys/01_Using_Lua_in_Q-Sys_Overview.htm) topic.

[Device Certificates](javascript:void(0))

To facilitate the many areas throughout Q-SYS where HTTPS communication is used, the Q-SYS Core processor is configured with a self-signed Device Certificate. This can generate privacy warnings in modern web browsers, which are expected. To prevent these warnings, the user can install a device certificate â signed by the organizationâs certificate authority (CA) â to each Q-SYS Core and peripheral.

* For Q-SYS Cores, use [Core Manager](../Core_Manager/CoreManager_Overview.htm) to configure device certificates.
* For Q-SYS peripherals, use [Peripheral Manager](../Peripheral_Manager/PeripheralManager_Overview.htm) to configure device certificates.

[802.1x](javascript:void(0))

All current Q-SYS Core processors and peripherals support 802.1X for network infrastructure access protection. Enabling 802.1X is an effective way of ensuring that only authorized devices can access network resources.

* For Q-SYS Core processors, use [Core Manager](../Core_Manager/CoreManager_Overview.htm) to enable and configure 802.1X.
* For Q-SYS peripherals, use [Peripheral Manager](../Peripheral_Manager/PeripheralManager_Overview.htm) to enable and configure 802.1X.

**Note:**  Discontinued Q-SYS PTZ-IP cameras do not support 802.1X.

[SSH](javascript:void(0))

While an SSH server exists on the Core, it is protected by certificate authentication and is not available to the user. SSH access is only for diagnostics and maintenance by QSC engineering if support is requested, authorized, and local access is provided by the user. SSH is disabled by default on the Core and this setting can be checked on the Core using the Secure Maintenance & Support network service in Core Manager > Network > Services.

**Note:** SSH access to the CLI cannot currently be disabled on Q-SYS peripherals. **QSC cannot access this interface without end-user authorization for support purposes.**

[QSC-signed firmware](javascript:void(0))

Q-SYS Designer Software (QDS) v9.1.0 and later implements cryptographic code signing for Core firmware images to ensure their authenticity. For the purpose of downgrading the Core to version 9.0.1 or earlier, administrators can enable the Allow Legacy Unsigned Firmware (QDS v9.0.1 or lower) option in Core Manager > Utilities. This option is available only for Administrator users with access to Q-SYS Core Manager.

[Software Applications](javascript:void(0))

Q-SYS offers dedicated OS-specific applications and modern web applications for various functions that can be performed by the system installer, the AV technician, and even the end user.

[Q-SYS Designer Software](javascript:void(0))

Q-SYS Designer Software (QDS) is the primary software application for designing, troubleshooting, and modifying a Q-SYS system. These functions are normally performed by the system installer or AV technician.

QDS uses QDP to discover all Q-SYS devices. QDS then uses encrypted communications for all further configuration, settings, design upload and download, and firmware updates for the Q-SYS Core. QDS also supports Audio Monitoring and Live Preview Streams, which are currently unencrypted.

**Tip:** HTTPS is enabled on the Core by default and cannot be disabled.

[Q-SYS Administrator](javascript:void(0))

Administrator is a standalone Windows application used for configuration of some Q-SYS features, primarily the Paging System and Scheduled Events. This can be a convenient way for end users to adjust the playback time of certain Paging Messages or other actions.

Q-SYS Administrator uses unencrypted QDP to discover Q-SYS Core processors on the network and then HTTPS for all further communications with the Core.

[Windows UCI Viewer](javascript:void(0))

This standalone UCI Viewer application can be installed on a Windows PC and enables the user to interact with any selected UCI.

Windows UCI Viewer uses unencrypted QDP to discover Q-SYS Cores on the network and then encrypted communications for all configuration, file sync and real-time control.

For more information about the UCI Viewer application, see the [UCI Viewer App (Windows)](../Schematic_Library/uci_viewer_app.htm) topic.

[Q-SYS Control for Microsoft Teams Rooms](javascript:void(0))

This standalone application, developed specifically for any Windows-based Microsoft Teams Room compute, enables a Q-SYS UCI to be shown on the Microsoft Teams Rooms controller. Q-SYS Control for Microsoft Teams Rooms uses HTTPS and TLS for all communications with the Core.

For more information, see the [Microsoft Teams Room (MTR)](../Schematic_Library/spe_uci.htm) topic.

[Q-SYS Control app for iOS](javascript:void(0))

The Q-SYS Control app for iOS, available on Appleâs App Store, enables the user to interact with a selected UCI using an iOS device. All communications between the Q-SYS Control app and the Core processor are encrypted.

**Tip:** For backwards compatibility, the Q-SYS Control app can be configured to use legacy, unencrypted communications with Cores running older firmware where encrypted communications were not available.

To ensure that the Q-SYS Control app is using encrypted communications:

1. Open the iOS Settings and scroll down to Q-SYS Control.
2. Ensure that the 'Allow Insecure Networking' option is disabled.

To learn more about the app, including its settings, see the [Q-SYS Control App (iOS)](../Schematic_Library/control_app.htm).

[Q-SYS Control for Zoom Rooms app](javascript:void(0))

The Q-SYS Control for Zoom Rooms App employs web-based technology to transmit the UCI to the Zoom Room Controller. It requires an internet connection to access the website [https://control-zr.qsys.com](https://control-zr.qsys.com/). Connection to this website only uses port 443 and DNS resolution of the URL.

To learn more about this app, including proper configuration, see [How To | Enable Third-Party Controls in Zoom Rooms](https://support.qsys.com/application-notes/how-to-|-enable-third-party-controls-in-zoom-rooms) in the Q-SYS Knowledge Base.

[Cloud Services](javascript:void(0))

QSC offers a number of optional, cloud-based services for a variety of applications and use cases. In all cases, customer privacy and data security are paramount and QSC collaborates with external cybersecurity professionals to ensure the robustness of the solution.

[Q-SYS Reflect](javascript:void(0))

Q-SYS Reflect is a modern web technology platform that can host numerous Q-SYS software services. This platform manages secure communications with Q-SYS Core processors and allows for Organization-level license management and API access control. Q-SYS Reflect is hosted on Microsoft Azure and leverages a number of Microsoft technologies for storage, encryption, key management, and more.

Q-SYS Reflect is a remote management and monitoring service for Q-SYS-based AV systems, including third-party devices.

### Communication

The Q-SYS Reflect user interface is browser-based using HTML5. All modern web browsers are therefore supported. QSC has followed IT industry best practices and implemented encrypted communications using TLS 1.3 over HTTPS and WSS between the user's web browser and the Q-SYS Reflect cloud infrastructure.

To improve the performance of real-time control on a Core processor when using a web browser, the Core and the userâs PC will route some real-time control data via a dedicated relay service. Control traffic via the relay service is always transported via Secure Web Sockets (WSS).

### Registration

The Q-SYS Core-to-Reflect registration process is manually initiated and requires local access to the Core with an Administrator login. During the registration process, an outbound connection to the Q-SYS Reflect servers is initiated. Once the registration process is complete, a persistent web socket connection between Core and Q-SYS Reflect cloud is maintained.

### Remote UCI Access

Q-SYS Reflect also allows authorized users to view and interact with all controls found on UCIs running on Cores to which they have access. This enables AV support technicians to provide operational support to clients without the need to be on-site â for example, to interact with room controls. If more granular access is required, then the system designer should consider leveraging the UCI PIN tool to further restrict and manage access to UCIs. Refer to the Core Manager > [User Control Interfaces](../Core_Manager/System_Management/User_Control_Interfaces.htm) topic to learn how.

### Q-SYS Reflect Third-Party API

Q-SYS Reflect provides a JSON-based API that can be used by third-party software solutions to extract scope-limited data from the Q-SYS Reflect database. Access to the API is governed by tokens that are generated at the Organization level by an Organization Owner. Encrypted HTTPS GET requests are then used to pull information related to system health and events. Audit events, which include username information per event, are included in the Core event logs that are accessible via the Q-SYS Reflect Third-Party API.

[QSC Licensing Portal](javascript:void(0))

If the user wishes to activate a Q-SYS perpetual feature license on the Q-SYS Core processor using the Online Activation Method, then the Q-SYS Core must be able to reach the QSC Licensing server. (To learn about license activation methods, see the Core Manager > [Licensing](../Core_Manager/Core_Management/Licensing.htm) topic.)

License activation is a user-initiated process and can be performed locally using Core Manager or remotely using Q-SYS Reflect. When the license activation process is initiated, the Core makes an outbound connection to the QSC Licensing server, which then responds with an activation code that is installed on the Core.

[Third-Party Integrations](javascript:void(0))

In addition to support for native Q-SYS hardware devices and software applications, Q-SYS can integrate with third-party hardware and software systems using commonly understood software services or protocols.

[IP-PBX and SIP servers](javascript:void(0))

The Q-SYS Core processor offers built-in SIP technology to facilitate VoIP call capability. The Core can present itself as a generic SIP endpoint or trunk to a standard SIP server. For compatibility with the huge variety of IP-PBX systems installed in the market, Q-SYS Cores offer a wide range of encrypted and unencrypted options for SIP telephony.

If secure telephony is required and supported by the SIP server, then all Q-SYS Softphones should be configured as follows in Core Manager > Softphones. To learn more about these settings, see the Core Manager > [Telephony > Softphones](../Core_Manager/System_Management/Softphones.htm) topic.

* Disable the Insecure Ciphers option in Shared Settings.
* Enable SRTP in Shared Settings.
* Select TLS for each Softphone's Transport property.

[External control of Q-SYS](javascript:void(0))

It is possible to control a Q-SYS system using a hardware or software product from a third-party vendor. The level of capability and sophistication of these systems varies widely. As a result, the Q-SYS Core processor offers both encrypted and unencrypted methods for external control.

**Note:** Owing to the flexible and configurable nature of Q-SYS, other control and data exchanges are possible. Through custom programming, it could be possible for the system designer to create scripts, plugins, or other methods that may capture and transmit PII between Q-SYS and third-party systems. Since these would be custom configurations created by the system designer, they are outside of the scope of this content.

Refer to the [Management APIs](../Management_APIs/Management_APIs_Overview.htm) and [External Control APIs](../External_Control_APIs/External_Control_APIs_Overview.htm) topics for more information.

[SNMP](javascript:void(0))

The Q-SYS Core processor hosts an SNMP server that can be enabled if the system design requires monitoring the Core and its peripherals using an external SNMP client. Q-SYS Core Manager allows the user to define access control parameters for the SNMP server, as well as define which SNMP version is enabled on the server.

SNMPv3 is considered the most secure and is recommended where possible. **SNMPv2c is available but may not be allowed based on the network security policies of the client network.**

**Tip:** The SNMP server is disabled by default on new designs.

To learn more, see the Core Manager > [Network > SNMP](../Core_Manager/Core_Management/SNMP.htm) topic.
