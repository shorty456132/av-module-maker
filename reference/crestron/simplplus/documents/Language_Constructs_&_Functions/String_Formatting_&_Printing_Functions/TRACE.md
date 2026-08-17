# TRACE

Name:

Trace

Syntax:

TRACE(<Static Specification String> [, <arg1> ...]);

Description:

The output of TRACE goes to the CONSOLE of the control system and can be monitored in the Trace window in the Crestron Toolbox SIMPL Debugger and in Crestron Viewport. It can display simple text strings or complex formatted strings.

NOTE: PRINT() and TRACE() are equivalent, with the exception that TRACE prepends the hex characters \xFA\xE0, and suffixes the string with \xFB - and with the exception of how the compiler directives #ENABLE_TRACE and #PRINT_TO_TRACE deal with the print() and trace() statements.

See also [Print](<PRINT.htm>) and [#ENABLE_TRACE](<../Compiler_Directives/_ENABLE_TRACE.htm>) and [#PRINT_TO_TRACE](<../Compiler_Directives/_PRINT_TO_TRACE.htm>) for more information.

Version:

2-Series

SIMPL v2.10.09 and later, [Same as X Generation SIMPL v1.20.01], but allows %c format specifier.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Formatting_%26_Printing_Functions/TRACE.htm*
