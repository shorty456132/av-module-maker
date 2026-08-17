# Compiler Error 1610

construct error: GetLastModifiedArrayIndex cannot be used within a Wait Statement

The compiler encountered this function call within a Wait Statement.

The following are examples of this error:

ANALOG_INPUT AnlgIn;

INTEGER i;

CHANGE AnlgIn

{

i = GetLastModifiedArrayIndex(); // ok

}

CHANGE AnlgIn

{

Wait( 100 )

i = GetLastModifiedArrayIndex(); // error

}

CHANGE AnlgIn

{

Wait( 100 )

{

i = GetLastModifiedArrayIndex(); // error

}

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1610.htm*
