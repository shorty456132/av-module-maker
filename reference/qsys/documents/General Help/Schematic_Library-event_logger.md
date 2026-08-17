# Event Logger

> Source: https://help.qsys.com/Content/Schematic_Library/event_logger.htm

# Event Logger

Use the Event Logger component to place custom event messages â with a specified severity â into the Q-SYS Core's event log. Log entries can optionally include argument strings from the control pins of other design components.

[Configuration Overview](javascript:void(0))

1. Drag the Event Logger component into your schematic.
2. In the component Properties, specify the number of argument strings to use. See [Properties](#Properti).
3. If you want to include argument strings in the log message:
   * Wire a component's output control pin to an Arg input control pin on the Event Logger component.
   * Repeat for additional arguments.
4. Run your design.
5. Double-click the Event Logger component to open the control panel.
6. Configure the Log Entry (message to place in the log) and Severity. See [Controls](#Controls).
7. Click Publish.

Your log entry and any arguments are placed in the Q-SYS Core's event log, which is viewable from the Q-SYS Core Manager > [Event Log](../Core_Manager/Event_Log.htm).

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Schematic Example](javascript:void(0))

In this example, a log entry containing a Gain component's current Gain value and Mute status is published to the Q-SYS Core's Event Log.

### Q-SYS Designer

### Q-SYS Core Manager > Event Log

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Event Logger Properties

#### Arg Count

Select how many arguments to optionally include in your log entry, from 0 to 16.

[Controls](javascript:void(0))

#### Log Entry

Type the text to appear in the log entry. Use curly braces {} to optionally insert argument strings, which are placed into the log entry in numerical order - Arg 1, Arg 2, etc. Argument values are received from connected output control pins of other components.

[Example](javascript:void(0))

If your Log Entry text is:

`This is my log message, which contains {}, {}, and {}.`

...your message would include argument strings from Arg 1, Arg 2, and Arg 3, in that order.

#### Severity

Select a severity to associate with the log entry: default (normal), error, or warning.

#### Publish

Click to publish this log entry to the Event Log.

#### Arg 1 - 16

These text boxes indicate what strings are being received for each argument from connected component control pins.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Arg *n* | (text) | | | Input / Output |
| Log Entry | (text) | | | Input / Output |
| Severity | - | default  error  warning | - | Input / Output |
| Publish | (trigger) | | | Input / Output |
