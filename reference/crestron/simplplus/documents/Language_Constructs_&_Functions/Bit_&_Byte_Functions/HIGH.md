# High  
  
Name:

High

Syntax:

INTEGER High(INTEGER VALUE);

Description:

Returns the upper most significant 8-bits of an Integer.

Parameters:

VALUE is an integer containing the value of the most significant byte. It is not sign extended.

Return Value:

The upper 8-bits of the passed value. The return value is not signed extended, It is intended only for unsigned short integers (16 bits).

Example:

ANALOG_INPUT VALUE;

CHANGE VALUE

{

PRINT("The upper byte of %X is %X\n", VALUE, HIGH(VALUE));

}

This will print the input value and the upper 8-bits of the value in hexadecimal. For example, if VALUE is 0x1234, then the output is The upper byte of 1234 is 12.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Bit_%26_Byte_Functions/HIGH.htm*
