# GetNumArrayCols

Name:

GetNumArrayCols

Syntax:

INTEGER GetNumArrayCols(STRING | INTEGER

Description:

Finds the number of columns in a two-dimensional array or the size of the array for a one-dimensional array.

Parameters:

ARRAY_NAME is the array as determined by the size.

Return Value:

For the data types in the table after this paragraph, the return value of GetNumArrayCols is shown.

DATA TYPE |  RETURN VALUE  
---|---  
ANALOG INPUT X [size] |  Size  
ANALOG INPUT X [size] |  Size  
DIGITAL INPUT X [size] |  Size  
DIGITAL OUTPUT X [size] |  Size  
STRING INPUT X [size] |  Chars  
STRING INPUT X [size] [chars] |  Chars  
STRING OUTPUT X [size] |  Size  
STRING X [chars] |  Chars  
STRING X [size] [chars] |  Chars  
INTEGER X [size] |  Size  
INTEGER X [size 1] [size 2] |  Size2  
SIGNED_INTEGER X [size] |  Size  
SIGNED_INTEGER X [size 1] [size 2] |  Size2  
SIGNED_LONG_INTEGER X [size] |  Size  
SIGNED_LONG_INTEGER X [size 1] [size 2] |  Size2  
BUFFER INPUT X [chars] |  Chars  
BUFFER INPUT X [size] [chars] |  Chars  
  
Example:

DIGITAL_INPUT TEST;

INTEGER My_Array[10][20];

PUSH TEST

{

PRINT("Columns = %d\n", GetNumArrayCols(My_Array));

}

In this example, Columns = 20 will be printed.

Version:

X Generation: SIMPL v1.50.06

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Array_Operations/GetNumArrayCols.htm*
