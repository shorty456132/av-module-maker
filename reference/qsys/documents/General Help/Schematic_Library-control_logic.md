# Control Function Component

> Source: https://help.qsys.com/Content/Schematic_Library/control_logic.htm

# Control Function

The **Control Function** applies the selected function to all of the inputs with the output being the result. Can be used to vary controls in ways other than a 1:1 ratio, trigger an action when one control becomes greater or less than another, and more. The **Control Function** provides logical, positional, and value related functions.

For **Logical Functions**, logic-type input controls produce 1 and 0 outputs, position and value controls use > or < midpoint of the input control to produce a 0 or 1 output.

For **Positional Functions**, logic-type input controls produce 1 and 0 outputs, position-type and value-type input controls produce 0.000 to 1.00 based on the position of the control regardless of the value.

For **String Functions**, string-type input controls produce true and false outputs based on whether the strings match at each input. Matching is also case sensitive.

For **Value Functions**, logic-type input controls produce 1 and 0 outputs, position-type input controls produce 0.000 to 1.00 based on the position of the control, value-type input controls produce the actual value of the control.

Text type inputs and outputs are not available with the Control Functions. However, if you need to use a text input or output, you can place a control, that can convert the text to a value, between the text-type control and the Control Function. (Text Edit box > Generic Integer control > Control function > Generic Integer > Text Display)

There are no audio connections for this component, so all connections are to and from **Control Pins**.

You can have the **Control Pin** output of one type of control going through a **Control Function**, and performing that operation on a different type of control, or the same type of control. You need to keep in mind, especially for the Value type controls, that ranges on controls are not always the same, so the results are not always one-to-one. There are some controls, like a Gain fader, that has more precision from 0 dB to 20 dB than from 0 dB to -100 dB, so the results will vary accordingly.

To get a feel for the results you can achieve, drag a component into a design that has various types of controls in it, for example a **Mixer**. Then connect the output **Control Pin**(s) of the **Mixer** to the input **Control Pins** of the **Control Function** component. Add a **Custom Controls** component to the design. Add as many different control types to the **Custom Control** component as you can, or want, make the count on all the controls only one because there is only one output from the **Control Function** component. Then **Emulate** or **Save to Core & Run**, and start experimenting to see the effects of the various **Control Functions** on the various types of controls. Next, use your imagination!

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Schematic Examples](javascript:void(0))

The **Control Function** component can be configured to perform a number of different types of functions, including *conditional statements*, *comparative validation*, *and-gates*, and *or-gates*, just to name a few.

**Note:** Upon dragging the **Control Function** into your schematic, you may realize the default name is *Value Sum*. This is normal.

[Value Sum Examples](javascript:void(0))

This example does it exactly what it sounds like: it adds up the Values of its incoming controls. In this example, we have some custom integer knobs, and right now, it is reporting there is a value of zero.

In this example, we have a Paging System and each Zone has an LED that will illuminate when an announcement is playing in that area. Using the Value Sum, we can quickly display how many Zones are currently busy in the venue.

[Trigger Combiner Example](javascript:void(0))

In this example, we are using the Trigger Combiner function to connect multiple different triggers through an or-gate, allowing any of the original triggers to activate the output trigger.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Control Function Properties

#### Function

Applies a selected function to multiple inputs, producing an output result.

#### Input Count

Is dependent on the Function Property chosen. Some Functions allow the Input Count to be between 2 and 512.

### Functions

[Logic Functions](javascript:void(0))

These functions are intended to be used with a logical type input, such as a toggle button. These output a *true* or *false* based on whether or not their conditions are met by the incoming controls.

#### Logic 1 of N

The output is a value of 1 if one input has a value of 1. More than one, the output is 0.

#### Logic AND

The output is a value of 1 if all the inputs have a value of 1.

#### Logic NAND

The output is a value of 0 if all the inputs have a value of 1.

#### Logic NOR

The output is a value of 1 if all the inputs have a value of 0.

#### Logic NOT

1 to 512 inputs. The output is a value of 1 if the input is 0.

#### Logic NOT XOR

The output is a value of 1 if none or an even number of inputs are 1.

#### Logic OR

The output is a value of 1 if one or more inputs are 1.

#### Logic XOR

The output is a value of 1 if an odd number of the inputs have a value of 1.

[Positional Functions](javascript:void(0))

These functions are intended to be used with a positional type input, such as a position knob or percent knob. These functions will perform their actions based on the .Position parameter of the incoming controls.

#### Position Average

The output is a positional value equal to the average position of all the inputs.

#### Position Difference

Two inputs only. The output is a positional value equal to **Input 1** minus **Input 2**.

#### Position Equal

Two inputs only. The output is a positional value of 1.00 when both inputs are equal. If not equal the output is a positional value of 0.00.

#### Position Greater

Two inputs only. The output is a positional value of 1.00 when **Input 1** is greater than **Input 2**. If not, the output is a positional value of 0.00.

#### Position Invert

One input only. The output is a positional value opposite of the input's positional value. The output equals the input when the input is exactly at midpoint.

#### Position Less

Two inputs only. The output is a positional value of 1.00 when **Input 1** is less than **Input 2**. If not, the output is a positional value of 0.00.

#### Position Maximum

The output is a positional value equal to the input with the greatest positional value.

#### Position Minimum

The output is a positional value equal to the input with the smallest positional value.

#### Position Product

The output is a positional value equal to the product of all the inputs.

#### Position Sum

