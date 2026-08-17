# Day

Name:

Day

Syntax:

STRING Day();

Description:

Returns the day of the week as a STRING.

Parameters:

None.

Return Value:

The day of the week is returned in a string. Valid returns are Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday.

Example:

STRING TheDay$[100];

FUNCTION MAIN()

{

TheDay$=DAY();

PRINT("The day of the week is %s\n", TheDay$);

}

An example output of this would be "The day of the week is Monday".

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/DAY.htm*
