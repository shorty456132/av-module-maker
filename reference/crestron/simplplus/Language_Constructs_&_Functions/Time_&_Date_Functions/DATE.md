# Date

Name:

Date

Syntax:

STRING Date(INTEGER FORMAT);

Description:

Returns a string corresponding to the current date with the specified FORMAT.

Parameters:

FORMAT is an integer describing the way to format the date for the return. Valid formats are 1 through 4.

FORMAT 1 returns a string in the form MM/DD/YYYY

FORMAT 2 returns a string in the form DD/MM/YYYY

FORMAT 3 returns a string in the form YYYY/MM/DD

FORMAT 4 returns a string in the form MM/DD/YY

In format 4, the year 2000 is shown as 00. Digits 58 - 99 are treated as 1958-1999 and 00-57 are treated as 2000 through 2057.

Return Value:

A STRING corresponding to the current date.

Example:

STRING TheDate$[100];

FUNCTION MAIN()

{

TheDate$=DATE(1);

PRINT("The date is %s\n", TheDate$);

}

This would print a string such as "The date is 03/25/1999".

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/DATE.htm*
