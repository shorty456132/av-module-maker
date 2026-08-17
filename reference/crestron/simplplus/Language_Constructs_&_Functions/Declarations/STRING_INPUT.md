# STRING_INPUT

Name:

STRING_INPUT

Syntax:

STRING_INPUT <var1[max_size1]>[,<var2[max_size2]>...];

STRING_INPUT <var[size][max_size]>;

STRING_INPUT <var[size[,<min>]][max_size]>;

STRING_INPUT <var1>[,[_SKIP_](<../Compiler_Directives/_SKIP_.htm>)][,<var2>...];

Description:

Routes serial inputs from the outside SIMPL program into a SIMPL+ program under the specified variable names. Strings are of arbitrary length, so a maximum size must be specified. Upon receiving new data, the value is cleared and the new string is put in. Strings received greater than the specified size are truncated to the size in the declaration. String inputs may be written to, so their data space may be used as a storage spot for doing something such as parsing through a string without declaring temporary storage. Refer to the discussion on fixed and variable arrays in [Declarations Overview.](<Declarations_Overview.htm>)

NOTE: STRING_INPUT variables may not be passed to functions in Version 3.00 for the 2-Series Control Systems. If you need to pass a STRING_INPUT variable to a function, assign it to a locally declared variable and pass that variable to the function.

The value of SIZE and NUM_CHARACTER may be up to 255 in SIMPL+ Version 1.00. In SIMPL+ Version 2.00 and later, they may be up to 65535. For an array of STRING_INPUTs, the maximum value of SIZE is 65535.

NOTE: <min> is the number of inputs shown at a minimum, in SIMPL the default is 1. The user can expand the minimum up to the full size. Only the last array of a type can have a <min>.

NOTE: The [_SKIP_](<../Compiler_Directives/_SKIP_.htm>) keyword can be used in DIGITAL_INPUT, DIGITAL_OUTPUT, ANALOG_INPUT, ANALOG_OUTPUT, BUFFER_INPUT, STRING_INPUT and STRING_OUTPUT declarations.

Example:

STRING_INPUT FirstName[100], SecondName[25];

Signifies that two serial inputs are coming into the SIMPL+ program from the SIMPL Program. The first one may only be a maximum of 100 characters, the second may only be a maximum of 25 characters. If an input is longer than the specified length, everything after the specified limit is lost.

STRING_INPUT DataBaseNames[9][100];

Signifies that 9 serial inputs are coming into the SIMPL+ program from the SIMPL program. Each name has a 100 character limit. The names are referenced as DataBaseNames[1] through DataBaseNames[9].

STRING_INPUT Database Names [9,3][100];

Same as above except at least three are shown at all times

Version:

X Generation

SIMPL v1.20.01 and later

SIMPL v1.50.06 and later, STRING_INPUT arrays and SIZE, NUM_CHARACTER to 65534.

2-Series

SIMPL v2.01.05 and later, [Same as X Generation SIMPL v1.50.06]

SIMPL v2.03.18 and later, for fixed arrays and minimum sizes.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Declarations/STRING_INPUT.htm*
