# Utilities

> Source: https://help.qsys.com/Content/Peripheral_Manager/Utilities.htm

# Utilities

Download the Q-SYS log file (when requested by Q-SYS Support), change the NV-32-H (Core Capable) and Q-SYS Core 510i processor configuration mode, and reboot the Q-SYS Core processor.

## Log Archive

In the event of a support request, Q-SYS Support may require a copy of the Q-SYS log for troubleshooting purposes.

Click Download to save a copy of the Q-SYS log (.qsyslog) to your PC. The filename includes the Q-SYS peripheral name, as well as a UTC date and time stamp.

**Note:** Q-SYS Support uses a special log viewer application to interpret the log and obtain key information about the health of your Q-SYS system, including Core status, design information, peripheral status, streaming issues, Q-SYS Feature Licensing information, and network information.

## Mode

Available only for the Core 110f, Core 8 Flex, Core Nano, NV-32-H (Core Capable) and Core 510i. Select a configuration mode:

#### Core

The device is deployed as a Q-SYS Core processor, with full processing capabilities for audio, video, and control. Click Switch to update the mode and reboot the device.

**Note:** Once the device reboots, you must save and run a design to the Core before configuring it using Q-SYS Core Manager or upgrading its firmware.

#### Peripheral

The device is deployed as a Peripheral. Click Switch to update the mode and reboot the device. In this mode, add the device from the Inventory menu in your design, and configure a separate Q-SYS Core for processing. Once the device reboots, you can then configure it using Peripheral Manager.

## Reboot

Click to reboot the Q-SYS peripheral. A reboot cycle typically takes a few minutes. During a reboot, the device goes offline and temporarily shows as 'Missing' in the running design.
