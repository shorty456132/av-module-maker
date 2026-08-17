# STRING

Name:

STRING

Syntax:

STRING <var1[size1]>[,<var2[size2]>...];

STRING <var1[num_elements1][num_characters1]>[,

<var2[num_elements2][num_characters2]>...];

Description:

Declares a string that is local to this SIMPL+ program. Strings are of arbitrary length, so a maximum size must be specified. When a STRING variable has new data assigned to it, the old data is lost.

NOTE: Strings in Version 3.00 for the 2-Series Control Systems may not be passed by value to a function. They must be passed by reference.

NOTE: If no Return Value is specified within an String_Function, then an empty string will be returned by default.

When used in its second form, a one-dimensional array of strings is allocated. The array has num_elements+1 elements, and num_characters per element allocated. The legal indices for referencing the strings are 0 through num_elements.

The value of SIZE and NUM_CHARACTER may be up to 255 in SIMPL+ Version 1.00. In SIMPL+ Version 2.00 and later, they may be up to 65534. The value of NUM_ELEMENTS may be up to 65535.

NOTE: (X-Gen) The values of STRINGs declared are non-volatile. If the system is powered down and up, the variables will take on their previous values. If programs are changed and uploaded, the values are not preserved.

NOTE: (2-Series) STRINGs can be volatile or non-volatile. The default is defined using the compiler directives #DEFAULT_NONVOLATILE or #DEFAULT_VOLATILE or overriden using the nonvolatile or volatile keywords.

Example:

STRING temp$[10];

Signifies that one local STRING is declared in this SIMPL+ program.

STRING temp$[2][10];

Signifies that three strings of 10 characters long have been allocated.

To assign values, the following would be legal:

temp$[0]="Val1";

temp$[1]="Val2";

temp$[2]="Val3";

Version:

X Generation

SIMPL v1.20.01 and later

SIMPL v1.50.06 and later, SIZE and NUM_CHARACTER up to 65534.

2-Series

SIMPL v2.01.05 and later, [Same as X Generation SIMPL v1.50.06]

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Declarations/STRING.htm*
