# Custom Controls Component

> Source: https://help.qsys.com/Content/Schematic_Library/custom_controls.htm

# Custom Controls

The Custom Controls component allows you to create a component with various types of Controls that can be used to control other components in your design through use of the Control Pins.

* The Custom Controls component has only Control Pin Input and Output, no audio inputs or outputs.
* You can create a Custom component with the type and number of controls you want.
* Controls of the same type are in Groups. You cannot have duplicate Groups in the same Component.
* You can have up to 10 different types, or Groups, of controls.
* Each Group can have up to 32 controls (of the same type).
* Each Group can have a different number of controls.
* You can give a label to the Custom Controls component by selecting the component in the Schematic and simply start typing and press enter or click off of the component when you're finished. You cannot "edit" the label once it has been entered, but you can replace the label in the same way it was entered initially.

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Custom Controls Properties

#### Type

Selects the type of control for the Group.

Initially, there is only one Group visible. When you select a Type for the first Group, a second Group is displayed, and so on until you have 10 Groups.

When you select a Type, Control Pins for each control of that Type, display below the Component in the Schematic, and below the Properties in the Control Pins Section.

#### Count

Selects the number of controls for the Group. Each Group can have a different Count. The options are 1 to 32.

#### Default Range Message

Some of the Control Types have variable ranges. This message gives the default range for the specific Control. If there is no range, as with a Toggle Button, there is no message.

#### Customize Range

Specifies if you want to customize the Control's range or not.

#### Minimum

If you set the Customize Range to Yes, enter the minimum of the desired range.

#### Maximum

If you set the Customize Range to Yes, enter the maximum of the desired range.

[Controls](javascript:void(0))

The available Controls are listed in the [Available Controls, and Ranges](#Available_Controls,_and_Ranges) table under Properties. Their individual functions depend on how you use them. In some cases, the ranges of the Controls can be customized.

### Available Controls, and Ranges

| Type | Default / Range | Custom | |
| --- | --- | --- | --- |
| Minimum | Maximum |
| Distance knob  (meters) | 0 to 100 | 0 | 999 |
| Frequency knob  (Hz) | 20 to 20000 | 0.1 | 20000 |
| Generic float knob | 0 to 1 | -1,000,000,000 | 1,000,000,000 |
| Generic integer knob | 0 to 1 | -16,777,216 | 16,777,216 |
| Hexadecimal knob | 0x0 to FFFFFF | 0 | 8 bits (24) |
| LED | Off / On | â | â |
| Level fader w/taper  (dBFS) | -100 to 10 | â | â |
| Level knob  (dBFS) | -100 to 20 | -100 | 100 |
| Meter  (dB) | -100 to 20 | â | â |
| Momentary button  (Click, hold, release) | Off / On | â | â |
| Mute button  (Toggle) | Off / On | â | â |
| Pan knob | -1 to 1 | â | â |
| Percent knob  (%) | 0 to 100 | 0 | 100 |
| Position knob | 0 to 1 | â | â |
| Status Display | 0 = OK - Green  1 = Compromised - Orange  2 = Fault - Red  3 = Not Present - Gray  4 = Missing - Red  5 = Initializing - Blue | â | â |
| Text display | â | â | â |
| Text edit | â | â | â |
| Time knob | 0 to 86,399 | 0 | 86,399 |
| Time knob  (seconds) | 0 to 1 | 0 | 86,400 |
| Toggle button | Off / On | â | â |
| Trigger button  (single pulse) | Off / On | â | â |
| <Remove>  (Can only be used on the last in list) | â | â | â |

[Control Pins](javascript:void(0))

For each Control you select, Input and Output Control Pins are supplied.

When you select a Control Type in the Properties, there are no "selectable" Control Pins in the right-side pane.

**Note:** The values in the following table are taken at the default setting of the Control.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Distance | 0 to 100 | â | 0.00 to 1.00 | Input / Output |
| Frequency knob  (Hz) | 0 to 25 and Infinity | 10 Hz to 20.0 kHz | 0.00 to 1.00 | Input / Output |
| Generic float knob | 0 to 1 | 0 to 1.00 | 0.00 to 1.00 | Input / Output |
| Generic integer knob | 0  1 | 0 or 1 | 0  1 | Input / Output |
| Hexadecimal | 0x0 to FFFFFF | â | 0.00 to 1.00 | Input / Output |
| LED | 0  1 | false  true | 0  1 | Input / Output |
| Level fader  (dBFS) | -100 to 20 | -100dB to 20.0dB | 0.00 to 1.00 | Input / Output |
| Level knob  (dBFS) | -100 to 20 | -100dB to 20.0dB | 0.00 to 1.00 | Input / Output |
| Meter  (dB) | -100 to 20 | -100dB to 20.0dB | 0.000 (-60 dB)  1.000 | Input / Output |
| Momentary button | 0  1 | false  true | 0  1 | Input / Output |
| Mute button | 0  1 | unmute  mute | 0  1 | Input / Output |
| Pan knob | -1 to 1 | -1.00 to 1.00 | 0.00 to 1.00 | Input / Output |
| Percent knob | 0 to 1 |  | 0 to 1 | Input / Output |
| Position knob | 0 to 1 | â | 0 to 1 | Input / Output |
| Status display | 0 to 5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Dark Red)  Initializing (Blue) | N / A | Input / Output |
| Text display | [1](#text_display) | text | [1](#text_display) | Input / Output |
| Text edit | [2](#text_edit) | text | [2](#text_edit) | Input / Output |
| Time knob  (seconds) | 0.000 to 1.00 | 0 ms to 1 s | 0.000 to 1.00 | Input / Output |
| Toggle button | 0  1 | false  true | 0  1 | Input / Output |
| Trigger button |  |  |  | Input / Output |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1. If there is a value/position type input to a Text Display there will be a value, string, and position output as well. If there is a text input, there is no value or position output, only text.2. If there is a numeric entered, or a value/position type input to a Text Edit box, there will be a value, string, and position output. If there is text entered, or input via the Control Pin, to a Text Edit box, the output is only text. | | | | |

[Troubleshooting](javascript:void(0))

### Using Components with Snapshot Controller Ramp Time

Components such as the [Crossover Component](crossover.htm) or other [Text Controller](device_controller_script.htm) or [Custom Controls](#) like the Integer Knobs, and Hexadecimal Knobs will not be recalled by Snapshot if the Ramp Time is a non-zero number.
