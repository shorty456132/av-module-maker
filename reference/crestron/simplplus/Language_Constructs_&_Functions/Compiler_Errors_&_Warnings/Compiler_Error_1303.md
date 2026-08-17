# Compiler Error 1303

declaration error: Declaration type not allowed within structure: '<identifier>'

Structure cannot contain String Arrays or Structure

variables: '<identifier>'

Structure definitions not allowed within other structures

Local Structure declarations are not allowed

Structure datatypes can only be defined globally. Variables of a defined structure datatype may be declared both globally and locally and passed as function arguments. INTEGER, LONG_INTEGER, SIGNED_INTEGER, SIGNED_LONG_INTEGER and STRING are the only SIMPL+ datatypes allowed to be used as structure member fields. INTEGER and LONG_INTEGER can include 1 and 2 dimensional arrays. String arrays are not permitted.

The following are examples of this error:

STRUCTURE MyStruct // ok

{

INTEGER i, i1[10], l2[10][20]; // ok

SIGNED_INTEGER si, si1[10], si2[10][20]; // ok

LONG_INTEGER l, l1[10], l2[10][20]; // ok

SIGNED_LONG_INTEGER sl, sl1[10], sl2[10][20]; // ok

STRING s[100]; // ok

STRING sArr[10]; // error – string arrays are not allowed

// within structures

DIGITAL_INPUT di; // error – declaration type not allowed

DIGITAL_OUTPUT do; // error – declaration type not allowed

ANALOG_INPUT ai; // error – declaration type not allowed

ANALOG_INPUT ao; // error – declaration type not allowed

STRING_INPUT si; // error – declaration type not allowed

BUFFER_INPUT bi; // error – declaration type not allowed

STRING_OUTPUT so; // error – declaration type not allowed

STRUCTURE locStruct // error – declaration type not allowed

{

INTEGER x;

}

MyStruct ptr; // error – declaration type not allowed

}

FUNCTION MyFunc()

{

STRUCTURE MyStruct // error – local structures are not supported

{

INTEGER i, i1[10], l2[10][20];

}

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1303.htm*
