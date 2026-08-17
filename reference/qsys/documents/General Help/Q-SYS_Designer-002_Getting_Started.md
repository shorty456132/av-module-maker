# Getting Started

> Source: https://help.qsys.com/Content/Q-SYS_Designer/002_Getting_Started.htm

# Getting Started with Q-SYS Designer

[The Design File](javascript:void(0))

The design file contains all the virtual components, their connections and initial DSP settings. The design is created and maintained on a PC running Q-SYS Designer. You can save the design file on your PC, and on the Core. Only one design at a time can be on the Core.

When the design is complete, it is loaded on the Core (Save to Core and Run - F5), tested, and adjustments made. When all adjustments are finalized, the design is saved to the Core and run. It is recommended that you save the design file on your PC as a backup. After creating and saving a design to the Core, Q-SYS Designer is not required to operate the Q-SYS system.

**Note:** If the entire system should lose power, any settings made to controls 30 seconds (or more) prior to losing power are automatically saved and restored when power is restored to the system.

[Q-SYS Designer Workspace](javascript:void(0))

The Q-SYS Designer workspace can be divided into the following areas: Title Bar, main menu, Left-side Pane, Right-side Pane, and the Schematic.

* The **Title Bar** displays the design name with an asterisk indicating unsaved changes and, "Q-SYS Designer [build number]".
* The **main menu** is a typical Windows drop-down menu with the following choices: File, Edit, View, Tools, and Help.
* The **Status Bar**, under the main menu, has the following information:
  + Core name and status - gives the user-defined name of the Core, and the status.Green indicates that communication with the Core is OK, red indicates an issue. Hovering over the Core name displays the communication status, the IP address currently being used by the Core, and all available IP Addresses.
  + If there is a Redundant Core, the status is given for that as well.
  + System Mute icon - loudspeaker with "sound waves" indicates the system is not muted. Click the icon to mute the system, the loudspeaker with the red international "NO" symbol displays, indicating the system is muted. If the Core is stopped and restarted, or you re-deploy the same design, the System Mute state is remembered. If you deploy a new design, the System Mute state is the default state of unmuted.
  + Show Administrator icon - click the icon to open a new tab in Q-SYS Designer showing the Administrator interface. Available in the Run or Emulate mode only.
* The Left-side Pane has accordion bars for:
  + **Inventory** - adding and configuring hardware proxies,
  + **Schematic Pages** - to assist in the layout of your design,
  + **User Control Interfaces** - for designing remote interfaces,
  + **Snapshots** - for saving sets of control settings to use for different events,
  + **Named Controls** - to make Q-SYS controls available to [Control Change Commands](../Administrator/Commands.htm), [Control Scripting](../Schematic_Library/control_script_2.htm), and [external control](../External_Control_APIs/External_Control_APIs_Overview.htm) systems,
* The **Schematic** is the area in the center of the screen. You can have one or many linked or un-linked pages of schematic diagrams. You add more pages under the **Schematic Pages** accordion bar. You can link components on different pages using **Signal Names**.
* Right-side Pane has four main sections:
  + The **[Schematic Library](013_Schematic_Library.htm)** contains a listing of all the virtual DSP, Control, and Layout components you can add to your system design. For a complete listing of the available components, and information about each one, refer to the *Table of Contents > Components and Inventory Reference* in this help system. When Q-SYS Designer is in Run/Emulate mode, the Schematic Library is not available.
  + The **User Library** allows you to drag frequently used, and pre-configured components into the User Library and have them available for use in any design you open.
  + In the **[Graphic Tools](014_Graphic_Tools.htm)** section, there is a Text tool, a Text Box tool, and a Box tool to assist in labeling and organizing your design.
  + The **Properties** section is available when you have a component selected. The **Properties** section is used to configure the Schematic Elements, for example, you can set the number of channels available on a Mixer, you can give the Core a specific name and location.
  + A sub-section of **Properties** is **Control Pins**. **Control Pins** give you access to the controls, meters, and so on within a Schematic Element to use in scripts, to control or trigger other controls, and so on. You can select the **Control Pins** you want to be available for each Schematic Element.

[Using the Main Menu](javascript:void(0))

Following is a list of features available on each of the main menu selections and a brief description of each.

[File](javascript:void(0))

* **New Design** (Ctrl+N) - Opens a new instance of Q-SYS Designer.
* **Open** (Ctrl+O) - Opens a Windows dialog box allowing you to navigate to any saved Q-SYS design file (file extension .qsys) and open it.
  + If you open more than one design, multiple instances of Q-SYS Designer are opened.
  + Q-SYS Designer remembers the Schematic Pages you have open from the last time you saved the file. The open pages are remembered by filename, not by the path. If you have multiple copies of a design with the same file name, in different locations, the open pages of the last copy of the file you saved are remembered for any copy you open after that.
