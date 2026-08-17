# GetExceptionMessage

Name:

GetExceptionMessage

Syntax:

GetExceptionMessage

Description:

Exceptions caught within TRY-CATCH blocks can also be evaluated using the GetExceptionMessage function. The message will contain a description of the error thrown.

Example:

Function MyFunc( INTEGER index )

{

INTEGER intArr[10];

TRY

{

intArr[index] = 1;

Print( “array index set” );

}

CATCH

{

Print( “Exception thrown: %s”, GetExceptionMessage() }

}

}

Version:

X Generation: Not Supported

2-Series: Not Supported

3-Series: v <> and above

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Exception_Handling/GetExceptionMessage.htm*
