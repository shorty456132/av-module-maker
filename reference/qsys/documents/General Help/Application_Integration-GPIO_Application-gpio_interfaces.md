# GPIO Interface

> Source: https://help.qsys.com/Content/Application_Integration/GPIO_Application/gpio_interfaces.htm

# GPIO Interface

The General Purpose Input Output (GPIO) interface is used to integrate Q-SYS with custom or third-party controls. The GPIO allows you to control external hardware and certain aspects of Q-SYS using external hardware.

## Relay and Dry-Contact Outputs

In addition to logic-level GPIO pins, several Q SYS devices provide isolated dry-contact relay outputs for controlling external equipment that expects a simple contact closure. These relays are voltage-free contacts (NO / C / NC) and do not supply power; they are intended to switch external low-voltage control circuits (for example, screen, blind, power sequencer, or other contact closure inputs).

Dry-contact relay outputs are available on:

* Core510i â GPIO relay pins: RNO / RNC / RC, 30 V, 1 A.
* DCIO / DCIO-H â 4 relay outputs.
* CX-Q, CXD-Q, DPA-Q â amplifier GPIO relay block: RELAY NO / COM /NC.
* QIO-LVR4 â 4 relay outputs on a 12-pin Euro connector: NO, C, NC per relay.

Use these relay contacts when you need a voltage-free contact closure interface, rather than a powered or logic-level GPIO output.

[GPIO (Core 510i)](javascript:void(0))

[GPIO DA-15 Connector Pinout](javascript:void(0))

