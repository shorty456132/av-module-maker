# ReadLongInteger

Name:

ReadLongInteger

Syntax:

SIGNED_INTEGER ReadLongInteger ( INTEGER file_handle,

LONG_INTEGER li )

Description:

Reads a long integer from a file starting at the current file position. Four bytes are read, most significant byte first and least significant byte last. Refer to the section entitled “[Reading and Writing Data to a File](<Reading_and_Writing_Data_to_a_File.htm>)” for a discussion of when to use this function and when to use the related functions: [FileRead](<FileRead.htm>), [ReadInteger](<ReadInteger.htm>), [ReadString](<ReadString.htm>), [ReadStructure](<Read_Structure.htm>), [ReadSignedInteger](<ReadSignedInteger.htm>), [ReadSignedLongInteger](<ReadSignedLongInteger.htm>), [ReadIntegerArray](<ReadIntegerArray.htm>), [ReadSignedIntegerArray](<ReadSignedIntegerArray.htm>), [ReadLongIntegerArray](<ReadLongIntegerArray.htm>), [ReadSignedLongIntegerArray](<ReadSignedLongIntegerArray.htm>), [ReadStringArray](<ReadStringArray.htm>).

NOTE: Input and Output variables of any kind are not allowed in the file read functions.

Parameters:

FILE_HANDLE specifies the file handle of the previously opened file (from [FileOpen](<FileOpen.htm>)).

LI is the long integer whose value is read.

Return Value:

Number of bytes read from file. If the return value is negative, it is an [error code](<File_Function_Return_Error_Codes.htm>).

If no Return Value is specified within an Integer_Function, then a 0 will be returned by default.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

SIGNED_INTEGER nFileHandle, iErrorCode;

LONG_INTEGER li;

StartFileOperations();

nFileHandle = FileOpen ( "\\\CF0\\\MyFile", _O_RDONLY );

IF (nFileHandle >= 0)

{

iErrorCode = ReadLongInteger(nFileHandle, li);

if (iErrorCode > 0)

PRINT ( "Read long integer from file correctly.\n");

else

PRINT ( "Error code %d\n", iErrorCode);

}

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/ReadLongInteger.htm*
