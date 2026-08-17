# Using the Schematic

> Source: https://help.qsys.com/Content/Q-SYS_Designer/Using_the_Schematic/Using_the_Schematic.htm

# Using the Schematic

The Schematic, in the center of the Q-SYS Designer workspace, is where your Q-SYS system is designed. You organize, connect, and configure Schematic Elements, write scripts, test control logic and audio signal flow, and operate and adjust the system from the Schematic area.

* To design a system, you add various elements to your Schematic including: Components, **Inventory** Items, **Snapshot Controllers**, and so on.
* The term Schematic Element refers to anything after it is in the Schematic.
* You can add multiple pages to your Schematic and link Schematic Elements across pages.

## Topics in This Section

|  |  |  |
| --- | --- | --- |
| **Basics**  [Moving Around the Schematic](#Moving_Around_the_Schematic)  [Schematic Element](About_Schematic_Elements.htm)  [Components](About_Schematic_Elements.htm#Components)  [Adding Components to the Schematic](About_Schematic_Elements.htm#Adding)  [Finding Items Using the Context Finder](About_Schematic_Elements.htm#Finding)  [Selecting Schematic Elements](About_Schematic_Elements.htm#Selectin)  [Copying and Pasting Schematic Elements](About_Schematic_Elements.htm#Copying_and_Pasting_Elements)  [Moving Schematic Elements](About_Schematic_Elements.htm#Moving_Schematic_Elements)  [Deleting Schematic Elements](About_Schematic_Elements.htm#Deleting_Schematic_Elements)  [Headers, Text, Boxes, and Other Graphics](About_Schematic_Elements.htm#Headings,_Text,_Boxes,_and_Other_Graphics) | [Signal Pins and Wiring in the Schematic](Connections_and_Wiring_in_the_Schematic.htm)  [Traditional Wiring](Connections_and_Wiring_in_the_Schematic.htm#Traditional_Wiring)  [Signal Names](Connections_and_Wiring_in_the_Schematic.htm#Signal_Names)  [Signal Snakes](Connections_and_Wiring_in_the_Schematic.htm#Signal_Snakes)  [Connection Types](Connections_and_Wiring_in_the_Schematic.htm#Connection_Types)  [Organizing Your Design](Labeling_and_Organizing_Schematic_Elements.htm)  [Labeling Schematic Elements](Labeling_and_Organizing_Schematic_Elements.htm#Labeling__Schematic_Elements)  [Aligning Schematic Elements](Labeling_and_Organizing_Schematic_Elements.htm#Aligning_Schematic_Elements)  [Properties Panel](../properties_panel.htm)  [Headers, Text, Boxes, and Other Graphics](Labeling_and_Organizing_Schematic_Elements.htm#Headers,_Text,_Boxes,_and_Other_Graphics)  [Schematic Pages](Labeling_and_Organizing_Schematic_Elements.htm#Schematic_Pages)  [Coloring in Q-SYS](Labeling_and_Organizing_Schematic_Elements.htm#Coloring_in_Q-SYS) | [Using Controls](using_controls.htm)  [Adjusting Controls](using_controls.htm#Adjustin)  [Placing Controls in the Schematic](using_controls.htm#Placing)  [Transferring Settings from one Control to Another](using_controls.htm#Transfer)  [Identifying Controls in the Schematic](using_controls.htm#Identify) |

## Moving Around the Schematic

There are several ways to navigate the Schematic when it becomes larger than what can fit on a single Schematic page.

**Context Finder**

This feature enables quick navigation between associated Schematic Elements.

* Select an item in the Inventory list and press Ctrl+F to display its components as clickable links in the upper-right corner of the Schematic .
* Select a control in a component's control panel; if it is part of a Snapshot Bank, a link to the Snapshot Bank appears in the Snapshots list.
* Select a Signal Name to jump between its source and destination, and back.

**Note:** Navigation from the Schematic Library to the Schematic is not supported. If an item is obscured by another component or panel, the system will jump to it, but may not be visible.

**Panning**

Clicking and releasing the mouse's scroll button activates a panning modeâmove the mouse in any direction to reposition the Schematic, then click again to exit.

**Scrolling**

Scroll bars on the right and bottom edges allow vertical and horizontal movement to navigate wide schematic layouts.

The platform-level horizontal bar feature is behavior that is consistent across the Q-SYS Designer application, including all schematic pages, containers (block controllers, text controllers, UCI script), and script editorsâboth VSCode-based and Legacy script editors. When the content extends beyond the visible width, horizontal scrolling is automatically available and can be activated using standard input methods:

* Touchpad Gestures: Use side-to-side (two-finger) swipes on supported trackpads.
* Mouse Wheel: Hold the Shift key while scrolling vertically with a mouse wheel.
* Native HID Devices: Use devices with dedicated horizontal scroll support (e.g., horizontal scroll wheels).
* Scroll Bar: Use mouse or arrow keys to drag the bar.
