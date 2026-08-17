# EndFileOperations

Name:

EndFileOperations

Syntax:

SIGNED_INTEGER EndFileOperations()

Description:

Signifies to the operating system that the current thread has completed its file operations.

[StartFileOperations](<StartFileOperations.htm>) is required prior to any operation accessing a file, including all functions in [FileOpen](<FileOpen.htm>).

EndFileOperations is required after finishing all file operations and prior to terminating the thread of execution (e.g., one of the PUSH commands).

Parameters:

None.

Return Value:

Returns 0 if successful and –1 if an error occurred.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

IF ( StartFileOperations() < 0 )

PRINT ( "Error in starting file ops\n" );

// various file operations

IF ( EndFileOperations() < 0 )

PRINT ( "Error Occurred in ending file ops\n" );

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/EndOfFileOperations.htm*
