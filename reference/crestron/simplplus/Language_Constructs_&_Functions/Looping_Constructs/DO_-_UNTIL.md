# DO - UNTIL

Name:

DO - UNTIL

Syntax:

DO

[{]

<statements>

[}] UNTIL (<expression>);

Description:

This loop performs a set of <statements> at least one time and will terminate when <expression> evaluates to true. If only one statement is present in the body of the loop, then the { and } characters are not required, but may be used. If more than one statement is present in the loop body, then the { and } characters are mandatory. Note that <expression> is evaluated each time through the loop.

Example:

INTEGER X;

X=0;

DO

{

X = X + 1;

PRINT("X = %d\n", X);

}

UNTIL (X = 25);

In this example, the loop will execute 25 times. The PRINT function will show the value of X after it is incremented to the computer port of the control system.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Looping_Constructs/DO_-_UNTIL.htm*
