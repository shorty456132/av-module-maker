# GETHOURNUM

Name:

GetHourNum

Syntax:

INTEGER GetHourNum();

Description:

Returns an integer corresponding to the number of hours in the current time.

Parameters:

None.

Return Value:

The number of hours from 0 to 23 (24-hour time format).

Example:

INTEGER NumHours;

FUNCTION MAIN()

{

NumHours = GetHourNum();

PRINT("The Number of hours on the clock is %d\n", NumHours);

}

An example output of this would be "The Number of hours on the clock is 22".

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/GETHOURNUM.htm*
