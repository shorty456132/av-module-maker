# CompareStringsNoCase

Name:

CompareStringsNoCase

Syntax:

SIGNED_INTEGER CompareStringsNoCase(STRING string1, STRING string2);

Description:

Performs a case-insensitive comparison of string1 and string2. The strings are internally converted to uppercase before the comparison is done. The original strings passed into the function are not modified. The comparison is done in ASCII order. (e.g., the string "ABC" is less than "ABD" however the string "AbC" and "aBC" are the same, since the comparison is case insensitive).

Parameters:

STRING string1: First string to use in the comparison

STRING string2: Second string to use in the comparison

Return Value:

-1: indicates that string1 is less than string2 in ASCII order.

0: indicates that string1 is equal to string2 in ASCII order.

1: indicates that string1 greater than string2 in ASCII order.

Example:

STRING FirstString, SecondString;

SIGNED_INTEGER result;

FirstString = "Valuea";

SecondString = "Valueb";

result = CompareStringsNoCase(FirstString, SecondString);

Print("Result is %d.\n", result);

The strings are internally converted to "VALUEA" and "VALUEB". Since the first 5 characters are the same, the result comes down to comparing 'A' and 'B'. Since the ASCII value of 'A' (0x41) is less than the ASCII value of 'B' (0x42), the result is string1 < string2. The output of the function is –1, so the Print statement prints: "Result is –1."

Version:

SIMPL+ Version 3.03.00 or later

CUZ 3.137 or later required

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/CompareStringsNoCase.htm*
