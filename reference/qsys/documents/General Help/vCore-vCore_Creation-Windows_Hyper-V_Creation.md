# How to Create a Windows Hyper-V vCore

> Source: https://help.qsys.com/Content/vCore/vCore_Creation/Windows_Hyper-V_Creation.htm

# How to Create a Windows Hyper-V vCore

Read this topic to understand how to install the vCore image on a Windows hypervisor.

[Prerequisites](javascript:void(0))

* Like most virtual machines, an image file is required for setup. Download the virtual hard disk image file from the Q-SYS website [vCore product page](https://www.qsys.com/products-solutions/q-sys/processing/vcore-virtualized-processor/).
* To create a vCore in Windows, you must first start Hyper-V Manager. If Hyper-V is not enabled, see the [Install Hyper-V](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v) topic at learn.microsoft.com.

**Note:** See [vCore Requirements](../vCore_Requirements.htm) for supported Windows operating systems.

[Hyper-V Setup](javascript:void(0))

[Create a new Virtual Network Switch](javascript:void(0))

Before creating the vCore, you must first create a new Virtual Network Switch to allow vCore(s) to connect to the Physical Ethernet Network.

1. In the Actions pane, select Virtual Switch Manager....
2. Under Global Network Settings, select MAC Address Range.
3. Make a note of the six least significant MAC address hex digits that will be used in the default vCore name.
4. Under Virtual Switches, click New virtual network switch.
5. Set the virtual switch type to External.
6. Click Create Virtual Switch.
7. Name the new virtual switch â for example, âQ-SYS Switchâ.
8. Set Connection type to External network and, if the PC has multiple NICs, the desired NIC.
9. Click OK.

[Create a vew Virtual Machine containing the vCore â Supported Windows operating systems except Windows Server 2019](javascript:void(0))

1. In the Actions pane, select Quick Createâ¦.
2. Select Local installation source.
3. Click Change installation source... .
4. Select the downloaded image file.
5. Uncheck the This virtual machine will run Windows checkbox.
6. Expand More options.
7. Under Name, enter a unique name, for example âQ-SYS vCore Control 1â

   **Note:** This is the Virtual Machine name, not the vCore name.
8. Under Network, select the previously created external virtual network switch (âQ-SYS Switchâ).
9. Click Create Virtual Machine (this may take a few seconds).
10. Click Edit settingsâ¦.
11. Under Hardware, select Processor and reduce the Number of virtual processors to 1.
12. Under Hardware, select Memory and uncheck the Enable Dynamic Memory checkbox.
13. Under Management, select Checkpoints and uncheck the Enable checkpoints checkbox.
14. Click OK.
15. Close the Create Virtual Machine window.

    **Note:** Do not Connect!
16. In the Virtual Machines pane, right-click the new virtual machine and select Start.
17. Monitor Uptime and wait for about a minute until the virtual machine reboots.
18. Wait for another minute or so to let the initial partial firmware installation complete.
19. Use Q-SYS Configurator (within Q-SYS Designer Software) to locate the vCore with a default name based on its six least significant MAC address hex digits.

    **Note:** Optionally use Q-SYS Core Manager to change the vCore name.
20. Activate the vCore license. Refer to the instructions in the [Licensing](../../Core_Manager/Core_Management/Licensing.htm) topic.
21. Use Q-SYS Designer Software to deploy a design to the vCore. This will also install the full Q-SYS firmware.
22. Optionally, shut down the virtual Core by right-clicking the virtual machine and selecting Shut Downâ¦.

    **CAUTION:** Do not use Turn Offâ¦, as this is equivalent to pulling the power on a physical Core and may result in data loss.

[Create a new Virtual Machine containing the vCore â Windows Server 2019](javascript:void(0))

The procedure for Windows Server 2019 contains some additional steps to get the vCore running.

1. Before beginning, make a copy of the Windows image file (`qsys_vcore_windows_hyperv_<qsys_version>.vhdx`) and place it in `C:\Users\Public\Documents\Hyper-V\Virtual hard disks` (or a location on the server you wish to store vCore images).
2. In the Actions pane, select New > Virtual Machine â¦
3. Click Next on Before you Begin.
4. Under Name, enter a unique name, for example âQ-SYS vCore Control 1â (this is the Virtual Machine name, not the vCore name) and click Next.
5. Select "Generation 2" on Specify Generation and click Next.
6. Under Startup memory, specify 2048Mb and make sure Use Dynamic Memory for this virtual machine is unchecked. Click Next.
7. On Connection select the virtual switch or network adapter you wish for the vCore to connect and click Next.
8. Select Use an existing virtual hard disk and click Browse to select the copy of the vhdx from Step 1. Click on Next.
9. Select Finish to create the virtual machine.
10. Right-click on the virtual machine in Virtual Machines and click on Settings
11. Under Security, disable Enable Secure Boot.
12. Under Processor, set the Number of virtual processors to 1.
13. Under Checkpoints, disable Enable Checkpoints.
14. Click Apply and Ok to close Settings.
15. In the Virtual Machines pane, right-click the new virtual machine and select Start.

    **Note:** Do not Connect!
16. Monitor Uptime and wait for about a minute until the virtual machine reboots.
17. Wait for another minute or so to let the initial partial firmware installation complete.
18. Use Q-SYS Configurator to locate the vCore with a default name based on its six least significant MAC address hex digits.

    **Note:** Optionally use Q-SYS Core Manager to change the vCore name.
19. Activate the vCore license. Refer to the instructions in the [Licensing](../../Core_Manager/Core_Management/Licensing.htm) topic.
20. Use Q-SYS Designer Software to deploy a design to the vCore. This will also install the full Q-SYS firmware.
21. Optionally, shut down the virtual Core by right-clicking the virtual machine and select Shut Downâ¦

    **CAUTION:** Do not use Turn Offâ¦, as this is equivalent to pulling the power on a physical Core and may result in data loss.
