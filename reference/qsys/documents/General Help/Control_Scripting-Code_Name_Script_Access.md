# Code Name and Script Access

> Source: https://help.qsys.com/Content/Control_Scripting/Code_Name_Script_Access.htm

# Code Name and Script Access

Q-SYS will automatically assign any added component a unique name for external control and scripting control purposes. The Code Name and Script Access can be set in the Properties for any component.

The Code name will also display over the top-left of a component when selected, or hovering over with the pointer.

#### Code Name

Displays the currently assign name for control access. You can use the auto-assigned name or customize it. Q-SYS will automatically check all Code Names in the design to ensure name is unique.

#### Script Access

Defines whether the component will be accessible by script and/or externally, or not at all. Choices include All, External, None (default), and Script.

* **None** (default) - Not accessible by any script, plugin, or by [Q-SYS Remote Control Protocol (QRC)](../External_Control_APIs/QRC/QRC_Overview.htm).
* **Script** - Can be accessed by scripts, such as Text Controller, Block Controllers, and plugins only.
* **External** - Can only be accessed by 3rd party controls systems using component commands from the [Q-SYS Remote Control Protocol (QRC)](../External_Control_APIs/QRC/QRC_Overview.htm).
* **All** - No restrictions, can be accessed by 3rd party control systems via [Q-SYS Remote Control Protocol (QRC)](../External_Control_APIs/QRC/QRC_Overview.htm), or script objects or plugin objects.

**Tip:** Use [Script Programmer Mode](../Schematic_Library/script_programmer_mode.htm) to quickly view the Script Access setting directly on the component in the design schematic without the need to disconnect from the Q-SYS Core processor.
