# _SKIP_

This allows a gap to be placed on the SIMPL+ symbol so chosen inputs and outputs can be made to line up visually. _SKIP_ can be used with parameters as well. This is a graphic consideration only and does not have an effect on the input and output relationships of the symbol.

NOTE: The _SKIP_ keyword can be used in DIGITAL_INPUT, DIGITAL_OUTPUT, ANALOG_INPUT, ANALOG_OUTPUT, BUFFER_INPUT, STRING_INPUT, STRING_OUTPUT, INTEGER_PARAMETER, LONG_INTEGER_PARAMETER, SIGNED_INTEGER_PARAMETER, SIGNED_LONG_INTEGER_PARAMETER and STRING_PARAMETER declarations.

Example:

DIGITAL_INPUT osc_in, _SKIP_, toggle_in;

ANALOG_OUTPUT an_level1, an_level2, _SKIP_, an_level3;

LONG_INTEGER_PARAMETER temp_level_min, _SKIP_, temp_level_max;

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Directives/_SKIP_.htm*
