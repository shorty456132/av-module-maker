# Abs

Name:

Abs

Syntax:

INTEGER Abs(INTEGER SOURCE);

INTEGER Abs(SIGNED_INTEGER SOURCE);

Description:

Takes the absolute value of SOURCE. If SOURCE is negative, a positive value is returned. If SOURCE is already positive, the same value is returned.

Parameters:

Takes the absolute value of an INTEGER.

Return Value:

An INTEGER corresponding to the absolute value of SOURCE.

Example:

DIGITAL_INPUT TRIG;

INTEGER I, K;

I=-5;

CHANGE TRIG

{

K=ABS(I);

PRINT("Original Value = %d, Absolute Value = %d\n", I, K);

}

The output would be:

Original Value = -5, Absolute Value = 5

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Mathematical_Functions/ABS.htm*
