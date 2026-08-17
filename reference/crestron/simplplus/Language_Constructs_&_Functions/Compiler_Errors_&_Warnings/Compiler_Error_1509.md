# Compiler Error 1509

**function argument error: Class variable name expected: '<variable>'**

A valid class name was expected for a function argument and was not found.

The following are examples of this error:

MyClass class1; // MyClass is defined within a SIMPL# Library

// ok – class1 is defined

RegisterEvent( class1, mySimplSharpEvent, mySPlusEventHandler );

// error – someclass is not defined

RegisterDelegate( someclass, myDelegateProp, myDelegateCallbackFn );

// error – only valid variables are allowed

RegisterEvent( “event”, mySimplSharpEvent, mySPlusEventHandler );

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1509.htm*
