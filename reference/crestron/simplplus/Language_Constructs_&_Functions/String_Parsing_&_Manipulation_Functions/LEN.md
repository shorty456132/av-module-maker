# Len

Name:

Len

Syntax:

INTEGER Len(STRING SOURCE);

Description:

Returns the actual length of the string, not the declared maximum length.

Parameters:

SOURCE is a string whose length is to be determined.

Return Value:

A value from 0 - 65535, which gives the number of characters in the string. An empty string returns a length of 0.

Example:

STRING_INPUT IN$[100];

INTEGER Temp;

CHANGE IN$

{

Temp = LEN(IN$);

PRINT("The Length of %s is %d\n", IN$, Temp);

}

In this example, if IN$ is equal to "This is a test" then Temp will contain the integer 14.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/LEN.htm*
