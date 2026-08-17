# BUFFER_INPUT

Name:

BUFFER_INPUT

Syntax:

BUFFER_INPUT <var1[max_length]>[,<var2[max_length]>...];

BUFFER_INPUT <var[size][max_length]>;

BUFFER_INPUT<var[size[,<min>]][max_length]>;

BUFFER_INPUT <var1>[,[_SKIP_](<../Compiler_Directives/_SKIP_.htm>)][,<var2>...];

Description:

Routes serial inputs from the outside SIMPL program into a SIMPL+ program under the specified variable names. This is used when a serial string coming from a communications port needs to be processed by a SIMPL+ program. When new data comes in on a BUFFER_INPUT, the data is appended to the end of a BUFFER_INPUT. If the buffer is full, the contents are shifted up and the new data is appended to the end. This differs from STRING_INPUTs in that new data entering into a STRING_INPUT variable replaces the previous string contents. BUFFER_INPUTs may be processed with string handling functions. The GETC function may be used to read a character from the beginning of the buffer and shift the contents up by 1. Buffer inputs may be written to, so their data space may be used as a storage spot for doing something such as parsing through a string without declaring temporary storage. Refer to the discussion on fixed and variable arrays in [Declarations Overview.](<Declarations_Overview.htm>)

NOTE: BUFFER_INPUT variables may not be passed to functions in Version 3.00 for the 2-Series Control Systems. If you need to pass a BUFFER_INPUT variable to a function, assign it to a locally declared variable and pass that variable to the function.

MAX_LENGTH may be a value up to 255 in SIMPL+ Version 1.00. SIMPL+ Version 2.00 and later allow for MAX_LENGTH to be up to 65534. For an array of BUFFER_INPUTs, the maximum value of SIZE is 65535. Valid indices are 1 through the specified size.

NOTE: <min> is the number of inputs shown at a minimum, in SIMPL the default is 1. The user can expand the minimum up to the full size. Only the last array of a type can have a <min>.

NOTE: The [_SKIP_](<../Compiler_Directives/_SKIP_.htm>) keyword can be used in DIGITAL_INPUT, DIGITAL_OUTPUT, ANALOG_INPUT, ANALOG_OUTPUT, BUFFER_INPUT, STRING_INPUT and STRING_OUTPUT declarations.

Example:

BUFFER_INPUT FromComPort[100];

Signifies that a 100 character buffer with the name "FromComPort" is specified as a BUFFER_INPUT.

BUFFER_INPUT ComBuffers[2][100];

Signifies that two 100 character buffers have been set up that may be referenced with the names ComBuffers[1] through ComBuffers[2].

BUFFER_INPUT ComBuffers[2,2][100];

Same as above except both are always shown on the symbol.

Version:

X-Generation

SIMPL v1.20.01 and later

SIMPL v1.50.06 and later, allow BUFFER_INPUT arrays and MAX_LENGTH to be 65535.

2 Series:

SIMPL v2.03.18 and later, [Same as X Generation SIMPL v1.50.06, and allow Fixed size arrays and minimum sizes]

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Declarations/BUFFER_INPUT.htm*
