# ItoA

Name:

ItoA

Syntax:

STRING ItoA(INTEGER CODE);

Description:

Takes the value in CODE and creates a string containing the string equivalent of that integer. The output string does not contain leading zeros.

Parameters:

CODE contains a number from 0 to 65535 to be converted into a string. CODE is treated as an unsigned number.

Return Value:

A string representing the code. If CODE is greater than 65535, lower 16-bits of CODE are used in the computation.

Note that the following two statements are equivalent:

out$ = itoa(CODE);

makestring(out$, "%d", CODE);

Example:

STRING_OUTPUT Code$;

ANALOG_INPUT VALUE;

CHANGE VALUE

{

Code$ = ITOA(VALUE);

PRINT("Code$ = %s\n", ITOA(VALUE);

}

For example, if VALUE was equal to 25, Code$ would contain the string "25".

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Data_Conversion_Functions/ITOA.htm*
