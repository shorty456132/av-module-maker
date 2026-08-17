# Media Display

> Source: https://help.qsys.com/Content/Schematic_Library/media_display.htm

# Media Display

The Media Display feature supports live video preview from Q-SYS cameras within a User Control Interface (UCI) on supported Q-SYS devices, as well as the display of JSON-encoded URL image content within a UCI.

## Display camera preview video within a UCI

Displaying Q-SYS camera live preview video on a supported Q-SYS device is as easy as dragging and dropping the Preview control from the camera's Status/Control component (or downstream USB Video Bridge) into your UCI.

[Device Support and Requirements](javascript:void(0))

### Cameras

All Q-SYS camera models, including the PTZ-IP Series and NC Series cameras, are capable of sending their Preview Streams to a UCI. You must enable the Preview Stream in either the camera's Status/Control or connected USB Video Bridge component:

1. In your design, double-click the camera's Status/Control component or USB Video Bridge component.
2. Click the Mediacast Streams tab.
3. For Preview Stream, click Enable.

**Note:** If Preview Stream is not enabled, live video preview defaults to a 1x per second refresh rate. For more information about the Preview Stream, see the [Status/Control (Cameras)](onvif_camera_operative.htm) or [USB Video Bridge](usb_uvc.htm) topics.

### Touch Screens and Apps

Live preview video is supported by all [Q-SYS Products](../Hardware/Hardware_Overview.htm#TSC_Series_Gen_3) touch screen models, [Microsoft Teams Room (MTR)](spe_uci.htm), and the [UCI Viewer App (Windows)](uci_viewer_app.htm) app for Windows. All platforms support the display of 30 fps (frame per second) live camera preview streams and 1 fps camera preview images.

* TSC Series Gen 3 touchscreen controllers support up to two unique simultaneous camera live preview video streams.
* The UCI Viewer app also supports up to two unique simultaneous live preview streams. Multiple instances of the same preview stream can be displayed without exceeding the count for unique live preview streams. These limits are enforced within each User Control Interface (UCI).
* There is no enforced limit on 1 fps images; however, UCI performance and network traffic may be affected while using a large number of them.
* Web based UCI viewers, excluding the UCI Viewer Windows App and the Q-SYS Control App (iOS), only support 1 fps images.

### Multicasting

Live video preview streaming requires that multicasting is allowed and properly configured on your network. See [Q-SYS Networking Requirements](../Networking/Q-SYS_Networking.htm).

[Configuration Overview](javascript:void(0))

1. Within your design schematic, double-click your camera's Status/Control component or downstream USB Video Bridge Component.
2. Either copy and paste or drag the Preview control screen into your UCI.
3. Within your UCI, click the Preview control.
4. Configure the [Media Display Properties](#Media2).
5. Save and run your design to the Core.

[Media Display Properties](javascript:void(0))

#### Priority

Each video Preview control within your UCI is assigned a priority. Adjusting this property is only necessary when you have more than one Preview control (each from a different Q-SYS camera) in a UCI page.

* Automatic: (Default) This is the lowest priority. At design startup, a Preview control with Automatic priority will decode live video only if other Media Displays with higher priority are not currently streaming live video.
* Preferred: This is the middle priority. At design startup, a Preview control with Preferred priority will decode live video after those with Fixed priority and before those with Automatic priority.
* Fixed: This is the highest priority. At design startup, a Preview control with Fixed priority will decode live video before those with other priorities.

**Note:** Switching to a different UCI page causes a re-evaluation of priorities based on the visible Preview controls on the page.

#### Touch Behavior

This property determines whether a user tapping the video Preview control within the UCI will request a live stream from the camera.

* None: (Default) Tapping the Preview control has no effect.
* Start: Tapping the Preview control will request that this Preview control should receive the live video stream. For Preview controls with either Automatic or Preferred priority, a touch event will "steal" live video from other Preview controls with Automatic or Preferred priority. For Preview controls with Fixed priority, a touch event can steal video from those with any priority.

**Note:** When tapping a Preview control, live video may or may not be available depending on the device displaying the UCI (see [Device Support and Requirements](#Device)) and the configured Priority property.

## Display URL image content within a UCI

Use the Media Display control Presentation to convert a JSON-encoded URL into media content that can be shown within a User Control Interface (UCI). This is useful for displaying media content that updates frequently.

[Media Support](javascript:void(0))

Currently, Media Display can show a PNG, JPEG, or GIF image in its original aspect ratio and can be optionally refreshed based on a set number of seconds. Video is not supported.

[Requirements](javascript:void(0))

### URL Requirements

* The specified media URL must be accessible to the device on which the UCI is displayed â TSC touch panel, PC running Windows UCI Viewer, etc.
* The URL must support secure HTTPS if the UCI will be viewed in Core Manager or Q-SYS Reflect.
* Only a single URL is currently supported.

### JSON Parameters

The JSON code must be in this format:

```lua
{  
  "Protocol": "Image",  
  "URLs": [ "https://<myurl>" ],  
  "ImageTimeSeconds": 1.0  
}
```

Where:

* `"Protocol"` : Always `"Image"`. No other format is supported.
* `"URLs"` : A URL that includes a supported media type.
* `"ImageTimeSeconds"` : Optional. A double value that specifies how often, in seconds, the image is refreshed â for example, `2.0`, `4.5`, `0.5`. If omitted, the URL will load once when the UCI starts.

[Configuration Overview](javascript:void(0))

1. Create a text edit control â for example, with [Custom Controls](custom_controls.htm) â and drag the new control it into the schematic. The Text Field Presentation will default to Text Field.
2. Press F6 to emulate the design.
3. Click the control text box and paste the JSON code for the media URL into the text box. Press Enter.
4. Press F7 to stop emulation.
5. Select the control text box again and change its Presentation in Properties to Media Display. If the URL is valid and contains a compatible media type, the text box changes to the media.
6. Drag the control into your UCI.

[Schematic Example](javascript:void(0))

In this example, a Custom Controls component is configured with a Text edit control. The control contains the JSON-encoded media URL and has been dragged into the schematic twice: the top text box presentation is Text Field while the bottom is Media Display. The JSON specifies to display the image located at "https://placecats.com/300/200" with an image refresh every second.

[Troubleshooting](javascript:void(0))

### "No imaging component suitable to complete this operation was found"

If the text box is displaying this message, it means that the referenced URL is not displaying a supported media type. See [Media Support](#Media).
