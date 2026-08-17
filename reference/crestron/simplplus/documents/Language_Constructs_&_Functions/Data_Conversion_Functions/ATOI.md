# Atoi

Name:

Atoi

Syntax:

INTEGER Atoi(STRING SOURCE);

Description:

Converts a STRING to an INTEGER value. The conversion looks for the first valid character (0-9), and then reads until it finds the first invalid character. The resulting string of valid characters is then converted. The "-" is ignored, hence the output is an unsigned number [i.e., ATOI("-1") would yield 1 as the output]. If the value exceeds 65535, the value is undefined. If no valid value to convert is found, 0 is returned.

Parameters:

SOURCE is a string containing characters that range from 0 to 9 to be converted.

The result will be an unsigned number from 0 to 65535.

Return Value:

An integer representing the given string value.

Example:

STRING_INPUT IN$[100];

INTEGER VAL;

CHANGE IN$

{

VAL = ATOI(IN$);

PRINT("Value of %s after ATOI is %d\n", IN$, VAL);

}

For example, if IN$ is "abc1234xyz", then VAL will hold the integer 1234. If IN$ is "-50", then VAL will hold the integer 50.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Data_Conversion_Functions/ATOI.htm*
