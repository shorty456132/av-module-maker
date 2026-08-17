# #DEFINE_CONSTANT

Name:

#DEFINE_CONSTANT

Syntax:

#DEFINE_CONSTANT <constant_name> <constant_value>

Description:

Define a <constant_value> that will be substituted anywhere in the current source file where <constant_name> is used.

Example:

#DEFINE_CONSTANT ETX 0x03

INTEGER I;

I=ETX;

Assigns the value of 0x03 to the variable I.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Directives/_DEFINE_CONSTANT.htm*
