# GPIO In (NV-32-H)

> Source: https://help.qsys.com/Content/Schematic_Library/vstreamer_gpio_input.htm

# GPIO In (NV-32-H)

The NV-32-H includes two General Purpose Input pins for extension of Q-SYS Control to third-party devices. In the Q-SYS Designer component properties, you can configure the input signal type for each pin â contact closure, digital, analog, potentiometer, or raw.

To see GPIO interface information, Example Applications, and Behavior During Boot-up and Redeploy for your device, visit [General Purpose Input Output (GPIO) Application](../Application_Integration/GPIO_Application/gpio_application_overview.htm).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### GPIO-1, 2 Type

Select the type of GPIO input:

* Digital Input (TTL 3.3V)
* Contact Closure Input
* Potentiometer (10k Ohm, 12V)
* Potentiometer (2-wire)
* Analog Input (0-24V, low z)
* Raw

[Controls](javascript:void(0))

#### Digital Input

This LED illuminates when there is a digital input present on a GPIO pin. Supported Types:

* Digital Input (+3.3VDC)
* Contact Closure â When this Type is selected, the pin has approximately 9 to 10VDC present when the contact is open (or nothing is connected) and the LED is off. When the contact is closed (pin is shorted to ground), the LED is on.
* Raw

#### Analog Input

The analog input knob appears for these Types:

* Analog â allows a low impedance, 0 â 24VDC signal input
* Raw

Both input voltages are displayed on a read-only knob control.

#### Potentiometer: Min Position, Calibrate Min, Max Position, Calibrate Max

The Potentiometer knob follows the position of the physical potentiometer connected to the GPIO pin. To calibrate Q-SYS to the potentiometer:

1. Turn the physical potentiometer to its minimum position.
2. Click the Calibrate Min button. A value displays in the Min Position field.
3. Turn the physical potentiometer to its maximum position.
4. Click the Calibrate Max button. A value displays in the Max Position field.

If you know the values for Min Position or Max Position, you can enter them manually.

#### Pullup Enable

When enabled, provides a 5.11K pull-up resistor to +12VDC on the input pin when the Type is Raw.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Digital Input | 0  1 | false  true | 0  1 | Output |
| Contact Closure | 0  1 | false  true | 0  1 | Output |
| Potentiometer Position | 0 to 1.00 | 0 to 1.00 | 0 to 1.00 | Output |
| Calibrate Maximum[1](#Availabl) | 0  1 | false  true | 0  1 | Input |
| Calibrate Minimum[1](#Availabl) | 0  1 | false  true | 0  1 | Input |
| Maximum Position[1](#Availabl) | 0 to 1.00 | 0 to 1.00 | 0 to 1.00 | Input / Output |
| Minimum Position[1](#Availabl) | 0 to 1.00 | 0 to 1.00 | 0 to 1.00 | Input / Output |
| Analog Input | 0 to 24 | *nn.nnn*V | 0 to 1.00 | Output |
| Raw | | | | |
| Analog Input | 0 to 24 | *nn.nnn*V | 0 to 1.00 | Output |
| Digital Input | 0  1 | false  true | 0  1 | Output |
| Pullup Enable[2](#Availabl2) | 0  1 | false  true | 0  1 | Input |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1. Available in the Control Pins list when Type is set to Potentiometer.2. Available in the Control Pins list when Type is set to Raw. | | | | |
