# Compiler Error 1402

assignment error: Variable can only be used for assignment: '<identifier>'

STRING_OUTPUT variables can only have their values read. Once assigned a value, that value is immediately acted upon by the control system, and the value is assumed to be unknown thereafter.

The following are examples of this error:

STRING_OUTPUT sOut;

STRING str[100];

FUNCTION MyFunc()

{

str = “abc”; // ok

sOut = str; // ok – sOut can be assigned a value

sOut = “abc”; // ok – sOut can be assigned a value

str = sOut; // error – the value of sOut is lost

Print( “str = %s”, str ); // ok – STRINGs can be read and written

Print( “sOut = %s”, sOut ); // error – the value of sOut is unknown

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1402.htm*
