# Numeric Formats

Numeric (Integer) constants may be expressed in three formats; decimal, hexadecimal, or quoted character.

Decimal constants are specified by writing a decimal number. Hexadecimal constants are specified by prefacing the hex constant by 0x. Quoted character constants are a single character placed between single quotes (') and have the numeric value specified on an ASCII chart.

Examples:

INTEGER I;

I=123; // Specify Decimal constant.

I=0xABC; // Specify a Hexadecimal constant (Decimal value 2748)

I='A'; // Specify a character constant (Decimal value 65)

INTEGER K;

K=54; // Specify Decimal constant

K=0x36; // Specify a Hexadecimal Constant (Decimal

// Value 54)

K='6'; // All three of these are the same value

// (Decimal value 54)

The three forms may be used interchangeably and are used to make code more readable.

Example:

STRING A$[10], B$[10], C$[10];

INTEGER I;

BUFFER_INPUT COM_IN$[50];

// A$, B$, and C$ contain identical values

// after these lines run.

A$=CHR('A');

B$=CHR(65);

C$=CHR(0x41);

// Preserve the lower nibble of a word, mask the rest out.

I = VAL1 & 0x000F;

// Read until a comma is detected in the stream.

DO

{

I = GetC(COM_IN$)

}

UNTIL (I = ',');

---
*Source: https://help.crestron.com/simpl_plus/Content/Operators/Numeric_Formats.htm*
