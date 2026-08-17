# Function Libraries  
  
NOTE: A function may be placed in the same body of code as the caller. In some cases, the same function needs to be used across several different modules. Although the code could be rewritten in all modules (as was the case with SIMPL+ Version 1.00), SIMPL+ Version 2.00 supports function libraries.

A function library is simply a group of functions in a SIMPL+ file. The file is saved as a SIMPL+ Library File (*.USL), from the Save As dialog in the SIMPL+ editor.

In order to include a function library, the #CRESTRON_LIBRARY or #USER_LIBRARY directives are used. The libraries are searched in the order they are included, in case a function name is used in more than one library. The first function found is used. Refer to #CRESTRON_LIBRARY and #USER_LIBRARY for more information.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/User_Defined_Functions/Function_Libraries.htm*
