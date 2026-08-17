# 

# Lower

Name:

Lower

Syntax:# 

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

# Mid

Name:

Mid

Syntax:

STRING Mid(STRING SOURCE, INTEGER START, INTEGER NUM);

Description:

Returns a string NUM characters long from SOURCE, starting at position START.

Parameters:

SOURCE is a STRING containing the input string.

START is an INTEGER telling MID at which character position in SOURCE to start. The first character of SOURCE is considered 1.

NUM is an INTEGER telling MID how many characters to use from SOURCE.

Return Value:

A string NUM characters long starting at START.

If START is greater than the length of SOURCE, an empty STRING is returned.

If NUM is greater than the total number of characters that can be retrieved starting from START, only the remaining characters in SOURCE will be pulled. For example, MID("ABCD", 2, 10) would return a STRING containing BCD.

Example:

STRING_INPUT Var$[100];

STRING Temp$[100];

CHANGE Var$

{

Temp$ = MID(Var$, 2, 5); 

PRINT("String starting at position 2 for 5 characters is %s\n",

Temp$);

}

In this example, if Var$ contains "abcdefghijklmnop", then Temp$ will contain "bcdef".

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/MID.htm*
