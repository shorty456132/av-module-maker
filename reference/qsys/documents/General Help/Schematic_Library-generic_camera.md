# Status/Control (Cameras)

> Source: https://help.qsys.com/Content/Schematic_Library/generic_camera.htm

# Status/Control (Cameras)

The Q-SYS NC Series cameras (NC-12x80, NC-20x60, NC-110, NC-90-G2, NC-Pro15x) are part of the Q-SYS Audio Video Conferencing solution. This topic covers the controls for the Camera component in Q-SYS Designer Software.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### NC Properties

#### IP Streaming

This property determines the network streaming method for Q-SYS camera Mediacast Streams:

* Compiler Choice: (Default) Select this option to allow Q-SYS Designer Software to determine whether unicast (point-to-point) or multicast (one-to-many) is best for your configuration. This is the recommended option.
* Unicast Only: Select this option when your design contains point-to-point camera video routing, meaning that each camera output pin can be connected to no more than two bridging peripherals in your design.
* Multicast Only: Select this option when your design contains one-to-many camera video routing, meaning that a camera video output pin is connected to more than two bridging peripherals in your design.

**Note:** Multicast streaming requires that the network switch infrastructure be correctly configured to support IGMPv2. For all networking requirements, see the [Q-SYS Networking Requirements](../Networking/Q-SYS_Networking.htm) section. Configure camera multicast address assignment in Q-SYS Core Manager. By default, Q-SYS automatically provisions multicast streaming addresses for Cameras, AES67 Transmitters, and Video Endpoints. For more information, see the Core Manager > [Network > Multicast](../Core_Manager/Core_Management/Multicast.htm) topic.

#### Max ePTZ Zoom (NC-110 & NC-90-G2)

As with any digital zoom device, increased zoom results in a noisier image due to the cropping and scaling involved in the processing. Use this control to set a maximum digital zoom used by the connected camera. Based on the model, the set value must be between:

* NC-110: 3 and 8 with a default of 4.
* NC-90-G2: 3-5 with a default of 4.

**Note:** The default of 4 affects old and new design files. For previously saved projects, either update your snapshots with the new Max ePTZ Zoom setting, or set it to 8 to retain the saved functionality.

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

[Status Tab](javascript:void(0))

### Status

#### IP Streaming

This LED illuminates if the camera is actively streaming video over the network.

#### ID

Press to identify the camera. The Status LED on the camera's front panel blinks green when in ID mode. Press again to turn off.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

### Network

#### IP Address

This displays the IP Address of the camera.

#### Flow Control

Ethernet Flow Control can be enabled for each NC Camera in its Status tab. When enabled, and the camera is connected to an Ethernet Switch port that has Flow Control Auto-Negotiation enabled, the camera will enable transmit and receive Flow Control to help reduce buffer overruns.

#### Traffic Shaping

*(For NC cameras only)* When this button is turned on, the cameraâs network traffic is spread out over the duration of the video frame reducing buffer overruns in network switches.

### Hardware Details

These controls are all read-only.

#### Model

The Q-SYS camera model number â for example, NC-110.

#### MAC Address

The camera's MAC address, as shown on the product label â for example, 00:60:74:00:00:99.

#### Serial Number

The camera's serial number, as shown on the product label â for example, H4021QXXX.

#### Camera FW Version

This is the firmware version running on a PTZ-IP Series camera. This control is not applicable to NC Series cameras.

**Note:** The following sections apply to the NC-Pro15x cameras.

### Tally Light

The tally LEDs are lights located on both the front and rear of the lens of the camera, and can be controlled to light up when the camera is actively âon airâ or recording/streaming live. The tally LED is designed to give a clear, visible indication to performers, presenters, or production crew so everyone knows which camera is live (or will become live).

#### Strength

Changes the brightness of the LED. Options are Weak, Medium, Strong.

#### Preview

Changes the LED to Green. This indicates the camera is queued up to go live next.

This helps camera operators frame, focus, and prepare without rushing.

#### Program

Changes the LED to Red. This indicates the camera is currently live/on-air.

This ensures presenters know where to look and operators avoid adjusting a shot thatâs on air.

