# Compiler Error 1200

expression error: Invalid numeric expression: '<expression>'

Invalid string expression

Invalid expression: '<expression>'

Expressions can be calculations, comparisons, or the validity of a value from a string or numeric variable or value. All expressions require that all variables and values within the equation are of the same type. For example, you cannot add or compare an integer and a string together. The result of a comparison (i.e.: “abc” = “def”) is always a numeric value and will be treated as a numeric expression.

The following are examples of this error:

INTEGER x, y;

STRING str[100];

INTEGER_FUNCTION myFunc( INTEGER i )

{

x = (1 + 2); // ok

if ( x > y ) // ok

{

if ( i ) // ok

{

if ( str = “abc” ) // ok

{

while ( 1 ) // ok

{

x = x + y + myFunc(1); // ok

break;

}

}

}

}

return (1);

}

INTEGER_FUNCTION AnotherFunc( INTEGER i )

{

x = (1 + str); // error – cannot add an integer

// and string

if ( x > “abc” ) // error – cannot compare an integer

// and string

{

if ( str ) // error – cannot check the validity

// of a string

{

if ( str = MyFunc(1) ) // error – cannot add strings

// and integers together

{

while ( str < “abc” ) // ok

{

x = (x + ); // error – incomplete expression

break;

}

}

}

}

return (1);

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1200.htm*
