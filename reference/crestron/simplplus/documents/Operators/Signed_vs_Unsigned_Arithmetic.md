# Signed vs Unsigned Arithmetic

ANALOG_INPUT, ANALOG_OUTPUTs, and INTEGER in SIMPL+ are 16-bit quantities. A 16-bit quantity can range from 0 - 65535 when it is treated without having a sign (positive or negative). If a 16-bit number is treated as signed in SIMPL+, the range becomes -32768 to 32767. The range from -32768 to -1 maps into 32768 to 65535. Expressed mathematically, the mapping is 65536 - AbsoluteValue(Number). The values are treated differently depending on whether signed or unsigned comparisons are used. Another way is as follows.

Signed |  0 - 32767 |  32768 - |  65535  
---|---|---|---  
Unsigned |  0 - 32767 |  -32768 - |  -1  
  
Assignments may be directly done with negative constants, for example:

INTEGER I, J;

I = -1;

J = 65535;

Results in I being equivalent to J.

Example:

IF (65535 S> 0)

X=0;

ELSE

X=1;

Above, the value of X is set to 1 since in signed arithmetic, 65535 is the same as -1, which is not greater than 0.

IF (65535 > 0)

X=0;

ELSE

X=1;

Above, the value of X is set to 0 since in unsigned arithmetic, 65535 is greater than 0.

---
*Source: https://help.crestron.com/simpl_plus/Content/Operators/Signed_vs_Unsigned_Arithmetic.htm*