**Note:** If both Preview and Program are enabled, the Program state takes priority and the LED is red.

### Firmware

**Note:** The NC-Pro-15x does not support Q-SYS Designer automatic firmware updates. Instead, firmware updates must be performed manually through the NC-Pro15x firmware upgrade controls.

#### Needs Upgrade

Indicates if a firmware update is available for the NC-Pro15x camera.

#### Firmware Version

Indicates the currently installed firmware version on the camera.

#### Force Downgrade

Enabling allows firmware to be downgraded on the camera.

**CAUTION:** Force Downgrade will Reset All Camera Settings. Data Migration for downgrading is not supported, so user settings are reset to defaults.

#### Program Firmware

Pressing begins the available firmware update.

**WARNING:** Do not disconnect power while updating. This will interrupt the update and damage the camera.

[Auto Framing Tab](javascript:void(0))

Auto-Framing is a feature that runs on the actual NC-110 and NC-PTZ camera CPUs. When enabled, video analytics in the cameras are used to more tightly âframeâ the faces found within the cameraâs actual field of view (FoV).

On NC-110 cameras, the entire camera FoV is analyzed, whereas on the NC-PTZ cameras, the current mechanical FoV is analyzed. As such, QDS preview images will only show the entire FoV instead of a zoomed view for the NC-110.

**Note:** When any of the Auto Framing controls (Enable, Face Count, or Outline Faces) are enabled, the JPEG previews in Q-SYS Designer and on TSC UCIs will only show full FoV. These preview types cannot show the auto framed FoV. Live previews available on devices such as TSC-G3 series will show auto framed FoV, just like the primary Mediacast stream.

### Auto Framing

**Note:** This tab is not visible on downstream Bridges or Controls, it is only visible on the individual camera control tabs.

**Tip:** Any time the **Auto-Framing Enable button**, **Face Count Button**, or **Outline Faces button** is enabled, *HDMI/SDI* get disabled on NC-PTZ cameras. Likewise, when you enable *HDMI/SDI*, all three buttons will be disabled.

#### Enable

When set to enable, this function controls the ePTZ Auto-Framing functionality. The default is disabled.

#### Frame Padding

This allows you to select the space left around the faces detected in the camera's field of view (FoV). This integer knob offers a range of sizes 1 to 15. A lower value results in tighter crop, higher value results in looser crop.

#### Deadband

This allows you to tune the tolerance for reframing when faces change position in the current cropped frame. This integer knob offers a range of sizes 1 to 15. A lower value results in lower tolerance, higher value results in higher tolerance.

**Note:** Deadband and Frame Padding should be used as relative tuning controls for personal preference. Deadband region is bound with respect the to Frame Padding. Variations in camera model max FoV introduce some error in the region calculation when a given frame is cropped.

**Tip:**  A smaller deadband region paired with a smaller frame padding is useful when you want tight tracking on a single face. A larger deadband region paired with a larger frame padding is useful when you want simple framing of multiple faces.

#### Transition Speed

Sets the transition speed for moving the image when new faces are added or faces are dropped. This dropdown offers **Instant**, **Slow**, **Medium**, and **Fast**. The default option is **Medium**.

* **Instant**: No transition time, the image is immediately updated to reflect the faces found in the camera FoV.
* **Slow**, **Medium**, **Fast**: Sets the transition speed to a new FoV is gradually changed based on this setting.

#### Face Count Button

This button allows you to turn **On** or **Off** the button. The default is **Off**.

* When it is set to **On**: Face Count control is enabled and active. The camera's analytics are enabled. The camera's face count is polled. When turned on, this turns off the NC-PTZ *HDMI/SDI Enable* button, disabling the camera's HDMI/SDI output.
* When it is set to **Off**: Face count control is grayed out and disabled. Camera's face count is not polled.

#### Face Count (Integer read-only status)

This is a read-only field. This value is grayed out / disabled when **Face Count Enable** button is **Off**. The default is **Off**.

#### Outline Faces (Beta)

This button allows you to turn **On** or **Off** the button. The default is **Off**.

