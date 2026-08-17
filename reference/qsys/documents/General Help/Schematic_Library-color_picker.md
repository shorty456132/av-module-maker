# Color Picker

> Source: https://help.qsys.com/Content/Schematic_Library/color_picker.htm

# Color Picker

Use the Color Picker to easily select a color â either visually with a control surface or manually with numeric values â for use by a downstream component that can receive a color hex code, such as the Lightbar component.

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Schematic Example](javascript:void(0))

In this example, Color Picker is used to send a very specific color to display on the TSC-70-G3 touch screen controller's light bar.

**Note:** Refer to the [Lightbar (TSC-G3, PS-TSCG3 Series)](lightbar.htm) topic to learn about how to use the Lightbar component for TSC-70-G3 and TSC-101-G3 touch screen controllers.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Color Picker Properties

#### Color Picker Size

Select a size for the color picker surface area, from 160 to 512 (default is 256).

[Controls](javascript:void(0))

#### Color

Read-only. Indicates the corresponding hex code of the selected color.

#### Red, Green, Blue

These controls display the red, green, and blue component values of the selected color. You can also manually enter values for each, from 0 to 255.

#### Hue

Manually enter a hue value for the selected color, from 0 to 360 (default is 0).

#### Saturation

This control displays the saturation component value of the selected color. You can also manually enter a value, from 0 to 100.

#### Value

This control displays the color value of the selected color. You can also manually enter a value, from 0 to 100.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Blue | 0 to 255 | 0 to 255 | 0 to 1.00 | Output |
| Color | - | #*nnnnnn* | - | Output |
| Green | 0 to 255 | 0 to 255 | 0 to 1.00 | Output |
| Hue | 0 to 360 | 0 to 360 | 0 to 1.00 | Input / Output |
| Red | 0 to 255 | 0 to 255 | 0 to 1.00 | Output |
| Saturation | 0 to 100 | 0 to 100 | 0 to 1.00 | Input / Output |
| Value | 0 to 100 | 0 to 100 | 0 to 1.00 | Input / Output |
