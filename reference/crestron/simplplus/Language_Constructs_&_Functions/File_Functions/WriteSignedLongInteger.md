# WriteSignedLongInteger

Name:

WriteSignedLongInteger

Syntax:

SIGNED_INTEGER WriteSignedLongInteger ( INTEGER file_handle,

SIGNED_LONG_INTEGER sli )

Description:

Writes data to a file starting at the current file position. Each element of the structure is written, without any padding bytes, that might actually be there in memory. Refer to the section titled  
“[Reading and Writing Data to a File](<Reading_and_Writing_Data_to_a_File.htm>)” for a discussion of when to use this function and when to use the related functions: [FileWrite](<FileWrite.htm>), [WriteInteger](<WriteInteger.htm>), [WriteString](<WriteString.htm>), [WriteStructure](<WriteStructure.htm>), [WriteSignedInteger,](<WriteSignedInteger.htm>) [WriteLongInteger](<WriteLongInteger.htm>), [WriteIntegerArray](<WriteIntegerArray.htm>), [WriteSignedIntegerArray](<WriteSignedIntegerArray.htm>), [WriteLongIntegerArray](<WriteLongIntegerArray.htm>), [WriteSignedLongIntegerArray](<WriteSignedLongIntegerArray.htm>), [WriteStringArray](<WriteStringArray.htm>).

NOTE: Use [ReadSignedLongInteger](<ReadSignedLongInteger.htm>) to read this.

Parameters:

FILE_HANDLE specifies the file handle of the previously opened file (from [FileOpen](<FileOpen.htm>)).

SLI is the signed long integer whose value is written.

Return Value:

Number of bytes written to the file. If the return value is negative, it is an error code.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

INTEGER nFileHandle, iErrorCode;

SIGNED_LONG_INTEGER sli;

StartFileOperations();

nFileHandle = FileOpen ( "\\\CF0\\\MyFile", _O_WRONLY );

IF (nFileHandle >= 0)

{

iErrorCode = WriteSignedLongInteger(nFileHandle, sli);

if (iErrorCode > 0)

PRINT ( "Written to file correctly.\n");

else

PRINT ( "Error code %d\n", iErrorCode);

}

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.03.18 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/WriteSignedLongInteger.htm*
