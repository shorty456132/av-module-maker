# ResumeAllWait

Name:

ResumeAllWait

Syntax:

ResumeAllWait();

Description:

Resumes all WAIT events for the current SIMPL+ program that had been previously paused. The WAIT will execute when the time from when it was frozen until the specified wait time has elapsed.

Parameters:

None.

Return Value:

None.

Example:

DIGITAL_INPUT Trig, PauseWaits, ResumeWaits;

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

PauseAllWait();

}

PUSH ResumeWaits

{

ResumeAllWaits();

}

In this example, when Trig is pushed, a 10-second and 20-second event is scheduled. When PauseWaits is triggered, any of the running WAIT events will be halted. When ResumeWaits is triggered, the previously paused waits will resume from when they were paused. For example, if FirstWait and SecondWait were paused at 5-second, when ResumeAllWait is called, FirstWait will have 5-seconds more to execute and SecondWait will have 15-seconds more to execute.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Wait_Events/RESUMEALLWAIT.htm*
