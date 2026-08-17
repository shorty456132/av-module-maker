# FileOpenShared

Name:

FileOpenShared

Syntax:

SIGNED_INTEGER FileOpenShared (STRING filename, INTEGER flags)

Description:

_3-Series and 4-Series  
_

_Opens a file in the specified folder. Unlike the function, [FileOpen](<FileOpen.htm>), this function will not prepend the Program ID Tag with the filename.  
_

**Virtual Control**

Opens a file in the specified folder. On Virtual Control, we will not prepend the Program ID Tag to the filename. For example, if you have a room called "HVAC" and want to open a file called "myFile.dat" in the directory, \NVRAM, the file “\NVRAM\\\myFile.dat” will be opened for that specific room.

Please see [File Functions Overview](<File_Functions_Overview.htm>) for additional information.

[FindFirstShared](<FindFirstShared.htm>) and [FileDeleteShared](<FileDeleteShared.htm>) should be used in conjunction with FileOpenShared when necessary.

NOTE: Refer to the [File Functions Overview](<File_Functions_Overview.htm>) topic statement on [Shared File Functions](<File_Functions_Overview.htm#SharedFileFunctions>) for more information.

NOTE: The function, [FileOpen](<FileOpen.htm>), will prepend the Program ID Tag to the filename

Parameters:

FILENAME specifies the full path name or relative path name (link) of the file to open/create.

FLAGS – File Open Flags. Can be combined using the Bitwise OR operator (|)

NOTE: One of the following flags must be specified: _O_RDONLY, _O_WRONLY, or _O_RDWR.

NOTE: When writing to the NVRAM disk, only one file can be open at one time. Subsequent requests to write a file will block for a period of time (currently 5 seconds) until the initial write completes. If the request times out, an error code of FILE_SHARE will be returned. It is then up to the programmer to retry or signify an error condition.

Open File Flags

KEYWORD |  FUNCTION  
---|---  
_O_APPEND |  Writes done at the end of file. Mutually exclusive with _O_TRUNC.  
_O_CREAT |  Creates file. If _O_APPEND is specified, the file will be created only if it doesn't already exist.  
_O_EXCL |  Open succeeds only if file doesn't already exist.  
_O_TRUNC |  Truncates file. Mutually exclusive with _O_APPEND.  
_O_TEXT |  Indicates the file is text.  
_O_BINARY |  Indicates the file is binary (basically raw data).  
_O_RDONLY |  Open file for reading only  
_O_RDWR |  Open file for both reading and writing  
_O_WRONLY |  Open file for writing only  
  
Return Value:

File handle if successful ( >= 0). Otherwise, file [error code](<File_Function_Return_Error_Codes.htm>) is returned.

NOTE: [FileClose](<FileClose.htm>)() must be called before the executing thread is terminated. Failure to do so will result in the file being left open and locked by the control system. Should this happen, the file will not be able to be opened again until the control system is rebooted.

Examples: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

1\. Open a file for read only:

SIGNED_INTEGER nFileHandle;

StartFileOperations();

nFileHandle = FileOpenShared ( "\\\CF0\\\MyFile", _O_RDONLY );

IF (nFileHandle < 0)

{

PRINT("Error Opening File MyFile\n");

}

EndFileOperations();

2\. Open an existing file to log data to the end:

SIGNED_INTEGER nFileHandle;

StartFileOperations();

nFileHandle = FileOpenShared ("\\\CF0\\\MyFile", _O_WRONLY | _O_APPEND) ;

IF (nFileHandle < 0)

{

PRINT("Error Opening File MyFile\n");

}

EndFileOperations();

3\. If a file exists, truncate it and get rid of previous contents. If it doesn't exist, create it.

SIGNED_INTEGER nFileHandle;

StartFileOperations();

nFileHandle = FileOpenShared ("\\\CF0\\\MyFile", _O_WRONLY | _O_CREAT | _O_TRUNC) ;

IF (nFileHandle < 0)

{

PRINT("Error Opening File MyFile\n");

}

EndFileOperations();

4\. Continue adding to the end of an existing log file, or create it if it does not already exist.

SIGNED_INTEGER nFileHandle;

StartFileOperations();

nFileHandle = FileOpenShared ("\\\CF0\\\MyFile", _O_WRONLY | _O_APPEND | _O_CREAT);

IF (nFileHandle < 0)

{

PRINT("Error Opening File MyFile\n");

}

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: Not Supported

3-Series: v <> and above

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/FileOpenShared.htm*
