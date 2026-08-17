# SMAX

Name:

SMax

Syntax:

INTEGER SMax(INTEGER VAL1, INTEGER VAL2)

Description:

Determine the maximum of two values based on a signed comparison.

Parameters:

VAL1 and VAL2 are both INTEGER values on which the test is performed.

Return Value:

The maximum of Val1, Val2 after a signed comparison is performed. Refer to "Signed vs. Unsigned Arithmetic" for a further explanation of how the values are compared.

Example:

INTEGER X, Y;

FUNCTION MAIN()

{

X = SMAX(65535, 0);

Y = SMAX(25, 26);

}

X would be 0 (65535 interpreted as -1), and Y would be 26.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Mathematical_Functions/SMAX.htm*
