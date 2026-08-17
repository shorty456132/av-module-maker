# SWITCH

Name:

SWITCH

Syntax:

SWITCH (<expression>)

{

CASE (<expression1>):

[{]

<statements1>

[}]

CASE (<expression2>):

[{]

<statements2>

[}]

[DEFAULT:

[{]

<statements>

[}]

}

NOTE: Many CASE statements may be used in the body of the SWITCH.

Description:

SWITCH is a more direct method of writing a complex IF-ELSE-IF statement. In the SWITCH, if <expression> is equal to <expression1>, <statements1> is executed. If <expression> is equal to <expression2>, <statements2> is executed. This same method would apply to as many CASE statements as are listed in the body of the SWITCH. Note that if any of the <statements> blocks are only a single statement, the { and } characters on the CASE may be omitted.

SWITCH has the restriction that the expressions may not be STRING expressions, they can only be INTEGER type expressions. SWITCH may only have up to 32 CASE statements in SIMPL+ Version 1.00. If more are used, a "FULL STACK" error results at the time of uploading the module to the control system. Version 2.00 has no restriction.

When a SWITCH is evaluated, the first matching CASE is used. If another CASE (or more) would have matched, only the first one is used. If no condition is met in the CASE statements, the DEFAULT case is used if specified.

Example:

ANALOG_INPUT AIN;

INTEGER X;

SWITCH(AIN)

{

CASE (2):

{

X = 0;

}

CASE (3):

{

X = AIN;

}

CASE (5):

{

X = AIN + 1;

}

DEFAULT:

PRINT("Unknown command %d!\n", AIN);

}

In this example, if the value of AIN is 2, X is set equal to 0. If AIN is 3, X is set equal to AIN. If AIN is 5, X is set equal to AIN+1. If AIN is any other value, an error message is printed.

Version:

X Generation

SIMPL v1.20.01, 32 CASE statements maximum.

SIMPL v1.50.06 and later, no CASE restriction.

2-Series

SIMPL v2.01.05 and later [same features as X Generation SIMPL v1.50.06]

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Branching_%26_Decision_Constructs/SWITCH.htm*
