# Compiler Error 1609

construct error: Function can only be contained within Function Main

The function can only be used within the Function Main. The compiler encountered this function call outside of this function

The following are examples of this error:

DIGITAL_INPUT digIn;

PUSH digIn

{

WaitForInitializationComplete(); // error – not in Function Main

}

FUNCTION MyFunc()

{

WaitForInitializationComplete(); // error – not in Function Main

}

FUNCTION MyFunc()

{

if( WaitForInitializationComplete() < 0 ) // ok

{

print(Error waiting for initialization complete\n");

return;

}

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1609.htm*
