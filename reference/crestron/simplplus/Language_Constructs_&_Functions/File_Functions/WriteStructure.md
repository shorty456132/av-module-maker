# WriteStructure

Name:

WriteStructure

Syntax:

WriteStructure ( INTEGER nFileHandle, STRUCTURE struct [, INTEGER nTotalBytesWritten] )

Description:

Writes data to a file starting at the current file position. Each element of the structure is written, without any padding bytes, that might actually be there in memory. Refer to the section entitled “[Reading and Writing Data to a File](<Reading_and_Writing_Data_to_a_File.htm>)” for a discussion of when to use this function and when to use the related functions: [FileWrite](<FileWrite.htm>), [WriteInteger](<WriteInteger.htm>), [WriteString](<WriteString.htm>), [WriteSignedInteger](<WriteSignedInteger.htm>), [WriteLongInteger](<WriteLongInteger.htm>), [WriteSignedLongInteger](<WriteSignedLongIntegerArray.htm>), [WriteIntegerArray](<WriteIntegerArray.htm>), [WriteSignedIntegerArray](<WriteSignedIntegerArray.htm>), [WriteLongIntegerArray](<WriteLongIntegerArray.htm>), [WriteSignedLongIntegerArray](<WriteSignedLongInteger.htm>), [WriteStringArray](<WriteStringArray.htm>).

NOTE: Input and Output variables of any kind are not allowed in the file reading and writing functions, just internal variables.

NOTE: Use [ReadStructure](<Read_Structure.htm>) to read this.

Parameters:

nFileHandle - File handle of the previously opened file (from [FileOpen](<FileOpen.htm>)).

struct - Structure variable whose data will be written to the file

nTotalBytesWritten - optional argument. INTEGER variable that will contain the total number of bytes written to the file from the structure.

Return Value:

NONE

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

SIGNED_INTEGER nFileHandle, nTotalBytesWritten;

STRUCTURE PhoneBookEntry

{

STRING Name[50];

STRING Address[100];

STRING PhoneNumber[20];

};

PhoneBookEntry OneEntry;

StartFileOperations();

nFileHandle = FileOpen ( "\\\CF0\\\MyFile.txt", _O_WRONLY );

if (nFileHandle >= 0)

{

WriteStructure( nFileHandle, OneEntry, nTotalBytesWritten );

if( nTotalBytesWritten < 0 )

PRINT ( "Error writing structure. Error code = %d\n", nTotalBytesWritten );

else

PRINT ( "Structure written to file correctly. Total bytes written = %d\n", nTotalBytesWritten );

}

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/WriteStructure.htm*
