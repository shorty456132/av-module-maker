# USB Video Bridge

> Source: https://help.qsys.com/Content/Schematic_Library/usb_uvc.htm

# USB Video Bridge

The USB Video Bridge receives Q-SYS Mediacast streams from Q-SYS Mediacast-capable devices (cameras) and bridges the streams to USB, enabling you to view camera video on a connected computer. Q-SYS devices supporting video bridging emulate webcam video drivers.

[Q-SYS Devices that Support Video Bridging](javascript:void(0))

These devices support USB video bridging from Q-SYS Mediacast-capable devices to a connected PC:

* [Core 8 Flex](../Hardware/Processing/Core_8_Flex.htm)
* [Core 24f](../Hardware/Processing/Core_24f.htm)
* [Core Nano](../Hardware/Processing/Core_Nano.htm)
* [Core 110f](../Hardware/Processing/Core_110f.htm)[1](#These)
* [Core 110c](../Hardware/Processing/Core_110c.htm)1 *Video Bridge is not supported after version 9.5.*
* [NV-21-HU Network Video Endpoint](../Hardware/Video/NV-21-HU.htm)
* [NV-32-H (Core Capable) Network Video Endpoint](../Hardware/Video/NV-32-H_Core_Capable.htm)
* [I/O-USB Bridge](../Hardware/IO_Expanders/IOUSB_Bridge.htm)
* [TSC-70-G3](../Hardware/Control_IO/TSC-70-G3.htm)[2](#To)
* [TSC-101-G3](../Hardware/Control_IO/TSC-101-G3.htm)[2](#To)

###### 1. These devices require a USB 3.0 connection between the device and the host PC for high resolution video streaming. See [Video Formats](#Video) for more information.

###### 2. To learn more about TSC-G3 Series video bridging, see the [TSC-70-G3](../Hardware/Control_IO/TSC-70-G3.htm) or [TSC-101-G3](../Hardware/Control_IO/TSC-101-G3.htm) topics.

[USB Connection Requirements](javascript:void(0))

* For most Q-SYS hardware, connect your PC or Mac host to the Q-SYS Core or peripheral's USB-B port or, if supported, the USB-C port.
* A USB 3.0 or USB-C cable must be 6 feet in length or less. Cables longer than 6 feet may have undetermined results.
* If the Q-SYS device has both USB-B and USB-C ports, only one can be used at a time to connect to a PC or Mac host. If both are connected to hosts, the USB-B port takes priority.
* QSC supports the direct connection between a Q-SYS peripheral and a host device. USB extenders, hubs, and docks are not supported.

**Note:** By default, USB 2.0 connections are not supported for TSC Series Gen 3 USB video bridging. There are two possible orientations for the TSC side of a USB-C cable and currently only one orientation is supported for USB 3.0 connections. The supported orientation for USB 3.0 depends on the type of USB cable and/or adapter used. The simplest method to quickly determine the correct USB cable orientation is to deploy a video bridging design with USB 2.0 disabled (set the TSCâs USB 2.0 Support property to âDisabledâ) then connect a USB 3.0 capable Host device to the TSC through the USB 3.0 cable and/or adapter that will be used. If the TSC status indicates it is âCompromisedâ, flip the cable connection at the TSC connector. Once the TSC is not in a Compromised state, USB 2.0 can be re-enabled (set the TSCâs USB 2.0 Support property to âEnabledâ). For more information, see the [USB Video Bridge](#) topic.

**Tip:** For most USB-C cables, orientation 1 is seen while the cable is connected with the logo side facing the RJ45 connection. QSC recommends using a USB-C to USB-A cable for most host PCs. USB-C only hosts should then use a common USB-C to USB-A adapter.

**Tip:** If a long distance USB bridging solution is required, we recommend the [I/O-USB Bridge](../Hardware/IO_Expanders/IOUSB_Bridge.htm), which can easily be extended to the desired location via network cabling.

[Configuration Overview](javascript:void(0))

The USB Video Bridge is a component within the inventory tree of a supported Q-SYS device.

1. Add a Q-SYS device that supports video bridging to your inventory.
2. From the Q-SYS device's properties, set the USB Video Bridge property to 'Enabled'.
3. From the Q-SYS device's inventory tree, drag the USB Video Bridge component into your schematic.
4. Add a Q-SYS  camera to your inventory and drag the [Status/Control (Cameras)](onvif_camera_operative.htm) component into your schematic.
5. Wire the Status/Control (Camera) component to the USB Video Bridge component.

**Tip:** You can also route multiple camera streams to one or more USB Video Bridges using a Mediacast Router component. For more information, see [Mediacast Router](video_router.htm).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### USB Bridging â Video Bridge Properties

These properties are available when the USB Video Bridge property is set to 'Enabled'.

#### UVC Camera Control

When this is enabled (disabled by default), the camera can be controlled by far-end third party applications which support Relative Movement Commands. When disabled, the cameras cannot be controlled by the applications.

#### Mediacast to HDMI Camera Control

As an expansion to Mediacast to HDMI you can provide basic camera control at the NV-32-H endpoint. Each NV-32-H will have a new Mediacast Input tab if at least 1 Mediacast Input is enabled. To see schematic examples of Mediacast and HDMI Video Source, or to see what Properties are available with Auto Privacy, see [HDMI I/O (NV-32-H)](streamer_hdmi_switcher.htm).

#### Video Formats

Select what video formats are allowed to pass from the Q-SYS device to the host application based on the capabilities of your USB infrastructure â USB 2.0 or USB 3.0.

**Tip:** USB 3.0 connections allow for HD YUY2 formats, which use less compression and therefore have a higher quality image.

The table below reflects video format support as exposed in Q-SYS Designer through the Video Bridge's Video Formats Property. The properties provide video format options based on both hardware's technical capabilities and best user experience.

Specifically, while the I/O USB Bridge supports YUY2 formats, it is optimized for low-resolution, YUY2 formats (e.g., 640x360) and does not support HD YUY2 formats (720p,1080p).

Since the I/O USB Bridge does not support HD YUY2 formats, the HD YUY2 Formats is not an option in the I/O USB Bridge's Video Format property. Additionally, the UC&C YUY2 Formats are not exposed for I/O USB Bridge, as this property would only expose the supported YUY2 formats (640x360).

Only exposing a low-resolution format will lead to poor user experience, as Microsoft Teams, Zoom, and other UC&C applications will scale up the small format into large windows. This results in compromised image quality. Generally, low resolution formats such as 640x360 are used for small preview windows or small cells, while HD resolution formats are used for large windows. To support the above use case, the I/O USB Bridge only exposes the low resolution YUY2 format in combination with HD MJPEG formats and does not allow only exposing low resolution formats.

| Device | USB Version | UC&C Formats | HD Formats | UC&C YUY2 Formats | HD YUY2 Formats |
| --- | --- | --- | --- | --- | --- |
| Core Nano  Core 8 Flex  NV-32-H  Core 24f  I/O-Core 24f | USB 2.0 | 640x360p15 YUY2  640x360p30 YUY2  1280x720p15 MJPEG  1280x720p30 MJPEG  1920x1080p15 MJPEG  1920x1080p30 MJPEG | 1280x720p15 MJPEG  1280x720p30 MJPEG  1920x1080p15 MJPEG  1920x1080p30 MJPEG | 640x360p15 YUY2  640x360p30 YUY2 | None  (USB Video Bridge will not work.) |
| USB 3.0 | 640x360p15 YUY2  640x360p30 YUY2  1280x720p15 YUY2  1280x720p30 YUY2  1920x1080p15 YUY2  1920x1080p30 YUY2  1280x720p15 MJPEG  1280x720p30 MJPEG  1920x1080p15 MJPEG  1920x1080p30 MJPEG | 1280x720p15 YUY2  1280x720p30 YUY2  1920x1080p15 YUY2  1920x1080p30 YUY2  1280x720p15 MJPEG  1280x720p30 MJPEG  1920x1080p15 MJPEG  1920x1080p30 MJPEG | 640x360p15 YUY2  640x360p30 YUY2  1280x720p15 YUY2  1280x720p30 YUY2  1920x1080p15 YUY2  1920x1080p30 YUY2 | 1280x720p15 YUY2  1280x720p30 YUY2  1920x1080p15 YUY2  1920x1080p30 YUY2 |
| Core-110f[1](#1.)  Core-110c[1](#1.) | USB 2.0 | Not Supported | Not Supported | 640x360p15 YUY2  640x360p30 YUY2  848x480p15 YUY2[2](#2.)  848x480p30 YUY2[2](#2.)  960x540p15 YUY2[2](#2.) | None  (USB Video Bridge will not work.) |
| USB 3.0 | Not Supported | Not Supported | 640x360p15 YUY2  640x360p30 YUY2  1280x720p15 YUY2  1280x720p30 YUY2  1920x1080p15 YUY2  1920x1080p30 YUY2 | 1280x720p15 YUY2  1280x720p30 YUY2  1920x1080p15 YUY2  1920x1080p30 YUY2 |
| TSC-70-G3  TSC-101-G3 | USB 2.0 | Not Supported | Not Supported | 640x360p15 YUY2  640x360p30 YUY2 | None  (USB Video Bridge will not work.) |
| USB 3.0 | Not Supported | Not Supported | 640x360p15 YUY2  640x360p30 YUY2  1280x720p15 YUY2  1280x720p30 YUY2  1920x1080p15 YUY2  1920x1080p30 YUY2 | 1280x720p15 YUY2  1280x720p30 YUY2  1920x1080p15 YUY2  1920x1080p30 YUY2 |
| I/O USB Bridge | USB 2.0 | 640x360p15 YUY2  640x360p30 YUY2  1280x720p15 MJPEG  1280x720p30 MJPEG  1920x1080p15 MJPEG  1920x1080p30 MJPEG | 1280x720p15 MJPEG  1280x720p30 MJPEG  1920x1080p15 MJPEG  1920x1080p30 MJPEG | 640x360p15 YUY2  640x360p30 YUY2 | None  (USB Video Bridge will not work.) |
| NV-21-HU | USB 2.0 | Not Supported | Not Supported | 640x360p15 YUY2  640x360p30 YUY2 | None  (USB Video Bridge will not work.) |
| USB 3.0 | Not Supported | Not Supported | 640x360p15 YUY2  640x360p30 YUY2  1280x720p15 YUY2  1280x720p30 YUY2 | 1280x720p15 YUY2  1280x720p30 YUY2 |

**Note:** Video formats that are exposed to the PC are also dynamically filtered at runtime based on the USB connection speed. Notice that HD YUY2 formats are automatically removed when the connection speed is USB 2.0. For example: In a BYOD scenario, a USB 3.0 capable laptop can connect to a Core Nano with a maximum format of 1920x1080p30 YUY2. Using the same USB cable, a different USB 2.0 capable laptop can connect with a maximum format of 1920x1080p30 MJPEG. This feature offers flexibility without the need to redeploy.

###### 1. The Q-SYS Core 110f and Core 110c processors supports YUY2 formats only and are therefore limited to a maximum format of 960x540p15 with a USB 2.0 connection; USB 3.0 connections are highly recommended. MJPEG formats are unavailable for USB 2.0 and USB 3.0 connections from Core 110f processors. *Video Bridging on the Core 110c is not supported after version 9.5.*

###### 2. 960x540p15 is the maximum format supported for Core 110f with USB 2.0 connection; however, most host applications will choose the next best, higher frame rate format 848x480p30. These formats are not available for TSC Generation 3.

#### USB 2.0 Support

##### Core 110f /Core 110c

When set to Enabled, the USB Video Bridge allows video formats compatible with USB 2.0 and 3.0 connections. When set to Disabled, the USB Video Bridge only allows USB 3.0 connections. To force support for USB 3.0 and HD formats exclusively, set this property to Disabled and set the Video Formats property to HD YUY2 Formats. The default is Enabled. *Video Bridging on the Core 110c is not supported after version 9.5.*

##### TSC-70-G3 / TSC-101-G3

When set to Enabled, the USB-C orientation check is bypassed and the USB Video Bridge allows USB 2.0 and 3.0 connections. When set to Disabled, the USB Video Bridge only allows USB 3.0 connections and bridging will only function in USB-C orientation 1. To force support for USB 3.0 and HD formats exclusively, set this property to Disabled and set the Video Formats property to HD YUY2 Formats. The default is Disabled.

[Controls](javascript:void(0))

[Control Tab](javascript:void(0))

Not all controls are supported by all camera models. When a design is running, controls are either not visible (Status/Control component) or grayed-out (Video Bridge component) if not supported by your camera model.

**Note:** Due to the wide variety of Q-SYS camera models and differing default values for camera controls, those default values are not indicated here. Use the Reset all Camera settings (Imaging, PTZ, and Focus) control in the Imaging tab to reveal the defaults for your camera model.

### Pan / Tilt / Zoom

#### Pan, Tilt

Pan left or right (allows for 360Â° pan), tilt upward or downward. Click and release for small increments, or click and hold to tilt continually until the camera reaches the mechanical limits.

#### Pan/Tilt

(NC Series cameras only) Combination pan and tilt. Click and release for small increments, or click and hold to tilt continually until the camera reaches the mechanical limits.

#### Zoom

Zooms out or zooms in, giving you a wider or smaller angle of view. Click and release for small increments, or click and hold to zoom continually.

#### Coordinates

Positional coordinates are P T Z F: P=Pan, T=Tilt, Z= Zoom, and F=Focus, with Focus being optional. Each coordinate is separated by a space. A set of coordinates of 0 0 0 (default) puts the camera level, facing front, and zoomed fully out. Appending a fourth value for Focus forces the camera into Manual focus mode. Without a Focus value, Auto Focus (AF) is engaged. Refer to the Control Pins table for valid coordinate value ranges.

**Tip:**  Copy and paste these coordinates into a Q-SYS Snapshot to create camera presets. In addition, you can select the coordinates and type in the desired position if you know it.

**Note:** The Focus coordinate is not supported by NC-110 cameras.

#### Speed by Zoom

When engaged, the speed of the pan, tilt and zoom decreases as you zoom closer to give you more control. The speed of the pan, tilt and zoom increases as the angle of view gets wider. The default is 'On'.

#### Recalibrate PTZ

Recalibrates the camera's PTZ stepper motor locations (Pan, Tilt and Zoom) and returns the cameras to the Privacy position.

**Note:** When cameras are properly configured with the VisionSuite plugins, the Seervision cameras will recall their default position containers 30 seconds after recalibration is complete. ACPR cameras will not recall any default position after recalibration is complete and will remain in their privacy position until a preset is fully loaded.

#### Ceiling Mount

Engaging this button flips the picture upside down to accommodate mounting the camera on the ceiling. The up and down Tilt controls are flipped as well. The default is 'Off'.

#### Is Moving

(NC Series cameras only) This LED control indicates when the camera is actively panning, tilting, or zooming. (Focusing does not affect this control.)

#### Move Completed

(NC Series cameras only) This LED control indicates when the camera has stopped moving. (Focusing does not affect this control.)

#### Home

The Home button returns the camera to the default Home position, or the position that was saved by the Save Home button.

#### Save Home

The Save Home button saves the current camera position (PTZ Coordinates) as the Home position.

#### Load Privacy

When engaged, the Load Privacy button recalls the privacy preset position as captured when the Save Privacy button was clicked. By default the camera is facing backwards and outputs a black video stream. When the button is disengaged, the camera returns to the position it was when the Load Privacy button was engaged. The Load Privacy button is disengaged when a coordinate is entered in the Coordinates field, or if a Q-SYS Snapshot is evoked.

#### Save Privacy

The Save Privacy sets the privacy preset position. This is the location to which the camera returns when the Load Privacy button is clicked, and when the camera first powers up. By default, this location is pointed towards the back of the camera.

#### Auto Privacy

**Tip:** Auto privacy will not work with un-wired outputs on the Mediacast Router.

* When on, cameras connected to the video bridge automatically enter privacy mode until video is requested (USB connected to a computer and an application viewing the video), at which point the camera exits privacy mode and moves to the home position. When video is no longer requested, the camera returns to privacy mode by recalibrating PTZ and recalling the specified privacy coordinates.
* When off, cameras do not automatically enter privacy mode when no video is requested. When manually entering privacy mode, the PTZ is not recalibrated.

**Note:** If the USB Video Bridge is connected to a [Mediacast Router](video_router.htm), the router automatically switches to the Camera 1 input. This is by design, and allows the room to be left in a known good configuration. Connect your room's "default" camera to the router's Camera 1 input.

#### AP Delay

Auto Privacy Delay, from 1 to 600 seconds (default is 60). After video is turned off (or USB disconnected) and after the AP Delay timeout period, the camera returns to the privacy mode again.

#### Pan Speed, Tilt Speed, Zoom Speed

Adjust the speed of motor movements for panning, tilting, or zooming the camera, from 0 to 1.00 (default .750). Use your mouse to drag the slider or enter a number.

#### Recall Speed

Adjust the speed of motor movements when recalling PTZ coordinates, such as when loading a saved [Snapshot](snapshot_controller.htm), from 0 to 1.00 (default is 1.00). Use your mouse to drag the slider or enter a number.

### Focus

**Note:** Focus controls are not applicable to NC-110 cameras.

#### Auto Focus

Toggles Auto Focus on or off (default is 'On'). Auto Focus is turned off when one of the Manual focus buttons is clicked.

#### Focus In, Focus Out

The Focus In button changes the focus mode to Manual and pushes the focal point toward the background of the shot. Objects in the foreground are less likely to be in focus, objects in the background are more likely to be in focus.

The Focus Out button changes the focus mode to Manual and pushes the focal point toward the foreground in the shot. Objects in the foreground are more likely to be in focus, objects in the background are less like to be in focus.

**Note:** When you first press Focus In or Focus Out, the camera transitions from Auto Focus mode to Manual Focus mode. After this transition, a subsequent press of Focus In or Focus Out affects the focus value. If you wish to adjust focus immediately when coming from Auto Focus mode, then double-click the Focus In or Focus Out buttons.

#### Manual Speed

The Focus Speed slider adjusts the speed at which the Focus In and Focus Out buttons operate, from .001 to .100 . Does not apply to the Auto Focus mode. Use your mouse to drag the slider or enter a number.

#### AF Sensitivity

The Sensitivity drop-down menu controls how aggressive the Auto Focus algorithm operates to keep the camera in focus. Setting this too low can create a semi-blurry image, while setting this too high can create focus-hunting. Does not apply to the Manual Focus mode. Choices are Low, Normal, and High (default).

#### AF Zone

Select an area of the image for the Auto Focus algorithm to prioritize: Center (default), Bottom, or Top. For example, if the camera's view includes a conference table in the bottom of the image but conference participants are seated more toward the top of the image (as in the case of a long conference table), you would set this control to 'Top' to avoid the table being a focus point.

While in emulation or runtime modes, selecting Face enables the Face Focus option for NC-PTZ cameras. This option uses AI to detect faces within the camera's field of view and maintain precise focus on a single person while moving within the frame. When enabled, the system automatically disables HDMI/SDI outputs to allow the camera's AI to deliver the best focus performance. All other Auto-Framing controls will continue to function as usual.

**Note:** Face Focus is not recommended when multiple faces are present, as the camera may focus on a region that does not keep all faces in focus, especially with increased zoom.

### Preview

The Preview screen shows the camera's current view and updates once per second. The screen includes controls for Pan, Tilt, and Zoom as documented in [Pan / Tilt / Zoom](#Pan).

**Note:** TSC Series touch screens can accommodate two or three Preview images on an single UCI before its operation and controls become sluggish.

**Note:** When any of the Auto Framing controls (Enable, Face Count, or Outline Faces) are enabled, the JPEG previews in Q-SYS Designer and on TSC UCIs will only show full FoV. These preview types cannot show the auto framed FoV. Live previews available on devices such as TSC-G3 series will show auto framed FoV, just like the primary Mediacast stream.

[Imaging Tab](javascript:void(0))

Not all controls are supported by all camera models. When a design is running, controls are either not visible (Status/Control component) or grayed-out (Video Bridge component) if not supported by your camera model.

**Note:** Due to the wide variety of Q-SYS camera models and differing default values for camera imaging controls, those default values are not indicated here. Use the Reset all Camera settings (Imaging, PTZ, and Focus) control to reveal the defaults for your camera model.

#### Reset all Camera settings (Imaging, PTZ, and Focus)

This button resets all of the camera's Control and Imaging tab settings back to their default values, excluding SDI/HDMI Enable and SDI/HDMI Format. Values that are reset to default include:

* All Pan / Tilt / Zoom controls, including the Home and Privacy positions.
* All Focus controls.
* All Imaging, Exposure, White Balance, and Noise Reduction controls.

**Tip:** This is a quick and easy way to go back to Auto mode on all of the settings.

### Imaging

#### Brightness

The general intensity of light in an image, from 0 to 14. Increasing this number makes the image brighter. Decreasing this number and the image will appear darker.

#### Saturation

Amount of total color (chroma) in the image, from 0 to 14. Reducing this number will result in the image displaying dull or muted colors. Increasing this will result in the images colors being more vivid.

#### Sharpness

The boundaries between different tones or colors, from 0 to 14. Increasing this number will improve definition between objects. Decreasing this number will reduce definition, creating blurred lines between objects.

#### Contrast

The separation between the darkest and brightest parts of an image, from 0 to 14. Increasing this number will make the separation grow, decreasing this number will reduce the separation.

### Exposure

#### Mode

Toggles between Auto and Manual. In Auto Mode (default), Aperture, Shutter, and Gain values are set automatically.

#### Backlight Comp

With this mode selected, a dark subject against a bright background (or a bright light in a dark image) will be compensated for by allowing more light in to brighten the image. With this mode selected in normal lighting conditions, the image will be overexposed. The default is 'Off'.

#### Anti-Flicker

Toggles whether to reduce the "beating" pattern created by the camera's exposure time and frequency of the lighting source. When on (default), the shutter's exposure time is increased to reduce the image "flicker" artifacts in the image. For very bright scenes, turn this off to allow the camera to reduces the exposure time and prevent the image from being overexposed.

> #### HDR Mode
>
> HDR improves image quality in rooms with both bright and dark areas. For example, details are preserved when people are presenting in front of a screen or sitting in a conference room with large windows. This makes faces and background details clearer and more balanced. HDR is enabled by default.
>
> **Note:** This applies to NC-90-G2 cameras only.

#### Compensation

Increase this value to make the image brighter reduce it to make it darker, from -7 to 7. This is the best adjustment to compensate for changes made by the Auto Exposure Mode.

#### Gain Limit

The camera increases the gain in its image sensor up to this limit to get the best image exposure, from 0 to 15. Too high of a gain shows more noise, while too low can create a darker image.

#### Dynamic Range

The range in which a camera can successfully capture the lightest and darkest area of an image, from 0 to 8. Increasing the range can lead to blurring and loss of detail. Too little dynamic range and there will not be separation of color or contrast between light and dark components in an image. This field is available in both Auto and Manual Modes.

#### Aperture

This controls the iris in the lens of the camera. Moving the slider to right increases the f-stop and makes the iris smaller, reducing the amount of light and extending the field of view. Moving the slider to the left does just the opposite. You can select from f/1.8 , f/2.0, f/2.4, f/2.8, f/3.4, f/4.0, f/4.8, f/5.6, f/6.8, f/8.0, f/9.6, f/11.0, and Close.

#### Shutter

This controls the camera's exposure time, in fractions of a second. The longer the exposure time, more light is allowed into the camera, which makes the image brighter. You can select from 1/30, 1/60, 1/90, 1/100, 1/125, 1/180, 1/250, 1/350, 1/500, 1/725, 1/1000, 1/1500, 1/2000, 1/3000, 1/4000, 1/6000, or 1/10000.

#### Gain

Often referred to as 'iris gain', this adjustment brightens or darkens the image sensor's output, from 0 to 7. Video with high gain is likely to be very 'noisy' or 'grainy'.

### White Balance

#### Mode

White balance adjusts the camera's color settings to compensate for the ambient lighting conditions. To our eyes, white looks white regardless of the ambient lighting. However, if you take a picture under fluorescent light, it looks greenish. You can adjust the camera settings to make the white appear white under these and other lighting conditions.

Select from these options:

* Auto: (Default) Full automatic mode for White Balance.
* Indoor/3000K: (PTZ-IP Series cameras only) Preset for indoor lighting with color temperatures around 3000Â° Kelvin
* Outdoor/5000K: (PTZ-IP Series cameras only) Preset for outdoor lighting with color temperatures around 5000Â° Kelvin
* Manual: Full manual mode for White Balance. Manual mode activates the Manual Red Gain and Manual Blue Gain controls.
* One Push:The functionality depends on the camera series:
  + NC Series: This mode is recommended for difficult lighting situations where each camera in a room experiences different lighting. Simply aim the camera at a 18% gray card (that occupies the entire image), press the One Push button, and the camera will self-calibrate. During the calibration period (approximately 5 seconds), all White Balance controls are disabled. Once the calibration is complete, the White Balance controls are re-enabled and the camera then transitions to Manual mode.
  + PTZ-IP Series: When selected, the camera uses its Auto White Balance algorithm once and then does not adjust the white balance again unless you click the One Push button again.

**Tip:** When you toggle an NC Series camera's White Balance Mode from 'Auto' to 'Manual', the current White Balance values are retained from the camera itself, not from the camera's Status/Control component or USB Video Bridge component. This means that you can "lock in" the current White Balance 'Auto' values simply by switching to 'Manual', and then adjust the White Balance controls as needed.

#### AWB Sensitivity

Sensitivity setting for Auto White Balance mode â Low (default), Medium, or High. Adjusting this will adjust the threshold for the AWB algorithm to recalculate.

#### AWB One Push

Momentary button to toggle the One Push functionality as described in **Mode** above. If you press the AWB One Push button while in any other White Balance mode, it causes the camera to enter One Push mode.

#### Hue

If the you believe the camera's white balance algorithm isn't quite right, or the display isn't showing whites as white, manually adjust the Hue setting to achieve the desired white â from 0 to 14.

#### Auto Red, Blue Gain

In 'Auto' white balance Mode, this sets the target value for the amount of red or blue in an image, from 1 to 255. For NC Series cameras, set these values to better support challenging lighting conditions.

#### Manual Red, Blue Gain

In 'Manual' white balance Mode, this adjusts the amount of red or blue in an image, from 1 to 5000.

### Noise Reduction

**Note:** 2D NR and Hot Pixel controls are not supported by NC Series cameras.

#### 2D NR Mode

Select the type of 2D (spatial) noise reduction:

* Off: Disable 2D noise reduction.
* Auto: (Default) The camera will attempt to eliminate spatial noise in the image.
* Manual: Enables the 2D NR control.

#### 3D NR Enable

Temporal noise in the image can be effectively reduced by enabling 3D Noise Reduction. The amount of 3D NR reduction applied to the image is determined by the 3D NR control. The higher the value, the more temporal / 3D noise is removed. Set too high, the image will create "ghosting" artifacts behind moving images. 3D NR is enabled by default.

#### Hot Pixel Enable

Toggle whether to allow the camera to compensate for bad pixels in the camera's image sensor. Often seen as bright or "hot" pixels, these can be effectively eliminated by enabling this Hot Pixel compensation setting. This control is disabled by default.

#### 2D NR

In 'Manual' 2D NR mode, select how much to spatially adjust the image, from 1 to 5. The higher the value, the more the image is softened / blurred.

#### 3D NR

When 3D NR is enabled, select how much to temporally filter the image, from 1 to 11. The higher the value, the more 3D noise is filtered.

#### Hot Pixel

When Hot Pixel is enabled, select how much to compensate for bad pixels, from 1 to 5. The higher the value, the more consecutive bad pixels can be compensated for / filtered out.

### SDI/HDMI Format

**Note:** This section is not applicable to NC-110 cameras.

#### Imaging Frame Rate (Hz)

Select the camera's frame rate. Available choices are determined by the camera model:

NC-Pro15x: 30Hz or 60Hz

NC-12x80 and NC-20x60: 50Hz, 59.94Hz, or 60Hz

#### Apply

Applies chosen frame rate to NC-Pro15x camera. This will reboot the camera.

#### SDI/HDMI Enable

When enabled, the SDI and HDMI outputs are active, otherwise they are turned off (default is off). The SDI/HDMI outputs are turned on whenever the OSD is turned on (ID Mode is on).

**Note:** After a Factory Reset of NC-12x80 and NC-20x60 cameras, the HDMI output and OSD (ID Mode) remain enabled if the camera is not connected to a Q-SYS Core processor in a design.

#### SDI/HDMI Mode

For NC-12x80 and NC-20x60 camera models only, this control toggles between SDI mode ('on') and HDMI mode ('off', default) when the SDI/HDMI Enable control is on.

**Note:** NC Series PTZ cameras support the usage of either HDMI or SDI, but not both simultaneously.

#### SDI/HDMI Format

Select the video format for the SDI and HDMI camera outputs. Selections depend on the camera model, selected SDI/HDMI Mode, and selected Imaging Frame Rate (Hz).

| Camera Model and Frame Rate | HDMI Mode | SDI Mode | HDMI/SDI Mode |
| --- | --- | --- | --- |
| NC-Pro15x @ 60Hz | 2160p30  1080p60  1080p30  1080i60  720p60  720p30 | 1080p60  1080p30  1080i60  720p60 | Yes |
| NC-Pro15x @ 59.94Hz | 2160p29.97  1080p59.94  1080p29.97  1080i59.94  720p59.94  720p29.97 | 1080p59.94  1080p29.97  1080i59.94  720p59.94 | Yes |
| NC-Pro15x @ 50Hz | 2160p25  1080p50  1080p25  1080i50  720p50  720p25 | 1080p50  1080p25  1080i50  720p50 | Yes |
| NC-Pro15x @ 30Hz | 2160p30  1080p30  720p30 | 1080p30 | Yes |
| NC-Pro15x @ 29.97Hz | 2160p29.97  1080p29.97  720p29.97 | 1080p29.97 | Yes |
| NC-Pro15x @ 25Hz | 2160p25  1080p25  720p25 | 1080p25 | Yes |
| NC-Pro15x @ 23.98Hz | 2160p23.98  1080p23.98  720p23.98 | 1080p23.98 | Yes |
| NC-12x80 and NC-20x60 @ 60Hz[1](#NC-12x80) | 2160p30  1080p60  1080p30  1080i60  720p60  720p30 | 1080p60  1080p30  1080i60  720p60 | N/A |
| NC-12x80 and NC-20x60 @ 59.94Hz | 2160p29.97  1080p59.94  1080p29.97  1080i59.94  720p59.94  720p29.97 | 1080p59.94  1080p29.97  1080i59.94  720p59.94 | N/A |
| NC-12x80 and NC-20x60 @ 50Hz | 2160p25  1080p50  1080p25  1080i50  720p50  720p25 | 1080p50  1080p25  1080i50  720p50 | N/A |

###### 1. NC-12x80 and NC-20x60 cameras reset to 1080p60 HDMI during a Factory Reset.

#### SDI Level A/B

For NC-12x80 and NC-20x60 camera models only, select whether the SDI output is Level A (most common) or Level B (interleaved). This control is applicable when a 3G-SDI format is selected (formats 1080p50 and higher). For HD-SDI formats (lower than 1080p50), this control is not applicable.

[Mediacast / IP Streams Tab](javascript:void(0))

### Preview Stream

The Preview Stream is a lower resolution (360p maximum) H.264 stream that can be viewed by third-party applications and hardware decoders.

**Note:** The Preview Stream is always multicast, no matter how many devices on the network request it. If your network doesn't support multicasting or you want to prevent third-party device access to the Preview Stream, it can easily be disabled with the Preview Stream Enable toggle.

#### Preview Stream Enable

The Preview Stream is disabled by default. Use this control to toggle it on or off. When enabled, the camera multicasts the Preview Stream to any clients (Q-SYS devices or third-party devices) that request a stream from the RTSP URL.

#### RTSP URL

When the Preview Stream is enabled, this control displays the camera's RTSP server URL for the stream. The control is empty if Preview Stream is disabled.

**Tip:** USB Bridging devices also display this control, allowing third-party RTSP clients to follow the USB Bridge's sources as they change.

#### RTP Address

This control shows the actual RTP address the camera uses to multicast the Preview Stream. Use Q-SYS [Core Manager](../Core_Manager/CoreManager_Overview.htm) to configure multicast addressing.

#### Streaming Mode

Select the resolution for the Preview Stream. Normally, you should leave this set to 'Auto', which allows Q-SYS to automatically set the resolution and frames per second (fps) based on the capabilities of the hardware. However, you can manually choose a resolution based on your needs.

* Auto (default)
* h.264 640x360
* h.264 480x270
* h.264 320x180

**Note:** Changing the Streaming Mode may disrupt IP streams and HDMI/SDI outputs.

#### Streaming Mode > fps

When Streaming Mode is set to 'Auto', the frames per second (fps) value is automatically adjusted for the Preview Stream. When a manual resolution is selected, you can choose an fps value from 1 to 30 (15 is default).

#### Video Format

This read-only control shows the current, actively streaming format of the Preview Stream.

#### Max Bitrate (Mbps)

The Preview Stream's bitrate will not exceed the value specified here, from .500 to 2.00.

### Mediacast Stream

The Mediacast Stream is a high resolution H.264-only stream for output to Q-SYS USB Bridging devices for playback on a USB host device, such as PC with conference software. The USB Video Bridge decompresses the H.264 stream and locally scales the resolution and frame rate to match format that the USB host requests.

#### RTP Address

This read-only control indicates the RTP address being used by the Mediacast stream, whether multicasting or unicasting.

#### Video Format

This read-only control shows the current, actively streaming format of the Mediacast stream.

#### Max Bitrate

The average Mediacast Stream bitrate will not exceed the value specified here, from 1.00 to 25.0.

**Note:** Instantaneous bitrate can exceed this value up to the limitations of the network.

#### Peak Frame Bitrate

This control defaults to 60 Mbps and limits each frameâs network bitrate, as averaged over the entire frameâs period. When set to 60Mbps, a gigabit Ethernet uplink port can support 1000/60 = 16 cameras. Users should reserve this bitrate setting for NV Decoders that also receive camera streams for USB Bridging or HDMI outputs (meaning, reduce the Encoder bitrates for each simultaneous camera stream that a NV Decoder will receive).

### NDI (NC-Pro15x)

#### NDI

Enables NDI stream.

#### NDI Only

Enables NDI Only output. This will shut off Mediacast Streaming.

[Status](javascript:void(0))

The following information is available only when the USB Video Bridge is set to 'Enabled' in the properties and the USB Video Bridge component is in the schematic.

**Note:** In order to see the data in the fields listed below, you must have a network connection between the camera and the I/O USB Bridge, and a USB connection to an output device. The output device must be receiving and displaying the video. If there is no signal flow, there are no statistics.

### Input

#### Input LED

Indicates whether or not there is active input to the Q-SYS video input device.

#### Input Connection

The network name of the Q-SYS video input device.

#### Bitrate (Kb/s)

The current input video bitrate, in kilobits per second.

#### Frames per Sec

Number of frames per second being sent by the video device.

#### Frame Count

Total number of frames sent.

#### Packet Count

Total number of packets since the last reset.

#### Packets Lost

Number of packets lost since the last reset.

#### Packet Loss%

The percentage of packets lost based on Packets Lost and Packet Count.

#### Test Button

Test the network setup for the Q-SYS video streaming implementation without having a PC or any USB connection. This tests QoS and IGMP on multicast.

### USB

#### USB Active LED

Video Bridge USB Active: Indicates if the USB is active or not.

#### USB Bridge Name

The network name of the Q-SYS video bridging device.

#### Video Format

Displays the format of the video present on the USB â for example, "1920x1080p30".

#### Encoding

Displays the type of encoding used for the USB video stream - for example, "MJPEG".

#### USB Speed

Displays the detected USB speed capability of the connection â for example, "High Speed (2.0)".

#### Bitrate (Mb/s)

USB bitrate, in megabits per second.

#### Frames per Sec

USB frames per second

#### SRC-

The number of samples removed in order to match the USB clock with the Q-SYS PTP clock

#### SRC+

The number of samples added in order to match the USB clock with the Q-SYS PTP clock

### Reset

#### Reset Button

Clears the readings, and restarts monitoring.

[Control Pins](javascript:void(0))

[Video Controls](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Exposure | | | | |
| Anti-Flicker | 0  1 | off  on | 0.00  1.00 | Input / Output |
| Aperture | 1 to 22 | f/1.8 , f/2.0, f/2.4, f/2.8, f/3.4, f/4.0, f/4.8, f/5.6, f/6.8, f/8.0, f/9.6, f/11.0, Close | 0, .083, .167, . 250, .333, .417, .500, .583, .667, .750, .833, .917, 1.00 | Input / Output |
| Backlight Comp | 0  1 | no  yes | 0.00  1.00 | Input / Output |
| Compensation | -7 to +7 | -7 to 7 | 0, .071, .143, .214, .286, .357, .429, .500, .571, .643, .714, .786, .857, .929, 1.0 | Input / Output |
| Dynamic Range | 0 to 8 | 0 to 8 | .125, .250, .375, .500, .625, .750, .875, 1.00 | Input / Output |
| Gain | 0 to 7 | 0 to 7 | 0, .143, .286, .429, .571, .714, .857, 1.00 | Input / Output |
| Gain Limit | 0 to 15 | 0 to 15 | 0, .067, .133, .200, .267, .333, .400,. 467, .533, .600, .667, .733, .800, .867, .933, 1.00 | Input / Output |
| Mode | N / A | off, auto, or manual | N / A | Input / Output |
| Shutter | 30, 60, 90, 100, 125, 180, 250, 350, 500, 725, 1000, 1500, 2000, 3000, 4000, 6000, 10000 | 1/30, 1/60, 1/90, 1/100, 1/125, 1/180, 1/250, 1/350, 1/500, 1/725, 1/1000, 1/1500, 1/2000, 1/3000, 1/4000, 1/6000, 1/10000 | 0, .083, .167, .250, .333, .417, .500, .583, .667, .750, .833, .917, 1.00 | Input / Output |
| Focus | | | | |
| AF | 1  0 | true  false | 1.00  0.00 | Input / Output |
| AF Zone | N / A | center, bottom, top, face | N / A | Input / Output |
| In | 0 or momentary 1 | 0 or momentary 1 | 0.00  momentary 1.00 | Input / Output |
| Manual Speed | 0.001 to 0.100 | .001 to .100 |  | Input / Output |
| Out | 0 or momentary 1 | 0 or momentary 1 | 0.00  momentary 1.00 | Input / Output |
| Sensitivity | N / A | Low, Normal, High | N / A | Input / Output |
| Imaging | | | | |
| Brightness | 0 to 14 | 0 to 14 | 0, .071, .143, .214, .286, .357, .429, .500, .571, .643, .714, .786, .857, .929, 1.00 | Input / Output |
| Contrast | 0 to 14 | 0 to 14 | 0, .071, .143, .214, .286, .357, .429, .500, .571, .643, .714, .786, .857, .929, 1.00 | Input / Output |
| Reset Cam Settings | 0  1 | 0 or false  1 or true | 0.00  1.00 | Input / Output |
| Saturation | 0 to 14 | 0 to 14 | 0, .071, .143, .214, .286, .357, .429, .500, .571, .643, .714, .786, .857, .929, 1.00 | Input / Output |
| Sharpness | 0 to 14 | 0 to 14 | 0, .071, .143, .214, .286, .357, .429, .500, .571, .643, .714, .786, .857, .929, 1.00 | Input / Output |
| IP Stream | | | | |
| Mediacast Stream | | | | |
| Max Bitrate | 1.00 to 30.0 | 1.00 to 30.0 | 0.000 to 1.00 | Input / Output |
| RTP Address | (text) | | | Output |
| Video Format | (text) | | | Output |
| Preview Stream | | | | |
| Enable | 0  1 | no  yes | 0.00  1.00 | Input / Output |
| Max Bitrate | .500 to 2.00 | .500 to 2.00 | 0.000 to 1.00 | Input / Output |
| RTP Address | (text) | | | Output |
| RTSP URL | (text) | | | Output |
| Streaming Mode Format | N/A | Auto  h.264 640x360  h.264 480x270  h.264 320x180 | N/A | Input / Output |
| Streaming Mode Frame Rate | 1 to 30 | 1 to 30 | 0.000 to 1.00 | Input / Output |
| Video Format | (text) | | | Output |
| Noise Reduction | | | | |
| 2D NR | 1 to 5 | 1 to 5 | 0, .250, .500, .750, 1.00 | Input / Output |
| 2D NR Mode | N/A | Auto, Off, Manual | N / A | Input / Output |
| 3D NR | 1 to 8 |  |  | Input / Output |
| 3D NR Enable | 0  1 | no  yes | 0.00  1.00 | Input / Output |
| Hot Pixel | 1 to 5 | 1 to 5 | 0, .250, .500, .750, 1.00 | Input / Output |
| Hot Pixel Enable | 0  1 | no  yes | 0.00  1.00 | Input / Output |
| Pan-Tilt-Zoom | | | | |
| Auto Privacy Mode | 0  1 | false  true | 0.00  1.00 | Input / Output |
| Auto-Privacy Delay | 1.00 to 600 | 1.00s to 600s | 0.00 to 1.00 | Input / Output |
| Ceiling Mount | 0  1 | no  yes | 0.00  1.00 | Input / Output |
| Coordinates | N/A | **P**an = -0.9936 to 0 to +0.9936  **T**ilt = -0.9936 to 2.9808  **Z**oom = 0.000000 to 1  **F**ocus = 0.00000 to 1  The coordinates are entered in the above order, separated by a space. | N/A | Input / Output |
| Home | 0  1 | 0 or false  1 or true | 0.00  1.00 | Input / Output |
| Is Moving | 0  1 | false  true | 0.00  1.00 | Output |
| Pan Left | 0  momentary 1 | false  momentary true | 0.00  momentary 1.00 | Input / Output |
| Pan Left / Tilt Down | 0  momentary 1 | false  momentary true | 0.00  momentary 1.00 | Input / Output |
| Pan Left / Tilt Up | 0  momentary 1 | false  momentary true | 0.00  momentary 1.00 | Input / Output |
| Pan Right | 0  momentary 1 | false  momentary true | 0.00  momentary 1.00 | Input / Output |
| Pan Right / Tilt Down | 0  momentary 1 | false  momentary true | 0.00  momentary 1.00 | Input / Output |
| Pan Right / Tilt Up | 0  momentary 1 | false  momentary true | 0.00  momentary 1.00 | Input / Output |
| Pan Speed | 0**.**000 to 1 | 0 to 1.00 | 0 to 1.00 | Input / Output |
| Privacy Mode | 0  1 | 0 or false  1 or true | 0.00  1.00 | Input / Output |
| Recalibrate PTZ | 0  1 | 0 or false  1 or true | 0.00  1.00 | Input / Output |
| Recall Speed | 0 to 1.00 | 0 to 1.00 | 0.00 to 1.00 | Input / Output |
| Save Home | 0  1 | 0 or false  1 or true | 0.00  1.00 | Input / Output |
| Save Privacy | 0  1 | 0 or false  1 or true | 0.00  1.00 | Input / Output |
| Speed By Zoom | 0 to 1.00 | 0 to 1.00 | 0.00 to 1.00 | Input / Output |
| Tilt Down | 0  momentary 1 | false  momentary true | 0.00  momentary 1.00 | Input / Output |
| Tilt Speed | 0 to 1.00 | 0 to 1.00 | 0.00 to 1.00 | Input / Output |
| Tilt Up | 0  momentary 1 | false  momentary true | 0.00  momentary 1.00 | Input / Output |
| Zoom In | 0  momentary 1 | false  momentary true | 0.00  momentary 1.00 | Input / Output |
| Zoom Out | 0  momentary 1 | false  momentary true | 0.00  momentary 1.00 | Input / Output |
| Zoom Speed | 0 to 1.00 | 0 to 1.00 | 0.00 to 1.00 | Input / Output |
| Video Format | | | | |
| Imaging Frame Rate (Hz) | N/A | Camera model-dependent. See "Controls" section for valid choices. | N/A | Input / Output |
| SDI Level A/B | 0  1 | no  yes | 0.00  1.00 | Input / Output |
| SDI/HDMI Enable | 0  1 | no  yes | 0.00  1.00 | Input / Output |
| SDI/HDMI Format | N/A | Camera model-dependent. See "Controls" section for valid choices. | N/A | Input / Output |
| SDI/HDMI Mode | 0  1 | no  yes | 0.00  1.00 | Input / Output |
| White Balance | | | | |
| Auto Blue Gain | 1 to 255 | 1 to 255 | 0.00 to 1.00 | Input / Output |
| Auto Red Gain | 1 to 255 | 1 to 255 | 0.00 to 1.00 | Input / Output |
| AWB One Push | 0  1 | 0 or false  1 or true | 0.00  1.00 | Input / Output |
| AWB Sensitivity | N / A | Low, Mid, High | N/A | Input / Output |
| Hue | 0 to 14 | 0 to 14 | 0, .071, .143, .214, .286, .357, .429, .500, .571, .643, .714, .786, .857, .929, 1.00 | Input / Output |
| Manual Blue Gain | 1 to 5000 | 1 to 5000 | 0.00 to 1.00 | Input / Output |
| Manual Red Gain | 1 to 5000 | 1 to 5000 | 0.00 to 1.00 | Input / Output |
| Mode | N / A | Auto, Manual, Indoor/3000K, Outdoor/5000K, One Push | N/A | Input / Output |

[Video Status](javascript:void(0))

The following control pins are available when the Status component or the USB Video Bridge component is selected.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| IP Streams 1 and 2 | | | | |
| Bitrate | 0.0000 and up | 0.0000 and up | 0.00 to 1.00 | Output |
| FPS | 0 to 30 | 0 to 30 | 0.00 to 1.00 | Output |
| Frame Count | 0 and up | 0 and up | 0.00 to 1.00 | Output |
| Packet Count | 0 and up | 0 and up | 0.00 to 1.00 | Output |
| Packet Loss Percentage | 0.00 to 100 | 0.00% to 100% | 0.00 to 1.00 | Output |
| Packets Lost | 0 and up | 0 and up | 0.00 to 1.00 | Output |
| Test Stream 1, 2 | 0  1 | false  true | 0  1.00 | Input / Output |
| USB | | | | |
| Active | 0  1 | false  true | 0  1.00 | Output |
| Bitrate | 0.0000 and up | 0 and up | 0.00 to 1.00 | Output |
| Bridge Name | (text) | | | Output |
| Encoding | (text) | | | Output |
| FPS | 0 to 30 | 0 to 30 | 0.00 to 1.00 | Output |
| SRC- | 0 and up | 0 and up | 0.00 to 1.00 | Output |
| SRC+ | 0 and up | 0 and up | 0.00 to 1.00 | Output |
| USB Speed | (text) | | | Output |
| Video Format | (text) | | | Output |
| Input Active | 0  1 | false  true | 0  1.00 | Output |
| Input Connection | (text) | | | Output |
| Reset | 0  1 | 0 or false  1 or true | 0.00  1.00 | Input / Output |

[Troubleshooting](javascript:void(0))

### "USB Device Not Recognized"

If you see this Windows pop-up message, it means that you've connected a TSC-G3 Series touch screen to the host PC but do not have the TSC-G3 USB Video Bridge or USB Audio Bridge enabled and included in a running design. To resolve, follow the steps in the [Configuration Overview](#ConfigOverview) section.

### No video or distorted video

If you have changed the [Video Formats](#Video) property to a YUY2-only format and video is either no longer being received by the host application or is distorted, try reverting to the default UC&C Formats option. If the video begins working again, there might be an issue with the USB connection.

**Note:** YUY2-only formats require a USB 3.0 connection for all formats greater than 360p. The USB cable and host USB port must be USB 3.0 capable. See [USB Connection Requirements](#USB) for other requirements.

### Camera controls in UCIs

When creating a User Control Interface (UCI) for camera control, if you drag the camera controls from the USB Video Bridge into the UCI, those controls will control ONLY the currently active camera on the USB Video Bridge. If you drag the controls from a camera into a UCI, those controls will ONLY control that camera regardless if it is active or not.
