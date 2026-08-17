# Compiler Error 1600

construct error: 'Function Main' cannot contain function parameters

'Function Main' cannot return a value

Function Main is the starting point of a SIMPL+ program. It is automatically called once when the system startup or is reset. Since this function is invoked by a method outside of the SIMPL+ module, no arguments can be included in it’s argument list and no value can be returned from it.

The following are examples of this error:

Function Main() // ok

{

}

INTEGER_FUNCTION Main() // error – Main() cannot return

// a value

{

}

Function Main( INTEGER cmdLineArg ) // error – Main() cannot contain

// a parameter list

{

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1600.htm*
