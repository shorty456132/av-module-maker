# GETHSECONDS

Name:

GetHSeconds

Syntax:

INTEGER GetHSeconds();

Description:

Returns an integer corresponding to the number of hundredths of a second based on the system clock. Typically, this function could be used for very fine timing, to determine if a specific amount of time has elapsed.

Parameters:

None.

Return Value:

The number of hundredths of a second based on the system clock.

Example:

INTEGER OldTime, NewTime, Loop;

Loop=0;

OldTime=GETHSECONDS();

WHILE(Loop < 10000)

{

Loop = Loop + 1

}

NewTime=GETHSECONDS();

PRINT ("Elapsed Time is %d hundredths of a second.\n",

Newtime-OldTime);

The output of this code would be "Elapsed Time is 400 hundredths of a second."

NOTE: This is bad programming as it ties up the CPU.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/GETHSECONDS.htm*
