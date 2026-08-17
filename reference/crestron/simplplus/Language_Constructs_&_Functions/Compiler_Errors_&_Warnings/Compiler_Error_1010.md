# Compiler Error 1010

syntax error: Symbol Name contains illegal character: ';'

The compiler directive, #SYMBOL_NAME, cannot contain a semicolon as part of the symbol name.

The following are examples of this error:

#SYMBOL_NAME “MySymbol” // ok

#SYMBOL_NAME “My Symbol” // ok

#SYMBOL_NAME “MySymbol;YourSymbol” // error

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1010.htm*
