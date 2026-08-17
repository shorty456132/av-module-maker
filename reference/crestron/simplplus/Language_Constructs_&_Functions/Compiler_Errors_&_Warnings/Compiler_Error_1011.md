# Compiler Error 1011

syntax error: Missing return value

The Return statement requires a valid value or expression when used inside of functions that return a value (INTEGER_FUNCTION, STRING_FUNCTION, etc.). The Return statement is available for functions that don’t return a value (FUNCTION), but do not allow values to be returned.

The following are examples of this error:

FUNCTION MyFunc( INTEGER x )

{

if ( x=1 )

return; // ok – MyFunc() does not return a value

return (5); // error – MyFunc is declared as FUNCTION and

// cannot return a value

}

INTEGER_FUNCTION AnotherFunc( INTEGER x )

{

if ( x=1 )

return; // error – MyFunc is declared as an INTEGER_FUNCTION

// and must return a value

else if ( x=2 )

return (5); // ok

else if ( x=3 )

return (); // error – no value or expression is given

return (x); // ok

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1011.htm*
