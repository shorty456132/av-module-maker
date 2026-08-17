# External Lua Modules

> Source: https://help.qsys.com/Content/Control_Scripting/External_Lua_Modules.htm

# External Lua Modules

Q-SYS supports external Lua modules which, when installed into a Design, are available for use by scripts or plugins used in the Design. Lua modules are installed in the Design via the Tools > Design Resources menu. Lua modules are limited to pure Lua but can use any of the built-in or Q-SYS specific Lua modules.

[Module Format](javascript:void(0))

Each module lives inside a folder within `%DOCS%/QSC/Q-Sys Designer/Modules`. Like styles, the name of the module is based on the name of the folder. The Lua file itself is always `init.lua`. As an example, a module called `test_module` would exist of as a single file - `%DOCUMENTS%/QSC/Q-Sys Designer/Modules/test_module/init.lua`. The module should be a standard Lua module and return a single table which is the module implementation.

Within the directory there needs to be a file call `info.json`. This contains version and other information about the module.

```lua
{  
"version": "1.2.3",  
"type": "LuaModule",  
"author": "someguy@overthere.com",  
"description": "this module does something fancy",  
"requiredVersion" : "9.5"  
}
```

Like styles, Designer will detect any changes between the files on disk and the files installed in the Design and ask to update the version in the Design when changes are detected. If the module is sourced from a git repo running `git pull` is the easiest way to update the module to the latest.

[Installing, Saving, and Removing Modules](javascript:void(0))

**Tip:** Because module files are installed to the design, if you share a design containing installed modules with someone else, that person will also see those modules.

### Installing New Modules to a Design

1. Place the module files into the Modules folder. See [Module Format](#Module).
2. In Q-SYS Designer, create or open a design file.
3. Click Tools > Design Resources.
4. From the Available list, select the module name, and then click Install Module.
5. Close the Design Resources window.

The installed module is now available in the design.

### Saving Modules from a Design

If a design contains a module that is not currently on your local disk, you can save it from the design. You can then edit the files.

1. Click Tools > Design Resources.
2. From the Installed list, select the module name, and then click . The module is now saved to the Modules folder on-disk.

### Removing Modules from a Design

1. In Q-SYS Designer, create or open a design file.
2. Click Tools > Design Resources.
3. From the Installed list, select the module name, and then click .
4. Close the Design Resources window.

[Example](javascript:void(0))

Itâs possible to create the files required directly on the file system but the quickest way to play with modules is to clone an already prepared git repo. Here is an example of a simple module which adds 2 numbers together - [jhndnn/add](https://bitbucket.org/jhndnn/add/src/master/). It consists of 3 files.

* `init.lua` - the main Lua module
* `info.json` - information about the module
* `readme.md` - documentation for the module

The easiest way to try this is to use `git` to clone the repo into `%DOCS%/QSC/Q-Sys Designer/Modules`. Make sure Git for Windows is installed and the `Modules` directory exists and then run the following command.

```lua
git clone https://bitbucket.org/jhndnn/add.git "%DOCS%/QSC/Q-Sys Designer/Modules/add"
```

At this point the module should be able to be installed in the Manage Design Resources page and can be used in a script.

```lua
add = require("add")  
   
print(add.go( 4, 5 )) -- prints 9
```

**Note:** The markdown preview within the Design Resources page doesnât currently deal well with the multi-line code blocks but they should display correctly in the actual repo web view.

[Additional Example Modules](javascript:void(0))

**CAUTION:** These examples come as-is with no guarantee of performance or quality.

* [Quote of the Day Generator](https://github.com/jhndnnqsc/qotd)
* [Q-SYS AWS Authentication Module](https://github.com/jhndnnqsc/aws-auth)
* [Q--SYS AWS Simple Email Service Module](https://github.com/jhndnnqsc/aws-ses)
* [Q-SYS AWS Polly TTS Module](https://github.com/jhndnnqsc/aws-polly)
