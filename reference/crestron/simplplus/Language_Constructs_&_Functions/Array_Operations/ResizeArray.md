# ResizeArray

Name:

ResizeArray

Syntax:

SIGNED_INTEGER ResizeArray (ARRAY_NAME, INTEGER NewNumElements, INTEGER NewSize);

Description:

Changes the allocated size of the string array to NewNumElements of NewSize bytes or the integer array to NewNumElements rows of NewSize columns or the structure array to NewSize elements.

NOTE: To use this function, the [#ENABLE_DYNAMIC](<../Compiler_Directives/_ENABLE_DYNAMIC.htm>) compiler directive must be present in the SIMPL+ module and the variable must be declared as [DYNAMIC](<../Declarations/Dynamic.htm>).

NOTE: The NewNumElements parameter is optional.

Parameters:

ARRAYNAME can be either an integer or string array variable that needs a change in allocated size.

NewNumElements indicates the new number of elements in the string array or number of rows for a 2-D integer array (should be 0 for 1-D arrays).

NewSize indicates the new number of bytes in each string in the array or the new number of columns for the integer array.

Return Value:

Status |  Definition  
---|---  
0 |  Success  
0x8001 |  Generic Error  
0x8002 |  Error – Max Resize limit reached  
0x8004* |  Error – Element is not dynamic  
0x8008 |  Warning – Truncation will occur  
0x8010 |  Error – Out of memory  
0x8020 |  Error – Out of memory  
0x8040 |  Error – Out of memory  
  
* This error indicates that the #ENABLE_DYNAMIC compiler directive is missing from the SIMPL+ module and/or that the variable has not been declared as DYNAMIC.

NOTE: The status might contain an error and a warning returned together. For example, if an array is resized from 20 to 10 elements, a truncation warning will result. However, if the system is out of memory, the resize cannot be completed. In this scenario, the returned status will be 0x8008 | 0x8010, or 0x8018.

Example:

INTEGER MyIntArray[10][10];

STRING MyStringArray[10][10];

Function main()

{ 

SIGNED_INTEGER Status;

Status = ResizeArray(MyStringArray, 200, 80);

If (status != 0) 

Print(“Error occurred in resizing string array MyStringArray\n”)

Status = ResizeArray(MyIntArray, 200, 100);

If (status != 0)

Print(“Error occurred in resizing string array MyIntArray\n”)

}

In this example, the columns and rows of MyIntArray and MyStringArray are changed from 10 and 10 (for both MyIntArray and MyStringArray) to 200 and 100 for MyIntArray and 200 and 80 for MyStringArray.

Version:

2 Series only

X Gen Not Supported

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Array_Operations/ResizeArray.htm*
