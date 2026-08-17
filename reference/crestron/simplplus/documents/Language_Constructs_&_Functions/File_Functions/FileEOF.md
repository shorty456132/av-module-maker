# FileEOF

Name:

FileEOF

Syntax:

SIGNED_INTEGER FileEOF (INTEGER handle)

Description:

Tests whether or not the current file pointer is at the end of the file.

Parameters:

HANDLE specifies the file handle of the previously opened file (from [FileOpen](<FileOpen.htm>)).

Return Value:

Returns 1 if end of file or 0 if not end of file. Otherwise, file [error code](<File_Function_Return_Error_Codes.htm>) is returned.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

SIGNED_INTEGER nFileHandle;

StartFileOperations();

nFileHandle = FileOpen ( "\\\CF0\\\MyFile", _O_RDONLY );

IF (nFileHandle < 0)

{

PRINT("Error Opening File MyFile\n");

return;

}

IF ( FileEOF ( nFileHandle ) = 1 )

PRINT ( "End of file reached\n" );

IF ( FileClose ( nFileHandle ) <> 0 )

PRINT ( "Error closing file\n" );

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/FileEOF.htm*
