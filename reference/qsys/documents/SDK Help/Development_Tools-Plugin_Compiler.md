# Plugin Compiler

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Development_Tools/Plugin_Compiler.htm

# Plugin Compiler

The plugin compiler tool is an automated text replacement tool designed to be used within Microsoft's VS Code application that compiles separate Lua files into a single Qplug file. This allows the developer to work with separate files rather than a large, single Qplug file, making managing and editing the code much easier. This tool also comes with some baked-in features.

[Feature Overview](javascript:void(0))

#### Compiler

Compiles multiple files into a single Qplug file.

#### Image Encoder

The ability to encode a PNG, JPEG, JPG or SVG file to base64.

#### GUID Generator

The ability to create a unique GUID if one does not exist.

#### Version Control

Increment the version number with each build.

#### Copy Qplug

After the compile process, the Qplug file is copied to the plugin folder.

[Setting up the Compiler](javascript:void(0))

The compiler is not a standalone application, and forms part of the "Basic Plugin Framework" code that is hosted in the [Code Exchange](https://developers.qsc.com/s/exchange/developer-repo/a3Y4X000001cjUBUAY/basic-plugin-framework) section of the Communities for Developers website. The code itself can be used to "compile" any plugin, though, when used with the appropriate files. To use it, follow these steps:

1. Download and install Microsoft VS Code ([code.visualstudio.com](https://code.visualstudio.com/)).

   **Note:** Issues with the plugin compiler have been noted on older versions of VS Code. Check for updates after installation to make sure the latest version is installed.
2. Download and install Git for Windows from (<https://git-scm.com/download/win>).
3. Locate the "Basic Plugin Framework" plugin via Code Exchange in Communities for Developers and download it to a known location on your machine.
4. Make a copy of the "Basic Plugin Framework" folder, renaming folder to be the name of the plugin that will be created.

   **Note:** With older versions of the Compiler, the path where the files are placed could not have any spaces in the folder names. To use paths with spaces, use the latest copy of the Compiler from the "Basic Plugin Framework" code that is hosted in the [Code Exchange](https://developers.qsc.com/s/exchange/developer-repo/a3Y4X000001cjUBUAY/basic-plugin-framework).
5. Use File > Open Folder, navigate to the new named folder, and click "Select Folder".

At this point, VS code should be open with all the files required to build a plugin.

[Associate .qplug with Lua in VS Code](javascript:void(0))

You can map the file extension .qplug with the Lua language in VS Code in order to get highlighted proper syntax.

1. Open Settings. File > Preferences > Settings (ctrl+,)
2. Search for files.associations
3. Add an item with a key of \*.qplug and a value of lua.

[VS Code Keyboard Shortcut](javascript:void(0))

The compiler runs as a task in VS Code and can be made a keyboard shortcut. To do this, go to File > Preferences > Keyboard Shortcuts. Search for "Run Build Task" and click the pencil icon next to Tasks: Run Build Task and follow the on-screen prompts to bind the desired keys.

**Tip:** A good key combo to use is Ctrl + Shift + B, as it should be available for binding and is easy to remember (see screenshot).

["sh.exe not found" Error](javascript:void(0))

One issue that can occur is the compiler action may fail indicating a error regarding 'sh.exe' not being found. The 'sh.exe' file is part of GIT for Windows and sometimes the PC needs to be told where to find this file. To resolve this, manually add the path to the PC environmental variables:

1. Locate the folder where 'sh.exe' is installed. If the default installation location for Git for Windows was used, it should be "C:\Program Files\Git\usr\bin".
2. Type "environment" into Windows search. This should bring up an "Edit the system environmental Variables" link, like this:
3. Open that link. This should open the "System Properties" screen.
4. Click the "Environment Variables" button at the bottom.
5. In the "Systems variables" box at the bottom, find the "Path" variable and select it.
6. Click the "Edit" button
7. Click "New" and add an entry for the folder location where the "Sh.exe" executable is located.
8. Restart VS Code and try compiling the plugin again.

This should only need to be applied once to a PC as the settings will apply for compiling any plugin.

[How does the Compiler work?](javascript:void(0))

The basic plugin framework breaks up the plugin code initially into nine Lua files. These files are:

* controls.lua
* info.lua
* layout.lua
* model.lua
* pages.lua
* plugin.lua
* properties.lua
* rectify\_properties.lua
* runtime.lua

The plugin.lua file is the skeleton of the plugin that creates the .qplug file. The initial function of the plugin "compiler" takes the plugin.lua file and looks for each multi-line comment that is formatted like this:

`--[[ #include â<filename.lua>â ]]`

It then replaces that line with the contents of the file from the pluginâs local folder whose name matches the reference. (In the above example, this line in plugin.lua would be replaced by the contents of the filename.lua file.) It repeats this for all such references across all the files.

Here is a graphic view of how the "compiler" puts the .qplug file together:

[Image Encoder](javascript:void(0))

The compiler is capable of encoding .png, .jpeg, .jpg and .svg files into base64 strings so they can be used as graphics in a plugin user interface. To use this feature, place an image file into the folder with the other plugin files. You can then use the following syntax to encode the file:

```lua
-â[[ #encode "test.jpg" ]])
```

**Note:** The file can be in a sub-folder, if required, but make sure the relative path to the file is included with the file name.

As these images will form part of the graphics a plugin will show, they are added as an element in the graphics table in the GetControlLayout(props) function.

Here is an example of using the encoder to encode a .png image. (This is also used for .jpeg and .jpg images). In this example, the image is encoded and stored in a variable first.

```lua
Logo = "--[[ #encode "logo.png" ]]"  
table.insert(graphics,{  
  Type="Image",  
  Image=Logo,  
  Position={0,0},  
  Size={75,9}  
})
```

An image that uses .svg files requires a slightly different syntax. It uses the same basic syntax as the other images, except it has the "Type" set as "svg" instead. In this example, the encoding is also done inline rather than using a separate variable.

```lua
table.insert(graphics,{  
  Type="svg",  
  Image="--[[ #encode "logo.svg" ]]",  
  Position={0,0},  
  Size={75,9}  
})
```

[GUID Generator](javascript:void(0))

The compiler tool has the ability to create a guid for the plugin if one does not already exist. The info.lua file contains the plugin header, which has the Id field. If that field contains the string â<guid>â, it will be replaced with a proper GUID during the compile.

[Version Control](javascript:void(0))

One advantage of using the compiler is the built-in version control. The BuildVersion field in the plugin info header in the info.lua file can be incremented automatically during the compile process. After starting the compiler in VS Code, you will have these versioning options:

* ver\_maj â increments the first octet of the BuildVersion string
* ver\_min - increments the second octet of the BuildVersion string
* ver\_fix - increments the third octet of the BuildVersion string
* ver\_dev - increments the last octet of the BuildVersion string
* ver\_none â compiles without incrementing the BuildVersion
* CANCEL â cancels the compile

Currently, the BuildVersion is used solely for version control and is not used by Q-SYS Designer Software (QDS). PluginInfo.Version is still the version QDS uses and needs to be manually updated.

[Copy Qplug](javascript:void(0))

Once the compiler is completed, the .qplug file will automatically be copied to the proper plugin folder (Documents/QSC/Q-Sys Designer/Plugins/<plugin name>) and recognized by QDS.

[Adding Custom Files](javascript:void(0))

To add your own custom files and have them compiled, simply add the .lua file to the plugin folder and use the above syntax to add the file contents to where it is desired. This syntax is valid in any file that is being compiled and not just the skeleton plugin.lua file.

**Note:** If using version control, make sure the file is also added to the repository the plugin is stored in.

An example of using a custom .lua file would be to use this method in the runtime.lua file. Here is an example of adding a group of basic functions to the runtime.lua file:
