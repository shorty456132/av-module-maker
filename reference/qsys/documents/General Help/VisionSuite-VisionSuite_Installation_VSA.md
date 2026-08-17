# VisionSuite Patch Installation/Upgrade (VSA-100)

> Source: https://help.qsys.com/Content/VisionSuite/VisionSuite_Installation_VSA.htm

# VisionSuite Patch Installation/Upgrade (VSA-100)

Read this topic to understand how to install or upgrade VisionSuite on a VSA-100 VisionSuite AI Accelerator.

[Requirements](javascript:void(0))

* Core running Q-SYS Designer firmware 10.0 or newer
* VSA-100 running Q-SYS firmware 10.0 or newer

[Procedure](javascript:void(0))

#### Patching VSA-100

1. Download the patch software from:

   <https://www.qsys.com/products/q-sys/video/q-sys-visionsuite/visionsuite-updates/>
2. Go to Q-SYS Patch Manager in your browser - <Core\_IP>/patch/vsa\_patch>
3. Any connected VisionSuite devices on the same network will be listed.
4. Click Local Patch.
5. Choose the downloaded patch file.
6. Click Install.
7. Click Install on all devices when prompted. Device will reboot and clear any current patches, then start installation. Status will be shown in Q-SYS Designer.

After installation, the VSA-100 will reboot again to complete the process.

#### Firmware Update

The VSA-100 follows the same firmware update procedure as Q-SYS Cores and peripherals. Please refer to [Installing and Updating Q-SYS Software and Firmware](../Q-SYS_Designer/0015_Installing_Q-SYS.htm) for the necessary steps.

**Note:** The VSA-100 requires Q-SYS Designer Software v10.0 or newer for proper functionality.

[Licensing](javascript:void(0)) 

VisionSuite on an AI Accelerator requires two licenses to start: a perpetual feature license and a term-limited update license. After the update license expires, the system continues to function but VisionSuite can no longer be updated. See the [Licensing](../Core_Manager/Core_Management/Licensing.htm) topic for more information about Q-SYS licenses.
