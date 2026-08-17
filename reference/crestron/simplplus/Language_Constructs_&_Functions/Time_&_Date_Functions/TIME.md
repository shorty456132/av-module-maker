# TIME

Name:

Time

Syntax:

STRING TIME();

Description:

Returns a string containing the current system time.

Parameters:

None.

Return Value:

The return string contains the time in HH:MM:SS format, in 24-hour time. If a value is not two digits wide, it is padded with leading 0s.

Example:

STRING TheTime$[100];

FUNCTION MAIN()

{

TheTime$=TIME();

PRINT("The Time is %s\n", TheTime$);

}

An example output from this would be "The Time is 14:25:32".

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/TIME.htm*
