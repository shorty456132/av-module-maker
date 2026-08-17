# Returning a Value

The syntax for returning a value from integer and string functions is RETURN <expression>;.   
To return from a FUNCTION, PUSH, CHANGE, RELEASE or EVENT, the syntax is RETURN.

Integer functions include INTEGER_FUNCTION, SIGNED_INTEGER_FUNCTION, LONG_INTEGER_FUNCTION and SIGNED_LONG_INTEGER_FUNCTION. String functions include STRING_FUNCTION.

For Integer Functions, any valid integer expression is legal. For example:

RETURN (25);

RETURN (Z + MULDIV(A,B,C) + 100);

Are legal (assuming Z, A, B, C, are INTEGERs). If no RETURN statement is present in an integer, 0 is returned.

NOTE: If no Return Value is specified within an String_Function, then an empty string will be returned by default.

NOTE: RETURN is a 2-Series only function.

For a string function, any valid string is legal (string expressions are not allowed). For example:

STRING str[100];

RETURN ("Hello!\n");

RETURN (str);

Are legal (assuming Z is an INTEGER and A$ is a STRING). If no RETURN statement is present in a STRING_FUNCTION, an empty string ("") is returned.

In SIMPL Version 3.00, the RETURN statement without arguments can be used in all functions that do not return strings or integers. For example:

INTEGER_FUNCTION MyIntegerFn ( )

{

IF (1)

{

RETURN (1);

}

RETURN (0);

}

LONG_INTEGER_FUNCTION MyLongIntFn ( )

{

IF (1)

{

RETURN (1);

}

RETURN (0);

}

SIGNED_INTEGER_FUNCTION MySignedIntFn ( )

{

IF (1)

{

RETURN (1);

}

RETURN (0);

}

SIGNED_LONG_ INTEGER_FUNCTION MySignedLongIntFn ( )

{

IF (1)

{

RETURN (1);

}

RETURN (0);

}

STRING_FUNCTION MyStringFn ( )

{

IF (1)

{

RETURN ("abc");

}

RETURN ("def");

}

FUNCTION MyFn ( )

{

IF (1)

{

return;

}

}

EVENT

{

if (1)

return;

}

PUSH

{

if (1)

return;

}

RELEASE

{

if (1)

return;

}

CHANGE

{

if (1)

return;

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/User_Defined_Functions/Returning_a_Value.htm*
