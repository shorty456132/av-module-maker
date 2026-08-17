# BREAK

Name:

BREAK

Syntax:

BREAK;

Description:

Terminates the innermost DO-UNTIL, FOR, or WHILE loop before the exit condition is met.

Execution resumes after the end of the loop.

Example:

INTEGER X;

ANALOG_INPUT Y;

X=0;

WHILE(X<25)

{

IF(Y = 69)

BREAK;

X = X + 1;

PRINT("X=%d\n", X);

}

In this example, the WHILE loop will terminate if the ANALOG_INPUT Y equals the value of 69. Otherwise, the loop will exit via the normal termination condition.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Branching_%26_Decision_Constructs/BREAK.htm*
