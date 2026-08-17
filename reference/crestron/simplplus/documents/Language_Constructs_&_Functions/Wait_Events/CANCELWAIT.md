# CancelWait

Name:

CancelWait

Syntax:

CancelWait(NAME);

Description:

Cancels a specified named WAIT event in the current SIMPL+ program. When an event is cancelled, it is removed from the wait list and will not activate. There is no effect if the wait event has finished running.

Parameters:

NAME is a name of a previously defined and named WAIT event.

Return Value:

None.

Example:

DIGITAL_INPUT Trig, KillWaits;

PUSH Trig

{

WAIT(1000, FirstWait)

{

PRINT("Wait 1 Triggered!\n");

}

WAIT(2000, SecondWait)

{

PRINT("Wait 2 Triggered!\n");

}

}

PUSH KillWaits

{

Cancelwait(FirstWait);

}

In this example, when Trig is pushed, a 10-second and 20-second event are scheduled. When KillWaits is triggered, if FirstWait is still on the wait list, it will be removed from the wait list and will not get activated. SecondWait will activate at the end of the 20-second wait time.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Wait_Events/CANCELWAIT.htm*
