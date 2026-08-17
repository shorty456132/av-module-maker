# ByRef, ByVal, ReadOnlyByRef

NOTE: Passing STRINGs with BYVAL and BYREF is not allowed in the 2-Series Control System. All STRINGs are passed by referenced in the 2-Series Control System.

NOTE: Passing I/O datatype variables (DIGITAL_INPUT, ANALOG_INPUT and STRING_INPUT) is not allowed in the 2-Series Control System.

KEYWORD |  MEANING  
---|---  
ByRef |  Changes made to the variable that is passed to the function actually change the contents of the source variable. Note that any change made to the source variable will be reflected in the function. For example, if an INTEGER is passed ByRef and its state changes, the function will know about the change. It is typically more efficient to pass a variable by reference because space is not taken up by making local copies as with ByVal. Also referred to as "Pass by Reference".  
ByVal |  The variable that is passed to the function has a local copy made of it. Changes made to the variable in the function are made on a local copy. The local copy is destroyed when the function terminates. The contents of this variable are a "snapshot" of the contents of the variable that was passed. Unlike Pass by Reference, changes made to the original variable that was passed to the function are not recognized in the function. When an expression is passed, it may only be passed by value since there is no source variable that the ByRef keyword may potentially modify. Also referred to as "Pass by Value".  
ReadOnlyByRef |  This performs a Pass by Reference, identical to ByRef, but the compiler catches operations that write to the variable that has been passed. This would be typically be used if a DIGITAL_INPUT or other input type has been passed and which cannot be written. It is also used as a tool to catch unintentional writes to variables that have been passed.  
  
If not specified in the function declaration, variables will be passed by reference if applicable. If the variable cannot be passed by reference (such as an element of an array), it will be passed by value. Any expression will always be passed by value.

The following table shows legal access methods for the basic data types when passed

to a function.

VARIABLE TYPE |  ByVal [LOCAL COPY] |  ByRef [SOURCE] |  ReadOnlyByRef [SOURCE]  
---|---|---|---  
ANALOG_INPUT |  R, W |  R, (E1) |  R  
ANALOG_INPUT array |  - |  R, (E1) |  R  
ANALOG_INPUT array element |  R,W |  - |  -  
ANALOG_OUTPUT |  R,W |  - |  R  
ANALOG_OUTPUT array |  - |  - |  R  
ANALOG_OUTPUT array element |  R, W |  - |  -  
BUFFER_INPUT |  R, W |  R |  R  
BUFFER_INPUT array |  - |  R |  R  
BUFFER_INPUT array element |  R, W |  - |  -  
DIGITAL_INPUT |  R, W |  R, (E1) |  R  
DIGITAL_INPUT array |  - |  R, (E1) |  R  
DIGITAL_INPUT array element |  R, W |  - |  -  
DIGITAL_OUTPUT |  R, W |  - |  R  
DIGITAL_OUTPUT array |  - |  - |  R  
DIGITAL_OUTPUT array element |  R, W |  - |  -  
INTEGER |  R, W |  R, W |  R  
INTEGER array |  - |  R, W |  R  
INTEGER array element |  R, W |  - |  -  
LONG_INTEGER |  R, W |  R, W |  R  
LONG_INTEGER array |  - |  R, W |  R  
LONG_INTEGER array element |  R, W |  - |  -  
SIGNED_INTEGER |  R, W |  R, W |  R  
SIGNED_INTEGER array |  - |  R, W |  R  
SIGNED_INTEGER array element |  R, W |  - |  -  
SIGNED_LONG_INTEGER |  R, W |  R, W |  R  
SIGNED_LONG_INTEGER array |  - |  R, W |  R  
SIGNED_LONG_INTEGER array element |  R, W |  - |  -  
STRING |  R, W |  R, W |  R  
STRING array |  - |  R, W |  R  
STRING array element |  R, W |  - |  -  
STRING_INPUT |  R, W |  R |  R  
STRING_INPUT array |  - |  R |  R  
STRING_INPUT array element |  R, W |  - |  -  
STRING_OUTPUT |  - |  - |  -  
STRING_OUTPUT array |  - |  - |  -  
STRING_OUTPUT array element |  - |  - |  -  
STRUCTURE |  - |  R, W |  R  
STRUCTURE element (INTEGER) |  R, W |  - |  -  
STRUCTURE element (LONG_INTEGER) |  R, W |  - |  -  
STRUCTURE element (SIGNED_INTEGER) |  R, W |  - |  -  
STRUCTURE element (SIGNED_LONG_INTEGER) |  R, W |  - |  -  
STRUCTURE element (STRING) |  - |  - |  -  
  
R: Read access allowed.

W: Write access allowed.

(E1): Generates a RunTime Error, not allowed to be write to INPUT values. The ReadOnlyByRef generates a compile error instead of a RunTime Error.

An example of a function declaration that has no parameters and returns no value would be:

FUNCTION PrintText()

{

// Code

}

The following is an example of a function declaration that takes an INTEGER and returns a STRING. The INTEGER is passed by value, so it cannot be modified.

NOTE: It is not strictly necessary to use the "ByVal" keyword here. ByVal can be used to make sure that no modifications to the original variable are done by accident within the function.

STRING_FUNCTION ComputeDate(ByVal INTEGER TheMonth)

{

STRING Month$[20];

// Code to compute Month$…

RETURN(Month$);

}

The following is an example of a function declaration that takes a STRING array and sorts it and an integer that takes the actual number of elements that are contained in the array. It returns an INTEGER error code:

INTEGER_FUNCTION SortNameInDatabase(STRING Name[],

INTEGER NumElements)

{

INTEGER Error;

// Code to sort Names[] and setError…

RETURN(Error);

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/User_Defined_Functions/ByRef%2C_ByVal%2C_ReadOnlyByRef.htm*
