# Upper

Name:

Upper

Syntax:

STRING Upper(STRING SOURCE);

Description:

Takes a source string and converts characters with the values a-z (lowercase) to A-Z (uppercase).

You can use the same variable for both the argument and return. e.g., s$=lower(s$);

Parameters:

SOURCE is a string to be converted to uppercase. SOURCE is not modified, unless it is also used as the return value, e.g., S$=UPPER(S$)

Return Value:

A STRING containing the uppercase version of SOURCE. Characters that do not fall into the range a-z are not modified and will stay as specified.

Example:

STRING_INPUT IN$[100];

STRING UPPER$[100];

CHANGE IN$

{

UPPER$ = UPPER(IN$);

PRINT("Uppercase version of %s is %s\n",IN$, UPPER$);

}

In this example, if IN$ contains "Hello There 123!" then UPPER$ contains "HELLO THERE 123!".

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/UPPER.htm*
