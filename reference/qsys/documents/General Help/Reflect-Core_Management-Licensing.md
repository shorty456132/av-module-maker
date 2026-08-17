# Licensing

> Source: https://help.qsys.com/Content/Reflect/Core_Management/Licensing.htm

# Licensing

This topic describes the different types of licenses available for the Q-SYS platform, their requirements, and activation instructions.

**Note:** If you encounter an error that a license has expired, be sure to remove the expired license and install the new license.

## Scaling Licenses

Q-SYS Scaling Licenses expand the available resources of certain Q-SYS Core processors to meet specific application needs.

[Q-SYS Core Nano and Core 8 Flex Scaling License](javascript:void(0))

Supported Q-SYS Core processors: Core Nano, Core 8 Flex

This license focuses on combining the Q-SYS Collaboration Bundle Scaling License and the Q-SYS Commercial AV Bundle Scaling License, including all-purpose DSP processing power, networked audio channel capacity (128x128 channels of Q-LAN/AES67), and Media Stream capacity (up to 24x24). It also increases the maximum Q-SYS peripheral count (up to 48 Q-SYS peripherals).

|  | Q-SYS Core Nano, Core 8 Flex Base Configuration | Q-SYS Core Nano, Core 8 Flex + Capacity Scaling License |
| --- | --- | --- |
| Q-LAN / AES67 network channels | 64 x 64 | 128 x 128 |
| DSP processing power | 1x | 2x |
| Softphones | 2 | **4** |
| AEC processors @ 200ms | 8 | **16** |
| NM-T1 microphones | up to 3 | **up to 6** |
| Media / WAN network channels | 12 x 12 | 24 x 24 |
| Q-SYS peripherals | 32 | 48 |

#### Requirements

