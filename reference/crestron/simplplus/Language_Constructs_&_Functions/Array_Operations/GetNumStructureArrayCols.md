# GetNumStructureArrayCols

Name:

GetNumStructureArrayCols

Syntax:

INTEGER GetNumStructureArrayCols( STRUCTURE_ARRAY );

Description:

Returns the number of columns in a structure array.

Parameters:

STRUCTURE_ARRAY is the structure array variable.

Return Value:

The number of columns in the structure array.

Example:

STRUCTURE tagStruct

{

INTEGER i;

};

tagStruct myStructArr[10];

FUNCTION foo()

{

INTEGER numCols;

numCols = GetNumStructureArrayCols( myStructArr ); // numCols = 10 

}

Version:

X Generation: SIMPL v1.50.06

2-Series: SIMPL v2.01.05 and later

3-Series:

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Array_Operations/GetNumStructureArrayCols.htm*
