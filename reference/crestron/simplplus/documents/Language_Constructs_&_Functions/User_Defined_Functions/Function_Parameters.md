# Function Parameters

NOTE: Passing [STRINGs](<../Declarations/STRING.htm>) with [BYVAL and BYREF](<ByRef%2c_ByVal%2c_ReadOnlyByRef.htm>) is not allowed in the 2-Series Control System. All STRINGs are passed by referenced in the 2-Series Control System.

NOTE: Passing I/O datatype variables ([DIGITAL_INPUT](<../Declarations/DIGITAL_INPUT.htm>), [ANALOG_INPUT](<../Declarations/ANALOG_INPUT.htm>) and [STRING_INPUT](<../Declarations/STRING_INPUT.htm>)) is not allowed in the 2-Series Control System.

Functions may contain a list of parameters that are passed by the caller. Typically, data is passed to a function in order to make the code readable, maintainable, and less prone to bugs. SIMPL+ Version 1.00 did not allow data to be passed to functions. The only way to get data into functions was to declare global variables and have the functions reference the global variables.

The function argument list contains a comma separated list of arguments. The arguments are of the form:

[ByRef | ByVal] <INTEGER | LONG_INTEGER | SIGNED_INTEGER | SIGNED_LONG_INTEGER | STRUCTURE> <variable_name>

[ByRef and ByVal](<ByRef%2c_ByVal%2c_ReadOnlyByRef.htm>) are keywords telling the system the read/write permissions and local behavior for the variable in the function.

[INTEGER](<../Declarations/INTEGER.htm>), [STRING](<../Declarations/STRING.htm>) or [STRUCTURE](<../Declarations/STRUCTURES.htm>) tells the function the<variable_name> type. [BUFFER_INPUT](<../Declarations/BUFFER_INPUT.htm>), [STRING_INPUT](<../Declarations/STRING_INPUT.htm>), [STRING_OUTPUT](<../Declarations/STRING_OUTPUT.htm>), and STRING declarations are passed into a function using the STRING type. All other types are passed using the INTEGER type.

The function refers to the passed variable as <variable_name>. Note that for a one-dimensional array, the syntax is <variable_name>[] and for a two-dimensional array the syntax is <variable_name>[][].

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/User_Defined_Functions/Function_Parameters.htm*
