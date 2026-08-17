# LOWER

# 

# Lower

Name:

Lower

Syntax:

STRING Lower(STRING SOURCE);

Description:

Takes a source string and converts characters with the values A-Z (uppercase) to a-z (lowercase).

Parameters:

SOURCE is a string to be converted to lowercase. SOURCE is not modified, unless it is also used as the return value, e.g., S$=LOWER(S$);

Return Value:

A STRING containing the lowercase version of SOURCE. Characters that do not fall into the range A-Z are not modified and will stay as specified. You can use the same variable for both the argument and return. e.g., s$=lower(s$);

Example:

STRING_INPUT IN$[100];

STRING LOWER$[100];

CHANGE IN$

{

LOWER$ = LOWER(IN$);

PRINT("Lowercase version of %s is %s\n",IN$, LOWER$);

}

In this example, if IN$ contains "This is a Test123!", then LOWER$ will contain "this is a test123!".

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/LOWER.htm*
