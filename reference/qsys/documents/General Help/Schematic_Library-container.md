# Container

> Source: https://help.qsys.com/Content/Schematic_Library/container.htm

# Container

The Container is used to group components into a collapsible object. You can add as many components as you need as long as the combined audio and Control Pins do not exceed 100 inputs and 100 outputs coming in and out of the Container.

[Using the Container](javascript:void(0))

1. After dragging the Container Component into the Schematic, enter a Name, and select the Input Count and Output Count in the Properties.
2. If you select Password Protected - Yes:
   1. Enter a password. The password is case-sensitive.
   2. Press the Tab key or click in the Confirm field.
   3. Retype the password. Initially the popup is red, when both the password and confirmation are entered and agree, the popup turns green.
   4. Press Enter. When you attempt to open the Container's Control Panel you are prompted to enter the password in order to gain access.
   5. Notes:
      * If you attempt to change the Container's Password Protected Property from Yes to No, you must enter the password to make the change.
      * You can delete the password protected Container component without the password.
      * You can copy a password-protected Container, the password is copied to the new container.
      * Be sure you remember the password, if you forget, it cannot be retrieved.
3. Set the Input Count and Output Count, then open the Container's Control Panel, the Container is sized based on the number of inputs / outputs. You can re-size it to meet your needs.
   * You can size the container and move the connectors as needed.
4. The Input pins are on the left side of the Container, and are numbered to match the Input pins on the Container component.
5. The Output pins are on the right side of the Container, and are numbered to match the Output pins on the Container component.
6. You can add Panels to a container. After a panel is added, you can name the panels. The same capabilities exist for a panel that exist for the schematic page with the exception of wiring. Any components added to a panel must use [Signal Names](../Q-Sys_Designer/Using_the_Schematic/Connections_and_Wiring_in_the_Schematic.htm#Signal_Names) in order to connect between the panel and the schematic page both components and inputs / outputs.
7. If you delete a Container, all the components in the Container are deleted.
8. You can copy and paste Container components, including the components and wiring inside the Container component. If you copy and paste a Container with an Inventory component inside, a new Inventory component, of the same type, is added to your design's Inventory.
9. You can add any of the Inventory components except the Core and the I/O Frame, including any of their components.
10. You can drag controls from the control panel of components to virtually build a custom, collapsible control panel.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Input** and **Output** Property.

### Input Pins

#### Input

Unidentified Pins are represented by the following symbol (), and wiring is represented by a black line.

### Output Pins

#### Output

Unidentified Pins are represented by the following symbol (), and wiring is represented by a black line.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Container Properties

#### Name

User-defined name uniquely identifies the Container.

#### Input Count [1](#Connectors)

User-defined name uniquely identifies the Container.

#### Output Count [1](#Connectors)

Sets the total number of audio and control outputs.

#### Password Protected

Allows you to restrict access to the Container's Control Panel.

###### 1. Initially, before making any connections, the Container component has diamond shaped external connectors. When you connect an audio type connector to one of the Container's internal connectors, the Container's external connectors change to circles, indicating audio. The same is true for the Control Pin connectors - the external connectors change to squares, indicating Control Pins.

[Controls](javascript:void(0))

#### +

Click the + to add a Panel to the Container. The Panels, by default, are numbered sequentially.

#### x

Click the "X" on the right side of a Panel to delete that Panel.

[Control Pins](javascript:void(0))

There are no control pins for this component.
