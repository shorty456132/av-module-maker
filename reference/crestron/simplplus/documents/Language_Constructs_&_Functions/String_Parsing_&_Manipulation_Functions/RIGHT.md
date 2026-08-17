# Right

Name:

Right

Syntax:

STRING Right(STRING SOURCE, INTEGER NUM);

Description:

Takes the rightmost NUM characters of SOURCE and returns them in an output string.

Parameters:

SOURCE is a STRING containing the source string.

NUM is an INTEGER that tells RIGHT how many characters to use in the computation.

Return Value:

A string representing the rightmost NUM characters of SOURCE. If NUM is greater than the number of characters in SOURCE, then the return is identical to SOURCE.

Example:

STRING_INPUT Var$[100]

STRING Temp$[100];

CHANGE Var$

{

Temp$ = RIGHT(Var$, 5); 

PRINT("Right most 5 characters of %s are %s\n", Var$, Temp$);

}

In this example, if Var$ contains "abcdefghijk", then Temp$ contains "ghijk".

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/RIGHT.htm*