| DB-15 Pin # | Signal Name | Signal Type | Description |
| --- | --- | --- | --- |
| 1 | RNO | Relay Contact | Relay Normally Open [1](#Q-SYS_Design) |
| 2 | RNC | Relay Contact | Relay Normally Closed [1](#Q-SYS_Design) |
| 3 | GPIO-1 | Normal Current | Configurable [2](#Word_Clock) |
| 4 | GPIO-3 | Normal Current | Configurable |
| 5 | Power | Power | +12 VDC |
| 6 | GPIO-5 | High Current | Configurable |
| 7 | GPIO-7 | High Current | Configurable |
| 8 | GND | Ground | Ground |
| 9 | RC | Relay Common | Relay Common [1](#Q-SYS_Design) |
| 10 | GND | Ground | Ground |
| 11 | GPIO-2 | Normal Current | Configurable |
| 12 | GPIO-4 | Normal Current | Configurable |
| 13 | Power | Power | +12 VDC |
| 14 | GPIO-6 | High Current | Configurable |
| 15 | GPIO-8 | High Current | Configurable |
|  |  |  |  |
| --- | --- | --- | --- |
| 1. The GPIO Relay is controlled in a Q-SYS Design.2. When Using a Word Clock. The GPIO input impedance is much higher than what would normally be required to terminate a word clock signal. QSC recommends using a termination resistor between pin 3 and ground (pin 8 or 10). The resistor value should match the cable impedance. If the cable impedance is unknown, use 75 Ohm. Refer to the [GPIO component](../../Schematic_Library/gpio.htm#Clock) for more information about external clocks. | | | |

[Specifications](javascript:void(0))

| Name | Normal Current Pins | High Current Pins |
| --- | --- | --- |
| Maximum Input Range | 0 V to 32 V | 0 V to 32 V |
| Analog Input Range | 0 V to 24 V | 0 V to 24 V |
| Digital Input, Low | 0.8 V maximum | 0.8 V maximum |
| Digital Input, High | 2.0 V minimum | 2.0 V minimum |
| Digital Output, Low | 0.4 V maximum | 0.4 V maximum |
| Digital Output, High | 2.4 V minimum, 3.3 V maximum | 2.4 V minimum, 3.3 V maximum |
| Digital Output Impedance | 1 k ohm | 1 k ohm |
| High Current Output, Low | N / A | 0.4 V maximum |
| High Current Output, High | N / A | 11 V minimum, 13 V maximum |
| High Current Output sink | 280 mA | 280 mA |
| High Current Output source | N / A | 280 mA |

| Specifications | | |
| --- | --- | --- |
| Relay Pins | Maximum Voltage, relative to Ground | 30 V |
| Maximum Current through Relay | 1 Amp |
| Power Pins | Output Voltage | 11 V min  13 V max |
| Maximum Output Current | 400 mA |
| All Power and High Current pins combined | Maximum Source Current | 400 mA |
| All GPIO Pins 1 through 8 combined | Maximum Sink Current | 1 A using 1 GND pin  2 A using 2 GND pins |

For more information on its properties, please visit [GPIO (Core 510i)](../../Schematic_Library/gpio.htm).

[GPIO (CX-Q, CXD-Q, DPA-Q Series)](javascript:void(0))

| Connector Pin | GPIO # and Function | Specification | 16-pin Euro Style Connector |
| --- | --- | --- | --- |
| **1** | 3.3 V | 100 mA max (power cycle to reset current limiting IC) |  |
| **2** | GPIO 1 | 5mA in/out, 3.3V max, 127 Ohm resistor in series |
| **3** | GPIO 2 | 5mA in/out, 3.3V max, 127 Ohm resistor in series |
| **4** | GND | Ground |
| **5** | GPIO 3 | 5mA in/out, 3.3V max, 127 Ohm resistor in series |
| **6** | GPIO 4 | 5mA in/out, 3.3V max, 127 Ohm resistor in series |
| **7** | GND | Ground |
| **8** | GPIO 5 | 18mA in/out max, 3.3V max, 127 Ohm resistor in series |
| **9** | RELAY NO | Relay Normally Open |
| **10** | RELAY COM | Relay Common |
| **11** | RELAY NC | Relay Normally Closed |
| **12** | GND | Ground |
| **13** | GPIO 6 | 18mA in/out max, 3.3V max, 127 Ohm resistor in series |
| **14** | GPIO 7 | 18mA in/out max, 3.3V max, 127 Ohm resistor in series |
| **15** | GND | Ground |
| **16** | GPIO 8 | 18mA in/out max, 3.3V max, 127 Ohm resistor in series |

For more information on its properties, please visit [GPIO (CX-Q, CXD-Q, DPA-Q Series)](../../Schematic_Library/amplifier_cxq_gpio.htm).

[GPIO (SPA-Qf Series)](javascript:void(0))

| Connector Pin | GPIO # and Function | Specification | 6-pin Euro Style Connector |
| --- | --- | --- | --- |
|  | 3.3V | 100 mA max (power cycle to reset current limiting) |  |
| 1 | GPIO 1 | 5mA in/out, 3.3V max, 127â¦ resistor in series |
| 2 | GPIO 2 | 5mA in/out, 3.3V max, 127â¦ resistor in series |
| 3 | GPIO 3 | 5mA in/out, 3.3V max, 127â¦ resistor in series |
| 4 | GPIO 4 | 5mA in/out, 3.3V max, 127â¦ resistor in series |
|  | GND | Ground |

For more information on its properties, please visit [GPIO (SPA-Qf Series)](../../Schematic_Library/spaq_4ch_gpio.htm).

[GPIO (Core 24f, I/O-Core 24f, Core 8 Flex)](javascript:void(0))

| Connector Pin | GPIO # and Function | Specification | 10-pin Euro Style Connector |
| --- | --- | --- | --- |
|  | 12V | 200 mA max (power cycle to reset current limiting) |  |
| 1 | GPIO 1 | 5mA in/out, 3.3V max, 127â¦ resistor in series |
| 2 | GPIO 2 | 5mA in/out, 3.3V max, 127â¦ resistor in series |
| 3 | GPIO 3 | 5mA in/out, 3.3V max, 127â¦ resistor in series |
| 4 | GPIO 4 | 5mA in/out, 3.3V max, 127â¦ resistor in series |
| 5 | GPIO 5 | 5mA in/out, 3.3V max, 127â¦ resistor in series |
| 6 | GPIO 6 | 5mA in/out, 3.3V max, 127â¦ resistor in series |
| 7 | GPIO 7 | 5mA in/out, 3.3V max, 127â¦ resistor in series |
| 8 | GPIO 8 | 5mA in/out, 3.3V max, 127â¦ resistor in series |
|  | GND | Ground |

For more information on its properties, please visit [GPIO In (Core 8 Flex , Core 24f, and I/O-Core 24f)](../../Schematic_Library/io8flex_gpio_input.htm) and [GPIO Out (Core 8 Flex , Core 24f, and I/O-Core 24f)](../../Schematic_Library/io8flex_gpio_output.htm).

[GPIO (Core 110f v1, I/O-Core 110f, Core 110c)](javascript:void(0))

| Connector Pin | GPIO # and Function | Specification | 10-pin Euro Style Connector |
| --- | --- | --- | --- |
|  | 12V | 200 mA max (power cycle to reset current limiting) |  |
| 1 | GPIO 1 | Configurable: Inputs (potentiometers) or Outputs (relays, LEDs); 3.3V Logic |
| 2 | GPIO 2 | Configurable: Inputs (potentiometers) or Outputs (relays, LEDs); 3.3V Logic |
| 3 | GPIO 3 | Configurable: Inputs (potentiometers) or Outputs (relays, LEDs); 3.3V Logic |
| 4 | GPIO 4 | Configurable: Inputs (potentiometers) or Outputs (relays, LEDs); 3.3V Logic |
| 5 | GPIO 5 | Configurable: Inputs (potentiometers) or Outputs (relays, LEDs); 3.3V Logic |
| 6 | GPIO 6 | Configurable: Inputs (potentiometers) or Outputs (relays, LEDs); 3.3V Logic |
| 7 | GPIO 7 | Configurable: Inputs (potentiometers) or Outputs (relays, LEDs); 3.3V Logic |
| 8 | GPIO 8 | Configurable: Inputs (potentiometers) or Outputs (relays, LEDs); 3.3V Logic |
|  | GND | Ground |

For more information on its properties, please visit [GPIO In (Core 110f, I/O-Core 110f, Core 110c)](../../Schematic_Library/io110_gpio_input.htm) and [GPIO Out (Core 110f, I/O-Core 110f, Core 110c)](../../Schematic_Library/io110_gpio_output.htm).

[GPIO (NV-32-H)](javascript:void(0))

**Note:** The RS-232 and GPIO IN pins share a 5-pin Euro connector. You can use both connection types simultaneously.

| Connector Pin | GPIO # and Function | Specification | RS-232 5-pin Euro Connector |
| --- | --- | --- | --- |
| 1 | GPIO 1 | Digital Input (TTL 3.3 V) |  |
| 2 | GPIO 2 | Digital Input (TTL 3.3 V) |
| 3 | TX | Digital Output (TTL 3.3 V) |
| 4 | RX | Digital Output (TTL 3.3 V) |
|  | GND | Ground |

The GPIO In component represents the GPIO IN connection pins on the rear of the NV-32-H. Use one of the included 5-pin Euro connectors. For more information on its properties, please visit [GPIO In (NV-32-H)](../../Schematic_Library/vstreamer_gpio_input.htm) and [GPIO Out (NV-32-H)](../../Schematic_Library/vstreamer_gpio_output.htm).

[GPIO (QIO-GP8x8, QIO-FLEX4A, QIO-LVR4)](javascript:void(0))

[QIO-GP8x8](javascript:void(0))

The GPIO In component represents the GPIO INPUTS connection pins on the rear of the QIO-GP8x8. Use one of the included 10-position black Euro connectors.

| Connector Pin | GPIO # and Function | Specification | 10-pin Euro Style Connector |
| --- | --- | --- | --- |
|  | 12V | 200 mA max (power cycle to reset current limiting) |  |
| 1 | GPIO 1 | 0-24 V analog input or contact |
| 2 | GPIO 2 | 0-24 V analog input or contact |
| 3 | GPIO 3 | 0-24 V analog input or contact |
| 4 | GPIO 4 | 0-24 V analog input or contact |
| 5 | GPIO 5 | 0-24 V analog input or contact |
| 6 | GPIO 6 | 0-24 V analog input or contact |
| 7 | GPIO 7 | 0-24 V analog input or contact |
| 8 | GPIO 8 | 0-24 V analog input or contact |
|  | GND | Ground |

[QIO-FLEX4A](javascript:void(0))

The GPIO In component represents the GPIO INPUTS connection pins on the rear of the QIO-FLEX4A. Use one of the included 14-position black Euro connectors.

| Connector Pin | GPIO # and Function | Specification | 14-pin Euro Style Connector |
| --- | --- | --- | --- |
|  | 12V | 200 mA max (power cycle to reset current limiting) |  |
| 1 | GPIO In 1 | Input, 0-24 V analog input or contact |
| 2 | GPIO In 2 | Input, 0-24 V analog input or contact |
| 3 | GPIO In 3 | Input, 0-24 V analog input or contact |
| 4 | GPIO In 4 | Input, 0-24 V analog input or contact |
| 1 | GPIO Out 1 | Digital Output (TTL 3.3V) |
| 2 | GPIO Out 2 | Digital Output (TTL 3.3V) |
| 3 | GPIO Out 3 | Digital Output (TTL 3.3V) |
| 4 | GPIO Out 4 | Digital Output (TTL 3.3V) |
| 5 | GPIO Out 5 | Digital Output (TTL 3.3V) |
| 6 | GPIO Out 6 | Digital Output (TTL 3.3V) |
| 7 | GPIO Out 7 | Digital Output (TTL 3.3V) |
| 8 | GPIO Out 8 | Digital Output (TTL 3.3V) |
|  | GND | Ground |

[QIO-LVR4](javascript:void(0))

| Connector Pin | Description | Specification | 12-pin, 3.5 mm Euro Connector |
| --- | --- | --- | --- |
| 1 | Relay 1 Normally Closed | 30 V AC/DC at 1A |  |
| 2 | Relay 1 Contact | 30 V AC/DC at 1 A |
| 3 | Relay 1 Normally Closed | 30 V AC/DC at 1 A |
| 4 | Relay 2 Normally Open | 30 V AC/DC at 1 A |
| 5 | Relay 2 Contact | 30 V AC/DC at 1 A |
| 6 | Relay 2 Normally Closed | 30 V AC/DC at 1 A |
| 7 | Relay 3 Normally Open | 30 V AC/DC at 1 A |
| 8 | Relay 3 Contact | 30 V AC/DC at 1 A |
| 9 | Relay 3 Normally Closed | 30 V AC/DC at 1 A |
| 10 | Relay 4 Normally Open | 30 V AC/DC at 1 A |
| 11 | Relay 4 Contact | 30 V AC/DC at 1 A |
| 12 | Relay 4 Normally Closed | 30 V AC/DC at 1 A |

For more information on its properties, please visit [GPIO In (QIO Devices)](../../Schematic_Library/lcqln_gpio_in.htm) and [GPIO Out (QIO Series)](../../Schematic_Library/lcqln_gpio_out.htm)
