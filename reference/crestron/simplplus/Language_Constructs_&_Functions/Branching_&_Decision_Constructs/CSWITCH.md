# CSWITCH

Name:

CSWITCH

Syntax:

CSWITCH (<expression>)

{

CASE (<unique integer constant>):

[{]

<statements1>

[break;]

[}]

CASE (<unique integer constant >):

[{]

<statements2>

[break;]

[}]

[DEFAULT:

[{]

<statements>

[break;]

[}]

}

NOTE: In SIMPL+ v3.01.00 and later, the 'break' statement is required to terminate the case statement block that it resides within. If no 'break' statement exists, the program will continuing executing to the next case statement block or default statement block.

NOTE: Many CASE statements may be used in the body of the CSWITCH. 

Description:

CSWITCH is a more direct method of writing a complex IF-ELSE-IF statement. In the CSWITCH, if <expression> is equal to a CASE’s constant, then the statement block for that CASE value is executed. This same method would apply to as many CASE statements as are listed in the body of the CSWITCH. Note that if any of the <statements> blocks are only a single statement, the { and } characters on the CASE may be omitted. If no condition is met in the CASE statements, the DEFAULT case, if specified, is used.

CSWITCH has the restriction that the case statement only contains unique integer constants. CSWITCH differs from SWITCH in that the operating system is able to evaluate and execute the CSWITCH statement faster. Therefore, you should use CSWITCH in place of SWITCH whenever unique constants are being evaluated.

Example:

ANALOG_INPUT AIN;

INTEGER X;

CSWITCH( AIN )

{

CASE (2):

{

X = 0;

break; // terminate this case statement block

}

CASE (3):

{

X = AIN;

// continue executing to next case statement block ==> case(5)

}

CASE (5):

{

X = X + AIN + 1;

break;

}

DEFAULT:

{

PRINT("Unknown command %d!\n", AIN);

break;

}

}

In this example, if the value of AIN is 2, X is set equal to 0. If AIN is 3, X is set AIN + AIN + 1. If AIN is 5, X is set equal to AIN+1. If AIN is any other value, an error message is printed.

Version:

X Generation: Not Supported

2-Series: SIMPL v2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Branching_%26_Decision_Constructs/CSWITCH.htm*
