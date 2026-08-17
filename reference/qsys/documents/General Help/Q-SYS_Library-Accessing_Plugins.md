# Accessing Plugins

> Source: https://help.qsys.com/Content/Q-SYS_Library/Accessing_Plugins.htm

# Accessing Plugins

Plugins enable you to integrate many third-party AV devices into your Q-SYS design and control those devices with separate, installable scripting components.

[Plugin Organization](javascript:void(0))

Plugins are located within the Schematic Elements > Plugins section of the Q-SYS Designer interface. Installed plugins are grouped into folders by manufacturer or category. Within each folder, the individual plugins are listed by name. For example, you might see:

Plugins > Sennheiser > Sennheiser - SpeechLine Digital Wireless

In this case, Sennheiser is the folder, and Sennheiser - SpeechLine Digital Wireless is the plugin you can drag into your design.

**Note:** Some existing QSC-authored plugins may still appear under an Enterprise Manager folder until those plugins are updated.

[Properties](javascript:void(0))

### Plugin Properties

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

**Note:** Each plugin has its own respective Properties. Refer to the [Plugin Help](#Plugin) for additional information.

#### Is Managed

For QSC-authored plugins only, select 'Yes' to add the plugin to your Inventory list, which makes the plugin's Status available for monitoring in Core Manager and Q-SYS Reflect. When enabled, you can then specify a Name and Location for the plugin, as with any other Inventory item. Enabling the Is Managed property also reveals the Is Required property, if applicable to the plugin.

#### Is Required

When enabled, and the device is not found on the network, the device is reported as 'Missing', which is an error condition. This is the default behavior. When disabled, and the device is not found on the network, the device is reported as 'Not Present', which is not an error condition.

#### Show Debug

Select 'Yes' to show the Debug Output window. See [Debug Output](../Schematic_Library/debug_output.htm).

[Plugin Help](javascript:void(0))

If a plugin includes a bundled help file, you can view the plugin help as with other Q-SYS Designer components: Drag the plugin into your schematic, select the plugin, and press F1.

**Note:** A plugin must be installed with Asset Installer to be able to view any bundled help. If you press F1 and see this page, either the plugin has not been installed with Q-SYS Asset Manager, or a bundled help file is not available.
