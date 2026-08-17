# Status Combiner

> Source: https://help.qsys.com/Content/Schematic_Library/status_combiner.htm

# Status Combiner

The Status Combiner component collects Status from multiple components via the Status Control Pins of the components. The Status Combiner presents a unified view containing the worst status of all the inputs. For example, if some of the inputs are OK, some Compromised and some Fault, the Status Combiner reports "Fault - < *name of first fault*> < *reason for first fault*>, < *label for next fault*> < *reason for next fault*>, and so on.

You can use one Status Combiner to collect the status of a single rack room, another for a second rack room, then another to combine those two.

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Schematic Example](javascript:void(0))

In this example, a Status Combiner is monitoring the status of 11 individual speaker components.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Status Combiner Properties

#### Input Count

Sets the number of inputs available, from 1 to 512.

[Controls](javascript:void(0))

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

**Note:** The `string` name of each status is listed by `value`. The priority is the highest `value`, so it is from the bottom of the table up.

| Value | Status |
| --- | --- |
| 0 | OK |
| 1 | Comprised |
| 2 | Fault |
| 3 | Not Found |
| 4 | Missing |
| 5 | Initialization |

#### OK

LED indicating that the status of all connected components is OK. Does not illuminate if any of the components are in a Compromised or Fault condition.

#### Compromised

LED indicating that one or more of the connected components is in a Compromised status.

#### Fault

LED indicating that one or more of the connected components is in a Fault status.

#### Input

A listing of the number of input connections as set in the Status Combiner Properties.

#### Disable

Toggle button that ignores input status for the specified input.

#### Suppress

Toggle button that suppresses the input of the associated component. When the Suppress button is on, and the status of the suppressed input changes, the Suppress button automatically turns off (un-suppresses), and the status of that item can be displayed.

#### Latch

Toggle button that holds the last received error/fault message for the specified input.

#### Reset

Momentary button that resets the latched error/fault status for the specified input.

#### Label

Text field. You can enter a user-defined name to identify the component associated with the input.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Combined Status | N / A | Text field | N / A | Output |
| Compromised | 0  1 | false  true | 0  1 | Output |
| Fault | 0  1 | false  true | 0  1 | Output |
| Label (1 - *n*) | N / A | User-defined | N / A | Input/Output |
| OK | 0  1 | false  true | 0  1 | Output |
| Disable (1 - *n*) | 0  1 | false  true | 0  1 | Input/Output |
| Suppress (1 - *n*) | 0  1 | false  true | 0  1 | Input/Output |
| Latch (1 - *n*) | 0  1 | false  true | 0  1 | Input/Output |
| Reset (1 - *n*) | 0  1 | false  true | 0  1 | Input/Output |
