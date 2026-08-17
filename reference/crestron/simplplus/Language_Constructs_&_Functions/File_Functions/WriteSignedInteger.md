# WriteSignedInteger

Name:

WriteSignedInteger

Syntax:

SIGNED_INTEGER WriteSignedInteger ( INTEGER file_handle,

SIGNED_INTEGER si )

Description:

Writes a signed integer to a file starting at the current file position. Two bytes are written, most significant first. Refer to the section entitled “[Reading and Writing Data to a File](<Reading_and_Writing_Data_to_a_File.htm>)” for a discussion of when to use this function and when to use the related functions: [FileWrite](<FileWrite.htm>), [WriteInteger](<WriteInteger.htm>), [WriteString](<WriteString.htm>), [WriteStructure](<WriteStructure.htm>), [WriteLongInteger](<WriteLongInteger.htm>), [WriteSignedLongInteger](<WriteSignedLongInteger.htm>), [WriteIntegerArray](<WriteIntegerArray.htm>), [WriteSignedIntegerArray](<WriteSignedIntegerArray.htm>), [WriteLongIntegerArray](<WriteLongIntegerArray.htm>), [WriteSignedLongIntegerArray](<WriteSignedLongIntegerArray.htm>), [WriteStringArray](<WriteStringArray.htm>).

NOTE: Input and Output variables of any kind are not allowed in the file reading and writing functions, just internal variables.

NOTE: Use [ReadSignedInteger](<ReadSignedInteger.htm>) to read this.

Parameters:

FILE_HANDLE specifies the file handle of the previously opened file (from [FileOpen](<FileOpen.htm>)).

SI is the signed integer whose value is written.

Return Value:

Number of bytes written to the file. If the return value is negative, it is an [error code](<File_Function_Return_Error_Codes.htm>).

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

SIGNED_INTEGER nFileHandle, iErrorCode;

SIGNED_INTEGER si;

StartFileOperations();

nFileHandle = FileOpen ( "\\\CF0\\\MyFile", _O_WRONLY );

IF (nFileHandle >= 0)

{

iErrorCode = WriteSignedInteger(nFileHandle, si);

if (iErrorCode > 0)

PRINT ( "Written to file correctly\n");

else

PRINT ( "Error code %d\n", iErrorCode);

}

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/WriteSignedInteger.htm*
