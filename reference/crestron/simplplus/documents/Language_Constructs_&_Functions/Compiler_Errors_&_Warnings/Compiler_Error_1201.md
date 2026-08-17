# Compiler Error 1201

expression error: Invalid \\\x sequence

Invalid \\\x sequence: '<expression>'

A hexadecimal sequence within a literal string contained an invalid format. Characters represented by a hexadecimal number must follow the format: \xXX, where ‘\x’ signifies that a hexadecimal sequence is to follow and XX is the 2 digit hexadecimal value.

The following are examples of this error:

Function myFunc()

{

STRING str[100];

MakeString( str, “Sending commands \xFF” ); // ok

MakeString( str, “Sending commands \x41\x1A\xFF” ); // ok

MakeString( str, “Sending cmd \x4” ); // error – 2 digits required

MakeString( str, “Sending cmd \x” ); // error – hex code expected

MakeString( str, “Sending cmd \xZZ” ); // error – invalid hex code

MakeString( str, “Sending cmd \xZZ” ); // error – invalid hex code

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1201.htm*
