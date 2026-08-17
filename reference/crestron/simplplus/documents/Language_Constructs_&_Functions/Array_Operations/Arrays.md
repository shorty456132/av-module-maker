# Arrays

Various one and two dimensional arrays are supported. All input and output arrays are 1-based, meaning that the first element has index 1, not 0. Internal variables are 0-based, meaning that the first element has index 0. In both cases, the index of the last element is the same as the dimension of the array.

Do not confuse the declaration of the length of STRINGs with the declaration of arrays. E.g., STRING s$[32] is a single string of length 32, and STRING ManyS$[10][32] is an array of 11 strings of length 32 each. You must use the BYTE function to access the character at a particular position in a string, but you can use the array index to access a particular string in an array of strings. Positions in a string are 1-based. See the discussion of Minimum Size Arrays in [Declaration Overview](<../Declarations/Declarations_Overview.htm>).

One dimensional arrays of the following types are supported:

DIGITAL_INPUT

DIGITAL_OUTPUT

ANALOG_INPUT

ANALOG_OUTPUT

STRING_OUTPUT

BUFFER_OUTPUT

STRUCTURES

One dimensional arrays of strings are also supported, although since the declaration also contains a string length, it looks like a 2-dimensional array:

STRING_INPUT

BUFFER_INPUT

STRING

One and two dimensional arrays of the following types are supported:

INTEGER

LONG_INTEGER

SIGNED_INTEGER

SIGNED_LONG_INTEGER

Examples:

Declaration |  Meaning  
---|---  
DIGITAL_INPUT in[10]; |  10 digital inputs, in[1] to in[10]  
INTEGER MyArray[10][20]; |  11 rows by 21 columns of data, from MyArray[0][0] to MyArray[10][20]  
STRING PhoneNumbers[100][32]; |  101 strings that are a maximum of 32 characters long, e.g. PhoneNumbers[0] to PhoneNumbers[100]  
STRING_INPUT in$[32]; |  One input string called in$ that is 32 characters long.  
STRING_OUTPUT out$[10]; |  Ten output strings, out$1 to out$[10]. Their length does not have to be specified.  
STRING_INPUT in$[5][32]; |  Five input strings, in$[1] to in$[5] that are 32 characters long.  
<struct_type> myStruct[10]; |  11 structure elements from myStruct[0] to myStruct[10].  
  
NOTE: An element of an integer array is not accepted where a function requires an integer.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Array_Operations/Arrays.htm*
