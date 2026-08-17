# CancelAllWait

Name:

CancelAllWait

Syntax:

CancelAllWait();

Description:

Cancels all WAIT events for the current SIMPL+ program. When an event is cancelled, it is removed from the wait list and will not activate. There is no effect on wait events that have finished running.

Parameters:

None.

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

CancelAllWait();

}

In this example, when Trig is pushed, a 10-second and 20-second event are scheduled. Whichever wait events are still running when KillWaits is triggered, will be removed from the Wait list and will not get activated.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Wait_Events/CANCELALLWAIT.htm*
