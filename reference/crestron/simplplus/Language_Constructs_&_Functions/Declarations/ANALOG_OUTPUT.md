# ANALOG_OUTPUT

Name:

ANALOG_OUTPUT

Syntax:

ANALOG_OUTPUT <var1>[,<var2>...];

ANALOG_OUTPUT <var[size]>;

ANALOG_OUTPUT<var[size[,<min>]]>;

ANALOG_OUTPUT <var1>[,[_SKIP_](<../Compiler_Directives/_SKIP_.htm>)][,<var2>...];

Description:

Routes a value from the SIMPL+ program to the SIMPL program as an analog value. ANALOG_OUTPUT values are 16-bit numbers. They are treated as signed or unsigned values inside of a SIMPL+ program depending on the operators or functions being used. Refer to the discussion on fixed and variable arrays in [Declarations Overview.](<Declarations_Overview.htm>)

NOTE: ANALOG_OUTPUTs may be jammed with other analog values from a SIMPL program (i.e., from a RAMP or other analog logic, even other SIMPL+ symbols). When such an output is jammed, the new value is read back into the SIMPL+ symbol and the value of the output is altered.

In X-Generation Control Systems, the logic process only sees the last analog that was posted after the SIMPL+ module tasks switched away. Therefore, in a loop that iterates from 1 to 10000, only a few of the values will be seen by the logic process. If all values should be seen by the logic process, a PROCESSLOGIC statement is required after the assignment to the ANALOG_OUTPUT.

When the SIMPL+ program writes to the ANALOG_OUTPUT, the new value is posted immediately. Therefore, if the value is read back after being assigned, the new value is read back (unlike a DIGITAL_OUTPUT on X-Generation control systems).

In the 2-Series Control Systems, the logic process sees ALL values that are assigned to the ANALOG_OUTPUT. No PROCESSLOGIC is required.

For an array of ANALOG_OUTPUTs, the maximum value of SIZE is 65535. Valid indices are 1 through the specified size.

NOTE: <min> is the number of outputs shown at a minimum, in SIMPL the default is 1. The user can expand the minimum up to the full size. Only the last array of a type can have a <min>.

NOTE: The [_SKIP_](<../Compiler_Directives/_SKIP_.htm>) keyword can be used in DIGITAL_INPUT, DIGITAL_OUTPUT, ANALOG_INPUT, ANALOG_OUTPUT, BUFFER_INPUT, STRING_INPUT and STRING_OUTPUT declarations.

Example:

ANALOG_OUTPUT LEVEL;

Signifies that one analog output is being sent from the SIMPL+ program to the SIMPL program.

ANALOG_OUTPUT LEVELS[25];

Signifies that up to 25 analog outputs, referenced as LEVELS[1] through LEVELS[25] are being sent from the SIMPL+ program to the SIMPL program.

ANALOG_OUTPUT LEVELS[25,5];

Signifies same as above, except that a minimum of 5 are shown at any time.

NOTE: If LEVEL or any of the elements from LEVELS is jammed from outside the symbol, it will take on that new jammed value.

NOTE: You should use [isSignalDefined](<../System_Interfacing/IsSignalDefined.htm>) to test whether the output is connected to an actual signal in the SIMPL program before assigning a value to it. If you assign a value and there is no signal, a message is placed in the system error log.

Version:

X-Generation

SIMPL v1.20.01 and later

SIMPL v1.50.06 and later, support for ANALOG_OUTPUT arrays

2-Series

SIMPL v2.01.05 and later [Same support as X Generation SIMPL v1.50.06, however, ANALOG_OUTPUTs or ANALOG_OUTPUT Arrays cannot be passed by reference]

SIMPL v2.03.18 and later, Fixed size arrays and minimum sizes.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Declarations/ANALOG_OUTPUT.htm*
