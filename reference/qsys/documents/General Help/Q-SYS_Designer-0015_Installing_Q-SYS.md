# Installing and Updating Q-SYS Software and Firmware

> Source: https://help.qsys.com/Content/Q-SYS_Designer/0015_Installing_Q-SYS.htm

# Installing and Updating Q-SYS Software and Firmware

Q-SYS consists of multiple pieces of hardware running Q-SYS firmware and a Q-SYS design file (on the Core). The design file is created and maintained by Q-SYS Designer software installed on a PC. When creating or maintaining a design file, Q-SYS Designer on the PC and the Q-SYS firmware on the system's hardware must be the same release version.

If you attempt to save and run a design file to a Core and a mismatch of software and firmware is detected, you are given the opportunity to update the hardware to the firmware associated with the Q-SYS Designer software running on your PC. If you choose to update the firmware, all of the Q-SYS hardware identified in the design receives the firmware update automatically. This design feature of Q-SYS ensures that all of the hardware pieces are quickly and easily kept synchronized with the same firmware version without having to individually update each piece.

**Note:** Anti-virus software can impact some Q-SYS Designer Software operations.

[Installing Q-SYS Designer](javascript:void(0))

To install Q-SYS Designer on your PC, download the latest installation files from the [QSC website](https://www.qsys.com/resources/software-and-firmware/). Follow the instructions provided in the installation program.

[Installing Multiple Copies of Q-SYS Designer on a Single PC](javascript:void(0))

To install multiple copies, or versions, of Q-SYS Designer on your PC:

1. After the first release version of Q-SYS Designer is installed, rename the following folder:

C:\Program Files\QSC\Q-SYS Designer

(This is the default installation folder.)

2. Install the second copy of Q-SYS Designer. You can use the default location or specify a new location.

**Note:** The installation program uninstalls any copy of Q-SYS Designer in a subdirectory defined during the installation process. Simply selecting different installation directories during the installation process will not allow you to install multiple copies.

[Installing Older Versions Q-SYS Designer Software](javascript:void(0))

At times you may have to work on a design file that was created in an older version of Q-SYS Designer. You may not want to update the design file to the latest version of Q-SYS Designer. To open the design file without updating the file's software version, you need to install an older version of Q-SYS Designer on your PC. There are two ways to accomplish this:

* Overwrite the version of Q-SYS Designer currently on your PC, or
* Install multiple versions of Q-SYS Designer on your PC. Refer to [Installing Multiple Copies of Q-SYS Designer on a Single PC](#Installing_Multiple_Copies).

[Updating Q-SYS Designer](javascript:void(0))

Periodically, a new version of Q-SYS Designer is released. The design files you have created using earlier versions of Q-SYS Designer can be opened with newer versions of Q-SYS Designer. However, some of the components may have changes or new features added that cause your designs to act somewhat differently than originally designed.

Designs you create with a newer version and then open in an older version of Q-SYS Designer are likely be incompatible with the older version of software. It is recommended that you use the same version of software as the design, or a newer version.

**CAUTION:** Check the [Release Notes](../Release_Notes.htm) for any important notices concerning upgrading.

[Updating Core Firmware](javascript:void(0))

When you install a new version of Q-SYS Designer software on your PC and then select File > Save to Core & Run, Q-SYS Designer detects whether the Core's firmware is older than the Designer version and alerts you that the hardware needs to be updated. Clicking Update automatically:

1. Updates the Primary Core and reboots.
2. Updates the Backup Core (if present) and reboots.
3. Updates all peripherals in the design, in parallel, and reboots.

**Note:** Updating firmware takes a while to complete, especially on large systems. During this time, the system cannot be used. Therefore, it is a good idea to plan this operation when the system is not being used or is at its lowest traffic point.

[Backups](javascript:void(0))

Although the Q-SYS firmware and design file are saved on the Core, it is good practice to archive the final version of the design in a safe place in case the Core is destroyed. You may also want to give a backup copy to the venue management.

**Tip:** Enable the File Recovery Save option in File > Preferences to configure auto-saving of design files with unsaved changes. To learn more, see [Preferences](../Schematic_Library/preferences.htm).
