# GETDATENUM

Name:

GetDateNum

Syntax:

INTEGER GetDateNum();

Description:

Returns an integer corresponding to the current day of the month.

Parameters:

None.

Return Value:

The day of the month as an integer from 1 to 31.

Example:

INTEGER NumDateOfMonth;

FUNCTION MAIN()

{

NumDateOfMonth = GetDateNum();

PRINT("The current day of the month is %d\n", NumDateOfMonth);

}

An example output of this would be "The current day of the month is 25".

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/GETDATENUM.htm*
