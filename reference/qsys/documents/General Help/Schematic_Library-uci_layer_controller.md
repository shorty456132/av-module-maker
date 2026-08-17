# UCI Layer Controller

> Source: https://help.qsys.com/Content/Schematic_Library/uci_layer_controller.htm

# UCI Layer Controller

Use the UCI Layer Controller to show or hide individual layers in a specified UCI and page.

[Configuration Overview](javascript:void(0))

1. Drag the UCI Layer Controller component into your schematic.
2. Select the component and configure its Properties. See [Properties](#Properti).
3. Press F5 to save your design to the Core and run it. (Or, press F6 to emulate your design.)
4. In your schematic, double-click the component to open its control panel.
5. For each UCI layer, configure a Transition type. See [Controls](#Controls).
6. Click a layer's Show button to show or hide the layer in the UCI.

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Schematic Example](javascript:void(0))

In this example, there are three UCI layers installed. Any of these layers can be transitioned on or off the screen by choosing the Transition type.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### UCI Layer Controller Properties

#### UCI

Select a UCI name.

#### Page

If **Is Shared** is set to 'No':

Select a page name to control the visibility of layers within that page.

#### Is Shared

Select 'No' to control the visibility of standard layers in a selected Page.

Select 'Yes' to control the visibility of Shared Layers in the selected UCI name.

For information about adding layers to a UCI, see [User Control Interface (UCI) Design Overview](user_control_interface.htm#Add_Layers).

[Controls](javascript:void(0))

#### Transition (combo box)

Assign a transition type for the layer name.

#### Show (button)

Click the button to show or hide the layer.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| *layer name*: Transition | N/A | left  right  top  bottom  fade  none | N/A | Input / Output |
| *layer name*: Visibility | 0  1 | false  true | â | Input / Output |

[Troubleshooting](javascript:void(0))

### UCI Layer Name Retrieval

When using a script to obtain the names of the layers on a UCI from a UCI Layer Controller component, it is recommended to avoid using underscores (â\_â ) in the layer names. This ensures that the name returned matches the actual layer name, preventing any potential discrepancies.
