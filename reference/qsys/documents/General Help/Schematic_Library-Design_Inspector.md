# Inspector

> Source: https://help.qsys.com/Content/Schematic_Library/Design_Inspector.htm

# Inspector

The Inspector automatically checks your design in Design, Emulate and Run modes.

[Inspected Items](javascript:void(0))

Inspector checks for these items in your design.

### Scripts

This is a list of all scripting components in your design and their current status.

* Load: This is the percentage of the time allocated to Core script processing that this scripting component is consuming.
* Memory: The amount of memory currently being used by the scripting component â for example: "1.2 MB", "890.5 KB".
* Errors: This indicates the number of errors the script is currently generating. Refer to the Debug Output window for details.
* Verification: This indicates the status of the script's code signing.
  + 'Trusted' indicates the script is QSC-authored and has not been modified.
  + 'Unverified' indicates the script is user-created or has come from an unknown source.
  + 'Verification Failed' indicates a trusted script's original source code has been modified.

### Plugins

This is a list of all plugin components in your design and their current status.

* Load: This is the percentage of the time allocated to Core script processing that this plugin is consuming.
* Memory: The amount of memory currently being used by the plugin â for example: "1.2 MB", "890.5 KB".
* Errors: This indicates the number of errors the plugin script is currently generating. Refer to the Debug Output window for details.
* Verification: This indicates the status of the plugin's code signing.
  + 'Trusted' indicates the plugin is QSC-authored and has not been modified.
  + 'Unverified' indicates the plugin is user-created or has come from an unknown source.
  + 'Verification Failed' indicates a trusted plugin's original source code has been modified.

### Orphaned Controls

These are controls that have been placed in the schematic or User Control Interface (UCI), but the parent component has been deleted.

### Unterminated Signals

These are Signal Names that are assigned to a component input or output, but there is no matching Signal Name on another component output or input.

### Licensed Elements

These are features requiring a license when deploying your design to a Q-SYS Core. For more information, see [Licensing](../Core_Manager/Core_Management/Licensing.htm).

[Using the Inspector to Troubleshoot](javascript:void(0))

When there is an orphaned control, unterminated signal, or another issue, a yellow triangle with an exclamation point in the center displays on the Design Inspector accordion bar.

1. Click the Inspector accordion bar to display the list of inspected items.
2. Click one of the items in the list. The problem is highlighted in red.
3. Fix the problem.
