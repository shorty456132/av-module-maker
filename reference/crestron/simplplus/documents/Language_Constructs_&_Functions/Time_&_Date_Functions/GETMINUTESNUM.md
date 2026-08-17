# GETMINUTESNUM

Name:

GetMinutesNum

Syntax:

INTEGER GetMinutesNum();

Description:

Returns an integer corresponding to the number of minutes in the current time.

Parameters:

None.

Return Value:

The number of minutes from 0 to 59.

Example:

INTEGER NumMinutes;

FUNCTION MAIN()

{

NumMinutes = GetMinutesNum();

PRINT("The Number of minutes on the clock is %d\n", NumMinutes);

}

An example output of this would be "The Number of minutes on the clock is 33".

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/GETMINUTESNUM.htm*
