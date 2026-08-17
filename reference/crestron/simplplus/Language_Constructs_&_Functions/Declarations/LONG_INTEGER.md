# LONG_INTEGER

Name:

LONG_INTEGER

Syntax:

LONG_INTEGER <var1>[,<var2>...];

LONG_INTEGER <var1>[size] [,<var2>[size]…];

LONG_INTEGER <var1>[rows1][columns1] [,<var2>[rows2][columns2]…];

Description:

The first form declares a long value that is local to this SIMPL+ program. LONG_INTEGER values are 32-bit quantities ranging from 0-4294967295.

The second form declares a one-dimensional array of LONG_INTEGER values.

The third form declares a two-dimensional array of LONG_INTEGER values. A two-dimensional array can be thought of as a table or matrix.

The values for SIZE, ROWS, and COLUMNS may be up to 65534.

A LONG_INTEGER array element may be used anywhere a LONG_INTEGER is legal. Array elements are referenced by using the name followed by [element] for one-dimensional arrays or [row][column] for two-dimensional arrays. The element number may range from 0 to the element size. For example, if an array is declared as NUM[2], then legal elements are NUM[0], NUM[1], and NUM[2]. The bracket notation is often called an array subscript.

NOTE: (2-Series) LONG_INTEGERs can be volatile or non-volatile. The default is defined using the compiler directives #DEFAULT_NONVOLATILE or #DEFAULT_VOLATILE or overriden using the nonvolatile or volatile keywords.

Example:

LONG_INTEGER temp_level;

Specifies one locally declared LONG_INTEGER in this SIMPL+ program

LONG_INTEGER CommandBytes[2];

Specifies an array of three LONG_INTEGERs that can be referenced under the name CommandBytes. In pictorial form, it appears as:

CommandBytes[0] |  CommandBytes[1] |  CommandBytes[2]  
---|---|---  
  
LONG_INTEGER Matrix[4][3];

Specifies a two-dimensional array of LONG_INTEGERs five rows deep by four columns wide. In pictorial form, it appears as:

Matrix[0][0] |  Matrix[0][1] |  Matrix[0][2] |  Matrix[0][3]  
---|---|---|---  
Matrix[1][0] |  Matrix[1][1] |  Matrix[1][2] |  Matrix[1][3]  
Matrix[2][0] |  Matrix[2][1] |  Matrix[2][2] |  Matrix[2][3]  
Matrix[3][0] |  Matrix[3][1] |  Matrix[3][2] |  Matrix[3][3]  
Matrix[4][0] |  Matrix[4][1] |  Matrix[4][2] |  Matrix[4][3]  
  
NOTE: The subscripts of an array may be an expression, i.e.:

LONG_INTEGER location[5], room;

room = 2;

location[room] = 10;

Version:

X Generation: Not Supported

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Declarations/LONG_INTEGER.htm*
