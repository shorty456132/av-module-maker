# SMin

Name:

SMin

Syntax:

INTEGER SMin(INTEGER VAL1, INTEGER VAL2)

Description:

Determine the minimum of two values based on a signed comparison.

Parameters:

VAL1 and VAL2 are both INTEGER values on which the test is performed.

Return Value:

The minimum of Val1, Val2 after a signed comparison is performed. Refer to "Signed vs. Unsigned Arithmetic" on page 5 for a further explanation of how the values are compared.

Example:

INTEGER X, Y;

FUNCTION MAIN()

{

X = SMIN(65535, 0);

Y = SMIN(25, 26);

}

X would be 65535 (interpreted as -1), and Y would be 25.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Mathematical_Functions/SMIN.htm*
