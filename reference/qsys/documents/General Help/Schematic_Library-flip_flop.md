# Flip-Flop Component

> Source: https://help.qsys.com/Content/Schematic_Library/flip_flop.htm

# Flip-Flop Component

The Flip-Flop Component converts a trigger type input to a Boolean type output.

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Schematic Examples](javascript:void(0))

**Use Case 1**
- If you want a physical momentary button to act like a toggle button.

1. Hard wire the button to a Digital Input pin on the GPIO connector on the Core or I/O Frame.
2. In Q-SYS Designer, wire the Digital Input pin to the Toggle Input Control Pin of a Flip-Flop component.
3. When the design is running, press the momentary button, a trigger is sent through the GPIO to the Toggle Input Control Pin on the Flip-Flop. The Flip-Flop changes State.
4. Every time the button is pressed, the Flip-Flop changes State.

**Use Case 2**
- If you want two physical momentary buttons, one to turn something on, the other to turn it off.

1. Hard wire the buttons to two Digital Input pins on the GPIO connector on the Core or I/O Frame.
2. In Q-SYS Designer, wire one Digital Input pin to the Set Input Control Pin, wire the other to the Reset Input Control Pin of a Flip-Flop component.
3. When the design is running, press the ON (or "Set") momentary button, a trigger is sent through the GPIO to the Set Control Pin on the Flip-Flop. Depending on the Flip-Flop's current State, the Flip-Flop may change State.
4. Press the OFF (or "Reset") button, after pressing the ON button, the Flip-Flop changes State.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Flip-Flop Properties

*This component has no configurable properties.*

[Controls](javascript:void(0))

When a trigger type control is wired to any one of the Flip-flop's trigger inputs, every time the trigger type control is triggered, the Flip-flop responds. When a Boolean control is wired to a Flip-flop trigger input, the Flip-flop responds when the Boolean control changes to true.

#### Set

A trigger that sets the State to True

#### Reset

A trigger that sets the State to False

#### Toggle

A trigger that toggles State

#### State

Represents the state of the flip-flop. This control can be stored in a snapshot. The value of the State button is restored on startup.

Although it is a toggle button, it isn't normally use it as such.

#### Out

Read-only LED. The value of State.

#### Not Out

Read-only LED. The complementary value of State.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Not out | 1  0 | true  false | 1.00  0 | Output |
| Out | 1  0 | true  false | 1.00  0 | Output |
| Reset | Trigger | | | Input / Output |
| Set | Trigger | | | Input / Output |
| State | 1  0 | true  false | 1.00  0 | Input / Output |
| Toggle | Trigger | | | Input / Output |
