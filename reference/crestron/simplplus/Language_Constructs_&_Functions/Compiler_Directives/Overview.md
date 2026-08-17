# Compiler Directives Overview

Compiler directives are used by the SIMPL+ compiler to control attributes of the symbol without generating actual SIMPL+ code. They come at the beginning of the program, and are used to provide explicit instructions to the compiler. As such, directives are not part of the SIMPL+ language itself and are distinguished from actual SIMPL+ code by the pound sign (#) preceding their names.

Compiler directives are provided in the template file that is created when a new program is started. The compiler directives are as follows:

Directive |  Description  
---|---  
[#ANALOG_SERIAL_EXPAND](<_ANALOG_SERIAL_EXPAND.htm>) |  This provides a way to expand, or add, inputs and/or outputs for a specified symbol.  
[#BEGIN_PARAMETER_PROPERTIES, #END_PARAMETER_PROPERTIES](<PARAMETER_PROPERTIES.htm>) |  This directive is used to declare parameter properties.  
[#CATEGORY](<_CATEGORY.htm>) |  A Category is the name of the folder in the Logic Symbols library tree where the module is shown.  
[#CRESTRON_LIBRARY](<_CRESTRON_LIBRARY.htm>) |  Directs the compiler to include code from a Crestron provided library.  
[#CRESTRON_SIMPLSHARP_LIBRARY](<_CRESTRON_SIMPLSHARP_LIBRARY.htm>) |  Directs the compiler to include code from a Crestron SIMPL# library. The module name specified is the library filename without the CLZ extension.  
[#DEFAULT_NONVOLATILE](<_DEFAULT_NONVOLATILE.htm>) |  Program variables retain their value if hardware power is lost.  
[#DEFAULT_VOLATILE](<_DEFAULT_VOLATILE.htm>) |  Program variables will not retain their value if hardware power is lost.  
[#DEFINE_CONSTANT](<_DEFINE_CONSTANT.htm>) |  Define a <constant_value> that will be substituted anywhere in the current source file where <constant_name> is used.  
[#DIGITAL_EXPAND](<_DIGITAL_EXPAND.htm>) |  This provides a way to expand, or add, inputs and/or outputs for a specified symbol.  
[#ENABLE_STACK_CHECKING](<_ENABLE_STACK_CHECKING.htm>) |  Allows run-time stack checking to be performed on a given module. If there is a stack overflow, an error will be produced.  
[#ENABLE_TRACE](<_ENABLE_TRACE.htm>) |  When invoked, this enables trace output. If it is not invoked no console output will be generated.  
[#ENCODING_ASCII](<../Encoding/_ENCODING_ASCII.htm>) |  This directive ensures that any strings in the SIMPL+ module without explicit encoding keywords are marked with ASCII encoding.  
[#ENCODING_UTF16](<../Encoding/_ENCODING_UTF16.htm>) |  This directive will ensure that any strings in the SIMPL+ module without explicit encoding keywords are marked with UTF16 encoding.  
[#ENCODING_INHERIT_FROM_PARENT](<../Encoding/_ENCODING_INHERIT_FROM_PARENT.htm>) |  This directive will ensure that any strings in the SIMPL+ module without explicit encoding keywords are marked with default encoding of the parent of this module.  
[#ENCODING_INHERIT_FROM_PROGRAM](<../Encoding/_ENCODING_INHERIT_FROM_PROGRAM.htm>) |  This directive will ensure that any strings in the SIMPL+ module without explicit encoding keywords are marked with default encoding of the SIMPL program.  
[#HELP](<_HELP.htm>) |  Several #HELP lines can be specified.  
  
[#HELP_BEGIN … #HELP_END](<_HELP_BEGIN_…__HELP_END.htm>) |  The #HELP_BEGIN, #HELP_END pair makes it easier to create help since each line does not need a separate #HELP directive.  
[#HINT](<_HINT.htm>) |  The #HINT shows up in the status bar and provides a short tactical clue as to the function of the symbol in the same way that Crestron-defined built-in symbols do.  
[#IF_DEFINED … #ENDIF](<_IF_DEFINED_…__ENDIF.htm>) |  Results in compilation of the <code> only if <constant_name> has not been previously defined.  
[#IF_NOT_DEFINED … #ENDIF](<_IF_NOT_DEFINED_…__ENDIF.htm>) |  Results in compilation of the <code> only if <constant_name> has not been previously defined.  
[#IF_SERIES2](<../Encoding/_IF_SERIES2.htm>) |  Using this compiler directive will cause the compiler to only include the statements for the 2-series control system.  
[#IF_SERIES3](<../Encoding/_IF_SERIES3.htm>) |  Using this compiler directive will cause the compiler to only include the statements for the 3-series control system.  
[#IF_SERIES4](<../Encoding/_IF_SERIES4.htm>) |  Using this compiler directive will cause the compiler to only include the statements for the 4-series control system.  
[#INCLUDEPATH](<_INCLUDEPATH.htm>) |  Directs the compiler to search for User SIMPL+ and SIMPL# Libraries in the specified paths.  
[#LARGE_STACK](<_LARGE_STACK.htm>) |  This is used to increase the stack size when necessary.  
[#MAX_INTERNAL_BUFFER_SIZE](<_MAX_INTERNAL_BUFFER_SIZE.htm>) |  Sets the maximum size for the compiler’s internal string allocations.  
[#OUTPUT_SHIFT](<_OUTPUT_SHIFT.htm>) |  This provides a way to arrange the inputs and outputs on the symbol graphic so that they line up and are easy to read.  
[#PRINT_TO_TRACE](<_PRINT_TO_TRACE.htm>) |  When invoked, this enables converts all print statements to trace statements.  
[#SYMBOL_NAME](<_SYMBOL_NAME.htm>) |  By specifying <name of symbol>, this name will show up on the header of the symbol in the detail view as well as in the USER SIMPL+ section of the Symbol Library.  
[#USER_LIBRARY](<_USER_LIBRARY.htm>) |  Directs the compiler to include code from a User written library.  
[#USER_SIMPLSHARP_LIBRARY](<_USER_SIMPLSHARP_LIBRARY.htm>) |  Directs the compiler to include code from a User SIMPL# library. The module name specified is the library filename without the CLZ extension. Relative or absolute path are not allowed within this directive (see #INCLUDEPATH).

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Directives/Overview.htm*
