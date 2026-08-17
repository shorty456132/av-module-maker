# AV Stream Router

> Source: https://help.qsys.com/Content/Schematic_Library/av_router_class.htm

# AV Stream Router

Use the Video Router component to route multiple input AV streams to multiple destinations. This is especially useful for AV control of large systems featuring many Q-SYS Network Video Endpoints.

[Inputs and Outputs](javascript:void(0))

### Input Pins

#### AV Input

These pins receive incoming AV signals from the AV Output pins on [HDMI I/O (NV-32-H)](streamer_hdmi_switcher.htm) components configured as Encoders.

### Output Pins

#### AV Output

These pins send outgoing, routed AV signals to the AV Input pins on [HDMI I/O (NV-32-H)](streamer_hdmi_switcher.htm) components configured as Decoders.

[Schematic Example](javascript:void(0))

In this example, we have a very large conference room with three NV-32-H Encoders for attendees to connect HDMI sources, such as laptop PCs. On the wall are six large displays to show meeting content, each with a connected NV-32-H configured as a Decoder. Using the AV Stream Router, any AV stream from the Encoders can be routed to any Decoder and its display.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### AV Stream Router Properties

#### Input Count

Specify the number of incoming AV signals to route, from 1 to 256 (default is 8).

#### Output Count

Specify the number of outgoing AV connections, from 1 to 256 (default is 8).

#### Outputs per Tab

Select how many outputs are grouped into individual tabs, from 1 to 256 (default is 32).

#### Selection Controls

Select what type of controls are available in the AV Stream Router's control panel: Knobs + Buttons, Knobs only, or Auto (default). The Auto setting configures the control type based on the number of configured outputs, inputs, and the Outputs per Tab property. This is the recommended setting and provides the best balance between component performance and control type.

**Note:** If you select the Knobs + Buttons option and the resulting number of buttons is greater than 1024, you must reduce the number of outputs per tab, the output count, or input count.

[Controls](javascript:void(0))

#### Output *n* Select

The Knob control indicates what Input is currently being routed for the selected Output. You can also use the text box to specify the Input number to route to that Output.

#### Output *n* Input *n* Select

For each Output, click an Input's button to route it to that Output. Only one input can be active at a time for a given output. Depending on the number of Inputs and Outputs configured in Properties, Output buttons may not appear if the Selection Controls property is set to 'Auto'.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Output *n* | | | | |
| Input *n* Select | 0  1 | false  true | 0  1 | Input / Output |
| Select | 1 to 256 | 1 to 256 | - | Input / Output |
