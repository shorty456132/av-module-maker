# RotateRight

Name:

RotateRight

Syntax:

INTEGER RotateRight( INTEGER X, INTEGER Y );

Description:

Rotate X to the right by Y bits; full 16 bits used. Same as }} operator.

e.g., Each bit takes the value of the bit that is Y bits more significant than it is. The most significant bit(s) are set from the least significant bits.

Parameters:

X is the INTEGER to have bits rotated

Y is the amount of bits to rotate

Return Value:

An INTEGER containing the result of the rotated bits.

Example:

INTEGER X, Y, result;

result = RotateRight( X, Y ); 

If X = 0x1234 and Y is 1, then the result is 0x091A

Version:

X Generation: Not Supported

2-Series: SIMPL v2.03.18 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Bit_%26_Byte_Functions/RotateRight.htm*
