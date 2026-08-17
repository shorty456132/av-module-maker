# HexToI

Name:

HexToI

Syntax:

INTEGER HexToI(STRING Source);

Description:

Returns the INTEGER value of Source. If Source exceeds 4 characters, the lower 4 characters of Source are used. 

Parameters:

STRING Source: A string containing the characters are 0 through 9, A through F, and a through f. If other characters are in the string, the result is undefined or zero, depending on the SIMPL+ Cross Compiler Include File version.

Return Value:

An integer representing the given string value.

If the source string contains characters other than A-F, a-f, 0-9 the result will be undefined if the SIMPL+ Cross Compiler Include file is less than version 1.45, or zero if the SIMPL+ Cross Compiler Include file is version 1.45 or later.

The Cross Compiler Include File version can be determined from the SIMPL+ Editor, under Help | About.

Example:

INTEGER V1, V2;

V1 = HexToI("ABCD");

V2 = HexToI("ABCDE"); // Only BCDE will be in the conversion.

PRINT("V1=%u, V2=%u\n", V1, V2);

For example, the code shown above would return: V1=43981, V2=48350

Version:

SIMPL+ Version 3.03.00 or later

CUZ 3.137 or later required

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Data_Conversion_Functions/HexToI.htm*
