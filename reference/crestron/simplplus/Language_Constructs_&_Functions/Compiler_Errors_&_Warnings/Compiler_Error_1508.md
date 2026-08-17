# Compiler Error 1508

function argument error: Variable cannot be passed to read file functions: '%1': '<identifier>'

Read file functions (ReadInteger, ReadString, etc.) can only contain variables that can be written to for the function’s resulting read buffer.

The following are examples of this error:

DIGITAL_OUTPUT digOut;

STRING_OUTPUT strOut;

INTEGER_PARAMETER intParam;

FUNCTION MyFunc( SIGNED_INTEGER nHandle )

{

STRING str[100];

INTEGER x;

ReadInteger( nHandle, x ); // ok

ReadString( nHandle, str ); // ok

ReadInteger( nHandle, digOut ); // error

ReadString( nHandle, strOut ); // error

ReadString( nHandle, intParam ); // error

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1508.htm*
