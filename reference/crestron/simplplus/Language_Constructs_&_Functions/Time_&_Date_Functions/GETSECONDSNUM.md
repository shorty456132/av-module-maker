# GETSECONDSNUM

Name:

GetSecondsNum

Syntax:

INTEGER GetSecondsNum();

Description:

Returns an integer corresponding to the number of seconds in the current time.

Parameters:

None.

Return Value:

The number of seconds from 0 to 59.

Example:

INTEGER NumSeconds;

FUNCTION MAIN()

{

NumSeconds = GetSecondsNum();

PRINT("The Number of seconds on the clock is %d\n", NumSeconds);

}

An example output of this would be "The Number of seconds on the clock is 25".

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/GETSECONDSNUM.htm*
