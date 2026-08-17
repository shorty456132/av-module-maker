# GPIO Out (Core 110f, I/O-Core 110f, Core 110c)

> Source: https://help.qsys.com/Content/Schematic_Library/io110_gpio_output.htm

# GPIO Out (Core 110f, I/O-Core 110f, Core 110c)

The General Purpose Input Output (GPIO) Controller is used to integrate Q-SYS with custom or third-party controls. Using the GPIO Output you can control external hardware. With the GPIO Input, you can control certain aspects of Q-SYS using external hardware.

**Note:** Use the [GPIO](core_status.htm#GPIO) property (in Core Properties) to toggle the GPIO In and Out components in the Inventory tree, depending on your Core 110 Series model. GPIO connections are not applicable to the Core 110f v2.

To see GPIO interface information, Example Applications, and Behavior During Boot-up and Redeploy for your device, visit [General Purpose Input Output (GPIO) Application](../Application_Integration/GPIO_Application/gpio_application_overview.htm).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### GPIO

(Core 110 Series models only)

This property determines whether to expose GPIO In and GPIO Out components in the Inventory tree.

* Disabled: GPIO components are not shown in the Inventory tree. Use this setting for Core 110v2, which does not include GPIO inputs and outputs.
* Enabled: (default) GPIO components are shown in the Inventory tree. Use this setting for Core 110f v1 or Core 110c, as these models include GPIO inputs and outputs.
* Optional: GPIO components are shown in the Inventory tree. However, reporting of Missing, Compromised, or Fault statuses related to the actual hardware presence of GPIO will not occur.

### GPIO 1-16

#### Type

Select one of the following for each of the 16 GPIO pins that you use.

* Digital Output (TTL 3.3V): 3.3VDC is supplied to the GPIO Output pin when the Output button is On.
* Open Collector (200 mA): 24V, 200 mA max, with Pullup to 3.3V.
* Raw: This mode is for advanced capabilities. If there is something you cannot do in the standard choices, contact QSC Support for detailed information. Note that when you select Raw as the direction, there are two instances of that pin on the GPIO component; one input, and one output.

[Controls](javascript:void(0))

#### Output

This button supplies a 0 in the Off position and a 1 (3.3V TTL) in the On position.

#### Pullup Enable

Available when the Properties > Type is Raw. The Raw mode is for advanced capabilities. If there is something you cannot do in the standard choices, contact QSC Support for detailed information.

[Control Pins](javascript:void(0))

The only Control Pin available under "Control Pins" in the Properties is Pullup Enable when you select Raw as the Type.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Output | 0  1 | false  true | 0  1 | Input |
| Pullup Enable | 0  1 | false  true | 0  1 | Input |
