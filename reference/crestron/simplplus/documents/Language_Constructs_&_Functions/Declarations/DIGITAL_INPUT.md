# DIGITAL_INPUT  
  
Name:

DIGITAL_INPUT

Syntax:

DIGITAL_INPUT <var1>[,<var2>...];

DIGITAL_INPUT <var[size]>;

DIGITAL_INPUT <var[size[,min]]>;

DIGITAL_INPUT <var1>[,[_SKIP_](<../Compiler_Directives/_SKIP_.htm>)][,<var2>...];

Description:

Routes digital inputs from the outside SIMPL program into a SIMPL+ program under the specified variable names. DIGITAL_INPUT values are either 0 (digital low) or 1 (digital high). Refer to the discussion on fixed and variable arrays in [Declarations Overview.](<Declarations_Overview.htm>)

NOTE: DIGITAL_INPUT variables may not be passed to functions in Version 3.00 for the 2-Series Control Systems. If you need to pass a DIGITAL_INPUT variable to a function, assign it to a locally declared variable and pass that variable to the function.

For an array of DIGITAL_INPUTs, the maximum value of SIZE is 65535. Valid indices are 1 through the specified size.

NOTE: <min> is the number of inputs shown at a minimum, in SIMPL the default is 1. The user can expand the minimum up to the full size. Only the last array of a type can have a <min>.

NOTE: The [_SKIP_](<../Compiler_Directives/_SKIP_.htm>) keyword can be used in DIGITAL_INPUT, DIGITAL_OUTPUT, ANALOG_INPUT, ANALOG_OUTPUT, BUFFER_INPUT, STRING_INPUT and STRING_OUTPUT declarations.

Example:

DIGITAL_INPUT osc_in, toggle_in;

Signifies that two digital inputs are coming into the SIMPL+ program from the SIMPL Program.

DIGITAL_INPUT status_bits[8];

Signifies that eight digital inputs are coming into the SIMPL+ program from the SIMPL Program, referenced under the names status_bits[1] through status_bits[8].

DIGITAL_INPUT flags[8,2];

Signifies up to eight digital inputs, with at least two shown.

Version:

SIMPL+ Version 3.01 for fixed arrays and minimum sizes.

SIMPL+ Version 2.00 for DIGITAL_INPUT arrays.

SIMPL+ Version 1.00 for everything else.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Declarations/DIGITAL_INPUT.htm*
