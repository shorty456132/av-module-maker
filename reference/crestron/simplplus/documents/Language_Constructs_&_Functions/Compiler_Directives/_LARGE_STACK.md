# #LARGE_STACK

Name: 

#LARGE_STACK

Syntax:

#LARGE_STACK

Description:

Increase the stack size. Usually the default stack size is sufficient, unless heavy recursion is being done. If you see an error similar to:

Module S-5 : foobar.umc at line 25: Stack overflow. Terminating Task. (space =xxxx)

You can try using the #LARGE_STACK directive, which increases the stack size to 8k. If this does not help, the module should be checked for heavy recursion. See [#Enable_Stack_Checking](<_ENABLE_STACK_CHECKING.htm>) to allow run-time stack checking to be performed on this module.

In functions, only INTEGER declarations (not strings, string arrays, or integer arrays) are taken from the stack.

NOTE: #LARGE_STACK must be defined before all User-Defined functions are declared.

Example:

#LARGE_STACK

Version:

X Generation: Not supported

2-Series: SIMPL v2.05.17 and later (Requires CUZ 3.080 or later)

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Directives/_LARGE_STACK.htm*
