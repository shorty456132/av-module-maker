# ReadStructure

Name:

ReadStructure

Syntax:

ReadStructure ( INTEGER nFileHandle, STRUCTURE struct [, INTEGER nTotalBytesRead] )

Description:

Reads data from a file starting at the current file position. Each element of the structure is read, without any padding bytes, that might actually be there in memory. Refer to the section entitled “[Reading and Writing Data to a File](<Reading_and_Writing_Data_to_a_File.htm>)” for a discussion of when to use this function and when to use the related functions: [FileRead](<FileRead.htm>), [ReadInteger](<ReadInteger.htm>), [ReadString](<ReadString.htm>), [ReadSignedInteger](<ReadSignedInteger.htm>), [ReadLongInteger](<ReadLongInteger.htm>), [ReadSignedLongInteger](<ReadSignedLongInteger.htm>), [ReadIntegerArray](<ReadIntegerArray.htm>), [ReadSignedIntegerArray](<ReadSignedIntegerArray.htm>), [ReadLongIntegerArray](<ReadLongIntegerArray.htm>), [ReadSignedLongIntegerArray](<ReadSignedLongIntegerArray.htm>), [ReadStringArray](<ReadStringArray.htm>).

NOTE: Input and Output variables of any kind are not allowed in the file reading and writing functions, just internal variables.  
There is no error if the structure does not match the data.

Parameters:

nFileHandle - File handle of the previously opened file (from [FileOpen](<FileOpen.htm>)).

struct - Structure variable that will receive data read from file

nTotalBytesRead - optional argument. INTEGER variable that will contain the

total number of bytes read from the file into the structure.

Return Value:

NONE

Example:

(see [File Functions Overview](<File_Functions_Overview.htm>))

SIGNED_INTEGER nFileHandle, nTotalBytesRead;

STRUCTURE PhoneBookEntry

{

STRING Name[50];

STRING Address[100];

STRING PhoneNumber[20];

};

PhoneBookEntry OneEntry;

StartFileOperations();

nFileHandle = FileOpen ( "\\\CF0\\\MyFile.txt", _O_RDONLY );

if (nFileHandle >= 0)

{

ReadStructure( nFileHandle, OneEntry, nTotalBytesRead );

if( nTotalBytesRead < 0 )

PRINT ( "Error reading structure. Error code = %d\n", nTotalBytesRead );

else

PRINT ( "Read structure from file correctly. Total bytes read = %d\n", nTotalBytesRead );

}

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/Read_Structure.htm*
