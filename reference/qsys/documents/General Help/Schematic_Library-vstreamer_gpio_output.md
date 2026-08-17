# GPIO Out (NV-32-H)

> Source: https://help.qsys.com/Content/Schematic_Library/vstreamer_gpio_output.htm

# GPIO Out (NV-32-H)

The NV-32-H includes three General Purpose Output pins for extension of Q-SYS Control to third-party devices. In the Q-SYS Designer component properties, you can configure the output signal type for each pin â digital, open collector, or raw.

To see GPIO interface information, Example Applications, and Behavior During Boot-up and Redeploy for your device, visit [General Purpose Input Output (GPIO) Application](../Application_Integration/GPIO_Application/gpio_application_overview.htm).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### GPIO-1, 2, 3 Type

Select the type of GPIO output:

* Digital Output (TTL 3.3V): 3.3VDC is supplied to the GPIO output pin when the Output control is enabled.
* Open Collector (200mA): 24V, 200mA max with pull-up to +3.3V.
* Raw: This mode is for advanced capabilities. If there is something you cannot do using the other choices, contact Q-SYS Support for assistance.

[Controls](javascript:void(0))

#### Output

This button sends a 0 in the Off position and a 1 (3.3V TTL) in the On position.

#### Invert

This button is available when the Type is Raw.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Output  (Digital Output, Open Collector, Raw) | 0  1 | false  true | 0  1 | Input |
| Invert[1](#Availabl) | 0  1 | false  true | 0  1 | Input / Output |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1. Available in the Control Pins list when Type is set to Raw. | | | | |
