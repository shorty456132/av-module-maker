# LtoHex

Name:

LtoHex

Syntax:

STRING LTOHEX(LONG_INTEGER CODE);

Description:

Takes the value in CODE and creates a string containing the hexadecimal equivalent. The output string does not contain leading zeros and is expressed in uppercase.

Parameters:

CODE contains a number from 0 to 4294967295 to be converted into a hexadecimal string. CODE is treated as an unsigned number.

Return Value:

A string representing the code.

Note that the following two statements are equivalent:

out$ = ltohex(CODE);

makestring(out$, "%X", CODE);

Example:

STRING_OUTPUT Code$;

LONG_INTEGER VALUE;

CHANGE VALUE

{

Code$ = LTOHEX(VALUE);

PRINT("Code = %s\n", Code$);

}

For example, if VALUE contained the integer 90, Code$ would contain the string "5A".

Version:

X Generation: Not Supported

2-Series: SIMPL v2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Data_Conversion_Functions/LtoHex.htm*
