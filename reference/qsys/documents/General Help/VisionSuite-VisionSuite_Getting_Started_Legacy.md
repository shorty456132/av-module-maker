# Getting Started with VisionSuite (Legacy SV)

> Source: https://help.qsys.com/Content/VisionSuite/VisionSuite_Getting_Started_Legacy.htm

# Getting Started with VisionSuite (Legacy SV)

This topic describes getting started with legacy SV (SVS1 or SVS4) VisionSuite AI Accelerator hardware.

**Note:** To ensure compatibility, ensure that the Plugin version and the Seervision Suite version is the same, (e.g., Suite v90 should be controlled by Plugin v90). The latest software can be found on our [VisionSuite Updates and Downloads](https://www.qsys.com/products/q-sys/video/q-sys-visionsuite/visionsuite-updates/) page.

[Accessing the User Interface](javascript:void(0))

The HDMI ports on the SVS1 and SVS4 servers cannot be used to access the web interface. They will just show a terminal login prompt and nothing else.

The Seervision UI is actually a website (more specifically, a web app). To access the UI, you'll need to visit the server IP by using Google's Chrome browser.

The server uses a DHCP address by default. If there is no DHCP server, it will use a link-local address in the **169.254.x.x** range.

#### Procedure:

1. Power up the SV AI Accelerator.
2. Connect it to your LAN.
3. Open up Q-SYS Designer and download the latest version of the VisionSuite plug-in package.
4. Once downloaded, open up the Seervision plug-in in your Q-SYS Design.

* On the Set Up tab of the plugin, under the Server Discovery (mDNS) section, press the Discover Servers button
* Make sure you're on the same LAN as the SV AI Accelerator.

5. Access the IP address of the identified server(s) by copying and pasting it into your Google Chrome browser

If you have an SVS4 (2 channel) server, you'll be able to navigate between both software instances by simply typing /1 or /2 at the end of IP address in your browser, or by using the navigation bar at the top:

* Instance 1: http://ip\_address/1
* Instance 2: http://ip\_address/2

[Configuring Control of the NC-Series Cameras](javascript:void(0))

To configure control of your NC-series PTZ, make sure it is either an NC 12x80 or an NC 20x60, then work through the following steps:

1. Open up the Operations Server (hamburger menu on the top right) and locate the **PTU Configuration** card.
2. Under **Name**, give it a friendly name with which you can recognize the PTZ (i.e. tracking cam 1).
3. Under **PTU**, select the appropriate driver for the camera (either **QSYS NC 12x80 v9.10+** or **QSYS NC 20x60 v9.10+**).
   * If you're using an NC-110 as a conductor camera, select **Virtual Driver** instead.
4. Under **IP**, provide the IP address of the PTZ camera.
   * You'll find the IP address of your camera in the Configurator tab using Q-SYS Designer.
5. Under **Model**, select Q-SYS.
6. Under **Lens**, select the lens that corresponds to your PTZ model.
7. If your camera is ceiling-mounted (i.e. upside down), make sure to select the tickboxes for **invert pan/tilt**.
8. Hit **Apply Immediately**.

[Connecting the Video Input](javascript:void(0))

To steer the camera, the server will also need its video feed. To ingest the RTSP video feed:

1. Navigate to the home page of the Seervision web UI
2. In the top left, open the **Video Input** dropdown menu
3. Click the RTSP option, and add the location of the RTSP stream, which should look something like **rtsp://yourcameraip/main** (for example: rtsp://192.168.1.24/main)
4. Select the RTSP stream that you've just added from the dropdown

[Connecting to the Plugin](javascript:void(0))

Once your server is up and running, you'll want to make sure it talks to the relevant Seervision plug-in in your Q-SYS Design. Make sure you've downloaded the latest version from **Asset Manager**.

To learn more about using the plug-in, follow the documentation provided once installed, or simply press F1 once you've dragged it into your Q-SYS design to access the help page.

[Q-SYS Seervision Hardware and Software Overview](javascript:void(0))

To enhance your understanding and skills, we recommend watching this [training video](https://www.youtube.com/watch?v=hClpzvRKcII). The video covers the Seervision hardware and provides guidance on setting up the server, connecting it to a network, and accessing the web user interface.
