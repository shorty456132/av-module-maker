# Compiler Error 1502

function argument error: Function contains incomplete number of arguments

Function call contains an unmatched number of

arguments

When calling a function that contains parameter lists, the number of arguments passed to the function must match the number of parameters defined for that function.

The following are examples of this error:

FUNCTION MyFunc( INTEGER x, STRING str )

{

Call MyFunc( 1, “abc” ); // ok

Call MyFunc(); // error – 2 arguments are expected

Call MyFunc( 1 ); // error – argument 2 is missing

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1502.htm*
