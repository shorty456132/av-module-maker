# Compiler Warning 1800

compiler warning: 'Return' statement will only terminate current

Wait statement's function scope

A ‘Return’ statement within a Wait Statement’s block of code will cause the Wait Statement to terminate. It will NOT terminate the current function that the Wait Statement resides within.

Wait Statements are similar to event functions (EVENT, PUSH, CHANGE, RELEASE) in that they execute in their own program thread. The control system can have many threads executing at the same time; each thread runs concurrent with one another.

The following are examples of this warning:

FUNCTION MyFunc( INTEGER x )

{

if ( x == 1 )

{

Wait( 500 )

{

return; // warning - this will terminate the

// Wait Statement. It will NOT

// terminate MyFunc()

}

}

else if ( x == 2 )

return; // this will terminate MyFunc()

x = x + 1;

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Warning_1800.htm*
