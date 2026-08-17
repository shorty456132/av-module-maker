# Relay Output (QIO-LVR4)

> Source: https://help.qsys.com/Content/Schematic_Library/lcqln_relay_out.htm

# Relay Output (QIO-LVR4)

The Relay Output component represents a Relay Output 1-4 on the [QIO-LVR4](../Hardware/IO_Expanders/QIO-LVR4.htm) device. Use the component to interface with various third-party devices such as lighting systems, motorized shades, and environmental systems. These relays allow the Q-SYS system to control these devices by opening or closing the relay contacts, effectively turning the connected devices on or off.

[Inputs and Outputs](javascript:void(0))

### Input Pins

#### Relay *n*

Controls the state of relay n.

### Output Pins

#### Relay *n*

Indicates the current state of relay n.

[Schematic Example](javascript:void(0))

In this example, controls from an interface are configured to open and close a relay. This type of control is typically used for a projector screen lift mechanism.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

### Relays 1-4

#### Open

The Open LED indicates that the Normally Open (NO) connection is connected to the Common (C) and the Normally Closed (NC) connection is open circuit.

#### Close

The Closed LED indicates that the Normally Closed (NC) connection is connected to the Common (C) and the Normally Open (NO) connection is open circuit.

#### Relay *n* Momentary Button

Press the button to place relay in Open position. Release the button to revert the relay to its default, Closed state.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins  Available |
| --- | --- | --- | --- | --- |
| Relay 1-4 | | | | |
| Close LED | 0  1 | false  true | 0  1 | Output |
| Open LED | 0  1 | false  true | 0  1 | Output |
