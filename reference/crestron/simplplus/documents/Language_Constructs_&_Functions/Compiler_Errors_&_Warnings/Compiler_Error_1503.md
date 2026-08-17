# Compiler Error 1503

function argument error: Input or Output signal expected: '<identifier>'

The expected identifier must be of an Input or Output signal datatype (i.e.: DIGITAL_INPUT, ANALOG_OUTPUT, STRING_INPUT, etc.).

The following are examples of this error:

DIGITAL_INPUT digIn, digInArr[10];

DIGITAL_INPUT digIn;

ANALOG_INPUT anlgIn;

ANALOG_OUTPUT anlgOut;

STRING_INPUT strIn[100];

STRING_OUTPUT strOut;

BUFFER_INPUT buffIn[100];

INTEGER i;

STRING str[100];

FUNCTION MyFunc()

{

i = IsSignalDefined( digIn ); // ok

i = IsSignalDefined( digInArr[5] ); // ok

i = IsSignalDefined( digOut ); // ok

i = IsSignalDefined( anlgIn ); // ok

i = IsSignalDefined( anlgOut ); // ok

i = IsSignalDefined( strIn ); // ok

i = IsSignalDefined( strOut ); // ok

i = IsSignalDefined( buffIn ); // ok

digOut = IsSignalDefined( i ); // error – ‘i’ is not an Input

// or Output signal

i = IsSignalDefined( str ); // error – ‘i’ is not an Input

// or Output signal

digOut = IsSignalDefined( 5 ); // error – ‘5’ is not an Input

// or Output signal

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1503.htm*
