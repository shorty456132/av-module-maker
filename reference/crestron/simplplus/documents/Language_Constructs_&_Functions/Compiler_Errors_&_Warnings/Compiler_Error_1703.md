# Compiler Error 1703

library error: Error: Library names cannot contain path

When including User or Crestron libraries, only the library name is needed within the functions, #USER_LIBRARY and #CRESTRON_LIBRARY. Passing in a fully qualified path is not allowed.

The following are examples of this error:

#USER_LIBRARY “MyLibrary” // ok – no path is given

#USER_LIBRARY “C:\MyPath\MyLibrary” // error – C:\MyPath\ should not be specified

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1703.htm*
