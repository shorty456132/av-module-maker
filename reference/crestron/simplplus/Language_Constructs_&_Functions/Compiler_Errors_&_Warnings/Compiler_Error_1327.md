# Compiler Error 1327

dconstruct error: Nonvolatile variables cannot be resized: <variable>

Variables that are declared as volatile are only allowed to be resized. Either the global compiler directive, #VOLATILE, or the declaration modifier, “VOLATILE”, may be used to declare a variable as volatile.

The following are examples of this error:

#DEFAULT_NONVOLATILE

integer intArr[10];

nonvolatile int2dArr[10][20];

nonvolatile string str[100];

volatile myIntArr[10];

volatile myStr[100];

function MyFunc()

{

ResizeArray( intArr, 100 ); // error – intArr is declared as nonvolatile by default;

ResizeArray( int2dArr, 15, 25 ); // error – int2dArr is nonvolatile

ResizeString( str, 200 ); // error – str is nonvolatile

ResizeArray( myIntArr, 20 ); // ok – myIntArr is volatile

ResizeString( myStr, 200 ); // ok – myStr is volatile

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1327.htm*
