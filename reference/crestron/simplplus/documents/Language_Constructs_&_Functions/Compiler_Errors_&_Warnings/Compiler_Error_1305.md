# Compiler Error 1305

declaration error: Local functions not supported

A function cannot be defined within another function definition. All function definitions must be defined with a global scope inside the module.

NOTE: Scope refers to the level at which an Event, user-defined function or statement resides. Having a global scope means that the function or variable can be called or accessed from anywhere within the program. A local scope means that the variable can only be accessed from within the event or function that it resides in.

The following are examples of this error:

FUNCTION MyFunc() // ok – MyFunc is global

{

FUNCTION MyLocalFunc() // error – MyLocalFunc is local to MyFunc

{

}

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1305.htm*
