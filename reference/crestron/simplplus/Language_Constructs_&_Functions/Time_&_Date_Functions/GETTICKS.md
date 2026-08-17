# GETTICKS

Name:

GetTicks

Syntax:

INTEGER GetTicks();

Description:

Returns an integer corresponding to the number of system ticks. Each tick is 1/112.5 seconds for X-Generation and 0.01 seconds for 2-Series, same as GetHSeconds(). Typically, this function could be used for very fine timing, to determine if a specific amount of time has elapsed. Use of this function is discouraged, use GetHSeconds() instead.

Parameters:

None.

Return Value:

The number of ticks in the clock.

Example:

INTEGER OldTime, NewTime, Loop;

Loop=0;

OldTime=GETTICKS();

WHILE(Loop < 10000)

{

Loop = Loop + 1;

}

NewTime=GETTICKS();

PRINT("Elapsed Time is %d ticks\n", Newtime-OldTime);

An example output from this code fragment would be "Elapsed Time is 7000 ticks".

NOTE: This is bad programming as it ties up the CPU.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/GETTICKS.htm*
