# #ENABLE_STACK_CHECKING

Name: 

#ENABLE_STACK_CHECKING

Syntax:

#ENABLE_STACK_CHECKING

Description:

Allow run-time stack checking to be performed on this module. If there is a stack overflow, you will see an error similar to:

Module S-5 : ExampleSimpl+Code.umc at line 25: Stack overflow. Terminating Task. (space =xxxx)

When a function is called, it adds memory to the stack. When the function returns, the memory is removed from the stack. However, if you have a recursive program or if inputs come in faster than they can be processed (i.e. the PUSH/CHANGE/EVENT function is called but does not finish and return), the stack may continue to grow. This option checks for a stack whose memory grows beyond that which is allocated. The default memory allocation is 4k.

Refer to [#Large_Stack](<_LARGE_STACK.htm>) to increase the stack size.

NOTE: #ENABLE_STACK_CHECKING must be defined before all User-Defined functions are declared.

Example:

#ENABLE_STACK_CHECKING

Version:

X Generation: Not supported

2-Series: SIMPL v2.05.17 and later (Requires CUZ 3.080 or later).

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Directives/_ENABLE_STACK_CHECKING.htm*
