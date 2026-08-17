# Video > Video Endpoints

> Source: https://help.qsys.com/Content/Reflect/System_Management/Video_Endpoints.htm

# Video > Video Endpoints

Use the Video Endpoints page to manage image content, idle screen settings, and EDID files for the NV Series devices in your design. At least one NV Series must be present in the running design for these properties to appear.

**Note:** Q-SYS Designer Software versions 9.7.0 and later include high resolution default images for Graphic 2, Graphic 3, and Idle Screen. Custom, uploaded images are retained when upgrading to 9.7.0 and later. However, if your pre-9.7.0 design currently uses default images and you would like to use the new high resolution default images in 9.7.0 and later, simply upload and then remove a custom image to refresh the defaults.

**Tip:** Video Endpoint image files are stored and updated within the running design file. Load and save the design in Q-SYS Designer Software to capture any updates to image files.

## Graphics

#### Core Disconnected Image

Select what image can appear on a connected HDMI display when the NV Series does not currently have a network connection to the Q-SYS Core processor.

* Boot Screen: Displays the device name (as selected in Q-SYS Configurator), firmware version, model, and LAN interface information â MAC address and cable state.
* Graphic 1, 2, 3: Displays a graphic image, as selected in the Images section.

#### Graphic 1, 2, 3

Select what images can appear on a connected HDMI display when "Graphic *n*" is toggled in the HDMI I/O component (HDMI Output Source), or when "Graphic *n*" is configured in the Generic HDMI Display component's Idle Mode or Sleep Mode controls.

Click Upload Image to select a JPG file with a maximum size of 3 MB and a resolution of 1920x1200, 1920x1080, or 640x480.

**Tip:** Images with a 16:9 aspect ratio are recommended.

## Idle Screen

Use the Idle Screen tab to configure what image and text appears when "Idle Screen" is configured in the Generic HDMI Display component's Idle Mode or Sleep Mode controls. The Idle Screen is useful for providing guidance to users when no HDMI signal is detected.

Click Edit to adjust the settings.

[Dynamic Idle Screen 'Off'](javascript:void(0))

To simply display an Idle Screen image for all Video Endpoints with no custom text, set this option to 'Off'.

* Click  to select an image for upload. You can upload any JPEG image with a resolution up to 1920x1080, and with a width that is divisible by 16.
* Click  to delete the uploaded image and revert to the default "no signal detected" image.

[Dynamic Idle Screen 'On'](javascript:void(0))

When 'On', you can specify not only a background image, but also the current date and time, a company logo image, and custom text line to appear on all Video Endpoints whenever Idle Mode occurs. Additionally, you can select text to appear for individual Video Endpoints, such as the room name where the Video Endpoint is located and a technical support number.

#### Shared Settings

These options appear for all Video Endpoints in your design when Idle Mode begins.

* Type a Company Name, which can be a maximum of 64 characters.
* Select either a date Format from the menu or use a combination of [date and time specifiers](../Resources/MiniTopics/DateTimeSpecifiers.htm) to create a custom Format String.
* Enter a custom message, up to 64 characters, in the Text Line 1 field. This is the first of up to three lines of custom text you can enter. Text Line 1 is shared across all devices, while lines 2 and 3 are device-specific.
* Under Logo Image, click  to upload any company logo JPEG file with a resolution up to 300x300. Click  to remove the image.
* Under Background Image, click  to upload any JPEG file with a resolution up to 1920x1080. Click  to remove the image and revert to the default "no signal detected" image.

#### Device-Specific Settings

Select a Video Endpoint from the device list to adjust the text that appears for just that selected device. This text can provide guidance to room users for contacting the company's AV support should any problems occur.

* Specify a Room Name where the device is located.
* Specify a Support Number for users to call for AV support.
* Optionally specify custom text for Text Line 2 and Text Line 3, up to 64 characters.

Click Save when you are finished making changes.

## EDID Manager

Use the EDID Manager tab to view and manage QSC default and user-saved EDID files on the Q-SYS Core.

EDID files include properties for supported video resolutions, frame rates, number of audio channels, and audio formats. In an HDMI video design running on the Q-SYS Core, you select an EDID file in the Generic AV Source component's "EDID" control. That EDID file is applied to the HDMI source, which tells the source what video and audio formats are available.

**Tip:** Use EDID files to manage the video format sent to an NV Series. For example, selecting a 1080p EDID would prevent a 4K source from sending 4K video. The source would send 1080p video instead.

[User EDIDs](javascript:void(0))

This section contains EDID files that have either been saved with the Generic HDMI Display component's "Save EDID to Core" button or manually uploaded. All user EDID files use the .bin file extension.

#### Saving a Generic HDMI Display's EDID

To save an EDID file to the User EDID list:

1. In Q-SYS Designer, load a design from the Q-SYS Core containing a Generic HDMI Display component.
2. Double-click the Generic HDMI Display Component.
3. Click Save EDID to Core.

   **Note:** Each button press adds an incrementing filename number suffix â for example, VA2246SERIES.bin, VA2246SERIES(1).bin, VA2246SERIES(2).bin.

#### Uploading New EDID Files

1. Navigate to the Video Endpoints > EDID Manager page.
2. In the User EDIDs section, click  to select an EDID .bin file to upload. Files must be either 128 bytes (one block) or 256 bytes (two blocks) in size. EDID file names can include alphanumeric characters, spaces, underscores, dashes, periods, and parentheses.

#### Renaming an User EDID File

1. Navigate to the Video Endpoints > EDID Manager page.
2. In the User EDIDs section, select an existing EDID file, and then click .
3. Type a new EDID name. EDID file names can include alphanumeric characters, spaces, underscores, dashes, periods, and parentheses
4. Click Save Changes.

#### Downloading a User EDID File

To download a user EDID file from the Q-SYS Core to your PC:

1. Navigate to the Video Endpoints > EDID Manager page.
2. In the User EDIDs section, select an existing EDID file, and then click .
3. Select a location on your PC, and then click Save.

#### Deleting a User EDID File

1. Navigate to the Video Endpoints > EDID Manager page.
2. In the User EDIDs section, select an existing EDID file, and then click .

[QSC Default EDIDs](javascript:void(0))

This section contains EDID files included with Q-SYS Core firmware. These EDID files contain audio and video formats that are compatible with the NV Series system. All QSC default EDID files use the .qedid file extension.

To download a QSC default EDID file, select it, and then click .

**Note:** QSC default EDID files cannot be renamed or deleted from the Q-SYS Core.
