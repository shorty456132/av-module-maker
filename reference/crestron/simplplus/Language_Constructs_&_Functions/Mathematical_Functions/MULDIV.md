# MulDiv

Name:

MulDiv

Syntax:

INTEGER MulDiv(INTEGER VAL1, INTEGER VAL2, INTEGER VAL3)

Description:

Computes the result (VAL1 * VAL2)/VAL3.

Parameters:

VAL1, VAL2, and VAL3 are INTEGER values.

Return Value:

A 16-bit integer is returned based on the above equation. The arithmetic operations are performed using unsigned arithmetic. Note that 32-bit math is used internally, so that if VAL1*VAL2 is greater than a 16-bit number, accuracy is maintained. If the final result is greater than 16-bits, the lower 16-bits are returned.

Example:

INTEGER X, Y;

FUNCTION MAIN()

{

X = 1970;

Y = 40;

PRINT("The result of (%d * %d)/25 = %d\n", X, Y,

MULDIV(X, Y, 25);

}

The PRINT statement would show the result as being 3152. In this case, X*Y is greater than a 16-bit number, but accuracy is maintained due to the use of 32-bit arithmetic internally.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Mathematical_Functions/MULDIV.htm*