Core Nano, Core 8 Flex: Requires QDS version 10.0 and later. The [Q-SYS Collaboration Bundle Scaling License](#Q-SYS) and [Q-SYS Commercial AV Bundle Scaling License](#Q-SYS2) can still be purchased for a Core Nano or Core 8 Flex for designs that continue to run version 9.x.x or earlier.

#### Notes

* Q-SYS Collaboration Bundle Scaling License and the Q-SYS Commercial AV Bundle Scaling License can still be used if a system already has them and upgrades to version 10.0 if an entitlement already purchased has unused licenses remaining.
* If the Q-SYS Capacity Scaling License is installed on a Core already having the Q-SYS Collaboration Bundle Scaling License and the Q-SYS Commercial AV Bundle Scaling License, the greater capacities of the Q-SYS Capacity Scaling License will be utilized.
* Q-SYS Collaboration Bundle Scaling License and the Q-SYS Commercial AV Bundle Scaling License will be available for sale to use with older software versions until a new LTS version is released.

## Feature Licenses

Feature Licenses utilize Nodelock model licensing, which allows both online and offline activation.

These features require activating a license when included in a design deployed to a Q-SYS Core processor manufactured with firmware version 7.0 and above. Licensed features can always be run in Emulate Mode.

[Q-SYS VisionSuite](javascript:void(0))

Two Q-SYS VisionSuite licenses are required when deploying a design containing a [VisionSuite VSA-100 AI Accelerator](../../Hardware/Video/VSA_100.htm) to any Core model: a perpetual VisionSuite feature license and a term-limited VisionSuite update license. After the update license expires, the system continues to function, but VisionSuite can no longer be updated.

The VSA-100 requires QDS version 10.0.0 and later.

[Q-SYS AV Bridging](javascript:void(0))

The Q-SYS AV Bridging feature license applies to the following products:

* TSC-70-G3
* TSC-101-G3

This license is required per device when deploying the following components to any Core model:

* 2ch Sound Card Input/Output
* 1ch Speakerphone Input/Output
* USB Video Bridge
* HID Conferencing

[Q-SYS NV-32-H Core Mode Video Streaming](javascript:void(0))

The Q-SYS NV-32-H (Core Mode) Video Streaming feature license applies only to the NV-32-H (Core Capable). This license is required for any system with Shift streaming where the core is an NV-32-H. For example, a system with this license applied could consist of a single NV-32-H operating in Core Mode with various NV-21-HU and NV-32-H encoders/decoders. The NV-32-H will support the same level of audio, video, and control processing as it currently does.

#### Requirements

NV-32-H (Core Capable) in Core Mode: Requires QDS version 9.9 and later.

[Software Dante](javascript:void(0))

Software Dante licensing depends on your Core model, Q-SYS release, and channel count.

| Software Dante License | Deployed to Core |
| --- | --- |
| 8x8, 16x16, 32x32 | Core Nano  Core 8 Flex  NV-32-H (Core Capable)  Core 110f  Core 24f  Core 510i  Server Core X10  Core 610  Server Core X20r  Core 5200  Core 6000 CXR |
| 64x64 | Core 24f  Core 510i  Server Core X10  Core 610  Server Core X20r  Core 5200  Core 6000 CXR |
| 128x128 | Core 510i  Server Core X10  Core 610  Server Core X20r  Core 5200  Core 6000 CXR |
| 256x256 | Core 610  Server Core X20r  Core 5200  Core 6000 CXR |
| 512x512\* | Core 5200  Core 6000 CXR |

\*For the Core 6000 CXR, the 512x512 license requires the Q-SYS Core 6000 CXR Scaling License.

#### Requirements

* Core Nano, Core 8 Flex: Requires Q-SYS Designer Software (QDS) version 9.0 and later. These Core models include an 8x8 license.
* NV-32-H (Core Capable) in Core Mode: Requires QDS version 9.0 and later.
* Core 110f: Requires QDS version 8.3 and later. Core 110f processors manufactured after March 30, 2020 include an 8x8 Software Dante license. Software Dante perpetual licenses are available for purchase for older Core 110f processors and can be licensed at any supported capacity. (An 8x8 license is not required first.)
* Core 24f, Server Core X10, Server Core X20r: Requires QDS 10.0.0 and later. These Core models include an 8x8 license.
* Core 510i, Core 5200: Requires QDS version 9.0 and later. These Core models manufactured after January 1, 2021 include an 8x8 Software Dante license. Software Dante perpetual licenses are available for purchase for older Core 510i and Core 5200 processors and can be licensed at any supported capacity. (An 8x8 license is not required first.)
* Core 610: Requires QDS version 9.6 and later. The Core 610 comes standard with an 8x8 Software Dante license.
* Core 6000 CXR: Requires QDS version 9.4.x LTS or 9.7 and later. The Core 6000 CXR comes standard with an 8x8 Software Dante license.

**Note:** Software Dante licenses are not additive. For example, if your configuration requires 16x16 channels, you must activate a 16x16 license as opposed to two 8x8 licenses.

[Multi-Track Audio Player (MTP)](javascript:void(0))

An MTP license is required when deploying a design that contains one or more Audio Player components with a total Track Count exceeding 16.

**Note:** The NV-32-H (Core Capable) has a limit of 16 total audio tracks and is incompatible with MTP feature licenses.

| MTP License | Deployed to Core |
| --- | --- |
| SLMTP-32  Multi-track player supporting 32 simultaneous tracks.  Stackable1 | Core Nano2  Core 8 Flex2  Core 110f2  Core 24f  Core 110c  Core 510i2  Core 510c  Server Core X10  Core 610  Server Core X20r  Core 5200  Core 6000 CXR |
| SLMTP-643  Multi-track player supporting 64 simultaneous tracks | Core 510i  Core 510c  Core 610  Core 5200  Core 6000 CXR |
| SLMTP-1283  Multi-track player supporting 128 simultaneous tracks | Core 510i  Core 510c  Core 610  Core 5200  Core 6000 CXR |

###### 1. For Cores running v10.0 and later, SLMTP-32 may be stacked (up to each Core's specified maximum multitrack capacity), i.e, multiple SLMTP-32 licenses can be installed on the Core to achieve the desired multitrack playback capacity of (32, 64, 96, or 128 tracks). See [qsys.com](https://www.qsys.com/products-solutions/q-sys/processing/) for your Core model's maximum multitrack capacity.

###### 2. The following Cores require a Media Drive Kit to be installed to activate this license: Nano, 8 Flex, 110f, 510i.

###### 3. The SLMTP-64 and SLMTP-128 licenses are still available for users remaining on earlier versions than v10.0.

To learn how to activate a Feature License, see [How to Activate a License](#How_to_Activate).

## vCore Licenses

A vCore product license is required when deploying a Q-SYS design to any supported virtual environment (Hypervisor) running a vCore image.

[What's included](javascript:void(0))

Each vCore product license includes:

* Product key
* 3-year or 5-year maintenance plan
* Q-SYS Control feature license for vCore, which is a bundle containing the [Scripting Engine](#Scriptin) and [UCI Deployment](#UCI) feature licenses.

[Requirements](javascript:void(0))

vCore requires Q-SYS Designer Software version 9.6.0 (minimum) along with a supported Hypervisor. See the [vCore Requirements](../../vCore/vCore_Requirements.htm) for more information.

The Q-SYS vCore utilizes a Flexible license model which requires online activation. An internet connection is also required to continually validate the license. This means:

* You will not be able to upgrade or deploy a design to your vCore until it is licensed.
* If the vCore license cannot be validated for 30 days, the currently running design will stop immediately.

To learn how to activate a vCore license, see [vCore License Activation](#vCore).

## How to Activate a License

Before proceeding with activation, ensure that you have received a QSC Entitlement Information email from QSC Software Licensing. This email contains your unique Entitlement ID (EID), which is required for license activation. If you do not have this email, contact the person at your organization who placed the order for the feature licenses and ask them to forward this email to you.

**Note:** Online activation of feature, scaling, and vCore licenses requires that the Q-SYS Core processor can access the QSC Licensing Portal.

[Feature License and Scaling License Activation - Core Manager](javascript:void(0))

**Tip:** To simplify the license activation process, QSC strongly recommends that you provide your Q-SYS Core with temporary internet access, required only during the license activation process. It can be disconnected afterward, if necessary. If you are unable to connect your Q-SYS Core to the internet, you can still activate your license using an internet-connected PC.

### Internet Connection Check

1. Navigate to Q-SYS Core Manager by entering your Q-SYS Coreâs IP address into a web browser. If you do not know your Coreâs IP address, you can obtain it from the Coreâs front panel. Press the Next button until you see the IP address.

   **Note:** If you see a security notice regarding certificates, you can safely proceed to the site. Your computer and the Q-SYS Core processor are not at risk by accessing Core Manager. To avoid these notices in the future, see the [Network > Certificates](../../Core_Manager/Core_Management/Certificates.htm) topic to learn how to install a device certificate.
2. From the left menu, navigate to Core Management > Licensing.
   * If the Licensing Server status shows "Connected", proceed to Online Activation.
   * If the Licensing Server status shows "Disconnected", proceed to Offline Activation.

### Online Activation

If your Q-SYS Core processor can connect to the QSC Licensing Server via the internet, use this method to activate your licenses in just two easy steps!

1. Copy the Entitlement ID (EID) from the QSC Entitlement Information email. In the Core Management > Licensing page, paste the EID into the License String or Entitlement ID field, and then click Activate.
2. Under Available Licenses, select the licenses to activate, and then click Install.

   **Note:** Only licenses included in your Entitlement ID that are applicable to your Q-SYS Core model will be shown. After activating the licenses, one quantity of those licenses will be automatically removed from the Entitlement.

### Offline Activation

If your Q-SYS Core is not connected to the internet, use this method to activate your licenses using an internet-connected PC. Use your Entitlement ID to activate your licenses on the QSC Licensing Portal, and then transfer the licenses to your Q-SYS Core processor.

1. In the QSC Entitlement Information email, copy the Entitlement ID (EID) and sign in to the [QSC Licensing Portal](http://licensing.qsc.com/customerlogin) online.
2. In the Licenses tab, select the licenses to activate, and then click Activate.

   **Note:** The Quantity to Activate for each license type (product) is always 1. You can only activate one license per product at a time.
3. In another browser window, navigate to your Q-SYS Core's IP address and access the Core Management > Licensing page. Copy the Locking ID.
4. Return to the QSC Licensing Portal window. Paste the Locking ID into the Q-SYS Core Locking ID field, and then click Next.
5. Specify the email address that will be associated with this activation and receive the license file. (If your email address is already correct, there is no need to change it.) Then, click Activate.
6. Check your email for a QSC Software License Activated email. It includes the activated license file as an attachment. The license file is a raw text file with the name lservrc\_*your-core-locking-ID*. Save this file to your PC.
7. Return to the Core Management > Licensing page. Select Upload License File, browse to the license file location and select it, and then click Activate.

   **Note:** After activating the licenses, one quantity of those licenses will be automatically removed from the Entitlement.

[Feature License and Scaling License Activation - Reflect](javascript:void(0))

1. Copy the Entitlement ID (EID) from the QSC Entitlement Information email. In the Core Management > Licensing page, paste the EID into the License String or Entitlement ID field, and then click Activate.
2. Under Available Licenses, select the licenses to activate, and then click Install.

   **Note:** Only licenses included in your Entitlement ID that are applicable to your Q-SYS Core model will be shown. After activating the licenses, one quantity of those licenses will be automatically removed from the Entitlement.

[vCore License Activation](javascript:void(0))

**Note:** As the Q-SYS vCore utilizes a Flexible license model, online activation is required. An internet connection is also required to continually validate the license.

1. After you have installed a vCore to a Hypervisor of your choosing, the vCore will appear in Configurator as âvCore Unlicensed.â
2. Click on "vCore Unlicensed" to open Core Manager.
3. Use the left side bar to navigate to the Licensing page.
4. Ensure the License Activation graphic shows all green connections and that License Server: Connected is shown as green. Notice that the Lease is shown as âNot Available.â
5. Copy the Entitlement ID (EID) from the QSC Entitlement Information email. Paste the EID into the Entitlement ID field, and then click Next.
6. Select the available product âQ-SYS - Virtual Coreâ and name your license with a unique License Name for each vCore. Accept the terms of the License Agreement, and then click Activate.

   **Tip:** Make a note of the License Name you specify, as it is tied to the vCore license on the licensing server and can be helpful in cases where the license needs to be located by name â for example, for recovery purposes.
7. If the license activation was successful, you will be prompted with this message and your vCore will reboot.
8. After reboot, the vCore will show as vCore Control with respect to the license that has been activated. You can now upgrade and deploy designs with core model âvCore Controlâ
9. Note the Lease is now shown as âLicense lease is activeâ

## How to Deactivate a vCore License

It is possible to âmoveâ a license to a different VM environment by deactivating the license and reactivating. Simply click the Deactivate License button and wait for your vCore to reboot. This frees up an available activation, which can then be transferred to a different vCore.

## How to Back Up and Restore Licenses

Click Back Up All to save all installed Q-SYS Core licenses to a text file on your device.

In the event that your Core's licenses need to be reinstalled (for example, if one or more licenses is inadvertently deleted):

1. Click Upload License File.
2. Locate the backup text file on your device, and then click Activate.

**Note:** If a backed up license is already installed, you will receive an error that you can safely ignore.

## Licensing FAQ

To learn more about QSC Feature Licensing, including how to activate a Feature License, watch the [Software Feature Licensing](https://training.qsc.com/mod/book/view.php?id=1433) video on the QSC Training website.

[How do I know if I need a Feature License for my design?](javascript:void(0))

As you build your design, Q-SYS Designer 7.0 and above will notify you of any features or components requiring a license:

* The Q-SYS Designer menu bar will show a highlighted Licensed Features menu item, with the total number of detected licensed features indicated. Click Show Me the Features that Need a License to view the Inspector > Licensed Elements section.
* In the left pane, Inspector will show a padlock icon. Click Inspector, and then expand Licensed Elements to see a list of features or components requiring a license. Click a component in the list to highlight in your design schematic.

**Note:** The Design Inspector only indicates what features require a license. It does not illustrate any Feature Licenses that may already be installed on the Q-SYS Core.

[Do I need a Feature License if my Core was manufactured prior to the Q-SYS 7.0 release?](javascript:void(0))

Q-SYS Cores manufactured prior to the introduction of Q-SYS feature licensing (and the release of Q-SYS 7.0) already include licenses for UCI Deployment and the Q-SYS Scripting Engine. Additional licensed features, such as Multi-Track Player expansion or any new feature, may require the purchase of software licenses.

**Note:** It is not possible to downgrade a Q-SYS Core 110f, 110c, 510i, or 510c manufactured with version 7.0 to a previous version.

[Do I need a separate Feature License for a redundant Q-SYS Core?](javascript:void(0))

Yes. A redundant Q-SYS Core installation requires that [Feature Licenses](#Feature_License) are installed on both the Primary and Backup Q-SYS Core processor. However, only one Reflect subscription is necessary for monitoring a redundant system.

[Do I need a separate Reflect subscription for a redundant Q-SYS Core?](javascript:void(0))

No. Only one Reflect subscription is necessary for monitoring a redundant system. However, a redundant Q-SYS Core installation requires that [Feature Licenses](#Feature_License) are installed on both the Primary and Backup Q-SYS Core processor.

[How do I purchase a Feature License?](javascript:void(0))

Contact your QSC reseller to purchase feature licenses. After the purchase is complete, you will receive an email containing an Entitlement ID, which is a record of the license rights (including the specific features and date of activation) to which you are entitled.

[What port does the Q-SYS Core use for online Feature License activation?](javascript:void(0))

The Q-SYS Core uses port 443 when communicating with the QSC Licensing Server via the internet.

[What if I need to transfer a Feature License to another Core?](javascript:void(0))

For transfers of perpetual software licenses, QSC will issue a license key that does not expire and is node-locked to a single Q-SYS Core processor. Once the license is activated, you will only be able to move the license due to a warranty action.

[Is the Core 610 Scaling License required to deploy the 256x256 channel Software Dante License on the Core 610?](javascript:void(0))

No, however be aware that fully utilizing 256x256 Software Dante channels on the Core 610 will consume all available network I/O resources leaving none leftover for Q-LAN, AES67, or System Link.

## Discontinued Licenses

The following licenses are discontinued with QDS v10.0.0 and later.

### Scaling Licenses - Discontinued

Q-SYS Scaling Licenses expand the available resources of certain Q-SYS Core processors to meet specific application needs.

**Note:** Scaling licenses are not additive. For example, both the Collaboration Bundle and Commercial AV Bundle expand the Q-LAN/AES67 network channels from 64x64 to 128x128. Installing both bundles does not expand the capability to 256x256.

[Q-SYS Collaboration Bundle Scaling License](javascript:void(0))

Supported Q-SYS Core processors: Core Nano, Core 8 Flex

This license focuses on expanding resources for meeting spaces, including AEC processing, Softphones, and NM-T1 microphones. It also unlocks more all-purpose DSP processing power and expands the networked audio channel capacity for Q-LAN/AES67 to 128x128.

To learn more, see the [Q-SYS Collaboration Bundle Scaling License](https://www.qsc.com/products-solutions/q-sys/control-licenses/q-sys-collaboration-bundle-scaling-license/) product page on the QSC website.

In version 10.0, this license has been merged with the Q-SYS Commercial AV Bundle Scaling License and is now offered as the Q-SYS Core Nano and Core 8 Flex Scaling License. If you are using a design with a version earlier than 10.0, this license remains available.

|  | Q-SYS Core Nano, Core 8 Flex Base Configuration | Q-SYS Core Nano, Core 8 Flex + Collaboration Bundle Scaling License |
| --- | --- | --- |
| Q-LAN / AES67 network channels | 64 x 64 | 128 x 128 |
| DSP processing power | 1x | Approximately 2x |
| Softphones | 2 | 4 |
| AEC processors @ 200ms | 8 | 16\* |
| NM-T1 microphones | up to 3 | up to 6\* |
| Media / WAN network channels | 12 x 12 | 12 x 12 |
| Q-SYS peripherals | 32 | 32 |

\* NM Series NM-T1 microphones and third-party microphone AEC processing share similar processing resources. When using both in the same Q-SYS design, the maximum number of NM-T1 and third-party AEC microphone channel / capabilities works on a sliding scale. See the  [NM-T1](https://q-syshelp.qsc.com/#Hardware/Audio_IO/NM-T1.htm) topic for details.

[Q-SYS Commercial AV Bundle Scaling License](javascript:void(0))

Supported Q-SYS Core processors: Core Nano, Core 8 Flex

This license focuses on expanding resources for larger BGM and paging applications, including all-purpose DSP processing power, networked audio channel capacity (128x128 channels of Q-LAN/AES67), and Media Stream capacity (up to 24x24). It also increases the maximum Q-SYS peripheral count (up to 48 Q-SYS peripherals).

|  | Q-SYS Core Nano, Core 8 Flex Base Configuration | Q-SYS Core Nano, Core 8 Flex + Commercial AV Bundle Scaling License |
| --- | --- | --- |
| Q-LAN / AES67 network channels | 64 x 64 | 128 x 128 |
| DSP processing power | 1x | Approximately 2x |
| Softphones | 2 | 2 |
| AEC processors @ 200ms | 8 | 8 |
| NM-T1 microphones | up to 3 | up to 3 |
| Media / WAN network channels | 12 x 12 | 24 x 24 |
| Q-SYS peripherals | 32 | 48 |

To learn more, see the [Q-SYS Commercial AV Bundle Scaling License](https://www.qsc.com/products-solutions/q-sys/control-licenses/q-sys-commercial-av-bundle-scaling-license/) product page on the QSC website.

In version 10.0, this license has been merged with the Q-SYS Collaboration Bundle Scaling License and is now offered as the Q-SYS Core Nano and Core 8 Flex Scaling License. If you are using a design with a version earlier than 10.0, this license remains available.

[Q-SYS Core Nano and Core 8 Flex Scaling License](javascript:void(0))

Supported Q-SYS Core processors: Core Nano, Core 8 Flex

This license focuses on combining the Q-SYS Collaboration Bundle Scaling License and the Q-SYS Commercial AV Bundle Scaling License, including all-purpose DSP processing power, networked audio channel capacity (128x128 channels of Q-LAN/AES67), and Media Stream capacity (up to 24x24). It also increases the maximum Q-SYS peripheral count (up to 48 Q-SYS peripherals).

|  | Q-SYS Core Nano, Core 8 Flex Base Configuration | Q-SYS Core Nano, Core 8 Flex + Capacity Scaling License |
| --- | --- | --- |
| Q-LAN / AES67 network channels | 64 x 64 | 128 x 128 |
| DSP processing power | 1x | 2x |
| Softphones | 2 | **4** |
| AEC processors @ 200ms | 8 | **16** |
| NM-T1 microphones | up to 3 | **up to 6** |
| Media / WAN network channels | 12 x 12 | 24 x 24 |
| Q-SYS peripherals | 32 | 48 |

#### Requirements

Core Nano, Core 8 Flex: Requires QDS version 10.0 and later.

#### Notes

* Q-SYS Collaboration Bundle Scaling License and the Q-SYS Commercial AV Bundle Scaling License can still be used if a system already has them and upgrades to version 10.0 if an entitlement already purchased has unused licenses remaining.
* If the Q-SYS Capacity Scaling License is installed on a Core already having the Q-SYS Collaboration Bundle Scaling License and the Q-SYS Commercial AV Bundle Scaling License, the greater capacities of the Q-SYS Capacity Scaling License will be utilized.
* Q-SYS Collaboration Bundle Scaling License and the Q-SYS Commercial AV Bundle Scaling License will be available for sale to use with older software versions until a new LTS version is released.

[Q-SYS Core 6000 CXR Scaling License](javascript:void(0))

Supported Q-SYS Core processors: Core 6000 CXR

This license expands the network audio, DSP processing, AEC processing, and media/WAN channel capacities to suit larger BGM and paging applications.

|  | Q-SYS Core 6000 CXR Base Configuration | Base Configuration + Q-SYS Core 6000 CXR Scaling License |
| --- | --- | --- |
| Q-LAN / AES67 network channels | 256 x 256 | 512 x 512 |
| DSP processing power (relative to Q-SYS Core Nano) | 20x | 40x |
| Softphones | 64 | 64 |
| AEC processors @ 200ms | 80 | 160 |
| Media / WAN network channels | 128 x 128 | 256 x 256 |

To learn how to activate a Scaling License, see [How to Activate a License](#How_to_Activate).

This license will be discontinued when the hardware discontinues.

[Q-SYS Core 610 Scaling License](javascript:void(0))

Supported Q-SYS Core processors: Core 610

This license expands the network audio, DSP processing, AEC processing, and media/WAN channel capacities to suit larger BGM and paging applications.

**Note:** For Core 610, the stream count does not increase with the 384 x 384 capacity scaling license; channels can become 384 x 384, but streams remain 256 x 256.

|  | Q-SYS Core 610 Base Configuration | Base Configuration + Q-SYS Core 610 Scaling License |
| --- | --- | --- |
| Q-LAN / AES67 network channels | 256 x 256 | 384 x 384 |
| DSP processing power (relative to Q-SYS Core Nano) | 16x | 24x |
| Softphones | 64 | 64 |
| AEC processors @ 200ms | 64 | 96 |
| Media / WAN network channels | 64 x 64 | 96 x 96 |

To learn how to activate a Scaling License, see [How to Activate a License](#How_to_Activate).

This license will be discontinued when the hardware discontinues.

### Integration Licenses - Discontinued

[Microsoft Teams Rooms UC Integration License](javascript:void(0))

The Q-SYS UC Integration License for Microsoft Teams Rooms (MTR) is designed to streamline integration of Q-SYS with Microsoft Teams Rooms. Unlike other licenses that must be purchased for specific Core models, this single license may be applied to any Q-SYS Core processor to enable a subset of Q-SYS control functionality aimed at the needs of a single room collaboration system. The enabled functionality includes:

* Support for up to 4 active UCIs
* Support for up to 8 plugins / scripts
* Enables the 2nd Page Experience (Q-SYS room controls on certified Microsoft Teams Rooms controllers) for Microsoft Teams Rooms systems
* Supports the ability to âstackâ or combine multiple instances of this license.
  + Ex. A Divisible room system with multiple MTR compute devices that exceeds the number of UCIs / scripts supported in a single license. In this system, multiple instances of the license combined to enable the additional control capabilities needed to support the system requirements.

**Note:**  A separate license is not required for Teams Rooms integration if both the Scripting Engine and UCI Deployment licenses are already active on the Core.

### Feature Licenses - Discontinued

Feature Licenses utilize Nodelock model licensing, which allows both online and offline activation.

These features require activating a license when included in a design deployed to a Q-SYS Core processor manufactured with firmware version 7.0 and above. Licensed features can always be run in Emulate Mode.

[Microsoft Teams Rooms](javascript:void(0))

The Q-SYS Software Feature License for Microsoft Teams Rooms is available for the Core Nano, Core 8 Flex, NV-32-H (Core Capable), Core 110f, Core 510i, and Core 610. It includes:

* Q-SYS Scripting Engine license
* Q-SYS UCI Deployment license

**Note:**  A separate license is not required for Teams Rooms integration if both the Scripting Engine and UCI Deployment licenses are already active on the Core.

[Scripting Engine](javascript:void(0))

The Q-SYS Scripting Engine feature license is required when deploying the following components to a Core Nano, Core 8 Flex, NV-32-H (Core Capable), Core 110f, Core 110c, Core 510i, Core 510c, and Core 610:

* Block Controller
* Text Controller
* Control Script
* Scriptable Controls
* Plugins

[UCI Deployment](javascript:void(0))

The User Control Interface (UCI) Deployment license is no longer required when deploying a design that contains a UCI to a Core. Users will now have the ability to generate an EID containing a free UCI Deployment and Scripting Engine license if they need to use a version earlier than v10.0.
