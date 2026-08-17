# GETDAYOFWEEKNUM

Name:

GetDayOfWeekNum

Syntax:

INTEGER GetDayOfWeekNum();

Description:

Returns an integer corresponding to the current day of the week.

Parameters:

None.

Return Value:

The day of the week as an integer from 0 to 6; 0 represents Sunday to 6 representing Saturday.

Example:

INTEGER NumDayOfWeek;

FUNCTION MAIN()

{

NumDayOfWeek = GetDayOfWeekNum();

PRINT("The current day of the week is %d\n", NumDayOfWeek);

}

An example output of this would be "The current day of the week is 4".

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/GETDAYOFWEEKNUM.htm*
