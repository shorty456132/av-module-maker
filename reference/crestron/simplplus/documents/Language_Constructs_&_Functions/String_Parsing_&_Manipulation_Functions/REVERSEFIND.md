# REVERSEFIND

Name:

ReverseFind

Syntax:

INTEGER ReverseFind(STRING MATCH_STRING, STRING SOURCE_STRING

[, INTEGER START_POSITION]);

Description:

Finds the position in SOURCE_STRING where MATCH_STRING last occurs. The search is case-sensitive.

Parameters:

MATCH_STRING is a STRING containing the searched for data.

SOURCE_STRING is a STRING containing the data to be searched.

START_POSITION is an INTEGER which tells REVERSEFIND at what character in the string to start the search, and is 1 based. If it is not specified, it defaults to the end of the string.

Return Value:

The index of where MATCH_STRING last occurs (going right to left) in SOURCE_STRING. If the data can not be found, or POSITION exceeds the length of the SOURCE_STRING then 0 is returned. The index is 1 based.

Example:

STRING_INPUT IN$[100];

INTEGER START_LOC;

CHANGE IN$

{

START_LOC = REVERSEFIND("XYZ", IN$);

PRINT("last XYZ occurrence was found at position %d in %s\n", START_LOC, IN$);

}

If IN$ was set equal to "Hello, World!" then START_LOC would be 0 since "XYZ" can not be found. If IN$ was equal to "CPE1704XYZXYZ", then START_LOC would be equal to 11.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/REVERSEFIND.htm*
