# Router

> Source: https://help.qsys.com/Content/Schematic_Library/router_with_output.htm

# Router

The Router allows you to route any of the available audio **Inputs** to any of the available **Outputs**. You can choose **Mono** to route inputs to outputs one at a time, **Stereo** to simultaneously route the left and right **Channels** of an Input to the left and right Channels of any available Output, or **Multi-channel** to simultaneously route up to 256 Channels of a single Input to any Output. The Outputs can be individually muted. When a Stereo or Multi-channel Output is muted, all the Channels associated with that Output are muted. You can choose one of three **Selection Controls**: **Crosspoint** buttons, **Knobs** or **Combo boxes**. In addition, you can select **between Source Select Mode** and **Destination Select Mode**.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Type** Property.

### Input Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Router component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

### Output Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Router component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs and outputs.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Router Properties

**Note:** When Selection Controls is set to Crosspoint Buttons, there is a limit of 16,384 controls (Input Count x Output Count must be <= 16,384).

#### Input Count

Sets the number of **Inputs** on the component. One **Input** can have up to 256 **Channels**. See **Type** below. This value must be between 1 and 1024.

#### Output Count

Sets the number of **Outputs** on the component. One **Output** can have up to 256 **Channels**. See Type below. This value must be between 1 and 1024.

#### Selection Controls

In the Router Control Panel you can have one of four different type of controls. Knobs, Combo boxes, Cross-point and Output Select Mode.

**Knobs** provide a knob and a text edit box for each **Output**. When you adjust the value of the knob, you are selecting the **Input** you want for that Output. You can select the same Input for multiple Outputs.

**Combo Boxes** provides a drop-down list for each Output. You can select the same Input for multiple Outputs.

**Crosspoint Buttons** provide a button matrix and a text edit box. You can click the button for the Input you want for that Output, or click the text edit box and enter the number of the Input. You can select the same Input for multiple Outputs.

#### Selection Mode

In the **Source** mode, you select the output for each **Input** (source). The **Inputs** are rows, the **Outputs** columns.

In the **Destination** mode, you select the **Input** for each **Output** (destination). The **Outputs** are rows, the **Inputs** columns. The **Mute** buttons act as radio buttons when more than one **Input** is selected for an **Output**.

### Channels

#### Type

Sets the type of **Channel** available for a **Inputs** and **Outputs**. When you select **Stereo** or **Multi-Channel**, all of the Channels for an Input, or Output change routing together when you select a different Input or Output.

#### Count

Available with **Multi-Channel** only. Sets the number of **Channels** for a single **Input** and/or **Output**. You can choose between 2 and 256 channels.

[Controls](javascript:void(0))

#### Mute (button)

In the **Source Selection Mode**, the Mute button mutes the associated **Output**.

In the **Destination Select Mode**, the Mute buttons mute the **Input**, and are On by default.

#### Input

In the **Source Selection Mode**, you select the **Input** row (source) for each **Output** column. You can have one **Input** feeding multiple **Outputs**.

In the Destination Selection Mode, you select the **Output** row (destination) for each **Input** column. If you multiple **Inputs** assigned to the same **Output**, the **Mute** buttons act as radio buttons.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Output *n* Input *n* Select[1](#Crosspoint) | 0  1 | false  true | 0  1 | Input / Output |
| Output *n* Select[2](#Output_Select) | 1 to 1024 | 0.000 to 2.00 | 0.000 to 1.00 | Input / Output |
| Input *n* Select[3](#Output_Select_Mode) | 1 to 1024 | 0.000 to 2.00 | 0.000 to 1.00 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Select |  |  |  | Input / Output |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1. Available with **Crosspoint** buttons only. Provides individual Control Pins for each Input for each output. Both the input and output side Control Pins are "true" when that **Input** is selected, all other input and output Control Pins for that **Output** are "false".2. Available with all **Selection Control** except **Output Select Mode**. Provides one Control Pin to select any **Input** for the **Output**.3. Available with **Output Select Mode** only. Provides one Control Pin to select any **Output** for the **Input**. | | | | |

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| When Selection Controls is set to **Crosspoint Buttons** (default) and Selection Mode is set to **Source** (default) or **Destination** | | | | |
| Output *n* | | | | |
| Input *n* Select | 1 to *n* | false  true | 0  1 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Select | 1 to *n* | 0 to *n* | 0.0-1.0 | Input / Output |
| Input *n* | | | | |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Output *n* Select | 1 to *n* | false  true | 0  1 | Input / Output |
| Select | 1 to *n* | 0 to *n* | 0.0-1.0 | Input / Output |
| When Selection Controls is set to **Knobs** and Selection Mode is set to **Source** or **Destination** | | | | |
| Output *n* | | | | |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Select | 1 to *n* | 0 to *n* | 0.0-1.0 | Input / Output |
| Input *n* | | | | |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Select | 1 to *n* | 0 to *n* | 0.0-1.0 | Input / Output |
| When Selection Controls is set to **Combo Boxes** and Selection Mode is set to **Source** or **Destination** | | | | |
| Output *n* | | | | |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Select | 1 to *n* | 0 to *n* | 0.0-1.0 | Input / Output |
| Input *n* | | | | |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Select | 1 to *n* | 0 to *n* | 0.0-1.0 | Input / Output |
