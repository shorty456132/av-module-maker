# Compiler Error 1707

**library error: Error: Library path cannot contain relative or absolute paths: ' <library_name>'. (use #INCLUDEPATH instead)**

Fully-qualified paths and relative paths cannot be used when including SIMPL# Libraries. Only the library name can be specified within the include directive.

The following are examples of this error:

// Module1.usp

`#USER_SIMPLSHARP_LIBRARY “MyLibrary” // ok – no path is given`

`#USER_SIMPLSHARP_LIBRARY “C:\MyPath\MyLibrary” // error – fully-qualified path specified`

`#USER_LIBRARY “..\..\MyPath\MyLibrary” // error – relative path specified`

`// Module2.usp`

`#INCLUDEPATH “C:\\MyLibraries”`

`#INCLUDEPATH “..\\..\\Projects”`

`#USER_SIMPLSHARP_LIBRARY “MySSharpLibrary” // ok`

`#USER_LIBRARY “MySPlusLibrary” // ok`

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1707.htm*
