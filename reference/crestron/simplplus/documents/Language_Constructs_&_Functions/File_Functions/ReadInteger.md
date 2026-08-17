# ReadInteger

Name:

ReadInteger

Syntax:

SIGNED_INTEGER ReadInteger ( INTEGER file_handle, INTEGER i )

Description:

Reads an integer from a file starting at the current file position. Two bytes are read, most significant byte first. Refer to the section entitled “[Reading and Writing Data to a File](<Reading_and_Writing_Data_to_a_File.htm>)” for a discussion of when to use this function and when to use the related functions: [FileRead](<FileRead.htm>), [ReadString](<ReadString.htm>), [ReadStructure](<Read_Structure.htm>), [ReadSignedInteger](<ReadSignedInteger.htm>), [ReadLongInteger](<ReadLongInteger.htm>), [ReadSignedLongInteger](<ReadSignedLongInteger.htm>), [ReadIntegerArray](<ReadIntegerArray.htm>), [ReadSignedIntegerArray](<ReadSignedIntegerArray.htm>), [ReadLongIntegerArray](<ReadIntegerArray.htm>), [ReadSignedLongIntegerArray](<ReadSignedLongIntegerArray.htm>), [ReadStringArray](<ReadStringArray.htm>).

NOTE: Input and Output variables of any kind are not allowed in the file read functions.

Parameters:

FILE_HANDLE specifies the file handle of the previously opened file (from [FileOpen](<FileOpen.htm>)).

I is the integer whose value is read.

Return Value:

Number of bytes read from file. If the return value is negative, it is an error code.  
If no Return Value is specified within an Integer_Function, then a 0 will be returned by default.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

SIGNED_INTEGER nFileHandle, iErrorCode;

INTEGER i;

StartFileOperations();

nFileHandle = FileOpen ( "\\\CF0\\\MyFile", _O_RDONLY );

IF (nFileHandle >= 0)

{

iErrorCode = ReadInteger(nFileHandle, i);

if (iErrorCode > 0)

PRINT ( "Read integer from file correctly.\n");

else

PRINT ( "Error code %d\n", iErrorCode);

}

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: SIMPL v2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/ReadInteger.htm*
