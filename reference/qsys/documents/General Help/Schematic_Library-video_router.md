# Mediacast Router

> Source: https://help.qsys.com/Content/Schematic_Library/video_router.htm

# Mediacast Router

Use the Mediacast Router component to route multiple Mediacast streams to multiple destination Mediacast-capable devices. For example, you might want to see more than one camera on a single USB Video Bridge and switch between them. Or, you might want to create a design that handles video distribution for divisible or multipurpose room types.

**Tip:** The Mediacast Router configuration can easily be added to a [Snapshot Bank](snapshot_bank.htm) for a simple and intuitive way to create presets.

[Supported Q-SYS Devices](javascript:void(0))

### Devices that send Mediacast streams

* [NC-12x80, NC-20x60 PTZ Conference Cameras](../Hardware/Video/NC-PTZ.htm)
* [NC-110 Conference Camera](../Hardware/Video/NC-110.htm)
* [NC-90-G2 Network ePTZ Camera](../Hardware/Video/NC-90-G2.htm)

### Devices that receive Mediacast streams

* Any Q-SYS device with a USB Video Bridge. Refer to the [USB Video Bridge](usb_uvc.htm) topic to see a list of supported hardware.

[Inputs and Outputs](javascript:void(0))

#### Input *n*

These pins receive incoming Mediacast streams from the Video Output pins of Mediacast-capable components.

#### Output *n*

This pins send outgoing, routed Mediacast streams to the Video Input pins of Mediacast-capable components.

[Schematic Example](javascript:void(0))

In this example, the Mediacast streams from four Q-SYS cameras can be routed to any of the USB Video Bridge-capable devices in the design â in this case, a Core Nano and an IO-USB Bridge.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Mediacast Router Properties

#### Input Count

Sets the number of input pins to receive Mediacast streams, from 1 to 255. The default is 2.

#### Output Count

Sets the number of output pins from which to send Mediacast streams, from 1 to 50. The default is 1.

#### Image Buttons

When set to Yes, the image that the camera is producing is displayed on the button. The default is No.

[Controls](javascript:void(0))

#### Output *n* Select

The combo box indicates what Input is currently being routed for the selected Output. You can also specify the Input number to route to that Output.

#### Output *n* Input *n* Select

For each Output, click an Input's button to route it to that Output. Only one input can be active at a time for a given output.

#### Preview Window

Displays the Preview of each of the outputs. You can then drag a Media Display preview from each of the outputs into UCIs to allow live video capable rendering devices to display the live video.

#### Source

Displays the Source of the output pin. You can choose between 1 and 50.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Output *n* | | | | |
| Input *n* Select | 0  1 | false  true | 0  1 | Input / Output |
| Select | 1 to 255 | 1 to 255 | - | Input / Output |
