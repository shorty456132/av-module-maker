# Print

Name:

Print

Syntax:

PRINT(<Static Specification String> [, <arg1> ...]);

Description:

The output of PRINT goes to the CONSOLE of the control system and can be monitored in the Crestron Viewport. It can print simple text strings or complex formatted strings. (See also [TRACE](<TRACE.htm>))

Parameters:

<Static Specification String> is a quoted string that contains text and formatting information. Format specifiers are of the form:

%[[Pad]Width]specifier

Valid format specifiers are:

s: Specifies a BUFFER_INPUT, STRING, or STRING_INPUT variable (unprintable characters are printed in the format that Viewport uses).

d: Specifies an ANALOG_INPUT, ANALOG_OUTPUT, or INTEGER to be printed as a signed decimal value.

u: Specifies an ANALOG_INPUT, ANALOG_OUTPUT, or INTEGER to be printed as an unsigned decimal value.

x: Specifies an ANALOG_INPUT, ANALOG_OUTPUT, or INTEGER to be printed as a lowercase hexadecimal number.

X: Specifies an ANALOG_INPUT, ANALOG_OUTPUT, or INTEGER to be printed as an uppercase hexadecimal number.

l: Specifies a LONG_INTEGER or UNSIGNED_LONG_INTEGER will follow, and is followed by d, u, x, or X.

%: Prints a % sign (i.e. use %% to print a % sign).

%ld: Specifies a LONG_INTEGER to be printed as a signed decimal value.

%c: Specifies a printable ASCII character to be printed.

The optional Width specifier is a number that states the width of the field as characters. If the value to be printed is less than the Width, it is padded on the left with spaces for alpha-characters and zeros for numeric characters. (Width can be two digits).

The optional Pad specifier works with the Width specifier. If the result of the Width operation results in the need to add spaces, the Pad specifier can be used to pad with different values rather than a space. '0' is the only valid pad value, i.e., %03d pads with leading zeros so 1Z would be printed as 012.

As each % value is found, it pulls the matching <arg> off the list. The first % uses <arg1>, the second % uses <arg2>, etc. If the number of % specifiers does not match the number of arguments, the program will generate a compile error. The compiler also checks to make sure the format specifier matches the type of the variable being used (i.e. if %d is used, the variable being used should be INTEGER type).

NOTE: If no format specifiers are used, then a simple quoted text string is printed.

NOTE: The total string length that can be guaranteed to print is 256 characters.   
For example:

string a[500], b[500];

a = " { A STRING WITH 200 CHARACTERS } ";

b = " { A STRING WITH 56 CHARACTERS } ";

print("%s%s", a,b);

You would see all 256 characters.

If the total adds up to greater than 256 characters, it is possible that more may be seen, but only 256 is guaranteed. [MAKESTRING()](<MAKESTRING.htm>) does not have this limitation.

NOTE: Hex sequence characters within the format specifier will be translated into the equivalent ascii character before the format specifier is translated. For example, Print( "\x25%s", "abc" );, will NOT result in printing "%abc". The result will be "%s" since the compiler will translate the \x25 to the % character first (the Print statement will become Print( "%%s", "abc");)

In the <Static Specification String>, certain values may be printed using "escape sequences". Escape sequences start with the \ character and have a variable number of characters following. The following table specifies the legal escape sequences:

ESCAPE |  MEANING |  HEX CONSTANT  
---|---|---  
\n |  Carriage Return + Linefeed |  \x0D\0A  
\t |  Tab |  \x09  
\b |  Backspace |  \x08  
\r |  Carriage Return |  \x0D  
\f |  Form Feed |  \x0C  
\a |  Audible Alert (Bell) |  \x07  
\\\ |  Backslash |  \x5C  
\' |  Single Quote |  \x27  
\" |  Double Quote |  \x22  
\xZZ |  Hex Constant. Z can range from 0-9, a-f or A-F |  \xZZ  
  
Return Value:

None.

Example:

INTEGER X;

STRING Z[100];

X=10;

Z="Hello";

FUNCTION MAIN()

{

// Outputs "This is a string" followed by a CRLF.

PRINT("This is a string\n");

// Outputs "The value of X is 10 in decimal, 0A in hex"

// followed by CRLF.

PRINT("The value of X is %u in decimal, %02X in hex\n",

X, X);

// Outputs "The String value is Hello"

PRINT("The String value is %s", Z);

}

Version:

X Generation

SIMPL v1.20.01 and later

2-Series

SIMPL v2.01.05 and later, [Same as X Generation SIMPL v1.20.01], but allows %c format specifier.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Formatting_%26_Printing_Functions/PRINT.htm*
