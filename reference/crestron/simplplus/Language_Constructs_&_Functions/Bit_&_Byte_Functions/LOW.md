# Low

Name:

Low

Syntax:

INTEGER Low(INTEGER VALUE)

Description:

Returns the lower least significant 8-bits of an Integer.

Parameters:

VALUE is an integer containing the value of the least significant byte.

Return Value:

The lower 8-bits of the passed value.

Example:

ANALOG_INPUT VALUE;

CHANGE VALUE

{

PRINT("The lower byte of %X is %X\n", VALUE, LOW(VALUE));

}

This will print the input value and the lower 8-bits of the value in hexadecimal. For example, if VALUE is 0x1234, then the output is The lower byte of 1234 is 34.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Bit_%26_Byte_Functions/LOW.htm*
