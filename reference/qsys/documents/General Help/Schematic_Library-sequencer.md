# Sequencer

> Source: https://help.qsys.com/Content/Schematic_Library/sequencer.htm

# Sequencer

The sequencer component is used to create and manage sequences of events or actions. It allows you to define a series of steps, each with specific timing and actions, which can be executed in order. This is useful for automating repetitive tasks and ensuring precise control over complex operations.

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Sequencer Properties

#### Output Count

This property allows you to set the number of steps or outputs that the sequencer will manage. Each step will have its own set of controls for length, delay, and active state. This setup allows for precise control over the sequencing operation, enabling you to create complex sequences with multiple steps. You can choose between 1 and 999.

#### Loop

Determines whether the sequencing operation will automatically restart after completing its first run. When the loop property is set to "Yes," the sequencer will continue to run in a loop until a stop command is issued.

[Controls](javascript:void(0))

#### Running LED

LED indicating that a sequencing operation is currently in progress. When the sequencer is active, the running LED remains lit, signaling that the sequence is being executed. If the sequencing operation is stopped or canceled, the running LED will turn off, indicating that the process has been halted.

#### Start

This button initiates the sequencing process. When you press this button, the sequencer begins executing the sequence of steps that have been configured. Each step will be processed in order, based on the settings for length, delay, and active state

#### Stop

This button, on the other hand, halts the sequencing operation. Pressing this button will immediately stop the sequencer from continuing its current sequence. This is useful if you need to interrupt the sequence for any reason, such as making adjustments or stopping the process altogether.

### Step *n*

#### Length

This property specifies the duration for which the corresponding step's active output will remain high after the delay period has expired. The valid range for the length is from 0.1 seconds (100 ms) to 10 seconds.

#### Delay

This property defines the time that must elapse before the corresponding step's active output goes high. The valid range for the delay is from 0.1 seconds (100 ms) to 86400 seconds (24 hours).

#### Active LED

This indicator lights up when the sequencing operation is triggered by the start button. It begins with Step 1 and continues in numeric order, showing which step is currently active.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Step *n* | | | | |
| Delay | (text) | | | Input / Output |
| Length | (text) | | | Input / Output |
| Running | 0  1 | false  true | 0  1 | Output |
| Start | 0  1 | false  true | 0  1 | Input |
| Stop | 0  1 | false  true | 0  1 | Input |
