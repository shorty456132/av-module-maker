# SETCLOCK

Name:

SetClock

Syntax:

SetClock(INTEGER HOURS, INTEGER MINUTES, INTEGER SECONDS);

Description:

Sets the system clock.

Parameters:

HOURS is an integer containing the hour portion of the time to which the clock is set. HOURS is expressed in 24-hour format, which can range from 0 to 23.

MINUTES is an integer containing the minutes portion of the time to which the clock is set. MINUTES range from 0 to 59.

SECONDS is an integer containing the seconds portion of the time to which the clock is set. SECONDS range from 0 to 59.

Return Value:

None.

Example:

ANALOG_INPUT Hours, Minutes, Seconds;

CHANGE Hours, Minutes, Seconds

{

SetClock(Hours, Minutes, Seconds);

PRINT("Current Time is: %s\n", Time());

}

In this example, the Hours, Minutes, and Seconds are specified from an external SIMPL Program. For example, if Hours = 5, Minutes = 10, Seconds = 25, then the output will be Current Time is: 05:10:25.

Version:

X Generation: SIMPL v1.50.06

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/SETCLOCK.htm*
