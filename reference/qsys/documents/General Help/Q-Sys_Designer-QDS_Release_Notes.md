# What's New in Q-SYS 10.2

> Source: https://help.qsys.com/Content/Q-Sys_Designer/QDS_Release_Notes.htm

# What's New in Q-SYS 10.2

This topic covers release information for Q-SYS 10.2 and any maintenance releases.

**Note:** Before upgrading your system, review the [Q-SYS Compatibility](../Q-SYS_Compatibility/Q-SYS_Compatibility_Overview.htm) section. This ensures that your products are compatible with the newest version of Q-SYS Designer Software.

## v10.2.0

Version 10.2.0 was released February 24, 2026 and includes these updates and resolved issues.

### Platform

[Refreshed Q-SYS Peripheral Manager Experience](javascript:void(0))

Q-SYS Peripheral Manager has been refreshed with a streamlined look and feel that aligns with Q-SYS Core Manager, delivering a more consistent and intuitive experience across the platform. The updated design standardizes navigation across Q-SYS management tools, and lays the groundwork for future enhancements to peripheral configuration and monitoring. This new interface is now available for all supported Q-SYS Peripherals, excluding NL, NM, and QIO series, which will be updated in a future release.

[Expanded Date and Time Configuration for Peripherals](javascript:void(0))

Q-SYS Peripheral Manager now introduces a Date & Time page that improves visibility and resilience for time synchronization on supported peripherals (excluding NL, NM, and QIO series). This page allows you to:

* View date / time status and NTP details inherited from the hosting Q-SYS Core, when the peripheral is part of a Design.
* Configure a backup NTP server to maintain accurate time when the device is operating not yet part of a system or temporarily cannot reach its hosting Core.
* Set up a secure backup NTP connection to meet requirements for authenticated or encrypted time sources in security-conscious environments.

[Early Warning When Opening Older Designs in a Newer Major Version](javascript:void(0))

Avoid surprises when evaluating new major releases. When you open a Design created in an earlier major version with a newer major version of Q-SYS Designer, you now see a clear warning dialog up front explaining that once you save in the newer major version, the Design can no longer be opened in older versions. This makes it easier to explore new releases, protect legacy projects, and decide when youâre ready to commit a Design to the latest major version.

[Enhanced Schematic Elements UI and Improved Plugin Organization](javascript:void(0))

Q-SYS Designer 10.2 introduces an optional Schematic Elements UI that you can enable under File âº Preferences âº Enable the new Schematic Elements UI and toggle on or off at any time based on your preference. When enabled, the Schematic Elements pane includes:

â¢ Search filtering by element type (Components, Plugins, User Components).

â¢ Category filtering (Audio, Control, Video, etc.).

â¢ Element-type color grouping for easier scanning.

Enabling the new UI also provides improved plugin organization, grouping plugins into more intuitive folders, by manufacturer, with each plugin listed by name. When the new UI is disabled, plugins continue to appear under the traditional Asset Manager and User folders.

[Deprecated: Windows 10 Support](javascript:void(0))

Windows 10.x is no longer supported by Q-SYS Designer Software.

### Security

[New Unified Security Configuration for Peripherals](javascript:void(0))

Q-SYS Peripheral Manager now includes a dedicated Security page that mirrors the capabilities of Q-SYS Core Manager, giving administrators a familiar way to apply security best practices. On Supported peripherals excludingâNL, NM, and QIO seriesâadministrators can now:

* Configure sign-in and password policies.
* Define session behavior, including session timeout and concurrent session limits.
* Present custom legal or security banners prior to login.

[New Custom Certificates for Q-SYS Peripherals](javascript:void(0))

Q-SYS Peripheral Manager now supports installing custom private key / certificate pairs from your internal Certificate Authority, similar to Q-SYS Core Manager. For supported peripherals excludingâNL, NM, and QIO seriesâadministrators can now:

* Deploy internal or wildcard TLS certificates.
* Align Q-SYS endpoints with existing enterprise PKI standards.
* Improve trust and security for browser-based access and integrations (such as cloud and UC workflows).

### Control

[Code-Focused Tab Names in Script Programmer Mode](javascript:void(0))

Stay oriented in scripting projects at-a-glance.When you edit Text Controllers, Block Controllers, or Control Scripts in Script Programmer Mode, Q-SYS Designer now names each editor tab using the componentâs Code Name instead of its Label, so your open tabs match the identifiers you use in code.

[Certificate validation for Q-SYS Lua TLS Sockets](javascript:void(0))

Build more secure integrations with external services from your Lua scripts. The `TcpSocket:NewTls()`API now supports TLS certificate validation, so your scripts can verify server certificates against trusted CAs and enforce stricter security policies when needed.

[Design-Specific Script Programmer Mode](javascript:void(0))

Keep your scripting workflow consistent every time you open a design. Q-SYS Designer now stores Script Programmer Mode as a design property, so each design can remember and enforce its own programmer mode settingâwithout breaking compatibility with older Designer versions.