When it is set to **On**: Faces detected in the camera's FoV will be outlined in a green box to aid in finding issues in the scene or its Auto-Framing operation.

When it is set to **Off**: Face will not be detected and the feature is disabled.

[AI Tab](javascript:void(0))

This tab is available on the NC-90-G2.

### Auto Framing

#### Enable

When set to enable, this function controls the ePTZ Auto-Framing functionality. The default is disabled.

#### Frame Padding

This allows you to select the space left around the faces detected in the camera's field of view (FoV). This integer knob offers a range of sizes 1 to 15. A lower value results in tighter crop, higher value results in looser crop.

#### Deadband

This allows you to tune the tolerance for reframing when faces change position in the current cropped frame. This integer knob offers a range of sizes 1 to 15. A lower value results in lower tolerance, higher value results in higher tolerance.

**Note:** Deadband and Frame Padding should be used as relative tuning controls for personal preference. Deadband region is bound with respect the to Frame Padding. Variations in camera model max FoV introduce some error in the region calculation when a given frame is cropped.

**Tip:**  A smaller deadband region paired with a smaller frame padding is useful when you want tight tracking on a single face. A larger deadband region paired with a larger frame padding is useful when you want simple framing of multiple faces.

#### Transition Speed

Sets the transition speed for moving the image when new faces are added or faces are dropped. This dropdown offers **Instant**, **Slow**, **Medium**, and **Fast**. The default option is **Medium**.

* **Instant**: No transition time, the image is immediately updated to reflect the faces found in the camera FoV.
* **Slow**, **Medium**, **Fast**: Sets the transition speed to a new FoV is gradually changed based on this setting.

#### Face Count Button

This button allows you to turn **On** or **Off** the button. The default is **Off**.

* When it is set to **On**: Face Count control is enabled and active. The camera's analytics are enabled. The camera's face count is polled. When turned on, this turns off the NC-PTZ *HDMI/SDI Enable* button, disabling the camera's HDMI/SDI output.
* When it is set to **Off**: Face count control is grayed out and disabled. Camera's face count is not polled.

#### Face Count (Integer read-only status)

This is a read-only field. This value is grayed out / disabled when **Face Count Enable** button is **Off**. The default is **Off**.

#### Outline Faces (Beta)

This button allows you to turn **On** or **Off** the button. The default is **Off**.

When it is set to **On**: Faces detected in the camera's FoV will be outlined in a green box to aid in finding issues in the scene or its Auto-Framing operation.

When it is set to **Off**: Face will not be detected and the feature is disabled.

### Active Speaker Framing

#### Enable

When enabled, the camera automatically frames the person speaking in the room. When no one is speaking, it defaults back to a wide room view so remote participants can see the full space. If multiple people speak at once, both are framed.

#### Hold Time

Use to set how long the camera holds the current in-room talker before framing the new talker.

#### Transition Speed

Sets how quickly the camera pans/tilts to a new talker or back to the wide view.

#### Far End Audio Detect

Indicates when far end audio is detected.

#### In-Room Release Time

The release time is used to set how long the camera holds the last in-room talker while the far end audio detect led is high (far end person is speaking) before falling back to room view.

### Tile View

#### Enable

When activated, Tile View displays every person in the room in their own box (cell), making it easy to see all participants. The active speakerâs tile is outlined so remote attendees know who is talking.

#### Room View

* Room View Enabled : Up to 7 participants + room view (8 total cells)
* Room View Disabled : Up to 9 participants without room view

