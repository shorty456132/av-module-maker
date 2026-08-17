# Utilities

> Source: https://help.qsys.com/Content/Core_Manager/Core_Management/Utilities.htm

# Utilities

Download the Q-SYS log file (when requested by Q-SYS Support), change the NV-32-H (Core Capable) and Q-SYS Core 510i processor configuration mode, and reboot the Q-SYS Core processor.

## System Information

In the event of a support request, Q-SYS Support may require a copy of the Q-SYS log for troubleshooting purposes.

Click Download to save a copy of the Q-SYS log (.qsyslog) to your PC. The filename includes the Q-SYS Core name, as well as a UTC date and time stamp.

**Note:** Q-SYS Support uses a special log viewer application to interpret the log and obtain key information about the health of your Q-SYS system, including Core status, design information, peripheral status, streaming issues, Q-SYS Feature Licensing information, and network information.

## Mode

Available only for the Core 110f, Core 8 Flex, Core Nano, NV-32-H (Core Capable) and Core 510i. Select a configuration mode:

#### Core

The device is deployed as a Q-SYS Core processor, with full processing capabilities for audio, video, and control. Click Switch to update the mode and reboot the device.

**Note:** Once the device reboots, you must save and run a design to the Core before configuring it using Q-SYS Core Manager or upgrading its firmware.

#### Peripheral

The device is deployed as a Peripheral. Click Switch to update the mode and reboot the device. In this mode, add the device from the Inventory menu in your design, and then configure a separate Q-SYS Core for processing. Once the device reboots, you can then configure it using Peripheral Manager, which is accessible from Configurator in Q-SYS Designer Software (Tools > Show Configurator).

**Note:** Switching to Peripheral Mode turns off LAN B and clears its settings. Use Peripheral Manager to configure the device's network settings.

## QSD Authentication

Toggle On or Off the preference to allow downgrade to earlier versions. It is disabled by default and is not persistent.

## Core Reboot

Click Reboot to stop the running design and reboot the Q-SYS Core processor. A reboot cycle typically takes a few minutes.

## Firmware Patches

Within Q-SYS Reflect, you can apply patches to both firmware and software.

**Note:** You must be an Administrator to Install or Remove Firmware Patches.

### Installing and Applying a Patch

Once a Firmware Patch is available, information on version, release date, and further details will appear. It will say "No patches for firmware version" if there are no patches available for download.

1. When ready, click **Install**.
2. It will confirm that the patch installation has started and alert other actions will not be available. When prompted, click on **Install**.
3. A progress bar will appear as the patch installs.
4. Once it is finished, the Core will reboot automatically and apply the patch.

### Removing a Patch

Installed Firmware Patches are easily removed.

1. When ready, click **Remove**.
2. It will confirm that the patch installation has started and alert other actions will not be available. When prompted, click on **Remove**.
3. When finished, the Core will reboot automatically without the patch.

### Updating a Patch

When a new version of the Installed Patch is available, it will show in the available Firmware Patches section. You will see a message that indicates the older version must be removed prior to the newer version being installed. See the steps for [Removing a Patch](#Removing)
