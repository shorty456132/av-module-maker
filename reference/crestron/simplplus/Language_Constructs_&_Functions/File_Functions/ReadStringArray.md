# ReadStringArray

Name:

ReadStringArray

Syntax:

SIGNED_INTEGER ReadStringArray ( INTEGER file_handle, STRING s[] )

Description:

Reads a string from a file starting at the current file position. Internally, the string is stored with the first 2 bytes indicating the total number of string written, then each string follows as a 2-byte length, most significant byte first, then the actual string bytes. In the case of a string variable, the total number of bytes is calculated from the size of the string, not the string allocation size. Refer to the section entitled “[Reading and Writing Data to a File](<Reading_and_Writing_Data_to_a_File.htm>)” for a discussion of when to use this function and when to use the related functions: [FileRead](<FileRead.htm>), [ReadInteger](<ReadInteger.htm>), [ReadString](<ReadString.htm>), [ReadStructure](<Read_Structure.htm>), [ReadSignedInteger](<ReadSignedInteger.htm>), [ReadLongInteger](<ReadLongInteger.htm>), [ReadSignedLongInteger](<ReadSignedLongInteger.htm>), [ReadIntegerArray](<ReadIntegerArray.htm>), [ReadSignedIntegerArray](<ReadSignedIntegerArray.htm>), [ReadLongIntegerArray](<ReadLongIntegerArray.htm>), [ReadSignedLongIntegerArray](<ReadSignedLongIntegerArray.htm>).

NOTE: Input and Output variables of any kind are not allowed in the file reading and writing functions, just internal variables.

Parameters:

FILE_HANDLE specifies the file handle of the previously opened file (from [FileOpen](<FileOpen.htm>)).

S is the string whose value is read.

Return Value:

Number of bytes read from file into the string. If the return value is negative, it is an [error code](<File_Function_Return_Error_Codes.htm>). An error occurs if the array is not large enough to hold the data.

If no Return Value is specified within an String_Function, then an empty string will be returned by default.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

SIGNED_INTEGER nFileHandle, iErrorCode;

STRING s[100][100];

StartFileOperations();

nFileHandle = FileOpen ( "\\\CF0\\\MyFile", _O_RDONLY );

IF (nFileHandle >= 0)

{

iErrorCode = ReadStringArray( nFileHandle, s);

if (iErrorCode > 0)

PRINT ( "Read string from file correctly.\n");

else

PRINT ( "Error code %d\n", iErrorCode);

}

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/ReadStringArray.htm*
