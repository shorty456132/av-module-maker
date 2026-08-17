# How to Create a VMware ESXi vCore

> Source: https://help.qsys.com/Content/vCore/vCore_Creation/VMware_ESXi_Creation.htm

# How to Create a VMware ESXi vCore

Read this topic to understand how to install the vCore image on a VMware ESXi hypervisor.

[Prerequisites](javascript:void(0))

* Like most virtual machines, an image file is required for setup. Download the virtual hard disk image file from the Q-SYS website [vCore product page](https://www.qsys.com/products-solutions/q-sys/processing/vcore-virtualized-processor/).
* To create a vCore in VMware ESXI, open vSphere Web Client in a browser and upload the virtual disk image file to the ESXi server Storage device.

[ESXi Setup](javascript:void(0))

To create a new virtual machine containing the vCore:

1. In the Navigator pane, select Virtual Machines and click Create / Register VM in the Virtual Machines window.
2. In the New virtual machine window, select Create a new virtual machine and click Next.
3. Enter a Virtual Machine name, for example Q-SYS vCore Control 1.

   **Note:** This is the Virtual Machine name, not the vCore name
4. Set the Guest OS family to Other, the Guest OS version to Other (64-bit) and click Next.
5. Select storage for the virtual machine and click Next.
6. Remove the following Virtual Hardware items: Hard Disk, CD/DVD Drive, USB Controller and SATA Controller.
7. Set the amount of Memory to 2048MB.
8. Set the SCSI Controller to VMware Paravirtual.
9. Set the Network Adapter to VM Network.
10. Expand the Network Adapter settings and set the Adapter Type to VMXNET3.
11. Select the VM Options tab, expand Boot Options, set Firmware to EFI and click Next.
12. Review settings and click Finish.
13. Start the SSH service under Host | Manage | Services | TSM-SSH and ssh into the ESXi server.
14. Import the vCore image file by executing the following command:

    `vmkfstools -i <virtual_disk_image_file_folder>/qsys_vcore_vmware_esxi_<qsys_version>.vmdk <virtual_machine_folder>/qsys.vmdk`
15. In the Navigator pane, select Virtual Machines and click the previously created vCore Control virtual machine.
16. Select Edit, Add hard disk and Existing hard disk.
17. Open the folder associated with the previously created vCore Control virtual machine, select the qsys.vmdk file, click Select and Save.
18. To start the vCore, click the Play icon on the virtual machine console.
19. Once the virtual Core starts in a new console window, wait for about a minute until the virtual machine reboots.
20. Wait for another minute or so to let the initial partial firmware installation complete.
21. Use Q-SYS Configurator (within Q-SYS Designer Software) to locate the vCore with a default name based on its six least significant MAC address hex digits.

    **Note:** Optionally use Q-SYS Core Manager to change the vCore name.
22. Activate the vCore license. Refer to the instructions in the [Licensing](../../Core_Manager/Core_Management/Licensing.htm) topic.
23. Use Q-SYS Designer Software to deploy a design to the vCore. This will also install the full Q-SYS firmware.
