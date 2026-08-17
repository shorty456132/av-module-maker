# FindNoCase

Name:

FindNoCase

Syntax:

INTEGER FindNoCase(STRING MATCH_STRING, STRING SOURCE_STRING

[,INTEGER START_POSITION]);

Description:

Finds the position in SOURCE_STRING where MATCH_STRING first occurs. The search is case insensitive.

Parameters:

MATCH_STRING is a STRING containing the string to be matched.

SOURCE_STRING is a STRING containing the string to be searched.

START_POSITION is an INTEGER which tells FINDNOCASE at what character in the string to start the search, and is 1 based. If it is not specified, it defaults to 1.

Return Value:

The index of where MATCH_STRING first occurs (going left to right) in SOURCE_STRING. If a match can not be found, or POSITION exceeds the length of the SOURCE_STRING then 0 is returned. The index is 1 based.

Example:

STRING_INPUT IN$[100];

INTEGER START_LOC;

CHANGE IN$

{

START_LOC = FINDNOCASE("XYZ", IN$);

PRINT("XYZ was found starting at position %d in %s\n",

START_LOC, IN$);

}

If IN$ was set equal to "Hello, World!" then START_LOC would be 0 since "XYZ" can not be found. If IN$ was equal to "CPE1704XYZXYZ", then START_LOC would be equal to 8.

Version:

SIMPL+ Version 3.03.00 or later

CUZ 3.137 or later required

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/FindNoCase.htm*
