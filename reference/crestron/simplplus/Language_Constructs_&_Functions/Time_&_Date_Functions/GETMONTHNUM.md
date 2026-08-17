# GETMONTHNUM

Name:

GetMonthNum

Syntax:

INTEGER GetMonthNum();

Description:

Returns an integer corresponding to the current month of the year.

Parameters:

None.

Return Value:

The month of the year as an integer from 1 to 12.

Example:

INTEGER NumMonth;

FUNCTION MAIN()

{

NumMonth = GetMonthNum();

PRINT("The current month of the year is %d\n", NumMonth);

}

An example output of this would be "The current month of the year is 9".

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/GETMONTHNUM.htm*
