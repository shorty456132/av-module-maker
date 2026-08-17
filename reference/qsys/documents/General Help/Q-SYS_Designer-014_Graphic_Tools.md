# Graphic Tools

> Source: https://help.qsys.com/Content/Q-SYS_Designer/014_Graphic_Tools.htm

# Graphic Tools

Use the Graphic Tools to organize, label, annotate, and enhance the appearance of your design or User Control Interface (UCI) layout.

[Text Block Tool](javascript:void(0))

Use the Text Block tool to add a text box to your design or UCI. You can adjust the style of both the text itself and the surrounding box.

### Adding a Text Block

1. Click the  icon.
2. Click and drag within the schematic to draw the Text Block.
3. Type your desired text. To edit the text later, double-click it.
4. In the Properties pane, Set the Graphic Properties and Text Style.

### Graphic Properties

#### Position

Set the horizontal and vertical coordinates of the Text Block location within the schematic. The values auto-adjust when you click and drag the Text Block, but you can also manually specify the values.

#### Size

Set the horizontal and vertical size of the Text Block. The values auto-adjust when you click and drag to re-size the Text Block, but you can also manually specify the values.

#### Fill

Click the Fill field to set the Text Block's background color and transparency, or use the eyedropper  to click an item within the schematic with the desired color. By default, the Text Block is transparent.

#### Corner Radius

Select how much corner rounding is applied to the Text Block, from 0 to 300. The higher the value, the more rounding is applied.

You can also adjust the corner radius for Text Boxes, Group Boxes, and controls using the corner radius handle.

[Show Me](javascript:void(0))

[
Your browser does not support the video tag.
](../Resources/Videos/corner_radius_adjust.webm)

#### Stroke Color

This is the color of the Text Block border. Click the Stoke Color field to select a color and set the transparency, or use the eyedropper  to click an item within the schematic with the desired color.

#### Stroke Width

This is the width of the Text Block border, from 0 to 64.

### Text Style

#### Text Color

Click the Text Color field to set the text color and transparency, or use the eyedropper  to click an item within the schematic with the desired color.

#### Size

Set the pixel size of the text, from 6 to 2,048 (default is 12).

#### Font

Set the font for the text (default is Roboto).

#### Font Style

Set the font's weight, slant, etc. The available styles are determined by the selected Font.

#### Horizontal Alignment

Set how the text aligns in relation to the left and right borders: Center (default), Left, Right.

#### Vertical Alignment

Set how the text aligns in relation to the top and bottom borders: Center (default), Bottom, Top.

[Header Tool](javascript:void(0))

Use the Header tool to add a title to an area of your design.

### Adding a Header

1. Click the  icon.
2. Click and drag within the schematic to draw the Header.
3. Type your desired Header text. To edit the text later, double-click it.
4. In the Properties pane, Set the Graphic Properties and Text Style.

### Graphic Properties

#### Position

Set the horizontal and vertical coordinates of the Header location within the schematic. The values auto-adjust when you click and drag the Header, but you can also manually specify the values.

#### Size

Set the horizontal and vertical size of the Header. The values auto-adjust when you click and drag to re-size the Header, but you can also manually specify the values.

#### Fill

Click the Fill field to set the Header's color and transparency, or use the eyedropper  to click an item within the schematic with the desired color. The Fill sets the color for both the horizontal rule and text.

### Text Style

#### Size

Set the pixel size of the text, from 6 to 2,048 (default is 12).

#### Font

Set the font for the text (default is Roboto).

#### Font Style

Set the font's weight, slant, etc. The available styles are determined by the selected Font.

#### Horizontal Alignment

Set how the text aligns in relation to the left and right borders: Center (default), Left, Right.

[Group Box Tool](javascript:void(0))

Use the Group Box tool to visually group objects within a Q-SYS design or UCI.

### Adding a Group Box

