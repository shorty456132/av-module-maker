# Compiler Error 1505

function argument error: Format string contains invalid format specifier

An invalid format specifier was used within a format string.

Format strings contain specifications that determine the output format for the arguments. The format argument consists of ordinary characters, escape sequences, and (if arguments follow format) format specifications Format Specifications always begin with a percent sign (%) and are read left to right. When the first format specification is encountered (if any), it converts the value of the first argument after format and outputs it accordingly. The second format specification causes the second argument to be converted and output, and so on.

The following are examples of this error:

FUNCTION MyFunc()

{

Print( “Hello World” ); // ok

Print( “My name is %s. My age is %d”, “David”, 33 ); // ok

Print( “My name is %xs”, “David” ); // error - %xs is an invalid

// format specifier

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1505.htm*
