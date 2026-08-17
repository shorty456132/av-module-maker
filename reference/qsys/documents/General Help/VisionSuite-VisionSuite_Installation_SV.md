# VisionSuite Installation/Upgrade (Legacy SV)

> Source: https://help.qsys.com/Content/VisionSuite/VisionSuite_Installation_SV.htm

# VisionSuite Installation/Upgrade (Legacy SV)

Read this topic to understand how to install or upgrade VisionSuite on legacy SV (SVS1 or SVS4) VisionSuite AI Accelerator hardware.

[Requirements](javascript:void(0))

**Note:** If the currently installed VisionSuite version is below v81, contact Q-SYS Support for assistance with upgrading to the latest VisionSuite version and recommended firmware.

Before starting the installation/upgrade, the following are needed:

* See the [VisionSuite Release Notes](VisionSuite_Release_Notes.htm) to review improvements, resolved issues, and QDS and firmware recommendations for the latest release.
* VisionSuite software patch download. Check current releases on the [VisionSuite Updates](https://www.qsys.com/products/q-sys/video/q-sys-visionsuite/visionsuite-updates/) page.
* IP address of the VisionSuite AI Accelerator (SVs). If you do not know the AI Accelerator IP, follow the AI Accelerator IP Discovery steps below.
* The VisionSuite offline upgrade application must be running on http://<accelerator-ip>:3030
  + Check with your browser.
  + Verify that the VisionSuite AI Accelerator (SVs) is running.

[AI Accelerator IP Discovery](javascript:void(0))

VisionSuite AI Accelerators are provisioned with DHCP enabled by default. Discover your AI Accelerator's IP address using mDNS.

1. Connect the server to a network with a DHCP server.
2. Open Q-SYS Designer Software (QDS) on a PC connected to your server's network and add a new Seervision plugin to the schematic.
3. Navigate to File > Emulate. Open the Seervision plugin and click the Discover Servers button on the Setup page. Observe the list of server hostnames in any of the Discovered Servers dropdowns and select a server to identify its IP address.

[Procedure](javascript:void(0))

1. Access the VisionSuite offline upgrade application at http://<accelerator-ip>:3030.
2. Click **Choose File** in the upgrade app, choose the VisionSuite software patch from your laptop, and click on **Upload**.
3. Wait until the patch appears. It will calculate the checksum and then upload the file. Depending on your connection speed, it can take 10-20 minutes.
4. Select the patch you wish to install by clicking on it and clicking **Start Upgrade**.
5. During the upgrade, the machine will reboot several times and perform many tests and validations. You can follow progress on the monitor and in the offline upgrade browser window.

   Followed by (see below). Be patient, as you might see several boot cycles.â
6. Once the following message is displayed, the upgrade has been completed successfully. This can take approx. 20 minutes. Click **Acknowledge** to return to the main page of the upgrade application.
7. After pressing Acknowledge, the log files of the upgrade process will be available for download if necessary.
8. Open the Suite UI via http://<accelerator-ip> to check whether the VisionSuite is running.

[Licensing](javascript:void(0)) 

Please contact Q-SYS Support for assistance with VisionSuite licensing.
