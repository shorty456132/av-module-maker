# FileSeek

Name:

FileSeek

Syntax:

SIGNED_LONG_INTEGER FileSeek (INTEGER handle, SIGNED_LONG_INTEGER offset,

INTEGER origin )

Description:

Positions the current file pointer.

Parameters:

HANDLE specifies the file handle of previously opened file (from [FileOpen](<FileOpen.htm>)).

OFFSET specifies the number of bytes to move relative to the origin.

ORIGIN is one of the file seek flags in the following table.

File Seek Flags

KEYWORD |  FUNCTION  
---|---  
SEEK_SET |  Start seeking from beginning of file  
SEEK_CUR |  Start seeking from current position in file  
SEEK_END |  Start seeking from end of file  
  
Return Value:

Number of bytes offset from the beginning of file. Otherwise, file [error code](<File_Function_Return_Error_Codes.htm>) is returned.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

SIGNED_INTEGER nFileHandle;

StartFileOperations();

nFileHandle = FileOpen("\\\CF0\\\MyFile", _O_RDONLY);

IF (nFileHandle >= 0)

{

IF (FileSeek( nFileHandle, 0, SEEK_SET)) < 0 )

PRINT ( "Error seeking file\n" );

IF ( FileClose ( nFileHandle ) <> 0 )

PRINT ( "Error closing file\n" );

}

EndFileOperations();

Other Examples:

1\. Go to beginning of file  
FileSeek (nFileHandle,0,SEEK_SET)

2\. Go to end of file  
FileSeek (nFileHandle,0,SEEK_END)

3\. Get current file position  
CurrentBytePosition= FileSeek(nFileHandle,0,SEEK_CUR)

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/FileSeek.htm*
