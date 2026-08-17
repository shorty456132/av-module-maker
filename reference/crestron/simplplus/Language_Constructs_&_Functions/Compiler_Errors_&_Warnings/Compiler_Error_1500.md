# Compiler Error 1500

function argument error: Argument <arg_num> cannot be passed by reference

A variable was being passed that can either only have a value assigned to it, or it’s value be copied into another variable or used within an expression. An example of this is trying to pass a STRING_INPUT variable as a function argument; the STRING_INPUT must first be copied into a STRING variable and then passed.

Pass by Reference – The function will act directly on the variable that was passed as the argument. Any changes to the variable within the called function the will be reflected within the calling function.

Pass by Value – The function creates a local copy of the source variable. Any changes to this local copy are not reflected in the source variable that was originally passed to the function. The source variable will still retains its original value from before the function was called.

The following are examples of this error:

INTEGER i;

STRING str[100];

STRING_INPUT strIn[100];

STRING_OUTPUT strOut;

DIGITAL_INPUT di;

FUNCTION MyFunc( STRING s )

{

str = strIn;

Call MyFunc( str ); // ok – the previous statement copied

// ‘strIn’ into ‘str’

Call MyFunc( “abc” ); // ok

Call MyFunc( strIn ); // error – strIn is a STRING_INPUT and

// cannot be passed by reference

Call MyFunc( strOut ); // error – strIn is a STRING_OUTPUT and

// cannot be passed by reference

}

FUNCTION MyFunc2( ByRef STRING s ) // error – STRINGs cannot be

// passed by reference

{

Call MyFunc2( str ); // error – STRINGs cannot be

// passed by reference

}

FUNCTION AnotherFunc( ByRef INTEGER x )

{

Call AnotherFunc( 1 ); // ok

Call AnotherFunc( di ); // error – di is a DIGITAL_INPUT and

// cannot be passed

// by reference

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1500.htm*
