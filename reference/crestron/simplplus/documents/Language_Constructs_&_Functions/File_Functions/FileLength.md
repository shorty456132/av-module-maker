# FileLength

Name:

FileLength

Syntax:

LONG_INTEGER FileLength (INTEGER handle)

Description:

Returns the length of a file.

Parameters:

HANDLE specifies the file handle of the previously opened file (from [FileOpen](<FileOpen.htm>)).

Return Value:

Number of bytes if successful. Otherwise, file [error code](<File_Function_Return_Error_Codes.htm>) is returned.

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

IF ( nFileHandle > 0 )

PRINT ( "Length of file = %d\n",

FileLength ( nFileHandle ) );

IF ( FileClose ( nFileHandle ) <> 0 )

PRINT ( "Error closing file\n" );

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/FileLength.htm*
