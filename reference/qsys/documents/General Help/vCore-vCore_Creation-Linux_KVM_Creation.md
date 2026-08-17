# How to Create a Linux KVM vCore

> Source: https://help.qsys.com/Content/vCore/vCore_Creation/Linux_KVM_Creation.htm

# How to Create a Linux KVM vCore

Read this topic to understand how to install the vCore image on a Linux hypervisor.

[Prerequisites](javascript:void(0))

* Like most virtual machines, an image file is required for setup. Download the virtual hard disk image file from the Q-SYS website [vCore product page](https://www.qsys.com/products-solutions/q-sys/processing/vcore-virtualized-processor/).
* To create a vCore in Linux, you must first start Virtual Machine Manager. If Virtual Machine Manager is not enabled, see [Install KVM on Ubuntu 20.04 {+ Create a Virtual Machine}](https://phoenixnap.com/kb/ubuntu-install-kvm).

[Virtual Machine Manager Setup](javascript:void(0))

To create a new virtual machine containing the vCore:

1. Create a unique Virtual Machine name (without spaces), for example Q-SYS\_vCore\_Control\_1.

   **Note:** This is the Virtual Machine name, not the vCore name.
2. As root, copy (while renaming) the vCore image file to `/var/lib/libvirt/images/`:

   `sudo cp qsys_vcore_linux_kvm_<qsys_version>.qcow2 /var/lib/libvirt/images/<new_VM_name>.qcow2`
3. Start Virtual Machine Manager.
4. Select File and New Virtual Machine.
5. Select Import existing disk image.
6. Select Browse... in order to provide the existing disk image storage path.
7. From the default Storage Volume, select <new\_VM\_name>.qcow2 and click Choose Volume.
8. Select Generic default as the operating system you are installing and click Forward.
9. Set Memory to 2048MB and click Forward.
10. Under Name, enter the previously created Virtual Machine name.
11. Check Customize configuration before install and click Finish.
12. Under Overview, set Firmware to UEFI and click Apply.
13. Under NIC:
    * Set Device model to virtio and click Apply.
    * Set Network Source such that the Virtual Machine is able to access your physical network. (This [article](https://computingforgeeks.com/how-to-create-and-configure-bridge-networking-for-kvm-in-linux/) may be of assistance.)
14. Under IDE Disk 1, open Advanced options, set Disk bus to VirtIO and click Apply.
15. In the upper left corner, select Begin installation.
16. Once the virtual Core starts in a new console window, wait for about a minute until the virtual machine reboots.
17. Wait for another minute or so to let the initial partial firmware installation complete.
18. Use Q-SYS Configurator (within Q-SYS Designer Software) to locate the vCore with a default name based on its six least significant MAC address hex digits.

    **Note:** Optionally use Q-SYS Core Manager to change the vCore name.
19. Activate the vCore license. Refer to the instructions in the [Licensing](../../Core_Manager/Core_Management/Licensing.htm) topic.
20. Use Q-SYS Designer Software to deploy a design to the vCore. This will also install the full Q-SYS firmware.
21. Optionally, turn off the virtual Core by right-clicking the virtual machine in Virtual Machine Manager and selecting Shut Down | Force Off.

    **Note:** Support for a more graceful Shutdown will be added in the future.
