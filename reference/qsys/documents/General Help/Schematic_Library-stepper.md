# Value Stepper

> Source: https://help.qsys.com/Content/Schematic_Library/stepper.htm

# Value Stepper

The Value Stepper component makes it easy to increase or decrease values of a downstream component in integer, gain, or percentage terms.

[Configuration Overview](javascript:void(0))

1. Drag the Value Stepper component into your schematic.
2. Select the component to configure how the value of a downstream component is adjusted. See [Properties](#Properti).
3. Connect the Value Stepper component's Value control pin to the input control pin of another component.
4. Press F5 to save your design to the Core and run it. (Or, press F6 to emulate your design.)
5. Double-click the Value Stepper component to open its control panel and control the value of the downstream component. See [Controls](#Controls).

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Schematic Example](javascript:void(0))

In this example, the Value Stepper component Value control pin is wired to the Gain control pin of the [Gain](gain.htm) component. Value Stepper is configured to increase or decrease the gain from 0 to 10 integer steps. When clicking and holding the Increase or Decrease button, it takes 1.00 second to start ramping the value and 5.00 seconds to go from the minimum to maximum value.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Value Stepper Properties

#### Control Type

Select how to adjust the value of the downstream component.

#### Mode

With Gain as the selected Control Type, select whether the gain is adjusted in continuous fashion or in a discrete number of steps.

#### Number of Steps

With Control Type set to 'Integer' or Gain Mode set to 'Discrete', set how many steps it takes to go from the minimum gain value to the maximum gain value.

#### Max Gain (dB)

With Gain as the selected Control Type, set the maximum gain level.

#### Min Gain (dB)

With Gain as the selected Control Type, set the minimum gain level.

[Controls](javascript:void(0))

#### Value

Specify a value to send to the downstream component:

* For Integer, the value can range from 0 to the Number of Steps defined in Properties.
* For Gain, the value must be within the defined range for Max Gain and Min Gain.
* For Percent, the percentage applies to the range defined in the downstream component.

#### Increase

Click to increase the Value. Click and hold to continuously increase the Value according to the Hold Off and Time controls.

#### Decrease

Click to decrease the Value. Click and hold to continuously decrease the Value according to the Hold Off and Time controls.

#### Hold Off

When clicking and holding the Increase or Decrease buttons, this is the amount of time it takes before the value starts to ramp.

#### Time

When clicking and holding the Increase or Decrease buttons, this is the amount of time it takes to ramp from the minimum value to the maximum value.

#### Step Meter

If Control Type is set to 'Integer', this meter indicates the selected Value.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Value | (text) | | | Output |
| Decrease | 0  1 | false  true | â | Input / Output |
| Hold Off | 0.000 to 60.0 | 0ms to 60.0s | 0.000 to 1.00 | Input / Output |
| Increase | 0  1 | false  true | â | Input / Output |
| Time | 0.000 to 60.0 | 0ms to 60.0s | 0.000 to 1.00 | Input / Output |
