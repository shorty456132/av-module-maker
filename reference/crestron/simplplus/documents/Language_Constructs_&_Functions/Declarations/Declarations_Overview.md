# Declarations Overview

Declarations control the name, type, and number of inputs and outputs on a SIMPL+ symbol. The name is shown as a cue on the symbol in SIMPL and is used as the variable name in the body of the SIMPL+ program. When the symbol is drawn in SIMPL, the inputs are shown in the order of DIGITAL_INPUTs, ANALOG_INPUTs, STRING_INPUTs. The outputs are shown in the order of DIGITAL_OUTPUTs, ANALOG_OUTPUTs, STRING_OUTPUTs. When specifying a declaration, several variable names can be put after a declaration or multiple declaration statements may be used.

For example:

ANALOG_INPUT val1, val2, val3;

is equivalent to

ANALOG_INPUT val1, val2;

ANALOG_INPUT val3;

Allowable I/O List Combinations:

SIMPL+ Version 2.00 and later gives the ability to define arrays in the Input/Output Lists. SIMPL+ version 3.01 and later introduced the ability to declare multiple fixed-size arrays in the input/output lists, and a minimum expanded size to variable-size arrays. The following are the allowable combinations:

  * Zero or more DIGITAL_INPUTs

  * Zero or more DIGITAL_INPUT arrays, the last is variable-size, the others are fixed-size.

  * Zero or more ANALOG_INPUTs, STRING_INPUTs, or BUFFER_INPUTs in any combination.

  * Zero or more ANALOG_INPUT, STRING_INPUT, or BUFFER_INPUT array, the last is variable-size, the others are fixed-size.

  * Zero or more DIGITAL_OUTPUTs

  * Zero or more DIGITAL_OUTPUT array, the last is variable-size, the others are fixed-size.

  * Zero or more ANALOG_OUTPUTs, STRING_OUTPUTs in any combination.

  * Zero or more ANALOG_OUTPUT or STRING_OUTPUT array, the last is variable-size, the others are fixed-size.




Fixed and Variable Size Arrays

Although SIMPL+ symbols can only handle one variable size DIGITAL_INPUT array, one variable-size DIGITAL_OUTPUT array, one variable-size ANALOG/STRING/BUFFER input array, and one variable size ANALOG/STRING/OUTPUT array, it is convenient to be able to refer to other inputs and outputs with array notation. Therefore, SIMPL+ allows an unlimited number of fixed-size input or output arrays, that are essentially single input or output values but array notation can be used. Every member of these fixed-size arrays is always shown in the symbol. All arrays, except the last one of each kind, are fixed-size arrays. The last one is variable-size, meaning that the symbol initially shows the first array value. The user can press ALT+ to expand the symbol to its maximum number of array inputs or outputs. In addition, a minimum size can be declared in all variable-size arrays, meaning that the minimum number of array members is always shown, not just the first one, and the array can be expanded from there.

NOTE: The minimum array size number must be from 1 to the size of the array. If a minimum array size is specified on any array, but it is the last one within any type, it will be a compile error.

Example:

DIGITAL_INPUT YesVotes[10]

DIGITAL_INPUT NoVotes[10]

DIGITAL_INPUT AbstainVotes[10,5];

The symbol will show 10 digital inputs labelled: YesVotes[1], YesVotes[2] ...YesVotes[10], followed by 10 more labelled: NoVotes[1], NoVotes[2] ...NoVotes[10], followed by 5 labelled: AbstainVotes[1], AbstainVotes[2] ...AbstainVotes[5]. You can continue to expand the last one up to AbstainVotes[10].

NOTE: SIMPL+ modules have at most two expandable lists of inputs and two expandable lists of outputs. The first expandable input list must contain the digital inputs. The second expandable list must contain the analogs, serials, and buffered inputs. The same goes for the outputs. Within each list, all of the fixed (non-array ) inputs or outputs come first, followed by at most one array which is expandable.

Predefined Names:

The names "on" and "off" are reserved. Assigning "on" to a variable sets the variable to 1, assigning "off" sets that variable to 0.

The following shows equivalent, given that VALUE is a DIGITAL_OUTPUT:

VALUE = 1; and VALUE = on;

VALUE = 0; and VALUE = off;

The current available declarations are listed below:

[ANALOG_INPUT](<ANALOG_INPUT.htm>)

[ANALOG_OUTPUT](<ANALOG_OUTPUT.htm>)

[ASCII](<../Encoding/ASCII.htm>)

[BUFFER_INPUT](<BUFFER_INPUT.htm>)

[DIGITAL_INPUT](<DIGITAL_INPUT.htm>)

[DIGITAL_OUTPUT](<DIGITAL_OUTPUT.htm>)

[INHERIT](<../Encoding/Inherit.htm>)

[INTEGER](<INTEGER.htm>)

[LONG_INTEGER](<LONG_INTEGER.htm>)

[VOLATILE](<VOLATILE.htm>)

[NONVOLATILE](<NONVOLATILE.htm>)

[SIGNED_INTEGER](<SIGNED_INTEGER.htm>)

[SIGNED_LONG_INTEGER](<SIGNED_LONG_INTEGER.htm>)

[STRING](<STRING.htm>)

[STRING_INPUT](<STRING_INPUT.htm>)

[STRING_OUTPUT](<STRING_OUTPUT.htm>)

[STRUCTURES](<STRUCTURES.htm>)

[UTF16](<../Encoding/UTF16.htm>)

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Declarations/Declarations_Overview.htm*
