# Compiler Error 1316

construct error: Invalid Parameter Type: '<identifier>'. Expected Types: 'Decimal',

'Time', 'HexAddress', 'Percent', 'Constant'

String Parameters cannot contain a type: '<identifier>'

An invalid Parameter Type was specified within a parameter declaration. Parameter Types are optional when declaring parameter data types and can only be one of the following types: ‘Decimal’, ‘Time’, ‘HexAddress’, ‘Percent’ or ‘Constant’. String parameters cannot contain a parameter type.

The following are examples of this error:

INTEGER_PARAMETER intParam; // ok

INTEGER_PARAMETER intParam:Decimal; // ok

INTEGER_PARAMETER intParam:String; // error – String is not a valid parameter type

LONG_INTEGER_PARAMETER longIntParam:Time; // ok

SIGNED_INTEGER_PARAMETER signedIntParam; // ok

SIGNED_LONG_INTEGER_PARAMETER signedLongIntParam; // ok

STRING_PARAMETER strParam; // ok

STRING_PARAMETER strParam:Time; // error – STRING_PARAMETERS cannot // contain a paramter type

STRING_PARAMETER strParam:String; // error – String is not a valid

// parameter type

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1316.htm*
