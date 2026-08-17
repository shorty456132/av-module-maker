# #USER_SIMPLSHARP_LIBRARY

Name:

#USER_SIMPLSHARP_LIBRARY

Syntax:

#USER_SIMPLSHARP_LIBRARY "<SIMPL# Library Name>"

Description:

Directs the compiler to include code from a User SIMPL# library. The module name specified is the library filename without the CLZ extension. Relative or absolute path are not allowed within this directive (see #INCLUDEPATH).

The compiler will search for the library in the following order:

1) Project Folder

2) Global SIMPL+ Folder (refer to Edit | Preferences | Paths in SIMPL).

3) Paths specified in #INCLUDEPATH compiler directive

Example:

#USER_SIMPLSHARP_LIBRARY "MyLibrary"

Directs the compiler to include the User SIMPL# Library, "MyLibrary.clz".

Version:

3-Series

SIMPL v4.02.00 and later

4-Series

SIMPL v4.14.06 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Directives/_USER_SIMPLSHARP_LIBRARY.htm*
