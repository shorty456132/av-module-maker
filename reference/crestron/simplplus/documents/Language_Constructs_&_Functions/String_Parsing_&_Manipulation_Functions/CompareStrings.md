# CompareStrings

Name:

CompareStrings

Syntax:

SIGNED_INTEGER CompareStrings(STRING string1, STRING string2);

Description:

Performs a case-sensitive comparison of string1 and string2. This function can be used in place of the "=", "<", ">", "<>" operators. The comparison is done in ASCII order (e.g., the string "ABC" is less than "ABD" and the string "abc" is greater than "ABC" since the character 'a' comes after 'A' in the ASCII table).

Parameters:

STRING string1: First string to use in the comparison

STRING string2: Second string to use in the comparison

Return Value:

< 0: indicates that string1 is less than string2 in ASCII order.

0: indicates that string1 is equal to string2 in ASCII order.

> 0: indicates that string1 is greater than string2 in ASCII order.

Example:

STRING FirstString, SecondString;

SIGNED_INTEGER result;

FirstString = "ValueA";

SecondString = "Valueb";

result = CompareStrings(FirstString, SecondString);

Print("Result is %d.\n", result);

Since the first 5 characters are the same, the result comes down to comparing 'A' and 'b'. Since the ASCII value of 'b' (0x62) is greater than the ASCII value of 'A' (0x41), the result is string1 > string2. The output of the function is –1, so the Print statement prints: "Result is 1."

Version:

SIMPL+ Version 3.03.00 or later

CUZ 3.137 or later required

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/CompareStrings.htm*
