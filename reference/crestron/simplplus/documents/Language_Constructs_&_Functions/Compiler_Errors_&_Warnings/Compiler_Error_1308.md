# Compiler Error 1308

declaration error: Declaration cannot be declared in library file: '<identifier>'

I/O declarations, Parameters and global variables can only be defined in a SIMPL+ module (.usp file). Libraries files (.usl files) are files that only contain functions. Local functions variables, function arguments and functions that return values are permitted within library files.

The following are examples of this error:

//////////////////////////////////////////////////////////////////

// MyLib.usl

INTEGER x; // error – x is global

STRING str[100]; // error – str is global

DIGITAL_INPUT di; // error – di is global

INTEGER_PARAMETER intParam; // error – intParam is

// a Parameter

FUNCTION MyFunc()

{

INTEGER i, j; // ok – i and j are local

STRING str[100]; // ok – str is local

}

INTEGER_FUNCTION MyIntFunc( INTEGER x ) // ok – x is local

{

INTEGER i, j; // ok – i and j are local

STRING str[100]; // ok – str is local

return (x);

}

STRING_FUNCTION MyStFunc( STRING s ) // ok – s is local

{

INTEGER i, j; // ok – i and j are local

STRING str[100]; // ok – str is local

return (str);

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1308.htm*
