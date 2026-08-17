# FOR

Name:

FOR

Syntax:

FOR (<variable> = <start_expression> TO <end_expression>

[STEP <step_expression>])

[{]

<statements>

[}]

Description:

This loop executes the <statements> while <variable> iterates from the value of <start_expression> to the value of <end_expression>. The variable is incremented by <step_expression> at the end of the loop, if STEP is specified, else it is incremented by 1. The <step_expression> can be negative which will result in the loop counting down. If only one statement is present in the body of the loop, then the { and } characters are not required, but may be used. If more than one statement is present in the loop body, then the { and } characters are mandatory. Note that <start_expression> and <end_expression> are evaluated once before the loop starts and are not re-evaluated during the execution of the loop. If it is defined, <step_expression> is evaluated each pass through the loop, so <step_expression> may be modified during execution of the loop.

In the 2-Series control systems, the <step_expression> cannot change its sign during the execution of the loop. That is, if it is initially a positive number, then it is assumed if it will always count up. If it is negative, it will always count down.

NOTE: If <variable> is set to a value greater than the <end_expression> within the body of the FOR loop, the FOR loop will exit when it reaches the end.

At the end of the loop, the loop index has the value of <end_expression> \+ 1 (unless the loop index was modified in the body of the loop).

The comparisons are based on signed numbers, the maximum loop size for a step of one would be from 1 to 32767. If larger indices are needed, for example, from 1 to 60000 a DO-UNTIL or WHILE loop could be used.

Example:

STRING_INPUT IN$[100];

INTEGER X;

FOR (X = 1 TO LEN(IN$))

{

PRINT("Character %d of String %s is %s\n", X, IN$,

MID(IN$, X, 1));

}

In this example, the loop will iterate through each character of a string and print out the string and its position in the original string.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Looping_Constructs/FOR.htm*
