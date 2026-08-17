# File Functions Overview

File Functions perform file handle access from SIMPL+. Because of the overhead involved with maintaining current directory and file positions, there are restrictions on file I/O. Each SIMPL+ thread (main loop or event handler) that requires file operations must first identify itself with the operating system. This is done with the function, [StartFileOperations](<StartFileOperations.htm>). Before terminating the thread, the function [EndFileOperations](<EndOfFileOperations.htm>) must be called. Files cannot be opened across threads. In other words, you cannot open a file in one thread (function main say) and then access the file with the returned file handle in another (say an event handler). This is to prevent two events from writing to different parts of a file. This means that you should open, access and then close a file within the same thread. For example, a program might be structured as follows:

STRING sBuf[1000];

SIGNED_INTEGER nFileHandle;

CHANGE input

{

SIGNED_INTEGER nNumRead;

StartFileOperations();

nFileHandle = FileOpen ( "\\\CF0\\\MyFile", _O_RDONLY );

if ( nFileHandle >= 0 )

{

nNumRead=FileRead( nFileHandle, sBuf, 500;

Print ("Read Error\n");

FileClose( nFileHandle );

}

EndFileOperations();

}

/*******************************************************************************************

Main()

Uncomment and place one-time startup code here

(This code will get called when the system starts up)

*******************************************************************************************/

Function Main()

{

SIGNED_INTEGER nNumWritten;

StartFileOperations();

nFileHandle = FileOpen ( "\\\CF0\\\MyFile", _O_WRONLY );

if ( nFileHandle >= 0 )

{

sBuf = "Hello World!";

nNumWritten=FileWrite( nFileHandle, sBuf, 500 );

if(nNumWritten<0) Print ("WriteError");

FileClose( nFileHandle );

}

EndFileOperations();

}

Shared File Functions.

There are now shared file functions in SIMPL+. The shared file functions are briefly described in the following paragraphs:

[FileOpenShared](<FileOpenShared.htm>) opens a file in the specified folder. Unlike the function, [FileOpen](<FileOpen.htm>), this function will not prepend the Program ID Tag with the filename. FileOpen opens a file in the specified folder, prepending the Program ID Tag to the filename. For example, if you have a program called "HVAC" and want to open a file called "myFile.dat" in the directory, \NVRAM, the file “\NVRAM\HVAC\myFile.dat” will be opened.

[FindFirst](<File_First.htm>) and [FileDelete](<FileDelete.htm>) should be used in conjunction with FileOpen.

[FindFirstShared](<FindFirstShared.htm>) and [FileDeleteShared](<FileDeleteShared.htm>) should be used in conjunction with FileOpenShared.

Virtual Control:

By default, Virtual Control installs in /opt/crestron/virtualcontrol/ and any rooms that are started have their own separate folder in /opt/crestron/virtualcontrol/RunningPrograms/ROOMID.

Where ROOMID here is the unique ID that is used when the room gets created.

For example, when /User/File.txt is opened on Virtual Control,/opt/crestron/virtualcontrol/RunningPrograms/ROOMID/User/File.txt is actually opened.

On Virtual Control, every program runs in a single “room” and there is no sharing between rooms.

So, for Virtual Control specific, FileOpen() and FileOpenShared() will both go to the exact same folder and won’t prepend Program ID Tag with the filename.

This is different from 3-Series and 4-Series behavior and won’t prepend Program ID Tag with the filename. This is different from 3-Series and 4-Series behavior.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/File_Functions_Overview.htm*
