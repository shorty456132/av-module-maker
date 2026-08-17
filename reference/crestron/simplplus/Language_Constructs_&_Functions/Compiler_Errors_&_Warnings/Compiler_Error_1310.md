# Compiler Error 1310

declaration error: Compiler directive cannot be in function scope

Compiler directives cannot be used locally within functions. They can only be used at a global level and the directive applies to the entire SIMPL+ module.

NOTE: Scope refers to the level at which an Event, user-defined function or statement resides. Having a global scope means that the function or variable can be called or accessed from anywhere within the program. A local scope means that the variable can only be accessed from within the event or function that it resides in.

The following are examples of this error:

#DEFINE_CONSTANT MyConst 100 // ok – used globally

#USER_LIBRARY “MyUserLib” // ok – used globally

FUNCTION MyFunc()

{

#DEFINE_CONSTANT AnotherConst 100 // error – constants cannot

// be used locally

#USER_LIBRARY “AnotherUserLib” // error – libraries cannot

// be included locally

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1310.htm*
