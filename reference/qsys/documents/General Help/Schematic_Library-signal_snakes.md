# Signal Snakes

> Source: https://help.qsys.com/Content/Schematic_Library/signal_snakes.htm

# Signal Snakes

Signal Snakes provide the means to reduce a set of signals to a single graphical wire or named signal, similar to wrapping a number of wires into a bundle. Signal Snakes are comprised of two components: a **Signal Snake Input**, and a **Signal Snake Output**. Signal Snakes can have from 1 to 256 channels, and the signal types of those channels can be mixed.

[Inputs and Outputs](javascript:void(0))

Signal Snake pins are unique; they change based on the type of pin to which they are connected.

* The exceptions are the Snake Input and Snake Output pins which are represented by the following polygon.
* The Input and Output Channels, prior to making any connections, are represented by a diamond shape .

**Tip:** The number of signal pins is variable and set in the component's **Channel Count** Property.

[Schematic Examples](javascript:void(0))

[Example 1: Using Signal Snakes](javascript:void(0))

These Signal Snakes were created by dragging out the Signal Snake Input and Signal Snake Output components.

[Example 2: Using Component Pins](javascript:void(0))

These Signal Snakes were created from selecting component pins.

[Example 3: Using Mixers](javascript:void(0))

These Signal Snakes were created by wiring the Mixer's pins to the Signal Snake pins and then connecting the Snakes.

[Creating Signal Snakes](javascript:void(0))

1. Select one or more pins on one or more components.
2. Click one of the pins and begin dragging away from the component.
3. Press the space bar. The Signal Snake is created.

OR

1. Drag a **Signal Snake Input** and/or **Signal Snake Output**, from the Schematic Library > Layout section, into the Schematic.
2. Manually wire the Signal Snakes to and from the desired components.

Or, you can copy and paste Signal Snakes.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Signal Snake Properties

#### Channel Count

Signal Snakes can have from 1 to 256 channels, and the signal types of those channels can be mixed. The default number is 8.

[Controls](javascript:void(0))

This component has no configurable controls.

[Control Pins](javascript:void(0))

This component has no control pins.

[Troubleshooting](javascript:void(0))

### Using Signal Snakes Inside Containers

As you copy and paste the Signal Names to the input / output they belong, the Signal Name will enumerate to prevent multiple connections on the same input / output.

**Tip:** When copying and pasting a Signal Name to any input/ output inside of a Container, be sure to use the correct Signal Name to the correct input / output.