* **Open Sample Design** - Opens a Windows Explorer window where you can select sample designs installed from Q-SYS Library.
* **Save** (Ctrl+S) - Saves the currently open Q-SYS design file, overwriting the original file with the same name. The file is saved on your hard drive, network, or another device you specify, not the Core. Any adjustments made to controls are saved with the design. Refer to [Different Versions of Q-SYS Designer](../Schematic_Library/core_status.htm#Different_Versions_of_Q-SYS) for information about version mismatch.
* **Save As**
  - Gives you the option to save the Q-SYS design file with a new name or location without overwriting the original file.
* **[Check Design](016_Check_Design.htm)**
  - Opens a dialog listing DSP Usage, Network Audio Input and Output, and Input and output Network Bandwidth.
* **Save to Core & Run** (F5) - Saves the currently open Q-SYS Designer file to the Core, overwriting the design file currently running (if any), and runs the new design on the Core. When the design is saved to the Core and running, audio may be processed through the system.

**Note:** If the entire system should lose power, any settings made to controls 30 seconds (or more) prior to losing power are automatically saved and restored when power is restored to the system.

* **Load from Core & Connect**
  - Click to display a list of available systems (Cores) on the network, listed by Core Name, Design Name, and IP Address. You can filter the list by System (locally discovered, hard linked, or both) and search by Core Name or Design Name. Select the Core you want, click OK, and the associated design is opened from the Core. You can make adjustments to any control, run scripts, and so on - any adjustments you make are live.
* [**Emulate**](003_Emulate_Mode.htm) (F6) - The **Emulate** mode allows you to enter a run type mode without being connected to a Core. This is helpful during the design phase of your system for setting the controls of Schematic Elements in your design. In the **Emulate** (F6) mode you can make initial control settings and process control logic such as User Control Interfaces, control scripts and so on; no audio is processed. The control settings are made in the **Emulate** mode and saved, either on the PC running Q-SYS Designer or on the Core using **Save to Core & Run**. You can have multiple designs open on a PC at one time, but you can only **Emulate** one design at a time.
* **Disconnect** (F7) - The design mode or **Disconnect (F7)** is the default mode when you start Q-SYS Designer. In the design mode you add items from Inventory, User Control Interfaces (UCI), Snapshots, and from the Schematic Library to create your design. Once the Components and Assets are in the Schematic, they are generically referred to as Schematic Elements. You can add, delete, arrange, configure, and connect the Schematic Elements in the design mode. In the design mode you cannot make any adjustments to the controls.
* **Recently opened designs**
  - Displays a list of design files on which you have recently worked. Click the file you want to open. Q-SYS Designer remembers the Schematic Pages you have open from the last time you saved the file. The open pages are remembered by filename, not by the path. If you have multiple copies of a design with the same file name, in different locations, the open pages of the last copy of the file you saved are remembered for any copy you open after that.
* **[Design Properties](../Schematic_Library/design_properties.htm)**
* **[Preferences](../Schematic_Library/preferences.htm)**
* **Close**

[Edit](javascript:void(0))

* Standard Windows edit operations: Cut (Ctrl+X), Copy (Ctrl+C), Paste (Ctrl+V), Delete (Del), Duplicate (Ctrl+D), Select All (Ctrl+A), Undo (Ctrl+Z) and Redo (Ctrl+Y).
* [Search and Replace](search_and_replace.htm) (Ctrl+H)

[View](javascript:void(0))

To zoom within Q-SYS Designer, use the following menu items or the **Zoom to** selector at the bottom of the Q-SYS Designer canvas. Each schematic page or UCI page can have an independent zoom level.

* Zoom In (Ctrl++)
* Zoom Out (Ctrl+-)
* Actual Size (Ctrl+0)
* Fit To Screen (Ctrl+9)
* Reset All Zooms - resets the zoom level across all pages to 100%.
* Find (Ctrl+F)
* Application
  + Application Zoom In (Ctrl+Shift++) (zooms the entire user interface)
  + Application Zoom Out (Ctrl+Shift+-) (zooms the entire user interface)
  + Application Zoom Actual Size (Ctrl+Shift+Backspace)

* Reset View

[Tools](javascript:void(0))

* [Group](Using_the_Schematic/About_Schematic_Elements.htm#Grouping_Schematic_Elements)
* [Ungroup](Using_the_Schematic/About_Schematic_Elements.htm#Grouping_Schematic_Elements)
* [Align](Using_the_Schematic/Labeling_and_Organizing_Schematic_Elements.htm#Align)
  + Horizontal Align Left (Ctrl+L)
  + Horizontal Align Center
  + Horizontal Align Right (Ctrl+R)
  + Horizontal Center in Page
  + Vertical Align Top (Ctrl+T)
  + Vertical Align Center
  + Vertical Align Bottom (Ctrl+B)
  + Vertical Center in Page
* [Distribute](Using_the_Schematic/Labeling_and_Organizing_Schematic_Elements.htm#Distribute)
  + Horizontal Distribute Center
  + Horizontal Distribute Equally Spaced
  + Vertical Distribute Center
  + Vertical Distribute Equally Spaced
* [Pack](Using_the_Schematic/Labeling_and_Organizing_Schematic_Elements.htm#Pack)
  + Pack Left (Ctrl+Shift+L)
  + Horizontal Pack Center
  + Pack Right (Ctrl+Shift+R)
  + Pack Top (Ctrl+Shift+T)
  + Vertical Pack Center
  + Pack Bottom (Ctrl+Shift+B)
* [Order](Using_the_Schematic/Labeling_and_Organizing_Schematic_Elements.htm#Ordering_Schematic_Elements)
  + Bring to Front (Ctrl+])
  + Send to Back (Ctrl+[)
* UCI Operations
  + [Remap UCI Controls [BETA]](../Schematic_Library/uci_control_remap.htm)
  + [Relink UCI Controls [BETA]](../Schematic_Library/uci_control_relink.htm)
  + [Import and Export UCIs](../Schematic_Library/import__export_UCIs.htm)
  + [Update UCI From Bundle](../Schematic_Library/uci_update_from_bundle.htm)
  + [Import and Export UCI Variables](../Schematic_Library/uci_variables_import_and_export.htm)
* [Component Controls](Using_the_Schematic/using_controls.htm#Copying_and_Pasting_All_Component_Controls)
  + Copy Component Controls
  + Paste Component Controls
* [Lock](Using_the_Schematic/Labeling_and_Organizing_Schematic_Elements.htm)
* [Unlock All](Using_the_Schematic/Labeling_and_Organizing_Schematic_Elements.htm)
* [Script Programmer Mode](../Schematic_Library/script_programmer_mode.htm)
* [View Component Controls Info...](Using_the_Schematic/using_controls.htm#Viewing)
* [Extract Named Controls...](../Schematic_Library/external_control.htm#Extract_External_Controls)
* [Show Design Resources...](../Schematic_Library/Design_Resources.htm)
* [Auto Update Styles](../Schematic_Library/Design_Resources.htm)
* [Open Q-SYS Library...](../Q-SYS_Library/Q-SYS_Library.htm)
* [Show Asset Installer...](../Q-SYS_Library/Asset_Installer.htm)
* [Show Configurator...](../Hardware/0017_Configurator.htm)
* [Show Administrator...](../Administrator/AdministrationInterface.htm)
* [Show Core Manager...](../Core_Manager/CoreManager_Overview.htm)

[Help (F1)](javascript:void(0))

* Displays the **Help** System. If you have an item selected, the help displays the topic relating to the selected element. An internet connection is required for this function.
* Download Offline Help
* [QSC Communities for Developers](https://developers.qsys.com/s/)
* [QSC Training Website](https://training.qsc.com/)
* About

[Icons](javascript:void(0))

#### Administrator

Quickly connects to the Administrator page. Only accessible when in Run or Emulate Mode. For more information, visit [Administrator](../Administrator/AdministrationInterface.htm).

#### Configurator

Quickly connects to Q-SYS Configurator. For more information, visit [Configurator](../Hardware/0017_Configurator.htm).

#### Q-SYS Library

Quickly connects to Q-SYS Library to manage and download available assets. For more information, visit [Q-SYS Library](../Q-SYS_Library/Q-SYS_Library_Overview.htm).

#### Q-SYS Reflect Sign In

Quickly connects to the Q-SYS Reflect platform. For more information, visit [Q-SYS Reflect](../Reflect/reflect_overview.htm).

#### Light/Dark Theme [BETA]

Toggling between light and dark themes allows you to switch the visual appearance of your interface to either a bright or a dark color scheme.

#### Window Control

Minimize: This button reduces the window to an icon on the taskbar, allowing you to keep the application running in the background without taking up screen space.

Restore: This button toggles the window between its maximized state (full screen) and its previous size and position. If the window is already maximized, clicking this button will restore it to its original size.

Close: This button closes the window and terminates the application, removing it from the taskbar and freeing up system resources.

#### Mute All Audio

Toggles between muted and unmuted audio within the design. Only accessible while in Run or Emulate Mode. When selected, the icon will turn red with a slash through it.

#### Auto-Hide

Each of the panes offer an Auto-Hide icon that will minimize the pane from the screen. The arrows may face the other way, depending on left or right pane.

[Using the Left-side Pane](javascript:void(0))

Each accordion bar in the Left-side Pane has different characteristics, purposes, and procedures. Refer to the following topics for information.

* [Using Inventory](../Schematic_Library/inventory.htm)
* [Using Schematic Pages](../Schematic_Library/schematic_pages.htm)
* [User Control Interfaces](../Schematic_Library/user_control_interface.htm)
* [Snapshots](../Schematic_Library/snapshots.htm)
* [Named Controls](../Schematic_Library/external_control.htm)
* [Inspector](../Schematic_Library/Design_Inspector.htm)

[Using the Schematic](javascript:void(0))

Refer to [Using the Schematic](Using_the_Schematic/Using_the_Schematic.htm).

[Using the Right-side Pane](javascript:void(0))

Refer to:

* [Schematic Library](013_Schematic_Library.htm)
* [Graphic Tools](014_Graphic_Tools.htm)
* [Accessing Plugins](../Q-SYS_Library/Accessing_Plugins.htm)
