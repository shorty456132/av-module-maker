# Press and Hold

> Source: https://help.qsys.com/Content/Schematic_Library/press_n_hold.htm

# Press and Hold

Use the Press and Hold component to trigger events based on the duration of a button press, hold, and release.

[Configuration Overview](javascript:void(0))

1. Drag the Press and Hold component into your schematic.
2. Connect the Long and Short trigger control pins (exposed by default) to the input control pins of other components. Use these pins to trigger events in your design. See [Controls](#Controls).
3. Press F5 to save your design to the Core and run it. (Or, press F6 to emulate your design.)
4. In the Press and Hold component's control panel, set a Hold Time duration (in seconds). This is the threshold that determines whether the Long trigger fires (if the Input button is pressed, held, and released for a duration longer than the threshold) or the Short trigger fires (if the Input button is pressed, held, and released for a duration less than the threshold).
5. Press, hold, and release the Input button to fire the desired trigger.

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Schematic Example](javascript:void(0))

In this example, the Press and Hold component's control pins are wired to an Audio Player component's Play and Stop trigger pins. If the Input button is pressed and held for at least 2 seconds and then released, playback begins. But if the Input button is pushed briefly and then released (for any duration shorter than 2 seconds), playback stops.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Press and Hold Properties

*This component has no configurable properties.*

[Controls](javascript:void(0))

#### Hold Time

The amount of time, in seconds, that the Input button must be pressed, held, and released that separates firing the Short trigger or Long trigger.

#### Input

To fire the Short trigger: Press, hold, and release the Input button for a duration shorter than the Hold Time.

To fire the Long trigger: Press, hold, and release the Input button for a duration longer than the Hold Time.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Long | (trigger) | | | Output |
| Short | (trigger) | | | Output |
| Hold Time | 0 to 3600 | 0ms to 3600s | 0.000 to 1.00 | Input / Output |
| Input | 0  1 | false  true | â | Input / Output |
