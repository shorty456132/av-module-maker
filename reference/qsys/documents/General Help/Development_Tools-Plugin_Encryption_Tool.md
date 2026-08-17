# Plugin Encryption Tool

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Development_Tools/Plugin_Encryption_Tool.htm

# Plugin Encryption Tool

The plugin encryption tool creates a .qplugx file from the .qplug file. The code in the qplugx is unreadable because it is encrypted with a key, allowing for the developer to avoid exposing the code. This file cannot be modified, which ensures that the code being used is the code that was encrypted.

**Note:** Download the Plugin Encryption Tool from [Github](https://github.com/qsys-plugins/PluginEncryptionTool).

## Encryption Tool Syntax

Navigate to the plugin tool folder and open a command prompt from that location. The syntax is:

./plugin\_tool.exe encrypt â<plugin location.qplug>â â<desired qplugx location.qplugx>â

## Example

Here is a code example of encoding a plugin (named "TestPlugin") that is in the plugin tool root folder:

./plugin\_tool.exe encrypt âTestPlugin.qplugâ "TestPlugin.qplugxâ