[Set a Default Script Access for New Components](javascript:void(0))

Q-SYS Designer 10.2 adds a âDefault Component Script Accessâ setting under File â Preferences â General that lets you choose how Script Access (None / External / Script / All) is applied to components as you add them to a design, so new components automatically follow your preferred scripting workflow.

[MTR Component Transition to Q-SYS Connect](javascript:void(0))

With the release of Q-SYS Designer 10.2, the Microsoft Teams Room (MTR) component has been moved to Discontinued status. This change aligns with our transition to Q-SYS Connect. In addition to enabling the TSC-101-G3 controller as a certified Zoom Room Controller, the Q-SYS Connect application bundles in the Q-SYS Control for Microsoft Teams room application enabling room controls integrations for Windows based MTR systems.

The MTR component is planned for deprecation at a later date, it is recommended that new designs migrate to uses the new functionality for Microsoft Teams Rooms integration found within the Q-SYS Connect application. Until the MTR component is fully deprecated, customers may still use the Q-SYS Control for Microsoft Teams Rooms application with the component.

Q-SYS Connect will be fully available in the 10.2.1 release.

[Q-SYS Connect for Zoom Rooms](javascript:void(0))

Bring your meeting spaces together with Q-SYS Connectâa new way to turn Q-SYS TSC Series Gen 3 touchscreens into native controllers for Zoom Rooms and other UC platforms on Windows-based room computers, while keeping all control and routing logic inside your Q-SYS Design. Instead of deploying a dedicated touch panel for every UC platform, you can present the controller interfaceâsuch as the Zoom Rooms UIâdirectly on Q-SYS touchscreens via Mediacast video and touch. From there, use familiar Q- SYS tools to map that interface to one or many controllers across single, combined, or divisible spaces. This means you can support flexible one-to-one or many-to-one mappings and even reassign control on the fly, all without extra hardware or complexity. The result? A consistent, integrated experience across all your rooms.

Ready to explore more? Click [Q-SYS Connect](../Schematic_Library/Q-SYS_Connect.htm) for a detailed look.

Q-SYS Connect is included in the Inventory, in version 10.2 to help you plan your system design today. Full download availability and support will roll out in an upcoming 10.2 hotfix, unlocking the complete Q-SYS Connect experience.

### Resolved Known Issues

* Control:Resolved an issue where pressing a button on a visible top‑layer UCI page and sliding a finger into the area of a hidden lower‑layer control could trigger that hidden control on all TSC‑G3 touchscreens.
* Control:Resolved an issue where multiple MTR UCI Viewer components in the same design would all change to the same UCI selection, preventing independent UCI selection per component.
* Control:Resolved an issue where UCI navigation buttons intermittently loaded the wrong page or did not load any page when clicked, affecting designs opened in Q-SYS Designer emulation and in Windows UCI Viewer across versions 9.10.2, 9.12.1, 9.13.x, and 10.0.x.
* Control:Resolved an issue where touching and holding an empty area of a TSC touchscreen caused all UCI elements (such as audio meters) to appear frozen and stop updating for as long as the touch was held.
* Control:Resolved an issue where Q-SYS Designer v10 crashed during emulation when both Q-SYS KNX IP Interface v1.0 and Q-SYS KNX Companion v1.0 plug-ins were used in the same design, linked by CodeName, and the Number of Groups (GA) property on the interface was set above 250.
* Control:Resolved an issue where setting the Date/Time component to Format = Custom with Format String = %s caused Q-SYS Designer to lock up and crash when emulating a design.
* Control:Resolved an issue where, the link to a css file's 'Local Source' was missing from Design Resources for an installed style.
* Control:Resolved an issue where TSC-101-G3 touchscreens reloaded the UCI when the screen was turned Off or when Screen Timeout turned the screen Off in designs that used Pin Pad controls placed on the UCI.
* Control:Resolved an issue where iterating over the controls of a component inside a plug-in using  `pairs(myComponent)` returned the first control repeatedly until reaching the Max Execution Limit, instead of iterating through all controls as expected.
* Control:Resolved an issue when the TSC-101-G3 screen turns Off (either by pressing Screen â Off or through Screen Timeout), the panel unexpectedly reloads the UCI / design instead of simply turning the screen Off.
* Control: Resolved an issue where Designer crashes when switching between UCI pages containing meters styled with CSS filmstrip classes.
* Control: Resolved an issue where non-ASCII characters drawn via the <text> element in SVG-based button graphics did not render correctly when viewed in Core Manager or Reflect.

* Control: Resolved an issue where enabling the Preview Stream for an NC-12x80 camera caused the Windows UCI Viewer screen to go black and stop displaying video, while disabling the Preview Stream restored normal UCI Viewer operation.

