# Compiler Error 1504

function argument error: Incomplete number of format string arguments

Format string contains an unmatched number

of arguments

Argument <arg_num> is missing or invalid.

Format Specifier expected

Argument <arg_num> is missing or invalid.

<decl_type> expected

Format lists contain format specifiers that tell the compiler to replace a given specifier with the value or result given in the argument list that follows. A format list is analogous to a function parameter list in that the format specifier tells the compiler what type of argument to expect. For each format specifier, their must be a corresponding value or result in the argument list that follows. This value or result must also be of the same datatype.

NOTE: Format strings contain specifications that determine the output format for the arguments. The format argument consists of ordinary characters, escape sequences, and (if arguments follow format) format specifications Format Specifications always begin with a percent sign (%) and are read left to right. When the first format specification is encountered (if any), it converts the value of the first argument after format and outputs it accordingly. The second format specification causes the second argument to be converted and output, and so on.

The following are examples of this error:

FUNCTION MyFunc()

{

INTEGER x, intArr[100];

STRING str[100], strArr[100][100];

Print( “Hello World” ); // ok

Print( “My name is %s. My age is %d”, “David”, 33 ); // ok

Print( “My name is %s. My age is %d”, str, x ); // ok

MakeString( str, “Hello World” ); // ok

MakeString( str, “My name is %s. My age is %d”, str, x ); // ok

Print( “My name is %s. My age is %d”, “David” ); // error –

// %d format specifier does not have a

// corresponding value

Print( “My name is %s. My age is %d”, 33, “David” ); // error -

// both format specifiers contain corresponding

// values of different datatypes

SetArray( strArr, 1 ); // ok

SetArray( strArr, “abc” ); // ok

SetArray( intArr, 0 ); // ok

SetArray( “abc”, 1 ); // error – “abc” is not an array

SetArray( 1, “abc” ); // error – 1 is not an array

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1504.htm*