1. Click the  icon.
2. Click and drag within the schematic to draw the Group Box.
3. Optionally, start typing to add a text label for the Group Box. To edit the text later, double-click it.
4. In the Properties pane, Set the Graphic Properties and Text Style.
5. Drag schematic items into the Group Box to create a visual grouping. You can add controls, text, lines, headings, and boxes from the control panels of Q-SYS components by either dragging or copying and pasting them into the box area. You can also add graphics from other applications by copying and pasting or dragging them from the other application into the box area. For more information about inserting graphic files into a UCI, see [User Control Interface (UCI) Design Overview](../Schematic_Library/user_control_interface.htm#Adding).

[Example 1](javascript:void(0))

[Example 2](javascript:void(0))

**Note:** A Group Box and the items within it are not linked. To move a Group Box and its items, you must select them all.

### Graphic Properties

#### Position

Set the horizontal and vertical coordinates of the Group Box location within the schematic. The values auto-adjust when you click and drag the Group Box, but you can also manually specify the values.

#### Size

Set the horizontal and vertical size of the Group Box. The values auto-adjust when you click and drag to re-size the Group Box, but you can also manually specify the values.

#### Fill

Click the Fill field to set the Group Box background color and transparency, or use the eyedropper  to click an item within the schematic with the desired color. By default, the Group Box is transparent.

#### Corner Radius

Select how much corner rounding is applied to the Group Box, from 0 to 300. The higher the value, the more rounding is applied.

You can also adjust the corner radius for Text Blocks, Group Boxes, and controls using the corner radius handle.

[Show Me](javascript:void(0))

[
Your browser does not support the video tag.
](../Resources/Videos/corner_radius_adjust.webm)

#### Stroke Color

This is the color of the Group Box border. Click the Stoke Color field to select a color and set the transparency, or use the eyedropper  to click an item within the schematic with the desired color.

#### Stroke Width

This is the width of the Group Box border, from 0 to 64.

### Text Style

#### Text Color

Click the Text Color field to set the text color and transparency, or use the eyedropper  to click an item within the schematic with the desired color.

#### Size

Set the pixel size of the text, from 6 to 2,048 (default is 12).

#### Font

Set the font for the text (default is Roboto).

#### Font Style

Set the font's weight, slant, etc. The available styles are determined by the selected Font.

#### Horizontal Alignment

Set how the text aligns in relation to the left and right borders: Center (default), Left, Right.

[Polygon Tool](javascript:void(0))

Use the Polygon tool to create a shape and assign a control to it. Clicking a Polygon changes the state of the control.

### Adding a Polygon

1. Click the  icon.
2. Point and click to draw the individual line segments of the Polygon. To finish the Polygon, connect the final segment to the first, or double-click.

   **Tip:** You can add points (or nodes) to a finished Polygon. Click and drag from any point on a line segment to create a new node.
3. Optionally, add text to the Polygon. Click the Polygon, and then begin typing. To edit the text later, double-click it.
4. In the Properties pane, set the Graphic Properties.

### Assigning a Control to a Polygon

1. Create a Polygon in your design or UCI.
2. Set the Region Properties for the polygon. These settings determine the style and action of the assigned control.
3. Drag a control from a control panel onto the shape while holding the Ctrl button.
4. Release the mouse button. The control is assigned to the shape.

[Example](javascript:void(0))

In this example, the treble clef is assigned to the Play button of the Audio Player. If it was in a design or UCI, clicking the treble clef sign would start playing the selected file.

### Region Properties

#### Button Style

Sets the style of button:

* Momentary: When the button is clicked, it stays in its opposite state until released.
* Off: Sets the button off, and it can't be changed except within the Control Panel from which it was copied. If the button is turned on from within the Control Panel, you can turn it off from the button in the Schematic or UCI.
* On: Sets the button on, and it can't be changed except within the Control Panel from which it was copied. If the button is turned off from within the Control Panel, you can turn it on from the button in the Schematic or UCI.
* String: When the button is clicked, it sends the string you entered to the control in the Control Panel. See Button String property.
* Toggle: Allows you to turn the button on or off.

#### Button String

Available when Button Style is set to 'String'. The string you enter is case sensitive and must be valid for the control in the Control Panel. For example a fader control has a range of -100 to 20, the string must be numeric and within that range, a toggle button must be true/false, On / Off, or 1/0.

[Special string commands](javascript:void(0))

In addition, the following special commands may be used in the String field:

* ++ moves the control plus 1 minor division
* -- moves the control minus 1 minor division
* += moves the control plus *n* major units where *n* = String value (ex.+=2)
* -= moves the control minus *n* major unit where *n* = String value (ex. -=2)
* \*= moves the control *n* times the major unit where n = String value (ex. \*=3) If the current value of the control is 0 (zero), the multiplication command will not move the control. If you enter 0 in the String field, the control moves to 0 (zero).
* max moves the control to its maximum value.
* min moves the control to its minimum value.

#### Reverse Action

Changes the direction of the control.

For example, set Reverse Action to 'Yes' if you want to change a mute button (on state is muted, off is passing audio) to an enable button (on state is passing audio, off state is muted).

### Graphic Properties

#### Position

Set the horizontal and vertical coordinates of the Polygon location within the schematic. The values auto-adjust when you click and drag the Polygon, but you can also manually specify the values.

#### Size

Set the horizontal and vertical size of the Polygon. The values auto-adjust when you click and drag to re-size the Polygon, but you can also manually specify the values.

#### Fill

Click the Fill field to set the Polygon's background color and transparency, or use the eyedropper  to click an item within the schematic with the desired color. If you have assigned a control to the Polygon, the Fill color is the "on" state color for controls with binary states.

#### Off Color

If you have assigned a control to the Polygon, this is the color for the "off" state for controls with binary states. When the Off Color is linked  to the Fill color, the Off Color is automatically assigned. When unlinked , you can manually adjust the color.

#### Stroke Color

This is the color of the Polygon border. Click the Stoke Color field to select a color and set the transparency, or use the eyedropper  to click an item within the schematic with the desired color.

#### Stroke Width

This is the width of the Polygon border, from 0 to 64.
