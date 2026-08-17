# GPIO (Core 510i)

> Source: https://help.qsys.com/Content/Schematic_Library/gpio.htm

# GPIO (Core 510i)

This topic describes how to configure and control the General Purpose Input Output (GPIO) hardware interfaces in Q-SYS Designer.

To see GPIO interface information, Example Applications, and Behavior During Boot-up and Redeploy for your device, visit [General Purpose Input Output (GPIO) Application](../Application_Integration/GPIO_Application/gpio_application_overview.htm).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Slot A-H

#### Card Type

Identifies the type of I/O card installed in the physical Core. After you make your selection, the I/O card displays under the Core in the Inventory list. The number of I/O Slots varies depending on the Core Model. Choices of I/O card installed are:

* Blank
* Line Out
* Mic/Line in H.P.
* DataPort Out
* AES3 In/Out
* Mic/Line In Std.
* CobraNet
* Dante
* AVB
* 16-Channel AES3 In
* POTS

### GPIO 1-8 (DA-15 Pins)

[Direction](javascript:void(0))

There are four possible "Directions" you can select for the GPIO pins.

#### Unused

The default position, and anytime the GPIO Pin is not in use

#### Input

Devices or signals connected to a configurable pin provide an input to the Q-SYS system.

#### Output

The Q-SYS hardware will be providing signals to devices connected to configurable pins.

#### Raw

The Raw mode is for advanced capabilities. If there is something you cannot do in the standard choices, contact QSC Support for detailed information.

[Type Settings when the Direction is Input](javascript:void(0))

| Property | GPIO Pins | Value |
| --- | --- | --- |
| Input used as clock source | 3 | When the Core Clock Source Property is set to GPIO A-1 or GPIO B-1, this GPIO is used only for the clock source.  The GPIO selections require an external TTL level word clock: pin 3 is signal, pin 8 is ground. When you select GPIO A-1 or GPIO B-1 as the clock source, the respective GPIO 1 Property changes to "Input used as clock source". The clock source should be connected to pin 3 of the respective GPIO connector - either GPIO A or GPIO B.  **Note:** Typically, Internal is used as the clock source. Only if there is a need to synchronize the Q-SYS system to an external clock would you use GPIO or AES3. You would use GPIO if the external clock signal is a word clock. You would use AES3 if the external clock signal is an AES3 signal. Often an AES3 signal without audio is used to reduce the clock jitter. This signal is called AES3 black. |
| Digital  (TTL 3.3 VDC @ 2 mA) | 1 to 8 | Digital zero = 0  Digital one = 3.3 |
| Potentiometer  (10 k Ohm, 12 V) | 1 to 8 | Allows a potentiometer to be connected to the GPIO pin, the position of which is represented by the control in the GPIO Control Panel. The value or range is 0 to 1. |
| Analog  (0-24 V. Low Z) | 1 to 8 | Input 0 to 24 V, Low Z  12-bit Resolution |
| Contact Closure | 1 to 8 | Allows a button, switch, or other binary device to be connected to the GPIO Relay contact. |
| WCP-1 | 1 to 8 | Interfaces with QSC's Wall Control Plate, version 1. For more information, see the [Self Help Portal](https://qsc.my.site.com/selfhelpportal/s/global-search/WCP). |
| WCP-2 (3 pins) | 1-3 and/or 5-7 | Selectable on GPIO pins 1 and 5 only. Interfaces with QSC's Wall Control Plate, version 2. Requires three configurable pins. For more information, see the [Self Help Portal](https://qsc.my.site.com/selfhelpportal/s/global-search/WCP). |
| Optical Rotary Encoder  (requires 2 pins) | 1-2, 3-4, 5-6, or 7-8 | Allows an Optical Rotary Encoder to be connected to two configurable pins. |
| Mechanical Rotary Encoder  (requires 2 pins) | 1-2, 3-4, 5-6, or 7-8 | Allows a Mechanical Rotary Encoder to be connected to two configurable pins. |

[Type Settings when the Direction is Output](javascript:void(0))

| Property | GPIO Pins | Value |
| --- | --- | --- |
| Digital Output | 1 to 8 | Digital zero = 0  Digital one = 1 |
| Pulse Width Modulated (PWM) Output  Good for operating a Fan or a DC motor that will likely require 12 V High Drive, High Current. | 1 to 8 | Pulse Width is set in the Control Panel 0 - 100%  Pulse Frequency is set in the Control Panel 50 to 50,000 Hz |
| Inverted Pulse Width Modulated (PWM) Output  If this pin is used in conjunction with the non-inverted PWM, linking the PWM Duty Control Pins together will produce opposite but equal signals since they must use the same frequency. | 1 to 8 | Pulse Width is set in the Control Panel 0 - 100%  Pulse Frequency is set in the Control Panel 50 to 50,000 Hz |
| No Clock output available on these pins | 1 and 5 | N / A |
| Sample Clock | 2 and 6 | System Frequency  48 kHz |
| Vector Clock | 3 and 7 | 3 kHz  6 kHz |
| Frame Clock  Mainly intended for software debug. | 4 and 8 | Programmable - 30 Hz to 120 Hz |

