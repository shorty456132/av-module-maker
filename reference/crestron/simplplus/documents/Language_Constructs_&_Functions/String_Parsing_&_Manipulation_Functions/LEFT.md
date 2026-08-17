# Left

Name:

Left

Syntax:

STRING Left(STRING SOURCE, INTEGER NUM);

Description:

Takes the leftmost NUM characters of SOURCE and returns them in an output string.

Parameters:

SOURCE is a STRING containing the source string.

NUM is an INTEGER that tells LEFT how many characters to use in the computation.

Return Value:

A string representing the leftmost NUM characters of SOURCE. If NUM is greater than the number of characters in SOURCE, then the return is identical to SOURCE.

Example:

STRING_INPUT Var$[100];

STRING Temp$[100];

CHANGE Var$

{

Temp$ = LEFT(Var$, 5); 

PRINT("Left most 5 characters of %s are %s\n", Var$, Temp$);

}

In this example, if Var$ is "abcdefghijk", Temp$ will contain "abcde".

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/LEFT.htm*
