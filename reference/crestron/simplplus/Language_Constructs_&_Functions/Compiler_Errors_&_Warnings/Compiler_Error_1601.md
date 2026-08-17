# Compiler Error 1601

construct error: Duplicate CASE Statement

Constant expected: '<identifier>'

Unlike the Switch Statement the CSwitch statement’s case statements must consist of unique values. Expressions are not permitted within the case statements. Instead, each case statement must contain a unique integer value for the CSwitch’s comparison.

The following are examples of this error:

FUNCTION MyFunc( INTEGER x )

{

STRING str[100];

CSwitch( x )

{

case (1): // ok – 1 has not been used yet

{

}

case (2): // ok – 2 has not been used yet

{

}

case (2): // error – 2 has been previously used

{

}

case (5+6): // error – expressions are not allowed

{

}

case (x): // error – variables are not allowed

{

}

case (“abc”): // error – strings are not allowed

{

}

case (str): // error – strings are not allowed

{

}

}

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1601.htm*
