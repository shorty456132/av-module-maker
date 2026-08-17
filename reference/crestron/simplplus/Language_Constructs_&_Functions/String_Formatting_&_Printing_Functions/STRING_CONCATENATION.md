# STRING CONCATENATION

String concatenation can be performed either using the + operator or by using MAKESTRING or PRINT functions. It is easier to use the + operator in general usage, although the formatting options of the MAKESTRING and PRINT functions give greater flexibility.

The + operator for strings is used the same way as in mathematical expressions. String concatenation may only be used as a standalone statement. The syntax is:

<Destination_string> = <String1 > [+ <String2> ...];

When string values appear on the right-side of the equal sign, the exact contents are appended to the new string. <String> values may be of type literal (quoted) strings, BUFFER_INPUT, STRING, STRING_INPUT, or any function that returns a string.

Examples:

INTEGER I;

INTEGER J; 

STRING A$[100], B$[100], C$[100];

B$="Hello";

C$="World!";

I=56;

J=2;

// This will output "Hello562xyzWorld!"

A$=B$+ITOA(I)+ITOA(J)+"xyz"+C$;

PRINT("%s", A$);

// This will output "8Hello2World"

A$=CHR(I)+B$+ITOA(J)+C$;

PRINT("%s", A$);

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Formatting_%26_Printing_Functions/STRING_CONCATENATION.htm*