* Control: Resolved an issue where TSC-101-G3 touchscreens ignored the `.meter-vertical-indicator` custom CSS class for Vertical Meter components, causing meters to display the default vertical bar style instead of the intended custom SVG / PNG styling.
* Control: Resolved an issue where custom CSS was not applied properly when viewing a UCI in Core Manager or Reflect.
* Control: Resolved an issue where button icons on TSC-101-G3 and TSC-70-G3 touchscreens would intermittently fail to load and instead display a swirling loading indicator after design deployment or panel reboot.
* Control: Resolved an issue where toggle button images using Custom Button Image would not display on TSC Gen 3 touchscreens or in Windows UCI Viewer when a custom CSS file was applied, even if the CSS did not define any image-related rules.
* Control: Resolved an issue where the Plugins section of the Schematic Elements pane in Designer 10.1 incorrectly instructed users to âOpen Asset Manager to download pluginsâ instead of referencing the Q-SYS Library.
* Control: Resolved an issue where Demo Modules were visible in the Components list, in Q-SYS Designer Software.
* Control:Resolved an issue where the opacity css class caused a button to be stuck on "high"state when controls are in flexbox.
* Platform: Resolved an issue where Administrator only displayed command buttons AâH for PS-TSCG3 paging stations, even when the station was configured for additional command buttons, preventing assignment of commands to buttons IâZ.
* Platform: Resolved an issue where configured command buttons did not appear in the Revert To drop-down for Virtual Page Stations (VPS) and PS-TSCG3 paging stations, causing the list to show only no Command even when command buttons were configured.
* Platform: Resolved an issue where the multicast address configured on an Atmos RX component did not persist across Core reboots or design re-deployments, causing the Multicast Address field to be blank and require re-entry after restart.
* Platform: Resolved an issue where PTP Announce messages from Q-SYS Cores could include an incorrect message length when the Core name had an even number of characters, causing Wireshark to report malformed packets and preventing compatibility with the Linux ptp4l library and Meinberg hardware clocks.
* Platform: Resolved an issue where the Q-SYS Configurator displayed a white LED for online and healthy Cores, instead of a green LED.
* Platform: Resolved an issue where NMOS registration could fail when a Core 510i started with one or more network interfaces physically disconnected, due to invalid interface information being reported for those ports.
* Video: Resolved an issue where NC-series PTZ cameras with Auto Framing disabled, Transition Speed set to Instant, and Face Count enabled could output a cropped USB video stream after toggling camera privacy On and then Off when no faces were detected.
* Video: Resolved an issue where NC-series camera peripherals reported âMissing - Camera Status Missingâ in Q-SYS Designer after enabling Secure Communication on the Core without setting a password on the camera, instead of correctly reporting âFault - Authentication failure, Communication failure.â
* Video: Resolved an issue where Dell Inspiron 16 5625 laptops with AMD Ryzen 7 5825U CPUs were unable to establish USB bridging with NV21 over USB‑C.
* Video: Resolved an issue where Dell Inspiron 16 5625 laptops exhibited inconsistent USB‑C DisplayPort Alt Mode behavior when connected to NV21, resulting in cable detect without a valid video format, intermittent loss of video, loss of video bridging, or delays of up to several minutes before video was established.
* Video:Resolved an issue where UCIs hosted on Windows UCI Viewer and deployed from Core did not load custom CSS files after upgrading from Q-SYS Designer 9.10 to 9.11 or later, causing UCIs with link `rel="stylesheet"` references in the HTML header to render without their intended styling.
* Video:Resolved an issue where IO-USB Bridge could introduce packet loss, image distortion, and approximately 2 seconds of video lag when bridging MJPEG video from NC cameras in UC&C + HD USB Video format, in designs originally created in older Q-SYS Designer versions and then upgraded to 9.10 or later.
* Video:Resolved an issue where Generic Display mute buttons on decoders would toggle visually but fail to mute audio when used in designs deployed with Q-SYS Designer 10.1.
* Video:Resolved an issue where selecting an unassigned Mediacast input on an NV-32 in either Core or peripheral mode could cause the design to temporarily stop and display the NV-32 informational splash screen.
* Video:Resolved an issue when running a design with NC-Pro15x peripherals for extended hours causes peripherals to become stuck in an âinitializingâ state and freezes all controls in Q-SYS Designer, with no Core Manager event log messages indicating peripherals initializing.
* Video:Resolved issue where NC-20x60 camera auto-focus could intermittently âpumpâ or breathe in and out while trying to keep subjects in focus, instead of smoothly locking focus on the subject in the frame.
* Video: Fixed an issue where switching resolution from 4K to 1080p during Tile-View streaming could cause the NV-21 encoder to enter a bad state, resulting in stream hangs.
* Video: Resolved an issue where the Windows UCI Viewer stops playing Mediacast Output preview streams, reverting to low frame rate images after a few seconds.
* Video: Resolved an issue where the camera auto-focus zone logging reported incorrect region valuesâshowing center, top, bottom, and face focus zones with mismatched identifiersâwhen changing AF sensitivity and zone settings.
