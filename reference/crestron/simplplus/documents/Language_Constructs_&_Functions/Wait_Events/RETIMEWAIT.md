# RetimeWait

Name:

RetimeWait

Syntax:

RetimeWait(INTEGER TIME, NAME);

Description:

Changes the time for a wait event in progress. When a WAIT is retimed, the WAIT is restarted. For example, if a 5-second wait is 3-second in, and it is retimed to 10-second, a full 10-seconds must elapse before the WAIT triggers.

Parameters:

TIME is an integer that specifies the new wait time in hundredths of a second. If time is set to 0, the event will occur immediately.

NAME is a name of a previously defined WAIT event.

Return Value:

None.

Example:

DIGITAL_INPUT Trig, ChangeWaitTime;

PUSH Trig

{

WAIT(1000, FirstWait)

{

PRINT("Wait 1 Triggered!\n");

}

}

PUSH ChangeWaitTime

{

RetimeWait(500, FirstWait);

}

In this example, when Trig is pushed, a 10-second event is scheduled. If ChangeWaitTime is activated while FirstWait is still running, the time will be reset to 5-seconds. If FirstWait has expired, no action will be taken.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Wait_Events/RETIMEWAIT.htm*
