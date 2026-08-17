# GPIO In (Core 110f, I/O-Core 110f, Core 110c)

> Source: https://help.qsys.com/Content/Schematic_Library/io110_gpio_input.htm

# GPIO In (Core 110f, I/O-Core 110f, Core 110c)

The General Purpose Input Output (GPIO) is used to integrate Q-SYS with custom or third-party controls. Using the GPIO Output you can control external hardware. With the GPIO Input, you can control certain aspects of Q-SYS using external hardware.

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

### GPIO 1 -16 Type

#### GPIO Type 1-16

* Digital Input (TTL 3.3V)
* Contact Closure Input
* Potentiometer (10k ohm, 12V)
* Potentiometer (2-wire)
* Analog Input (0-24V, Low z)
* Raw

[Controls](javascript:void(0))

The following table describes the controls available in the GPIO Input Control Panel.

#### Digital Input (LED)

This LED illuminates when there is a digital input on a GPIO pin. Each of the following Types of input has an LED to indicate a digital input is present:

* Digital Input (+3.3VDC)
* Contact Closure â When this Type is selected, the pin has approximately 9 to 10VDC present when the contact is open (or nothing is connected) and the LED is off. When the contact is closed (pin is shorted to ground), the LED is on.
* Raw

#### Analog Input (Knob)

The analog input knob is provided when one of two Input Types is selected.

* Analog â allows a low impedance, 0 â 24VDC signal input
* Raw

Both input voltages are displayed on a read-only knob control.

#### Potentiometer

The Potentiometer knob follows the position of the physical potentiometer connected to the GPIO pin. To calibrate Q‑Sys to the potentiometer:

1. Turn the physical potentiometer to its minimum position.
2. Click the Calibrate Min button. A value displays in the Min Position field.
3. Turn the physical potentiometer to its maximum position.
4. Click the Calibrate Max button. A value displays in the Max Position field.

If you know the values for Min Position and/or Max Position, you can enter them manually.

#### Pullup Enable

Provides a 5.11K Pullup resistor to +12VDC on the input pin when the Type is Raw.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**. Each of the following Control Pins are available on all GPIO Input pins.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Digital Input  (LED) | 0  1 | false  true | 0  1 | Output |
| Contact Closure (LED) | 0  1 | false  true | 0  1 | Output |
| Potentiometer | 0 to 1.00 | 0 to 1.00 | 0 to 1.00 | Output |
| Minimum Position [1](#Selectable_Pins) | 0 to 1.00 | 0 to 1.00 | 0 to 1.00 | Input / Output |
| Minimum Calibrate [1](#Selectable_Pins) | 0  1 | false  true | 0  1 | Input / Output |
| Maximum Position [1](#Selectable_Pins) | 0 to 1.00 | 0 to 1.00 | 0 to 1.00 | Input / Output |
| Maximum Calibrate [1](#Selectable_Pins) | 0  1 | false  true | 0  1 | Input / Output |
| Analog Input  (Knob) | 0 to 24 | *nn.nnn*V | 0 to 1.00 | Output |
| Raw |  |  |  |  |
| Digital Input  (LED) | 0  1 | false  true | 0  1 | Output |
| Analog Input  (Knob) | 0 to 24 | *nn.nnn*V | 0 to 1.00 | Output |
| Pullup Enable | 0  1 | false  true | 0  1 | Output |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1. These control pins are selectable in the Control Pins list at the bottom of the GPIO selections. You must select the Type (Potentiometer or Raw) to make these Control Pins accessible. | | | | |
