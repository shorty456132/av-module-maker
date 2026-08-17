# PauseWait

Name:

PauseWait

Syntax:

PauseWait(NAME);

Description:

Pauses a specified named WAIT event in the current SIMPL+ program. When an event is paused, the timer for it freezes and may later be resumed, retimed, or cancelled. When a wait is resumed, it executes the remaining time from when it was paused until the defined wait time.

Parameters:

NAME is a name of a previously defined and named WAIT event.

Return Value:

None.

Example:

DIGITAL_INPUT Trig, PauseWait;

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

PUSH PauseWait

{

PauseWait(SecondWait);

}

In this example, when Trig is pushed, a 10-second and 20-second event is scheduled. When PauseWait is triggered, the SecondWait event will be paused if it has not already run to completion. It may be later cancelled, resumed, or retimed.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Wait_Events/PAUSEWAIT.htm*
