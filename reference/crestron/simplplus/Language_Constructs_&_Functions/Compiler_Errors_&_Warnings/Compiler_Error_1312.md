# Compiler Error 1312

declaration error: Array boundary exceeded maximum size of ‘num_bytes’ bytes

The maximum number of indices for an array is 65535.

The following are examples of this error.

FUNCTION MyFunc()

{

INTEGER int[100], intArr[100][100]; // ok

STRING str[100], strArr[100][100]; // ok

INTEGER int[100000]; // error

INTEGER intArr[100000][100]; // error

INTEGER intArr[100][100000]; // error

STRING str[100000]; // error

STRING strArr[100000][100]; // error

STRING strArr[100][100000]; // error

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1312.htm*
