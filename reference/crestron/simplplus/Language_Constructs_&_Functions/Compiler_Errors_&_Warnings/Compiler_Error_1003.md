# Compiler Error 1003

syntax error: Incorrect type '<decl_type>', expected type(s):

'<decl_type1[,decl_type2] [,decl_typen]>'

Incorrect type, expected type(s):

'<decl_type1[,decl_type2][,decl_typen]>'

A specific variable or type was expected and not found. Examples are variables of one type being used in place of another, and incorrect variable types within function arguments.

The following are examples of this error:

STRING_FUNCTION MyFunc( INTEGER x )

{ 

INTEGER y;

x = getc( y ); // error – y is not of type STRING

x = MyFunc( 1 ); // error – x cannot accept the resulting string

// returned from MyFunc()

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1003.htm*
