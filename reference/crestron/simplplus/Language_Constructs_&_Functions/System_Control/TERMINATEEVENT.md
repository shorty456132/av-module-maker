# TerminateEvent

Name:

TerminateEvent

Syntax:

TerminateEvent;

Description:

Exits a CHANGE, PUSH, or RELEASE event. It may also be used to exit a loop in the main() function if desired. TERMINATEEVENT cannot be used inside of a function.

Example:

INTEGER X;

ANALOG_INPUT Y;

CHANGE Y

{

X=0;

WHILE(X<25)

{

IF(Y = 69)

TerminateEvent;

X = X + 1;

PRINT("X=%d\n", X);

}

}

In this example, the CHANGE event will terminate if the ANALOG_INPUT Y equals the value of 69. Otherwise, the CHANGE will exit after the WHILE loop finishes.

Version:

X Generation

SIMPL v1.20.01 and later

2-Series

SIMPL v2.01.05 and later. Within functions, returns from the function, it does NOT terminate the event. Existing code that relies on the event terminating should be revised.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/System_Control/TERMINATEEVENT.htm*
