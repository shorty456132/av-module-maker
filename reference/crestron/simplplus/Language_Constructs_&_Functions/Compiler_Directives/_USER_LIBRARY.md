# #USER_LIBRARY

Name:

#USER_LIBRARY

Syntax:

#USER_LIBRARY "<User Library Name>"

Description:

Directs the compiler to include code from a User written library. The module name specified is the User Library Filename without the USL extension that is used by User Libraries. Relative or absolute path are not allowed within this directive (see #INCLUDEPATH).

The compiler will search for the library in the following order:

1) Project Folder

2) Global SIMPL+ Folder (refer to Edit | Preferences | Paths in SIMPL).

3) Paths specified in #INCLUDEPATH compiler directive

Example:

#USER_LIBRARY "MyFunctions"

Directs the compiler to include the User Library "MyFunctions.usl" from the User SIMPL+ directory. User libraries can be created by saving a SIMPL+ module as type SIMPL+ library, instead of the default SIMPL+ file.

Version:

X-Generation

SIMPL v1.50.06

SIMPL v2.01.05 and later, Global variables can no longer be declared within User Library (.usl) files.

2-Series

SIMPL v2.01.05 and later [Same features as X Generation SIMPL v2.01.05]

3-Series

SIMPL v4.00.00 and later

4-Series

SIMPL v4.14.06 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Directives/_USER_LIBRARY.htm*