**Note:** Expected Behavior if number of in-room participants is over the max : The NC-90-G2 falls back to room view.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Coordinates | (text) | | | Output |
| Firmware Build | (text) | | | Output |
| Firmware Selector |  |  |  | Input / Output |
| Firmware Version | (text) | | | Output |
| Auto Framing | | | | |
| Deadband | 0  1 | off  on | 0.00  1.00 | Input / Output |
| Enable | 0  1 | no  yes | 0.00  1.00 | Input / Output |
| Face Count | 0  1 | off  on | 0.00  1.00 | Output |
| Face Count Enable | 0  1 | off  on | 0.00  1.00 | Input / Output |
| Frame Padding | 0  1 | off  on | 0.00  1.00 | Input / Output |
| Outline Faces Enable | 0  1 | no  yes | 0.00  1.00 | Input / Output |
| Transition Speed | (text) | | | Input / Output |
| Camera | | | | |
| Camera Reset | 0  momentary 1 | false  momentary true | 0.00  momentary 1.00 | Input / Output |
| Exposure | | | | |
| Anti-Flicker | 0  1 | off  on | 0.00  1.00 | Input / Output |
| Backlight Comp | 0  1 | no  yes | 0.00  1.00 | Input / Output |
| Compensation | -7 to +7 | -7 to 7 | 0, .071, .143, .214, .286, .357, .429, .500, .571, .643, .714, .786, .857, .929, 1.0 | Input / Output |
| Dynamic Range | 0 to 8 | 0 to 8 | .125, .250, .375, .500, .625, .750, .875, 1.00 | Input / Output |
| Gain | 0 to 7 | 0 to 7 | 0, .143, .286, .429, .571, .714, .857, 1.00 | Input / Output |
| Gain Limit | 0 to 15 | 0 to 15 | 0, .067, .133, .200, .267, .333, .400,. 467, .533, .600, .667, .733, .800, .867, .933, 1.00 | Input / Output |
| Mode | N / A | off, auto, or manual | N / A | Input / Output |
| Shutter | 30, 60, 90, 100, 125, 180, 250, 350, 500, 725, 1000, 1500, 2000, 3000, 4000, 6000, 10000 | 1/30, 1/60, 1/90, 1/100, 1/125, 1/180, 1/250, 1/350, 1/500, 1/725, 1/1000, 1/1500, 1/2000, 1/3000, 1/4000, 1/6000, 1/10000 | 0, .083, .167, .250, .333, .417, .500, .583, .667, .750, .833, .917, 1.00 | Input / Output |
| Firmware | | | | |
| Firmware Version | (text) | | | Output |
| Force Downgrade | 0  1 | false  true | 0.00  1.00 | Input / Output |
| Needs Upgrade | 0  1 | false  true | 0.00  1.00 | Output |
| Program Firmware | 0  1 | false  true | 0.00  1.00 | Input / Output |
| Upload | 0  1 | false  true | 0.00  1.00 | Input / Output |
| Focus | | | | |
| AF | 0  1 | false  true | 0.00  1.00 | Input / Output |
| AF Zone | N / A | center, bottom, top, face | N / A | Input / Output |
| In | 0  1 | false  true | 0.00  1.00 | Input / Output |
| Manual Speed | 0.001 to 0.100 | .001 to .100 | 0.001 to 0.100 | Input / Output |
| Out | 0  1 | false  true | 0.00  1.00 | Input / Output |
| Sensitivity | N / A | Low, Normal, High | N / A | Input / Output |
| FreeD | | | | |
| FreeD Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| FreeD Toggle | 0  1 | false  true | 0.00  1.00 | Input / Output |
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
| Streaming Mode Format | N / A | Auto  h.264 640x360  h.264 480x270  h.264 320x180 | N / A | Input / Output |
| Streaming Mode Frame Rate | 1 to 30 | 1 to 30 | 0.000 to 1.00 | Input / Output |
| Video Format | (text) | | | Output |
| Network | | | | |
| Flow Control | 0  1 | off  on | 0  1 | Input /  Output |
| IP Address | (text) | | | Output |
| Traffic Shaping | 0  1 | off  on | 0  1 | Input / Output |
| Noise Reduction | | | | |
| 3D NR | 0  1 | off  on | 0.00  1.00 | Input / Output |
| 3D NR Enable | 0  1 | no  yes | 0.00  1.00 | Input / Output |
| Pan-Tilt-Zoom | | | | |
| Ceiling Mount | 0  1 | no  yes | 0.00  1.00 | Input / Output |
| Coordinates | N / A | **P**an = -0.9936 to 0 to +0.9936  **T**ilt = -0.9936 to 2.9808  **Z**oom = 0.000000 to 1  **F**ocus = 0.00000 to 1  The coordinates are entered in the above order, separated by a space. | N / A | Input / Output |
| Home | 0  1 | 0 or false  1 or true | 0.00  1.00 | Input / Output |
| Is Moving | 0  1 | false  true | 0.00  1.00 | Output |
| Move Completed | 0  1 | false  true | 0.00  1.00 | Output |
| Pan Left | 0  momentary 1 | false  momentary true | 0.00  momentary 1.00 | Input / Output |
| Pan Left / Tilt Down | 0  momentary 1 | false  momentary true | 0.00  momentary 1.00 | Input / Output |
| Pan Left / Tilt Up | 0  momentary 1 | false  momentary true | 0.00  momentary 1.00 | Input / Output |
| Pan Right | 0  momentary 1 | false  momentary true | 0.00  momentary 1.00 | Input / Output |
| Pan Right / Tilt Down | 0  momentary 1 | false  momentary true | 0.00  momentary 1.00 | Input / Output |
| Pan Right / Tilt Up | 0  momentary 1 | false  momentary true | 0.00  momentary 1.00 | Input / Output |
| Pan Speed | 0**.**000 to 1 | 0 to 1.00 | 0 to 1.00 | Input / Output |
| Privacy Mode | 0  1 | 0 or false  1 or true | 0.00  1.00 | Input / Output |
| Recalibrate PTZ | 0  1 | o or false  1 or true | 0.00  1.00 | Input / Output |
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
| Standby | | | | |
| Mode | 0  1 | 0 or false  1 or true | 0.00  1.00 | Input / Output |
| Status | | | | |
| HW | | | | |
| MAC Address | (text) | | | Output |
| Model | (text) | | | Output |
| S/N | (text) | | | Output |
| Identify | 0  1 | 0 or false  1 or true | 0.00  1.00 | Input / Output |
| IP Streaming | 0  1 | 0 or false  1 or true | 0.00  1.00 | Output |
| Status Bar | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Tally | | | | |
| Preview | 0  1 | 0 or false  1 or true | 0.00  1.00 | Input / Output |
| Program | 0  1 | 0 or false  1 or true | 0.00  1.00 | Input / Output |
| Strength | N/A | Weak  Medium  Strong | N/A | Input / Output |
| Tile View | | | | |
| Enable | 0  1 | 0 or false  1 or true | 0.00  1.00 | Input / Output |
| Room View Enable | 0  1 | 0 or false  1 or true | 0.00  1.00 | Input / Output |
| Video Format | | | | |
| Apply Frame Rate | 0  1 | no  yes | 0.00  1.00 | Input / Output |
| Imaging Frame Rate | N / A | Camera model-dependent. See "Controls" section for valid choices. | N / A | Input / Output |
| SDI Level A/B | 0  1 | no  yes | 0.00  1.00 | Input / Output |
| SDI/HDMI Enable | 0  1 | no  yes | 0.00  1.00 | Input / Output |
| SDI/HDMI Format | N / A | Camera model-dependent. See "Controls" section for valid choices. | N / A | Input / Output |
| SDI/HDMI Mode | 0  1 | no  yes | 0.00  1.00 | Input / Output |
| White Balance | | | | |
| Auto Blue Gain | 1 to 255 | 1 to 255 | 0.00 to 1.00 | Input / Output |
| Auto Red Gain | 1 to 255 | 1 to 255 | 0.00 to 1.00 | Input / Output |
| AWB One Push | 0  1 | 0 or false  1 or true | 0.00  1.00 | Input / Output |
| Hue | 0 to 14 | 0 to 14 | 0, .071, .143, .214, .286, .357, .429, .500, .571, .643, .714, .786, .857, .929, 1.00 | Input / Output |
| Manual Blue Gain | 1 to 5000 | 1 to 5000 | 0.00 to 1.00 | Input / Output |
| Manual Red Gain | 1 to 5000 | 1 to 5000 | 0.00 to 1.00 | Input / Output |
| Mode | N / A | Auto, Manual, Indoor/3000K, Outdoor/5000K, One Push | N / A | Input / Output |
