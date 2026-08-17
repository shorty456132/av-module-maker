# GPIO (CX-Q, CXD-Q, DPA-Q Series)

> Source: https://help.qsys.com/Content/Schematic_Library/amplifier_cxq_gpio.htm

# GPIO (CX-Q, CXD-Q, DPA-Q Series)

This topic describes how to configure and control the General Purpose Input Output (GPIO) hardware interface for CX-Q, CXD-Q, and DPA-Q amplifiers in Q-SYS Designer.

The GPIO Controller is used to integrate Q-SYS with custom or third-party controls. Using the GPIO, Q-SYS can control external hardware and certain aspects of Q-SYS can be controlled by external hardware.

The GPIO Interface is physical hardware, and is represented in Q-SYS Designer by the GPIO component. There are eight configurable GPIO pins on the GPIO component. You can configure these pins to be Digital Inputs, Digital Outputs, Analog Inputs, or PWM Output. Refer to the Properties section in this topic for details.

To see GPIO interface information, Example Applications, and Behavior During Boot-up and Redeploy for your device, visit [General Purpose Input Output (GPIO) Application](../Application_Integration/GPIO_Application/gpio_application_overview.htm).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### CX-Q Amplifier Properties

What you select in the Properties determines the use of that GPIO pin, unused, input, output, or clock.

#### GPIO Pin Selections

Unused

Digital Input (TTL 3.3 VDC @ 2 mA)

Analog Input

Digital Output

PWM Output *(Only available for pins 1-4 and 6.)*

#### Channel Configuration

Select the configuration needed for your venue.

**Note:**  Eight-channel models have two sets of four channels for configuration.

* 4 Channel, A B C D
* 3 Channel, A+B Bridged
* 2 Channel, A+B Bridged C+D Bridged
* 3 Channel, AB Parallel
* 2 Channel, AB Parallel C+D Bridged
* 2 Channel, A B Parallel C D Parallel
* 1 Channel, A B Parallel Bridged with CD Parallel
* 2 Channel, A B C Parallel
* 1 Channel, A B C D Parallel

Space between letters (A B C D) = single channels, "+" between letters (A+B) = bridged, no space between letters (ABCD) = parallel. When you make your selection, then run the design, the configuration is made available to the amplifier. Follow the instructions on the amplifier display.

#### Standalone Mode

Standalone Mode provides the capability to connect the inputs of an amplifier to the outputs when connection to the Core is lost. In addition you can boot the amplifier without a connection to the Core.

* Off â Turns Standalone Mode off.
* One-to-one â Each audio input is routed to its corresponding output Ch1 â Output A, Ch2 â Output B, Ch3 â Output C, Ch4 â Output D.
* One-to-all â Input Channel 1 is routed to all outputs.

[Controls](javascript:void(0))

The Controls are displayed in GPIO Pin number order, 1 through 8, from left to right in the Control Panel. For each control the Euro-style connector pin number is listed under the GPIO pin numbers. Refer to the GPIO Interface section in this topic.

#### Digital In (Indicator)

This LED lights when there is a Digital input of 1 (3.3 V TTL) present.

#### Analog In Volts

This knob controls the analog input level up to 3.3 V

#### Digital Out

This toggle button supplies:

* 0 VDC output in the 0/Off position and
* 3.3 VDC output in the 1/On position.

#### PWM Duty %

Sets the duty cycle of the pulse.

#### PWM Invert

Inverts the PWM pulse.

#### PWM Frequency Hz

Sets the frequency of the pulse. If there are multiple PWM assignments for one amplifier, all are controlled by the same frequency control.

#### Relay

This button changes position of the internal relay.

[Control Pins](javascript:void(0))

There is one control pin for each GPIO pin that has either Digital Input, Analog Input or Digital Output selected in the Properties. The GPIO Pins that have Unused will not have a Control Pin associated with it. For PWM there is a Duty and Invert for each PWM selected in the Properties, and one PWM Frequency for all of the PWM Outputs are selected in the Properties.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Digital Input | 0  1 | false  true | 0  1 | Output |
| Analog Input | 0 to 3.3 | 0.00 V to 3.3 V | 0 to 1.00 | Output |
| Digital Output | 0  1 | false  true | 0  1 | Input / Output |
| PWM Duty | 0 to 100 | â | 0 to 1.00 | Input / Output |
| PWM Invert | 0 to 100 | â | 0 to 1.00 | Input / Output |
| PWM Frequency | 5.00 to 1000 | 5.00 Hz to 50 kHz | 0 to 1.00 | Input / Output |
| Relay Out | 0  1.00 | false (normal)  true (activated) | 0  1.00 | Input / Output |
