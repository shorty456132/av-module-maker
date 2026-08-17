# Compiler Error 1301

declaration error: Invalid array index

An index is required when accessing any element of an array. Two dimensional arrays require both indices of the array to be specified. This index must be a valid numeric expression.

All arrays are passed to functions by reference, so specifying an index in this case is not allowed.

The following are examples of this error:

INTEGER xArr[10], x2dArr[10][20]; // ok

STRING str[100], strArr[50][100]; // ok

STRING_INPUT strIn[100]; // ok

STRING_OUTPUT strOut; // ok

STRING str; // error – no length specified

STRING_INPUT strIn; // error – no length specified

BUFFER_INPUT bufIn; // error – no length specified

STRING_OUTPUT strOutArr[10][20]; // error – 2-D arrays not supported

STRING str[x]; // error – variables are not allowed

STRING str[myFunc()]; // error – function calls are

// not allowed

INTEGER_FUNCTION MyIntFunc( INTEGER x[], INTEGER xArr[][] )

{

xArr[1] = 5; // ok

xArr[1+2] = xArr[3+4]; // ok

xArr[1+xArr[2]] = xArr[xArr[3]]; // ok

xArr[MyIntFunc(xArr,x2dArr)] = 6; // ok

x2dArr[1][2] = 6; // ok

x2dArr[xArr[1]][xArr[2]] = x2dArr[xArr[5]][xArr[6]]; // ok

Call MyFunc( xArr, x2dArr ); // ok

xArr = 5; // error – no index specified

xArr[] = 0; // error – no index specified

xArr[str] = 6; // error - s is a STRING

xArr[5][6] = 7; // error – xArr is not a 2D array

xArr = xArr; // error – cannot copy arrays

xArr = x2dArr[1]; // error – cannot copy arrays

x2dArr[1] = xArr; // error – cannot copy arrays

Call MyIntFunc( xArr[5], x2dArr ); // error – cannot pass index

// arrays are passed

// by reference

}

FUNCTION MyStrFunc( STRING s, STRING s[] ) // ok

{

STRING sLocal[100];

str = “abc”; // ok

strArr[5] = “def”; // ok

strIn = s; // ok

strOut = s; // ok

sInArr[5] = “abc”; // ok

sOutArr[5] = “abc”; // ok

Call MyStrFunc( str, strArr ); // ok

str[1] = “a”; // error – s is a string, not an array

sLocal = str[1]; // error – individual characters within

// a string can only be accessed

// with the function, Byte()

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1301.htm*
