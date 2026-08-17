# Compiler Error 1510

**function argument error: Class event handler expected: '<variable>'**

**A** valid class event handler was expected for a function argument and was not found.

The following are examples of this error:

MyClass class1; // MyClass is defined within a SIMPL# Library

// ok – class1 is defined

RegisterEvent( class1, mySimplSharpEvent, mySPlusEventHandler );

// error – someSimplSharpEvent is not defined within SIMPL# Library

RegisterEvent( class1, someSimplSharpEvent, mySPlusEventHandler);

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1510.htm*
