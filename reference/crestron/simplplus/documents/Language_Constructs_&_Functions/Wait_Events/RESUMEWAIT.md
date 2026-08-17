# ResumeWait

Name:

ResumeWait

Syntax:

ResumeWait(NAME);

Description:

Resumes the specified named WAIT event in the current SIMPL+ program that has been previously paused. The WAIT will execute from the time when it was paused until the specified wait time has elapsed.

Parameters:

NAME is a name of a previously defined and named WAIT event.

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

PUSH ResumeWait

{

ResumeWait(FirstWait);

}

In this example, when Trig is pushed, a 10-second and 20-second event is scheduled. When PauseWaits is triggered, any of the running WAIT events will be halted. When ResumeWaits is triggered, the FirstWait event that was previously paused will resume from when it was paused. For example, if FirstWait was paused at 5-seconds, when ResumeWait(FirstWait) is called, FirstWait will have 5-seconds more to execute. SecondWait will still be paused.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Wait_Events/RESUMEWAIT.htm*
