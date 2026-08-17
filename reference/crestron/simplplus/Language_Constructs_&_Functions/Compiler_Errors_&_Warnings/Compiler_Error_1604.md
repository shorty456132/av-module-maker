# Compiler Error 1604

construct error: 'EVENT' already has a body

The EVENT statement can only be defined once per SIMPL+ module. A previously defined definition of EVENT was already encountered by the compiler.

The following are examples of this error:

EVENT // ok

{

}

EVENT // error – EVENT is already defined

{

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1604.htm*
