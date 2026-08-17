# Compiler Error 1002

syntax error: Missing '<token>'

A language element was expected and not found. The compiler expects certain language elements to appear before or after other elements. If any other language element is used, the compiler cannot understand the statement. Examples are missing parenthesis after a function call, missing semicolons after a statement and missing braces when defining functions.

NOTE: A token is a language element such as a keyword or operator. Anything that is not whitespace (i.e.: spaces, tabs, line feeds and comments) is a token.

  * Examine the last uncommented non-blank line or statement within the program. If a token was required in a previous statement and was not encountered, the compiler will continue onto the next line and mark the first token of the new statement as the error.




The following are examples of this error:

STRUCTURE MyStruct

{

INTEGER x;

STRING s[100];

}

MyStruct struct; // error – missing ‘;’ from preceding

// structure definition

INTEGER_FUNCTION MyFunc( INTEGER ) // error – argument variable

// not specified

INTEGER x; // error – ‘{’ missing before INTEGER

Print “abc”; // error – missing parenthesis

// should be Print (“abc” );

// printing…

Print “def” // error – error message will occur on

// next statement

// more printing…

Print “ghi”; // error – missing ‘;’from preceding Print

// statement

x = ((1+2) + 3; // error – unmatched set of parentheses

x = atoi( “abc”, 1 ); // error – atoi() does not take 2 arguments

if ( x = 4 )

return 5; // error – should be return (5);

return (6); // ok

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1002.htm*
