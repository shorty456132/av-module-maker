# Atol

Name:

Atol

Syntax:

LONG_INTEGER Atol(STRING SOURCE);

Description:

Converts a STRING to an LONG_INTEGER value. The conversion looks for the first valid character (0-9), and then reads until it finds the first invalid character. The resulting string of valid characters is then converted. The "-" is ignored, hence the output is an unsigned number [i.e., ATOL("-1") would yield 1 as the output]. If no valid value to convert is found, 0 is returned. If the integer would exceed 32 bits, the value returned is undefined.

Parameters:

SOURCE is a string containing characters that range from 0 to 9 to be converted. The result will be an unsigned number from 0 to 4294967295.

Return Value:

A long integer representing the given string value.

Example:

STRING_INPUT IN$[100];

LONG_INTEGER VAL;

CHANGE IN$

{

VAL = ATOL(IN$);

PRINT("Value of %s after ATOL is %ld\n", IN$, VAL);

}

For example, if IN$ is "abc1234xyz", then VAL will hold the number 1234. If IN$ is "-50", then VAL will hold the number 50.

Version:

X Generation: Not Supported

2-Series: SIMPL v2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Data_Conversion_Functions/ATOL.htm*
