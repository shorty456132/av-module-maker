# Getting Started

> Source: https://help.qsys.com/Content/Application_Integration/NV_Series_Endpoint_Application/NV_Series_Endpoint_Getting_Started.htm

# Getting Started

Now that you're familiar with the NV Series endpoints, you're ready to get one installed and integrated with your Q-SYS system.

[1. Install the NV Series Endpoints](javascript:void(0))

Use the NV Series Video Endpoints User Manual, available from the [NV Series product page](https://www.qsys.com/products-solutions/q-sys/video/nv-series/) on the QSC website, to mount and connect the NV Series Endpoints.

[2. Add the NV Series to your design](javascript:void(0))

* Using Q-SYS Designer Software, add an NV Series endpoint model to your design from the Inventory > Video tab. Repeat for any additional endpoints you have.
* Drag the endpoint's Status/Control component into your design.

[3. Configure the endpoint's network settings and password](javascript:void(0))

Use Q-SYS [Configurator](../../Hardware/0017_Configurator.htm) (Tools > Show Configurator) to find and select the discovered NV endpoint in the list. From there, click Open Peripheral Manager. Use Q-SYS [Peripheral Manager](../../Peripheral_Manager/PeripheralManager_Overview.htm) to configure the endpoint's hostname, IP address, 802.1X settings, device certificates, and password.

[4. Set the endpoint's design properties](javascript:void(0))

Select the endpoint's Status/Control component in your design, and then configure the endpoint's Properties, including its name in the design and IP streaming setting. To learn about these properties, see the [Status (NV-32-H)](../../Schematic_Library/vstreamer_status.htm), or [Status (NV-21-HU)](../../Schematic_Library/vstreamer_nv1smb_status.htm), or [Status (NV-1-H-WE)](../../Schematic_Library/vstreamer_nv1wp_status.htm) topics.

[5. Add Additional Video Components](javascript:void(0))

* The HDMI or AV I/O Encoder or Decoder component serves as the configuration of video and audio routing in Q-SYS. Refer to the [HDMI I/O (NV-32-H)](../../Schematic_Library/streamer_hdmi_switcher.htm), or [AV I/O (NV-21-HU)](../../Schematic_Library/av_io.htm) or [AV I/O (NV-1-H-WE)](../../Schematic_Library/vstreamer_nv1wp_av_io.htm) topics to see what Q-SYS devices support I/O Encoding and Decoding
  + For Q-SYS peripherals, add the peripheral to your Inventory first, and then drag the HDMI I/O Encoder peripheral from the device's Inventory tree into your design.
  + Set its Device Type property to 'Encoder' or 'Decoder'.
* The Video Bridge component serves as the software link between the Q-SYS device that supports USB bridging and the host PC. Refer to the [USB Video Bridge](../../Schematic_Library/usb_uvc.htm) topic to see what Q-SYS devices support USB bridging.
  + For Q-SYS Core processors, select the Core in your Inventory list and then toggle the USB Video Bridge property to 'Enabled'.
  + For Q-SYS peripherals, add the peripheral to your Inventory first, and then set its USB Video Bridge property to 'Enabled'.
  + Drag the Video Bridge peripheral from the device's Inventory tree into your design.

[6. Wire the endpoint](javascript:void(0))

You can wire the endpoint's components directly to other Video components, in cases where you want to connect multiple endpoints to multiple video bridges, you can use the Mediacast Router. Refer to the [USB Video Bridge](../../Schematic_Library/usb_uvc.htm) and [Mediacast Router](../../Schematic_Library/video_router.htm) topics to learn more.

[7. Run the design and adjust endpoint controls](javascript:void(0))

Press F5 to save the design to the Core and run it. Double-click any of the endpoint's Video components to open the control panel, and then adjust the endpoint's controls as desired.
