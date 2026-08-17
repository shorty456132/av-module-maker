# Compiler Error 1401

assignment error: Variable cannot be used for assignment: '<identifier>'

Function arguments that have been declared as ReadOnlyByRef can only have their values read; values cannot be assigned to them. 

The following are examples of this error:

FUNCTION MyFunc( INTEGER x, ReadOnlyByRef INTEGER y )

{

x = 5; // ok

x = y; // ok – the value of y can be read

y = 6; // error – y is read-only

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1401.htm*
