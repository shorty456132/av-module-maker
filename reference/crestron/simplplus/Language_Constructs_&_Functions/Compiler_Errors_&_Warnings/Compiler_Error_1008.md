# Compiler Error 1008

syntax error: Invalid integer argument or undefined variable: '<identifier>'

The construct being used requires either an integer value or variable passed as a function argument.

  * Make sure the variable has been declared




The following are examples of this error:

STRUCTURE MyStruct

{

INTEGER x;

STRING s[100];

}

MyStruct struct;

Function MyFunc()

{

INTEGER i;

STRING s[100];

for ( i = 1 to 10 ) // ok

{

for ( j = 1 to 5 ) // error – ‘j’ has not been declared

{

x = j; // error – should be struct.x = j;

}

for ( s = “a” to “z” ) // error – strings are not allowed

{

}

}

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1008.htm*
