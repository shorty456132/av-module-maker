# MakeString

Name:

MakeString

Syntax:

MakeString(STRING DESTINATION, <Static Specification

String> [, <arg1> ...]);

MakeString(0 | 1 | 2, <Static Specification String> [,

<arg1> ...]);

Description:

MAKESTRING is a variant of [PRINT](<PRINT.htm>). The output of MAKESTRING goes to the DESTINATION string. It can print simple text strings or complex formatted strings. The second form of MAKESTRING allows different destinations to be selected:

0: Console Port, same as PRINT.

1: CPU (same functionality as SendPacketToCPU function)

2: Cresnet Network (same functionality as SendCresnetPacket function).

NOTE: In the second form, the first argument may not be a variable containing 0, 1, 2. It must be the written as 0, 1, 2. Crestron is discouraging the use of the second form of MAKESTRING in favor of either the PRINT command or alternate methods for activating devices that do not require knowledge of Cresnet packets, which are subject to change.

Parameters:

DESTINATION is a string where the output goes to after it has been formatted and processed. For a further description of formatting, refer to [PRINT](<PRINT.htm>).

Return Value:

None.

Example:

INTEGER X;

STRING Z[100], OUT[100];

X=10;

Z="Hello";

FUNCTION MAIN()

{

// Puts "This is a string" followed by a CRLF onto OUT.

MAKESTRING(OUT, "This is string\n");

// Puts "The value of X is 10 in decimal, 0A in hex"

// followed by CRLF onto OUT.

MAKESTRING(OUT, "The value of X is %u in decimal, %02X in

hex\n", X, X);

// Puts "The String value is Hello" onto OUT.

MAKESTRING(OUT, "The String value is %s", Z);

}

Version:

X Generation

SIMPL v1.20.01 and later

SIMPL v1.50.06 and later, adds Console, Cresnet, and CPU destinations.

2-Series

SIMPL v2.01.05 and later, [Same as X Generation SIMPL v1.50.06], but allows %c format specifier.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Formatting_%26_Printing_Functions/MAKESTRING.htm*
