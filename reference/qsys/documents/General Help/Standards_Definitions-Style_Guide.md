# Code Style Guide

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Standards_Definitions/Style_Guide.htm

# Code Style Guide

## Formatting

[Naming](javascript:void(0))

* Branch Naming Schema:

  + main
  + develop
  + bugfix/MyBugFix **or** bugfix/[JIRA Ticket]
  + feature/MyNewFeature **or** feature/[JIRA Ticket]
* Names of controls, functions, aliases, global objects, and global variables are **PascalCase** or **UpperCamelCase**.

  + For reserved control names, see **Reserved Control Names**.
* Names of local variables and local objects are **camelCase** or **lowerCamelCase**.
* Repository Names (and therefore plugin file names) are **PascalCase**.

[White space rules](javascript:void(0))

* One statement per line
* One assignment per statement
* Indentation for scoping depth should be two spaces
* Space after control structures (if, for, while, etc.), operators, and commas
* Comments

  + General comments (single or multi-line) go one line above the respective chunk â e.g., "this function does abc"
  + Granular comments should be in line â e.g., "this conditional tests abc for xyz"
  + Single line comments with three asterisks on either side of the description should denote different sections of the code.
* Spaces can be added for readability for API documentation or large sets of look-up data.

## Organization

[Design Time](javascript:void(0))

* General code information captured in single line comments.

  + Name of plugin
  + Name of developer
  + Month (MM) and Year (YYYY) of development
* PluginInfo Header
* Constants
* Reserved functions (See [Reserved Functions](Reserved_Functions.htm) for more information)
* Custom functions

[Runtime (contained within the <if Controls then> conditional)](javascript:void(0))

* Organization

  + **require** declarations go at the top and should be ordered alphabetically.
  + Non-functions:

    - Control Aliases
    - Variables
    - Objects and tables
    - Constants
  + Reserved function (See [Reserved Functions](Reserved_Functions.htm) for more information)
  + Custom functions
  + EventHandlers
  + Initialization function
* Print statements

  + Socket Events should always print to the debug window for basic troubleshooting. They should be presented in a clear and concise manner â e.g., "Socket Closed due to error: [error message]"

**Note:** For a working example of the plugin framework, see [Basic Plugin Framework](../Code_Examples/Basic_Plugin_Framework.htm).

## Example

Style Guide Example

```lua
-- An Example Plugin                              -- General information about the plugin/developer at the top  
-- by Your Name  
-- Month Year  
  
MyAlias = true                                    -- Aliases and global variables are PascalCase  
MyObject = {}                                     -- Global Objects are PascalCase  
  
-- Basic commands                                 -- General comments go one line above  
Commands = {  
  NACK                   = string.char(0x10),     -- Add whitespace to increase readability of large chunks of data  
  PingPong               = string.char(0x01),     -- One assignment per line  
  AnotherCommand         = string.char(0x20),  
  AnEvenLongerCommand    = string.char(0x21),  
}  
  
--*** Helper functions ***                        -- Single line comment with asterisks to denote what is contained in this section  
  
-- This function is an example                    -- General comments go on the line above  
function MyFunction()                             -- Functions are PascalCase  
  local myVariable                                -- Local variables and objects are camelCase  
  if MyAlias then                                 -- Single space after operators  
    myVariable = false                              
  end  
  return myVariable                               -- Indentation for scoping depth is two spaces  
end  
  
-- This function is another example  
function MyOtherFunction()  
  local myString = "" -- A String                 -- Granular comments go in line  
  if MyFunction() then  
    myString = myString .. "Example"              -- Single space after operators  
  end  
end
```
