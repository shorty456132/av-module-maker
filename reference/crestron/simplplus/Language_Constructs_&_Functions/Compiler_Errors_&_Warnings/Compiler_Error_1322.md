# Compiler Error 1322

construct error: Variable cannot be declared as dynamic: <variable>

The declaration keyword, Dynamic, can only be used with string or array declarations. I/O declarations are not allowed to be declared as dynamic.

The following are examples of this error:

#DEFAULT_VOLATILE

dynamic integer i; // error – ‘i’ is not an array

dynamic string_input si // error – I/O declarations are not

permitted

dynamic integer intArr[10]; // ok

dynamic string str[10]; // ok

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1322.htm*
