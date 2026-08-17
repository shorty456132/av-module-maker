# VisionSuite Release Notes

> Source: https://help.qsys.com/Content/VisionSuite/VisionSuite_Release_Notes.htm

# VisionSuite Release Notes

This topic covers release information for the Q-SYS VisionSuite software.

[v90.2.0](javascript:void(0))

Q-SYS VisionSuite Patch v90.2.0 was released February 26, 2026 with the following updates and resolved issues.

### Software Compatibility

v90.2.0 adds support for Q-SYS firmware v10.2.x.

### Hardware Compatibility

* v90.2.0 ([.patch file](https://www.qsys.com/products/q-sys/video/q-sys-visionsuite/visionsuite-updates/)) supports Q-SYS VisionSuite (ACPR + Seervision) Plugin running on the VSA-100 on Q-SYS Designer 10.2. v90.2.0 is not compatible with Q-SYS Designer 10.0.x.
* v90.2.0 is not compatible with SVS1/4. Please continue to use 90.0.5 with Q-SYS Designer 10.2 with 90.2.0 plugins for SVS1/4 applications.

[v90.1.0](javascript:void(0))

Q-SYS VisionSuite Patch v90.1.0 was released February 10, 2026 with the following updates and resolved issues.

### Prerequisites

* If your VSA-100 is running v112.0.2, you must downgrade to 90.1.0 for improved stability.
* If your SVS1/4 is running v112.0.2, you must downgrade to 90.0.5 for improved stability. The downgrade process from 112.0.2 to 90.0.5 will result in the user not being able to add zones and position containers will be improperly configured. Please contact QSC support to downgrade SVS1/4 systems.
* v90.1.0 .squash cannot be used with SVS1/4. Please continue to use 90.0.5 with Q-SYS Designer 10.1 with the 90.1.0 plugins for these devices.
* v90.1.0 cannot be used with VisionSuite Designer or VisionSuite Native.

### New Features

[Seervision Plugin Updates](javascript:void(0))

Improved plugin property and component labeling to more clearly indicate SVS1/4 vs VSA-100 connection modes

[SV Suite Updates (VSA-100 Only)](javascript:void(0))

* Compatibility with Q-SYS Designer 10.1.0
* Support for NC-Pro15x, NC-90-G2, and NC-110 PTUs
* Support for presenter tracking using NC-Pro15x with RTSP alongside the cameraâs external NDI-HX stream
* Improved detection frame rate on VSA-100 for smoother and more reliable presenter tracking
* Improved RTSP stream decode performance
* Removal of SDI option in SV Suite for VSA-100

### Resolved Known Issues

* Video Experience: Resolved issue where NC-Pro15x will randomly move to an unexpected position while tracking.
* **Seervision Plugin**: Error in Seervision Plugin when static camera has MCR Output set to <None> and system is recalibrated
* **Seervision Plugin**: "SVS1 / SVS4 Mode" property has been renamed to "VSA model" in SV Plugin.

  **Note:** Freshly installed plugins will be configured with VSA model = SVS1/4. Any existing Seervision plugins that were configured for VSA-100 with Legacy Property = No, must be manually reconfigured with VSA model = VSA-100. VSA-100 will not connect if VSA model = SVS1/4.
* **SV Suite**: RTSP stream intermittently drops out under certain stressful network conditions
* **SV Suite**: RTSP video is extremely delayed after several hours of use, resulting in poor presenter tracking

### Software Compatibility

v90.1.0 adds support for Q-SYS firmware v10.1.x.

### Hardware Compatibility

* v90.1.0 ([.patch file](https://www.qsys.com/products/q-sys/video/q-sys-visionsuite/visionsuite-updates/)) supports Q-SYS VisionSuite (ACPR + Seervision) Plugin running on the VSA-100 on Q-SYS Designer 10.1. v90.1.0 is not compatible with Q-SYS Designer 10.0.x.
* v90.1.0 is not compatible with SVS1/4. Please continue to use 90.0.5 with Q-SYS Designer 10.1 with 90.1.0 plugins for SVS1/4 applications.

[v90.0.6](javascript:void(0))

Q-SYS VisionSuite v90.0.6 was released on December 9, 2025 with the following updates and resolved issues.

### Prerequisites

* If your VSA-100 is running v112.0.2, you must downgrade to 90.0.6 for improved stability.
* If your SVS1/4 is running v112.0.2, you must downgrade to 90.0.5 for improved stability. The downgrade process from 112.0.2 to 90.0.5 will result in the user not being able to add zones and position containers will be improperly configured. Please contact QSC support to downgrade SVS1/4 systems.
* v90.0.6 cannot be used with VisionSuite Designer or VisionSuite Native.

### New Features

[Seervision Plugin Updates](javascript:void(0))

* Write Protect improved to function as both a read and write protect.
* New plugin Lock property that protects against plugin configuration corruption and tampering.

### Resolved Known Issues

* **Seervision Plugin:** The issue with zones drifting after placement has been resolved.
* **Seervision Plugin:** The issue with Is Managed property missing from Seervision plugin has been corrected.
* **VisionSuite:** "Legacy Connection" property has been renamed to "SVS1 / SVS4 Mode" in SV Plugin.

  **Note:** Freshly installed plugins will be configured with SVS1/SVS4 Mode = Yes. Any existing Seervision plugins that were configured for VSA-100 with Legacy Property = No, must be manually reconfigured with SVS1/SVS4 Mode = No. VSA-100 will not connect if SVS1/SVS4 Mode = Yes.
* **ACPR:** The issue causing the graphic layout of ACPR MXA920 rotation in the wrong direction has been resolved.
* **ACPR:** The issue causing the graphic layout of crossover zones to be incorrect if the mic orientation is rotated has been resolved.
* **VisionSuite:** VSA-100 is stuck âfinishing patching processingâ has been resolved.
* **VisionSuite:** Resolve issue causing slow presenter tracking performance and frequent loss of VIP
* **VisionSuite:** The issue where tracking exclusion zone sometimes affects tracked subject causing a loss of VIP has been resolved.

### Software Compatibility

v90.0.6 requires Q-SYS firmware v10.0.x.

**Note:** v90.0.6 is not compatible with Q-SYS firmware 10.1.x.

### Hardware Compatibility

* v90.0.6 ([.squash file](https://www.qsys.com/products/q-sys/video/q-sys-visionsuite/visionsuite-updates/)) supports Q-SYS VisionSuite (ACPR + Seervision) Plugin running on the VSA-100 only.
* v90.0.6 is not compatible with SVS1/4. Please continue to use 90.0.5 for SVS1/4 applications.

[v90.0.5.2](javascript:void(0))

Q-SYS VisionSuite v90.0.5.2 was released March 25, 2025 with the following updates.

### Resolved Known Issues

* VisionSuite Plugin: ACPR connectivity issues with MXA920 fixed in bypassed state.

[v90.0.5.1](javascript:void(0))

Q-SYS VisionSuite v90.0.5.1 was released February 25, 2025 with the following updates.

### Resolved Known Issues

* VisionSuite Plugin: Fixed connectivity Issues with Shure MXA920.

[v90.0.5](javascript:void(0))

Q-SYS VisionSuite v90.0.5 was released February 4, 2025 with the following updates.

### Resolved Known Issues

* VisionSuite: The issue with the zone states not persisting after a server reboot when set via the public websocket API has been resolved.
* VisionSuite: The issue with tracking getting stuck has been resolved.
* VisionSuite Plugin: The issue where the mediacast router does not switch between Seervision cameras when in ACPR mode and an SV zone is active has been resolved.
* VisionSuite Plugin: The issue where reboot controls revert on redeploy if the room configuration is not saved before redeploying has been resolved.

[v90.0.4](javascript:void(0))

Q-SYS VisionSuite v90.0.4 was released October 15, 2024 with the following updates.

**Note:** While it may appear that certain versions are missing, note that versions 90.0.2 and 90.0.3 were released exclusively for internal use.

### Improvements

* Release notes in VisionSuite package in Asset Manager now point to Q-SYS help
* VisionSuite Plugin now has the ability to schedule rebooting all connected Seervision Servers (SVs), either daily, or on a specific day of the week. This can be used to mitigate issues with an SVs becoming sluggish or unresponsive after some time.

**Tip:** We recommend using v90.0.4 with firmware v2.0.1 and QDS 9.10.2 (or later) for all new installs. See [VisionSuite Installation/Upgrade (Legacy SV)](VisionSuite_Installation_SV.htm).

### Resolved Known Issues

* VisionSuite: Fixed multiple bugs which caused tracking to be interrupted or computer vision to fail.
* VisionSuite: Fixed a bug which caused the computer vision health to incorrectly show error when RTSP stream is not selected on factory fresh boot.
* VisionSuite: Fixed an issue with interference errors on fresh booth with no RTSP streams.
* VisionSuite Plugin: Fixed an issue where pressing F1 in Q-SYS Designer did not load the Seervision or ACPR help file.
* VisionSuite Plugin: Fixed a bug which allowed Manual Recall button to bypass the ACPR / SV Plugin's Video Auto Switch.
* VisionSuite Plugin: Fixed a bug so Exclusion Zone and Tracking Zone dropdowns are initialized to "<None>" on initial plugin load.
* VisionSuite Plugin: Fixed a bug which caused room configuration controls to not save their values/states between multiple room configurations.
* VisionSuite Plugin: Fixed TCCM's in ACPR caused by mismatched controls.
* VisionSuite Plugin: Fixed a bug that caused the privacy button not to be turned off when a USB video bridge left its privacy position in all cases.

[v90.0.1](javascript:void(0))

Q-SYS VisionSuite v90.0.1 was released August 28, 2024 with the following updates.

### Resolved Known Issues

* VisionSuite: Fixed an issue that caused tracking to be stuck in 'enable' state, which prevented position containers from being recalled manually.

[v90.0.0](javascript:void(0))

Q-SYS VisionSuite v90.0.0 was released August 19, 2024 with the following updates.

### New Features

[Offline updates for Q-SYS AI Accelerator](javascript:void(0))

Allows you to update firmware on your AI accelerator without an internet connection.

[mDNS server discovery](javascript:void(0))

Enables the Seervision control plugin to discover the Seervision server using Q-SYS Designer Software, replacing the manual IP address discovery process.

[Privacy Mode for Divisible Rooms](javascript:void(0))

Enables a single press to rotate PTZ cameras to a privacy position, switch to a user configurable privacy graphic, and stop all camera automation.

[Q-SYS Reflect Ready](javascript:void(0))

New global microphone status for ACPR enables seamless remote status monitoring from Q-SYS Reflect.

[Yamaha RM-CG Support](javascript:void(0))

Added support for the Yamaha RM-CG network ceiling microphone.

[Asset Manager Update](javascript:void(0))

Automatic Camera Preset Recall (ACPR) plugin (v3.1.0.0) has been deprecated. To deploy the latest ACPR functionality, you should continue to leverage the new Q-SYS VisionSuite plugin, which is now inclusive of both ACPR and Seervision intelligent presenter tracking control plugins.

### Improvements

* New user consent dialogue for recording video
* Improvements for ACPR RX/TX logging/debugging
* Improvements for perception / computer vision logs
* Seervision Control plugin's event log provides an easy way to trace events and actions.

### Resolved Known Issues

[VisionSuite](javascript:void(0))

* Significant improvements to RTSP robustness
* Owner ID no longer changes after provisioning
* Resolved the issue with link local VisionSuite firmware upgrades
* Resolved the issue with DNS service failures/instability
* Updates to manage UI snack bars while tracking with multiple tracking zones. When a trackable person is outside of all tracking zones, a snackbar is displayed and provides an option to disable all tracking zones.
* Resolved the issue with valid licenses displayed as expired licenses

[SV Plugin](javascript:void(0))

* Fix for intermittent disconnections between plugin and VisionSuite
* On/off functionality for Video Auto Switch with Mediacast Router now works as intended. Also, Video Auto Switch now properly waits for camera movement to complete before switching the video feed.
* Fix for recalling static camera containers with NC-110 cameras
* Fix static camera control pins for privacy opt-out
* NC-110 static camera position container does not complete because IsMoving doesn't illuminate during coordinate recalls.
* Fix for deleted containers showing in the containers drop down
