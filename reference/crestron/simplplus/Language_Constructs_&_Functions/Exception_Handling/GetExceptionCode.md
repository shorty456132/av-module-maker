# GetExceptionCode

Name:

GetExceptionCode

Syntax:

GetExceptionCode

Description:

Exceptions caught within TRY-CATCH blocks can also be evaluated using the GetExceptionCode function. The code will either be [SPLUS_EXCEPTION_OUT_OF_RANGE](<Exception_Handling_Error_Codes.htm>) or [SPLUS_EXCEPTION_UNKNOWN](<Exception_Handling_Error_Codes.htm>).

Example:

Function MyFunc( INTEGER index )

{

INTEGER intArr[10];

TRY

{

intArr[index] = 1;

Print( "array index set" );

}

CATCH

{

Switch( GetExceptionCode() )

{

case (SPLUS_EXCEPTION_OUT_OF_RANGE):

{

}

case (SPLUS_EXCEPTION_UNKNOWN):

{

}

}

}

}

Version:

X Generation: Not Supported

2-Series: Not Supported

3-Series: v <> and above

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Exception_Handling/GetExceptionCode.htm*
