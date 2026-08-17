# #INCLUDEPATH

Name: 

#INCLUDEPATH

Syntax:

#INCLUDEPATH "<absolute_path or relative_path>"

Description:

Directs the compiler to search for User SIMPL+ and SIMPL# Libraries in the specified paths.

The compiler will search for the library in the following order:

1) Project Folder

2) Global SIMPL+ Folder (refer to Edit | Preferences | Paths in SIMPL).

3) Paths specified in #INCLUDEPATH compiler directive

Example:

#INCLUDEPATH "c:\\\MyLibrares"

#INCLUDEPATH "..\\\\..\\\Projects\\\bin"

#USER_LIBRARY "MySPlusLibrary"

#USER_SIMPLSHARP_LIBRARY "MySSharpLibrary" 

Version:

3-Series

SIMPL v4.02.17 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Directives/_INCLUDEPATH.htm*
