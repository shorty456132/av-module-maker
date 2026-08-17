# StartFileOperations

Name:

StartFileOperations

Syntax:

SIGNED_INTEGER StartFileOperations()

Description:

Signifies to the operating system that the current thread is starting its file operations.

Required prior to any operation accessing a file, including all functions in [FileFunctions](<File_Functions_Overview.htm>).

[EndFileOperations](<EndOfFileOperations.htm>) is required after finishing all file operations and prior to terminating the thread of execution (e.g., one of the PUSH commands).

Parameters:

None.

Return Value:

Returns 0 if successful and –1 if an error occurred.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>), specifically refer to the note about StartFileOperations)

IF ( StartFileOperations() < 0 )

PRINT ( "Error in starting file ops\n" );

// various file operations

IF ( EndFileOperations() < 0 )

PRINT ( "Error Occurred in ending file ops\n" );

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/StartFileOperations.htm*
