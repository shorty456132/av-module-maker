# ReadSignedIntegerArray

Name:

ReadSignedIntegerArray

Syntax:

SIGNED_INTEGER ReadSignedIntegerArray ( INTEGER file_handle,

SIGNED_INTEGER isArray[m][n] )

Description:

Reads the array from a file starting at the current file position. Two bytes are read, most significant first containing the row dimension of the array, then two more bytes are read, containing the column dimension of the array. Then each signed integer is read as a two byte quantity, most significant byte first. The integers are stored in row-major order, e.g. all the elements of row 0 first, then the elements of row 1, etc. Note that there is one more row and one more column than the dimensions that are read, because there is a row 0 and a column 0. Refer to the section entitled “[Reading and Writing Data to a File](<Reading_and_Writing_Data_to_a_File.htm>)” for a discussion of when to use this function and when to use the related functions: [FileRead](<FileRead.htm>), [ReadInteger](<ReadInteger.htm>), [ReadString](<ReadString.htm>), [ReadStructure](<Read_Structure.htm>), [ReadSignedInteger](<ReadSignedInteger.htm>), [ReadLongInteger](<ReadLongInteger.htm>), [ReadSignedLongInteger](<ReadSignedLongInteger.htm>), [ReadIntegerArray](<ReadIntegerArray.htm>), [ReadLongIntegerArray](<ReadLongIntegerArray.htm>), [ReadSignedLongIntegerArray](<ReadSignedLongIntegerArray.htm>), [ReadStringArray](<ReadStringArray.htm>).

NOTE: Input and Output variables of any kind are not allowed in the file read functions.

Parameters:

FILE_HANDLE specifies the file handle of the previously opened file (from [FileOpen](<FileOpen.htm>)).

ISARRAY is the array whose values are read. If no Return Value is specified within an Integer_Function, then a 0 will be returned by default.

Return Value:

Number of bytes read from file. If the return value is negative, it is an [error code](<File_Function_Return_Error_Codes.htm>). An error occurs if the array is not large enough to hold the data.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

SIGNED_INTEGER nFileHandle, iErrorCode;

SIGNED_INTEGER isArray[10][5];

StartFileOperations();

nFileHandle = FileOpen ( "\\\CF0\\\MyFile", _O_RDONLY );

IF (nFileHandle >= 0)

{

iErrorCode = ReadSignedIntegerArray(nFileHandle, isArray);

if (iErrorCode > 0)

PRINT ( "Read array from file correctly.\n");

else

PRINT ( "Error code %d\n", iErrorCode);

}

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/ReadSignedIntegerArray.htm*
