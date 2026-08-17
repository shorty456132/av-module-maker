# Compiler Error 1321

construct error: Dynamic variable declarations cannot be used with the

#DEFAULT_NONVOLATILE compiler directive

The declaration keyword, Dynamic, can only be used when #DEFAULT_VOLATILE is specified for the program module.

The following are examples of this error:

// MODULE A

#DEFAULT_NONVOLATILE

dynamic integer intArr[10]; // error

// MODULE B

dynamic integer intArr[10]; // error – #DEFAULT_NONVOLATILE is the

default state for this module

// MODULE C

#DEFAULT_VOLATILE

dynamic integer intArr[10]; // ok

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1321.htm*
