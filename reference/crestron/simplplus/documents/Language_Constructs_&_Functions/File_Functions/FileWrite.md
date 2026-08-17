# FileWrite

Name:

FileWrite

Syntax:

SIGNED_INTEGER FileWrite (INTEGER handle, STRING buffer,

INTEGER count )

Description:

Writes data to a file as a series of bytes from a buffer, starting at the current file position. Refer to the section entitled “[Reading and Writing Data to a File](<Reading_and_Writing_Data_to_a_File.htm>)” for a discussion of when to use this function and when to use the related functions: [WriteInteger](<WriteInteger.htm>), [WriteString](<WriteString.htm>), [WriteStructure](<WriteStructure.htm>), [WriteSignedInteger](<WriteSignedInteger.htm>), [WriteLongInteger](<WriteLongInteger.htm>), [WriteSignedLongInteger](<WriteSignedLongInteger.htm>), [WriteIntegerArray,](<WriteIntegerArray.htm>) [WriteSignedIntegerArray](<WriteSignedIntegerArray.htm>), [WriteLongIntegerArr](<WriteLongIntegerArray.htm>)ay, [WriteSignedLongIntegerArray,](<WriteSignedLongIntegerArray.htm>) [WriteStringArray.](<WriteStringArray.htm>)

NOTE: Input and Output variables of any kind are not allowed in the file reading and writing functions, just internal variables.

Parameters:

HANDLE specifies the file handle of the previously opened file (from FileOpen).

BUFFER is the variable containing the bytes to be written.

COUNT specifies the number of bytes to write.

Return Value:

Number of bytes written to the file. If the return value is negative, it is an error code.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

SIGNED_INTEGER nFileHandle;

STRING sBuf[4096];

StartFileOperations();

sBuf = "Hello World!";

nFileHandle = FileOpen ( "\\\CF0\\\MyFile", _O_WRONLY );

IF (nFileHandle >= 0)

{

if( FileWrite(nFileHandle, sBuf, 4096) > 0 )

PRINT ( "Written to file: %s\n", sBuf );

IF ( FileClose ( nFileHandle ) <> 0 )

PRINT ( "Error closing file\n" );

}

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.03.18 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/FileWrite.htm*