The output is a positional value equal to the sum of the positional values of all the inputs. When the output reaches 1.00 (full position), any controls that would add to the sum have no effect on the output.

[String Functions](javascript:void(0))

#### String Equal

Two inputs only. The output value is true when strings match, and false when different. String values are case sensitive.

[Trigger Combiner Functions](javascript:void(0))

#### Trigger Combiner

Multiple trigger type inputs, one trigger output. Any input receiving a trigger, causes a trigger on the output. Acts like a "trigger" OR gate.

[Value Functions](javascript:void(0))

These functions are intended to be used with a value type input, such as a generic float knob or an integer knob. These functions will perform their actions based on the .Value parameter of the incoming controls.

#### Value Absolute Value

One input only. The output is a value equal to its distance from zero, regardless of whether it is positive or negative.

#### Value Average

The output is a value equal to the average value of all the inputs.

#### Value Difference

Two inputs only. The output is a value equal to the difference of the value of the inputs.

#### Value Equal

Two inputs only. The output is a value of 1, when both inputs are equal. If not equal the output is 0.

#### Value Greater

Two inputs only. The output is 1 when **Input 1** is greater than **Input 2**. Otherwise, the output is 0.

#### Value Less

Two inputs only. The output is 1 when **Input 1** is less than **Input 2**. Otherwise, the output is 0.

#### Value Maximum

The output is a value equal to the input with the greatest value. If the greatest input is less than .5 (50%), the logical output is 0, if it is greater than .5 (50%), the logical output is 1.

#### Value Minimum

The output is a value equal to the input with the smallest value.

#### Value Negate

Only one input. The output is inverted and tracks a value control inversely within the range of both controls. If the Input control has a range of -100 to 20, and the Output control's range is -200 to 200, the output control tracks from -20 to 100.

#### Value Product

The output is a value equal to the product of all the inputs.

#### Value Quotient

The output is the value of **Input 1** divided by **Input 2**.

#### Value Square

One input only. The output is equal to the square of the input.

#### Value Square Root

One input only. The output is equal to the square root of the input.

#### Value Sum

The output is a value equal to the sum of all the inputs.

### Input Count

#### Input Count

Selects the number of inputs. Depends on the Function selected, some functions have only one or two inputs. You can choose between 1 and 512 Inputs.

[Controls](javascript:void(0))

There are no Controls for the **Control Function** component.

[Control Pins](javascript:void(0))

There is only one type of control pin for a **Control Function** component. The type or **Function** is selected in the **Properties**, and the number available depends on the **Function**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Logic AND | 0  1 | N / A | 0  1 | Input / Output |
| Logic NAND | 0  1 | N / A | 0  1 | Input / Output |
| Logic NOR | 0  1 | N / A | 0  1 | Input / Output |
| Logic NOT | 0  1 | N / A | 0  1 | Input / Output |
| Logic NOT XOR | 0  1 | N / A | 0  1 | Input / Output |
| Logic OR | 0  1 | N / A | 0  1 | Input / Output |
| Logic XOR | 0  1 | N / A | 0  1 | Input / Output |
| Position Average | 0.000 to 1.00 | N / A | 0.000 to 1.00 | Input / Output |
| Position Difference | 0.000 to 1.00 | N / A | 0.000 to 1.00 | Input / Output |
| Position Equal | 0  1 | N / A | 0  1 | Input / Output |
| Position Greater | 0  1 | N / A | 0  1 | Input / Output |
| Position Invert | 0.000 to 1.00 | N / A | 0.000 to 1.00 | Input / Output |
| Position Less | 0  1 | N / A | 0  1 | Input / Output |
| Position Maximum | 0.000 to 1.00 | N / A | 0.000 to 1.00 | Input / Output |
| Position Minimum | 0.000 to 1.00 | N / A | 0.000 to 1.00 | Input / Output |
| Position Product | 0.000 to 1.00 | N / A | 0.000 to 1.00 | Input / Output |
| Position Sum | true / false | N / A | 0.000 to 1.00 | Input / Output |
| String Equal | string entry | true/false | N/A | Input / Output |
| Value Absolute Value | 0.000 to 1.00 | N / A | 0.000 to 1.00 | Input / Output |
| Value Average | 0.000 to 1.00 | N / A | 0.000 to 1.00 | Input / Output |
| Value Difference | 0.000 to 1.00 | N / A | 0.000 to 1.00 | Input / Output |
| Value Equal | 0  1 | N / A | 0  1 | Input / Output |
| Value Greater | 0  1 | N / A | 0  1 | Input / Output |
| Value Less | 0  1 | N / A | 0  1 | Input / Output |
| Value Maximum | 0.000 to 1.00 | N / A | 0.000 to 1.00 | Input / Output |
| Value Minimum | 0.000 to 1.00 | N / A | 0.000 to 1.00 | Input / Output |
| Value Negate | 0.000 to 1.00 | N / A | 0.000 to 1.00 | Input / Output |
| Value Product | 0.000 to 1.00 | N / A | 0.000 to 1.00 | Input / Output |
| Value Quotient | 0.000 to 1.00 | N / A | 0.000 to 1.00 | Input / Output |
| Value Square | 0.000 to 1.00 | N / A | 0.000 to 1.00 | Input / Output |
| Value Square Root | 0.000 to 1.00 | N / A | 0.000 to 1.00 | Input / Output |
| Value Sum | 0.000 to 1.00 | N / A | 0.000 to 1.00 | Input / Output |
