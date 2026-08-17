# Compiler Error 1615

construct error: GetExceptionMessage/GetExceptionCode can only be used within a CATCH statement block

The functions, GetExcpetionMessage and GetExceptionCode can only be used within the CATCH portion of a TRY-CATCH statement block. It cannot be used inside any other type of statement block or event handler.

The following are examples of this error:

Function MyFunc()

{

string str[100];

integer result;

TRY

{

// some code…

}

CATCH

{

str = GetExceptionMessage(); // ok – GetExceptionMessage is within the CATCH block.

}

result = GetExceptionCode(); // error – GetExceptionCode is outside of the CATCH block.

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1615.htm*
