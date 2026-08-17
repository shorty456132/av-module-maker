# GETYEARNUM

Name:

GetYearNum

Syntax:

INTEGER GetYearNum();

Description:

Returns an integer corresponding to the current year.

Parameters:

None.

Return Value:

The year as an integer. The full year is specified. For example, the year 2000 will return the integer 2000.

Example:

INTEGER NumYear;

FUNCTION MAIN()

{

NumYear = GetYearNum();

PRINT("The current year is %d\n", NumYear);

}

An example output from this would be "The current year is 1999".

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/GETYEARNUM.htm*
