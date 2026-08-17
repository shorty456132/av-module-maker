# Compiler Error 1328

declaration error: Encoding Types are only valid for STRING declarations

Encoding only applies to strings. The declaration modifiers, ASCII, UTF16 and INHERIT can only be used with variables of type STRING.

The following are examples of this error:

ASCII string str[100]; // ok – str is of type ‘string’

UTF16 integer myIntArr[10]; // error – myIntArr is of type ‘integer’

INHERIT string myStr[100]; // ok – myStr is of type ‘string’

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1328.htm*
