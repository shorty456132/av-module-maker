# GetNumArrayRows

Name:

GetNumArrayRows

Syntax:

INTEGER GetNumArrayRows(STRING | INTEGER ARRAY_NAME);

Description:

Returns the number of rows for two-dimensional arrays or string arrays.

Parameters:

ARRAY_NAME is the array name as determined by the size.

Return Value:

For the data types in the table after this paragraph, the return value of GetNumArrayRows is shown.

Example:

DIGITAL_INPUT TEST;

INTEGER My_Array[10][20];

PUSH TEST

{

PRINT("Rows = %d\n", GetNumArrayRows(My_Array));

}

In this example, Rows = 10 will be printed.

Version:

X Generation: SIMPL v1.50.06

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Array_Operations/GetNumArrayRows.htm*
