# When

> Source: https://help.qsys.com/Content/Schematic_Library/when.htm

# When

The when component enables you to schedule events based on specific days and times. Configure the component to activate events on selected days, at precise times, and for defined durations. This feature ensures that your scheduled events run seamlessly and efficiently, providing you with greater control over your system's operations.

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### When Properties

*This competent does not have any configurable properties.*

[Controls](javascript:void(0))

#### Enable

This control activates or deactivates the scheduled event. When enabled, the event will execute based on the specified settings. If disabled, the event will not run, regardless of the other configurations.

#### Active LED

This indicator shows whether the scheduled event is currently active. It provides a visual confirmation that the event is running as scheduled.

#### Days

This control allows you to specify the days of the week on which the event should occur. You can select specific days (e.g., Monday, Wednesday, Friday) to ensure the event only runs on those days.

#### Time

This control sets the exact time of day when the event should start. You can specify the hour and minute to ensure precise timing for the event's execution.

**Note:** The Time control is configured in 24-hour format.

#### Length

This property specifies the duration of the trigger event. The valid range for the length is from 0 seconds to 10 seconds.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Active | 0  1 | false  true | 0  1 | Output |
| Days | | | | |
| Fri-Wed | 0  1 | disabled  enable | 0  1 | Input |
| Enable | 0  1 | disabled  enable | 0  1 | Input / Output |
| Length | (text) | | | Input |
| Time | (text) | | | Input |
