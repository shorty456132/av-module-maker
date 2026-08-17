# Compiler Warning 1803

compiler warning: Possible data loss: LONG_INTEGER to INTEGER assignment

A LONG_INTEGER result was assigned to an INTEGER variable or passed to a function for an INTEGER parameter. The 32-bit LONG_INTEGER will be truncated to 16-bit value and assigned to the integer, resulting in a loss of data.

  * Make sure all the datatypes within an expression are of the same datatype.

  * Make sure the parameter of a function being called is of the same datatype as the argument being passed in.

  * Make sure the return value of a function matches the destination’s datatype.




The following are examples of this warning:

LONG_FUNCTION MyFunc( INTEGER x )

{

INTEGER i;

LONG_INTEGER j;

i = i; // ok – both sides of the assigment are of

// the same datatype

j = i; // ok – no loss of data

j = j; // ok – both sides of the assigment are of

// the same datatype

i = j; // warning – LONG_INTEGER being assigned to

// an INTEGER

Call MyFunc( i ); // ok

Call MyFunc( j ); // warning

i = MyFunc( 5 ); // warning – the integer, i, is being assigned a

// LONG_INTEGER value

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Warning_1803.htm*
