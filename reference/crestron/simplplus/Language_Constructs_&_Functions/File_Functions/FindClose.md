# FindClose

Name:

FindClose

Syntax:

SIGNED_INTEGER FindClose()

Description:

Signifies to the operating system that the find operation has ended. Always follows a [FindFirst](<File_First.htm>) or [FindNext](<FindNext.htm>).

Parameters:

None.

Return Value:

Returns 0 if successful and –1 if an error occurred.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

[FILE_INFO](<File_INFO_Structure.htm>) FileInfo;

SIGNED_INTEGER Found;

StartFileOperations();

Found = FindFirst("*.dat", FileInfo );

WHILE (Found = 0)

{

PRINT ( "%s\n", FileInfo.Name );

Found = FindNext(FileInfo);

}

IF ( FindClose() < 0 )

PRINT ( "Error in closing find operation\n" );

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/FindClose.htm*