[Drive Settings when the Direction is Output](javascript:void(0))

| Property | Value |
| --- | --- |
| GPIO Pins 1 - 4 | 3.3 V TTL  Open Collector High Current |
| GPIO Pins 5 - 8 | 3.3 V TTL  12 V Push-Pull High Current  12 V High-Drive High Current  Open Collector High Current |

[When the Direction is Raw](javascript:void(0))

The Raw mode is for advanced capabilities. If there is something you cannot do in the standard choices, contact QSC Support for detailed information. Note that when you select Raw as the direction, there are two instances of that pin on the GPIO component; one input, and one output.

[Controls](javascript:void(0))

The Controls are displayed in GPIO Pin number order, 1 through 8, from left to right in the Control Panel with the related DA-15 pin number listed. The DA-15 pin / GPIO pin number relationship can change based on the controls assigned to the GPIO pins.

### General

#### Relay

The function of the Relay button is to open and close the contacts of the relay on the GPIO Interface.

* RNO 1 (Relay Normally Open on DA-15 Pin 1)
* RNC 2 (Relay Normally Closed on DA-15 Pin 2)
* RC 9 (Relay Common on DA-15 Pin 9)

#### Digital In (Indicator)

This LED lights when there is a Digital input of 1 (3.3 V TTL) present.

#### Analog In (VDC)

This is a read-only knob that displays the DC voltage applied to the GPIO pin.

#### Digital Out

This toggle button supplies a 0 in the Off position and a 1 in the On position.

#### PWM Duty (Percentage)

Sets the percentage of a period when the pulse is positive.

#### PWM Frequency (Hz)

Sets the period time. (1 / frequency). Affects all PWM outputs.

[Control Pins](javascript:void(0))

The GPIO pins display as control pins on the GPIO component and are always present except when "Unused" is selected for a pin's Direction. The GPIO pins are not used to change controls in the Control Panel. Some of the Direction/Type combinations provide Control Pins you can use to change the Controls within the Control Panel.

[General](javascript:void(0))

The Relay Out Control Pin is always available.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Relay Out | 0  1.00 | false (normal)  true (activated) | 0  1.00 | Input / Output |

[When the Direction is Input](javascript:void(0))

The Pin Name reflects the Input Type you select for a given GPIO pin. Indented below each GPIO Type are any Control Pins that may be available for that Type.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Digital Input | 0  1 | false  true | 0  1 | Output |
| Contact Closure | 0  1 | false  true | 0  1 | Output |
| Potentiometer (10k Ohm, 12 V) and Potentiometer (2-wire) | 0 to 1 | N / A | 0 to 1.00 | Output |
| Calibrate Maximum |  |  |  |  |
| Calibrate Minimum |  |  |  |  |
| Maximum Position |  |  |  |  |
| Minimum Position |  |  |  |  |
| Analog Input | 0 to 24.00 | 0.00 V to 24.0 V | 0 to 1.00 | Output |
| WCP-1 | 0.00  1.00  2.00  3.00  4.00  5.00  6.00  7.00  8.00  9.00  10.00 | 0  1  2  3  4  5  6  7  8  9  10 | 0  .100  .200  .300  .400  .500  .600  .700  .800  .900  1.00 | Output |
| WCP-2 | 1.00  2.00  3.00  4.00  5.00  6.00 | 1  2  3  4  5  6 | 0  .200  .400  .600  .800  1.00 | Output |
| Rotary Encoder (Mechanical or Optical) | 0 to 1.00 | N / A | 0 to 1.00 | Input / Output |
| Rotary Encoder Resolution | 4 to 4096 | 4 to 4096 | 0 to 1.00 | Input / Output |
| Rotary Encoder Reverse | 0  1.00 | normal  invert | 0 to 1.00 | Input / Output |

[When the Direction is Output](javascript:void(0))

The Pin Name reflects the Output Type that must be selected for a particular Control Pin to be available.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Digital Output [1](#Digital_Out) | 0  1 | false  true | 0  1 | Input / Output |
| PWM Output | 0 to 100 | â | 0 to 1.00 | Input / Output |
| PWM Duty | 0 to 100 | 0% to 100% | 0 to 1.00 | Input/Output |
| PWM Invert | 0  1.00 | normal  inverted | 0 to 1.00 | Input / Output |
| PWM Frequency | 5 to 50,000 | 5.00Hz to 50.0kHz | 0 to 1.00 | Input / Output |
| Inverted PWM Output | 0 to 100 | â | 0 to 1.00 | Input / Output |
| PWM Duty | 0 to 100 | 0% to 100% | 0 to 1.00 | Input/Output |
| PWM Invert | 0  1.00 | normal  inverted | 0 to 1.00 | Input / Output |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1. When Digital Output is selected, the Control Pin for the "Digital Out" button in the Control Panel displays as an input to the selected GPIO pin. It is not shown in the Control Pins list as other "Control Pins". | | | | |
