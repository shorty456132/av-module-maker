# ANALOG_INPUT

Name:

ANALOG_INPUT

Syntax:

ANALOG_INPUT <var1>[,<var2>...];

ANALOG_INPUT <var[size]>;

ANALOG_INPUT <var[size[,<min>]]>

ANALOG_INPUT <var1>[,[_SKIP_](<../Compiler_Directives/_SKIP_.htm>)][,<var2>...];

Description:

Routes analog inputs from the outside SIMPL program into a SIMPL+ program under with the specified variable names. ANALOG_INPUT values are 16-bit numbers. They are treated as signed or unsigned values inside of a SIMPL+ program depending on the operators or functions being used. Refer to the discussion on fixed and variable arrays in [Declarations Overview.](<Declarations_Overview.htm>)

NOTE: ANALOG_INPUT variables may not be passed to functions in Version 3.00 for the 2-Series Control Systems. If you need to pass an ANALOG_INPUT variable to a function, assign it to a locally declared variable and pass that variable to the function.

For an array of ANALOG_INPUTs, the maximum value of SIZE is 65535. Valid indices are 1 through the specified size.

NOTE: <min> is the number of inputs shown at a minimum, in SIMPL the default is 1. The user can expand the minimum up to the full size. Only the last array of a type can have a <min>.

NOTE: The [_SKIP_](<../Compiler_Directives/_SKIP_.htm>) keyword can be used in DIGITAL_INPUT, DIGITAL_OUTPUT, ANALOG_INPUT, ANALOG_OUTPUT, BUFFER_INPUT, STRING_INPUT and STRING_OUTPUT declarations.

Example:

ANALOG_INPUT ramp1;

Signifies that one analog input is coming into the SIMPL+ program from the SIMPL Program.

ANALOG_INPUT light_levels[25];

Signifies that up to 25 analog inputs are coming into the SIMPL+ program from the SIMPL Program, referenced as light_levels[1] through light_levels[25]. One is shown as a minimum but the symbol input can be expanded by the user up to 25.

ANALOG_INPUT temp_set_pts[20,4];

Signifies that up to 20 analog inputs exist, referenced as temp_set_pts[1] through temp_set_pts[20]. Four are shown at a minimum, and the symbol inputs can be expanded by the user up to 20.

Version:

X Generation

SIMPL v1.20.01 and later

SIMPL v1.50.06 and later for ANALOG_INPUT arrays

2-Series

SIMPL v2.01.05 and later [Same features as X Generation SIMPL v1.50.06]

SIMPL v2.03.18 and later for fixed arrays and minimum sizes.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Declarations/ANALOG_INPUT.htm*
