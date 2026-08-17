# Control Router

> Source: https://help.qsys.com/Content/Schematic_Library/control_router.htm

# Control Router

The Control Router allows you to select any of the available control **Inputs** for a single **Output**. You can select only one Input for a given Output, but you can have the same Input going to all of the Outputs. The Outputs can be individually muted. You can choose one of three **Selection Controls**: **Crosspoint** buttons, **Knobs**, or **Combo boxes**.

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Schematic Example](javascript:void(0))

In this example, a Control Router is being used to deliver multiple different editable text fields into the Dial String of a Softphone, so that you could quickly toggle between commonly-used telephone numbers.

[Properties](javascript:void(0)) 

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Control Router Properties

#### Input Count

Sets the number of **Inputs** on the component.

#### Output Count

Sets the number of **Outputs** on the component.

#### Selection Controls

In the Router Control Panel you can have one of three different type of controls. Knobs, Combo boxes, and Cross-point.

**Knobs** provide a knob and a text edit box for each **Output**. When you adjust the value of the knob, you are selecting the **Input** you want for that Output. You can select the same Input for multiple Outputs.

**Combo boxes** provides a drop-down list for each Output. You can select the same Input for multiple Outputs.

**Crosspoint** buttons provide a button matrix and a text edit box. You can click the button for the Input you want for that Output, or click the text edit box and enter the number of the Input. You can select the same Input for multiple Outputs.

[Controls](javascript:void(0))

#### Input

Selects the **Input** and associated **Control Channel** going to the associated **Output**.

* **Crosspoint** - provides a column of radio buttons to select one Input for the associated Output.
* **Knob** - provides a knob with range equal to the number of Inputs, and a text edit box to enter the number of the Input.
* **Combo-box** - provides a drop-down list from which to select the input.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Output *n* Input *n* Select [1](#Crosspoint) | 0  1 | false  true | 0  1 | Input / Output |
| Output *n* Select [2](#Output_Select) | 1 to 1024 | 0.000 to 2.00 | 0.000 to 1.00 | Input / Output |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1. Available with **Crosspoint** buttons only. Provides individual Control Pins for each Input for each output. Both the input and output side Control Pins are "true" when that **Input** is selected, all other input and output Control Pins for that **Output** are "false"2. Available with all **Selection Controls**. Provides one Control Pin to select any **Input** for the **Output**. | | | | |
