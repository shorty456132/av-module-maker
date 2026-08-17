# PauseAllWait

Name:

PauseAllWait

Syntax:

PauseAllWait();

Description:

Pauses all WAIT events for the current SIMPL+ program. When an event is paused, the timer for it freezes and may later be resumed, retimed, or cancelled. When a wait is resumed, it executes the remaining time from when it was paused until the defined wait time.

Parameters:

None.

Return Value:

None.

Example:

DIGITAL_INPUT Trig, PauseWaits;

PUSH Trig

{

WAIT(1000, FirstWait)

{

PRINT("Wait 1 Triggered!\n");

}

WAIT(2000, SecondWait)

{

PRINT("Wait 2 Triggered!\n";

}

}

PUSH PauseWaits

{

PauseAllWaits();

}

In this example, when Trig is pushed, a 10-second and 20-second event is scheduled. When PauseWaits is triggered, any of the running WAIT events will be halted, but may later be resumed, cancelled, or retimed.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Wait_Events/PAUSEALLWAIT.htm*
