# Compiler Error 1323

construct error: #ENABLE_DYNAMIC compiler directive must be used when

using declaring variables dynamically

In order to declare Strings and Arrays dynamically, the compiler directive, #ENABLE_DYNAMIC, must be specified beforehand within the module.

Dynamic memory allocation is the allocation of a variable’s memory at run-time. The amount of memory allocated is determined by the program at the time of allocation and need not be known in advance.

Using Dynamic variables allows a String or Array variable’s memory allocation to grow or shrink in size. Rather than initially declare a String or Array variable to some large amount, the variable can be dynamically resized to the correct amount in real-time.

NOTE: Dynamic variables are specific to Firmware versions 4.000 and later

The following are examples of this error:

/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

// Example 1

#ENABLE_DYNAMIC

DYNAMIC STRING str[10]; // ok, #ENABLE_DYNAMIC

// declared at top of module

FUNCTION foo()

{

SIGNED_INTEGER status;

DYNAMIC INTEGER arr[10][10]; // ok, #ENABLE_DYNAMIC

// declared at top of module

status = ResizeString( str, 100 );

status = ResizeArray( arr, 200, 100);

}

//////////////////////////////////////////////////////////////////////////

// Example 2

DYNAMIC STRING str[10]; // error, #ENABLE_DYNAMIC not

// declared at top of module

FUNCTION foo()

{

SIGNED_INTEGER status;

DYNAMIC INTEGER arr[10][10]; // error, #ENABLE_DYNAMIC not

// declared at top of module

status = ResizeString( str, 100 );

status = ResizeArray( arr, 200, 100);

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1323.htm*
