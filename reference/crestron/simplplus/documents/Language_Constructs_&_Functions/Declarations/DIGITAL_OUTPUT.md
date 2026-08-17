# DIGITAL_OUTPUT

Name:

DIGITAL_OUTPUT

Syntax:

DIGITAL_OUTPUT <var1>[,<var2>...];

DIGITAL_OUTPUT <var[size]>;

DIGITAL_OUTPUT <var[size[,<min>]]>;

DIGITAL_OUTPUT <var1>[,[_SKIP_](<../Compiler_Directives/_SKIP_.htm>)][,<var2>...];

Description:

Routes a value from the SIMPL+ program to a SIMPL program. If a value different from 0 is placed on a DIGITAL_OUTPUT, the digital signal in the SIMPL program is set high when the control system processes the logic. Refer to the discussion on fixed and variable arrays in [Declarations Overview.](<Declarations_Overview.htm>)

NOTE: DIGITAL_OUTPUTs may be jammed with other digital values from a SIMPL program (i.e., from a BUFFER or other jammable digital logic, even other SIMPL+ symbols). When such an output is jammed, the new value is read back into the SIMPL+ symbol and the value of the output is altered.

NOTE: You should use [isSignalDefined](<../System_Interfacing/IsSignalDefined.htm>) to test whether the output is connected to an actual signal in the SIMPL program before assigning a value to it. If you assign a value and there is no signal, a message is placed in the system error log.

In X-Generation Control Systems, if a new value is assigned to the DIGITAL_OUTPUT from the SIMPL+ program, the value read back from it within the SIMPL+ program will have the original state until the logic is serviced. For example, if a DIGITAL_OUTPUT has a value of 0, and the value 1 is written to it, the value read back will be 0 until the system processes the rest of the logic attached to that SIMPL+ symbol. This is unlike an ANALOG_OUTPUT. If every change of a DIGITAL_OUTPUT is required to be seen by the logic, a PROCESSLOGIC statement is required after the assignment to the DIGITAL_OUTPUT.

In the 2-Series Control Systems, the logic process sees ALL values that are assigned to the DIGITAL_OUTPUT. No PROCESSLOGIC is required. As an example, if the following code is used in the 2-Series Control Systems:

DIGITAL_OUTPUT State1;

State1=1;

State1=0;

The logic will end up seeing a short pulse.

For an array of DIGITAL_OUTPUTs, the maximum value of SIZE is 65535. Valid indices are 1 through the specified size.

NOTE: <min> is the number of outputs shown at a minimum, in SIMPL the default is 1. The user can expand the minimum up to the full size. Only the last array of a type can have a <min>.

NOTE: The [_SKIP_](<../Compiler_Directives/_SKIP_.htm>) keyword can be used in DIGITAL_INPUT, DIGITAL_OUTPUT, ANALOG_INPUT, ANALOG_OUTPUT, BUFFER_INPUT, STRING_INPUT and STRING_OUTPUT declarations.

Example:

DIGITAL_OUTPUT State1, State2;

Signifies that two digital signals are to be sent to a SIMPL program from this SIMPL+ program.

NOTE: For example, if State1 is jammed high via a BUFFER from outside the SIMPL+ program, the value of State1 becomes 1 and should be handled accordingly in the SIMPL+ code.

DIGITAL_OUTPUT state_bits[3];

Signifies that up to three digital signals are to be sent to a SIMPL program from this SIMPL+ program. The names are referenced as state_bits[1] through state_bits[3]. The same jamming rules apply as in the previous example.

DIGITAL_OUTPUT state_bits[3,3];

Same as above except all three are always shown on the symbol.

Version:

X-Generation

SIMPL v1.20.01 and later

SIMPL v1.50.06 and later, support for DIGITAL_OUTPUT arrays

2-Series

SIMPL v2.01.05 and later [Same support as X Generation SIMPL Winodws v1.50.06, however, DIGITAL_OUTPUTs or DIGITAL_OUTPUT Arrays cannot be passed by reference]

SIMPL v2.03.18 and later, Fixed size arrays and minimum sizes.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Declarations/DIGITAL_OUTPUT.htm*
