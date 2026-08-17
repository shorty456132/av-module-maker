# Chr

Name:

Chr

Syntax:

STRING Chr(INTEGER CODE);

Description:

Takes the integer value specified and returns the corresponding ASCII character as a one-byte string.

Parameters:

CODE contains a number from 0 to 255 to be converted into an ASCII string.

Return Value:

A string representing the code. If CODE is greater than 255, lower 8-bits of CODE are used in the computation.

Example:

STRING_OUTPUT Code$;

ANALOG_INPUT VALUE;

CHANGE VALUE

{

Code$ = CHR(VALUE);

PRINT("Code = %s\n", Code$);

}

In this example, if VALUE was equal to 72, the output would be Code = H.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Data_Conversion_Functions/Chr.htm*
