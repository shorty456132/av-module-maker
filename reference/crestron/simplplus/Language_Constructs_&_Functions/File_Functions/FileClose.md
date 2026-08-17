# FileClose

Name:

FileClose

Syntax:

SIGNED_INTEGER FileClose (INTEGER handle)

Description:

Closes a file opened previously by [FileOpen](<FileOpen.htm>). You MUST close a file that was opened, you won't be able to open it again, or eventually the control system may hang or reboot. A reboot clears all open files. Files must be opened and closed during a single thread of operation. Refer to [StartFileOperation](<StartFileOperations.htm>)s.

Parameters:

HANDLE specifies the file handle of the previously opened file (from [FileOpen](<FileOpen.htm>)).

Return Value:

Returns 0 if successful. Otherwise, file [error code](<File_Function_Return_Error_Codes.htm>) is returned.

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

IF (nFileHandle >= 0)

{

IF ( FileClose ( nFileHandle ) <> 0 )

PRINT ( "Error closing file\n" );

}

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/FileClose.htm*
