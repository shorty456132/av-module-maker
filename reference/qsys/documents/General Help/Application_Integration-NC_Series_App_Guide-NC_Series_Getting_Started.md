# Getting Started

> Source: https://help.qsys.com/Content/Application_Integration/NC_Series_App_Guide/NC_Series_Getting_Started.htm

# Getting Started

Now that you're familiar with the NC Series cameras, you're ready to get one installed and integrated with your Q-SYS system.

[1. Install the camera](javascript:void(0))

Use the NC Series Hardware User Manual, available from the [NC Series product page](http://www.qsys.com/ncseries) on the QSC website, to mount and connect the camera.

[2. Add the camera to your design](javascript:void(0))

* Using Q-SYS Designer Software, add an NC Series camera model to your design from the Inventory > Video tab. Repeat for any additional cameras you have.
* Drag the camera's Status/Control component into your design.

[3. Configure the camera's network settings and password](javascript:void(0))

Use Q-SYS [Configurator](../../Hardware/0017_Configurator.htm) (Tools > Show Configurator) to find and select the discovered NC camera in the list. From there, click Open Peripheral Manager. Use Q-SYS [Peripheral Manager](../../Peripheral_Manager/PeripheralManager_Overview.htm) to configure the camera's hostname, IP address, 802.1X settings, device certificates, and password.

[4. Set the camera's design properties](javascript:void(0))

Select the camera's Status/Control component in your design, and then configure the camera's Properties, including its name in the design and IP streaming setting. To learn about these properties, see the [Status/Control (Cameras)](../../Schematic_Library/onvif_camera.htm) topic.

[5. Add a Video Bridge](javascript:void(0))

The Video Bridge component serves as the software link between the Q-SYS device that supports USB bridging and the host PC. Refer to the [USB Video Bridge](../../Schematic_Library/usb_uvc.htm) topic to see what Q-SYS devices support USB bridging.

* For Q-SYS Core processors, select the Core in your Inventory list and then toggle the USB Video Bridge property to 'Enabled'.
* For Q-SYS peripherals, add the peripheral to your Inventory first, and then set its USB Video Bridge property to 'Enabled'.
* Drag the Video Bridge peripheral from the device's Inventory tree into your design.

[6. Wire the camera](javascript:void(0))

You can wire the camera's Status/Control component directly to the Video Bridge component or, in cases where you want to connect multiple cameras to multiple video bridges, you can use the Mediacast Router. Refer to the [USB Video Bridge](../../Schematic_Library/usb_uvc.htm) and [Mediacast Router](../../Schematic_Library/video_router.htm) topics to learn more.

[7. Run the design and adjust camera controls](javascript:void(0))

Press F5 to save the design to the Core and run it. Double-click the camera's Status/Control component to open the control panel, and then adjust the camera's controls as desired. Refer to the [Status/Control (Cameras)](../../Schematic_Library/onvif_camera_operative.htm) topic for control information.
