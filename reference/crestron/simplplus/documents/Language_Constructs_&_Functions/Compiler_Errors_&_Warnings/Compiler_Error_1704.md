# Compiler Error 1704

library error: Error: Library name cannot be the same as the module symbol name

Library names must be unique. They cannot have the same name as the SIMPL+ module.

The following are examples of this error:

#SYMBOL_NAME “CommonFns”

#USER_LIBRARY “CommonFns” // error – same name as #SYMBOL_NAME

#USER_LIBRARY “LibraryFns” // ok

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1704.htm*
