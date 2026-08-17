# Compiler Error 1304

declaration error: Local variables must be declared at top of function

All local variables within a function block must be declared before any statements are encountered. Local variables are not allowed to be declared within a block of statements such as inside an if-else or while loop.

The following are examples of this error:

FUNCTION MyFunc( INTEGER arg1, STRING arg2 ) // ok

{

INTEGER i; // ok

STRING str[100]; // ok

Print( “Inside MyFunc!” );

INTEGER j; // error

if ( i > 1 )

{

INTEGER k; // error – if-statement block cannot

contain local variables

}

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1304.htm*
