# FindFirstShared

Name:

FindFirstShared

Syntax:

SIGNED_INTEGER FindFirstShared(STRING filespec, FILE_INFO info)

Description:

This command searches a directory for file(s) matching the given file specification (first file shared). Always followed with a [FindClose](<FindClose.htm>). Requires [StartFileOperations()](<StartFileOperations.htm>).

[FileOpenShared](<FileOpenShared.htm>) and [FileDeleteShared](<FileDeleteShared.htm>) should be used in conjunction with FindFirstShared when necessary.

NOTE: Refer to the [File Functions Overview](<File_Functions_Overview.htm>) topic statement on [Shared File Functions](<File_Functions_Overview.htm#SharedFileFunctions>) for more information.

Parameters:

FILESPEC specifies the filename to look for. It can be a full path name or a [relative path name](<../../General_Information/Relative_Path_Names_for_Files.htm>) with wildcards ( the ‘*’ character).

INFO – FILE_INFO structure containing the information about a found file:

File Attribute Bit Flags (May be checked with bitwise & character)

KEYWORD |  ATTRIBUTE  
---|---  
ARDONLY |  File is marked read only  
AHIDDEN |  File is hidden  
ASYSTEM |  File is marked as a system file  
AVOLUME |  File is a volume label  
ADIRENT |  File is a directory  
ARCHIVE |  File is marked as archived  
  
Return Value:

Returns 0 if a file is found matching the specification and –1 if an error occurred.

Example:

(see [File Functions Overview](<File_Functions_Overview.htm>))

FILE_INFO FileInfo;

SIGNED_INTEGER Found;

StartFileOperations();

Found = FindFirstShared("*.dat", FileInfo );

WHILE (Found = 0)

{

IF ((FileInfo.iAttributes & ADIRENT)<>0)

PRINT ( "%s is a directory\n",FileInfo.Name);

else

PRINT ("%s is a file\n",FileInfo.Name);

Found = FindNext(FileInfo);

}

IF ( FindClose() < 0 )

PRINT ( "Error in closing find operation\n" );

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: Not Supported

3-Series: v <> and above

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/FindFirstShared.htm*
