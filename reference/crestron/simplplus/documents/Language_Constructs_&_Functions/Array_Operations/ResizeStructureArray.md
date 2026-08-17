# ResizeStructureArray

Name:

ResizeStructureArray

Syntax:

SIGNED_INTEGER ResizeStructureArray (ARRAYNAME, INTEGER NewSize);

Description:

Changes the allocated size of the structure array to NewSize elements.

NOTE: To use this function, the [#ENABLE_DYNAMIC](<../Compiler_Directives/_ENABLE_DYNAMIC.htm>) compiler directive must be present in the SIMPL+ module and the variable must be declared as [DYNAMIC](<../Declarations/Dynamic.htm>).

Parameters:

ARRAYNAME - a Structure array variable that needs a change in allocated size.

NewSize indicates the new number of elements for the structure array.

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

STRUCTURE tagMyStruct

{

INTEGER MyIntArray[10][10];

STRING MyStrArray[10][10];

};

dynamic tagMyStruct myStructArr[10];

Function main()

{

SIGNED_INTEGER Status;

Status = ResizeStructureArray(myStructArr, 20);

If (status != 0)

Print(“Error occurred in resizing array MyStructArr\n”)

}

Version:

2 Series only

X Gen not supported

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Array_Operations/ResizeStructureArray.htm*
