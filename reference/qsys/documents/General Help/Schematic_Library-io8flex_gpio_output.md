# GPIO Out (Core 8 Flex , Core 24f, and I/O-Core 24f)

> Source: https://help.qsys.com/Content/Schematic_Library/io8flex_gpio_output.htm

# GPIO Out (Core 8 Flex , Core 24f, and I/O-Core 24f)

The General Purpose Input/Output (GPIO) connections allow the
Q-SYS network to interface with miscellaneous outside devices, such as LED indicators, switches,
relays, and potentiometers, and with custom or third-party controls. Using the GPIO Out you can control external hardware.

The GPIO pins in Q-SYS Designer are representative of the pins on the color-coded (typically black) Euro-style connector on the rear panel of the device. The numbers stamped on the rear panel relate to the GPIO pins in Q-SYS Designer. The first and last pins are not numbered as they are not GPIO pins but a DC reference voltage and ground, respectively.

To see GPIO interface information, Example Applications, and Behavior During Boot-up and Redeploy for your device, visit [General Purpose Input Output (GPIO) Application](../Application_Integration/GPIO_Application/gpio_application_overview.htm).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### GPIO 1-8

#### Type

Select one of the following for each of the 8 GPIO pins that you use.

* Digital Output (TTL 3.3V) â 3.3VDC is supplied to the GPIO Output pin when the Output button is On.
* Open Collector (24V, 200mA Max), with Pullup to 3.3V
* Raw â The Raw mode is for advanced capabilities. If there is something you cannot do in the standard choices, contact QSC Support for detailed information. Note that when you select Raw as the direction, there are two instances of that pin on the GPIO component; one input, and one output.

[Controls](javascript:void(0))

#### Output

This button supplies a 0 in the Off position and a 1 (3.3V TTL) in the On position.

#### Invert

Available when the Properties > Type is Raw. The Raw mode is for advanced capabilities. If there is something you cannot do in the standard choices, contact QSC Support for detailed information.

[Control Pins](javascript:void(0))

The Control Pins that show, depend on the type of GPIO in use. You must select the Type (Raw) to make this Control Pins accessible.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Output | 0  1 | false  true | 0  1 | Input |
| Invert | 0  1 | false  true | 0  1 | Input / Output |
