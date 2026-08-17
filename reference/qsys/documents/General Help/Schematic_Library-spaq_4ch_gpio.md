# GPIO (SPA-Qf Series)

> Source: https://help.qsys.com/Content/Schematic_Library/spaq_4ch_gpio.htm

# GPIO (SPA-Qf Series)

This topic describes how to configure and control the General Purpose Input Output (GPIO) hardware interface for SPA-Qf Series amplifiers in Q-SYS Designer.

The GPIO Controller is used to integrate Q-SYS with custom or third-party controls. Using the GPIO, Q-SYS can control external hardware and certain aspects of Q-SYS can be controlled by external hardware.

The GPIO Interface is physical hardware, and is represented in Q-SYS Designer by the GPIO component. There are four configurable GPIO pins on the GPIO component. You can configure these pins to be Digital Inputs, Digital Outputs, or Analog Inputs. Refer to the Properties section in this topic for details.

To see GPIO interface information, Example Applications, and Behavior During Boot-up and Redeploy for your device, visit [General Purpose Input Output (GPIO) Application](../Application_Integration/GPIO_Application/gpio_application_overview.htm).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### SPA-Qf Amplifier Properties

What you select in the Properties determines the use of that GPIO pin, unused, input, output, or clock.

#### GPIO Pin Selections

Digital Input (TTL 3.3V)

Analog Input (0 - 3.3V, low Z)

Digital Output (TTL 3.3V)

#### Model

Select the hardware model from the drop-down list.

#### Channel Configuration

Select the configuration needed for your venue.

**Note:** Eight-channel models have two sets of four channels for configuration.

* 4 Channel, A B C D
* 3 Channel, A+B C D | A B Bridged
* 2 Channel, A+B+C+D | A B Bridged C D Bridged

Channel configurations are as follows:

* Space between letters (A B C D) = single channels,
* "+" between letters (A+B) = bridged,
* no space between letters (ABCD) = parallel.

When you make your selection, then run the design, the configuration is made available to the amplifier. Follow the instructions on the amplifier display.

#### Standalone Mode

**Off** â Turns Standalone Mode off.

**One-to-all** â Input Channel 1 is routed to all outputs.

**Note:** See the [Standalone Mode](#Standalone) below for details.

[Controls](javascript:void(0))

The Controls are displayed in GPIO Pin number order, 1 through 4, from left to right in the Control Panel. For each control the Euro-style connector pin number is listed under the GPIO pin numbers.

#### Digital In (Indicator)

This LED lights when there is a Digital input of 1 (3.3V TTL) present.

#### Analog In Volts

The knob is not controllable by the user; it is just an indicator of the voltage that is coming in to that input pin.

#### Digital Out

This toggle button supplies:

* 0 VDC output in the 0 / Off position and
* 3.3 VDC output in the 1 / On position.

[Control Pins](javascript:void(0))

This component does not have any Control Pins aside from all four GPIO having an Output Pin.

[Standalone Mode](javascript:void(0))

Standalone Mode provides the capability to connect the inputs of an amplifier to the outputs when connection to the Core is lost. In addition you can boot the amplifier without a connection to the Core.

Two ways to engage the Standalone Mode. For either way you must enable the **Standalone Mode** in the Q-SYS Designer Properties for the amplifier.

1. Amplifier Loses Network Connection to the Core:
   1. When connection to the Core is lost, audio is interrupted, and the amplifier counts down the number of seconds (15-60) specified in the amplifier's Properties in the Q-SYS design.
   2. After the timeout period, the inputs of the amplifier are sent directly to the outputs.
   3. When the connection to the Core is restored, the original audio streams are restored. There will be a short drop in audio while the amplifier is re-initialized.
2. Boot the Amplifier Without a Connection to the Core
   1. The amplifier waits 10 seconds to determine if the connection to the Core can be made.
   2. The amplifier then launches the last design run if it had the Standalone Mode enabled.
   3. When the amplifier re-connects to the Core, the Core pushes the design to the amplifier and the original audio is restored. There is a short loss of audio while the amplifier is initialized.
