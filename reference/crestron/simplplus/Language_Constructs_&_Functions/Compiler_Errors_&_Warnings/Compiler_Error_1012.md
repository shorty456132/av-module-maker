# Compiler Error 1012

syntax error: Unterminated string constant

A literal string was used and was not contained within quotes. If a quotation character is needed within a literal string, a backslash should be placed before the quotation character (i.e.: \”). This will indicate to the compiler that the quotation character is not the terminating quote for the literal string.

The following are examples of this error:

FUNCTION MyFunc()

{

Print( "%s", "abc\"" ); // ok

Print( "%s", "abc\" ); // error - \" is not a closing quote

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1012.htm*
