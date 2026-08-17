# Compiler Error 1004

syntax error: Unmatched symbol: '<identifier>'

Some language constructs are composed of more than one keyword. In these cases, each keyword may require statements before and after it is used.

For example, the Switch statement uses the following keywords, Switch, Case, and Default. If the keyword, Case, is encountered before or outside of switch statement, this error will result.

The following are examples of this error:

FUNCTION MyFunc( INTEGER x )

{ 

x = 1;

while ( 1 )

{

x = x + 1;

} until ( x > 5 ); // error – ‘until’ is not part of the

// ‘while’ construct

else // error – no preceding ‘if’ statement

{

x = 0;

}

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1004.htm*
