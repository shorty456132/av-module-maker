# Compiler Error 1616

**construct error: Callback function missing or has an unmatched argument list: **

**‘ <splus_callback_function>’**

When registering delegates, the callback function specified must be valid and exist within the SIMPL+ module. The delegate callback function’s signature must match the signature within the SIMPL# Library.

The following are examples of this error:

// SimplSharpLibrary.clz

public delegate int DelegateIntFn(int value);

SPlusModule.usp

// UserModule.usp

#USER_SIMPLSHARP_LIBRARY "SimplSharpLibrary"

MyClass class1; // MyClass is defined within a SIMPL# Library

callback signed_long_integer_function MyIntDelegateCallbackFn(

signed_long_integer value )

callback string_function MyStringDelegateCallbackFn()

{

return (0);

}

// ok – MyIntDelegateCallbackFn is defined and has a matching signature

RegisterDelegate( class1, myDelegateFn, MyIntDelegateCallbackFn);

// error – MyStringDelegateCallbackFn is defined, but does not have a

matching signature

RegisterDelegate( class1, myDelegateFn, MyStringDelegateCallbackFn);

// error – someDelegateCallbackFn is not defined

RegisterDelegate( class1, myDelegateFn, someDelegateCallbackFn);

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1616.htm*
