# Lightbar (TSC-G3, PS-TSCG3 Series)

> Source: https://help.qsys.com/Content/Schematic_Library/lightbar.htm

# Lightbar (TSC-G3, PS-TSCG3 Series)

Use the Lightbar component to set the color of the two LED lightbars (left and right side) on TSC-70-G3 and TSC-101-G3 (including the PS-TSCG3 Touchscreen Page Station) touch screen controllers.

[Lightbar Overview](javascript:void(0))

Each lightbar consists of four 24-bit high-brightness RGB LED elements. You can set all LEDs to be the same color (both the left side and right side lightbars) or set each LED individually.

To configure the lightbars:

1. Drag the Lightbar component into the schematic workspace.
2. Click the Lightbar component to display its Properties pane, and then set the Light Bar Drive Mode. See [Properties](#Properti) for more information.
3. Save and run the design to the Core.
4. Double-click the Lightbar component to open its control panel.
5. Select a Color for all LEDs or individual LEDs, depending on the Light Bar Drive Mode.

**Tip:** Alternatively, you can send a hex value or text value ("red", "white", "blue", etc.) to the Lightbar's input Color control pin. The [Color Picker](color_picker.htm) component, available from the Control Components category, provides an easy way to visually select a desired color and output its corresponding hex value to the Lightbar component.

[Schematic Examples](javascript:void(0))

### Example 1: Setting the color for all LEDs

In this example, Lightbar is configured to display the same color on both the left and right side LED bars. (The Light Bar Drive Mode is set to "One color for all LEDs".) The Color control pin is exposed, and receives the color chosen via the [Color Picker](color_picker.htm) component.

### Example 2: Setting the color for each LED

In this example two [Selector](selector.htm) components are used to send different "status" colors to each side's LED lightbar. (The Light Bar Drive Mode is set to "Set color for each LED".)

[Properties](javascript:void(0))

These properties are specific to the Lightbar component for the TSC-70-G3 or TSC-101-G3 (including the PS-TSCG3 Touchscreen Page Station)touch screen controllers.

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Light Bar Drive Mode

Select what LEDs are affected by the color selection:

* One color for all LEDs: The color selection is applied to both the right and left LED lightbars. All LEDs are the same color.
* Set color for each LED: You can select a color for each of the 8 LEDs. LEDs 1-4 are on the left side of the touch screen controller, while LEDs 5-8 are on the right side.

[Controls](javascript:void(0))

#### Hex Code

This is the hexadecimal code that corresponds to the selected color being output to the touch screen controller's light bars - either the same color for all LEDs or for individual LEDs, depending on the Light Bar Drive Mode. This control is read-only within the control panel, but is changeable when sending a hex code (or a color name) to the Color input control pin.

#### Color

The Color drop-down menu allows you to select from 17 common color names. Selecting a color name automatically updates the corresponding Hex Code control.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Color | - | #*nnnnnn*  or  *color name* (blue, green, etc.) | - | Input |
| Hex Code | - | #*nnnnnn* | - | Output |
