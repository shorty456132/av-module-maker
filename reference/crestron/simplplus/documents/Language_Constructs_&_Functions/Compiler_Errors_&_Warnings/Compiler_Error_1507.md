# Compiler Error 1507

function argument error: Argument <arg_num>: Missing or invalid array

An integer or string variable array was expected and was not encountered.

The following are examples of this error:

FUNCTION MyFunc( INTEGER x[], STRING str[] )

{

INTEGER i;

STRING strArr[100][100];

SetArray( x, 1 ); // ok

Call MyFunc( x, StrArr ); // ok

SetArray( i, 1 ); // error – i is not an array

Call MyFunc( 1, “abc” ); // error – 1 is not an array

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1507.htm*
