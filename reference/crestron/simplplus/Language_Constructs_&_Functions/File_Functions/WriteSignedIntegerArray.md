# WriteSignedIntegerArray

Name:

WriteSignedIntegerArray

Syntax:

SIGNED_INTEGER WriteSignedIntegerArray ( INTEGER file_handle,

SIGNED_INTEGER isArray[m][n] )

Description:

Writes the array to a file starting at the current file position. Two bytes are written, most significant first containing the row dimension of the array, then two more bytes are Write, containing the column dimension of the array. Then each signed integer is written as a two byte quantity, most significant byte first. The integers are stored in row-major order, e.g. all the elements of row 0 first, then the elements of row 1, etc. Note that there is one more row and one more column than the dimensions that are written, because there is a row 0 and a column 0. Refer to the section entitled “[Reading and Writing Data to a File](<Reading_and_Writing_Data_to_a_File.htm>)” for a discussion of when to use this function and when to use the related functions: [FileWrite](<FileWrite.htm>), [WriteInteger](<WriteInteger.htm>), [WriteString](<WriteString.htm>), [WriteStructure](<WriteStructure.htm>), [WriteSignedInteger](<WriteSignedInteger.htm>), [WriteLongInteger](<WriteLongInteger.htm>), [WriteSignedLongInteger](<ReadSignedLongInteger.htm>), [WriteIntegerArray](<WriteIntegerArray.htm>), [WriteLongIntegerArray](<WriteLongIntegerArray.htm>), [WriteSignedLongIntegerArray](<WriteSignedLongIntegerArray.htm>), [WriteStringArray](<WriteStringArray.htm>).

NOTE: Input and Output variables of any kind are not allowed in the file reading and writing functions, just internal variables.

NOTE: Use [ReadSigned IntegerArray](<ReadSignedIntegerArray.htm>) to read this.

Parameters:

FILE_HANDLE specifies the file handle of the previously opened file (from [FileOpen](<FileOpen.htm>)).

ISARRAY is the array whose values are Write.

Return Value:

Number of bytes written to the file. If the return value is negative, it is an [error code](<File_Function_Return_Error_Codes.htm>).

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

SIGNED_INTEGER nFileHandle, iErrorCode;

SIGNED_INTEGER isArray[10][5];

StartFileOperations();

nFileHandle = FileOpen ( "\\\CF0\\\MyFile", _O_WRONLY );

IF (nFileHandle >= 0)

{

iErrorCode = WriteSignedIntegerArray(nFileHandle, isArray);

if (iErrorCode > 0)

PRINT ( "Array written to file correctly.\n");

else

PRINT ( "Error code %d\n", iErrorCode);

}

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/WriteSignedIntegerArray.htm*
