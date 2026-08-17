# MONTH

Name:

Month

Syntax:

STRING Month();

Description:

Returns the current month as a string.

Parameters:

None.

Return Value:

The current month is returned in a string. Valid returns are January, February, March, April, May, June, July, August, September, October, November, or December.

Example:

STRING TheMonth$[100];

FUNCTION MAIN()

{

TheMonth$=MONTH();

PRINT("The Month is %s\n", TheMonth$);

}

An example output of this would be "The Month is September".

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/MONTH.htm*
