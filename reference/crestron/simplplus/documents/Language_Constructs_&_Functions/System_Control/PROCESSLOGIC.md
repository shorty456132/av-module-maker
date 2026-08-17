# ProcessLogic

Name:

ProcessLogic

Syntax:

ProcessLogic();

Description:

Forces a task switch away from the current SIMPL+ module, so that the SIMPL program can process the outputs of the SIMPL+ module. Refer to the discussion on [Task Switching](<../../Task_Switching/Task_Switching_for_2-Series_Control_Systems.htm>).

Parameters:

None.

Return Value:

None.

Example:

INTEGER X;

ANALOG_OUTPUT I;

FOR(X=0 TO 25)

{

I = X;

PROCESSLOGIC();

}

In this example, the analog output I is updated every pass through the loop. Logic dependent upon the analog value will see the new analog value every pass through the loop.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/System_Control/PROCESSLOGIC.htm*
