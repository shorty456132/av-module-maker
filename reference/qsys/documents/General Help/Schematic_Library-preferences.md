# Preferences

> Source: https://help.qsys.com/Content/Schematic_Library/preferences.htm

# Preferences

To access the Q-SYS Designer Preferences, select File > Preferences.

## General

[Auto Save](javascript:void(0))

#### Mode

Select whether to allow Q-SYS Designer to auto-save your current design file.

* Off: Design files are not auto-saved.
* Periodic: Design files are auto-saved according to the Save Timeout (min) parameter.

#### Save Timeout (min)

Select how often Designer saves a backup of your design file, from 0 to 1999999999 minutes (default is 5 minutes). In the event of a problem forcing Designer to close, you are prompted to select one or more design files to recover (if any were saved) at the next Designer start-up.

**Note:** Only design files with unsaved changes are auto-saved during each period. Recovery files are saved in `c:\Users\<user>\AppData\Roaming\QSC\Q-SYS Designer\Recovery`. These files are discarded when you dismiss the Select Recovery File window.

[Diagnostics](javascript:void(0))

#### Allow Q-SYS to collect performance data

Select your data collection preference for Q-SYS Designer Software.

* **Selected**: Opt in to data collection. This will enable the collection of anonymous software usage data. To learn what types of data are collected, see [Data Collection](../Data_Collection.htm).
* **Deselected**: Opt out of data collection. This will stop the collection of anonymous software usage data.

[General](javascript:void(0))

#### Asset Directory

Specify the location for Q-SYS Designer Software to use for assets, including plugins and UCI styles. Click the  button to clear the setting, which will set the directory to the default of C:\Users\Your.Name\Documents\QSC\Q-Sys Designer. Click  to select a custom location.

#### Default Component Script Access

Select a default setting for the Script Access property for components: None, External, Script, or All. See [Code Name and Script Access](../Control_Scripting/Code_Name_Script_Access.htm) for an explanation of these settings.

#### Enable the new Schematic Elements UI

Select whether to enable Schematic Elements UI improvements, including search filtering by element type (Components, Plugins, User Components) and category (e.g., Audio, Control, Video), as well as element type color grouping.

#### Script Editor

Select the type of Lua script editor to use in scripting components and UCI scripts.

* Legacy: This is the traditional editor found in previous versions of Q-SYS Designer Software.
* VSCode: (Default) The VSCode editor is a more powerful, robust editor that provides enhanced code completion, error highlighting, and hover help. To learn more, see [VSCode Script Editor](../Control_Scripting/VSCode_Editor.htm).

#### Theme [BETA]

Use the Theme preference to adjust the appearance of the Q-SYS Designer interface, including menus, editors, and dialog windows.

* Light: This is the traditional light gray theme.
* Dark: This changes the theme to a dark, modern look. In low-light viewing, this mode can help to reduce eye strain.
* Auto: This mode adjusts the theme based on the Windows color settings (Settings > Colors > Default app mode, Light or Dark).

**Tip:** Temporarily switch between Light and Dark mode by clicking the  icon near the top-right corner of the Q-SYS Designer window. The next time you open Designer, the theme preference reverts to what is selected in Preferences.

[HoverMon](javascript:void(0))

#### Driver

Select an audio driver for use with the [HoverMon](../Q-SYS_Designer/Using_the_Schematic/About_Schematic_Elements.htm#HoverMon) feature, which allows you to listen to sound being processed on the Core via your PC's sound card. Select the driver that works best with your PC's configuration. HoverMon may not work properly on all PCs with all audio drivers.

**Note:** For Q-SYS Designer to stream HoverMon audio, HoverMon must be enabled in Q-SYS Core Manager > [Network > Services](../Core_Manager/Core_Management/Network_Services.htm).

#### Driver Buffer

Set the audio buffer to use with HoverMon, if available for the selected audio driver.

[Notifications](javascript:void(0))

#### Disable Notifications

Select whether to enable or disable notifications about plugins and other Q-SYS Library updates.

[Proxy Server](javascript:void(0))

#### Proxy Server Enabled

Select whether to enable or disable the use of a proxy server. When enabled, the other proxy server setting becomes active.

#### Proxy Server Address

This field allows you to specify the address of the proxy server. It should be a valid URL or IP address that the Q-SYS Designer will use to route its network traffic.

## Hard Links

See [Remote Connectivity](../Networking/Remote_Connectivity.htm).
